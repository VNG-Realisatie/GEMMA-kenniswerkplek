"""Beslistabel (criteria van 2026-10-01): regelnummers, consistentie, drempel met kernrelatie, specialisatie en aanvullingen."""
import json
import sys
from pathlib import Path

import jsonschema
import pytest

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import bepaal_type as bt  # noqa: E402

WIKI = TOOLS.parent


def beoordeling(ja: set[str], **extra) -> dict:
    return {
        "begrip": "test",
        "kenmerken": {s: {"waarde": "ja" if s in ja else "nee", "onderbouwing": "test"} for s in bt.SLEUTELS},
        **extra,
    }


SCOPE = {"herkenbaar", "gemeentelijk"}
BASIS = SCOPE | {"eigen_identiteit", "betekenis_in_onderwerp", "zelfstandige_specialisatie"}
BO = BASIS | {"onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"}
ACTOR = BASIS | {"handelende_partij", "los_van_verantwoordelijkheid", "vervult_een_rol"}
ROL = BASIS | {"hoedanigheid", "voert_gedrag_uit"}
PROCES = BASIS | {"gedrag", "per_keer_doorlopen", "toegewezen_partij", "gebruikt_objecten", "aanleiding",
                  "benoembaar_resultaat", "komt_herhaald_voor", "eigen_normering"}
FUNCTIE = BASIS | {"gedrag", "gegroepeerd_gedrag", "toegewezen_partij", "gebruikt_objecten", "stabiel_over_tijd"}
DIENST = BASIS | {"gedrag", "aangeboden_gedrag", "gerealiseerd_door", "afnemer", "benoembaar_resultaat"}
GEBEURTENIS = BASIS | {"gedrag", "toestandsverandering", "leidt_tot_gedrag", "komt_herhaald_voor"}
PRODUCT = BASIS | {"aanbod_als_geheel", "omvat_diensten_en_afspraken", "afnemer", "benoembaar_resultaat"}
SAMENWERKING = BASIS | {"samenwerkingsverband", "voert_gedrag_uit"}
KANAAL = BASIS | {"toegangspunt", "ontsluit_een_dienst"}
BELEIDSKADER = BASIS | {"regeling_als_geheel", "landelijk", "in_werking", "is_grondslag_voor"}


