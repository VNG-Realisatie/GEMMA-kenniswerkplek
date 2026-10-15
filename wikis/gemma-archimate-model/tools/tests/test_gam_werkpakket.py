"""tools/werkpakket.py: begrippen, passages, UPL, relaties, cluster en het werkpakket als geheel."""
import json

import pytest
import yaml

import werkpakket
from gam_hulp import KENMERKEN_BO, VELDEN_BO
from llmwiki import beoordeling, sources

WET = "2026-rijk-voorbeeldwet-wettekst"
RAW = """# Voorbeeldwet

### Hoofdstuk 1

#### Artikel 1:1

- Toon relaties in LiDO

- Maak een permanente link

1 Onder bezwaar wordt verstaan: het indienen van een bezwaarschrift
bij het bestuursorgaan.

2 Het bezwaar wordt schriftelijk gedaan.

#### Artikel 1:2

Een klacht gaat over een gedraging.

### Hoofdstuk 2. Horen

Het bestuursorgaan hoort de indiener.
"""
BRONDUIDING = """# Voorbeeldwet

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| bezwaar | het indienen van een bezwaarschrift | bezwaarschrift | art. 1:1 lid 1 |
| klacht | klacht over een gedraging | — | art. 1:2 |
| horen | het horen van de indiener | — | kop Horen |
| besluit | een besluit | — | nergens |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| bezwaar | gaat over | besluit | art. 1:1 |
| klacht | gaat over | gedraging | art. 1:2 |
"""


def _kenmerken():
    return {s: {"waarde": w, "onderbouwing": "Niet van toepassing." if w == "nee" else "Ja, want x."}
            for s, w in KENMERKEN_BO.items()}


@pytest.fixture
def wiki(archimate_repo, tmp_path):
    root, wiki = archimate_repo
    origineel = tmp_path / "wet.md"
    origineel.write_text(RAW, encoding="utf-8")
    sources.add(root, WET, origineel, titel="Voorbeeldwet (BWBR0001234)", tags=["test"], brontype="rijksregelgeving",
                url="https://wetten.overheid.nl/BWBR0001234/")
    (root / "sources" / "raw" / f"{WET}.md").write_text(RAW, encoding="utf-8")
    index = root / "sources" / "index" / f"{WET}.md"
    index.write_text(index.read_text(encoding="utf-8") + "\n## Begrippen\n\n| Begrip | Regel | Soort |\n|---|---|---|\n"
                     "| Besluit | 22 | definitie |\n", encoding="utf-8")
    demo = wiki / "onderwerpen" / "demo"
    (demo / "bronduidingen" / "rijksregelgeving").mkdir(parents=True)
    (demo / "bronduidingen" / "rijksregelgeving" / f"{WET}.md").write_text(BRONDUIDING, encoding="utf-8")
    (demo / "beoordelingen").mkdir()
    (demo / "afbakening.yaml").write_text(yaml.safe_dump({
        "naam": "Demo", "niveau": "thematisch", "status": "in-behandeling",
        "omschrijving": ["Het bestuursrecht (art. 1:1). Tweede zin."], "bronnen": [WET],
        "besluiten": [{"datum": "2026-10-01", "begrip": "Klacht", "besluit": "Hoort elders.", "gevolg": "afwijzen"}]},
        allow_unicode=True), encoding="utf-8")
    for bid, naam, extra in [
        ("besluit", "Besluit", {"gemma": {"id": "id-besluit", "sterkte": "sterk", "onderbouwing": "x"}}),
        ("bezwaar", "Bezwaar", {"kernobject": "besluit", "bronnen": ["2025-vng-upl-producten-en-diensten-extern"],
                                "toelichting": "UPL nr. 64."}),
        ("behandelen-bezwaar", "Behandelen bezwaar", {"kernobject": "bezwaar"}),
    ]:
        data = {"begrip": naam, "onderwerpen": ["demo"], **VELDEN_BO, "kenmerken": _kenmerken(), "definitie": f"Definitie {naam}.",
                **extra, "beslist": {"uitkomst": {"soort": "element", "archimate_type": "business-object",
                                                  "paginatype": "bedrijfsobject"}}, "status": "review"}
        beoordeling.schrijf(demo / "beoordelingen" / f"{bid}.yaml", data)
    _upl(root, wiki)
    return wiki


