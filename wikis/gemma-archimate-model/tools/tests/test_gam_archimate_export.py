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
    # de twee bedrijfsobjecten met een beleidsdomein krijgen elk een aggregatie vanuit een nieuwe groepering
    assert uit.relaties_gekoppeld == 1 and uit.relaties_nieuw == 4
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


GEMMA_INDELING = """<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:archimate="http://www.archimatetool.com/archimate" name="GEMMA" id="id-gemma" version="5.0.0">
  <folder name="Business" id="f-business" type="business">
    <folder name="Bedrijfsprocessen" id="f-proc">
      <element xsi:type="archimate:BusinessProcess" name="Behandelen aanvraag vergunning of ontheffing" id="id-generiek"/>
      <element xsi:type="archimate:BusinessEvent" name="Aanvraag ontvangen" id="id-gebeurtenis"/>
    </folder>
    <folder name="Bedrijfsrollen" id="f-rol">
      <element xsi:type="archimate:BusinessRole" name="Inwoners en ondernemers" id="id-doelgroep-inwoners">
        <property key="GEMMA type" value="Groep"/>
      </element>
    </folder>
    <folder name="Actoren en rollen" id="f-ar">
      <element xsi:type="archimate:BusinessRole" name="Inwoners en ondernemers" id="id-aaa-rol-zonder-groep"/>
    </folder>
    <folder name="Bedrijfsobjecten" id="f-bo">
      <element xsi:type="archimate:BusinessObject" name="Beschikking" id="id-beschikking"/>
    </folder>
    <folder name="Bedrijfsfuncties" id="f-bf">
      <element xsi:type="archimate:BusinessFunction" name="Uitvoering fysieke leefomgeving" id="id-uitvoering-fl">
        <property key="GEMMA type" value="Bedrijfsfunctie domein"/>
      </element>
    </folder>
  </folder>
  <folder name="Other" id="f-other" type="other">
    <folder name="Domein en doelgroep" id="f-dd">
      <folder name="Domeinen" id="f-domeinen">
        <element xsi:type="archimate:Grouping" name="Fysieke leefomgeving" id="id-domein-fl"/>
      </folder>
    </folder>
    <folder name="Beleidsdomeinen" id="f-bd">
      <element xsi:type="archimate:Grouping" name="Besluitvorming" id="id-bd-besluitvorming">
        <property key="GEMMA type" value="Beleidsdomein"/>
      </element>
      <element xsi:type="archimate:Grouping" name="Bestuur" id="id-taakveld-bestuur">
        <property key="GEMMA type" value="Taakveld Iv3"/>
      </element>
    </folder>
  </folder>
  <folder name="Relations" id="f-rel" type="relations">
    <element xsi:type="archimate:AggregationRelationship" id="r-agg-bd" source="id-bd-besluitvorming" target="id-beschikking"/>
    <element xsi:type="archimate:AggregationRelationship" id="r-agg-fl" source="id-domein-fl" target="id-uitvoering-fl"/>
  </folder>
</archimate:model>
"""


def _indeling_begrippen():
    def element(naam, atype, paginatype, **extra):
        data = _begrip(naam, atype, status="review", **extra)
        data["afgeleid"]["uitkomst"]["paginatype"] = paginatype
        return data

    beschikking = element("Beschikking", "business-object", "bedrijfsobject", gemma_id="id-beschikking",
                          taakveld="Bestuur", beleidsdomein="Besluitvorming")
    beschikking["afgeleid"]["uitkomst"]["objectniveau"] = "generiek"
    taak = element("Verzorgen lijkbezorging", "business-process", "bedrijfsproces",
                   relaties=[{"soort": "aggregatie", "naar": "opgraven-lijk", "grondslag": "bron", "bronnen": ["2026-bron"]}])
    taak["afgeleid"]["uitkomst"]["procesniveau"] = "taak"
    deel = element("Opgraven lijk", "business-process", "bedrijfsproces", taakveld="Volksgezondheid",
                   beleidsdomein="Begraafplaatsen", kernobject="lijk", afnemer="extern",
                   gemma_generiek={"id": "id-generiek", "onderbouwing": "Een vergunningaanvraag."},
                   relaties=[{"soort": "toegang (registreren)", "naar": "beschikking", "grondslag": "bron",
                              "bronnen": ["2026-bron"], "via": "vergunning-tot-opgraving"}])
    deel["afgeleid"]["uitkomst"]["procesniveau"] = "deelproces"
    lijk = element("Lijk", "business-object", "bedrijfsobject", taakveld="Volksgezondheid", beleidsdomein="Begraafplaatsen")
    lijk["afgeleid"]["uitkomst"]["objectniveau"] = "kernobject"
    functie = element("Exploiteren van begraafplaatsen", "business-function", "bedrijfsfunctie", domein="Fysieke leefomgeving")
    domeinfunctie = element("Uitvoering fysieke leefomgeving", "business-function", "bedrijfsfunctie",
                            gemma_id="id-uitvoering-fl", domein="Fysieke leefomgeving",
                            relaties=[{"soort": "aggregatie", "naar": "exploiteren", "grondslag": "bron", "bronnen": ["2026-bron"]}])
    nabestaande = element("Nabestaande", "business-role", "rol", doelgroep="inwoners en ondernemers")
    zonder = element("Gemeente", "business-actor", "actor", doelgroep="onbekende groep")
    specialisatie = {"begrip": "Vergunning tot opgraving", "status": "review"}
    return {"beschikking": beschikking, "verzorgen-lijkbezorging": taak, "opgraven-lijk": deel, "lijk": lijk,
            "exploiteren": functie, "uitvoering-fl": domeinfunctie, "nabestaande": nabestaande, "gemeente": zonder,
            "vergunning-tot-opgraving": specialisatie}