def test_elke_regel_van_stap_0_tot_4_heeft_een_geval():
    gevallen = [
        beoordeling(BO, synoniem_van="Urn"),
        beoordeling(set()),
        beoordeling(SCOPE | {"buiten_dit_model"}),
        beoordeling(SCOPE | {"slechts_eigenschap"}, genoemd_begrip="Pand"),
        beoordeling(SCOPE, genoemd_begrip="Besluit"),
        beoordeling(SCOPE | {"eigen_identiteit"}),
        beoordeling(BO | {"per_keer_doorlopen"}),
        beoordeling(ROL | {"handelende_partij"}),
        beoordeling(SAMENWERKING),
        beoordeling(BASIS | {"gedrag", "aanbod_als_geheel"}),
        beoordeling(ACTOR),
        beoordeling(ROL),
        beoordeling(PRODUCT),
        beoordeling(KANAAL),
        beoordeling(BASIS | {"plaats"}),
        beoordeling(BELEIDSKADER),
        beoordeling(PROCES),
        beoordeling(BASIS | {"gedrag"}),
        beoordeling(BASIS | {"waarneembare_vorm"}, genoemd_begrip="Aanslag"),
        beoordeling(BO | {"afspraak"}),
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
    assert bt.voorgestelde_status(u) == "kandidaat"


def test_niet_in_dit_onderwerp_is_verwijzing():
    u = bt.evalueer(beoordeling(BO - {"betekenis_in_onderwerp"}))
    assert u.soort == "verwijzing" and u.paginatype is None


def test_consistentie_kenmerken_passen_bij_de_aard():
    # Gedragskenmerk bij een ding
    assert bt.evalueer(beoordeling(BO | {"aanleiding"})).soort == "conflict"
    # Afspraak naast gedrag
    assert bt.evalueer(beoordeling(PROCES | {"afspraak"})).soort == "conflict"
    # Partijkenmerk zonder partij
    assert bt.evalueer(beoordeling(BO | {"voert_gedrag_uit"})).soort == "conflict"
    # Beleidskaderkenmerk zonder regeling
    assert bt.evalueer(beoordeling(BO | {"landelijk"})).soort == "conflict"
    # Afnemer en resultaat mogen bij een product, exemplaren en bewerkt bij een partij (tegenhanger)
    assert bt.evalueer(beoordeling(PRODUCT)).paginatype == "product"
    assert bt.evalueer(beoordeling(ACTOR | {"onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"})).paginatype == "actor"


def test_drempel_kernrelatie_moet_ja():
    for ja, kern in [(BO, "wordt_bewerkt"), (PROCES, "toegewezen_partij"), (FUNCTIE, "toegewezen_partij"),
                     (DIENST, "gerealiseerd_door"), (GEBEURTENIS, "leidt_tot_gedrag"), (ACTOR, "vervult_een_rol"),
                     (ROL, "voert_gedrag_uit"), (PRODUCT, "omvat_diensten_en_afspraken"),
                     (SAMENWERKING, "voert_gedrag_uit"), (KANAAL, "ontsluit_een_dienst"), (BELEIDSKADER, "is_grondslag_voor")]:
        u = bt.evalueer(beoordeling(ja - {kern}))
        assert (u.soort, u.regel, u.voorleggen) == ("geen_element", bt.EERSTE_DREMPELREGEL, True), kern
        assert f"{bt.NAAM[kern]}: nee" in u.redenen


def test_drempel_hoogstens_een_overig_nee():
    u = bt.evalueer(beoordeling(BO - {"levenscyclus"}))
    assert u.soort == "element" and not u.voorleggen and "levenscyclus" in u.toelichting
    assert bt.voorgestelde_status(u) == "review"
    u = bt.evalueer(beoordeling(BO - {"levenscyclus", "onderscheidbare_exemplaren"}))
    assert (u.soort, u.regel) == ("geen_element", bt.EERSTE_DREMPELREGEL + 1)
    assert bt.evalueer(beoordeling(PROCES - {"komt_herhaald_voor"})).paginatype == "bedrijfsproces"
    assert bt.evalueer(beoordeling(PROCES - {"komt_herhaald_voor", "eigen_normering"})).soort == "geen_element"
    # Dienst zonder toegewezen partij (besluit 2026-10-01); product zonder exemplaren
    assert bt.evalueer(beoordeling(DIENST)).paginatype == "dienst"
    assert "toegewezen_partij" not in bt.TYPE[("dienst", "business-service")].drempel
    assert "onderscheidbare_exemplaren" not in bt.TYPE[("product", "product")].drempel


def test_specialisatieniveau():
    u = bt.evalueer(beoordeling(BO - {"zelfstandige_specialisatie"}, genoemd_begrip="Vergunning"))
    assert (u.soort, u.regel, u.genoemd_begrip, u.paginatype) == ("specialisatie", bt.EERSTE_SPECIALISATIEREGEL, "Vergunning", None)
    u = bt.evalueer(beoordeling(BO - {"zelfstandige_specialisatie"}))
    assert (u.soort, u.voorleggen) == ("geen_element", True)
    assert bt.evalueer(beoordeling(ROL - {"zelfstandige_specialisatie"}, genoemd_begrip="Aanvrager")).soort == "specialisatie"


def test_actor_rol_en_samenwerking():
    houder = bt.evalueer(beoordeling(ROL | {"handelende_partij"}))
    assert houder.paginatype == "rol"
    burgemeester = bt.evalueer(beoordeling(ACTOR | {"hoedanigheid"}))
    assert burgemeester.paginatype == "actor"
    assert bt.evalueer(beoordeling(ACTOR - {"los_van_verantwoordelijkheid"})).soort == "conflict"
    assert bt.evalueer(beoordeling(ROL | {"los_van_verantwoordelijkheid"})).soort == "conflict"
    # GGD: organisatie en samenwerkingsverband met eigen rechtspersoon → actor
    ggd = bt.evalueer(beoordeling(BASIS | {"handelende_partij", "samenwerkingsverband", "eigen_rechtspersoon",
                                           "vervult_een_rol"}))
    assert ggd.paginatype == "actor"
    # Zorg- en Veiligheidshuis: zonder eigen rechtspersoon → bedrijfssamenwerking
    assert bt.evalueer(beoordeling(SAMENWERKING)).paginatype == "bedrijfssamenwerking"


def test_kanaal_wordt_altijd_voorgelegd():
    u = bt.evalueer(beoordeling(KANAAL))
    assert u.paginatype == "kanaal" and u.voorleggen and bt.voorgestelde_status(u) == "kandidaat"


def test_regeling_landelijk_of_bron():
    assert bt.evalueer(beoordeling(BELEIDSKADER)).paginatype == "beleidskader"
    assert bt.evalueer(beoordeling(BELEIDSKADER - {"in_werking"})).paginatype == "beleidskader"
    assert bt.evalueer(beoordeling(BELEIDSKADER - {"landelijk"})).soort == "bron"
    # De soort regeling is een bedrijfsobject
    assert bt.evalueer(beoordeling(BO)).archimate_type == "business-object"


def test_geen_pagina_en_herkend():
    vorm = bt.evalueer(beoordeling(BASIS | {"waarneembare_vorm"}, genoemd_begrip="Graf"))
    assert (vorm.soort, vorm.archimate_type, vorm.paginatype, vorm.voorleggen) == ("geen_pagina", "representation", None, False)
    assert bt.evalueer(beoordeling(BASIS | {"waarneembare_vorm"})).voorleggen  # zonder genoemd object
    plaats = bt.evalueer(beoordeling(BASIS | {"plaats"}))
    assert (plaats.soort, plaats.archimate_type, plaats.voorleggen) == ("geen_pagina", "location", False)
    interactie = bt.evalueer(beoordeling(BASIS | {"gedrag", "gezamenlijk_gedrag"}))
    assert (interactie.soort, interactie.archimate_type, interactie.voorleggen) == ("herkend", "business-interaction", True)
    for u in (vorm, plaats, interactie):
        assert bt.voorgestelde_status(u) is None


def test_aanvullingen():
    u = bt.evalueer(beoordeling(ACTOR | {"onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"}))
    assert u.tegenhanger == "bedrijfsobject"
    assert bt.evalueer(beoordeling(ACTOR)).tegenhanger is None
    assert bt.evalueer(beoordeling(PROCES)).procesniveau == "bedrijfsproces"
    assert bt.evalueer(beoordeling(PROCES | {"bijdrage_aan_groter_proces"})).procesniveau == "deelproces"
    data_object = bt.evalueer(beoordeling(BO | {"geautomatiseerd_verwerkt"}))
    assert data_object.data_object == "ja"
    assert bt.voorgestelde_status(data_object, ggm_match="partieel") == "kandidaat"
    assert bt.voorgestelde_status(data_object, ggm_match="sterk") == "review"
    assert bt.voorgestelde_status(bt.evalueer(beoordeling(BO)), grondslag="regelgeving") == "kandidaat"
    besluit = {"datum": "2026-10-01", "besluit": "Opnemen.", "gevolg": "opnemen", "redenen": [bt.REDEN_GEEN_GGM]}
    assert bt.voorgestelde_status(data_object, ggm_match="geen", besluiten=[besluit]) == "review"
    assert bt.voorgestelde_status(data_object, besluiten=[besluit, {**besluit, "gevolg": "afwijzen"}]) == "afgewezen"


def test_buiten_scope_en_eigenschap():
    assert bt.evalueer(beoordeling(ACTOR - {"gemeentelijk"})).soort == "buiten_scope"
    u = bt.evalueer(beoordeling(SCOPE | {"slechts_eigenschap"}, genoemd_begrip="Inwoner"))
    assert (u.soort, u.genoemd_begrip) == ("eigenschap", "Inwoner")


def test_onvolledige_beoordeling_wordt_geweigerd():
    b = beoordeling(SCOPE)
    del b["kenmerken"]["plaats"]
    b["kenmerken"]["herkenbaar"]["onderbouwing"] = ""
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("plaats" in f for f in exc.value.fouten)
    assert any("onderbouwing" in f for f in exc.value.fouten)


def test_elk_kenmerk_telt_ergens():
    gebruikt = set()
    for t in bt.TYPEN:
        gebruikt |= set(t.bep) | set(t.drempel) | set(t.aanvulling) | ({t.kern} if t.kern else set())
    gebruikt |= {k.sleutel for k in bt.KENMERKEN if k.groep in ("Poort", "Specialisatie")}
    assert set(bt.SLEUTELS) - gebruikt == set()


def test_gegenereerd_schema_is_actueel_en_geldig():
    opgeslagen = json.loads((WIKI / "schemas" / "beoordeling.schema.json").read_text(encoding="utf-8"))
    assert opgeslagen == bt.schema(), "draai: uv run python tools/bepaal_type.py schema --schrijf"
    jsonschema.Draft202012Validator(opgeslagen).validate({**beoordeling(BO), "onderwerpen": ["test"]})


def test_documentatie_is_gegenereerd():
    skill = bt.SKILL_PATH.read_text(encoding="utf-8")
    wiki = bt.DOC_PATH.read_text(encoding="utf-8")
    assert bt.markdown("skill") in skill, "draai: uv run python tools/bepaal_type.py markdown --schrijf"
    assert bt.markdown("wiki") in wiki, "draai: uv run python tools/bepaal_type.py markdown --schrijf"
    assert "### Stappentabel" not in wiki
