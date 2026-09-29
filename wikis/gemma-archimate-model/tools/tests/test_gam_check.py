"""tools/check_elementen.py: een correcte wiki geeft geen fouten; elke ingebrachte fout wordt gevonden."""
import pytest
from gam_hulp import KENMERKEN_BO, element_tekst

import check_elementen

BO_PAD = "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md"
PROCES_PAD = "bedrijfsarchitectuur/bedrijfsprocessen/8-wonen/vergunningen/aanvraag-behandelen.md"


def _bo(**over):
    meta = {"id": "beschikking", "type": "bedrijfsobject", "status": "review", "naam": "Beschikking",
            "archimate_type": "business-object", "onderwerp": "vergunningen", "taakveld": "8 Wonen",
            "beleidsdomein": "Vergunningen", "bronnen": ["2026-utrecht-nota"],
            "definitie": "Schriftelijk besluit over een individueel geval.", "grondslag": "bron",
            "data_object": "nee", "kenmerken": dict(KENMERKEN_BO)}
    meta.update(over)
    return {k: v for k, v in meta.items() if v is not None}


def _schrijf(wiki, pad, meta, body="# x\n"):
    doel = wiki / pad
    doel.parent.mkdir(parents=True, exist_ok=True)
    doel.write_text(element_tekst(meta, body), encoding="utf-8")


@pytest.fixture
def wiki(archimate_repo):
    root, wiki = archimate_repo
    _schrijf(wiki, "begrippen/vergunningen.md",
             {"id": "vergunningen", "type": "onderwerp", "naam": "Vergunningen", "status": "in-behandeling",
              "bronnen": ["2026-utrecht-nota"]},
             "## Begrippen\n\n| Begrip | Uitkomst | Reden |\n|---|---|---|\n"
             f"| [Beschikking](../{BO_PAD}) | bedrijfsobject | passief |\n"
             f"| [Aanvraag behandelen](../{PROCES_PAD}) | bedrijfsproces | gedrag |\n")
    _schrijf(wiki, "bronanalyses/vergunningen/2026-utrecht-nota.md",
             {"id": "2026-utrecht-nota", "type": "bronanalyse", "onderwerp": "vergunningen",
              "bronnen": ["2026-utrecht-nota"], "relevant": "ja"})
    _schrijf(wiki, BO_PAD, _bo())
    proces_kenmerken = {k: "nee" for k in KENMERKEN_BO} | {"herkenbaar": "ja", "gemeentelijk": "ja", "gedrag": "ja", "per_keer_doorlopen": "ja"}
    _schrijf(wiki, PROCES_PAD, _bo(id="aanvraag-behandelen", type="bedrijfsproces", naam="Aanvraag behandelen",
                                   archimate_type="business-process", kenmerken=proces_kenmerken,
                                   definitie="Het behandelen van een aanvraag tot een besluit."),
             "## Relaties\n\n| Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie | Bron |\n|---|---|---|---|---|---|---|\n"
             "| toegang (schrijven) | [Beschikking](beschikking.md) | maakt | | bron | | 2026-utrecht-nota (§2) |\n".replace(
                 "beschikking.md", "../../../bedrijfsobjecten/8-wonen/vergunningen/beschikking.md"))
    return wiki


def _fouten(wiki):
    return [(x.naam, x.melding) for x in check_elementen.controleer(wiki) if x.ernst == "fout"]


def test_correcte_wiki_heeft_geen_fouten(wiki):
    assert _fouten(wiki) == []


def test_verkeerde_map(wiki):
    _schrijf(wiki, BO_PAD, _bo(beleidsdomein="Anders"))
    assert any(n == "plaats" for n, _ in _fouten(wiki))


def test_review_zonder_levenscyclus_mag_niet(wiki):
    _schrijf(wiki, BO_PAD, _bo(kenmerken=KENMERKEN_BO | {"levenscyclus": "nee"}))
    assert any(n == "status" for n, _ in _fouten(wiki))


def test_kenmerken_passen_niet_bij_type(wiki):
    _schrijf(wiki, BO_PAD, _bo(kenmerken=KENMERKEN_BO | {"afspraak": "ja"}))
    assert any(n == "kenmerken-type" for n, _ in _fouten(wiki))


