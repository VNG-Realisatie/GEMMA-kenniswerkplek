"""Beslistabel (plan 2026-10-18): vier fasen, zeven stappen; keuzekenmerken, toetskenmerken, afbakenen, typeren, indelen."""
import json
import sys
from pathlib import Path

import jsonschema
import pytest

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import bepaal_type as bt  # noqa: E402
from gam_hulp import maak  # noqa: E402

WIKI = TOOLS.parent


def beoordeling(ja: set[str], **extra) -> dict:
    """Een beoordeling uit de kenmerken met ja (zie gam_hulp.maak)."""
    return maak(ja, **extra)


SCOPE = {"herkenbaar", "gemeentelijk"}
BASIS = SCOPE | {"betekenis_in_onderwerp"}
BO = BASIS | {"object", "wordt_bewerkt", "onderscheidbare_exemplaren", "levenscyclus"}
ACTOR = BASIS | {"handelende_partij", "vervult_een_rol", "soort_partij"}
ROL = BASIS | {"hoedanigheid", "voert_gedrag_uit"}
PROCES = BASIS | {"gedrag", "per_keer_doorlopen", "toegewezen_partij", "aanleiding", "benoembaar_resultaat"}
CLUSTER = BASIS | {"gedrag", "per_keer_doorlopen", "omvat_processen"}
FUNCTIE = BASIS | {"gedrag", "gegroepeerd_gedrag", "bedient_gedrag", "gebruikt_objecten", "stabiel_over_tijd",
                   "in_functie_indeling"}
DIENST = BASIS | {"gedrag", "aangeboden_gedrag", "gerealiseerd_door", "afnemer", "benoembaar_resultaat"}
GEBEURTENIS = BASIS | {"gedrag", "toestandsverandering", "leidt_tot_gedrag", "komt_herhaald_voor"}
PRODUCT = BASIS | {"aanbod_als_geheel", "omvat_diensten_en_afspraken", "afnemer", "benoembaar_resultaat",
                   "zelfstandig_aanbod"}
SAMENWERKING = BASIS | {"samenwerkingsverband", "voert_gedrag_uit", "soort_partij"}
KANAAL = BASIS | {"toegangspunt", "ontsluit_een_dienst"}
BELEIDSKADER = BASIS | {"regeling_als_geheel", "landelijk", "in_werking", "is_grondslag_voor"}
CAPABILITY = BASIS | {"vermogen", "gerealiseerd_door", "beoordeelbaar", "onderscheidend", "stabiel_over_tijd"}
TWEE_FUNCTIES = ["bevolkingsadministratie-bijhouding", "burgerlijke-stand-diensten"]


def capability(ja: set[str] = CAPABILITY, naar: list = TWEE_FUNCTIES) -> dict:
    """Een capability-beoordeling waarvan *gerealiseerd door* de functies in `naar` noemt."""
    b = beoordeling(ja)
    if "gerealiseerd_door" in ja:
        b["kenmerken"]["gerealiseerd_door"]["naar"] = naar
    return b


def test_elke_regel_van_stap_0_tot_3_heeft_een_geval():
    gevallen = [
        beoordeling(BO, synoniem_van="Urn"),
        beoordeling(set()),
        beoordeling(SCOPE | {"buiten_dit_model", "betekenis_in_onderwerp"}),
        beoordeling(SCOPE),
        beoordeling(BASIS, afhankelijkheid="eigenschap", genoemd_begrip="Pand"),
        beoordeling(BASIS, afhankelijkheid="onderdeel", genoemd_begrip="Besluit"),
        beoordeling(BASIS, afhankelijkheid="deelproces", genoemd_begrip="Behandelen aanvraag"),
        beoordeling(BASIS, afhankelijkheid="invoer_van_een_ander", genoemd_begrip="Verlenen verlof"),
        beoordeling(BASIS, afhankelijkheid="variant", genoemd_begrip="Vergunning"),
        {**beoordeling(PROCES), "vak": "bedrijf/passief", "hoofdkenmerk": "gedrag"},
        beoordeling(SAMENWERKING),
        beoordeling(ACTOR),
        beoordeling(ROL),
        beoordeling(PRODUCT),
        beoordeling(KANAAL),
        beoordeling(BASIS | {"plaats"}),
        beoordeling(BELEIDSKADER),
        capability(),
        beoordeling(PROCES),
        beoordeling(BASIS | {"representatie"}, genoemd_begrip="Aanslag"),
        beoordeling(BO - {"object"} | {"afspraak"}),
        beoordeling(BO),
    ]
    assert len(gevallen) == len(bt.REGELS)
    for nr, b in enumerate(gevallen, start=1):
        u = bt.evalueer(b)
        assert (u.typeregel or u.regel) == nr, (nr, u)


def test_stap_0_synoniem_en_homoniem():
    u = bt.evalueer(beoordeling(BO, synoniem_van="Urn"))
    assert (u.soort, u.genoemd_begrip, u.paginatype) == ("synoniem", "Urn", None)
    u = bt.evalueer(beoordeling(BO, homoniem_van="Regeling (GGM Inkomen)"))
    assert u.soort == "element" and u.voorleggen and any("naamkeuze" in r for r in u.redenen)
    assert bt.voorgestelde_status(u) == "review"   # voorgelegd bij het akkoord, geen eigen status


def test_stap_1_scope_is_een_afwijking():
    """Zonder antwoord is de scope doorlopen; een afwijking laat het begrip afvallen."""
    assert bt.evalueer(beoordeling(BO)).soort == "element"
    assert bt.evalueer(beoordeling(BO - {"betekenis_in_onderwerp"})).soort == "verwijzing"
    assert bt.evalueer(beoordeling(BO - {"gemeentelijk"})).soort == "buiten_scope"
    assert bt.evalueer(beoordeling(BO | {"buiten_dit_model"}, archimate_buiten_model="Goal")).soort == "buiten_model"
    b = beoordeling(BO)
    assert not {"herkenbaar", "gemeentelijk", "betekenis_in_onderwerp"} & set(b["kenmerken"])