def _export_indeling(tmp_path, begrippen=None):
    pad = tmp_path / "gemma-indeling.archimate"
    pad.write_text(GEMMA_INDELING, encoding="utf-8")
    begrippen = begrippen or _indeling_begrippen()
    gemma_data = gemma.parse(pad)
    uit = ae.bouw(gemma_data, begrippen, "2026-vng-gemma", "2026-10-04T12:00:00", True, "", WIKI_YAML)
    return uit, ET.fromstring(uit.xml)


def _relaties_van(root, rtype, bron=None, doel=None):
    return [e for e in root.iter("element") if e.get("{http://www.w3.org/2001/XMLSchema-instance}type") == rtype
            and (bron is None or e.get("source") == bron) and (doel is None or e.get("target") == doel)]


def test_elementen_krijgen_niveau_en_indelingsvelden_als_eigenschap(tmp_path):
    uit, root = _export_indeling(tmp_path)
    assert not uit.fouten, uit.fouten
    deel = _props(_el(root, ae.vast_id("element", "opgraven-lijk")))
    assert deel["wiki-gemma-model procesniveau"] == "deelproces" and deel["wiki-gemma-model afnemer"] == "extern"
    assert deel["wiki-gemma-model kernobject"] == "lijk"
    assert _props(_el(root, ae.vast_id("element", "lijk")))["wiki-gemma-model objectniveau"] == "kernobject"
    assert _props(_el(root, ae.vast_id("element", "exploiteren")))["wiki-gemma-model domein"] == "Fysieke leefomgeving"
    assert _props(_el(root, "id-beschikking"))["wiki-gemma-model objectniveau"] == "generiek"


def test_processen_staan_in_de_map_procesindeling_naar_taak(tmp_path):
    _, root = _export_indeling(tmp_path)
    namen = [n for n, _ in _pad(root, ae.vast_id("element", "opgraven-lijk"))]
    assert namen == ["Business", "wiki-gemma-model", "Procesindeling naar taak", "Volksgezondheid", "Begraafplaatsen"]


def test_aggregatie_tussen_processen_heeft_indeling_en_niveau(tmp_path):
    _, root = _export_indeling(tmp_path)
    (agg,) = _relaties_van(root, "archimate:AggregationRelationship", ae.vast_id("element", "verzorgen-lijkbezorging"),
                           ae.vast_id("element", "opgraven-lijk"))
    props = _props(agg)
    assert props["wiki-gemma-model indeling"] == "Procesindeling naar taak"
    assert props["wiki-gemma-model procesniveau"] == "taak → deelproces"


def test_via_wordt_een_eigenschap_van_de_relatie(tmp_path):
    _, root = _export_indeling(tmp_path)
    (toegang,) = _relaties_van(root, "archimate:AccessRelationship", ae.vast_id("element", "opgraven-lijk"))
    assert _props(toegang)["wiki-gemma-model specialisatie"] == "Vergunning tot opgraving"


def test_gemma_generiek_wordt_een_specialisatie_naar_het_gemma_element(tmp_path):
    uit, root = _export_indeling(tmp_path)
    (spec,) = _relaties_van(root, "archimate:SpecializationRelationship", ae.vast_id("element", "opgraven-lijk"), "id-generiek")
    assert _props(spec)["wiki-gemma-model indeling"] == "Procesindeling naar soort werk"
    generiek = _el(root, "id-generiek")  # het GEMMA-element gaat letterlijk mee, zonder wiki-eigenschappen
    assert generiek.get("name") == "Behandelen aanvraag vergunning of ontheffing"
    assert not any(k.startswith("wiki-gemma-model") for k in _props(generiek))
    assert _pad(root, "id-generiek") == [("Business", "f-business"), ("Bedrijfsprocessen", "f-proc")]
    assert uit.specialisaties == ["Opgraven lijk → Behandelen aanvraag vergunning of ontheffing"]


