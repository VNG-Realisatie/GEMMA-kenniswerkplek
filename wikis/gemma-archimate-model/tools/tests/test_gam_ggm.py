"""tools/ggm.py: parser, bevragingen, velden, release en verrijken (met een klein XMI-fixture)."""
import json

import yaml
from gam_hulp import KENMERKEN_BO, element_tekst

import ggm
import gam_gemeen

XMI = """<?xml version="1.0" encoding="UTF-8"?>
<xmi:XMI xmi:version="2.1" xmlns:uml="http://schema.omg.org/spec/UML/2.1" xmlns:xmi="http://schema.omg.org/spec/XMI/2.1">
 <uml:Model xmi:type="uml:Model" name="GGM">
  <packagedElement xmi:type="uml:Package" xmi:id="P_TV" name="1 Veiligheid">
   <packagedElement xmi:type="uml:Package" xmi:id="P_BD" name="Vergunningen">
    <packagedElement xmi:type="uml:Class" xmi:id="EAID_BESCHIKKING" name="Beschikking">
     <ownedAttribute xmi:id="A1" name="datumBesluit"/>
    </packagedElement>
    <packagedElement xmi:type="uml:Class" xmi:id="EAID_ONDERDEEL" name="Onderdeel beschikking"/>
    <packagedElement xmi:type="uml:Class" xmi:id="EAID_BESLUIT" name="Besluit">
     <generalization xmi:type="uml:Generalization" xmi:id="EAID_GEN1" general="EAID_BESCHIKKING"/>
    </packagedElement>
    <packagedElement xmi:type="uml:Enumeration" xmi:id="EAID_SOORT" name="Soort besluit">
     <ownedAttribute xmi:id="L1" name="Weigering"/>
    </packagedElement>
    <packagedElement xmi:type="uml:Association" xmi:id="EAID_AGG1" name="bevat">
     <ownedEnd xmi:id="EAID_src1" aggregation="composite"><type xmi:idref="EAID_BESCHIKKING"/></ownedEnd>
     <ownedEnd xmi:id="EAID_dst1"><type xmi:idref="EAID_ONDERDEEL"/></ownedEnd>
    </packagedElement>
   </packagedElement>
  </packagedElement>
  <packagedElement xmi:type="uml:Package" xmi:id="P_TV2" name="2 Anders">
   <packagedElement xmi:type="uml:Package" xmi:id="P_BD2" name="Musea">
    <packagedElement xmi:type="uml:Class" xmi:id="EAID_BESCHIKKING2" name="Beschikking"/>
   </packagedElement>
  </packagedElement>
 </uml:Model>
 <xmi:Extension extender="Enterprise Architect">
  <elements>
   <element xmi:idref="P_TV" xmi:type="uml:Package" name="1 Veiligheid"><properties stereotype="Domein"/><model package="ROOT"/></element>
   <element xmi:idref="P_BD" xmi:type="uml:Package" name="Vergunningen"><properties stereotype="Domein"/></element>
   <element xmi:idref="P_TV2" xmi:type="uml:Package" name="2 Anders"><properties stereotype="Domein"/></element>
   <element xmi:idref="P_BD2" xmi:type="uml:Package" name="Musea"><properties stereotype="Domein"/></element>
   <element xmi:idref="EAID_BESCHIKKING" xmi:type="uml:Class" name="Beschikking">
    <properties documentation="Een &lt;b&gt;besluit&lt;/b&gt; over een individueel geval." stereotype="Objecttype"/>
    <tags><tag name="Synoniemen" value="Besluit op aanvraag"/><tag name="Toelichting" value="Toelichting#NOTES#notitie"/></tags>
   </element>
   <element xmi:idref="EAID_ONDERDEEL" xmi:type="uml:Class" name="Onderdeel beschikking"><properties documentation="Deel" stereotype="Objecttype"/></element>
   <element xmi:idref="EAID_BESLUIT" xmi:type="uml:Class" name="Besluit"><properties documentation="Besluit" stereotype="Objecttype"/></element>
   <element xmi:idref="EAID_BESCHIKKING2" xmi:type="uml:Class" name="Beschikking"><properties documentation="Ander begrip" stereotype="Objecttype"/></element>
  </elements>
  <connectors>
   <connector xmi:idref="EAID_AGG1">
    <source xmi:idref="EAID_BESCHIKKING"><type multiplicity="1" aggregation="composite"/></source>
    <target xmi:idref="EAID_ONDERDEEL"><type multiplicity="1..*" aggregation="none"/></target>
    <properties ea_type="Aggregation" subtype="Strong"/>
    <labels lb="1" rb="1..*" mt="bevat"/>
    <documentation value="De &lt;i&gt;onderdelen&lt;/i&gt; van een beschikking | per besluit."/>
   </connector>
   <connector xmi:idref="EAID_GEN1">
    <source xmi:idref="EAID_BESLUIT"/><target xmi:idref="EAID_BESCHIKKING"/>
    <properties ea_type="Generalization"/><labels mt="is een"/>
   </connector>
  </connectors>
  <diagrams>
   <diagram xmi:id="D1"><properties name="Diagram Vergunningen"/><elements><element subject="EAID_BESCHIKKING"/></elements></diagram>
  </diagrams>
 </xmi:Extension>
</xmi:XMI>
"""


def _xmi(tmp_path):
    pad = tmp_path / "ggm.xml"
    pad.write_text(XMI, encoding="utf-8")
    return pad