def test_stap_2_afhankelijkheid_is_een_keuzekenmerk():
    for waarde, soort, atype in [("eigenschap", "eigenschap", None), ("onderdeel", "onderdeel", None),
                                 ("deelproces", "onderdeel", "business-process"),
                                 ("invoer_van_een_ander", "onderdeel", None),
                                 ("variant", "specialisatie", None)]:
        u = bt.evalueer(beoordeling(BASIS, afhankelijkheid=waarde, genoemd_begrip="Inwoner"))
        assert (u.soort, u.genoemd_begrip, u.archimate_type, u.paginatype) == (soort, "Inwoner", atype, None), waarde
        assert not u.voorleggen
        assert bt.evalueer(beoordeling(BASIS, afhankelijkheid=waarde)).voorleggen  # zonder genoemd begrip
    # de afwijking gaat vóór het type: een variant krijgt de kenmerken van het type niet
    assert bt.evalueer(beoordeling(BASIS | {"gedrag"}, afhankelijkheid="variant", genoemd_begrip="X")).soort == "specialisatie"
    # een keuzekenmerk heeft een onderbouwing
    b = beoordeling(BASIS, afhankelijkheid="variant", genoemd_begrip="X")
    b["kenmerken"]["afhankelijkheid"]["onderbouwing"] = ""
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("keuzekenmerk 'afhankelijkheid': onderbouwing ontbreekt" in f for f in exc.value.fouten)
    b["kenmerken"]["afhankelijkheid"] = {"waarde": "onbekend", "onderbouwing": "x"}
    with pytest.raises(bt.BeoordelingFout):
        bt.evalueer(b)


def test_stap_3_consistentie_kenmerken_passen_bij_de_aard():
    # Gedragskenmerk bij een ding
    assert bt.evalueer(beoordeling(BO | {"aanleiding"})).soort == "conflict"
    # Afspraak naast gedrag
    assert bt.evalueer({**beoordeling(PROCES), "vak": "bedrijf/passief", "hoofdkenmerk": "afspraak"}).soort == "conflict"
    # Partijkenmerk zonder partij
    assert bt.evalueer(beoordeling(BO | {"voert_gedrag_uit"})).soort == "conflict"
    # Beleidskaderkenmerk zonder regeling
    assert bt.evalueer(beoordeling(BO | {"landelijk"})).soort == "conflict"
    # Objectkenmerken bij een partij
    assert bt.evalueer(beoordeling(ACTOR | {"wordt_bewerkt"})).soort == "conflict"
    # Afnemer en resultaat mogen bij een product
    assert bt.evalueer(beoordeling(PRODUCT)).paginatype == "product"


def test_stap_5_elk_toetskenmerk_moet_ja_zijn():
    gevallen = [(BO, "wordt_bewerkt"), (PROCES, "toegewezen_partij"), (PROCES, "aanleiding"), (FUNCTIE, "bedient_gedrag"),
                (DIENST, "gerealiseerd_door"), (GEBEURTENIS, "leidt_tot_gedrag"), (ACTOR, "vervult_een_rol"),
                (ROL, "voert_gedrag_uit"), (PRODUCT, "omvat_diensten_en_afspraken"), (SAMENWERKING, "voert_gedrag_uit"),
                (KANAAL, "ontsluit_een_dienst"), (BELEIDSKADER, "is_grondslag_voor"), (CAPABILITY, "gerealiseerd_door"),
                # de andere toetskenmerken zijn standaard ja; een nee wordt voorgelegd
                (BO, "levenscyclus"), (BO, "onderscheidbare_exemplaren"), (PROCES, "benoembaar_resultaat"),
                (FUNCTIE, "stabiel_over_tijd"), (FUNCTIE, "gebruikt_objecten"), (DIENST, "afnemer"),
                (GEBEURTENIS, "komt_herhaald_voor"), (PRODUCT, "zelfstandig_aanbod"), (BELEIDSKADER, "in_werking"),
                (CAPABILITY, "beoordeelbaar"), (CAPABILITY, "onderscheidend"), (CAPABILITY, "stabiel_over_tijd")]
    for ja, kenmerk in gevallen:
        u = bt.evalueer(capability(ja - {kenmerk}) if ja is CAPABILITY else beoordeling(ja - {kenmerk}))
        assert (u.soort, u.regel, u.voorleggen) == ("geen_element", bt.EERSTE_TOETSREGEL, True), kenmerk
        assert f"{bt.NAAM[kenmerk]}: nee" in u.redenen


def test_standaardantwoord_hoeft_niet_te_worden_geschreven():
    """Een toetskenmerk dat geen relatie is, is standaard ja: de beoordeling schrijft alleen een nee."""
    b = beoordeling(BO)
    b["kenmerken"] = {s: a for s, a in b["kenmerken"].items() if s not in ("onderscheidbare_exemplaren", "levenscyclus")}
    assert bt.evalueer(b).soort == "element"
    b["kenmerken"]["levenscyclus"] = {"waarde": "nee", "onderbouwing": "Eén exemplaar."}
    assert bt.evalueer(b).soort == "geen_element"
    # een relatiekenmerk heeft altijd een antwoord
    b = beoordeling(BO)
    del b["kenmerken"]["wordt_bewerkt"]
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("op het pad niet beantwoord: wordt bewerkt" in f for f in exc.value.fouten)
    # een capability beantwoordt zijn toetskenmerken expliciet, ook *stabiel over tijd*
    c = capability()
    del c["kenmerken"]["stabiel_over_tijd"]
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(c)
    assert any("stabiel over tijd" in f for f in exc.value.fouten)


