"""tools/afleiden.py en tools/render.py: van beoordeling naar status en pagina's."""
import pytest
from test_gam_bepaal_type import (ACTOR, BELEIDSKADER, BO, DIENST, FUNCTIE, GEBEURTENIS, KANAAL, PROCES, PRODUCT, ROL,
                                  SAMENWERKING)

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
    return _element("Beschikking", BO | {"generiek"}, ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}, **extra)


def _proces(**extra) -> dict:
    relatie = {"soort": "toegang (registreren)", "naar": "beschikking", "naam": "stelt vast", "grondslag": "bron",
               "bronnen": [WET], "vindplaats": "art. 2"}
    return _element("Behandelen aanvraag", PROCES, relaties=[relatie], kernobject="beschikking", afnemer="extern",
                    **extra)


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
    assert "#### Inkomend" in pagina
    assert "[Behandelen aanvraag](../../../bedrijfsprocessen/8-wonen/vergunningen/behandelen-aanvraag.md)" in pagina
    assert f"[{WET}](../../../../bronanalyses/test/{WET}.md)" in pagina
    assert "**Status: review.**" in pagina
    lijst = (wiki / "begrippen/test.md").read_text(encoding="utf-8")
    assert "[Beschikking](../bedrijfsarchitectuur/bedrijfsobjecten/8-wonen/vergunningen/beschikking.md)" in lijst
    assert "Behandelen aanvraag" in (wiki / "ter-beoordeling.md").read_text(encoding="utf-8")


def _rel(soort: str, naar: str) -> dict:
    return {"soort": soort, "naar": naar, "grondslag": "bron", "bronnen": [WET], "vindplaats": "art. 3"}


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
    _afleiden(wiki)

    for bid, (paginatype, archimate_type, _) in gevallen.items():
        d = _lees(wiki, bid)
        uitkomst = d["afgeleid"]["uitkomst"]
        assert (uitkomst["soort"], uitkomst["paginatype"], uitkomst["archimate_type"]) == \
            ("element", paginatype, archimate_type), bid
        # Een kanaal wordt altijd voorgelegd (centrale set); de rest is na afleiden klaar voor review.
        assert d["status"] == ("kandidaat" if paginatype == "kanaal" else "review"), (bid, d["afgeleid"].get("open"))
        assert d["afgeleid"]["pad"].startswith(afleiden.paths.load_wiki_yaml(wiki)["page_types"][paginatype]["dir"])
        assert (wiki / d["afgeleid"]["pad"]).exists(), bid
    lijst = (wiki / "begrippen/test.md").read_text(encoding="utf-8")
    assert all(data["begrip"] in lijst for _, _, data in gevallen.values())


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
    (lambda d: d["kenmerken"]["gedrag"].pop("bronnen"), "kenmerk 'ja' zonder bron: gedrag"),
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
    _schrijf(wiki, "aanvraag-behandeling", _element("Aanvraagbehandeling", PROCES, kernobject="beschikking", afnemer="extern"))
    res = afleiden.afleiden(wiki)
    assert res.fouten == []
    assert any("regel Naamvorm" in w and "aanvraag-behandeling" in w for w in res.waarschuwingen)
    assert any("regel Beslistabel beslist" in w and "geregistreerd" in w for w in res.waarschuwingen)


def test_bronanalyse_zonder_bronregel_is_een_fout(wiki):
    pad = wiki / "bronanalyses" / "test" / f"{WET}.md"
    pad.write_text(pad.read_text(encoding="utf-8").replace("Bron: ", "Zie: "), encoding="utf-8")
    _schrijf(wiki, "beschikking", _bo())
    assert any("'Bron:'" in f for f in afleiden.afleiden(wiki).fouten)


def test_element_zonder_enige_bron_is_een_fout(wiki):
    bo = _bo()
    for antwoord in bo["kenmerken"].values():
        antwoord.pop("bronnen", None)
    _schrijf(wiki, "beschikking", bo)
    fouten = afleiden.afleiden(wiki).fouten
    assert any("element zonder bron" in f for f in fouten)
    assert any("kenmerk 'ja' zonder bron" in f for f in fouten)


# --- Stap 7: indeling ---


def _deelproces(**extra) -> dict:
    ja = (PROCES - {"omvat_levensloop"}) | {"bijdrage_aan_groter_proces", "eigen_besluit"}
    return _element("Verlenen grafrecht", ja, kernobject="beschikking", afnemer="extern", **extra)