def _upl(root, wiki):
    """Een VNG-lijst (JSON uit Excel) en de UPL van Logius (CSV), met hun bronduiding in modellen/upl/."""
    bd = wiki / "modellen" / "upl" / "bronduidingen" / "informatiemodel"
    bd.mkdir(parents=True)
    vng, logius = "2025-vng-upl-producten-en-diensten-extern", "2026-logius-upl-actueel"
    for b in (vng, logius):
        (bd / f"{b}.md").write_text(f"# {b}\n", encoding="utf-8")
    kop = {"B": "UniformeProductnaam ", "E": "Burger ", "F": "Bedrijf ", "I": "Grondslaglabel 1", "J": "Grondslaglink 1",
           "U": "Soort product", "V": "Specifiek/Generiek: x", "W": "GEMMA Domeinen"}
    rijen = [{"cellen": kop, "rij": 1},
             {"cellen": {"A": "64", "B": "bezwaar ", "E": "X ", "I": "Artikel 1:1 Voorbeeldwet",
                         "J": "https://wetten.overheid.nl/jci1.3:c:BWBR0001234&artikel=1:1", "U": "Primair", "V": "Generiek",
                         "W": "Bestuur"}, "rij": 2},
             {"cellen": {"A": "65", "B": "klachtenregeling ", "I": "Artikel 9 Andere wet", "W": "Bestuur"}, "rij": 3},
             {"cellen": {"A": "66", "B": "hondenbelasting ", "I": "Artikel 226 Gemeentewet", "W": "Belastingen"}, "rij": 4}]
    modellen = root / "sources" / "modellen"
    modellen.mkdir(parents=True, exist_ok=True)
    (modellen / f"{vng}.json").write_text(json.dumps({"data": {"werkbladen": [{"naam": "Producten en diensten", "rijen": rijen}]}}),
                                          encoding="utf-8")
    (modellen / f"{logius}.csv").write_text(
        "UniformeProductnaam,URI,Gemeente,Burger,Bedrijf,Autonomie,Medebewind,Aanvraag,Subsidie,Melding,Verplichting,Grondslag,Grondslaglabel,Grondslaglink\n"
        "bezwaar,u1,X,X,X,X,X,,,,,,Artikel 1:1 Voorbeeldwet,https://wetten.overheid.nl/jci1.3:c:BWBR0001234\n"
        "dwangsom bij niet tijdig beslissen,u2,X,X,,X,,X,,,,,Artikel 1:5 Voorbeeldwet,https://wetten.overheid.nl/jci1.3:c:BWBR0001234\n"
        "rijksproduct,u3,,X,,,,,,,,,Artikel 1 Voorbeeldwet,\n", encoding="utf-8")


def test_artikelen_uit_een_vindplaats():
    assert werkpakket._artikelen("art. 1:3 lid 3; art. 4:1") == ["1:3", "4:1"]
    assert werkpakket._artikelen("art. 4:7–4:9") == ["4:7", "4:9"]
    assert werkpakket._artikelen("art. 4:13, 4:14; opschorting art. 4:15") == ["4:13", "4:14", "4:15"]
    assert werkpakket._artikelen("kop Horen") == []


def test_passages_op_artikel_kop_regel_en_index(wiki):
    repo = wiki.parent.parent
    [p] = werkpakket.passages(repo, WET, "bezwaar", "art. 1:1 lid 1")
    assert p.waar == "art. 1:1" and p.tekst.startswith("1 Onder bezwaar wordt verstaan: het indienen van een bezwaarschrift bij")
    assert "Toon relaties" not in p.tekst and "Artikel" not in p.tekst and " / 2 Het bezwaar" in p.tekst
    assert werkpakket.passages(repo, WET, "horen", "kop Horen")[0].tekst == "Het bestuursorgaan hoort de indiener."
    assert werkpakket.passages(repo, WET, "klacht", "regel 18")[0].tekst.startswith("Een klacht")
    assert werkpakket.passages(repo, WET, "besluit", "nergens")[0].waar == "index, regel 22"
    assert werkpakket.passages(repo, WET, "onbekend", "nergens") == []
    assert len(werkpakket.passages(repo, WET, "bezwaar", "art. 1:1", max_woorden=3)[0].tekst.split()) == 4  # met …