def test_soort_partij_hoort_bij_typeren():
    """Een partij die niet voor alle gemeenten geldt, valt af in stap 3, vóór de toetskenmerken."""
    for ja in (ACTOR, SAMENWERKING):
        u = bt.evalueer(beoordeling(ja - {"soort_partij", "vervult_een_rol", "voert_gedrag_uit"}))
        assert (u.soort, u.regel, u.voorleggen) == ("geen_element", bt.EERSTE_NIVEAUREGEL, True)
        assert u.redenen == ["soort partij: nee"]


def test_capability_in_vak_strategie():
    """Een vermogen is een capability in het vak strategie; een functie of proces met *vermogen* is een conflict."""
    b = capability()
    assert (b["vak"], "hoofdkenmerk" in b) == ("strategie/gedrag", False)
    u = bt.evalueer(b)
    assert (u.soort, u.paginatype, u.archimate_type) == ("element", "capability", "capability")
    assert bt.evalueer({**capability(), "vak": "bedrijf/gedrag-intern", "hoofdkenmerk": "vermogen"}).soort \
        == "conflict"
    assert bt.evalueer(capability(CAPABILITY | {"aanleiding"})).soort == "conflict"


def test_capability_alleen_bij_bundeling_van_ten_minste_twee_functies():
    """K3: een capability die samenvalt met één functie is geen element; de functie volstaat. Een nog niet bestaande
    functie (naam en type) telt mee, een ander type niet."""
    for naar in (TWEE_FUNCTIES[:1], [{"naam": "Verkiezingen", "type": "bedrijfsproces"}, TWEE_FUNCTIES[0]]):
        u = bt.evalueer(capability(naar=naar))
        assert (u.soort, u.regel, u.voorleggen) == ("geen_element", bt.EERSTE_TOETSREGEL, True)
        assert any("minder dan 2 bedrijfsfuncties" in r for r in u.redenen)
    nieuw = {"naam": "Identiteitvaststelling", "type": "bedrijfsfunctie"}
    assert bt.evalueer(capability(naar=[TWEE_FUNCTIES[0], nieuw])).soort == "element"
    assert bt.evalueer(capability(naar=TWEE_FUNCTIES + ["officiele-documenten-verstrekking"])).paginatype == "capability"


def test_actor_rol_en_samenwerking():
    assert bt.evalueer(beoordeling(ROL)).paginatype == "rol"
    assert bt.evalueer(beoordeling(ACTOR)).paginatype == "actor"
    # *los van verantwoordelijkheid* volgt uit het hoofdkenmerk; alleen een afwijking staat in de beoordeling
    assert "los_van_verantwoordelijkheid" not in beoordeling(ACTOR)["kenmerken"]
    assert bt.evalueer(beoordeling(ACTOR, nee=("los_van_verantwoordelijkheid",))).soort == "conflict"
    assert bt.evalueer(beoordeling(ROL | {"los_van_verantwoordelijkheid"})).soort == "conflict"
    # GGD: altijd een samenwerkingsverband, met eigen rechtspersoon → actor
    ggd = bt.evalueer(beoordeling(BASIS | {"samenwerkingsverband", "eigen_rechtspersoon", "vervult_een_rol",
                                           "soort_partij"}))
    assert ggd.paginatype == "actor"
    # Zorg- en Veiligheidshuis: zonder eigen rechtspersoon → bedrijfssamenwerking
    assert bt.evalueer(beoordeling(SAMENWERKING)).paginatype == "bedrijfssamenwerking"


def test_kanaal_wordt_altijd_voorgelegd():
    u = bt.evalueer(beoordeling(KANAAL))
    assert u.paginatype == "kanaal" and u.voorleggen and bt.voorgestelde_status(u) == "review"


def test_regeling_landelijk_of_bron():
    assert bt.evalueer(beoordeling(BELEIDSKADER)).paginatype == "beleidskader"
    assert bt.evalueer(beoordeling(BELEIDSKADER - {"landelijk"})).soort == "bron"
    # De soort regeling is een bedrijfsobject
    assert bt.evalueer(beoordeling(BO)).archimate_type == "business-object"


def test_geen_pagina_en_herkend():
    vorm = bt.evalueer(beoordeling(BASIS | {"representatie"}, genoemd_begrip="Graf"))
    assert (vorm.soort, vorm.archimate_type, vorm.paginatype, vorm.voorleggen) == ("geen_pagina", "representation", None, False)
    assert bt.evalueer(beoordeling(BASIS | {"representatie"})).voorleggen  # zonder genoemd object
    plaats = bt.evalueer(beoordeling(BASIS | {"plaats"}))
    assert (plaats.soort, plaats.archimate_type, plaats.voorleggen) == ("geen_pagina", "location", False)
    for u in (vorm, plaats):
        assert bt.voorgestelde_status(u) is None


def test_hoofdkenmerk_bij_een_ding():
    """Het passieve vak kent object, afspraak en representatie."""
    assert bt.evalueer(beoordeling(BO)).archimate_type == "business-object"
    assert bt.evalueer(beoordeling(BO - {"object"} | {"afspraak"})).archimate_type == "contract"
    b = beoordeling(BO)
    del b["hoofdkenmerk"]
    assert "hoofdkenmerk" in " ".join(bt.controleer(b))


