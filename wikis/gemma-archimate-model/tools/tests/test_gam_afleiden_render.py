"""tools/afleiden.py en tools/render.py: van beoordeling naar status en pagina's."""
import pytest
from test_gam_bepaal_type import BO, PROCES

import afleiden
import bepaal_type as bt
import render
from llmwiki import beoordeling, logbook

WET = "2026-overheid-gemeentewet"


@pytest.fixture
def wiki(archimate_repo):
    root, wiki = archimate_repo
    bronnen = [WET, "2026-vng-ggm", "2026-utrecht-nota"]
    for bron_id in bronnen:
        pad = wiki / "bronanalyses" / "test" / f"{bron_id}.md"
        pad.parent.mkdir(parents=True, exist_ok=True)
        pad.write_text(f"---\nid: {bron_id}\ntype: bronanalyse\nonderwerp: test\nbronnen: [{bron_id}]\n---\n\n# {bron_id}\n\n"
                       f"Bron: [tekst](../../../../sources/raw/{bron_id}.md)\n", encoding="utf-8")
    beoordeling.schrijf(wiki / "beoordelingen/onderwerpen/test.yaml",
                        {"naam": "Test", "status": "in-behandeling", "omschrijving": ["Een onderwerp."], "bronnen": bronnen})
    (wiki / "beoordelingen/begrippen").mkdir(parents=True)
    return wiki


def _element(begrip: str, ja: set[str], **extra) -> dict:
    return {
        "begrip": begrip,
        "onderwerpen": ["test"],
        "kenmerken": {s: {"waarde": "ja", "onderbouwing": "Volgt uit de wet (art. 1).", "bronnen": [WET]} if s in ja
                      else {"waarde": "nee", "onderbouwing": "Niet van toepassing."} for s in bt.SLEUTELS},
        "definitie": f"Definitie van {begrip.lower()}.",
        "beschrijving": [f"{begrip} volgens {WET}."],
        "taakveld": "8 Wonen",
        "beleidsdomein": "Vergunningen",
        "grondslag": "bron",
        "gemma": {"sterkte": "geen", "onderbouwing": "Niet in GEMMA."},
        **extra,
    }


def _bo(**extra) -> dict:
    return _element("Beschikking", BO, ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}, **extra)


def _proces(**extra) -> dict:
    relatie = {"soort": "toegang (registreren)", "naar": "beschikking", "naam": "stelt vast", "grondslag": "bron",
               "bronnen": [WET], "vindplaats": "art. 2"}
    return _element("Behandelen aanvraag", PROCES, relaties=[relatie], **extra)


def _schrijf(wiki, bid, data):
    beoordeling.schrijf(wiki / f"beoordelingen/begrippen/{bid}.yaml", data)


def _lees(wiki, bid):
    return beoordeling.laad(wiki / f"beoordelingen/begrippen/{bid}.yaml")


def _afleiden(wiki):
    res = afleiden.afleiden(wiki)
    assert res.fouten == []
    assert render.main(["--wiki", str(wiki)]) == 0
    return res


