"""tools/relaties.py: GGM-mapping, optillen, ketenen, ArchiMate-toets en relaties uit de bronanalyses."""
import pytest
import yaml

import relaties
from llmwiki import beoordeling


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


def _begrip(wiki, id_, naam, archimate="business-object", guid=None, soort="element", **extra):
    """Een afgeleide beoordeling: alleen wat relaties.py leest (naam, match, uitkomst)."""
    genoemd = extra.pop("genoemd", None)
    data = {"begrip": naam, **({"ggm": {"guid": guid, "sterkte": "exact", "onderbouwing": "x"}} if guid else {}),
            "status": "review" if soort == "element" else None, **extra,
            "beslist": {"uitkomst": {"soort": soort, "archimate_type": archimate, "genoemd_begrip": genoemd}}}
    beoordeling.schrijf(wiki / f"beoordelingen/begrippen/{id_}.yaml", {k: v for k, v in data.items() if v is not None})


@pytest.fixture
def wiki(archimate_repo):
    root, wiki = archimate_repo
    _begrip(wiki, "beschikking", "Beschikking", guid="G_BESCH",
            specialisaties=[{"naam": "Soort", "omschrijving": "x", "ggm_guid": "G_SUBTYPE"}])
    _begrip(wiki, "onderdeel-beschikking", "Onderdeel beschikking", guid="G_ONDER")
    _begrip(wiki, "besluit", "Besluit", guid="G_BESLUIT")
    _begrip(wiki, "aanvraag", "Aanvraag", guid="G_AANVR")
    _begrip(wiki, "zaak", "Zaak", guid="G_ZAAK")
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
    assert relaties.toegestaan("serving", "product", "business-role")
    assert not relaties.toegestaan("serving", "product", "business-process")
    assert not relaties.toegestaan("assignment", "business-object", "business-process")
    assert relaties.toegestaan("assignment", "business-actor", "business-role")
    assert not relaties.toegestaan("assignment", "business-role", "business-role")
    assert not relaties.toegestaan("assignment", "business-actor", "business-actor")


def test_voorstel_als_yaml_voor_de_beoordeling(wiki):
    k = relaties.voorstel("beschikking", DATA, wiki)
    tekst = relaties.yaml_voorstel("beschikking", k)
    uitgaand = yaml.safe_load(tekst)["relaties"]
    bevat = next(r for r in uitgaand if r["naar"] == "onderdeel-beschikking")
    assert bevat == {"soort": "compositie", "naar": "onderdeel-beschikking", "naam": "bevat", "kardinaliteit": "1 → 0..*",
                     "grondslag": "ggm-exact", "ggm_relatie": ["R_BEVAT"]}
    assert "# Inkomend" in tekst and "besluit -> specialisatie" in tekst


# --- Relaties uit de bronnen ---


