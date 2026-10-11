"""tools/beslissen.py en tools/render.py: van beoordeling naar status en pagina's."""
import pytest
from test_gam_bepaal_type import (ACTOR, BELEIDSKADER, BO, DIENST, FUNCTIE, GEBEURTENIS, KANAAL, PROCES, PRODUCT, ROL,
                                  SAMENWERKING)

import beslissen
import bepaal_type as bt
import render
from llmwiki import beoordeling, logbook, modellen

WET = "2026-overheid-gemeentewet"


BRONTYPE = {WET: "rijksregelgeving", "2026-vng-ggm": "informatiemodel", "2026-utrecht-nota": "beleid"}


@pytest.fixture
def wiki(archimate_repo):
    root, wiki = archimate_repo
    bronnen = [WET, "2026-vng-ggm", "2026-utrecht-nota"]
    for bron_id in bronnen:
        pad = wiki / "onderwerpen" / "test" / "bronduidingen" / BRONTYPE[bron_id] / f"{bron_id}.md"
        pad.parent.mkdir(parents=True, exist_ok=True)
        pad.write_text(f"---\nid: {bron_id}\ntype: bronduiding\nonderwerp: test\nbronnen: [{bron_id}]\n---\n\n# {bron_id}\n\n"
                       f"Bron: [tekst](../../../../../../sources/raw/{bron_id}.md)\n", encoding="utf-8")
    beoordeling.schrijf(wiki / "onderwerpen/test/afbakening.yaml",
                        {"naam": "Test", "niveau": "eigen", "status": "in-behandeling", "omschrijving": ["Een onderwerp."], "bronnen": bronnen})
    (wiki / "onderwerpen/test/beoordelingen").mkdir(parents=True)
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
        "gemma": {"sterkte": "geen", "onderbouwing": "Niet in GEMMA."},
        **extra,
    }


def _bo(**extra) -> dict:
    return _element("Beschikking", BO | {"generiek"}, ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}, **extra)


def _proces(**extra) -> dict:
    relatie = {"soort": "toegang (registreren)", "naar": "beschikking", "naam": "stelt vast", "ggm_match": "geen",
               "bronnen": [WET], "vindplaats": "art. 2"}
    return _element("Behandelen aanvraag", PROCES, relaties=[relatie], kernobject="beschikking", afnemer="extern",
                    **extra)


def _schrijf(wiki, bid, data):
    """Schrijf de beoordeling in de map van haar thuisonderwerp (het eerste in `onderwerpen`)."""
    for oud in wiki.glob(f"onderwerpen/*/beoordelingen/{bid}.yaml"):
        oud.unlink()
    beoordeling.schrijf(wiki / f"onderwerpen/{data['onderwerpen'][0]}/beoordelingen/{bid}.yaml", data)


def _lees(wiki, bid):
    return beoordeling.laad(next(wiki.glob(f"onderwerpen/*/beoordelingen/{bid}.yaml")))


def _beslissen(wiki):
    res = beslissen.beslissen(wiki)
    assert res.fouten == []
    assert render.main(["--wiki", str(wiki)]) == 0
    return res


