"""Modellen en lijsten als bron: sources/modellen/ met een omzetting naar JSON (llmwiki/modellen)."""
import subprocess
import zipfile

import pytest

from llmwiki import cli, lint, modellen, sources

AMEFF = """<?xml version="1.0" encoding="UTF-8"?>
<model xmlns="http://www.opengroup.org/xsd/archimate/3.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" identifier="id-model">
  <name xml:lang="nl">Testmodel</name>
  <elements>
    <element identifier="id-a" xsi:type="BusinessObject"><name xml:lang="nl">Beschikking</name></element>
  </elements>
</model>
"""

XMI_ZONDER_INHOUD = '<?xml version="1.0"?><xmi:XMI xmlns:xmi="http://schema.omg.org/spec/XMI/2.1" xmlns:uml="http://schema.omg.org/spec/UML/2.1"/>'


def _xlsx(pad):
    """Een minimale werkmap met één werkblad: een gedeelde tekst, een getal en een inline tekst."""
    with zipfile.ZipFile(pad, "w") as z:
        z.writestr("xl/workbook.xml", '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   '<sheets><sheet name="Producten" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/sharedStrings.xml", '<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                   '<si><t>UniformeProductnaam</t></si><si><r><t>aangifte </t></r><r><t>geboorte</t></r></si></sst>')
        z.writestr("xl/worksheets/sheet1.xml", '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>'
                   '<row r="1"><c r="B1" t="s"><v>0</v></c></row>'
                   '<row r="2"><c r="A2"><v>1</v></c><c r="B2" t="s"><v>1</v></c><c r="C2" t="inlineStr"><is><t>X</t></is></c><c r="D2"/></row>'
                   '<row r="3"/></sheetData></worksheet>')


def test_herken_de_vorm_van_een_bestand(tmp_path):
    ameff, xlsx, md = tmp_path / "a.xml", tmp_path / "b.xlsx", tmp_path / "c.md"
    ameff.write_text(AMEFF, encoding="utf-8")
    _xlsx(xlsx)
    md.write_text("# Tekst\n", encoding="utf-8")
    assert modellen.herken(ameff) == "archimate"
    assert modellen.herken(tmp_path / "x.archimate") == "archimate"
    assert modellen.herken(xlsx) == "lijst"
    assert modellen.herken(tmp_path / "f.csv") == "lijst"
    assert modellen.herken(md) is None
    xmi = tmp_path / "d.xml"
    xmi.write_text(XMI_ZONDER_INHOUD, encoding="utf-8")
    assert modellen.herken(xmi) == "xmi"
    (tmp_path / "e.xml").write_text("<ander/>", encoding="utf-8")
    assert modellen.herken(tmp_path / "e.xml") is None


def test_een_lijst_wordt_per_werkblad_met_niet_lege_cellen_omgezet(tmp_path):
    pad = tmp_path / "lijst.xlsx"
    _xlsx(pad)
    vorm, data = modellen.converteer(pad)
    assert vorm == "lijst"
    assert data == {"werkbladen": [{"naam": "Producten", "rijen": [
        {"rij": 1, "cellen": {"B": "UniformeProductnaam"}},
        {"rij": 2, "cellen": {"A": "1", "B": "aangifte geboorte", "C": "X"}}]}]}


def test_een_csv_wordt_een_werkblad_met_records_als_rijen(tmp_path):
    pad = tmp_path / "2026-test-upl.csv"
    pad.write_text('\ufeffUniformeProductnaam,URI,Gemeente\n'
                   'aangifte vertrek buitenland,http://x/AangifteVertrekBuitenland,X\n'
                   '"naam, met komma","regel\nover twee regels",\n'
                   ',,\n'
                   + ",".join(f"k{i}" for i in range(28)) + "\n", encoding="utf-8")
    vorm, data = modellen.converteer(pad)
    assert vorm == "lijst"
    blad = data["werkbladen"][0]
    assert blad["naam"] == "2026-test-upl"
    assert blad["rijen"][:3] == [
        {"rij": 1, "cellen": {"A": "UniformeProductnaam", "B": "URI", "C": "Gemeente"}},
        {"rij": 2, "cellen": {"A": "aangifte vertrek buitenland", "B": "http://x/AangifteVertrekBuitenland", "C": "X"}},
        {"rij": 3, "cellen": {"A": "naam, met komma", "B": "regel\nover twee regels"}}]
    assert blad["rijen"][3]["rij"] == 5 and blad["rijen"][3]["cellen"]["AB"] == "k27"


def test_json_omzetting_heeft_een_hash_die_wijziging_aanwijst(tmp_path):
    pad = tmp_path / "m.json"
    modellen.schrijf_json(pad, "lijst", {"werkbladen": []})
    assert modellen.lees_json(pad) == {"werkbladen": []}
    assert modellen.controleer_json(pad) is None
    pad.write_text(pad.read_text(encoding="utf-8").replace("[]", '[{"naam": "x"}]'), encoding="utf-8")
    assert "met de hand gewijzigd" in modellen.controleer_json(pad)


def test_een_model_gaat_naar_sources_modellen_met_json(tmp_path, repo):
    root, _ = repo
    ameff = tmp_path / "model.xml"
    ameff.write_text(AMEFF, encoding="utf-8")
    sources.add(root, "2026-test-model", ameff, titel="Testmodel", tags=["demo"], brontype="model")
    assert (root / "sources" / "modellen" / "2026-test-model.xml").exists()
    assert modellen.lees_json(root / "sources" / "modellen" / "2026-test-model.json")["elementen"]["id-a"]["naam"] == "Beschikking"
    assert not list((root / "sources" / "raw").glob("2026-test-model.*"))
    assert sources.read_index_entry(root, "2026-test-model")["pad"] == "sources/modellen/2026-test-model.xml"
    with pytest.raises(sources.SourceExistsError):
        sources.add(root, "2026-test-model", ameff, titel="Nog een keer", tags=[])


def test_de_vorm_bepaalt_de_map_niet_de_rol(tmp_path, repo):
    root, _ = repo
    ameff = tmp_path / "overig.xml"
    ameff.write_text(AMEFF, encoding="utf-8")
    sources.add(root, "2026-test-methode", ameff, titel="Methode", tags=[], brontype="overig")
    assert (root / "sources" / "modellen" / "2026-test-methode.json").exists()  # brontype overig, toch een model
    sources.add(root, "2026-test-document", ameff, titel="Als document", tags=[], brontype="overig", vorm="document",
                markdown_override=_md(tmp_path))
    assert (root / "sources" / "raw" / "2026-test-document.xml").exists()
    assert not (root / "sources" / "modellen" / "2026-test-document.json").exists()


def _md(tmp_path):
    pad = tmp_path / "tekst.md"
    pad.write_text("# Tekst\n", encoding="utf-8")
    return pad


def test_bronregel_noemt_de_tekst_het_origineel_en_de_omzetting(tmp_path, repo):
    root, _ = repo
    lijst = tmp_path / "lijst.xlsx"
    _xlsx(lijst)
    sources.add(root, "2026-test-lijst", lijst, titel="Lijst", tags=[], markdown_override=_md(tmp_path), brontype="informatiemodel")
    regel = sources.bronregel(root, "2026-test-lijst", root / "wikis" / "demo" / "bronduidingen" / "x.md")
    assert regel.startswith("Bron: [tekst](../../../sources/modellen/2026-test-lijst.md) · [origineel (xlsx)](")
    assert "[omzetting (json)](../../../sources/modellen/2026-test-lijst.json)" in regel
    assert "Tekst: `sources/modellen/2026-test-lijst.md`" in sources.inhoud_markdown(root, "2026-test-lijst")


def test_een_verplaatsing_uit_sources_raw_is_toegestaan_een_wijziging_niet(tmp_path):
    def git(*a):
        subprocess.run(["git", *a], cwd=tmp_path, check=True, capture_output=True)

    git("init", "-q")
    git("config", "user.email", "t@example.org")
    git("config", "user.name", "t")
    (tmp_path / "sources" / "raw").mkdir(parents=True)
    (tmp_path / "sources" / "modellen").mkdir()
    for naam in ("a.xml", "b.xml"):
        (tmp_path / "sources" / "raw" / naam).write_text(f"<{naam[0]}>" + "regel\n" * 20, encoding="utf-8")
    git("add", "-A")
    git("commit", "-qm", "begin")
    git("mv", "sources/raw/a.xml", "sources/modellen/a.xml")
    assert cli._git_changed_paths(tmp_path, "MDR") == []  # R100: geen wijziging
    git("mv", "sources/raw/b.xml", "sources/modellen/b.xml")
    (tmp_path / "sources" / "modellen" / "b.xml").write_text("<b>" + "regel\n" * 10 + "andere\n" * 10, encoding="utf-8")
    git("add", "-A")
    gewijzigd = cli._git_changed_paths(tmp_path, "MDR")
    assert gewijzigd == ["sources/raw/b.xml"]
    assert lint.check_sources_immutable(tmp_path, ["sources/modellen/c.json"])
