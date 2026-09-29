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
    assert relaties.toegestaan("assignment", "business-actor", "business-role")
    assert not relaties.toegestaan("assignment", "business-role", "business-role")
    assert not relaties.toegestaan("assignment", "business-actor", "business-actor")


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


# --- Relaties uit de bronnen ---


@pytest.mark.parametrize("bron,doel,werkwoord,verwacht", [
    ("business-role", "business-process", "behandelt", ("assignment", False, None)),
    ("business-process", "business-object", "stelt vast", ("access", False, "schrijven")),
    ("business-process", "business-object", "toetst aan", ("access", False, "lezen")),
    ("business-object", "business-process", "wordt behandeld in", ("access", True, "lezen-schrijven")),
    ("business-event", "business-process", "start", ("triggering", False, None)),
    ("business-process", "business-process", "volgt op", ("triggering", True, None)),
    ("business-process", "business-service", "levert", ("realization", False, None)),
    ("business-service", "business-role", "is bestemd voor", ("serving", False, None)),
    ("business-object", "business-object", "bestaat uit", ("composition", False, None)),
    ("business-object", "business-object", "maakt deel uit van", ("aggregation", True, None)),
    ("contract", "business-object", "is een", ("specialization", False, None)),
    ("business-object", "business-object", "hoort bij", ("association", False, None)),
    ("business-actor", "business-role", "vervult", ("assignment", False, None)),
    ("business-actor", "business-role", "benoemen", ("association", False, None)),
    ("business-role", "business-role", "waarschuwt", ("association", False, None)),
    ("business-actor", "business-actor", "stellen ter beschikking aan", ("association", False, None)),
])
def test_van_bron(bron, doel, werkwoord, verwacht):
    a = relaties.van_bron(bron, doel, werkwoord)
    assert (a["relatie"], a["omgedraaid"], a["toegang"]) == verwacht


def test_van_bron_valt_terug_op_associatie_bij_ongeldige_combinatie():
    a = relaties.van_bron("business-object", "business-role", "bestaat uit")
    assert a["relatie"] == "association" and a["gericht"]


def _voorstel(begrip, soort, archimate, doel, genoemd=None, relaties_=()):
    uitkomst = {"soort": soort, "archimate_type": archimate, "genoemd_begrip": genoemd}
    return {"doel": doel, "beoordeling": {"begrip": begrip, "uitkomst": uitkomst}, "relaties": list(relaties_)}


def test_uit_bronnen_lost_op_tilt_op_en_laat_vervallen(wiki):
    assessment = {"voorstellen": [
        _voorstel("Heffingsambtenaar", "element", "business-role", "bedrijfsarchitectuur/rollen/heffingsambtenaar.md", relaties_=[
            {"van": "Heffingsambtenaar", "werkwoord": "legt op", "naar": "Aanslag opleggen", "bronnen": ["2026-overheid-gemeentewet"], "vindplaats": "art. 231"},
        ]),
        _voorstel("Aanslag opleggen", "element", "business-process", "bedrijfsarchitectuur/bedrijfsprocessen/tv/bd/aanslag-opleggen.md", relaties_=[
            {"van": "Aanslag opleggen", "werkwoord": "stelt vast", "naar": "Aanslagbedrag", "bronnen": ["2026-utrecht-nota"]},
            {"van": "Aanslag opleggen", "werkwoord": "draagt bij aan", "naar": "Rechtvaardige heffing", "bronnen": ["2026-utrecht-nota"]},
        ]),
        _voorstel("Aanslagbedrag", "eigenschap", None, "begrippen/o.md", genoemd="Beschikking"),
        _voorstel("Rechtvaardige heffing", "buiten_model", None, "begrippen/o.md"),
    ]}
    kandidaten, vervallen = relaties.uit_bronnen(assessment, wiki)
    rol = [k for k in kandidaten if k.bron == "heffingsambtenaar"][0]
    assert (rol.relatie, rol.doel, rol.grondslag, rol.bronnen, rol.vindplaats) == (
        "assignment", "aanslag-opleggen", "bron", ["2026-overheid-gemeentewet"], "art. 231")
    opgetild = [k for k in kandidaten if k.doel == "beschikking"][0]  # Aanslagbedrag → bestaand element Beschikking
    assert (opgetild.bron, opgetild.relatie, opgetild.toegang) == ("aanslag-opleggen", "access", "schrijven")
    assert "opgetild" in opgetild.toelichting
    assert [v["naar"] for v in vervallen] == ["Rechtvaardige heffing"]


def test_uit_bronnen_verhuizend_begrip_krijgt_geen_element_id(wiki):
    assessment = {"voorstellen": [
        _voorstel("Verklaring", "element", "business-object", "bedrijfsarchitectuur/bedrijfsobjecten/tv/bd/verklaring.md", relaties_=[
            {"van": "Verklaring", "werkwoord": "wordt gevoegd bij", "naar": "Akte", "bronnen": ["2026-overheid-gemeentewet"]},
        ]),
        _voorstel("Akte", "element", "business-object", "begrippen/o.md"),
    ]}
    kandidaten, vervallen = relaties.uit_bronnen(assessment, wiki)
    assert kandidaten == []
    assert "geen elementpagina" in vervallen[0]["reden"] and "begrippen/o.md" in vervallen[0]["reden"]


def test_combineer_bevestigt_ggm_relatie_met_bron(wiki):
    ggm_k = relaties.voorstel("beschikking", DATA, wiki)
    bron_k = [relaties.Kandidaat("aggregation", "beschikking", "onderdeel-beschikking", "bevat", "", "bron", [],
                                 bronnen=["2026-overheid-gemeentewet"], vindplaats="art. 1")]
    samen = relaties.combineer(ggm_k, bron_k)
    (bevat,) = [k for k in samen if k.doel == "onderdeel-beschikking"]
    assert bevat.grondslag == "ggm-exact" and bevat.bronnen == ["2026-overheid-gemeentewet"]
    assert "bron noemt aggregation" in bevat.toelichting
    assert len(samen) == len(ggm_k)


def test_bronrelatie_zonder_bron_id_is_fout(wiki):
    pad = wiki / "bedrijfsarchitectuur/bedrijfsobjecten/tv/bd/zaak.md"
    pad.write_text(pad.read_text(encoding="utf-8") + (
        "\n## Relaties\n\n| Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie | Bron |\n|---|---|---|---|---|---|---|\n"
        "| associatie | [Besluit](besluit.md) | | | bron | | |\n"), encoding="utf-8")
    (r,) = relaties.alle_relaties(wiki)["zaak"]
    assert any("zonder bron-id" in f for f in r.fouten)