def test_parser_domein_relaties_en_deel_geheel(tmp_path):
    data = ggm.parse_xmi(_xmi(tmp_path))
    b = data["entities"]["EAID_BESCHIKKING"]
    assert (b["taakveld"], b["beleidsdomein"]) == ("1 Veiligheid", "Vergunningen")
    assert data["entities"]["EAID_SOORT"]["literals"] == ["Weigering"]
    agg = data["relations"]["EAID_AGG1"]
    assert agg["aggregatie"] == "composite" and ggm.geheel_en_deel(agg) == ("EAID_BESCHIKKING", "EAID_ONDERDEEL")
    gen = data["relations"]["EAID_GEN1"]
    assert gen["uml_type"] == "Generalization" and gen["name"] == "is een"
    assert (gen["source_id"], gen["target_id"]) == ("EAID_BESLUIT", "EAID_BESCHIKKING")


def test_domeinpagina_toont_guid_en_definitie_van_relaties(tmp_path):
    data = ggm.parse_xmi(_xmi(tmp_path))
    pagina = ggm.domein_pagina(data, "1 Veiligheid", "Vergunningen")
    assert "## Beschikking" in pagina
    rij = next(r for r in pagina.splitlines() if r.startswith("- ") and "`EAID_AGG1`" in r)
    assert "*Aggregation" in rij
    assert rij.endswith(": De onderdelen van een beschikking | per besluit.")


def test_velden_zijn_letterlijk_en_zonder_lege_waarden(tmp_path):
    data = ggm.parse_xmi(_xmi(tmp_path))
    v = ggm.velden(data["entities"]["EAID_BESCHIKKING"])
    assert v["ggm_definitie"] == "Een besluit over een individueel geval."
    assert v["ggm_toelichting"] == "Toelichting"
    assert v["ggm_diagram"] == ["Diagram Vergunningen"]
    assert "ggm_herkomst" not in v


def test_bevragingen(tmp_path):
    data = ggm.parse_xmi(_xmi(tmp_path))
    assert {e["beleidsdomein"] for e in ggm.naamgenoten(data, "beschikking")} == {"Vergunningen", "Musea"}
    assert ggm.attribuut(data, "weigering")[0]["als"] == "waarde"
    assert ggm.generalisaties(data, "EAID_BESCHIKKING")["specialisaties"] == ["EAID_BESLUIT"]
    assert any(e["id"] == "EAID_BESCHIKKING" for e in ggm.zoek(data, "op aanvraag"))


def test_release_schrijft_bron_json_paginas_en_wiki_yaml(tmp_path, archimate_repo):
    root, wiki = archimate_repo
    resultaat = ggm.release(_xmi(tmp_path), "2024-vng-ggm-test", "GGM test", wiki_root=wiki)
    assert resultaat["entiteiten"] == 5
    assert (root / "sources" / "raw" / "2024-vng-ggm-test.xml").exists()
    index = yaml.safe_load((root / "sources" / "index" / "2024-vng-ggm-test.md").read_text(encoding="utf-8").split("---")[1])
    assert index["brontype"] == "model"
    assert "bron: 2024-vng-ggm-test" in (wiki / "wiki.yaml").read_text(encoding="utf-8")
    pagina = wiki / "ggm" / "1-veiligheid" / "vergunningen.md"
    assert gam_gemeen.controleer_gegenereerd(pagina) is None
    assert gam_gemeen.controleer_json_gegenereerd(wiki / "ggm" / "ggm_parsed.json") is None
    pagina.write_text(pagina.read_text(encoding="utf-8") + "handmatig\n", encoding="utf-8")
    assert "met de hand gewijzigd" in gam_gemeen.controleer_gegenereerd(pagina)


def test_kandidaten_voor_de_match_op_betekenis(tmp_path):
    data = ggm.parse_xmi(_xmi(tmp_path))
    k = ggm.kandidaten(data, "Beschikking")
    assert [n["guid"] for n in k["naamgenoten"]] == ["EAID_BESCHIKKING", "EAID_BESCHIKKING2"]  # duplicaat of homoniem
    assert k["naamgenoten"][0]["definitie"] == "Een besluit over een individueel geval."
    assert k["naamgenoten"][0]["specialisaties"] == ["Besluit"]
    assert ggm.kandidaten(data, "schikking")["treffers"] == []  # alleen treffers aan het begin van een woord


def test_release_zonder_bestand_haalt_op_van_herkomst(tmp_path, archimate_repo, monkeypatch):
    from llmwiki import fetch

    root, wiki = archimate_repo
    opgevraagd = []

    def nep_fetch(url, timeout=60):
        opgevraagd.append(url)
        return fetch.Opgehaald(inhoud=XMI.encode(), content_type="application/xml", url=url)

    monkeypatch.setattr(fetch, "fetch", nep_fetch)
    ggm.release(None, "2026-vng-ggm-2-5-1", "GGM 2.5.1", wiki_root=wiki)
    assert opgevraagd == ["https://raw.githubusercontent.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/"
                          "Voorbereidingen-Release-v2.5.1/v2.5.1/Gemeentelijk%20Gegevensmodel%20XMI2.1.xml"]
    index = yaml.safe_load((root / "sources" / "index" / "2026-vng-ggm-2-5-1.md").read_text(encoding="utf-8").split("---")[1])
    assert index["url"] == opgevraagd[0]
    assert index["url_pagina"].startswith("https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/")
    assert "bron: 2026-vng-ggm-2-5-1" in (wiki / "wiki.yaml").read_text(encoding="utf-8")
