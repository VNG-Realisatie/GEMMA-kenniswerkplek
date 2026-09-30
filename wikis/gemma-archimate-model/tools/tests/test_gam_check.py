"""tools/check_elementen.py: een correcte wiki geeft geen fouten; elke ingebrachte fout wordt gevonden."""
import re

import pytest
from gam_hulp import KENMERKEN_BO, element_tekst

import check_elementen
import gam_gemeen

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


def _schrijf(wiki, pad, meta, body="# x\n", definitie_bovenaan=True, bronlinks=True):
    """Schrijf een pagina; een elementpagina krijgt `## Bronnen` en bron-id's als link, zoals de regel voorschrijft."""
    doel = wiki / pad
    doel.parent.mkdir(parents=True, exist_ok=True)
    if bronlinks and meta.get("archimate_type"):
        if "## Bronnen" not in body:
            body = body.rstrip("\n") + "\n\n## Bronnen\n\n" + "".join(f"- {b}\n" for b in meta.get("bronnen", []))
        body = gam_gemeen.bronnen_als_link(doel, body, wiki)
    doel.write_text(element_tekst(meta, body, definitie_bovenaan), encoding="utf-8")


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
              "bronnen": ["2026-utrecht-nota"], "relevant": "ja"},
             "# Nota\n\nBron: [tekst](../../../../sources/raw/2026-utrecht-nota.md)\n")
    _schrijf(wiki, BO_PAD, _bo())
    proces_kenmerken = {k: "nee" for k in KENMERKEN_BO} | {
        k: "ja" for k in ("herkenbaar", "gemeentelijk", "eigen_identiteit", "betekenis_in_onderwerp", "relaties",
                          "zelfstandig_beleidsbegrip", "gedrag", "per_keer_doorlopen", "toegewezen_partij",
                          "gebruikt_objecten", "aanleiding", "benoembaar_resultaat", "herhaald_uitgevoerd",
                          "eigen_normering")}
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


def test_review_bij_governance_object_mag_niet(wiki):
    _schrijf(wiki, BO_PAD, _bo(grondslag="governance-object"))
    assert any(n == "status" for n, _ in _fouten(wiki))


def test_een_criterium_nee_mag_review(wiki):
    _schrijf(wiki, BO_PAD, _bo(kenmerken=KENMERKEN_BO | {"levenscyclus": "nee"}))
    assert _fouten(wiki) == []


def test_onder_de_drempel_geen_element(wiki):
    _schrijf(wiki, BO_PAD, _bo(kenmerken=KENMERKEN_BO | {"levenscyclus": "nee", "relaties": "nee"}))
    assert any(n == "kenmerken-type" for n, _ in _fouten(wiki))


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


def test_definitie_niet_bovenaan(wiki):
    _schrijf(wiki, BO_PAD, _bo(), "# x\n\n## Beschrijving\n\nTekst.\n\n## Definitie\n\nSchriftelijk besluit over een individueel geval.\n",
             definitie_bovenaan=False)
    assert any(n == "definitie-bovenaan" and "eerste sectie" in m for n, m in _fouten(wiki))


def test_definitie_bovenaan_wijkt_af_van_frontmatter(wiki):
    _schrijf(wiki, BO_PAD, _bo(), "# x\n\n## Definitie\n\nIets anders.\n", definitie_bovenaan=False)
    assert any(n == "definitie-bovenaan" and "niet letterlijk" in m for n, m in _fouten(wiki))


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
    tekst = re.sub(r"\[2026-utrecht-nota\]\([^)]*\) \(§2\)", "2026-overheid-gemeentewet (art. 1)", pad.read_text(encoding="utf-8"))
    pad.write_text(tekst, encoding="utf-8")
    fouten = _fouten(wiki)
    assert any(n == "relatie-bron" for n, _ in fouten)
    assert ("bron-link", "'## Relaties': bron '2026-overheid-gemeentewet' heeft geen bronanalyse") in fouten