def test_gemma_generiek_met_ander_type_is_een_fout(tmp_path):
    begrippen = _indeling_begrippen()
    begrippen["opgraven-lijk"]["gemma_generiek"] = {"id": "id-gebeurtenis", "onderbouwing": "Verkeerd type."}
    uit, _ = _export_indeling(tmp_path, begrippen)
    assert any("een specialisatie heeft hetzelfde type" in f for f in uit.fouten)


def test_beleidsdomein_uit_gemma_wordt_hergebruikt_en_een_onbekende_wordt_nieuw(tmp_path):
    uit, root = _export_indeling(tmp_path)
    # Besluitvorming bestaat in GEMMA, met een eigen aggregatie die haar id behoudt
    assert _el(root, "r-agg-bd").get("source") == "id-bd-besluitvorming"
    assert _props(_el(root, "r-agg-bd"))["wiki-gemma-model indeling"] == "Beleidsdomeinindeling"
    assert _el(root, "id-bd-besluitvorming").get("name") == "Besluitvorming"
    # Begraafplaatsen niet: een nieuwe groepering in de map van de wiki, zonder taakveld in GEMMA
    nieuw = _el(root, ae.vast_id("groepering", "beleidsdomein", "Begraafplaatsen"))
    assert nieuw.get("name") == "Begraafplaatsen" and _props(nieuw)["GEMMA type"] == "Beleidsdomein"
    assert [n for n, _ in _pad(root, nieuw.get("id"))] == ["Other", "wiki-gemma-model", "Beleidsdomeinindeling", "Volksgezondheid"]
    assert uit.groeperingen_nieuw == ["Begraafplaatsen (taakveld Volksgezondheid)"]
    assert _relaties_van(root, "archimate:AggregationRelationship", nieuw.get("id"), ae.vast_id("element", "lijk"))


def test_domein_en_doelgroep_aggregeren_vanuit_de_gemma_groepering(tmp_path):
    uit, root = _export_indeling(tmp_path)
    # een functie hangt alleen op domeinniveau aan de domeingroepering, daaronder aan haar bovenliggende functie
    assert _el(root, "r-agg-fl").get("source") == "id-domein-fl"
    assert not _relaties_van(root, "archimate:AggregationRelationship", "id-domein-fl", ae.vast_id("element", "exploiteren"))
    (agg,) = _relaties_van(root, "archimate:AggregationRelationship", "id-uitvoering-fl", ae.vast_id("element", "exploiteren"))
    assert _props(agg)["wiki-gemma-model indeling"] == "Functie-indeling naar domein"
    # de doelgroep is de GEMMA-rol met GEMMA type Groep, niet een gewone rol met dezelfde naam
    assert _relaties_van(root, "archimate:AggregationRelationship", "id-doelgroep-inwoners", ae.vast_id("element", "nabestaande"))
    assert not _relaties_van(root, "archimate:AggregationRelationship", "id-aaa-rol-zonder-groep")
    assert _pad(root, "id-doelgroep-inwoners") == [("Business", "f-business"), ("Bedrijfsrollen", "f-rol")]
    assert any("onbekende groep" in o for o in uit.overgeslagen)


def test_indelingen_geven_geen_dubbele_ids_en_geen_dangling_relaties(tmp_path):
    _, root = _export_indeling(tmp_path)
    ids = [e.get("id") for e in root.iter("element")]
    assert len(ids) == len(set(ids))
    for r in root.iter("element"):
        if r.get("source"):
            assert r.get("source") in ids and r.get("target") in ids, r.attrib


def test_rapport_noemt_specialisaties_en_nieuwe_groeperingen(tmp_path):
    uit, _ = _export_indeling(tmp_path)
    rapport = ae.rapport_md(uit, "2026-10-04T12:00:00", "2026-vng-gemma", True)
    assert "## Specialisaties naar een GEMMA-element" in rapport
    assert "- Opgraven lijk → Behandelen aanvraag vergunning of ontheffing" in rapport
    assert "## Nieuwe groeperingen" in rapport and "- Begraafplaatsen (taakveld Volksgezondheid)" in rapport


def test_functie_zonder_bovenliggende_functie_heeft_geen_plaats(tmp_path):
    begrippen = _indeling_begrippen()
    begrippen["uitvoering-fl"]["relaties"] = []
    uit, root = _export_indeling(tmp_path, begrippen)
    assert not _relaties_van(root, "archimate:AggregationRelationship", "id-domein-fl", ae.vast_id("element", "exploiteren"))
    assert any("Exploiteren van begraafplaatsen: geen plaats in de Functie-indeling naar domein" in o for o in uit.overgeslagen)


