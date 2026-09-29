"""Eén onderwerp door de hele keten: run start --onderwerp → INGEST → ASSESS (beslistabel) → WRITE (element op
review, element op kandidaat, begrippenlijst, relatie, terugmelding) → VALIDATE (core + check_elementen) →
promotievoorstel → akkoord → alleen de review-pagina wordt goedgekeurd."""
import json

from gam_hulp import element_tekst

import bepaal_type
import check_elementen
import terugmelding
from llmwiki import frontmatter, gate, lint, paths, runs, validate

JA = {"herkenbaar", "gemeentelijk", "eigen_identiteit", "betekenis_in_onderwerp", "relaties", "zelfstandig_beleidsbegrip"}


def _beoordeling(begrip, ja):
    return {"begrip": begrip, "onderwerp": "vergunningen",
            "kenmerken": {s: {"waarde": "ja" if s in ja else "nee", "onderbouwing": "uit de bron", "bronnen": ["2026-utrecht-nota"]}
                          for s in bepaal_type.SLEUTELS}}


def _json(pad, data):
    pad.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return pad


def test_onderwerp_door_de_hele_keten(archimate_repo, tmp_path):
    root, wiki = archimate_repo
    wiki_yaml = paths.load_wiki_yaml(wiki)

    # Onderwerp en bronanalyse bestaan (INGEST schrijft de bronanalyse direct, zoals wiki-ingest)
    (wiki / "begrippen").mkdir()
    (wiki / "begrippen/vergunningen.md").write_text(element_tekst(
        {"id": "vergunningen", "type": "onderwerp", "naam": "Vergunningen", "status": "in-behandeling",
         "bronnen": ["2026-utrecht-nota", "2026-overheid-gemeentewet"]},
        "## Begrippen\n\n| Begrip | Uitkomst | Reden | Herkomst | GGM |\n|---|---|---|---|---|\n"), encoding="utf-8")
    for bron in ("2026-utrecht-nota", "2026-overheid-gemeentewet"):
        pad = wiki / f"bronanalyses/vergunningen/{bron}.md"
        pad.parent.mkdir(parents=True, exist_ok=True)
        pad.write_text(element_tekst({"id": bron, "type": "bronanalyse", "onderwerp": "vergunningen",
                                      "bronnen": [bron], "relevant": "ja"}), encoding="utf-8")

    state = runs.start(wiki, wiki_yaml, "gemma-archimate-model-update", onderwerp="vergunningen")
    run_id, rdir = state["run_id"], runs.run_dir(wiki, state["run_id"])
    assert state["bronnen"] == ["2026-overheid-gemeentewet", "2026-utrecht-nota"]  # bronvoorrang: wet vóór beleid
    runs.complete(wiki, wiki_yaml, run_id, "ingest", _json(tmp_path / "s.json", {"run": run_id, "bronnen": [{"id": b} for b in state["bronnen"]]}))

    # ASSESS: kenmerken → beslistabel
    bo_ja = JA | {"onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"}
    proces_ja = JA | {"gedrag", "per_keer_doorlopen"}
    zonder_levenscyclus = bo_ja - {"levenscyclus"}
    assessment = {"run": run_id, "voorstellen": [
        {"doel": "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md", "soort": "nieuw",
         "motivering": "kernbegrip", "bronnen": ["2026-utrecht-nota"], "beoordeling": _beoordeling("Beschikking", bo_ja)},
        {"doel": "bedrijfsarchitectuur/bedrijfsprocessen/8-wonen/vergunningen/aanvraag-behandelen.md", "soort": "nieuw",
         "motivering": "proces", "bronnen": ["2026-utrecht-nota"], "beoordeling": _beoordeling("Aanvraag behandelen", proces_ja)},
        {"doel": "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/leges.md", "soort": "nieuw",
         "motivering": "twijfel", "bronnen": ["2026-utrecht-nota"], "beoordeling": _beoordeling("Leges", zonder_levenscyclus)},
    ]}
    pad_assessment = _json(tmp_path / "assessment.json", assessment)
    assert bepaal_type.main(["evalueer", str(pad_assessment), "--schrijf"]) == 0
    uitkomsten = [v["beoordeling"]["uitkomst"] for v in json.loads(pad_assessment.read_text())["voorstellen"]]
    assert [u["paginatype"] for u in uitkomsten] == ["bedrijfsobject", "bedrijfsproces", "bedrijfsobject"]
    assert not uitkomsten[2]["voorleggen"] and "levenscyclus" in uitkomsten[2]["toelichting"]  # 6/7: binnen de drempel
    runs.complete(wiki, wiki_yaml, run_id, "assess", pad_assessment)

    # WRITE: pagina's stagen
    def kenmerken(ja):
        return {s: "ja" if s in ja else "nee" for s in bepaal_type.SLEUTELS}

    def element(id_, naam, type_, archimate, ja, status, body):
        meta = {"id": id_, "type": type_, "status": status, "naam": naam, "archimate_type": archimate,
                "onderwerp": "vergunningen", "taakveld": "8 Wonen", "beleidsdomein": "Vergunningen",
                "bronnen": ["2026-utrecht-nota"], "definitie": f"{naam} zoals de gemeente die kent.",
                "grondslag": "bron" if type_ != "bedrijfsobject" else "procesobject",
                "data_object": "nee", "kenmerken": kenmerken(ja)}
        return element_tekst(meta, body)

    bronnen = "## Bronnen\n\n- [Nota](../../../../bronanalyses/vergunningen/2026-utrecht-nota.md)\n"
    staged = {
        "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md":
            ("bedrijfsobject", element("beschikking", "Beschikking", "bedrijfsobject", "business-object", bo_ja, "review", bronnen)),
        "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/leges.md":
            ("bedrijfsobject", element("leges", "Leges", "bedrijfsobject", "business-object", zonder_levenscyclus, "kandidaat",
                                       bronnen + "\n## Ter discussie\n\nLevenscyclus: nee (6/7). Is dit een zelfstandig ding?\n")),
        "bedrijfsarchitectuur/bedrijfsprocessen/8-wonen/vergunningen/aanvraag-behandelen.md":
            ("bedrijfsproces", element("aanvraag-behandelen", "Aanvraag behandelen", "bedrijfsproces", "business-process", proces_ja, "review",
                                       bronnen + "\n## Relaties\n\n| Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie | Bron |\n"
                                       "|---|---|---|---|---|---|---|\n| toegang (schrijven) | "
                                       "[Beschikking](../../../bedrijfsobjecten/8-wonen/vergunningen/beschikking.md) | maakt | | bron | | 2026-utrecht-nota (§2) |\n")),
        "begrippen/vergunningen.md": ("onderwerp", element_tekst(
            {"id": "vergunningen", "type": "onderwerp", "naam": "Vergunningen", "status": "afgerond",
             "bronnen": ["2026-utrecht-nota", "2026-overheid-gemeentewet"], "conclusie": "Twee elementen, één ter discussie."},
            "## Begrippen\n\n| Begrip | Uitkomst | Reden | Herkomst | GGM |\n|---|---|---|---|---|\n"
            "| [Beschikking](../bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md) | bedrijfsobject | passief | beleid | nee |\n"
            "| [Leges](../bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/leges.md) | bedrijfsobject (voorleggen) | geen levenscyclus | beleid | nee |\n"
            "| [Aanvraag behandelen](../bedrijfsarchitectuur/bedrijfsprocessen/8-wonen/vergunningen/aanvraag-behandelen.md) | bedrijfsproces | gedrag | beleid | nee |\n")),
    }
    concept = {"run": run_id, "paginas": []}
    for i, (pad, (type_, tekst)) in enumerate(staged.items()):
        (rdir / "changeset" / f"p{i}.md").write_text(tekst, encoding="utf-8")
        concept["paginas"].append({"pad": pad, "staged_bestand": f"p{i}.md", "actie": "wijzigen" if (wiki / pad).exists() else "nieuw", "type": type_})
    _json(rdir / "changeset-concept.json", concept)
    terugmelding.voeg_toe(wiki, run_id, "hiaat", "Vergunningen", "—", "Beschikking ontbreekt als gegevensobject", "beschikking")
    runs.complete(wiki, wiki_yaml, run_id, "write", rdir / "changeset-concept.json")

    # VALIDATE: core per pagina (met changeset-context) + domeincontroles
    controles = []
    for p in json.loads((rdir / "changeset.json").read_text())["paginas"]:
        doelpad, bestaande = validate.changeset_context(wiki, rdir, rdir / "changeset" / p["staged_bestand"])
        fouten = validate.validate_page(wiki, rdir / "changeset" / p["staged_bestand"], wiki_yaml, doelpad=doelpad, bestaande_paden=bestaande)
        assert fouten == [], fouten
        controles.append({"naam": "page", "doel": p["pad"], "resultaat": "ok", "ernst": "info"})
    rapport = _json(tmp_path / "validation-report.json", {"run": run_id, "controles": controles})
    bevindingen = check_elementen.controleer(wiki, run_id)
    assert [x for x in bevindingen if x.ernst == "fout"] == []
    check_elementen.naar_rapport(bevindingen, rapport, run_id)
    runs.complete(wiki, wiki_yaml, run_id, "validate", rapport)

    # GATE + PROMOTE (smaak A: de redacteur zet zelf akkoord in het voorstel)
    voorstel = gate.plan(wiki, wiki_yaml, run_id)
    tekst = voorstel.read_text(encoding="utf-8")
    assert "beschikking.md" in tekst.split("Wordt geschreven zonder goedkeuring")[0]
    page = frontmatter.read(voorstel)
    page.meta.update(akkoord_voor_publicatie="ja", beoordeeld_door="Redacteur")
    frontmatter.write(voorstel, page)
    gate.apply(wiki, wiki_yaml, run_id)

    status = {p: frontmatter.read(wiki / p).meta.get("status") for p in staged if p.startswith("bedrijfsarchitectuur")}
    assert status == {
        "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md": "goedgekeurd",
        "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/leges.md": "kandidaat",
        "bedrijfsarchitectuur/bedrijfsprocessen/8-wonen/vergunningen/aanvraag-behandelen.md": "goedgekeurd",
    }
    assert terugmelding.rijen(frontmatter.read(wiki / "analyses/ggm-terugmeldingen.md"))[0]["Type"] == "hiaat"
    assert lint.check_goedgekeurd_guard(root) == []
    assert [x for x in check_elementen.controleer(wiki) if x.ernst == "fout"] == []
