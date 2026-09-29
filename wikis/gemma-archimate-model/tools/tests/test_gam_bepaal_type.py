"""Beslistabel: één testbegrip per tegenstrijdigheid uit de analyse (T1–T7) plus de randgevallen."""
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
PASSIEF_BO = SCOPE | {"eigen_identiteit", "onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"}


def test_regelnummers_volgen_de_tabel():
    """Het regelnummer in een uitkomst moet gelijk zijn aan de positie in REGELS."""
    gevallen = {
        1: beoordeling(set()),
        2: beoordeling(SCOPE | {"buiten_kernlagen"}),
        3: beoordeling(SCOPE | {"slechts_eigenschap"}, genoemd_begrip="Pand"),
        4: beoordeling(SCOPE | {"handelende_partij", "hoedanigheid"}, benoemde_partij="ja"),
        5: beoordeling(SCOPE | {"gedrag", "aanbod_als_geheel"}),
        6: beoordeling(SCOPE | {"handelende_partij"}),
        7: beoordeling(SCOPE | {"hoedanigheid"}),
        8: beoordeling(SCOPE | {"aanbod_als_geheel"}),
        9: beoordeling(SCOPE | {"samenwerkingsverband"}),
        10: beoordeling(SCOPE | {"toegangspunt"}),
        11: beoordeling(SCOPE | {"plaats"}),
        12: beoordeling(SCOPE | {"gedrag", "per_keer_doorlopen"}),
        13: beoordeling(SCOPE | {"gedrag"}),
        14: beoordeling(SCOPE | {"per_keer_doorlopen"}),
        15: beoordeling(SCOPE | {"waarneembare_vorm"}, genoemd_begrip="Aanslag"),
        16: beoordeling(PASSIEF_BO | {"afspraak"}),
        17: beoordeling(PASSIEF_BO),
        18: beoordeling(SCOPE | {"eigen_identiteit"}),
    }
    assert len(gevallen) == len(bt.REGELS)
    for nr, b in gevallen.items():
        assert bt.evalueer(b).regel == nr, nr


def test_t1_doelgroep_is_rol_of_eigenschap_geen_eigen_type():
    # "Minima": indeling van inwoners → eigenschap van Inwoner
    u = bt.evalueer(beoordeling(SCOPE | {"slechts_eigenschap"}, genoemd_begrip="Inwoner"))
    assert u.soort == "eigenschap" and u.genoemd_begrip == "Inwoner"
    # "Belastingplichtige": hoedanigheid in een handeling → rol
    assert bt.evalueer(beoordeling(SCOPE | {"hoedanigheid"})).paginatype == "rol"


def test_t2_verordening_is_bedrijfsobject_geen_contract():
    u = bt.evalueer(beoordeling(PASSIEF_BO))
    assert (u.paginatype, u.archimate_type) == ("bedrijfsobject", "business-object")
    assert bt.voorgestelde_status(u, grondslag="governance-object") == "kandidaat"
    contract = bt.evalueer(beoordeling(PASSIEF_BO | {"afspraak"}))
    assert contract.archimate_type == "contract"


def test_t3_tegenhanger_zonder_registratietaal():
    u = bt.evalueer(beoordeling(SCOPE | {"handelende_partij", "onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"}))
    assert u.paginatype == "actor" and u.tegenhanger == "bedrijfsobject"
    alleen_actor = bt.evalueer(beoordeling(SCOPE | {"handelende_partij"}))
    assert alleen_actor.tegenhanger is None


def test_t4_t5_geen_tegenhanger_bij_gedrag():
    u = bt.evalueer(beoordeling(PASSIEF_BO | {"gedrag", "per_keer_doorlopen"}))
    assert u.paginatype == "bedrijfsproces" and u.tegenhanger is None


def test_t6_ketenpartner_bij_directe_samenwerking_is_actor():
    assert bt.evalueer(beoordeling(SCOPE | {"handelende_partij"})).paginatype == "actor"
    assert bt.evalueer(beoordeling({"herkenbaar", "handelende_partij"})).soort == "buiten_scope"


def test_t7_autonomie_proces_zonder_ggm_kan_review():
    u = bt.evalueer(beoordeling(SCOPE | {"gedrag", "gegroepeerd_gedrag"}))
    assert u.paginatype == "bedrijfsfunctie"
    assert bt.voorgestelde_status(u) == "review"
    data_object = bt.evalueer(beoordeling(PASSIEF_BO | {"geautomatiseerd_verwerkt"}))
    assert data_object.data_object == "ja"
    assert bt.voorgestelde_status(data_object, ggm_match="partieel") == "kandidaat"
    assert bt.voorgestelde_status(data_object, ggm_match="sterk") == "review"


def test_actor_en_rol_samen_zonder_benoemde_partij_wordt_voorgelegd():
    u = bt.evalueer(beoordeling(SCOPE | {"handelende_partij", "hoedanigheid"}))
    assert u.voorleggen


def test_geen_levenscyclus_wordt_voorgelegd():
    u = bt.evalueer(beoordeling(SCOPE | {"eigen_identiteit", "onderscheidbare_exemplaren", "wordt_bewerkt"}))
    assert u.paginatype == "bedrijfsobject" and u.voorleggen
    assert bt.voorgestelde_status(u) == "kandidaat"


def test_herkende_typen_krijgen_geen_pagina():
    for ja, archimate in [
        ({"samenwerkingsverband"}, "business-collaboration"),
        ({"gedrag", "gezamenlijk_gedrag"}, "business-interaction"),
        ({"waarneembare_vorm"}, "representation"),
    ]:
        u = bt.evalueer(beoordeling(SCOPE | ja, genoemd_begrip="X"))
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
