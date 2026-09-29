"""tools/relaties.py: GGM-mapping, optillen, ketenen, ArchiMate-toets en de relatietabel."""
import pytest
from gam_hulp import KENMERKEN_BO, element_tekst

import relaties


def _ent(guid, naam, uml="Class"):
    return {"id": guid, "name": naam, "uml_type": uml, "attributes": [], "literals": [], "tags": {}}


def _rel(rid, soort, bron, doel, naam="", sc="1", tc="0..*", **extra):
    return {"id": rid, "uml_type": soort, "source_id": bron, "target_id": doel, "name": naam,
            "source_card": sc, "target_card": tc, **extra}


DATA = {
    "entities": {g: _ent(g, n) for g, n in [
        ("G_BESCH", "Beschikking"), ("G_ONDER", "Onderdeel beschikking"), ("G_BESLUIT", "Besluit"),
        ("G_AANVR", "Aanvraag"), ("G_TUSSEN", "Tussenobject"), ("G_ZAAK", "Zaak"), ("G_SUBTYPE", "Soort beschikking"),
    ]} | {"G_ENUM": _ent("G_ENUM", "Beschikkingstype", "Enumeration")},
    "relations": {r["id"]: r for r in [
        _rel("R_BEVAT", "Aggregation", "G_BESCH", "G_ONDER", "bevat", aggregatie="composite", geheel="source"),
        _rel("R_GEN", "Generalization", "G_BESLUIT", "G_BESCH", sc="", tc=""),
        _rel("R_LEIDT", "Aggregation", "G_AANVR", "G_BESCH", "leidt tot", aggregatie="composite", geheel="source"),
        _rel("R_KETEN1", "Aggregation", "G_BESCH", "G_TUSSEN", "bevat", sc="1", tc="1..*", aggregatie="composite", geheel="source"),
        _rel("R_KETEN2", "Association", "G_TUSSEN", "G_ZAAK", "hoort bij", sc="0..*", tc="1"),
        _rel("R_ENUM", "Association", "G_BESCH", "G_ENUM", "is van type"),
        _rel("R_SUB", "Association", "G_SUBTYPE", "G_AANVR", "volgt op"),
    ]},
}


def _element(wiki, id_, naam, guid, body="# x\n", map_="bedrijfsarchitectuur/bedrijfsobjecten/tv/bd"):
    pad = wiki / map_ / f"{id_}.md"
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(element_tekst({
        "id": id_, "type": "bedrijfsobject", "status": "review", "naam": naam, "archimate_type": "business-object",
        "onderwerp": "o", "bronnen": ["2026-vng-ggm"], "definitie": naam, "grondslag": "ggm-entiteit",
        "kenmerken": KENMERKEN_BO, "ggm_entiteit": naam, "ggm_guid": guid,
    }, body), encoding="utf-8")
    return pad


@pytest.fixture
def wiki(archimate_repo):
    root, wiki = archimate_repo
    specialisaties = "## Specialisaties\n\n| Specialisatie | Omschrijving | GGM-entiteit | GGM-guid |\n|---|---|---|---|\n| Soort | x | Soort beschikking | G_SUBTYPE |\n"
    _element(wiki, "beschikking", "Beschikking", "G_BESCH", specialisaties)
    _element(wiki, "onderdeel-beschikking", "Onderdeel beschikking", "G_ONDER")
    _element(wiki, "besluit", "Besluit", "G_BESLUIT")
    _element(wiki, "aanvraag", "Aanvraag", "G_AANVR")
    _element(wiki, "zaak", "Zaak", "G_ZAAK")
    return wiki


def _vind(kandidaten, bron, doel):
    return [k for k in kandidaten if (k.bron, k.doel) == (bron, doel)]


def test_exacte_compositie_en_specialisatie(wiki):
    k = relaties.voorstel("beschikking", DATA, wiki)
    (bevat,) = _vind(k, "beschikking", "onderdeel-beschikking")
    assert (bevat.relatie, bevat.grondslag, bevat.ggm_relaties) == ("composition", "ggm-exact", ["R_BEVAT"])
    (gen,) = _vind(k, "besluit", "beschikking")
    assert gen.relatie == "specialization"