def test_bedrijfsinteractie_is_een_element_met_een_interactievorm():
    """Een ketensamenwerking is een bedrijfsinteractie: een pagina met een kernobject en een interactievorm (estafette
    of orkestratie); voorleggen alleen bij twijfel."""
    keten = BASIS | {"gedrag", "gezamenlijk_gedrag", "toegewezen_partij", "aanleiding", "benoembaar_resultaat"}
    u = bt.evalueer(beoordeling(keten, kernobject="stoffelijk-overschot"))
    assert (u.soort, u.paginatype, u.archimate_type) == ("element", "bedrijfsinteractie", "business-interaction")
    assert not u.voorleggen and bt.voorgestelde_status(u) == "review"
    assert any("kernobject ontbreekt" in r for r in bt.evalueer(beoordeling(keten)).redenen)
    assert bt.evalueer(beoordeling(keten - {"toegewezen_partij"})).soort == "geen_element"
    b = beoordeling(keten, kernobject="x")
    del b["kenmerken"]["interactievorm"]
    assert any("interactievorm" in f for f in bt.controleer(b))
    assert bt.evalueer(beoordeling(keten, kernobject="x", interactievorm="orkestratie")).soort == "element"


def test_aanvullingen():
    data_object = bt.evalueer(beoordeling(BO))
    assert bt.REDEN_GEEN_GGM in bt.voor_te_leggen(data_object, [{"ggm_sterkte": "partieel"}])
    assert bt.REDEN_GEEN_GGM not in bt.voor_te_leggen(data_object, [{"ggm_sterkte": "sterk"}])
    assert not bt.voor_te_leggen(data_object)   # geen data-object: geen GGM nodig
    assert bt.voorgestelde_status(data_object, ggm_match="partieel") == "review"
    besluit = {"datum": "2026-10-01", "besluit": "Keuze.", "gevolg": "verwerkt"}
    assert bt.voorgestelde_status(data_object, besluiten=[besluit, {**besluit, "gevolg": "afwijzen"}]) == "afgewezen"
    assert bt.voorgestelde_status(data_object, besluiten=[{**besluit, "gevolg": "afwijzen"}, besluit]) == "review"


def test_een_kenmerk_dat_niet_bij_het_type_hoort_wordt_geweigerd():
    """De annotaties van het proces (eigen besluit, levert aanbod …) en de tegenhanger-kenmerken bestaan niet meer."""
    b = beoordeling(PROCES)
    b["kenmerken"]["eigen_besluit"] = {"waarde": "ja", "onderbouwing": "x"}
    assert any("onbekend kenmerk 'eigen_besluit'" in f for f in bt.controleer(b))
    b = beoordeling(ACTOR)
    b["kenmerken"]["levenscyclus"] = {"waarde": "ja", "onderbouwing": "x"}
    assert bt.evalueer(b).soort == "conflict"   # een kenmerk van een object bij een partij
    b = beoordeling(ROL)
    b["kenmerken"]["aanleiding"] = {"waarde": "nee", "onderbouwing": "x"}
    assert any("niet bij het type Rol" in f for f in bt.controleer(b))


def test_onvolledige_beoordeling_wordt_geweigerd():
    b = beoordeling(SCOPE)
    b["kenmerken"]["betekenis_in_onderwerp"]["onderbouwing"] = ""
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("onderbouwing" in f for f in exc.value.fouten)
    b = beoordeling(BO)
    del b["vak"]
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("keuzeveld `vak` ontbreekt" in f for f in exc.value.fouten)


def test_vak_en_hoofdkenmerk_in_conflict():
    u = bt.evalueer({**beoordeling(ROL), "vak": "bedrijf/passief"})
    assert u.soort == "conflict" and "past niet bij het vak" in u.redenen[0]
    u = bt.evalueer({**beoordeling(PROCES), "vak": "bedrijf/gedrag-extern"})
    assert u.soort == "conflict" and "per keer doorlopen" in u.redenen[0]
    assert bt.vak_bij("gedrag", "aangeboden_gedrag") == "bedrijf/gedrag-extern"
    assert bt.hoofdkenmerk({"vak": "bedrijf/gedrag-extern"}) == "gedrag"
    assert bt.soort_gedrag({"vak": "bedrijf/gedrag-extern"}) == "aangeboden_gedrag"
    assert bt.hoofdkenmerk({"vak": "bedrijf/actief-intern"}) is None


def _op_pad(b: dict) -> dict:
    """De beoordeling met alleen wat de beslistabel leest: het pad, de ja's en de nee die een afwijking is."""
    a, f = bt.pad(bt.waarden(b), bt.extra_velden(b))
    return {**b, "kenmerken": {s: x for s, x in b["kenmerken"].items()
                               if s in a + f or x["waarde"] == "ja" or s in bt.STANDAARD}}


@pytest.mark.parametrize("ja", [BO, ACTOR, ROL, PROCES, FUNCTIE, DIENST, GEBEURTENIS, PRODUCT, SAMENWERKING, KANAAL,
                                BELEIDSKADER, SCOPE, SCOPE | {"buiten_dit_model", "betekenis_in_onderwerp"},
                                BASIS | {"plaats"}, BASIS | {"representatie"}, BASIS | {"regeling_als_geheel"}])
def test_buiten_het_pad_leidt_het_script_het_standaardantwoord_af(ja):
    b = beoordeling(ja, genoemd_begrip="Graf", kernobject="Graf", afnemer="extern")
    kort = _op_pad(b)
    assert bt.evalueer(kort) == bt.evalueer(b)


def test_pad_per_fase():
    a, f = bt.pad(bt.waarden(beoordeling(PROCES)), bt.extra_velden(beoordeling(PROCES)))
    assert a[-1] == "procesniveau" and "afhankelijkheid" in a
    assert f == ["toegewezen_partij", "aanleiding", "benoembaar_resultaat", "generiek"]
    b = beoordeling(BO)
    a, f = bt.pad(bt.waarden(b), bt.extra_velden(b))
    assert a[-1] == "afhankelijkheid" and f[0] == "wordt_bewerkt"
    b = beoordeling(SCOPE | {"buiten_dit_model", "betekenis_in_onderwerp"})
    assert bt.pad(bt.waarden(b), bt.extra_velden(b)) == (["herkenbaar", "gemeentelijk", "buiten_dit_model", "afhankelijkheid"], [])
    b = beoordeling(set())
    assert bt.pad(bt.waarden(b), bt.extra_velden(b)) == (["herkenbaar", "gemeentelijk", "afhankelijkheid"], [])
    b = beoordeling(ACTOR)
    a, f = bt.pad(bt.waarden(b), bt.extra_velden(b))
    assert a[-2:] == ["soort_partij", "los_van_verantwoordelijkheid"] and f[0] == "vervult_een_rol"
    assert bt.pad(bt.waarden(beoordeling(BO)), {"synoniem_van": "Graf"}) == ([], [])