def test_begrippen_uit_bronduiding_en_beoordelingen(wiki):
    alle = {b: d for b, (_, d) in beoordeling.alle(wiki, werkpakket.gam_gemeen.wiki_yaml(wiki)).items()}
    index = werkpakket.naamindex(alle)
    lijst = werkpakket.begrippen_van("demo", alle, werkpakket.bronbegrippen(wiki, "demo"), index)
    assert [(b.naam, b.bid) for b in lijst] == [("horen", None), ("klacht", None), ("Behandelen bezwaar", "behandelen-bezwaar"),
                                                ("besluit", "besluit"), ("bezwaar", "bezwaar")]
    assert lijst[4].bron.andere == ["bezwaarschrift"]
    cluster = werkpakket._cluster("bezwaar", alle, index)
    assert {b.bid for b in werkpakket.begrippen_van("demo", alle, werkpakket.bronbegrippen(wiki, "demo"), index, cluster)} \
        == {"bezwaar", "behandelen-bezwaar"}
    with pytest.raises(werkpakket.Fout):
        werkpakket._cluster("bestaatniet", alle, index)


def test_upl_op_grondslag_en_naam_met_dekking(wiki):
    repo = wiki.parent.parent
    producten = werkpakket.upl_producten(wiki, repo)
    assert [p.naam for p in producten] == ["bezwaar", "klachtenregeling", "hondenbelasting", "dwangsom bij niet tijdig beslissen"]
    assert producten[0].vlaggen == "autonomie, medebewind" and producten[0].doelgroep == "burger"
    selectie = werkpakket.upl_selectie(producten, werkpakket.wetten(repo, [WET]), ["klacht", "horen"])
    assert [(p.naam, r) for p, r in selectie] == [("bezwaar", "grondslag Voorbeeldwet"), ("klachtenregeling", "naam: klacht"),
                                                  ("dwangsom bij niet tijdig beslissen", "grondslag Voorbeeldwet")]
    alle = {b: d for b, (_, d) in beoordeling.alle(wiki, werkpakket.gam_gemeen.wiki_yaml(wiki)).items()}
    assert werkpakket.upl_dekking(alle) == {("2025-vng-upl-producten-en-diensten-extern", "64"): {"bezwaar"}}


def test_woorden_om_op_terug_te_vallen():
    assert werkpakket.woorden(["beslissing op bezwaar"]) == ["beslissing", "bezwaar"]
    assert werkpakket.woorden(["bezwaar"]) == []  # de hele naam is al gezocht
    assert werkpakket.woorden(["horen"]) == []


def test_werkpakket_als_geheel(wiki, capsys):
    assert werkpakket.main(["--wiki", str(wiki), "demo"]) == 0
    pad = wiki.parent.parent / ".work" / "werkpakket" / "demo.md"
    tekst = pad.read_text(encoding="utf-8")
    assert "demo.md:" in capsys.readouterr().out
    assert "- B1: 2026-rijk-voorbeeldwet-wettekst (rijksregelgeving)" in tekst
    assert "- demo (thematisch): Het bestuursrecht (art. 1:1)." in tekst
    assert "| klacht | klacht over een gedraging (B1) | art. 1:2 (B1) | nieuw; besluit onderwerp 2026-10-01 |" in tekst
    assert "bezwaar (bedrijfsobject, thuis demo, kernobject besluit)" in tekst
    assert "- **horen**" in tekst and "- **bezwaar**" not in tekst.split("## Passages")[1].split("## GGM")[0]  # alleen nieuw
    assert "Model niet gevonden" in tekst
    assert "naam: bezwaar | bezwaar |" in tekst and "| logius | - | dwangsom bij niet tijdig beslissen |" in tekst
    assert "- bezwaar → associatie (gericht) → besluit (gaat over) | art. 1:1 | B1" in tekst
    assert "- klacht — gaat over → gedraging" in tekst
    assert "- bedrijfsobject: kennismodel/bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md" in tekst
    assert werkpakket.main(["--wiki", str(wiki), "demo", "--alles"]) == 0
    assert "- **bezwaar**" in pad.read_text(encoding="utf-8")
    assert werkpakket.main(["--wiki", str(wiki), "bestaatniet"]) == 1
