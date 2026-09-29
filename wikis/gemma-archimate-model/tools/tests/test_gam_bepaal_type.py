"""Beslistabel: regelnummers, drempel, specialisatieniveau, actor/rol en de randgevallen."""
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
# De generieke criteria (stap 2, 4 en 5), bij alle typen ja
ZELFSTANDIG = SCOPE | {"eigen_identiteit", "betekenis_in_onderwerp", "relaties", "zelfstandig_beleidsbegrip"}
PASSIEF_BO = ZELFSTANDIG | {"onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"}
ACTOR = ZELFSTANDIG | {"handelende_partij", "los_van_verantwoordelijkheid"}
ROL = ZELFSTANDIG | {"hoedanigheid", "meerdere_vervullers"}
PROCES = ZELFSTANDIG | {"gedrag", "per_keer_doorlopen"}


def test_regelnummers_stap_1_tot_3_volgen_de_tabel():
    """Het regelnummer (of bij een uitkomst uit stap 4/5: de typeregel) is gelijk aan de positie in REGELS."""
    gevallen = {
        1: beoordeling(set()),
        2: beoordeling(SCOPE | {"buiten_kernlagen"}),
        3: beoordeling(SCOPE | {"slechts_eigenschap"}, genoemd_begrip="Pand"),
        4: beoordeling(SCOPE, genoemd_begrip="Besluit"),
        5: beoordeling(ACTOR | {"hoedanigheid"}),
        6: beoordeling(ZELFSTANDIG | {"gedrag", "aanbod_als_geheel"}),
        7: beoordeling(ACTOR),
        8: beoordeling(ROL),
        9: beoordeling(ZELFSTANDIG | {"aanbod_als_geheel", "onderscheidbare_exemplaren"}),
        10: beoordeling(ZELFSTANDIG | {"samenwerkingsverband"}),
        11: beoordeling(ZELFSTANDIG | {"toegangspunt"}),
        12: beoordeling(ZELFSTANDIG | {"plaats"}),
        13: beoordeling(PROCES),
        14: beoordeling(ZELFSTANDIG | {"gedrag"}),
        15: beoordeling(ZELFSTANDIG | {"per_keer_doorlopen"}),
        16: beoordeling(ZELFSTANDIG | {"waarneembare_vorm"}, genoemd_begrip="Aanslag"),
        17: beoordeling(PASSIEF_BO | {"afspraak"}),
        18: beoordeling(PASSIEF_BO),
    }
    assert len(gevallen) == len(bt.REGELS)
    for nr, b in gevallen.items():
        u = bt.evalueer(b)
        assert (u.typeregel or u.regel) == nr, nr


def test_element_komt_uit_stap_5():
    u = bt.evalueer(beoordeling(PASSIEF_BO))
    assert (u.soort, u.regel, u.typeregel) == ("element", bt.EERSTE_SPECIALISATIEREGEL + 2, 18)
    assert u.paginatype == "bedrijfsobject" and not u.voorleggen


def test_drempel_bedrijfsobject_zes_van_zeven():
    # Eén criterium nee (zoals het oude 5 van de 6): element, zelfstandig af te handelen
    u = bt.evalueer(beoordeling(PASSIEF_BO - {"levenscyclus"}))
    assert u.soort == "element" and not u.voorleggen and "levenscyclus" in u.toelichting
    assert bt.voorgestelde_status(u) == "review"
    # Twee nee: geen element, voorleggen met de ontbrekende criteria
    u = bt.evalueer(beoordeling(PASSIEF_BO - {"levenscyclus", "relaties"}))
    assert (u.soort, u.regel, u.voorleggen) == ("geen_element", bt.EERSTE_DREMPELREGEL, True)
    assert set(u.redenen) == {"levenscyclus: nee", "relaties: nee"}
    assert bt.voorgestelde_status(u) is None


def test_drempel_per_type():
    assert bt.evalueer(beoordeling(ACTOR - {"relaties", "betekenis_in_onderwerp"})).soort == "geen_element"
    assert bt.evalueer(beoordeling(ACTOR - {"relaties"})).paginatype == "actor"
    assert bt.evalueer(beoordeling(ROL - {"meerdere_vervullers", "relaties"})).soort == "geen_element"
    assert bt.evalueer(beoordeling(PROCES - {"relaties", "betekenis_in_onderwerp"})).soort == "geen_element"


def test_eigen_identiteit_is_harde_poort_voor_alle_typen():
    for ja in (PASSIEF_BO, ACTOR, PROCES):
        u = bt.evalueer(beoordeling(ja - {"eigen_identiteit"}, genoemd_begrip="Lijkbezorging"))
        assert (u.soort, u.regel, u.genoemd_begrip) == ("onderdeel", 4, "Lijkbezorging")
    assert bt.evalueer(beoordeling(PASSIEF_BO - {"eigen_identiteit"})).voorleggen


def test_specialisatieniveau():
    # Vergunning tot opgraving: variant van een breder begrip → specialisatie zonder pagina
    u = bt.evalueer(beoordeling(PASSIEF_BO - {"zelfstandig_beleidsbegrip"}, genoemd_begrip="Vergunning"))
    assert (u.soort, u.regel, u.genoemd_begrip, u.paginatype) == (
        "specialisatie", bt.EERSTE_SPECIALISATIEREGEL, "Vergunning", None)
    assert bt.voorgestelde_status(u) is None
    # Zonder genoemd begrip: voorleggen
    u = bt.evalueer(beoordeling(PASSIEF_BO - {"zelfstandig_beleidsbegrip"}))
    assert (u.soort, u.regel, u.voorleggen) == ("geen_element", bt.EERSTE_SPECIALISATIEREGEL + 1, True)
    # Geldt ook voor gedrag
    u = bt.evalueer(beoordeling(PROCES - {"zelfstandig_beleidsbegrip"}, genoemd_begrip="Behandelen vergunningaanvraag"))
    assert u.soort == "specialisatie"