def test_beoordelingen_worden_paginas_met_relaties_in_beide_richtingen(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    _beslissen(wiki)

    bo, proces = _lees(wiki, "beschikking"), _lees(wiki, "behandelen-aanvraag")
    assert (bo["status"], proces["status"]) == ("review", "review")
    assert bo["beslist"]["pad"] == "elementpaginas/bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md"
    assert bo["beslist"]["herkomst"] == "rijksregelgeving"

    pagina = (wiki / bo["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "#### Inkomend" in pagina
    assert "[Behandelen aanvraag](../../../bedrijfsprocessen/8-wonen/vergunningen/behandelen-aanvraag.md)" in pagina
    assert f"[{WET}](../../../../../onderwerpen/test/bronduidingen/rijksregelgeving/{WET}.md)" in pagina
    assert "**Status: review.**" in pagina
    lijst = (wiki / "onderwerpen/test/begrippen.md").read_text(encoding="utf-8")
    assert "[Beschikking](../../elementpaginas/bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md)" in lijst
    assert "Behandelen aanvraag" in (wiki / "ter-beoordeling.md").read_text(encoding="utf-8")


def _rel(soort: str, naar: str) -> dict:
    return {"soort": soort, "naar": naar, "ggm_match": "geen", "bronnen": [WET], "vindplaats": "art. 3"}


def test_elk_paginatype_wordt_afgeleid_en_gerenderd(wiki):
    """Elk paginatype uit de criteria van 2026-10-01, met de relaties zoals de criteria ze voorschrijven."""
    geen_ggm = {"ggm": {"sterkte": "geen", "onderbouwing": "Niet in het GGM."}}
    gevallen = {
        "graf": ("bedrijfsobject", "business-object", _element("Graf", BO, **geen_ggm)),
        "grafrecht": ("bedrijfsobject", "contract", _element("Grafrecht", BO | {"afspraak", "generiek"}, **geen_ggm)),
        "ruimen-graf": ("bedrijfsproces", "business-process", _element("Ruimen graf", PROCES, relaties=[
            _rel("toegang (beëindigen)", "graf"), _rel("realisatie", "onderhoud-van-graven")],
            kernobject="graf", afnemer="extern")),
        "begraafplaatsbeheer": ("bedrijfsfunctie", "business-function", _element("Begraafplaatsbeheer", FUNCTIE,
                                relaties=[_rel("bediening", "ruimen-graf")], domein="Fysieke leefomgeving")),
        "overlijden": ("gebeurtenis", "business-event", _element("Overlijden", GEBEURTENIS,
                       relaties=[_rel("triggering", "ruimen-graf")])),
        "onderhoud-van-graven": ("dienst", "business-service", _element("Onderhoud van graven", DIENST,
                                 domein="Fysieke leefomgeving", afnemer="extern")),
        "grafproduct": ("product", "product", _element("Grafproduct", PRODUCT, relaties=[
            _rel("aggregatie", "onderhoud-van-graven"), _rel("aggregatie", "grafrecht")],
            domein="Fysieke leefomgeving", afnemer="extern", **geen_ggm)),
        "houder-van-de-begraafplaats": ("rol", "business-role", _element("Houder van de begraafplaats", ROL, relaties=[
            _rel("toewijzing", "ruimen-graf"), _rel("toegang (houder)", "graf")], doelgroep="ketenpartners")),
        "kerkgenootschap": ("actor", "business-actor", _element("Kerkgenootschap", ACTOR,
                            relaties=[_rel("toewijzing", "houder-van-de-begraafplaats")], doelgroep="ketenpartners")),
        "zorg-en-veiligheidshuis": ("bedrijfssamenwerking", "business-collaboration", _element(
            "Zorg- en Veiligheidshuis", SAMENWERKING, relaties=[_rel("toewijzing", "ruimen-graf")],
            doelgroep="ketenpartners")),
        "publieksbalie": ("kanaal", "business-interface", _element("Publieksbalie", KANAAL,
                          relaties=[_rel("toewijzing", "onderhoud-van-graven")], doelgroep="inwoners en ondernemers")),
        "wet-op-de-lijkbezorging": ("beleidskader", "driver", _element("Wet op de lijkbezorging", BELEIDSKADER,
                                    relaties=[_rel("associatie (gericht)", "ruimen-graf")], regelgever="rijk")),
    }
    for bid, (_, _, data) in gevallen.items():
        _schrijf(wiki, bid, data)
    _beslissen(wiki)

    for bid, (paginatype, archimate_type, _) in gevallen.items():
        d = _lees(wiki, bid)
        uitkomst = d["beslist"]["uitkomst"]
        assert (uitkomst["soort"], uitkomst["paginatype"], uitkomst["archimate_type"]) == \
            ("element", paginatype, archimate_type), bid
        # Een kanaal wordt altijd voorgelegd (centrale set); de rest is na beslissen klaar voor review.
        assert d["status"] == ("kandidaat" if paginatype == "kanaal" else "review"), (bid, d["beslist"].get("open"))
        assert d["beslist"]["pad"].startswith(beslissen.paths.load_wiki_yaml(wiki)["page_types"][paginatype]["dir"])
        assert (wiki / d["beslist"]["pad"]).exists(), bid
    lijst = (wiki / "onderwerpen/test/begrippen.md").read_text(encoding="utf-8")
    assert all(data["begrip"] in lijst for _, _, data in gevallen.values())


def test_beslissen_en_render_zijn_idempotent_en_check_vangt_handwerk(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _beslissen(wiki)
    assert beslissen.beslissen(wiki).gewijzigd == []
    assert render.main(["--wiki", str(wiki), "--check"]) == 0

    pagina = wiki / _lees(wiki, "beschikking")["beslist"]["pad"]
    pagina.write_text(pagina.read_text(encoding="utf-8") + "\nHandmatig.\n", encoding="utf-8")
    assert render.main(["--wiki", str(wiki), "--check"]) == 1
    (wiki / "elementpaginas/bedrijfsarchitectuur/rollen").mkdir(parents=True)
    (wiki / "elementpaginas/bedrijfsarchitectuur/rollen/los.md").write_text("# Los\n", encoding="utf-8")
    assert render.main(["--wiki", str(wiki)]) == 0
    assert not (wiki / "elementpaginas/bedrijfsarchitectuur/rollen/los.md").exists()
    assert render.main(["--wiki", str(wiki), "--check"]) == 0


def test_gegevensobject_zonder_ggm_blijft_kandidaat_tot_de_redacteur_beslist(wiki):
    _schrijf(wiki, "beschikking", _element("Beschikking", BO | {"generiek", "geautomatiseerd_verwerkt"},
                                           ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}))
    _beslissen(wiki)
    data = _lees(wiki, "beschikking")
    assert data["status"] == "kandidaat"
    assert data["beslist"]["open"] == [bt.REDEN_GEEN_GGM]
    assert "## Ter discussie" in (wiki / data["beslist"]["pad"]).read_text(encoding="utf-8")

    data["besluiten"] = [{"datum": "2026-10-01", "besluit": "Opnemen.", "gevolg": "opnemen",
                          "redenen": [bt.REDEN_GEEN_GGM]}]
    _schrijf(wiki, "beschikking", data)
    _beslissen(wiki)
    assert _lees(wiki, "beschikking")["status"] == "review"

    data = _lees(wiki, "beschikking")
    data["besluiten"].append({"datum": "2026-10-02", "besluit": "Toch niet.", "gevolg": "afwijzen"})
    _schrijf(wiki, "beschikking", data)
    _beslissen(wiki)
    data = _lees(wiki, "beschikking")
    assert data["status"] == "afgewezen" and "pad" not in data["beslist"]
    assert not (wiki / "elementpaginas/bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md").exists()


def test_goedgekeurd_blijft_tot_de_inhoud_wijzigt(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _beslissen(wiki)
    data = _lees(wiki, "beschikking")
    data["status"] = "goedgekeurd"
    _schrijf(wiki, "beschikking", data)
    logbook.append_log(wiki, "promote", "beschikking", "Redacteur", beoordeling.inhoud_hash(data))
    _beslissen(wiki)
    assert _lees(wiki, "beschikking")["status"] == "goedgekeurd"

    data = _lees(wiki, "beschikking")
    data["definitie"] = "Een andere definitie."
    _schrijf(wiki, "beschikking", data)
    _beslissen(wiki)
    assert _lees(wiki, "beschikking")["status"] == "review"


def test_goedgekeurd_zonder_logregel_wordt_review(wiki):
    _schrijf(wiki, "beschikking", {**_bo(), "status": "goedgekeurd"})
    _beslissen(wiki)
    assert _lees(wiki, "beschikking")["status"] == "review"


@pytest.mark.parametrize("wijziging, melding", [
    (lambda d: d["relaties"][0].update(naar="onbekend"), "geen element"),
    (lambda d: d["relaties"][0].update(soort="toegang (houder)"), "toegang 'houder'"),
    (lambda d: d["kenmerken"]["gedrag"].update(bronnen=["2026-onbekende-bron"]), "staat niet in sources/index"),
    (lambda d: d.pop("definitie"), "zonder 'definitie'"),
    (lambda d: d.update(onderwerpen=["ander"]), "onderwerp 'ander'"),
    (lambda d: d.update(onverwacht="x"), "onverwacht"),
    (lambda d: d["kenmerken"]["gedrag"].pop("bronnen"), "kenmerk 'ja' zonder bron: gedrag"),
])
def test_harde_fouten_schrijven_niets(wiki, wijziging, melding):
    _schrijf(wiki, "beschikking", _bo())
    proces = _proces()
    wijziging(proces)
    _schrijf(wiki, "behandelen-aanvraag", proces)
    res = beslissen.beslissen(wiki)
    assert any(melding in f for f in res.fouten), res.fouten
    assert "status" not in _lees(wiki, "beschikking")


def test_nieuwe_terugmelding_krijgt_het_volgende_nummer(wiki):
    _schrijf(wiki, "beschikking", _bo())
    register = {"terugmeldingen": [
        {"nummer": 1, "domein": "Vergunningen", "type": "hiaat", "bevinding": ["**Bevinding:** ontbreekt.", "**Voorstel:** opnemen."],
         "element": "beschikking", "status": "open"},
        {"domein": "Vergunningen", "type": "definitie", "bevinding": ["**Bevinding:** te smal.", "**Voorstel:** verbreden."],
         "element": "beschikking"}]}
    beoordeling.schrijf(wiki / beslissen.TERUGMELDINGEN, register)
    _beslissen(wiki)
    meldingen = beoordeling.laad(wiki / beslissen.TERUGMELDINGEN)["terugmeldingen"]
    assert [(m["nummer"], m["status"]) for m in meldingen] == [(1, "open"), (2, "open")]
    pagina = (wiki / _lees(wiki, "beschikking")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "[Nummer 2](../../../../../modellen/ggm/terugmeldingen.md)" in pagina


def test_open_terugmelding_zonder_voorstel_is_een_fout(wiki):
    _schrijf(wiki, "beschikking", _bo())
    register = {"terugmeldingen": [
        {"nummer": 1, "domein": "Vergunningen", "type": "hiaat", "bevinding": ["**GGM:** ontbreekt.", "**Bevinding:** nodig."],
         "element": "beschikking", "status": "open"},
        {"nummer": 2, "domein": "Vergunningen", "type": "hiaat", "bevinding": "Oud.", "element": "beschikking", "status": "opgelost"}]}
    beoordeling.schrijf(wiki / beslissen.TERUGMELDINGEN, register)
    res = beslissen.beslissen(wiki, schrijven=False)
    assert res.fouten == ["terugmelding 1: een open melding heeft een alinea die begint met **Voorstel:**"]


def test_gemma_terugmelding_noemt_wiki_en_gemma_elementen(wiki):
    import gam_gemeen

    modellen.schrijf_json(
        gam_gemeen.model_json(wiki, "gemma"), "archimate",
        {"elementen": {"id-functie": {"id": "id-functie", "naam": "Uitvoering veiligheid", "type": "business-function",
                                      "documentatie": "", "map": "Business", "map_id": "f", "eigenschappen": {}}},
         "mappen": {}, "model": {}, "relaties": {}})
    _schrijf(wiki, "beschikking", _bo())
    register = {"terugmeldingen": [
        {"type": "element", "elementen": ["beschikking"], "gemma_elementen": [{"id": "id-functie", "naam": "Uitvoering veiligheid"}],
         "bevinding": ["**Bevinding:** vervalt in de wiki.", "**Voorstel:** herzien."]}]}
    beoordeling.schrijf(wiki / beslissen.GEMMA_TERUGMELDINGEN, register)
    _beslissen(wiki)
    meldingen = beoordeling.laad(wiki / beslissen.GEMMA_TERUGMELDINGEN)["terugmeldingen"]
    assert [(m["nummer"], m["status"]) for m in meldingen] == [(1, "open")]
    lijst = (wiki / "modellen/gemma/terugmeldingen/gemma-team.md").read_text(encoding="utf-8")
    assert "Uitvoering veiligheid (GEMMA)" in lijst and "## Terugmeldingen" in lijst
    pagina = (wiki / _lees(wiki, "beschikking")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "[Nummer 1](../../../../../modellen/gemma/terugmeldingen/gemma-team.md)" in pagina
    # een GEMMA-element dat niet bestaat of anders heet, is een fout
    register["terugmeldingen"][0]["gemma_elementen"] = [{"id": "id-functie", "naam": "Andere naam"}]
    register["terugmeldingen"][0] |= {"nummer": 1, "status": "open"}
    beoordeling.schrijf(wiki / beslissen.GEMMA_TERUGMELDINGEN, register)
    res = beslissen.beslissen(wiki, schrijven=False)
    assert res.fouten == ["GEMMA-terugmelding 1: GEMMA-element 'id-functie' heet 'Uitvoering veiligheid', niet 'Andere naam'"]


def test_signalen_noemen_de_regel_bij_naam(wiki):
    _schrijf(wiki, "beschikking", _bo(beschrijving=["Wordt geregistreerd in het zaaksysteem."]))
    _schrijf(wiki, "aanvraag-behandeling", _element("Aanvraagbehandeling", PROCES, kernobject="beschikking", afnemer="extern"))
    res = beslissen.beslissen(wiki)
    assert res.fouten == []
    assert any("regel Naamvorm" in w and "aanvraag-behandeling" in w for w in res.waarschuwingen)
    assert any("regel Beslistabel beslist" in w and "geregistreerd" in w for w in res.waarschuwingen)


def test_relatie_buiten_het_kennismodel_is_een_signaal_en_staat_op_de_pagina(wiki):
    """Geldig in ArchiMate maar niet in het kennismodel: vastgelegd, signaal, markering op beide pagina's."""
    _schrijf(wiki, "beschikking", _bo())
    proces = _proces()
    proces["relaties"][0].update(soort="associatie (gericht)", naam="betreft")
    _schrijf(wiki, "behandelen-aanvraag", proces)
    res = _beslissen(wiki)
    assert any("behandelen-aanvraag" in w and "nergens in het kennismodel" in w for w in res.waarschuwingen)
    for pad in wiki.rglob("behandelen-aanvraag.md"), wiki.rglob("beschikking.md"):
        tekst = next(pad).read_text(encoding="utf-8")
        assert "niet in het kennismodel, gaat niet mee in de export" in tekst


def test_relatie_in_het_kennismodel_heeft_geen_signaal_en_geen_markering(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    res = _beslissen(wiki)
    assert not any("kennismodel (" in w or "in het kennismodel;" in w for w in res.waarschuwingen)
    assert "niet in het kennismodel" not in next(wiki.rglob("beschikking.md")).read_text(encoding="utf-8")


def test_relatie_ongeldig_in_archimate_blijft_een_fout(wiki):
    _schrijf(wiki, "beschikking", _bo())
    proces = _proces()
    proces["relaties"][0].update(soort="compositie")  # gedrag → passief bestaat niet in ArchiMate
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert any("niet geldig in de ArchiMate-relatietabel" in f for f in beslissen.beslissen(wiki).fouten)


def test_kenmerk_ja_zonder_kernrelatie_is_een_signaal(wiki):
    _schrijf(wiki, "beschikking", _bo())  # wordt_bewerkt: ja, maar niets bewerkt haar
    res = beslissen.beslissen(wiki)
    assert res.fouten == []
    assert any("beschikking" in w and "kenmerk wordt_bewerkt is ja" in w for w in res.waarschuwingen)
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    assert not any("beschikking: kenmerk wordt_bewerkt" in w for w in beslissen.beslissen(wiki).waarschuwingen)



def test_kernrelatie_telt_ook_eronder():
    """Een kernrelatie mag liggen bij wat het element omvat of bedient, bij een specialisatie of bij een gebeurtenis die
    het triggert (regel Beslistabel beslist)."""
    import signalen
    rel = lambda van, soort, naar, doel="bedrijfsproces": (van, {"soort": soort, "naar": naar}, "x", doel)  # noqa: E731
    relaties = [rel("levensloop", "aggregatie", "proces"), rel("functie", "bediening", "levensloop"),
                rel("beschikking", "specialisatie", "besluit"), rel("verval", "triggering", "inlevering", "gebeurtenis"),
                rel("inlevering", "triggering", "inhouden"), rel("rol", "toewijzing", "proces")]
    assert signalen._eronder("functie", relaties) == {"functie", "levensloop", "proces"}
    assert signalen._eronder("besluit", relaties) == {"besluit", "beschikking"}
    assert signalen._eronder("verval", relaties) == {"verval", "inlevering"}   # niet verder dan de gebeurtenis
    assert signalen._eronder("rol", relaties) == {"rol"}


def _modelbron(wiki, tmp_path, bron_id, model, *, bronduiding=True, bronnen=()):
    """Een bron van brontype `model` in sources/, met haar bronduiding in modellen/<model>/bronduidingen/model/."""
    from llmwiki import sources
    for b in (bron_id, *bronnen):
        origineel = tmp_path / f"{b}.md"
        origineel.write_text(f"# {b}\n", encoding="utf-8")
        sources.add(wiki.parent.parent, b, origineel, titel=f"Titel van {b}", tags=["test"], brontype="model")
    if bronduiding:
        pad = wiki / "modellen" / model / "bronduidingen" / "model" / f"{bron_id}.md"
        pad.parent.mkdir(parents=True, exist_ok=True)
        pad.write_text(f"---\nid: {bron_id}\ntype: bronduiding\nmodel: {model}\nbronnen: [{', '.join((bron_id, *bronnen))}]\n"
                       f"relevant: ja\nkorte_titel: Website\n---\n\n# {bron_id}\n\nBron: [tekst](../../../../../../sources/raw/{bron_id}.md)\n",
                       encoding="utf-8")
    return bron_id


def test_model_als_bron_is_een_signaal(wiki, tmp_path):
    """Het GGM en het GEMMA-model zijn matchdoel, geen bron (regel Bronvoorrang)."""
    model = _modelbron(wiki, tmp_path, "2026-vng-gemma-2026-10-02", "gemma")
    bo = _bo()
    bo["kenmerken"]["wordt_bewerkt"]["bronnen"] = [WET, model]
    _schrijf(wiki, "beschikking", bo)
    res = beslissen.beslissen(wiki, schrijven=False)
    assert res.fouten == []
    assert any(w.startswith(f"beschikking: {model} is een model, matchdoel en geen bron") for w in res.waarschuwingen)


def test_modelbron_linkt_naar_haar_bronduiding(wiki, tmp_path):
    """Pagina → bronduiding → laag 1, ook bij het GEMMA-model (repo-AGENTS.md, Herleidbaarheid)."""
    import gam_gemeen
    model = _modelbron(wiki, tmp_path, "2026-vng-gemma-2026-10-02", "gemma")
    assert gam_gemeen.bron_doel(wiki, model) == (wiki / f"modellen/gemma/bronduidingen/model/{model}.md").resolve()
    assert render.Wiki(wiki).bron("elementpaginas/x.md", model) == f"[{model}](../modellen/gemma/bronduidingen/model/{model}.md)"


def test_modelbron_zonder_bronduiding_is_een_fout(wiki, tmp_path):
    model = _modelbron(wiki, tmp_path, "2026-vng-gemma-2026-10-02", "gemma", bronduiding=False)
    bo = _bo()
    bo["kenmerken"]["wordt_bewerkt"]["bronnen"] = [WET, model]
    _schrijf(wiki, "beschikking", bo)
    assert f"beschikking: bron {model} heeft geen bronduiding" in beslissen.beslissen(wiki, schrijven=False).fouten


def test_een_bronduiding_duidt_ook_de_bronnen_in_haar_bronnenlijst(wiki, tmp_path):
    """Een website van veel pagina's heeft één bronduiding; elke pagina linkt daarheen, met haar eigen titel."""
    import gam_gemeen
    _modelbron(wiki, tmp_path, "2026-ggm-website", "ggm", bronnen=["2026-ggm-website-cookbook"])
    doel = (wiki / "modellen/ggm/bronduidingen/model/2026-ggm-website.md").resolve()
    assert gam_gemeen.bron_doel(wiki, "2026-ggm-website-cookbook") == doel
    w = render.Wiki(wiki)
    assert w.korte_titel("2026-ggm-website") == "Website"
    assert w.korte_titel("2026-ggm-website-cookbook") == "Titel van 2026-ggm-website-cookbook"
    assert gam_gemeen.bron_doel(wiki, "2026-ggm-onbekend") is None


def test_bronduiding_staat_in_de_map_van_haar_brontype(wiki):
    pad = wiki / "onderwerpen" / "test" / "bronduidingen" / "rijksregelgeving" / f"{WET}.md"
    fout = wiki / "onderwerpen" / "test" / "bronduidingen" / "beleid" / f"{WET}.md"
    pad.rename(fout)
    _schrijf(wiki, "beschikking", _bo())
    assert f"onderwerpen/test/bronduidingen/beleid/{WET}.md: hoort in onderwerpen/test/bronduidingen/rijksregelgeving/" in beslissen.beslissen(wiki).fouten


def test_bronduiding_zonder_bronregel_is_een_fout(wiki):
    pad = wiki / "onderwerpen" / "test" / "bronduidingen" / "rijksregelgeving" / f"{WET}.md"
    pad.write_text(pad.read_text(encoding="utf-8").replace("Bron: ", "Zie: "), encoding="utf-8")
    _schrijf(wiki, "beschikking", _bo())
    assert any("'Bron:'" in f for f in beslissen.beslissen(wiki).fouten)


def test_element_zonder_enige_bron_is_een_fout(wiki):
    bo = _bo()
    for antwoord in bo["kenmerken"].values():
        antwoord.pop("bronnen", None)
    _schrijf(wiki, "beschikking", bo)
    fouten = beslissen.beslissen(wiki).fouten
    assert any("element zonder bron" in f for f in fouten)
    assert any("kenmerk 'ja' zonder bron" in f for f in fouten)


# --- Stap 7: indeling ---


def _deelproces(**extra) -> dict:
    ja = (PROCES - {"omvat_levensloop"}) | {"bijdrage_aan_groter_proces", "klant_tot_klant", "eigen_besluit"}
    return _element("Verlenen grafrecht", ja, kernobject="beschikking", afnemer="extern", **extra)


def test_object_zonder_proces_wordt_voorgelegd_en_een_kernobject_is_een_kernobject(wiki):
    _schrijf(wiki, "graf", _element("Graf", BO, ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}))
    _beslissen(wiki)
    data = _lees(wiki, "graf")
    assert data["status"] == "kandidaat"
    assert any("levensloop" in r for r in data["beslist"]["voor_te_leggen"])

    _schrijf(wiki, "beheren-graven", _element("Beheren graven", PROCES, kernobject="graf", afnemer="extern",
                                              relaties=[_rel("toegang (registreren)", "graf")]))
    _beslissen(wiki)
    assert _lees(wiki, "graf")["beslist"]["uitkomst"]["objectniveau"] == "kernobject"
    assert _lees(wiki, "graf")["status"] == "review"
    assert _lees(wiki, "beheren-graven")["beslist"]["uitkomst"]["procesniveau"] == "levensloopproces"


def test_twee_processen_voor_een_kernobject_is_een_fout(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    _schrijf(wiki, "beheren", _element("Beheren beschikkingen", PROCES, kernobject="beschikking", afnemer="extern"))
    res = beslissen.beslissen(wiki)
    assert any("per kernobject één levensloopproces" in f for f in res.fouten)


def test_levensloopproces_onder_een_levensloopproces_is_een_fout(wiki):
    """Een keten is een bedrijfsinteractie, geen proces boven de levensloopprocessen (besluit 2026-10-08)."""
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "aanvraag", _element("Aanvraag", BO, ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}))
    _schrijf(wiki, "behandelen-aanvraag", _element("Behandelen aanvragen", PROCES, kernobject="aanvraag", afnemer="extern"))
    _schrijf(wiki, "keten", _element("Afhandelen beschikkingen", PROCES, kernobject="beschikking", afnemer="extern",
                                     relaties=[_rel("aggregatie", "behandelen-aanvraag")]))
    res = beslissen.beslissen(wiki)
    assert any("levensloopproces aggregeert levensloopproces 'behandelen-aanvraag'" in f for f in res.fouten)


def test_indelingsveld_ontbreekt_wordt_voorgelegd_en_een_onbekende_waarde_is_een_fout(wiki):
    _schrijf(wiki, "beschikking", _bo())
    data = _proces()
    del data["afnemer"]
    _schrijf(wiki, "behandelen-aanvraag", data)
    assert beslissen.beslissen(wiki).fouten == []
    _beslissen(wiki)
    beslist = _lees(wiki, "behandelen-aanvraag")
    assert beslist["status"] == "kandidaat"
    assert "indelingsveld ontbreekt: afnemer" in beslist["beslist"]["voor_te_leggen"]
    data["afnemer"] = "allemaal"
    _schrijf(wiki, "behandelen-aanvraag", data)
    assert any("allemaal" in f for f in beslissen.beslissen(wiki).fouten)  # het schema weigert de waarde


def test_via_moet_een_specialisatie_van_het_doel_zijn(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "verlof", _element("Verlof", BO - {"zelfstandige_specialisatie"}, genoemd_begrip="Beschikking",
                                      ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}))
    proces = _proces()
    proces["relaties"][0]["via"] = "verlof"
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert beslissen.beslissen(wiki).fouten == []
    proces["relaties"][0]["via"] = "beschikking"  # een element, geen specialisatie
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert any("geen specialisatie van dat doel" in f for f in beslissen.beslissen(wiki).fouten)


def test_leidt_tot_gebeurtenis_vraagt_een_triggering(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "overlijden", _element("Overlijden", GEBEURTENIS, relaties=[_rel("triggering", "behandelen-aanvraag")]))
    proces = _proces()
    proces["kenmerken"]["leidt_tot_gebeurtenis"] = {"waarde": "ja", "onderbouwing": "Eindigt in een overlijden.", "bronnen": [WET]}
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert any("geen relatie 'triggering' naar een gebeurtenis" in f for f in beslissen.beslissen(wiki).fouten)
    proces["relaties"].append(_rel("triggering", "overlijden"))
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert beslissen.beslissen(wiki).fouten == []


def test_gemma_generiek_moet_in_het_gemma_model_staan(wiki):
    import gam_gemeen

    modellen.schrijf_json(
        gam_gemeen.model_json(wiki, "gemma"), "archimate",
        {"elementen": {"id-vergunning": {"id": "id-vergunning", "naam": "Behandelen aanvraag vergunning of ontheffing",
                                         "type": "business-process", "documentatie": "", "map": "Business", "map_id": "f",
                                         "eigenschappen": {}}}, "mappen": {}, "model": {}, "relaties": {}})
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "behandelen-aanvraag", _proces(gemma_generiek={"id": "id-vergunning", "onderbouwing": "Generiek proces."}))
    assert beslissen.beslissen(wiki).fouten == []
    _schrijf(wiki, "behandelen-aanvraag", _proces(gemma_generiek={"id": "id-weg", "onderbouwing": "Bestaat niet."}))
    assert any("gemma_generiek 'id-weg' bestaat niet" in f for f in beslissen.beslissen(wiki).fouten)


def test_kwaliteitsdoelen_van_een_beleidskader(wiki):
    import gam_gemeen

    def goal(naam, gemma_type="Kwaliteitsdoel"):
        return {"id": f"id-{naam.lower()}", "naam": naam, "type": "goal", "documentatie": f"{naam} als doel.",
                "map": "Motivation", "map_id": "f", "eigenschappen": {"GEMMA type": gemma_type}}

    modellen.schrijf_json(
        gam_gemeen.model_json(wiki, "gemma"), "archimate",
        {"elementen": {"id-rechtmatig": goal("Rechtmatig"), "id-ander": goal("Ander", "Doel")},
         "mappen": {}, "model": {}, "relaties": {}})
    doel = {"id": "id-rechtmatig", "sterkte": "++", "onderbouwing": "De wet regelt de taak.", "bronnen": [WET],
            "vindplaats": "art. 1"}
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "wet", _element("Wet op de lijkbezorging", BELEIDSKADER, regelgever="rijk", kwaliteitsdoelen=[doel],
                                   relaties=[_rel("associatie (gericht)", "behandelen-aanvraag")]))
    _beslissen(wiki)
    wet = _lees(wiki, "wet")
    assert wet["beslist"]["kwaliteitsdoelen"] == [{"gemma_id": "id-rechtmatig", "gemma_naam": "Rechtmatig",
                                                   "gemma_definitie": "Rechtmatig als doel."}]
    pagina = (wiki / wet["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "### Kwaliteitsdoelen" in pagina and "| *Rechtmatig* (GEMMA) | `++` | De wet regelt de taak." in pagina
    # alleen een kwaliteitsdoel van GEMMA, één keer, en alleen bij een beleidskader
    _schrijf(wiki, "wet", {**_lees(wiki, "wet"), "kwaliteitsdoelen": [{**doel, "id": "id-ander"}, doel, doel]})
    fouten = beslissen.beslissen(wiki).fouten
    assert any("'id-ander' is geen kwaliteitsdoel" in f for f in fouten)
    assert any("Rechtmatig staat er twee keer" in f for f in fouten)
    _schrijf(wiki, "wet", {**_lees(wiki, "wet"), "kwaliteitsdoelen": [doel]})
    _schrijf(wiki, "beschikking", _bo(kwaliteitsdoelen=[doel]))
    assert any("horen alleen bij een beleidskader" in f for f in beslissen.beslissen(wiki).fouten)


def test_signalen_voor_de_indeling():
    import signalen

    def el(paginatype, **u):
        return {"paginatype": paginatype, "soort": "element", **u}

    elementen = {
        "beheren": el("bedrijfsproces", procesniveau="levensloopproces"),
        "cluster": el("bedrijfsproces", procesniveau="cluster naar soort werk"),
        "deel": el("bedrijfsproces", procesniveau="bedrijfsproces"),
        "wees": el("bedrijfsproces", procesniveau="bedrijfsproces"),
        "alleen-soort": el("bedrijfsproces", procesniveau="bedrijfsproces"),
        "keten": el("bedrijfsinteractie"),
        "lege-keten": el("bedrijfsinteractie"),
        "onderhoud": el("dienst"),
        "wet": el("beleidskader"),
        "wet-dienst": el("beleidskader"),
        "gemeente": el("actor"),
        "raad": el("actor"),
        "arts": el("gebeurtenis", generiek=True),
    }
    rel = lambda soort, naar, naam=None: {"soort": soort, "naar": naar, "naam": naam}  # noqa: E731
    alle = {b: {"onderwerpen": ["lijkbezorging" if b != "elders" else "burgerzaken"]} for b in elementen}
    alle["beheren"]["relaties"] = [rel("aggregatie", "deel")]
    alle["cluster"]["relaties"] = [rel("aggregatie", "deel"), rel("aggregatie", "alleen-soort")]
    alle["deel"]["relaties"] = [rel("realisatie", "onderhoud"), rel("bediening", "keten")]
    alle["wet-dienst"]["relaties"] = [rel("associatie (gericht)", "onderhoud", "is grondslag voor")]
    alle["gemeente"]["relaties"] = [rel("associatie (gericht)", "raad", "geeft melding door aan"),
                                    rel("associatie (gericht)", "raad", "is voorzitter van")]
    relaties = [(van, r) for van in elementen for r in alle[van].get("relaties", [])]
    tekst = "\n".join(signalen.indeling(alle, elementen, relaties))
    assert "wees: hangt onder geen levensloopproces" in tekst
    assert "alleen-soort: hangt onder geen levensloopproces" in tekst  # een cluster naar soort werk telt niet
    assert "deel: hangt onder geen" not in tekst and "beheren: hangt" not in tekst
    assert "lege-keten: geen bedrijfsproces bedient" in tekst and "keten: geen bedrijfsproces" not in tekst.replace("lege-keten", "")
    assert "wet: geen dienst of product heeft dit beleidskader" in tekst
    assert "wet-dienst: geen dienst" not in tekst  # grondslag voor een dienst volstaat
    assert "geeft melding door aan" in tekst and "is voorzitter van" not in tekst
    assert "arts: generiek, maar geen `gemma_generiek`" in tekst


def _functie_gemma():
    """Een kleine GEMMA-functiehiërarchie: domein › domeinfunctie › soort › onderwerp, en een functie onder het domein."""
    def el(id_, type_="business-function", gemma_type=None, map_="Business / Bedrijfsfuncties", naam=None):
        return {"id": id_, "naam": naam or id_, "type": type_, "map": map_,
                "eigenschappen": {"GEMMA type": gemma_type} if gemma_type else {}}
    elementen = {
        "g-fl": el("g-fl", "grouping", map_="Other / Domein en doelgroep / Domeinen", naam="Fysieke leefomgeving"),
        "g-domein": el("g-domein", gemma_type="Bedrijfsfunctie domein"),
        "g-soort": el("g-soort", gemma_type="Bedrijfsfunctie"),
        "g-onderwerp": el("g-onderwerp"),
        "g-elders": el("g-elders"),
    }
    agg = lambda i, bron, doel: {"id": i, "type": "aggregation-relationship", "bron": bron, "doel": doel}  # noqa: E731
    relaties = {r["id"]: r for r in (agg("r0", "g-fl", "g-domein"), agg("r1", "g-domein", "g-soort"),
                                     agg("r2", "g-soort", "g-onderwerp"))}
    return {"elementen": elementen, "relaties": relaties}


def test_signalen_voor_de_functie_indeling():
    import signalen

    gemma_data = _functie_gemma()
    elementen = {b: {"paginatype": "bedrijfsfunctie", "soort": "element"}
                 for b in ("domein", "soort", "onderwerp", "nieuw", "wees", "elders", "eigen")}
    agg = lambda naar: {"soort": "aggregatie", "naar": naar}  # noqa: E731
    fl = "Fysieke leefomgeving"
    alle = {
        "domein": {"gemma": {"id": "g-domein"}, "domein": fl, "relaties": [agg("soort")]},
        "soort": {"gemma": {"id": "g-soort"}, "domein": fl, "relaties": [agg("onderwerp"), agg("nieuw"), agg("elders")]},
        "onderwerp": {"gemma": {"id": "g-onderwerp"}, "domein": fl},
        "nieuw": {"gemma": {"sterkte": "geen"}, "domein": fl, "relaties": [agg("eigen")]},
        "wees": {"gemma": {"sterkte": "geen"}, "domein": fl},
        "elders": {"gemma": {"id": "g-elders"}, "domein": "Publieksdiensten"},
        "eigen": {"gemma": {"sterkte": "geen"}, "domein": fl},
    }
    relaties = [(van, r) for van in elementen for r in alle[van].get("relaties", [])]
    tekst = "\n".join(signalen.functie_indeling(alle, elementen, relaties, gemma_data))
    assert "wees: hangt onder geen bovenliggende functie" in tekst
    assert "elders: domein 'Publieksdiensten' wijkt af" in tekst
    assert "elders: in GEMMA aggregeert soort deze functie niet" in tekst
    assert "eigen: de bovenliggende functie nieuw heeft geen GEMMA-match" in tekst
    # een dienst hangt onder één functie in hetzelfde domein
    elementen.update({"dienst": {"paginatype": "dienst", "soort": "element"}, "los": {"paginatype": "dienst", "soort": "element"},
                      "verkeerd": {"paginatype": "dienst", "soort": "element"},
                      "product": {"paginatype": "product", "soort": "element"},
                      "los-product": {"paginatype": "product", "soort": "element"}})
    alle.update({"dienst": {"domein": fl}, "los": {"domein": fl}, "verkeerd": {"domein": "Publieksdiensten"},
                 "product": {"domein": fl}, "los-product": {"domein": fl}})
    alle["onderwerp"]["relaties"] = [agg("dienst"), agg("verkeerd"), agg("product")]
    relaties = [(van, r) for van in elementen for r in alle[van].get("relaties", [])]
    tekst = "\n".join(signalen.functie_indeling(alle, elementen, relaties, gemma_data))
    assert "los: hangt onder geen functie" in tekst and "dienst:" not in tekst
    assert "verkeerd: domein 'Publieksdiensten' wijkt af van dat van de functie onderwerp" in tekst
    # een product hangt via domein aan de domeingroepering, niet onder een functie (besluit 2026-10-05)
    assert "product: product onder een functie (onderwerp)" in tekst and "los-product:" not in tekst
    # domeinniveau hangt aan de groepering; een functie onder een GEMMA-functie die GEMMA volgt geeft geen signaal
    assert not any(tekst_regel.startswith(("domein:", "soort:", "onderwerp:", "nieuw:")) for tekst_regel in tekst.splitlines())


def test_signalen_voor_gemma_functie():
    """De bovenliggende functie is een GEMMA-functie zonder beoordeling (`gemma_functie`): zelfde controles."""
    import signalen

    gemma_data = _functie_gemma()
    elementen = {b: {"paginatype": t, "soort": "element"}
                 for b, t in (("kind", "bedrijfsfunctie"), ("dienst", "dienst"), ("elders-dienst", "dienst"),
                              ("kind-elders", "bedrijfsfunctie"), ("tweeledig", "dienst"), ("product", "product"))}
    fl = "Fysieke leefomgeving"
    gf = lambda i: {"id": i}  # noqa: E731
    alle = {
        "kind": {"gemma": {"id": "g-onderwerp"}, "domein": fl, "gemma_functie": gf("g-soort")},
        "dienst": {"domein": fl, "gemma_functie": gf("g-soort")},
        "elders-dienst": {"domein": "Publieksdiensten", "gemma_functie": gf("g-soort")},
        "kind-elders": {"gemma": {"id": "g-elders"}, "domein": fl, "gemma_functie": gf("g-soort")},
        "tweeledig": {"domein": fl, "gemma_functie": gf("g-soort")},
        "product": {"domein": fl, "gemma_functie": gf("g-soort")},
    }
    relaties = [("kind", {"soort": "aggregatie", "naar": "tweeledig"})]
    elementen["kind"]["paginatype"] = "bedrijfsfunctie"
    tekst = "\n".join(signalen.functie_indeling(alle, elementen, relaties, gemma_data))
    regels = tekst.splitlines()
    assert not any(r.startswith(("dienst:", "kind:")) for r in regels)  # gemma_functie volstaat, en GEMMA volgt de keten
    assert "elders-dienst: domein 'Publieksdiensten' wijkt af van dat van de functie g-soort (Fysieke leefomgeving)" in tekst
    assert "kind-elders: in GEMMA aggregeert g-soort deze functie niet" in tekst
    assert "tweeledig: meer functies (kind, g-soort)" in tekst
    assert "product: product onder een functie (g-soort)" in tekst
    # een functie zonder beide plekken en een domeinfunctie met een bovenliggende functie
    alle["los"] = {"gemma": {"sterkte": "geen"}, "domein": fl}
    alle["g-domein-element"] = {"gemma": {"id": "g-domein"}, "domein": fl, "gemma_functie": gf("g-soort")}
    elementen.update({"los": {"paginatype": "bedrijfsfunctie", "soort": "element"},
                      "g-domein-element": {"paginatype": "bedrijfsfunctie", "soort": "element"}})
    tekst = "\n".join(signalen.functie_indeling(alle, elementen, relaties, gemma_data))
    assert "los: hangt onder geen bovenliggende functie: aggregatie vanaf een functie of `gemma_functie` ontbreekt" in tekst
    assert "g-domein-element: functie op domeinniveau met een bovenliggende functie (g-soort)" in tekst


def test_domein_past_bij_de_gemma_domeinen_van_het_beleidsdomein():
    import signalen

    # GEMMA-domeinen aggregeren beleidsdomeinen; een beleidsdomein kan onder meer domeinen vallen (besluit 2026-10-05)
    groep = lambda naam, map_, soort=None: {"type": "grouping", "naam": naam, "map": map_,  # noqa: E731
                                            "eigenschappen": {"GEMMA type": soort} if soort else {}}
    gemma_data = {
        "elementen": {
            "d-fl": groep("Fysieke leefomgeving", "Other / Domein en doelgroep / Domeinen"),
            "d-pd": groep("Publieksdiensten", "Other / Domein en doelgroep / Domeinen"),
            "b-erfgoed": groep("Erfgoed", "Other / Beleidsdomeinen", "Beleidsdomein"),
            "b-burgerzaken": groep("Burgerzaken", "Other / Beleidsdomeinen", "Beleidsdomein"),
        },
        "relaties": {
            "r1": {"type": "aggregation-relationship", "bron": "d-fl", "doel": "b-erfgoed"},
            "r2": {"type": "aggregation-relationship", "bron": "d-pd", "doel": "b-erfgoed"},
            "r3": {"type": "aggregation-relationship", "bron": "d-pd", "doel": "b-burgerzaken"},
        },
    }
    fl, pd = "Fysieke leefomgeving", "Publieksdiensten"
    alle = {
        "monument": {"beleidsdomein": "Erfgoed", "domein": fl},
        "akte": {"beleidsdomein": "Burgerzaken", "domein": pd},
        "verkeerd": {"beleidsdomein": "Burgerzaken", "domein": fl},
        "graf": {"beleidsdomein": "Begraafplaatsen", "domein": fl},
        "register": {"beleidsdomein": "Begraafplaatsen", "domein": pd},
        "alleen": {"beleidsdomein": "Nieuw en enkel", "domein": fl},
    }
    elementen = {b: {"paginatype": "dienst", "soort": "element"} for b in alle}
    elementen["graf"]["paginatype"] = "product"
    tekst = "\n".join(signalen.domein_en_beleidsdomein(alle, elementen, gemma_data))
    assert "verkeerd: domein 'Fysieke leefomgeving' past niet bij beleidsdomein 'Burgerzaken'" in tekst
    assert "monument:" not in tekst and "akte:" not in tekst
    assert "beleidsdomein 'Begraafplaatsen' (nieuw voor GEMMA): producten en diensten in 2 domeinen" in tekst
    assert "Nieuw en enkel" not in tekst
    assert signalen.domein_en_beleidsdomein(alle, elementen, {}) == []
    # het model mag afwijken, mits teruggemeld: een procesarchitectuur-terugmelding dekt het signaal
    gemeld = [{"elementen": ["verkeerd"]}, {"beleidsdomein": "begraafplaatsen"}]
    assert signalen.domein_en_beleidsdomein(alle, elementen, gemma_data, gemeld) == []

def _indeling_wiki(wiki):
    """Een ketensamenwerking, een levensloopproces met een bedrijfsproces, een kernobject met subobject, een generiek
    object met specialisatie, een functie, een gebeurtenis en een dienst."""
    import gam_gemeen

    modellen.schrijf_json(
        gam_gemeen.model_json(wiki, "gemma"), "archimate",
        {"elementen": {"id-vergunning": {"id": "id-vergunning", "naam": "Behandelen aanvraag vergunning of ontheffing",
                                         "type": "business-process", "documentatie": "", "map": "Business", "map_id": "f",
                                         "eigenschappen": {}}}, "mappen": {}, "model": {}, "relaties": {}})
    geen_ggm = {"ggm": {"sterkte": "geen", "onderbouwing": "Niet in het GGM."}}
    keten = (PROCES - {"per_keer_doorlopen", "omvat_levensloop"}) | {"gezamenlijk_gedrag"}
    deel = (PROCES - {"omvat_levensloop"}) | {"bijdrage_aan_groter_proces", "klant_tot_klant", "eigen_besluit"}
    gevallen = {
        "bezorgen-lijken": _element("Bezorgen lijken", keten, kernobject="lijk",
                                    relaties=[_rel("toegang (registreren)", "lijk")]),
        "toestaan-lijkbezorging": _element("Toestaan lijkbezorging", PROCES, kernobject="lijk", afnemer="extern",
                                           relaties=[_rel("aggregatie", "opgraven-lijk")]),
        "opgraven-lijk": _element("Opgraven lijk", deel, kernobject="grafbedekking", afnemer="extern",
                                  gemma_generiek={"id": "id-vergunning", "onderbouwing": "Een vergunningaanvraag."},
                                  relaties=[{**_rel("toegang (registreren)", "vergunning"), "via": "vergunning-tot-opgraving"},
                                            _rel("realisatie", "onderhoud-van-graven"), _rel("bediening", "bezorgen-lijken")]),
        "lijk": _element("Lijk", BO, relaties=[_rel("compositie", "grafbedekking")], **geen_ggm),
        "grafbedekking": _element("Grafbedekking", BO | {"deel_van_object"}, **geen_ggm),
        "vergunning": _element("Vergunning", BO | {"generiek"}, **geen_ggm),
        "vergunning-tot-opgraving": _element("Vergunning tot opgraving", BO - {"zelfstandige_specialisatie"},
                                             genoemd_begrip="Vergunning", **geen_ggm),
        "onderhoud-van-graven": _element("Onderhoud van graven", DIENST, domein="Fysieke leefomgeving", afnemer="extern"),
        "exploiteren-begraafplaatsen": _element("Exploiteren van begraafplaatsen", FUNCTIE, domein="Fysieke leefomgeving",
                                                relaties=[_rel("bediening", "opgraven-lijk")]),
        "overlijden": _element("Overlijden", GEBEURTENIS, relaties=[_rel("triggering", "toestaan-lijkbezorging")]),
    }
    for bid, data in gevallen.items():
        _schrijf(wiki, bid, data)
    _beslissen(wiki)
    return gevallen


def test_pagina_toont_de_plaats_in_de_indelingen(wiki):
    _indeling_wiki(wiki)
    opgraven = _lees(wiki, "opgraven-lijk")
    assert opgraven["beslist"]["uitkomst"]["procesniveau"] == "bedrijfsproces"
    pagina = (wiki / opgraven["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "procesniveau: bedrijfsproces" in pagina and "afnemer: extern" in pagina
    assert "kernobject:" not in pagina.split("---")[1]  # een verwijzing staat niet in de frontmatter
    assert "#### Plaats in de indelingen" in pagina or "### Plaats in de indelingen" in pagina
    assert "**Procesindeling naar kernobject, onderdeel van**: [Toestaan lijkbezorging]" in pagina
    assert "**Ketensamenwerking, bedient**: [Bezorgen lijken]" in pagina
    assert "**Kernobject**: [Grafbedekking]" in pagina
    assert "**Procesindeling naar soort werk, specialisatie van**: GEMMA-element *id-vergunning*" in pagina or \
        "specialisatie van**: GEMMA-element" in pagina
    assert "**Functie-indeling naar domein, bediend door**: [Exploiteren van begraafplaatsen]" in pagina

    keten = (wiki / _lees(wiki, "bezorgen-lijken")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "bedrijfsinteracties" in _lees(wiki, "bezorgen-lijken")["beslist"]["pad"]
    assert "**Kernobject**: [Lijk]" in keten and "**Ketensamenwerking, bediend door**: [Opgraven lijk]" in keten
    levensloop = (wiki / _lees(wiki, "toestaan-lijkbezorging")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "**Procesniveau**: levensloopproces." in levensloop and "**Gestart door gebeurtenis**: [Overlijden]" in levensloop
    assert "omvat**: [Opgraven lijk]" in levensloop

    lijk = (wiki / _lees(wiki, "lijk")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "objectniveau: kernobject" in lijk and "**Levensloop bepaald door**: [Toestaan lijkbezorging]" in lijk
    assert "**Ketensamenwerking**: [Bezorgen lijken]" in lijk
    bedekking = (wiki / _lees(wiki, "grafbedekking")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "objectniveau: subobject" in bedekking and "**Subobject van**: [Lijk]" in bedekking
    assert "**Mutaties door bedrijfsprocessen**: [Opgraven lijk]" in bedekking

    vergunning = (wiki / _lees(wiki, "vergunning")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "objectniveau: generiek" in vergunning and "Specialisaties per onderwerp" in vergunning
    assert "**Vergunning tot opgraving**" in vergunning and "Genoemd door [Opgraven lijk]" in vergunning


def test_overzicht_per_onderwerp_toont_de_views(wiki):
    _indeling_wiki(wiki)
    overzicht = (wiki / "onderwerpen" / "test" / "overzicht.md").read_text(encoding="utf-8")
    assert "## Procesindeling naar kernobject" in overzicht
    assert "- **Vergunningen** *(beleidsdomein, taakveld 8 Wonen)*" in overzicht
    assert "  - [Toestaan lijkbezorging](" in overzicht and "*(levensloopproces, afnemer extern)*" in overzicht
    assert "    - [Opgraven lijk](" in overzicht and "bediend door [Exploiteren van begraafplaatsen]" in overzicht
    assert "levert [Onderhoud van graven]" in overzicht
    assert "## Ketensamenwerking" in overzicht and "bediend door [Opgraven lijk](" in overzicht
    assert "## Procesindeling naar soort werk" in overzicht
    assert "## Gebeurtenissen" in overzicht and "| [Overlijden](" in overzicht
    assert "**Kernobjecten**" in overzicht and "subobjecten [Grafbedekking]" in overzicht
    assert "**Generiek**" in overzicht and "[Vergunning]" in overzicht
    assert "## Functies" in overzicht and "## Producten en diensten" in overzicht
    lijst = (wiki / "onderwerpen" / "test" / "begrippen.md").read_text(encoding="utf-8")
    assert "overzicht.md" in lijst
    assert render.main(["--wiki", str(wiki), "--check"]) == 0


def test_signalen_voor_een_model_over_alle_onderwerpen():
    import signalen

    el = lambda paginatype, **u: {"soort": "element", "paginatype": paginatype, **u}  # noqa: E731
    rel = lambda naar: {"soort": "associatie", "naar": naar}  # noqa: E731
    alle = {
        "graf": {"begrip": "Graf", "onderwerpen": ["lijkbezorging"], "synoniemen": [{"naam": "Grafplaats", "context": "beleid"}],
                 "gemma": {"id": "id-1", "sterkte": "sterk"}, "relaties": [rel("beheren-graf")]},
        "grafplaats": {"begrip": "Grafplaats", "onderwerpen": ["lijkbezorging"], "gemma": {"id": "id-1", "sterkte": "exact"},
                       "relaties": [rel("graf")]},
        "gezindte": {"begrip": "Gezindte", "onderwerpen": ["lijkbezorging"], "synoniem_van": "Kerkgenootschap"},
        "kerkgenootschap": {"begrip": "Kerkgenootschap", "onderwerpen": ["lijkbezorging"],
                            "synoniemen": [{"naam": "Gezindte", "context": "wet"}], "relaties": [rel("graf")]},
        "beheren-graf": {"begrip": "Beheren graf", "onderwerpen": ["burgerzaken", "lijkbezorging"], "kernobject": "graf"},
        "beschikking": {"begrip": "Beschikking", "onderwerpen": ["besluitvorming"], "relaties": [rel("akte-opmaken")]},
        "akte-opmaken": {"begrip": "Opmaken akte", "onderwerpen": ["burgerzaken"], "kernobject": "beschikking",
                         "relaties": [rel("ambtenaar")]},
        "ambtenaar": {"begrip": "Ambtenaar", "onderwerpen": ["lijkbezorging"], "relaties": [rel("beheren-graf")]},
        "akte": {"begrip": "Akte", "onderwerpen": ["lijkbezorging"],
                 "kenmerken": {"betekenis_in_onderwerp": {"onderbouwing": "Hoort bij Burgerzaken."}}},
        "wees": {"begrip": "Wees", "onderwerpen": ["lijkbezorging"]},
    }
    uitkomsten = {b: el("bedrijfsobject") for b in alle}
    uitkomsten["gezindte"] = {"soort": "synoniem"}
    uitkomsten["akte"] = {"soort": "verwijzing"}
    onderwerpen = {o: {"naam": o.capitalize()} for o in ("lijkbezorging", "burgerzaken")}
    onderwerpen["besluitvorming"] = {"naam": "Besluitvorming", "niveau": "thematisch"}   # thuis in een gedeeld onderwerp
    tekst = "\n".join(signalen.modulariteit(alle, uitkomsten, onderwerpen))
    assert "'grafplaats' is naam of synoniem van graf, grafplaats" in tekst and "regel Eén element" in tekst
    assert "gezindte" not in tekst
    assert "graf, grafplaats: zelfde GEMMA-match id-1" in tekst
    assert "beheren-graf: thuisonderwerp 'burgerzaken', maar het kernobject graf hoort bij 'lijkbezorging'" in tekst
    assert "akte-opmaken: thuisonderwerp" not in tekst  # kernobject in een gedeeld onderwerp
    assert "akte: verwijst naar onderwerp 'burgerzaken'" in tekst
    assert "wees: geen relatie met een ander element" in tekst
    assert "ambtenaar: 2 relaties met elementen van 'burgerzaken' en 0 met het eigen thuisonderwerp" in tekst
    assert "beschikking: " not in tekst.replace("kernobject", "")


def test_begrippenlijst_en_voortgang_tonen_thuisonderwerp_en_samenhang(wiki):
    beoordeling.schrijf(wiki / "onderwerpen/ander/afbakening.yaml",
                        {"naam": "Ander", "niveau": "eigen", "status": "in-behandeling", "omschrijving": ["Een ander onderwerp."], "bronnen": []})
    _schrijf(wiki, "beschikking", _bo(onderwerpen=["ander", "test"]))
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    res = _beslissen(wiki)
    assert not any("behandelen-aanvraag: thuisonderwerp" in w for w in res.waarschuwingen)  # generiek kernobject
    lijst = (wiki / "onderwerpen" / "test" / "begrippen.md").read_text(encoding="utf-8")
    assert "Uit onderwerp [Ander](../ander/begrippen.md)." in lijst
    assert "Uit onderwerp" not in (wiki / "onderwerpen" / "ander" / "begrippen.md").read_text(encoding="utf-8")
    voortgang = (wiki / "voortgang.md").read_text(encoding="utf-8")
    assert "## Samenhang tussen onderwerpen" in voortgang
    assert "| Ander | 1 | 0 | 0 | Test 1 |" in voortgang and "| Test | 1 | 1 | 0 | Ander 1 |" in voortgang


def test_wettelijke_grondslag():
    import signalen

    def el(paginatype):
        return {"paginatype": paginatype, "soort": "element"}
    def data(bronnen, **extra):
        return {"beslist": {"bronnen": bronnen}, **extra}
    soorten = {"wet": "rijksregelgeving", "hup": "richtlijn", "2025-vng-upl-producten": "informatiemodel",
               "2026-logius-upl-actueel": "informatiemodel", "site": "overig"}
    alle = {
        "wet-x": data(["wet"], regelgever="rijk", relaties=[{"soort": "associatie (gericht)", "naar": "dienst-a", "naam": "is grondslag voor"}]),
        "hup-x": data(["hup"], regelgever="landelijke organisatie",
                      relaties=[{"soort": "associatie (gericht)", "naar": "dienst-a", "naam": "is grondslag voor"}]),
        "vng-model": data(["site"], regelgever="VNG-model",
                          relaties=[{"soort": "associatie (gericht)", "naar": "dienst-upl", "naam": "is grondslag voor"},
                                    {"soort": "associatie (gericht)", "naar": "dienst-a", "naam": "is grondslag voor"},
                                    {"soort": "associatie (gericht)", "naar": "proces-upl", "naam": "werkt uit voor"}]),
        "dienst-a": data(["site"]),                       # gegrond via het beleidskader van het Rijk
        "dienst-upl": data(["2025-vng-upl-producten"]),   # UPL zonder landelijke grondslag: blijft, geen uitwerking
        "proces-upl": data(["wet"], relaties=[{"soort": "realisatie", "naar": "dienst-upl"}]),
        "proces-vervallen": data(["site"], status="afgewezen", relaties=[{"soort": "realisatie", "naar": "dienst-upl"}]),
        "rol-zonder": data(["site"]),
        "functie": data(["site"]),
        "dienst-logius": data(["2026-logius-upl-actueel"]),   # ook de UPL van Logius: geen signaal
    }
    elementen = {"wet-x": el("beleidskader"), "hup-x": el("beleidskader"), "vng-model": el("beleidskader"), "dienst-a": el("dienst"),
                 "dienst-upl": el("dienst"), "proces-upl": el("bedrijfsproces"),
                 "proces-vervallen": el("bedrijfsproces"), "rol-zonder": el("rol"),
                 "functie": el("bedrijfsfunctie"), "dienst-logius": el("dienst")}
    fouten, signalen_ = signalen.wettelijke_grondslag(alle, elementen, soorten.get)
    assert fouten[0] == ("hup-x: een richtlijn is geen wettelijke grondslag; noem de relatie naar 'dienst-a' 'geeft "
                         "richtlijn voor' (regel Wettelijke grondslag)")
    # een VNG-model is nooit grondslag, ook niet voor een UPL-dienst zonder landelijke grondslag
    assert [f.split(":")[0] for f in fouten] == ["hup-x", "vng-model", "vng-model", "proces-upl"]   # een vervallen proces telt niet mee
    assert "een VNG-model is nooit grondslag; noem de relatie naar 'dienst-upl' 'werkt uit voor'" in fouten[1]
    assert "noem de relatie naar 'dienst-a' 'werkt uit voor'" in fouten[2]
    assert "realiseert UPL-dienst 'dienst-upl'" in fouten[3]
    assert [s.split(":")[0] for s in signalen_] == ["rol-zonder"]
    # de hoek zonder grondslag: UPL als bron, geen landelijke bron en geen 'is grondslag voor' van de EU of het Rijk
    assert signalen.zonder_grondslag(alle, elementen, soorten.get) == {"dienst-upl", "dienst-logius"}
    assert signalen.zonder_grondslag_terugmelding({"dienst-upl", "dienst-logius"}, [{"elementen": ["dienst-upl"]}]) == [
        "dienst-logius: UPL-dienst zonder landelijke grondslag zonder procesarchitectuur-terugmelding; meld haar terug "
        "als geen wettelijke taak (regel Wettelijke grondslag)"]


def test_zonder_grondslag_geen_signalen_van_uitwerking():
    """Een dienst zonder grondslag hoeft geen proces, geen kernrelatie en geen relatie met een ander element te hebben."""
    import bepaal_type
    import signalen

    kenmerken = {k: {"waarde": "nee"} for k in bepaal_type.SLEUTELS}
    kenmerken["gerealiseerd_door"] = {"waarde": "ja", "bronnen": ["upl"]}
    alle = {"dienst-z": {"begrip": "Dienst Z", "onderwerpen": ["test"], "kenmerken": kenmerken}}
    uitkomsten = {"dienst-z": {"soort": "element", "paginatype": "dienst", "archimate_type": "business-service"}}
    for zonder, verwacht in ((set(), True), ({"dienst-z"}, False)):
        w = (signalen.over_begrippen(alle, uitkomsten, zonder=zonder) + signalen.kennismodel(alle, uitkomsten, zonder)
             + signalen.modulariteit(alle, uitkomsten, {"test": {"naam": "Test"}}, zonder))
        assert any("geen proces of functie realiseert" in x for x in w) is verwacht
        assert any("kenmerk gerealiseerd_door is ja" in x for x in w) is verwacht
        assert any("geen relatie met een ander element" in x for x in w) is verwacht


def test_besluiten_van_een_onderwerp(wiki):
    onderwerp = beoordeling.laad(wiki / "onderwerpen/test/afbakening.yaml")
    onderwerp["besluiten"] = [{"datum": "2026-09-30", "begrip": "Uitdaagrecht", "besluit": "Geen eigen pagina.",
                               "stand": "open (todo)"},
                              {"datum": "2026-10-01", "besluit": "Afbakening van het onderwerp."}]
    beoordeling.schrijf(wiki / "onderwerpen/test/afbakening.yaml", onderwerp)
    _beslissen(wiki)
    assert not (wiki / "besluiten").exists()
    lijst = (wiki / "onderwerpen" / "test" / "begrippen.md").read_text(encoding="utf-8")
    assert "## Besluiten" in lijst and "- 2026-10-01: Afbakening van het onderwerp." in lijst
    assert "- 2026-09-30: **Uitdaagrecht**: Geen eigen pagina. *Stand: open (todo)*" in lijst
    # zonder datum, met een onbekend veld, over een begrip met een beoordeling of met een bestandspad: een fout
    _schrijf(wiki, "beschikking", _bo())
    begrip = "Beschikking"
    onderwerp["besluiten"] = [{"besluit": "Zie references/relaties.md.", "onderwerp": "test"},
                              {"datum": "2026-10-02", "begrip": begrip, "besluit": "Iets (regel Thuishoren, "
                                                                              "ARCHITECTURE.md *Indelingen*)."}]
    beoordeling.schrijf(wiki / "onderwerpen/test/afbakening.yaml", onderwerp)
    fouten = beslissen.beslissen(wiki, schrijven=False).fouten
    assert "onderwerp test, besluit 1: 'datum' ontbreekt of is geen datum (jjjj-mm-dd)" in fouten
    assert "onderwerp test, besluit 1: onbekend veld 'onderwerp'" in fouten
    assert any(f.startswith("onderwerp test, besluit 1: 'besluit' noemt het bestandspad 'references/relaties.md'") for f in fouten)
    assert any(f.startswith(f"onderwerp test, besluit 2: '{begrip}' heeft een beoordeling") for f in fouten)
    assert not any("besluit 2: 'besluit' noemt" in f for f in fouten)   # ARCHITECTURE.md bij naam mag


def test_object_van_zet_een_object_voort_en_wordt_getoetst(wiki):
    van = {"id": "oud-begrip", "wijziging": "hernoemd", "datum": "2026-10-05"}
    _schrijf(wiki, "beschikking", _bo(object_van=van))
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    assert _beslissen(wiki).fouten == []
    # een tweede element dat hetzelfde object voortzet
    _schrijf(wiki, "behandelen-aanvraag", _proces(object_van=van))
    assert any("wordt al door 'behandelen-aanvraag' voortgezet" in f or "wordt al door 'beschikking' voortgezet" in f
               for f in beslissen.beslissen(wiki).fouten)
    # het object is zelf nog een element
    _schrijf(wiki, "behandelen-aanvraag", _proces(object_van={**van, "id": "beschikking"}))
    assert any("is zelf nog een element" in f for f in beslissen.beslissen(wiki).fouten)


def _functie_model(wiki):
    """Een GEMMA-model met de functiehiërarchie domein › domeinfunctie › soort › functie."""
    import gam_gemeen

    def el(id_, naam, type_="business-function", gemma_type=None, map_="Business / Bedrijfsfuncties"):
        return {"id": id_, "naam": naam, "type": type_, "documentatie": "", "map": map_, "map_id": "f",
                "eigenschappen": {"GEMMA type": gemma_type} if gemma_type else {}}

    agg = lambda i, bron, doel: {"id": i, "type": "aggregation-relationship", "bron": bron, "doel": doel}  # noqa: E731
    modellen.schrijf_json(
        gam_gemeen.model_json(wiki, "gemma"), "archimate",
        {"elementen": {
            "id-fl": el("id-fl", "Fysieke leefomgeving", "grouping", map_="Other / Domein en doelgroep / Domeinen"),
            "id-uitvoering": el("id-uitvoering", "Uitvoering fysieke leefomgeving", gemma_type="Bedrijfsfunctie domein"),
            "id-exploitatie": el("id-exploitatie", "Exploitatie fysieke leefomgeving", gemma_type="Bedrijfsfunctie"),
            "id-begraafplaatsen": el("id-begraafplaatsen", "Exploiteren van begraafplaatsen"),
            "id-haven": el("id-haven", "Exploiteren van havens"),
            "id-object": el("id-object", "Beschikking", "business-object", map_="Business / Bedrijfsobjecten")},
         "mappen": {}, "model": {}, "relaties": {r["id"]: r for r in (
             agg("id-r0", "id-fl", "id-uitvoering"), agg("id-r1", "id-uitvoering", "id-exploitatie"),
             agg("id-r2", "id-exploitatie", "id-begraafplaatsen"), agg("id-r3", "id-exploitatie", "id-haven"))}})


def test_gemma_functie_wordt_getoetst_en_gerenderd(wiki):
    _functie_model(wiki)
    _schrijf(wiki, "beschikking", _bo())
    functie = _element("Exploiteren van begraafplaatsen", FUNCTIE, domein="Fysieke leefomgeving",
                       gemma={"id": "id-begraafplaatsen", "sterkte": "exact", "onderbouwing": "Zelfde functie."},
                       gemma_functie={"id": "id-exploitatie", "gemma_relatie": "id-r2"})
    _schrijf(wiki, "exploiteren-van-begraafplaatsen", functie)
    dienst = _element("Grafonderhoud", DIENST, domein="Fysieke leefomgeving", afnemer="extern",
                      gemma_functie={"id": "id-exploitatie", "bronnen": [WET], "vindplaats": "art. 23"})
    _schrijf(wiki, "grafonderhoud", dienst)
    res = _beslissen(wiki)
    assert not any("gemma_functie" in f for f in res.fouten)
    functie = _lees(wiki, "exploiteren-van-begraafplaatsen")
    assert functie["beslist"]["gemma_functie"]["gemma_naam"] == "Exploitatie fysieke leefomgeving"
    assert functie["beslist"]["gemma_functie"]["gemma_paden"] == [
        "Fysieke leefomgeving › Uitvoering fysieke leefomgeving › Exploitatie fysieke leefomgeving"]
    pagina = (wiki / functie["beslist"]["pad"]).read_text(encoding="utf-8")
    assert ("**Functie-indeling naar domein, onderdeel van**: GEMMA-functie *Exploitatie fysieke leefomgeving* "
            "(geen element van de wiki; Fysieke leefomgeving › Uitvoering fysieke leefomgeving › Exploitatie fysieke "
            "leefomgeving), GEMMA-relatie `id-r2`.") in pagina
    assert "`id-exploitatie`" not in pagina.split("---")[1]  # geen verwijzing in de frontmatter
    dienstpagina = (wiki / _lees(wiki, "grafonderhoud")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert f"bron: [{WET}]" in dienstpagina or WET in dienstpagina

    # de indelingspagina toont de hiërarchie as-is met de elementen eronder en de dekking
    indeling = (wiki / "elementpaginas/overig/indelingen/bedrijfsfuncties.md").read_text(encoding="utf-8")
    assert "## Fysieke leefomgeving" in indeling
    assert "  - **Exploitatie fysieke leefomgeving**" in indeling
    assert "    - **Exploiteren van begraafplaatsen** → [Exploiteren van begraafplaatsen]" in indeling
    assert "    - Exploiteren van havens" in indeling  # een knoop zonder inhoud staat er ook, as-is
    assert "**dienst** (1): [Grafonderhoud]" in indeling
    assert "Functies: 4; met inhoud van de wiki: 3." in indeling
    assert "## Niveau eigen" in (wiki / "elementpaginas/overig/indelingen/onderwerpen.md").read_text(encoding="utf-8")
    assert (wiki / "elementpaginas/overig/indelingen/beleidsdomeinen.md").exists()
    assert render.main(["--wiki", str(wiki), "--check"]) == 0

    # de plek steunt op de GEMMA-relatie of op een bron, niet op beide; en alleen een functie of dienst
    def fouten(**wijziging):
        _schrijf(wiki, "exploiteren-van-begraafplaatsen", {**_lees(wiki, "exploiteren-van-begraafplaatsen"), **wijziging})
        return beslissen.beslissen(wiki, schrijven=False).fouten

    assert any("niet op beide of geen van beide" in f
               for f in fouten(gemma_functie={"id": "id-exploitatie", "gemma_relatie": "id-r2", "bronnen": [WET],
                                              "vindplaats": "art. 1"}))
    assert any("is geen aggregatie van 'Exploitatie fysieke leefomgeving' naar de GEMMA-match" in f
               for f in fouten(gemma_functie={"id": "id-exploitatie", "gemma_relatie": "id-r3"}))
    assert any("'id-object' is geen bedrijfsfunctie" in f for f in fouten(gemma_functie={"id": "id-object", "gemma_relatie": "id-r2"}))
    assert any("gemma_relatie zonder GEMMA-match" in f for f in fouten(
        gemma_functie={"id": "id-exploitatie", "gemma_relatie": "id-r2"}, gemma={"sterkte": "geen", "onderbouwing": "Nee."}))
    assert any("bronnen zonder vindplaats" in f for f in fouten(gemma_functie={"id": "id-exploitatie", "bronnen": [WET]}))
    _schrijf(wiki, "beschikking", _bo(gemma_functie={"id": "id-exploitatie", "gemma_relatie": "id-r2"}))
    assert any("beschikking: gemma_functie hoort alleen bij een bedrijfsfunctie of dienst" in f
               for f in beslissen.beslissen(wiki, schrijven=False).fouten)


def test_dienst_zonder_grondslag_krijgt_melding_en_staat_op_de_lijst(wiki):
    """Een UPL-dienst zonder landelijke grondslag: `beslist.zonder_grondslag`, een melding op de pagina, de lijst
    elementpaginas/overig/zonder-grondslag.md en een signaal zolang de procesarchitectuur-terugmelding ontbreekt."""
    from llmwiki import sources

    upl = "2025-vng-upl-test"
    origineel = wiki.parent.parent.parent / f"{upl}.md"
    origineel.write_text(f"# {upl}\n", encoding="utf-8")
    sources.add(wiki.parent.parent, upl, origineel, titel=upl, tags=["test"], brontype="informatiemodel")
    pad = wiki / "onderwerpen/test/bronduidingen/informatiemodel" / f"{upl}.md"
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(f"---\nid: {upl}\ntype: bronduiding\nonderwerp: test\nbronnen: [{upl}]\n---\n\n# {upl}\n\n"
                   f"Bron: [tekst](../../../../../../sources/raw/{upl}.md)\n", encoding="utf-8")
    afbakening = beoordeling.laad(wiki / "onderwerpen/test/afbakening.yaml")
    afbakening["bronnen"].append(upl)
    beoordeling.schrijf(wiki / "onderwerpen/test/afbakening.yaml", afbakening)
    dienst = _element("Legaliseren", DIENST, afnemer="extern", domein="Publieksdiensten")
    for k in dienst["kenmerken"].values():
        if k.get("bronnen"):
            k["bronnen"] = [upl]
    dienst["beschrijving"] = ["Een UPL-dienst."]
    _schrijf(wiki, "legaliseren", dienst)
    res = _beslissen(wiki)
    assert _lees(wiki, "legaliseren")["beslist"]["zonder_grondslag"] is True
    assert any(w.startswith("legaliseren: UPL-dienst zonder landelijke grondslag zonder procesarchitectuur-terugmelding")
               for w in res.waarschuwingen)
    pagina = (wiki / _lees(wiki, "legaliseren")["beslist"]["pad"]).read_text(encoding="utf-8")
    assert "**Zonder landelijke wettelijke grondslag.**" in pagina and "nog niet teruggemeld" in pagina
    lijst = (wiki / render.ZONDER_GRONDSLAG).read_text(encoding="utf-8")
    assert "| Test | ontbreekt |" in lijst and "Legaliseren" in lijst
    # een tweede run vindt niets verouderd (de vlag blijft staan)
    assert beslissen.beslissen(wiki, schrijven=False).gewijzigd == []