def test_object_zonder_proces_wordt_voorgelegd_en_een_kernobject_is_een_kernobject(wiki):
    _schrijf(wiki, "graf", _element("Graf", BO, ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}))
    _afleiden(wiki)
    data = _lees(wiki, "graf")
    assert data["status"] == "kandidaat"
    assert any("levensloop" in r for r in data["afgeleid"]["voor_te_leggen"])

    _schrijf(wiki, "beheren-graven", _element("Beheren graven", PROCES, kernobject="graf", afnemer="extern",
                                              relaties=[_rel("toegang (registreren)", "graf")]))
    _afleiden(wiki)
    assert _lees(wiki, "graf")["afgeleid"]["uitkomst"]["objectniveau"] == "kernobject"
    assert _lees(wiki, "graf")["status"] == "review"
    assert _lees(wiki, "beheren-graven")["afgeleid"]["uitkomst"]["procesniveau"] == "bedrijfsproces"


def test_twee_processen_voor_een_kernobject_is_een_fout(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "behandelen-aanvraag", _proces())
    _schrijf(wiki, "beheren", _element("Beheren beschikkingen", PROCES, kernobject="beschikking", afnemer="extern"))
    res = afleiden.afleiden(wiki)
    assert any("per kernobject één proces" in f for f in res.fouten)


def test_indelingsveld_ontbreekt_of_heeft_een_onbekende_waarde(wiki):
    _schrijf(wiki, "beschikking", _bo())
    data = _proces()
    del data["afnemer"]
    _schrijf(wiki, "behandelen-aanvraag", data)
    assert any("zonder 'afnemer'" in f for f in afleiden.afleiden(wiki).fouten)
    data["afnemer"] = "allemaal"
    _schrijf(wiki, "behandelen-aanvraag", data)
    assert any("allemaal" in f for f in afleiden.afleiden(wiki).fouten)  # het schema weigert de waarde


def test_via_moet_een_specialisatie_van_het_doel_zijn(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "verlof", _element("Verlof", BO - {"zelfstandige_specialisatie"}, genoemd_begrip="Beschikking",
                                      ggm={"sterkte": "geen", "onderbouwing": "Niet in het GGM."}))
    proces = _proces()
    proces["relaties"][0]["via"] = "verlof"
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert afleiden.afleiden(wiki).fouten == []
    proces["relaties"][0]["via"] = "beschikking"  # een element, geen specialisatie
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert any("geen specialisatie van dat doel" in f for f in afleiden.afleiden(wiki).fouten)


def test_leidt_tot_gebeurtenis_vraagt_een_triggering(wiki):
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "overlijden", _element("Overlijden", GEBEURTENIS, relaties=[_rel("triggering", "behandelen-aanvraag")]))
    proces = _proces()
    proces["kenmerken"]["leidt_tot_gebeurtenis"] = {"waarde": "ja", "onderbouwing": "Eindigt in een overlijden.", "bronnen": [WET]}
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert any("geen relatie 'triggering' naar een gebeurtenis" in f for f in afleiden.afleiden(wiki).fouten)
    proces["relaties"].append(_rel("triggering", "overlijden"))
    _schrijf(wiki, "behandelen-aanvraag", proces)
    assert afleiden.afleiden(wiki).fouten == []


def test_gemma_generiek_moet_in_het_gemma_model_staan(wiki):
    import gam_gemeen

    gam_gemeen.schrijf_json_gegenereerd(
        wiki / "gemma" / "gemma_parsed.json",
        {"elementen": {"id-vergunning": {"id": "id-vergunning", "naam": "Behandelen aanvraag vergunning of ontheffing",
                                         "type": "business-process", "documentatie": "", "map": "Business", "map_id": "f",
                                         "eigenschappen": {}}}, "mappen": {}, "model": {}, "relaties": {}}, "test")
    _schrijf(wiki, "beschikking", _bo())
    _schrijf(wiki, "behandelen-aanvraag", _proces(gemma_generiek={"id": "id-vergunning", "onderbouwing": "Generiek proces."}))
    assert afleiden.afleiden(wiki).fouten == []
    _schrijf(wiki, "behandelen-aanvraag", _proces(gemma_generiek={"id": "id-weg", "onderbouwing": "Bestaat niet."}))
    assert any("gemma_generiek 'id-weg' bestaat niet" in f for f in afleiden.afleiden(wiki).fouten)