def test_actor_of_rol_via_los_van_verantwoordelijkheid():
    # Kerkgenootschap: partij, los van de verantwoordelijkheid → actor
    assert bt.evalueer(beoordeling(ACTOR)).paginatype == "actor"
    # Houder van de begraafplaats: partij én hoedanigheid, gebonden aan de verantwoordelijkheid → rol
    houder = bt.evalueer(beoordeling(ROL | {"handelende_partij"}))
    assert houder.paginatype == "rol" and houder.typeregel == 5
    burgemeester = bt.evalueer(beoordeling(ACTOR | {"hoedanigheid"}))
    assert burgemeester.paginatype == "actor" and burgemeester.typeregel == 5


def test_tegenstrijdige_partijantwoorden_worden_voorgelegd():
    u = bt.evalueer(beoordeling(ACTOR - {"los_van_verantwoordelijkheid"}))
    assert (u.soort, u.regel) == ("conflict", 7)
    u = bt.evalueer(beoordeling(ROL | {"los_van_verantwoordelijkheid"}))
    assert (u.soort, u.regel) == ("conflict", 8)


def test_doelgroep_is_eigenschap_geen_eigen_type():
    # "Minima": indeling van inwoners → eigenschap van Inwoner
    u = bt.evalueer(beoordeling(SCOPE | {"slechts_eigenschap"}, genoemd_begrip="Inwoner"))
    assert u.soort == "eigenschap" and u.genoemd_begrip == "Inwoner"


def test_verordening_is_bedrijfsobject_geen_contract():
    u = bt.evalueer(beoordeling(PASSIEF_BO))
    assert (u.paginatype, u.archimate_type) == ("bedrijfsobject", "business-object")
    assert bt.voorgestelde_status(u, grondslag="governance-object") == "kandidaat"
    assert bt.evalueer(beoordeling(PASSIEF_BO | {"afspraak"})).archimate_type == "contract"


def test_tegenhanger_zonder_registratietaal():
    u = bt.evalueer(beoordeling(ACTOR | {"onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"}))
    assert u.paginatype == "actor" and u.tegenhanger == "bedrijfsobject"
    assert bt.evalueer(beoordeling(ACTOR)).tegenhanger is None


def test_geen_tegenhanger_bij_gedrag():
    u = bt.evalueer(beoordeling(PASSIEF_BO | {"gedrag", "per_keer_doorlopen"}))
    assert u.paginatype == "bedrijfsproces" and u.tegenhanger is None


def test_ketenpartner_zonder_structurele_samenwerking_buiten_scope():
    assert bt.evalueer(beoordeling(ACTOR)).paginatype == "actor"
    assert bt.evalueer(beoordeling(ACTOR - {"gemeentelijk"})).soort == "buiten_scope"


def test_autonomie_proces_zonder_ggm_kan_review():
    u = bt.evalueer(beoordeling(ZELFSTANDIG | {"gedrag", "gegroepeerd_gedrag"}))
    assert u.paginatype == "bedrijfsfunctie"
    assert bt.voorgestelde_status(u) == "review"
    data_object = bt.evalueer(beoordeling(PASSIEF_BO | {"geautomatiseerd_verwerkt"}))
    assert data_object.data_object == "ja"
    assert bt.voorgestelde_status(data_object, ggm_match="partieel") == "kandidaat"
    assert bt.voorgestelde_status(data_object, ggm_match="sterk") == "review"


def test_herkende_typen_krijgen_geen_pagina():
    for ja, archimate in [
        ({"samenwerkingsverband"}, "business-collaboration"),
        ({"gedrag", "gezamenlijk_gedrag"}, "business-interaction"),
        ({"waarneembare_vorm"}, "representation"),
    ]:
        u = bt.evalueer(beoordeling(ZELFSTANDIG | ja, genoemd_begrip="X"))
        assert u.soort == "herkend" and u.archimate_type == archimate and u.paginatype is None
        assert bt.voorgestelde_status(u) is None


def test_onvolledige_beoordeling_wordt_geweigerd():
    b = beoordeling(SCOPE)
    del b["kenmerken"]["plaats"]
    b["kenmerken"]["herkenbaar"]["onderbouwing"] = ""
    with pytest.raises(bt.BeoordelingFout) as exc:
        bt.evalueer(b)
    assert any("plaats" in f for f in exc.value.fouten)
    assert any("onderbouwing" in f for f in exc.value.fouten)


def test_gegenereerd_schema_is_actueel_en_geldig():
    opgeslagen = json.loads((WIKI / "schemas" / "beoordeling.schema.json").read_text(encoding="utf-8"))
    assert opgeslagen == bt.schema(), "draai: uv run python tools/bepaal_type.py schema --schrijf"
    jsonschema.Draft202012Validator(opgeslagen).validate(beoordeling(PASSIEF_BO))


def test_skilltabel_is_gegenereerd():
    skill = (WIKI / ".agents" / "skills" / "gemma-archimate-model-criteria" / "SKILL.md").read_text(encoding="utf-8")
    assert bt.markdown() in skill, "tabellen in de criteria-skill wijken af: draai tools/bepaal_type.py markdown"
