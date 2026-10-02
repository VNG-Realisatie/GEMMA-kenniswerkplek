"""tools/archimate_export.py: id's en mappen uit GEMMA, vaste id's voor nieuw, eigenschappen, selectie, determinisme."""
import xml.etree.ElementTree as ET

import archimate_export as ae
import gemma
from llmwiki import beoordeling, hashing

GEMMA = """<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:archimate="http://www.archimatetool.com/archimate" name="GEMMA" id="id-gemma" version="5.0.0">
  <folder name="Business" id="f-business" type="business">
    <folder name="Bedrijfsobjecten" id="f-bo">
      <documentation>Map van GEMMA</documentation>
      <element xsi:type="archimate:BusinessObject" name="Beschikking" id="id-beschikking" profiles="p-1">
        <documentation>Oude definitie.</documentation>
        <property key="Object ID" value="c481e8b8"/>
        <property key="wiki-gemma-model exportdatum" value="2026-01-01T00:00:00"/>
      </element>
    </folder>
    <element xsi:type="archimate:BusinessProcess" name="Behandelen aanvraag" id="id-proces"/>
  </folder>
  <folder name="Motivation" id="f-motivation" type="motivation"/>
  <folder name="Relations" id="f-rel" type="relations">
    <folder name="GGM" id="f-rel-ggm">
      <element xsi:type="archimate:AccessRelationship" id="r-lezen" source="id-proces" target="id-beschikking" accessType="1"/>
    </folder>
  </folder>
  <property key="Release" value="2026-07-01"/>
  <profile name="Kernobject" id="p-1" conceptType="BusinessObject"/>
</archimate:model>
"""


def _gemma(tmp_path):
    pad = tmp_path / "gemma.archimate"
    pad.write_text(GEMMA, encoding="utf-8")
    return gemma.parse(pad)


def _begrip(naam, atype, status="goedgekeurd", gemma_id=None, relaties=(), **extra):
    data = {"begrip": naam, "definitie": f"Definitie van {naam}.", "beschrijving": ["Uitleg."],
            "gemma": {"id": gemma_id, "sterkte": "sterk"} if gemma_id else {"sterkte": "geen"},
            "relaties": list(relaties), "status": status,
            "afgeleid": {"uitkomst": {"soort": "element", "archimate_type": atype, "paginatype": "bedrijfsobject"},
                         "bronnen": ["2026-bron"], "pad": f"x/{naam}.md"}, **extra}
    return {k: v for k, v in data.items() if v is not None}


def _log(begrippen):
    return "\n".join(f"- [2026-10-02] promote | {bid} | {hashing.short(beoordeling.inhoud_hash(d))}"
                     for bid, d in begrippen.items() if d["status"] == "goedgekeurd")


def _begrippen():
    return {
        "beschikking": _begrip("Beschikking", "business-object", gemma_id="id-beschikking",
                               taakveld="Bestuur", beleidsdomein="Besluitvorming"),
        "behandelen-aanvraag": _begrip("Behandelen aanvraag", "business-process", gemma_id="id-proces", relaties=[
            {"soort": "toegang (raadplegen)", "naar": "beschikking", "naam": "leest", "grondslag": "bron", "bronnen": ["2026-bron"]},
            {"soort": "toegang (registreren)", "naar": "beschikking", "grondslag": "bron", "bronnen": ["2026-bron"]},
            {"soort": "triggering", "naar": "graf", "grondslag": "bron", "bronnen": ["2026-bron"]},
            {"soort": "associatie (gericht)", "naar": "urn", "grondslag": "bron", "bronnen": ["2026-bron"]}]),
        "urn": _begrip("Urn", "business-object", taakveld="Lijkbezorging", beleidsdomein="Begraven",
                       synoniemen=[{"naam": "Asbus", "context": "wet"}]),
        "graf": _begrip("Graf", "business-object", status="review"),
    }


WIKI_YAML = {"page_types": {"bedrijfsobject": {"dir": "bedrijfsarchitectuur/bedrijfsobjecten"}}}


def _export(tmp_path, concept=False, tijd="2026-10-02T12:00:00", begrippen=None):
    begrippen = begrippen or _begrippen()
    uit = ae.bouw(_gemma(tmp_path), begrippen, "2026-vng-gemma", tijd, concept, _log(begrippen), WIKI_YAML)
    return uit, ET.fromstring(uit.xml)


def _el(root, eid):
    return next(e for e in root.iter("element") if e.get("id") == eid)


def _props(el):
    return {p.get("key"): p.get("value") for p in el.findall("property")}


def _pad(root, eid):
    """Namen en id's van de mappen boven het object."""
    ouders = {kind: ouder for ouder in root.iter() for kind in ouder}
    keten, huidig = [], ouders[_el(root, eid)]
    while huidig.tag == "folder":
        keten.insert(0, (huidig.get("name"), huidig.get("id")))
        huidig = ouders[huidig]
    return keten