def test_signalen_voor_de_indeling():
    import signalen

    def el(paginatype, **u):
        return {"paginatype": paginatype, "soort": "element", **u}

    elementen = {
        "taak": el("bedrijfsproces", procesniveau="taak"),
        "beheren": el("bedrijfsproces", procesniveau="bedrijfsproces"),
        "los": el("bedrijfsproces", procesniveau="bedrijfsproces"),
        "keten": el("bedrijfsproces", procesniveau="ketenproces"),
        "deel": el("bedrijfsproces", procesniveau="deelproces"),
        "elders": el("bedrijfsproces", procesniveau="deelproces"),
        "wees": el("bedrijfsproces", procesniveau="deelproces"),
        "onderhoud": el("dienst"),
        "wet": el("beleidskader"),
        "gemeente": el("actor"),
        "raad": el("actor"),
        "arts": el("gebeurtenis", generiek=True),
    }
    rel = lambda soort, naar, naam=None: {"soort": soort, "naar": naar, "naam": naam}  # noqa: E731
    alle = {b: {"onderwerpen": ["lijkbezorging" if b != "elders" else "burgerzaken"]} for b in elementen}
    alle["taak"]["relaties"] = [rel("aggregatie", "beheren"), rel("aggregatie", "keten")]
    alle["beheren"]["relaties"] = [rel("aggregatie", "deel")]
    alle["keten"]["relaties"] = [rel("aggregatie", "elders")]
    alle["deel"]["relaties"] = [rel("realisatie", "onderhoud")]
    alle["gemeente"]["relaties"] = [rel("associatie (gericht)", "raad", "geeft melding door aan"),
                                    rel("associatie (gericht)", "raad", "is voorzitter van")]
    relaties = [(van, r) for van in elementen for r in alle[van].get("relaties", [])]
    tekst = "\n".join(signalen.indeling(alle, elementen, relaties))
    assert "los: hangt onder geen taak" in tekst
    assert "wees: deelproces hangt onder geen bedrijfs- of ketenproces" in tekst
    assert "deel: een deelproces levert een dienst" in tekst
    assert "keten: ketenproces met deelproces 'elders' uit een andere taak" in tekst
    assert "wet: geen product heeft dit beleidskader" in tekst
    assert "geeft melding door aan" in tekst and "is voorzitter van" not in tekst
    assert "arts: generiek, maar geen `gemma_generiek`" in tekst
    assert "beheren: hangt onder geen taak" not in tekst and "keten: hangt onder geen taak" not in tekst


def _indeling_wiki(wiki):
    """Een taak met een ketenproces, een deelproces, een kernobject met subobject, een generiek object met
    specialisatie, een functie, een gebeurtenis en een dienst."""
    import gam_gemeen

    gam_gemeen.schrijf_json_gegenereerd(
        wiki / "gemma" / "gemma_parsed.json",
        {"elementen": {"id-vergunning": {"id": "id-vergunning", "naam": "Behandelen aanvraag vergunning of ontheffing",
                                         "type": "business-process", "documentatie": "", "map": "Business", "map_id": "f",
                                         "eigenschappen": {}}}, "mappen": {}, "model": {}, "relaties": {}}, "test")
    geen_ggm = {"ggm": {"sterkte": "geen", "onderbouwing": "Niet in het GGM."}}
    taak = BASIS_TAAK = {"herkenbaar", "gemeentelijk", "eigen_identiteit", "betekenis_in_onderwerp",
                         "zelfstandige_specialisatie", "gedrag", "groepeert_processen", "omvat_processen"}
    keten = PROCES | {"meer_organisaties"}
    deel = (PROCES - {"omvat_levensloop"}) | {"bijdrage_aan_groter_proces", "eigen_besluit"}
    gevallen = {
        "verzorgen-lijkbezorging": _element("Verzorgen lijkbezorging", taak, relaties=[_rel("aggregatie", "bezorgen-lijken")]),
        "bezorgen-lijken": _element("Bezorgen lijken", keten, kernobject="lijk", afnemer="extern",
                                    relaties=[_rel("aggregatie", "opgraven-lijk"), _rel("toegang (registreren)", "lijk")]),
        "opgraven-lijk": _element("Opgraven lijk", deel, kernobject="grafbedekking", afnemer="extern",
                                  gemma_generiek={"id": "id-vergunning", "onderbouwing": "Een vergunningaanvraag."},
                                  relaties=[{**_rel("toegang (registreren)", "vergunning"), "via": "vergunning-tot-opgraving"},
                                            _rel("realisatie", "onderhoud-van-graven")]),
        "lijk": _element("Lijk", BO, relaties=[_rel("compositie", "grafbedekking")], **geen_ggm),
        "grafbedekking": _element("Grafbedekking", BO | {"deel_van_object"}, **geen_ggm),
        "vergunning": _element("Vergunning", BO | {"generiek"}, **geen_ggm),
        "vergunning-tot-opgraving": _element("Vergunning tot opgraving", BO - {"zelfstandige_specialisatie"},
                                             genoemd_begrip="Vergunning", **geen_ggm),
        "onderhoud-van-graven": _element("Onderhoud van graven", DIENST, domein="Fysieke leefomgeving", afnemer="extern"),
        "exploiteren-begraafplaatsen": _element("Exploiteren van begraafplaatsen", FUNCTIE, domein="Fysieke leefomgeving",
                                                relaties=[_rel("bediening", "opgraven-lijk")]),
        "overlijden": _element("Overlijden", GEBEURTENIS, relaties=[_rel("triggering", "bezorgen-lijken")]),
    }
    for bid, data in gevallen.items():
        _schrijf(wiki, bid, data)
    _afleiden(wiki)
    return gevallen