def test_kandidaat_zonder_ter_discussie(wiki):
    _schrijf(wiki, BO_PAD, _bo(status="kandidaat"))
    assert any(n == "ter-discussie" for n, _ in _fouten(wiki))


def test_formele_definitie_uit_beleid_en_zonder_uitleg(wiki):
    _schrijf(wiki, BO_PAD, _bo(definitie_formeel="Een besluit dat niet van algemene strekking is.",
                               definitie_formeel_bron={"bron": "2026-utrecht-nota", "plaats": "p. 3"}))
    meldingen = [m for n, m in _fouten(wiki) if n == "definitie-formeel"]
    assert any("brontype 'beleid'" in m for m in meldingen)
    assert any("## Definitie" in m for m in meldingen)


def test_bron_zonder_bronanalyse_en_element_niet_in_begrippenlijst(wiki):
    _schrijf(wiki, BO_PAD, _bo(bronnen=["2026-overheid-gemeentewet"]))
    (wiki / "begrippen/vergunningen.md").write_text(
        (wiki / "begrippen/vergunningen.md").read_text(encoding="utf-8").replace(f"[Beschikking](../{BO_PAD})", "Beschikking"),
        encoding="utf-8")
    meldingen = [m for n, m in _fouten(wiki) if n == "herleidbaarheid"]
    assert any("geen bronanalyse" in m for m in meldingen)
    assert any("geen enkele begrippenlijst" in m for m in meldingen)


def test_ongeldige_archimate_relatie_en_technische_link(wiki):
    body = ("## Relaties\n\n| Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie | Bron |\n|---|---|---|---|---|---|---|\n"
            "| compositie | [Aanvraag behandelen](../../../bedrijfsprocessen/8-wonen/vergunningen/aanvraag-behandelen.md) | | | bron | | 2026-utrecht-nota |\n"
            "\nZie [regels](../../../../AGENTS.md).\n")
    _schrijf(wiki, BO_PAD, _bo(), body)
    namen = [n for n, _ in _fouten(wiki)]
    assert "relatie-archimate" in namen and "technische-verwijzing" in namen


def test_verwijzing_in_frontmatter(wiki):
    _schrijf(wiki, BO_PAD, _bo(toelichting="Zie [Besluit](besluit.md)."))
    assert any(n == "frontmatter-links" for n, _ in _fouten(wiki))


def test_registratietaal_is_waarschuwing(wiki):
    _schrijf(wiki, BO_PAD, _bo(), "Wordt geregistreerd in het zaaksysteem, dus een bedrijfsobject.\n")
    bevindingen = check_elementen.controleer(wiki)
    assert any(x.naam == "anti-patroon" and x.ernst == "waarschuwing" for x in bevindingen)


def test_rapport_wordt_aangevuld(wiki, tmp_path):
    import json

    rapport = tmp_path / "validation-report.json"
    rapport.write_text(json.dumps({"run": "r1", "controles": [{"naam": "page", "resultaat": "ok", "ernst": "info"}]}))
    _schrijf(wiki, BO_PAD, _bo(status="kandidaat"))
    check_elementen.naar_rapport(check_elementen.controleer(wiki), rapport, "r1")
    data = json.loads(rapport.read_text())
    assert data["controles"][0]["naam"] == "page"
    assert any(c["naam"] == "gemma-archimate-model:ter-discussie" and c["ernst"] == "fout" for c in data["controles"])


def test_relatiebron_zonder_bronanalyse(wiki):
    pad = wiki / PROCES_PAD
    pad.write_text(pad.read_text(encoding="utf-8").replace("2026-utrecht-nota (§2)", "2026-overheid-gemeentewet (art. 1)"), encoding="utf-8")
    assert any(n == "relatie-bron" for n, _ in _fouten(wiki))


def test_relatietabel_in_bronanalyse_heeft_vaste_kolommen(wiki):
    pad = wiki / "bronanalyses/vergunningen/2026-utrecht-nota.md"
    pad.write_text(pad.read_text(encoding="utf-8") + "\n## Relaties\n\n| Van | Naar |\n|---|---|\n| A | B |\n", encoding="utf-8")
    assert any(n == "bronanalyse" and "relatietabel" in m for n, m in _fouten(wiki))