def test_beoordelingen_worden_paginas_met_relaties_in_beide_richtingen(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    _afleiden(wiki)

    bo, proces = _lees(wiki, "beschikking"), _lees(wiki, "behandelen-aanvraag")
    assert (bo["status"], proces["status"]) == ("review", "review")
    assert bo["afgeleid"]["pad"] == "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md"
    assert bo["afgeleid"]["herkomst"] == "wet"

    pagina = (wiki / bo["afgeleid"]["pad"]).read_text(encoding="utf-8")
    assert "## Inkomende relaties" in pagina
    assert "[Behandelen aanvraag](../../../bedrijfsprocessen/8-wonen/vergunningen/behandelen-aanvraag.md)" in pagina
    assert f"[{WET}](../../../../bronanalyses/test/{WET}.md)" in pagina
    assert "**Status: review.**" in pagina
    lijst = (wiki / "begrippen/test.md").read_text(encoding="utf-8")
    assert "[Beschikking](../bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md)" in lijst
    assert "Behandelen aanvraag" in (wiki / "ter-beoordeling.md").read_text(encoding="utf-8")


def test_afleiden_en_render_zijn_idempotent_en_check_vangt_handwerk(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _afleiden(wiki)
    assert afleiden.afleiden(wiki).gewijzigd == []
    assert render.main(["--wiki", str(wiki), "--check"]) == 0

    pagina = wiki / _lees(wiki, "beschikking")["afgeleid"]["pad"]
    pagina.write_text(pagina.read_text(encoding="utf-8") + "\nHandmatig.\n", encoding="utf-8")
    assert render.main(["--wiki", str(wiki), "--check"]) == 1
    (wiki / "bedrijfsarchitectuur/rollen").mkdir(parents=True)
    (wiki / "bedrijfsarchitectuur/rollen/los.md").write_text("# Los\n", encoding="utf-8")
    assert render.main(["--wiki", str(wiki)]) == 0
    assert not (wiki / "bedrijfsarchitectuur/rollen/los.md").exists()
    assert render.main(["--wiki", str(wiki), "--check"]) == 0


def test_regelgeving_blijft_kandidaat_tot_de_redacteur_beslist(wiki):
    _schrijf(wiki, "beschikking", _bo(grondslag="regelgeving", grondslag_toelichting=["Gemeentewet art. 147."]))
    _afleiden(wiki)
    data = _lees(wiki, "beschikking")
    assert data["status"] == "kandidaat"
    assert data["afgeleid"]["open"] == [bt.REDEN_REGELGEVING]
    assert "## Ter discussie" in (wiki / data["afgeleid"]["pad"]).read_text(encoding="utf-8")

    data["besluiten"] = [{"datum": "2026-10-01", "besluit": "Opnemen.", "gevolg": "opnemen",
                          "redenen": [bt.REDEN_REGELGEVING]}]
    _schrijf(wiki, "beschikking", data)
    _afleiden(wiki)
    assert _lees(wiki, "beschikking")["status"] == "review"

    data = _lees(wiki, "beschikking")
    data["besluiten"].append({"datum": "2026-10-02", "besluit": "Toch niet.", "gevolg": "afwijzen"})
    _schrijf(wiki, "beschikking", data)
    _afleiden(wiki)
    data = _lees(wiki, "beschikking")
    assert data["status"] == "afgewezen" and "pad" not in data["afgeleid"]
    assert not (wiki / "bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md").exists()


def test_goedgekeurd_blijft_tot_de_inhoud_wijzigt(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _afleiden(wiki)
    data = _lees(wiki, "beschikking")
    data["status"] = "goedgekeurd"
    _schrijf(wiki, "beschikking", data)
    logbook.append_log(wiki, "promote", "beschikking", "Redacteur", beoordeling.inhoud_hash(data))
    _afleiden(wiki)
    assert _lees(wiki, "beschikking")["status"] == "goedgekeurd"

    data = _lees(wiki, "beschikking")
    data["definitie"] = "Een andere definitie."
    _schrijf(wiki, "beschikking", data)
    _afleiden(wiki)
    assert _lees(wiki, "beschikking")["status"] == "review"


def test_goedgekeurd_zonder_logregel_wordt_review(wiki):
    _schrijf(wiki, "beschikking", {**_bo(), "status": "goedgekeurd"})
    _afleiden(wiki)
    assert _lees(wiki, "beschikking")["status"] == "review"


@pytest.mark.parametrize("wijziging, melding", [
    (lambda d: d["relaties"][0].update(naar="onbekend"), "geen element"),
    (lambda d: d["relaties"][0].update(soort="toegang (houder)"), "toegang 'houder'"),
    (lambda d: d["kenmerken"]["gedrag"].update(bronnen=["2026-onbekende-bron"]), "staat niet in sources/index"),
    (lambda d: d.pop("definitie"), "zonder 'definitie'"),
    (lambda d: d.update(onderwerpen=["ander"]), "onderwerp 'ander'"),
    (lambda d: d.update(onverwacht="x"), "onverwacht"),
])
def test_harde_fouten_schrijven_niets(wiki, wijziging, melding):
    _schrijf(wiki, "beschikking", _bo())
    proces = _proces()
    wijziging(proces)
    _schrijf(wiki, "behandelen-aanvraag", proces)
    res = afleiden.afleiden(wiki)
    assert any(melding in f for f in res.fouten), res.fouten
    assert "status" not in _lees(wiki, "beschikking")


def test_nieuwe_terugmelding_krijgt_het_volgende_nummer(wiki):
    _schrijf(wiki, "beschikking", _bo())
    register = {"terugmeldingen": [
        {"nummer": 1, "domein": "Vergunningen", "type": "hiaat", "bevinding": "Ontbreekt.", "element": "beschikking", "status": "open"},
        {"domein": "Vergunningen", "type": "definitie", "bevinding": "Te smal.", "element": "beschikking"}]}
    beoordeling.schrijf(wiki / afleiden.TERUGMELDINGEN, register)
    _afleiden(wiki)
    meldingen = beoordeling.laad(wiki / afleiden.TERUGMELDINGEN)["terugmeldingen"]
    assert [(m["nummer"], m["status"]) for m in meldingen] == [(1, "open"), (2, "open")]
    pagina = (wiki / _lees(wiki, "beschikking")["afgeleid"]["pad"]).read_text(encoding="utf-8")
    assert "[Nummer 2](../../../../analyses/ggm-terugmeldingen.md)" in pagina


def test_signalen_noemen_de_regel_bij_naam(wiki):
    _schrijf(wiki, "beschikking", _bo(beschrijving=["Wordt geregistreerd in het zaaksysteem."]))
    _schrijf(wiki, "aanvraag-behandeling", _element("Aanvraagbehandeling", PROCES))
    res = afleiden.afleiden(wiki)
    assert res.fouten == []
    assert any("regel Naamvorm" in w and "aanvraag-behandeling" in w for w in res.waarschuwingen)
    assert any("regel Beslistabel beslist" in w and "geregistreerd" in w for w in res.waarschuwingen)


def test_bronanalyse_zonder_bronregel_is_een_fout(wiki):
    pad = wiki / "bronanalyses" / "test" / f"{WET}.md"
    pad.write_text(pad.read_text(encoding="utf-8").replace("Bron: ", "Zie: "), encoding="utf-8")
    _schrijf(wiki, "beschikking", _bo())
    assert any("'Bron:'" in f for f in afleiden.afleiden(wiki).fouten)