def test_aggregatie_zonder_deel_geheel_naam_wordt_associatie_met_terugmelding(wiki):
    (leidt,) = _vind(relaties.voorstel("beschikking", DATA, wiki), "aanvraag", "beschikking")
    assert leidt.relatie == "association" and leidt.gericht and "leidt tot" in leidt.terugmelding


def test_keten_via_niet_opgenomen_entiteit_krijgt_zwakste_type(wiki):
    (keten,) = _vind(relaties.voorstel("beschikking", DATA, wiki), "beschikking", "zaak")
    assert keten.relatie == "association" and keten.grondslag == "ggm-afgeleid"
    assert keten.ggm_relaties == ["R_KETEN1", "R_KETEN2"]
    assert keten.kardinaliteit == "0..* → 1..*"


def test_enumeratie_vervalt_en_specialisatie_zonder_pagina_wordt_opgetild(wiki):
    k = relaties.voorstel("beschikking", DATA, wiki)
    assert not [x for x in k if "R_ENUM" in x.ggm_relaties]
    (opgetild,) = [x for x in k if "R_SUB" in x.ggm_relaties]
    assert (opgetild.bron, opgetild.doel, opgetild.grondslag) == ("beschikking", "aanvraag", "ggm-afgeleid")
    assert opgetild.terugmelding is None


def test_samengestelde_multipliciteit():
    assert relaties.samengestelde_multipliciteit("1", "1..*") == "1..*"
    assert relaties.samengestelde_multipliciteit("0..1", "2") == "0..2"
    assert relaties.samengestelde_multipliciteit("", "1") == ""


def test_archimate_toets():
    assert relaties.toegestaan("composition", "business-object", "business-object")
    assert relaties.toegestaan("access", "business-process", "business-object")
    assert relaties.toegestaan("specialization", "contract", "business-object")
    assert not relaties.toegestaan("composition", "business-object", "business-process")
    assert not relaties.toegestaan("specialization", "business-actor", "business-role")
    assert not relaties.toegestaan("assignment", "business-object", "business-process")


def test_markdown_rijen_en_teruglezen_met_inkomend(wiki):
    k = relaties.voorstel("beschikking", DATA, wiki)
    rijen = relaties.markdown_rijen("beschikking", k, wiki)
    assert "[Onderdeel beschikking](onderdeel-beschikking.md)" in rijen
    pad = wiki / "bedrijfsarchitectuur/bedrijfsobjecten/tv/bd/beschikking.md"
    pad.write_text(pad.read_text(encoding="utf-8") + "\n## Relaties\n\n" + rijen, encoding="utf-8")
    alle = relaties.alle_relaties(wiki)
    assert {r.naar for r in alle["beschikking"]} >= {"onderdeel-beschikking", "zaak", "aanvraag"}
    assert all(not r.fouten for r in alle["beschikking"])
    assert [i["van"] for i in relaties.inkomend("onderdeel-beschikking", wiki)] == ["beschikking"]


def test_fouten_in_relatietabel(wiki):
    pad = wiki / "bedrijfsarchitectuur/bedrijfsobjecten/tv/bd/zaak.md"
    pad.write_text(pad.read_text(encoding="utf-8") + (
        "\n## Relaties\n\n| Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie |\n|---|---|---|---|---|---|\n"
        "| verbinding | [X](bestaat-niet.md) |  |  | ggm-exact |  |\n| toegang | [Besluit](besluit.md) | | | bron | |\n"
    ), encoding="utf-8")
    (eerste, tweede) = relaties.alle_relaties(wiki)["zaak"]
    assert any("onbekende relatie" in f for f in eerste.fouten)
    assert any("wijst niet naar een elementpagina" in f for f in eerste.fouten)
    assert any("zonder GGM-relatie" in f for f in eerste.fouten)
    assert any("toegang zonder" in f for f in tweede.fouten)