def test_kale_nee_en_keuze_als_kenmerk_worden_geweigerd():
    b = beoordeling(PROCES)
    b["kenmerken"]["gebruikt_objecten"] = "nee"
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("normaliseer" in f for f in exc.value.fouten)
    b = beoordeling(PROCES)
    b["kenmerken"]["gedrag"] = {"waarde": "ja", "onderbouwing": "Iets wat gedaan wordt."}
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("keuze" in f and "hoofdkenmerk" in f for f in exc.value.fouten)


def test_naar_bij_een_relatiekenmerk():
    b = beoordeling(PROCES)
    b["kenmerken"]["toegewezen_partij"] = {"waarde": "ja", "naar": ["houder"]}   # bron uit de relatie (beslissen)
    assert bt.evalueer(b).paginatype == "bedrijfsproces"
    b["kenmerken"]["toegewezen_partij"] = {"waarde": "ja", "naar": [{"naam": "Houder", "type": "rol"}]}
    with pytest.raises(bt.BeoordelingFout) as exc:   # een tegenpartij die geen element is: onderbouwing en bron
        bt.evalueer(b)
    assert any("onderbouwing ontbreekt" in f for f in exc.value.fouten)
    b["kenmerken"]["toegewezen_partij"] = {"waarde": "ja", "naar": ["houder"]}
    b["kenmerken"]["benoembaar_resultaat"] = {"waarde": "ja", "naar": ["wet"], "onderbouwing": "x"}
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("alleen bij een relatiekenmerk" in f for f in exc.value.fouten)
    alle = {"p": {"relaties": []}, "houder": {"relaties": [{"soort": "toewijzing", "naar": "p", "bronnen": ["x"]}]}}
    assert bt.steunt_op_relatie("p", "toegewezen_partij", {"waarde": "ja", "naar": ["houder"]}, alle)
    assert not bt.steunt_op_relatie("p", "gebruikt_objecten", {"waarde": "ja", "naar": ["houder"]}, alle)


def test_schema_keuzevelden_en_naar():
    validator = jsonschema.Draft202012Validator(bt.schema())
    b = {**_op_pad(beoordeling(PROCES)), "onderwerpen": ["test"]}
    assert not list(validator.iter_errors(b))
    for fout in ({"plaats": "nee"}, {"gedrag": {"waarde": "ja", "onderbouwing": "x"}},
                 {"toegewezen_partij": {"waarde": "ja", "naar": [{"naam": "Houder"}]}},
                 {"afhankelijkheid": {"waarde": "ja", "onderbouwing": "x"}},
                 {"procesniveau": {"waarde": "klant", "onderbouwing": "x"}}):
        assert list(validator.iter_errors({**b, "kenmerken": {**b["kenmerken"], **fout}})), fout
    assert list(validator.iter_errors({**b, "vak": "bedrijf/onbekend"}))
    goed = {"toegewezen_partij": {"waarde": "ja", "naar": ["houder", {"naam": "Houder", "type": "rol"}]}}
    assert not list(validator.iter_errors({**b, "kenmerken": {**b["kenmerken"], **goed}}))


def test_vragen_per_fase():
    nieuw = "\n".join(bt.vragen(None))
    assert nieuw.startswith("Afbakenen") and "`herkenbaar`" in nieuw and "`per_keer_doorlopen`" in nieuw
    assert "`bedrijf/gedrag-intern`" in nieuw and "Soort gedrag (`soort_gedrag`)" in nieuw and "normaliseer" in nieuw
    assert "`afhankelijkheid`" in nieuw and "`variant`" in nieuw
    b = beoordeling(BO)
    tekst = "\n".join(bt.vragen({**b, "kenmerken": {}}))
    assert tekst.startswith("Onderbouwen, Bedrijfsobject") and "`wordt_bewerkt` †" in tekst
    assert "(standaard ja)" not in tekst   # een standaardantwoord wordt niet gevraagd
    tekst = "\n".join(bt.vragen(paginatype="bedrijfsobject"))
    assert "`levenscyclus` (standaard ja)" in tekst and "`generiek`" in tekst
    assert bt.vragen(b)[0].startswith("Alle kenmerken op het pad")
    assert "\n".join(bt.vragen({**b, "vak": None})).startswith("Afbakenen")
    onderdeel = beoordeling(BASIS, afhankelijkheid="onderdeel", genoemd_begrip="Graf")
    assert bt.vragen(onderdeel)[0].startswith("Geen Onderbouwen: uitkomst onderdeel")
    assert "`omvat_processen`" in "\n".join(bt.vragen(paginatype="procescluster"))
    with pytest.raises(ValueError):
        bt.vragen(paginatype="onbekend")
    # een proces vraagt eerst het niveau
    p = beoordeling(PROCES)
    del p["kenmerken"]["procesniveau"]
    assert "`procesniveau`" in "\n".join(bt.vragen(p)) and "`levensloopproces`" in "\n".join(bt.vragen(p))


def test_elk_kenmerk_telt_ergens():
    gebruikt = set()
    for t in bt.TYPEN:
        gebruikt |= set(t.bep) | set(t.toets)
    gebruikt |= {k.sleutel for k in bt.KENMERKEN if k.groep in ("Scope", "Indeling", "Partij en regeling")}
    assert set(bt.SLEUTELS) - gebruikt == set()