@pytest.mark.parametrize("bron,doel,werkwoord,verwacht", [
    ("business-role", "business-process", "behandelt", ("assignment", False, None)),
    ("business-process", "business-object", "stelt vast", ("access", False, "registreren")),
    ("business-process", "business-object", "toetst aan", ("access", False, "raadplegen")),
    ("business-process", "business-object", "levert op", ("access", False, "registreren")),
    ("business-process", "business-object", "trekt in", ("access", False, "beëindigen")),
    ("business-process", "business-object", "vernietigt", ("access", False, "vernietigen")),
    ("business-role", "business-object", "houdt", ("access", False, "houder")),
    ("business-role", "business-object", "houdt bij", ("access", False, "bronhouder")),
    ("business-role", "contract", "heeft", ("access", False, "partij")),
    ("business-role", "business-object", "vraagt aan", ("association", False, None)),
    ("business-actor", "business-process", "draagt zorg voor", ("association", False, None)),
    ("business-function", "business-process", "ondersteunt", ("serving", False, None)),
    ("business-interface", "business-service", "ontsluit", ("assignment", False, None)),
    ("business-process", "business-object", "vereist", ("access", False, "raadplegen")),
    ("business-object", "business-process", "wordt behandeld in", ("access", True, "bijwerken")),
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


def test_uit_bronnen_lost_op_tilt_op_en_laat_vervallen(wiki):
    _begrip(wiki, "heffingsambtenaar", "Heffingsambtenaar", "business-role")
    _begrip(wiki, "aanslag-opleggen", "Aanslag opleggen", "business-process")
    _begrip(wiki, "aanslagbedrag", "Aanslagbedrag", None, soort="eigenschap", genoemd="Beschikking")
    _begrip(wiki, "rechtvaardige-heffing", "Rechtvaardige heffing", None, soort="buiten_model")
    _begrip(wiki, "verklaring", "Verklaring", status="afgewezen")
    rijen = [
        {"van": "Heffingsambtenaar", "werkwoord": "legt op", "naar": "Aanslag opleggen", "bronnen": ["2026-overheid-gemeentewet"], "vindplaats": "art. 231"},
        {"van": "Aanslag opleggen", "werkwoord": "stelt vast", "naar": "Aanslagbedrag", "bronnen": ["2026-utrecht-nota"]},
        {"van": "Aanslag opleggen", "werkwoord": "draagt bij aan", "naar": "Rechtvaardige heffing", "bronnen": ["2026-utrecht-nota"]},
        {"van": "Aanslag opleggen", "werkwoord": "stelt vast", "naar": "Verklaring", "bronnen": ["2026-utrecht-nota"]},
    ]
    kandidaten, vervallen = relaties.uit_bronnen(rijen, relaties.begrippen(wiki))
    rol = [k for k in kandidaten if k.bron == "heffingsambtenaar"][0]
    assert (rol.relatie, rol.doel, rol.grondslag, rol.bronnen, rol.vindplaats) == (
        "assignment", "aanslag-opleggen", "bron", ["2026-overheid-gemeentewet"], "art. 231")
    opgetild = [k for k in kandidaten if k.doel == "beschikking"][0]  # Aanslagbedrag → Beschikking
    assert (opgetild.bron, opgetild.relatie, opgetild.toegang) == ("aanslag-opleggen", "access", "registreren")
    assert "opgetild" in opgetild.toelichting
    assert [v["naar"] for v in vervallen] == ["Rechtvaardige heffing", "Verklaring"]
    assert "afgewezen" in vervallen[1]["reden"]


def test_bronrelaties_uit_de_relatietabel_van_een_bronanalyse(wiki):
    pad = wiki / "bronanalyses/o/rijksregelgeving/2026-overheid-gemeentewet.md"
    pad.parent.mkdir(parents=True)
    pad.write_text("# x\n\n## Relaties\n\n| Van | Werkwoord | Naar | Vindplaats |\n|---|---|---|---|\n"
                   "| Besluit | is een | Beschikking | art. 1 |\n", encoding="utf-8")
    (rij,) = relaties.bronrelaties(wiki)
    assert rij == {"van": "Besluit", "werkwoord": "is een", "naar": "Beschikking",
                   "bronnen": ["2026-overheid-gemeentewet"], "vindplaats": "art. 1"}


def test_combineer_bevestigt_ggm_relatie_met_bron(wiki):
    ggm_k = relaties.voorstel("beschikking", DATA, wiki)
    bron_k = [relaties.Kandidaat("aggregation", "beschikking", "onderdeel-beschikking", "bevat", "", "bron", [],
                                 bronnen=["2026-overheid-gemeentewet"], vindplaats="art. 1")]
    samen, alleen_ggm = relaties.combineer(ggm_k, bron_k)
    (bevat,) = samen
    assert bevat.doel == "onderdeel-beschikking"
    assert bevat.grondslag == "ggm-exact" and bevat.bronnen == ["2026-overheid-gemeentewet"]
    assert "bron noemt aggregation" in bevat.toelichting
    assert len(alleen_ggm) == len(ggm_k) - 1 and bevat not in alleen_ggm


def test_ggm_relatie_zonder_gevonden_relatie_is_geen_voorstel(wiki):
    ggm_k = relaties.voorstel("beschikking", DATA, wiki)
    samen, alleen_ggm = relaties.combineer(ggm_k, [])
    assert samen == [] and len(alleen_ggm) == len(ggm_k)
    tekst = relaties.yaml_voorstel("beschikking", samen, alleen_ggm, {"onderdeel-beschikking"})
    assert yaml.safe_load(tekst)["relaties"] is None
    assert "# Alleen in het GGM" in tekst and "R_BEVAT; staat al in de beoordeling: matchen" in tekst


def test_gemma_modelleerafspraken():
    # Actor alleen via een rol
    assert not relaties.toegestaan("assignment", "business-actor", "business-process")
    assert relaties.toegestaan("assignment", "business-role", "business-process")
    # Functie bedient proces, geen aggregatie
    assert not relaties.toegestaan("aggregation", "business-function", "business-process")
    assert relaties.toegestaan("serving", "business-function", "business-process")
    # Kanaal: toegewezen aan dienst, bedient rol
    assert relaties.toegestaan("assignment", "business-interface", "business-service")
    assert relaties.toegestaan("serving", "business-interface", "business-role")
    assert not relaties.toegestaan("assignment", "business-interface", "business-process")
    # Dienst: geen rol toegewezen, geen toegang tot een object
    assert not relaties.toegestaan("assignment", "business-role", "business-service")
    assert not relaties.toegestaan("access", "business-service", "business-object")


def test_toegangstype_volgt_uit_handeling_of_verantwoordelijkheid():
    assert relaties.toegangstype("beëindigen") == "schrijven"
    assert relaties.toegangstype("houder") == "lezen-schrijven"
    assert relaties.toegangstype("lezen") is None
