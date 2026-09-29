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


AMEFF = """<?xml version="1.0" encoding="UTF-8"?>
<model xmlns="http://www.opengroup.org/xsd/archimate/3.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" identifier="id-model">
  <name xml:lang="nl">GEMMA</name>
  <properties><property propertyDefinitionRef="propid-75"><value xml:lang="nl">2026-07-01</value></property></properties>
  <elements>
    <element identifier="id-besch" xsi:type="BusinessObject">
      <name xml:lang="nl">Beschikking</name>
      <documentation xml:lang="nl">Besluit over een individueel geval.</documentation>
      <properties>
        <property propertyDefinitionRef="propid-6"><value xml:lang="nl">{0E19C86B-9088-41bd-9DD0-15094426570E}</value></property>
        <property propertyDefinitionRef="propid-11"><value xml:lang="nl">https://gemmaonline.nl/index.php/GEMMA/id-besch</value></property>
      </properties>
    </element>
    <element identifier="id-groep" xsi:type="Grouping"><name xml:lang="nl">Vergunningen</name></element>
  </elements>
  <relationships>
    <relationship identifier="id-r1" source="id-groep" target="id-besch" xsi:type="Aggregation"/>
  </relationships>
  <organizations>
    <item><label xml:lang="nl">Business</label>
      <item><label xml:lang="nl">Bedrijfsobjecten</label><item identifierRef="id-besch"/></item>
    </item>
    <item><label xml:lang="nl">Relations</label><item identifierRef="id-r1"/></item>
  </organizations>
  <propertyDefinitions>
    <propertyDefinition identifier="propid-6" type="string"><name>GGM-guid</name></propertyDefinition>
    <propertyDefinition identifier="propid-11" type="string"><name>GEMMA URL</name></propertyDefinition>
    <propertyDefinition identifier="propid-75" type="string"><name>Release</name></propertyDefinition>
  </propertyDefinitions>
</model>
"""


def test_ameff_wordt_herkend_en_gelijk_verwerkt(tmp_path):
    pad = tmp_path / "GEMMA release.xml"
    pad.write_text(AMEFF, encoding="utf-8")
    data = gemma.parse(pad)
    assert data["model"] == {"naam": "GEMMA", "eigenschappen": {"Release": "2026-07-01"}, "formaat": "ameff"}
    v = gemma.velden(data["elementen"]["id-besch"])
    assert v["gemma_type"] == "business-object" and v["gemma_map"] == "Business / Bedrijfsobjecten"
    assert v["gemma_eigenschappen"]["GEMMA URL"].endswith("id-besch")
    assert data["relaties"]["id-r1"]["type"] == "aggregation-relationship"
    assert gemma.groepering(data, "id-besch") == ["Vergunningen"]
    assert [e["id"] for e in gemma.koppel(data, "EAID_0E19C86B_9088_41bd_9DD0_15094426570E")] == ["id-besch"]


def test_archi_bronbestand_blijft_werken(tmp_path):
    pad = tmp_path / "gemma.archimate"
    pad.write_text(ARCHIMATE, encoding="utf-8")
    assert gemma.parse(pad)["model"]["formaat"] == "archimate"


def test_release_zonder_bestand_haalt_ameff_op(tmp_path, archimate_repo, monkeypatch):
    import yaml

    from llmwiki import fetch

    root, wiki = archimate_repo
    opgevraagd = []

    def nep_fetch(url, timeout=60):
        opgevraagd.append(url)
        return fetch.Opgehaald(inhoud=AMEFF.encode(), content_type="application/xml", url=url)

    monkeypatch.setattr(fetch, "fetch", nep_fetch)
    resultaat = gemma.release(None, "2026-vng-gemma-2026-07-01", "GEMMA", wiki_root=wiki)
    assert resultaat["formaat"] == "ameff" and resultaat["release"] == "2026-07-01"
    assert opgevraagd == ["https://raw.githubusercontent.com/VNG-Realisatie/GEMMA-Archi-repository/master/export/GEMMA%20release.xml"]
    assert (root / "sources" / "raw" / "2026-vng-gemma-2026-07-01.xml").exists()
    index = yaml.safe_load((root / "sources" / "index" / "2026-vng-gemma-2026-07-01.md").read_text(encoding="utf-8").split("---")[1])
    assert index["versie"] == "2026-07-01" and index["brontype"] == "model"