def test_gegenereerd_schema_is_actueel_en_geldig():
    opgeslagen = json.loads((WIKI / "schemas" / "beoordeling.schema.json").read_text(encoding="utf-8"))
    assert opgeslagen == bt.schema(), "draai: uv run python tools/bepaal_type.py schema --schrijf"
    jsonschema.Draft202012Validator(opgeslagen).validate({**beoordeling(BO), "onderwerpen": ["test"]})


def test_procesniveau_is_een_keuzekenmerk():
    proces = bt.evalueer(beoordeling(PROCES, kernobject="grafrecht", afnemer="extern"))
    assert (proces.procesniveau, proces.voorleggen, proces.regel) == ("levensloopproces", False, bt.EERSTE_INDELINGSREGEL + 1)
    zonder = bt.evalueer(beoordeling(PROCES))
    assert zonder.voorleggen and any("kernobject" in r for r in zonder.redenen)
    u = bt.evalueer(beoordeling(PROCES, niveau="bedrijfsproces", kernobject="grafrecht", afnemer="extern"))
    assert (u.procesniveau, u.voorleggen, u.regel) == ("bedrijfsproces", False, bt.EERSTE_INDELINGSREGEL + 2)
    # het niveau is verplicht voor een proces dat een element wordt; zonder niveau toetst het script het bedrijfsproces
    b = beoordeling(PROCES)
    del b["kenmerken"]["procesniveau"]
    assert any("procesniveau" in f for f in bt.controleer(b))
    b = beoordeling(PROCES - {"aanleiding"})
    del b["kenmerken"]["procesniveau"]
    assert bt.controleer(b) == [] and bt.evalueer(b).soort == "geen_element"


def test_deelproces_is_een_afhankelijkheid():
    stap = bt.evalueer(beoordeling(BASIS, afhankelijkheid="deelproces", genoemd_begrip="Behandelen aanvraag reisdocument"))
    assert (stap.soort, stap.genoemd_begrip, stap.voorleggen, stap.archimate_type) == (
        "onderdeel", "Behandelen aanvraag reisdocument", False, "business-process")
    assert bt.evalueer(beoordeling(BASIS, afhankelijkheid="deelproces")).voorleggen  # zonder genoemd begrip


def test_procescluster_is_een_procesniveau():
    # een groepering zonder soort werk is een taak, en de taak is geen procesniveau (besluit 2026-10-08)
    taak = bt.evalueer(beoordeling(CLUSTER, niveau="cluster naar soort werk"))
    assert (taak.paginatype, taak.procesniveau, taak.voorleggen) == ("bedrijfsproces", None, True)
    assert any("taak is geen procesniveau" in r for r in taak.redenen)
    soort_werk = bt.evalueer(beoordeling(CLUSTER, niveau="cluster naar soort werk",
                                         gemma_generiek={"id": "id-1", "onderbouwing": "GEMMA-proces."}))
    assert soort_werk.procesniveau == "cluster naar soort werk" and not soort_werk.voorleggen
    # het cluster heeft de toetskenmerken van een Procescluster, niet die van een bedrijfsproces
    u = bt.evalueer(beoordeling(CLUSTER - {"omvat_processen"}, niveau="cluster naar soort werk"))
    assert (u.soort, u.regel) == ("geen_element", bt.EERSTE_TOETSREGEL)
    assert bt.typedef("bedrijfsproces", "business-process", "cluster naar soort werk").toets == ("omvat_processen",)
    # een cluster is gedrag intern
    assert bt.evalueer({**beoordeling(CLUSTER, niveau="cluster naar soort werk"), "vak": "bedrijf/gedrag-extern"}).soort == "conflict"


def test_objectniveau_per_begrip():
    assert bt.evalueer(beoordeling(BO | {"generiek"})).objectniveau == "generiek"
    invoer = bt.evalueer(beoordeling(BASIS, afhankelijkheid="invoer_van_een_ander", genoemd_begrip="Verlenen verlof"))
    assert (invoer.soort, invoer.genoemd_begrip) == ("onderdeel", "Verlenen verlof")
    for soort in (GEBEURTENIS, ROL, DIENST):
        assert bt.evalueer(beoordeling(soort | {"generiek"})).generiek
    assert not bt.evalueer(beoordeling(GEBEURTENIS)).generiek


def _bo_uitkomsten(**kenmerken):
    """Beoordelingen en uitkomsten voor `indeling`: elk argument is `id=(kenmerken, extra)`."""
    beoordelingen = {i: beoordeling(ja, begrip=i.capitalize(), **extra) for i, (ja, extra) in kenmerken.items()}
    return beoordelingen, {i: bt.asdict(bt.evalueer(b)) for i, b in beoordelingen.items()}


def test_indeling_kernobject_subobject_onderdeel():
    beoordelingen, uitkomsten = _bo_uitkomsten(
        grafrecht=(BO, {}),
        beheren=(PROCES, {"kernobject": "grafrecht"}),
        verlenen=(PROCES, {"kernobject": "bedekking", "niveau": "bedrijfsproces"}),
        bedekking=(BO, {"afhankelijkheid": "onderdeel", "genoemd_begrip": "Graf"}),
        stoep=(BO, {"afhankelijkheid": "onderdeel", "genoemd_begrip": "Graf"}),
        losse=(BO, {}),
        besluit=(BO | {"generiek"}, {}),
    )
    assert uitkomsten["bedekking"]["soort"] == "onderdeel"
    assert bt.indeling(beoordelingen, uitkomsten) == []
    assert uitkomsten["grafrecht"]["objectniveau"] == "kernobject"
    # een onderdeel dat kernobject is van een bedrijfsproces, is een subobject: een element dat de toets doorstaat
    assert (uitkomsten["bedekking"]["soort"], uitkomsten["bedekking"]["objectniveau"]) == ("element", "subobject")
    assert (uitkomsten["stoep"]["soort"], uitkomsten["stoep"]["genoemd_begrip"]) == ("onderdeel", "Graf")
    assert uitkomsten["besluit"]["objectniveau"] == "generiek"
    assert uitkomsten["losse"]["voorleggen"] and any("levensloop" in r for r in uitkomsten["losse"]["redenen"])


