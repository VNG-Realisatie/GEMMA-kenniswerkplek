"""tools/gemma.py: parsen van een Archi-bronbestand, matchen op GGM-GUID, velden en groepering."""
import gemma

ARCHIMATE = """<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:archimate="http://www.archimatetool.com/archimate" name="GEMMA" id="m1" version="5.0.0">
  <folder name="Business" id="f-business" type="business">
    <folder name="Bedrijfsobjecten" id="f-bo">
      <element xsi:type="archimate:BusinessObject" name="Beschikking" id="id-beschikking">
        <documentation>Besluit over een individueel geval.</documentation>
        <property key="GGM-guid" value="{0E19C86B-9088-41bd-9DD0-15094426570E}"/>
        <property key="GEMMA-url" value="https://www.gemmaonline.nl/wiki/Beschikking"/>
      </element>
    </folder>
    <element xsi:type="archimate:BusinessRole" name="Aanvrager" id="id-aanvrager"/>
  </folder>
  <folder name="Other" id="f-other" type="other">
    <element xsi:type="archimate:Grouping" name="Vergunningen" id="id-groep"/>
  </folder>
  <folder name="Relations" id="f-rel" type="relations">
    <element xsi:type="archimate:AggregationRelationship" id="r1" source="id-groep" target="id-beschikking"/>
    <element xsi:type="archimate:AssociationRelationship" id="r2" source="id-aanvrager" target="id-beschikking"/>
  </folder>
  <folder name="Views" id="f-views" type="diagrams">
    <element xsi:type="archimate:ArchimateDiagramModel" name="Overzicht" id="v1"/>
  </folder>
</archimate:model>
"""


def _data(tmp_path):
    pad = tmp_path / "gemma.archimate"
    pad.write_text(ARCHIMATE, encoding="utf-8")
    return gemma.parse_archimate(pad)


def test_parse_elementen_relaties_en_map(tmp_path):
    data = _data(tmp_path)
    assert set(data["elementen"]) == {"id-beschikking", "id-aanvrager", "id-groep"}
    assert data["elementen"]["id-beschikking"]["map"] == "Business / Bedrijfsobjecten"
    assert data["relaties"]["r1"]["type"] == "aggregation-relationship"


def test_koppel_op_ggm_guid_in_ander_formaat(tmp_path):
    data = _data(tmp_path)
    gevonden = gemma.koppel(data, "EAID_0E19C86B_9088_41bd_9DD0_15094426570E")
    assert [e["id"] for e in gevonden] == ["id-beschikking"]


def test_velden_en_groepering(tmp_path):
    data = _data(tmp_path)
    v = gemma.velden(data["elementen"]["id-beschikking"])
    assert v["gemma_type"] == "business-object"
    assert v["gemma_eigenschappen"]["GEMMA-url"].endswith("/Beschikking")
    assert gemma.groepering(data, "id-beschikking") == ["Vergunningen"]


def test_release_zet_modelbron(tmp_path, archimate_repo):
    root, wiki = archimate_repo
    pad = tmp_path / "gemma.archimate"
    pad.write_text(ARCHIMATE, encoding="utf-8")
    assert gemma.release(pad, "2026-vng-gemma-model", "GEMMA", wiki_root=wiki)["elementen"] == 3
    assert "gemma:\n  bron: 2026-vng-gemma-model" in (wiki / "wiki.yaml").read_text(encoding="utf-8")
    assert (root / "sources" / "raw" / "2026-vng-gemma-model.archimate").exists()