def test_parse_archimate_levert_mappen_profielen_en_toegang(tmp_path):
    data = _gemma(tmp_path)
    assert data["mappen"]["f-bo"]["ouder"] == "f-business"
    assert data["elementen"]["id-beschikking"]["map_id"] == "f-bo"
    assert data["elementen"]["id-beschikking"]["profiel"] == "p-1"
    assert data["model"]["profielen"]["p-1"]["concept"] == "BusinessObject"
    assert data["model"]["eigenschappen"]["Release"] == "2026-07-01"
    assert data["relaties"]["r-lezen"]["toegang"] == 1


def test_gekoppeld_element_houdt_gemma_id_map_en_eigenschappen(tmp_path):
    uit, root = _export(tmp_path)
    assert not uit.fouten
    el = _el(root, "id-beschikking")
    assert el.get("name") == "Beschikking" and el.findtext("documentation") == "Definitie van Beschikking."
    assert el.get("profiles") == "p-1" and root.find("profile").get("id") == "p-1"
    assert _pad(root, "id-beschikking") == [("Business", "f-business"), ("Bedrijfsobjecten", "f-bo")]
    props = _props(el)
    assert props["Object ID"] == "c481e8b8"
    assert props["wiki-gemma-model exportdatum"] == "2026-10-02T12:00:00"
    assert props["wiki-gemma-model herkomst"] == "gekoppeld"
    assert props["wiki-gemma-model vorige definitie"] == "Oude definitie."
    assert "wiki-gemma-model vorige naam" not in props
    assert [p.get("key") for p in el.findall("property")].count("wiki-gemma-model exportdatum") == 1
    bo = next(f for f in root.iter("folder") if f.get("id") == "f-bo")
    assert bo.findtext("documentation") == "Map van GEMMA"


def test_nieuw_element_krijgt_vast_id_in_eigen_map(tmp_path):
    _, root = _export(tmp_path)
    eid = ae.vast_id("element", "urn")
    el = _el(root, eid)
    assert _props(el)["wiki-gemma-model herkomst"] == "nieuw"
    assert _props(el)["wiki-gemma-model synoniemen"] == "Asbus (wet)"
    assert "Object ID" not in _props(el)
    assert [n for n, _ in _pad(root, eid)] == ["Business", "wiki-gemma-model", "Bedrijfsobjecten", "Lijkbezorging", "Begraven"]


def test_relaties_hergebruiken_gemma_id_en_hebben_expliciet_toegangstype(tmp_path):
    uit, root = _export(tmp_path)
    lezen = _el(root, "r-lezen")
    assert lezen.get("accessType") == "1" and lezen.get("name") == "leest"
    assert _pad(root, "r-lezen") == [("Relations", "f-rel"), ("GGM", "f-rel-ggm")]
    schrijven = _el(root, ae.vast_id("relatie", "behandelen-aanvraag", "toegang (registreren)", "beschikking", ""))
    assert schrijven.get("accessType") == "0"
    gericht = _el(root, ae.vast_id("relatie", "behandelen-aanvraag", "associatie (gericht)", "urn", ""))
    assert gericht.get("directed") == "true"
    assert uit.relaties_gekoppeld == 1 and uit.relaties_nieuw == 2
    assert any("graf" in o for o in uit.overgeslagen)


def test_alleen_goedgekeurd_tenzij_concept(tmp_path):
    _, root = _export(tmp_path)
    assert ae.vast_id("element", "graf") not in {e.get("id") for e in root.iter("element")}
    uit, root = _export(tmp_path, concept=True)
    assert ae.vast_id("element", "graf") in {e.get("id") for e in root.iter("element")}
    assert root.get("name").startswith("CONCEPT")
    assert _props(_el(root, "id-beschikking"))["wiki-gemma-model soort export"] == "concept"


def test_goedgekeurd_zonder_logregel_is_fout(tmp_path):
    begrippen = _begrippen()
    uit = ae.bouw(_gemma(tmp_path), begrippen, "b", "t", False, "", WIKI_YAML)
    assert any("log.md" in f for f in uit.fouten)


def test_afwijkend_type_is_fout(tmp_path):
    begrippen = _begrippen()
    begrippen["beschikking"]["afgeleid"]["uitkomst"]["archimate_type"] = "contract"
    uit, _ = _export(tmp_path, begrippen=begrippen)
    assert any("wijkt af van GEMMA" in f for f in uit.fouten)


def test_verwijzingen_kloppen_en_export_is_deterministisch(tmp_path):
    uit1, root = _export(tmp_path)
    ids = {e.get("id") for e in root.iter("element")}
    for r in root.iter("element"):
        if r.get("source"):
            assert r.get("source") in ids and r.get("target") in ids
    mappen = [f.get("type") for f in root.findall("folder")]
    assert mappen == list(ae.BOVENSTE)
    uit2, _ = _export(tmp_path)
    assert uit1.xml == uit2.xml
    uit3, _ = _export(tmp_path, tijd="2026-10-03T08:00:00")
    assert uit3.xml.replace(b"2026-10-03T08:00:00", b"2026-10-02T12:00:00") == uit1.xml