def test_indeling_toetst_de_afhankelijkheid():
    """Een deelproces hangt af van een bestaand bedrijfsproces, een variant van een bestaand element van hetzelfde type."""
    beoordelingen, uitkomsten = _bo_uitkomsten(
        graf=(BO, {}),
        beheren=(PROCES, {"kernobject": "graf"}),
        stap=(BASIS, {"afhankelijkheid": "deelproces", "genoemd_begrip": "Beheren"}),
        stoep=(BASIS, {"afhankelijkheid": "deelproces", "genoemd_begrip": "Graf"}),
        urn=(BASIS, {"afhankelijkheid": "variant", "genoemd_begrip": "Graf"}),
        pad=(BASIS, {"afhankelijkheid": "variant", "genoemd_begrip": "Bestaat-niet"}),
        weg=(BASIS, {"afhankelijkheid": "variant", "genoemd_begrip": "Beheren"}),
    )
    assert bt.indeling(beoordelingen, uitkomsten) == []
    assert not uitkomsten["stap"]["voorleggen"]
    assert any("geen bedrijfsproces" in r for r in uitkomsten["stoep"]["redenen"])
    assert (uitkomsten["urn"]["voorleggen"], uitkomsten["urn"]["archimate_type"]) == (False, "business-object")
    assert any("geen element" in r for r in uitkomsten["pad"]["redenen"])


def test_indeling_per_kernobject_een_proces():
    beoordelingen, uitkomsten = _bo_uitkomsten(
        graf=(BO, {}),
        beheren=(PROCES, {"kernobject": "graf"}),
        ruimen=(PROCES, {"kernobject": "graf"}),
        verdwaald=(PROCES, {"kernobject": "bestaat-niet"}),
    )
    fouten = bt.indeling(beoordelingen, uitkomsten)
    assert any("al het levensloopproces" in f for f in fouten)
    assert any("bestaat-niet" in f and "geen bedrijfsobject" in f for f in fouten)


def test_indeling_is_strikt_hierarchisch():
    """Een levensloopproces aggregeert geen levensloopproces, een bedrijfsproces hangt onder één levensloopproces, en
    het beleidsdomein van een levensloopproces of bedrijfsinteractie volgt uit het kernobject (besluit 2026-10-08)."""
    keten = BASIS | {"gedrag", "gezamenlijk_gedrag", "toegewezen_partij", "aanleiding", "benoembaar_resultaat"}
    agg = lambda *naar: [{"soort": "aggregatie", "naar": n, "ggm_match": "geen"} for n in naar]  # noqa: E731
    beoordelingen, uitkomsten = _bo_uitkomsten(
        graf=(BO, {"beleidsdomein": "Begraafplaatsen"}),
        recht=(BO, {"beleidsdomein": "Begraafplaatsen"}),
        beheren=(PROCES, {"kernobject": "graf", "beleidsdomein": "Begraafplaatsen", "relaties": agg("ruimen", "rechten")}),
        rechten=(PROCES, {"kernobject": "recht", "beleidsdomein": "Burgerzaken", "relaties": agg("ruimen")}),
        ruimen=(PROCES, {"kernobject": "graf", "niveau": "bedrijfsproces"}),
        bezorgen=(keten, {"kernobject": "graf", "beleidsdomein": "Begraafplaatsen"}),
    )
    fouten = bt.indeling(beoordelingen, uitkomsten)
    assert any(f.startswith("beheren: levensloopproces aggregeert levensloopproces 'rechten'") for f in fouten)
    assert any(f.startswith("ruimen: hangt onder meer levensloopprocessen") for f in fouten)
    assert any(f.startswith("rechten: beleidsdomein 'Burgerzaken' wijkt af") for f in fouten)
    assert not any(f.startswith("bezorgen") or f.startswith("beheren: beleidsdomein") for f in fouten)
    assert uitkomsten["graf"]["objectniveau"] == "kernobject"


def test_triggering_wijst_op_een_deelproces():
    """Een bedrijfsproces dat een ander bedrijfsproces onder hetzelfde levensloopproces triggert: voorleggen; een
    gebeurtenis die een deelproces triggert: fout (klant tot klant)."""
    rel = lambda soort, *naar: [{"soort": soort, "naar": n, "ggm_match": "geen"} for n in naar]  # noqa: E731
    beoordelingen, uitkomsten = _bo_uitkomsten(
        document=(BO, {}),
        beheren=(PROCES, {"kernobject": "document", "relaties": rel("aggregatie", "aanvragen", "uitreiken")}),
        aanvragen=(PROCES, {"kernobject": "document", "niveau": "bedrijfsproces", "relaties": rel("triggering", "uitreiken")}),
        uitreiken=(PROCES, {"kernobject": "document", "niveau": "bedrijfsproces"}),
        inhouden=(BASIS, {"afhankelijkheid": "deelproces", "genoemd_begrip": "Aanvragen"}),
        verval=(GEBEURTENIS, {"relaties": rel("triggering", "inhouden")}),
    )
    fouten = bt.indeling(beoordelingen, uitkomsten)
    assert uitkomsten["uitreiken"]["voorleggen"]
    assert any("getriggerd door bedrijfsproces 'aanvragen'" in r for r in uitkomsten["uitreiken"]["redenen"])
    assert not any("getriggerd" in r for r in uitkomsten["aanvragen"]["redenen"])
    assert any(f.startswith("verval: gebeurtenis triggert deelproces 'inhouden'") for f in fouten)