def test_pagina_toont_de_plaats_in_de_indelingen(wiki):
    _indeling_wiki(wiki)
    opgraven = _lees(wiki, "opgraven-lijk")
    assert opgraven["afgeleid"]["uitkomst"]["procesniveau"] == "deelproces"
    pagina = (wiki / opgraven["afgeleid"]["pad"]).read_text(encoding="utf-8")
    assert "procesniveau: deelproces" in pagina and "afnemer: extern" in pagina
    assert "kernobject:" not in pagina.split("---")[1]  # een verwijzing staat niet in de frontmatter
    assert "#### Plaats in de indelingen" in pagina or "### Plaats in de indelingen" in pagina
    assert "**Procesindeling naar taak, onderdeel van**: [Bezorgen lijken]" in pagina
    assert "**Kernobject**: [Grafbedekking]" in pagina
    assert "**Procesindeling naar soort werk, specialisatie van**: GEMMA-element *id-vergunning*" in pagina or \
        "specialisatie van**: GEMMA-element" in pagina
    assert "**Functie-indeling naar domein, bediend door**: [Exploiteren van begraafplaatsen]" in pagina

    keten = (wiki / _lees(wiki, "bezorgen-lijken")["afgeleid"]["pad"]).read_text(encoding="utf-8")
    assert "**Procesniveau**: ketenproces." in keten and "**Gestart door gebeurtenis**: [Overlijden]" in keten
    assert "onderdeel van**: [Verzorgen lijkbezorging]" in keten and "omvat**: [Opgraven lijk]" in keten

    lijk = (wiki / _lees(wiki, "lijk")["afgeleid"]["pad"]).read_text(encoding="utf-8")
    assert "objectniveau: kernobject" in lijk and "**Levensloop bepaald door**: [Bezorgen lijken]" in lijk
    bedekking = (wiki / _lees(wiki, "grafbedekking")["afgeleid"]["pad"]).read_text(encoding="utf-8")
    assert "objectniveau: subobject" in bedekking and "**Subobject van**: [Lijk]" in bedekking
    assert "**Mutaties door deelprocessen**: [Opgraven lijk]" in bedekking

    vergunning = (wiki / _lees(wiki, "vergunning")["afgeleid"]["pad"]).read_text(encoding="utf-8")
    assert "objectniveau: generiek" in vergunning and "Specialisaties per onderwerp" in vergunning
    assert "**Vergunning tot opgraving**" in vergunning and "Genoemd door [Opgraven lijk]" in vergunning


def test_overzicht_per_onderwerp_toont_de_views(wiki):
    _indeling_wiki(wiki)
    overzicht = (wiki / "overzichten" / "test.md").read_text(encoding="utf-8")
    assert "## Procesindeling naar taak" in overzicht
    assert "- [Verzorgen lijkbezorging](" in overzicht
    assert "  - [Bezorgen lijken](" in overzicht and "*(ketenproces, afnemer extern)*" in overzicht
    assert "    - [Opgraven lijk](" in overzicht and "bediend door [Exploiteren van begraafplaatsen]" in overzicht
    assert "levert [Onderhoud van graven]" in overzicht
    assert "## Ketens" in overzicht and "deelprocessen [Opgraven lijk]" in overzicht
    assert "## Procesindeling naar soort werk" in overzicht
    assert "## Gebeurtenissen" in overzicht and "| [Overlijden](" in overzicht
    assert "**Kernobjecten**" in overzicht and "subobjecten [Grafbedekking]" in overzicht
    assert "**Generiek**" in overzicht and "[Vergunning]" in overzicht
    assert "## Functies" in overzicht and "## Producten en diensten" in overzicht
    lijst = (wiki / "begrippen" / "test.md").read_text(encoding="utf-8")
    assert "overzichten/test.md" in lijst
    assert render.main(["--wiki", str(wiki), "--check"]) == 0