def test_dienst_hangt_onder_haar_functie_en_niet_onder_de_domeingroepering(tmp_path):
    begrippen = _indeling_begrippen()
    dienst = _begrip("Graf aanvragen", "business-service", status="review", domein="Fysieke leefomgeving", afnemer="extern")
    dienst["afgeleid"]["uitkomst"]["paginatype"] = "dienst"
    begrippen["graf-aanvragen"] = dienst
    zonder = _begrip("Losse dienst", "business-service", status="review", domein="Fysieke leefomgeving", afnemer="extern")
    zonder["afgeleid"]["uitkomst"]["paginatype"] = "dienst"
    begrippen["losse-dienst"] = zonder
    begrippen["exploiteren"]["relaties"] = [{"soort": "aggregatie", "naar": "graf-aanvragen", "grondslag": "bron", "bronnen": ["2026-bron"]}]
    uit, root = _export_indeling(tmp_path, begrippen)
    (agg,) = _relaties_van(root, "archimate:AggregationRelationship", ae.vast_id("element", "exploiteren"), ae.vast_id("element", "graf-aanvragen"))
    assert _props(agg)["wiki-gemma-model indeling"] == "Functie-indeling naar domein"
    assert not _relaties_van(root, "archimate:AggregationRelationship", "id-domein-fl", ae.vast_id("element", "graf-aanvragen"))
    assert any("Losse dienst: geen plaats in de Functie-indeling naar domein" in o for o in uit.overgeslagen)



def test_product_hangt_aan_de_domeingroepering(tmp_path):
    # ArchiMate laat een functie geen product aggregeren: het product hangt via domein aan de groepering (2026-10-05)
    begrippen = _indeling_begrippen()
    product = _begrip("Grafuitgifte", "product", status="review", domein="Fysieke leefomgeving", afnemer="extern")
    product["afgeleid"]["uitkomst"]["paginatype"] = "product"
    begrippen["grafuitgifte"] = product
    uit, root = _export_indeling(tmp_path, begrippen)
    (agg,) = _relaties_van(root, "archimate:AggregationRelationship", "id-domein-fl", ae.vast_id("element", "grafuitgifte"))
    assert _props(agg)["wiki-gemma-model indeling"] == "Functie-indeling naar domein"
    assert not any("Grafuitgifte" in o for o in uit.overgeslagen)

def test_element_zonder_plaats_in_een_indeling_wordt_gemeld(tmp_path):
    uit, _ = _export_indeling(tmp_path)
    # alleen de actor met een onbekende doelgroep staat nergens
    assert uit.zonder_plaats == ["Gemeente", "Verzorgen lijkbezorging"]


def test_gebeurtenis_hangt_onder_het_proces_in_de_procesindeling_naar_taak(tmp_path):
    begrippen = _indeling_begrippen()
    gebeurtenis = _begrip("Overlijden", "business-event", status="review")
    gebeurtenis["afgeleid"]["uitkomst"]["paginatype"] = "gebeurtenis"
    begrippen["overlijden"] = gebeurtenis
    uit, root = _export_indeling(tmp_path, begrippen)
    assert "Overlijden" in uit.zonder_plaats
    begrippen["opgraven-lijk"]["relaties"].append(
        {"soort": "aggregatie", "naar": "overlijden", "grondslag": "bron", "bronnen": ["2026-bron"]})
    uit, root = _export_indeling(tmp_path, begrippen)
    (agg,) = _relaties_van(root, "archimate:AggregationRelationship", ae.vast_id("element", "opgraven-lijk"),
                           ae.vast_id("element", "overlijden"))
    assert _props(agg)["wiki-gemma-model indeling"] == "Procesindeling naar taak"
    assert "Overlijden" not in uit.zonder_plaats


def test_taak_hangt_onder_haar_beleidsdomein_en_zonder_beleidsdomein_heeft_zij_geen_plaats(tmp_path):
    begrippen = _indeling_begrippen()
    begrippen["verzorgen-lijkbezorging"].update(taakveld="Volksgezondheid", beleidsdomein="Begraafplaatsen")
    uit, root = _export_indeling(tmp_path, begrippen)
    nieuw = ae.vast_id("groepering", "beleidsdomein", "Begraafplaatsen")
    assert _relaties_van(root, "archimate:AggregationRelationship", nieuw, ae.vast_id("element", "verzorgen-lijkbezorging"))
    assert "Verzorgen lijkbezorging" not in uit.zonder_plaats


def test_taakveld_wordt_op_nummer_gevonden():
    gemma_data = {"elementen": {"a": {"id": "a", "type": "grouping", "naam": "0 Bestuur, Politiek en Ondersteuning",
                                      "eigenschappen": {"GEMMA type": "Taakveld Iv3"}}}}
    assert ae._vind_taakveld(gemma_data, "0 Bestuur en Ondersteuning")["id"] == "a"
    assert ae._vind_taakveld(gemma_data, "7 Volksgezondheid en Milieu") is None