def test_een_levensloopproces_per_partij_binnen_een_ketensamenwerking():
    """Meer levensloopprocessen met hetzelfde kernobject mogen alleen als ze samen een bedrijfsinteractie met dat
    kernobject bedienen: elk het deel van één partij."""
    keten = BASIS | {"gedrag", "gezamenlijk_gedrag", "toegewezen_partij", "aanleiding", "benoembaar_resultaat"}
    bedient = lambda naar: [{"soort": "bediening", "naar": naar, "ggm_match": "geen"}]  # noqa: E731
    beoordelingen, uitkomsten = _bo_uitkomsten(
        lijk=(BO, {}), graf=(BO, {}),
        toestaan=(PROCES, {"kernobject": "lijk", "relaties": bedient("bezorgen")}),
        begraven=(PROCES, {"kernobject": "lijk", "relaties": bedient("bezorgen")}),
        bezorgen=(keten, {"kernobject": "lijk"}),
        andere=(keten, {"kernobject": "graf"}),
    )
    assert bt.indeling(beoordelingen, uitkomsten) == []
    assert uitkomsten["lijk"]["objectniveau"] == "kernobject"
    # bedient een van beide de interactie niet, of een interactie met een ander kernobject: fout
    beoordelingen["begraven"]["relaties"] = bedient("andere")
    assert any(f.startswith("toestaan: kernobject 'lijk' heeft al het levensloopproces 'begraven'")
               for f in bt.indeling(beoordelingen, uitkomsten))


def test_indelingsvelden_zijn_verplicht_en_beperkt():
    product = bt.evalueer(beoordeling(PRODUCT))
    assert product.voorleggen and "indelingsveld ontbreekt: domein" in product.redenen
    assert "indelingsveld ontbreekt: afnemer" in product.redenen
    assert bt.voorgestelde_status(product) == "review"
    compleet = bt.evalueer(beoordeling(PRODUCT, domein="Publieksdiensten", afnemer="extern"))
    assert not compleet.voorleggen and bt.voorgestelde_status(compleet) == "review"
    # de redenen liggen voor tot het akkoord, bij een begrip zonder pagina tot een afwijzing
    assert bt.open_redenen(product.redenen, "review", None) == product.redenen
    assert bt.open_redenen(product.redenen, "goedgekeurd", None) == []
    assert bt.open_redenen(["x"], None, [{"gevolg": "afwijzen"}]) == [] and bt.open_redenen(["x"], None, None) == ["x"]
    # de waarden zijn beperkt
    assert bt.controleer_indelingsvelden({"domein": "Verkeerd", "afnemer": "extern"}, bt.asdict(compleet))
    assert bt.controleer_indelingsvelden({"domein": "Publieksdiensten", "afnemer": "extern"}, bt.asdict(compleet)) == []
    # een cluster naar soort werk heeft geen afnemer; een proces wel
    cluster = bt.evalueer(beoordeling(CLUSTER, niveau="cluster naar soort werk",
                                      gemma_generiek={"id": "id-1", "onderbouwing": "GEMMA-proces."}))
    assert not cluster.voorleggen
    proces = bt.evalueer(beoordeling(PROCES, kernobject="graf"))
    assert "indelingsveld ontbreekt: afnemer" in proces.redenen
    assert not bt.evalueer(beoordeling(PROCES, kernobject="graf", afnemer="intern")).voorleggen
    for ja, veld in [(FUNCTIE, "domein"), (ACTOR, "doelgroep"), (ROL, "doelgroep"), (KANAAL, "doelgroep"),
                     (BELEIDSKADER, "regelgever")]:
        assert f"indelingsveld ontbreekt: {veld}" in bt.evalueer(beoordeling(ja)).redenen, veld


def test_elk_type_met_pagina_is_compleet():
    """Elk type met een pagina heeft een typebepalend kenmerk, een toetskenmerk (een relatiekenmerk als kernrelatie), een
    regel voor een eigen pagina en een plaats in de indelingen."""
    for t in bt.TYPEN:
        if t.laag != "pagina":
            continue
        assert t.bep, t.naam
        assert t.toets, t.naam
        assert any(s in bt.RELATIONEEL for s in t.toets) or t.naam == "Product", t.naam
        assert bt.km.indeling_tekst(t.paginatype), t.naam
        assert {s for s in t.toets if s in bt.RELATIONEEL} <= set(bt.RELATIONEEL)
        assert all(s not in bt.STANDAARD or bt.STANDAARD[s] == "ja" for s in t.toets if s not in bt.RELATIONEEL)


def test_besluit_heeft_altijd_tekst_en_is_verwerkt_of_afwijzen():
    validator = jsonschema.Draft202012Validator(bt.schema())
    basis = {**beoordeling({"herkenbaar"}), "onderwerpen": ["test"]}

    def fout(b: dict) -> bool:
        return any("besluiten" in "/".join(map(str, e.path)) for e in validator.iter_errors({**basis, "besluiten": [b]}))

    assert not fout({"datum": "2026-10-15", "besluit": "Keuze.", "gevolg": "verwerkt"})
    assert fout({"datum": "2026-10-15", "gevolg": "afwijzen"})
    assert fout({"datum": "2026-10-15", "besluit": "Keuze.", "gevolg": "opnemen"})
    assert fout({"datum": "2026-10-15", "besluit": "Keuze.", "gevolg": "verwerkt", "redenen": ["x"]})
    assert not fout({"datum": "2026-10-15", "besluit": "Keuze.", "gevolg": "verwerkt", "zekerheid": "indruk"})
    assert fout({"datum": "2026-10-15", "besluit": "Keuze.", "gevolg": "verwerkt", "zekerheid": "zeker"})
