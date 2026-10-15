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
    assert (root / "sources" / "modellen" / "2026-vng-gemma-model.archimate").exists()
    assert (root / "sources" / "modellen" / "2026-vng-gemma-model.json").exists()  # de omzetting naar JSON
    assert gemma.laad(root / "sources" / "modellen" / "2026-vng-gemma-model.json")["model"]["formaat"] == "archimate"


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
    assert (root / "sources" / "modellen" / "2026-vng-gemma-2026-07-01.xml").exists()
    index = yaml.safe_load((root / "sources" / "index" / "2026-vng-gemma-2026-07-01.md").read_text(encoding="utf-8").split("---")[1])
    assert index["versie"] == "2026-07-01" and index["brontype"] == "model"


FUNCTIES = """<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:archimate="http://www.archimatetool.com/archimate" name="GEMMA" id="m1" version="5.0.0">
  <folder name="Business" id="f-business" type="business">
    <folder name="Bedrijfsfuncties" id="f-bf">
      <element xsi:type="archimate:BusinessFunction" name="Uitvoering Publieksdiensten" id="id-uitvoering">
        <property key="GEMMA type" value="Bedrijfsfunctie domein"/>
      </element>
      <element xsi:type="archimate:BusinessFunction" name="Realisatie" id="id-realisatie"/>
      <element xsi:type="archimate:BusinessFunction" name="Publicatie" id="id-publicatie"/>
      <element xsi:type="archimate:BusinessFunction" name="Burgerlijke stand" id="id-bs"/>
    </folder>
  </folder>
  <folder name="Other" id="f-other" type="other">
    <folder name="Domeinen" id="f-domeinen">
      <element xsi:type="archimate:Grouping" name="Publieksdiensten" id="id-domein"/>
      <element xsi:type="archimate:Grouping" name="Niet domeingebonden" id="id-niet"/>
    </folder>
    <element xsi:type="archimate:Grouping" name="Beleidsdomein" id="id-bd"/>
  </folder>
  <folder name="Relations" id="f-rel" type="relations">
    <element xsi:type="archimate:AggregationRelationship" id="r1" source="id-domein" target="id-uitvoering"/>
    <element xsi:type="archimate:AggregationRelationship" id="r2" source="id-uitvoering" target="id-realisatie"/>
    <element xsi:type="archimate:AggregationRelationship" id="r3" source="id-realisatie" target="id-bs"/>
    <element xsi:type="archimate:AggregationRelationship" id="r4" source="id-niet" target="id-publicatie"/>
    <element xsi:type="archimate:AggregationRelationship" id="r5" source="id-publicatie" target="id-bs"/>
    <element xsi:type="archimate:AggregationRelationship" id="r6" source="id-bd" target="id-bs"/>
    <element xsi:type="archimate:ServingRelationship" id="r7" source="id-bs" target="id-realisatie"/>
  </folder>
</archimate:model>
"""


def test_functiehierarchie_is_de_hierarchie_van_gemma_as_is(tmp_path):
    pad = tmp_path / "functies.archimate"
    pad.write_text(FUNCTIES, encoding="utf-8")
    data = gemma.parse_archimate(pad)
    h = gemma.functiehierarchie(data)
    # de wortels zijn de groeperingen in de map Domeinen die functies aggregeren; een andere groepering is geen knoop
    assert h["wortels"] == ["id-niet", "id-domein"]
    assert h["onder"]["id-realisatie"] == [("id-bs", "r3")]
    assert sorted(h["boven"]["id-bs"]) == [("id-publicatie", "r5"), ("id-realisatie", "r3")]  # een functie kan onder meer ouders
    assert "id-bd" not in h["boven"].get("id-bs", [])
    assert gemma.functie_tak(h, "id-realisatie") == ({"id-realisatie", "id-uitvoering", "id-domein"}, {"r1", "r2"})
    assert gemma.functie_tak(h, "id-bs")[1] == {"r1", "r2", "r3", "r4", "r5"}
    assert gemma.functie_paden(data, h, "id-bs") == [
        ["Niet domeingebonden", "Publicatie", "Burgerlijke stand"],
        ["Publieksdiensten", "Uitvoering Publieksdiensten", "Realisatie", "Burgerlijke stand"]]
    assert gemma.functie_domein_namen(data, h, "id-realisatie") == ["Publieksdiensten"]
    assert gemma.functie_domein_namen(data, h, "id-bs") == ["Niet domeingebonden", "Publieksdiensten"]


def test_kandidaten_naamgenoten_en_treffers_aan_het_begin_van_een_woord(tmp_path):
    data = _data(tmp_path)
    k = gemma.kandidaten(data, "Beschikking")
    assert [e["id"] for e in k["naamgenoten"]] == ["id-beschikking"]
    assert k["naamgenoten"][0]["groepering"] == ["Vergunningen"]
    assert [e["id"] for e in gemma.kandidaten(data, "besluit")["treffers"]] == ["id-beschikking"]  # in de definitie
    assert gemma.kandidaten(data, "schikking")["treffers"] == []