def test_relatietabel_in_bronanalyse_heeft_vaste_kolommen(wiki):
    pad = wiki / "bronanalyses/vergunningen/2026-utrecht-nota.md"
    pad.write_text(pad.read_text(encoding="utf-8") + "\n## Relaties\n\n| Van | Naar |\n|---|---|\n| A | B |\n", encoding="utf-8")
    assert any(n == "bronanalyse" and "relatietabel" in m for n, m in _fouten(wiki))


def test_gangbare_term_als_synoniem_geeft_waarschuwing(wiki):
    _schrijf(wiki, BO_PAD, _bo(synoniemen=[{"naam": "Besluit", "context": "dagelijks gebruik"}]))
    assert any(x.naam == "naam-wetsterm" for x in check_elementen.controleer(wiki))
    _schrijf(wiki, BO_PAD, _bo(synoniemen=[{"naam": "Besluit", "context": "dagelijks gebruik"},
                                           {"naam": "Beschikking (Awb)", "context": "wet"}]))
    assert not any(x.naam == "naam-wetsterm" for x in check_elementen.controleer(wiki))


def test_bron_als_tekst_in_tabel_is_fout(wiki):
    body = ("## Kenmerken\n\n| Kenmerk | Waarde | Onderbouwing | Bron |\n|---|---|---|---|\n"
            "| herkenbaar | ja | Gangbaar. | 2026-utrecht-nota |\n")
    _schrijf(wiki, BO_PAD, _bo(), body, bronlinks=False)
    fouten = _fouten(wiki)
    assert ("bron-link", "'## Kenmerken': bron '2026-utrecht-nota' staat er als tekst; maak er een link naar de bronanalyse van") in fouten
    assert ("bron-link", "'## Bronnen' linkt niet naar de bronanalyse van '2026-utrecht-nota'") in fouten


def test_bronlink_naar_verkeerd_doel_is_fout(wiki):
    body = ("## Kenmerken\n\n| Kenmerk | Waarde | Onderbouwing | Bron |\n|---|---|---|---|\n"
            "| herkenbaar | ja | Gangbaar. | [2026-utrecht-nota](../../../../../../sources/index/2026-utrecht-nota.md) |\n")
    _schrijf(wiki, BO_PAD, _bo(), body)
    assert any(n == "bron-link" and "wijst niet naar de bronanalyse" in m for n, m in _fouten(wiki))


def test_bronanalyse_zonder_bronregel(wiki):
    pad = wiki / "bronanalyses/vergunningen/2026-utrecht-nota.md"
    pad.write_text(pad.read_text(encoding="utf-8").replace("Bron: [tekst]", "Zie [tekst]"), encoding="utf-8")
    assert any(n == "bronregel" for n, _ in _fouten(wiki))


def test_bronnen_als_link_laat_links_en_datums_staan(wiki):
    van = wiki / BO_PAD
    tekst = "Zie 2026-utrecht-nota (§2), [2026-utrecht-nota](x.md) en besluit van 2026-09-30."
    assert gam_gemeen.bronnen_als_link(van, tekst, wiki) == (
        "Zie [2026-utrecht-nota](../../../../bronanalyses/vergunningen/2026-utrecht-nota.md) (§2), "
        "[2026-utrecht-nota](x.md) en besluit van 2026-09-30.")


def test_onderwerpgebonden_beschrijving_is_waarschuwing(wiki):
    _schrijf(wiki, BO_PAD, _bo(), "## Beschrijving\n\nIn dit onderwerp wordt de beschikking door het college genomen.\n")
    bevindingen = check_elementen.controleer(wiki)
    assert any(x.naam == "beschrijving-onderwerp" and x.ernst == "waarschuwing" for x in bevindingen)
    # Onder '## Per onderwerp' mag het wel
    _schrijf(wiki, BO_PAD, _bo(), "## Beschrijving\n\nBesluit over een individueel geval.\n\n"
             "## Per onderwerp\n\n### Vergunningen\n\nIn dit onderwerp neemt het college de beschikking.\n")
    assert not any(x.naam == "beschrijving-onderwerp" for x in check_elementen.controleer(wiki))
