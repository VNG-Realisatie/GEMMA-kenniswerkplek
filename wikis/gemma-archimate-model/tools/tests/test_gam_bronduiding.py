"""tools/bronduiding.py: delen, citaat uit de vindplaats, schrijven en de controle op letterlijke citaten."""
import pytest

import bronduiding
import signalen
from llmwiki import sources

WET = "2026-rijk-voorbeeldwet-wettekst"
RAW = """wetten.nl - Voorbeeldwet

## Berichten over uw Buurt

# Voorbeeldwet

### Hoofdstuk 1. Algemeen

#### Artikel 1

- Toon relaties in LiDO

1 Onder bezwaar wordt verstaan: het indienen van een bezwaarschrift
bij het bestuursorgaan.

2 Het *bezwaar* wordt schriftelijk gedaan, met _opgave_ van redenen.

#### Artikel 1a

Een klacht gaat over een gedraging.
"""
BRONDUIDING = """---
id: 2026-rijk-voorbeeldwet-wettekst
type: bronduiding
onderwerp: demo
bronnen: [2026-rijk-voorbeeldwet-wettekst]
relevant: ja
---

# Voorbeeldwet

## Citaten

> Onder bezwaar wordt verstaan: het indienen van een bezwaarschrift bij het bestuursorgaan. (vindplaats: art. 1 lid 1)

> Het bezwaar wordt schriftelijk gedaan … van redenen. (art. 1 lid 2)

## Relevantie

Tekst.
"""


@pytest.fixture
def repo(archimate_repo, tmp_path):
    root, _ = archimate_repo
    pad = tmp_path / "wet.md"
    pad.write_text(RAW, encoding="utf-8")
    sources.add(root, WET, pad, titel="Voorbeeldwet", tags=["test"], brontype="rijksregelgeving", url="https://wetten.overheid.nl/BWBR1/")
    (root / "sources" / "raw" / f"{WET}.md").write_text(RAW, encoding="utf-8")
    return root


def test_delen_beginnen_bij_de_titel(repo):
    assert bronduiding.delen(repo, WET) == [(5, "# Voorbeeldwet"), (7, "### Hoofdstuk 1. Algemeen"), (9, "#### Artikel 1"),
                                            (18, "#### Artikel 1a")]


def test_citaat_van_een_lid_een_artikel_en_een_onbekend_artikel(repo):
    tekst, plaats = bronduiding.citaat(repo, WET, "art. 1 lid 1")
    assert plaats == "art. 1 lid 1"
    assert tekst == "Onder bezwaar wordt verstaan: het indienen van een bezwaarschrift bij het bestuursorgaan."
    assert bronduiding.citaat(repo, WET, "artikel 1")[0].startswith("1 Onder bezwaar") and bronduiding.citaat(repo, WET, "art. 1")[1] == "art. 1"
    assert bronduiding.citaat(repo, WET, "art. 1a") == ("Een klacht gaat over een gedraging.", "art. 1a")
    for fout in ("art. 9", "art. 1 lid 7", "art. 1 en art. 1a", "kop Algemeen"):
        with pytest.raises(bronduiding.Fout):
            bronduiding.citaat(repo, WET, fout)


def test_schrijf_zet_het_citaat_onder_de_sectie_zonder_dubbel(repo, tmp_path):
    pad = tmp_path / "bd.md"
    pad.write_text(BRONDUIDING, encoding="utf-8")
    regel = bronduiding.als_regel(*bronduiding.citaat(repo, WET, "art. 1a"))
    assert bronduiding.schrijf(pad, regel) and not bronduiding.schrijf(pad, regel)
    tekst = pad.read_text(encoding="utf-8")
    assert tekst.index(regel) < tekst.index("## Relevantie") and tekst.count(regel) == 1
    kaal = tmp_path / "kaal.md"
    kaal.write_text("# T\n", encoding="utf-8")
    bronduiding.schrijf(kaal, regel)
    assert kaal.read_text(encoding="utf-8").endswith(f"## Citaten\n\n{regel}\n")


def test_controle_op_letterlijke_citaten(repo):
    from llmwiki import frontmatter

    page = frontmatter.parse(BRONDUIDING)
    assert bronduiding.controleer(repo, [WET], page.body) == []  # leestekens, opmaak en weglating tellen niet
    fout = page.body.replace("## Relevantie", "> Het bezwaar wordt mondeling gedaan. (art. 1 lid 2)\n\n> Een klacht gaat over een gedraging.\n\n## Relevantie")
    meldingen = bronduiding.controleer(repo, [WET], fout)
    assert len(meldingen) == 2 and "mondeling" in meldingen[0] and "zonder vindplaats" in meldingen[1]
    assert bronduiding.controleer(repo, ["2026-onbekend"], fout) == []  # een modelbron heeft geen tekst in sources/raw/


def test_vindplaats_met_haakjes_in_de_kop(repo):
    body = "## Citaten\n\n> Een klacht gaat over een gedraging. (vindplaats: kop Klacht (BRP))\n"
    assert bronduiding.citaten(body) == [("Een klacht gaat over een gedraging.", "kop Klacht (BRP)")]


def test_signaal_voor_de_hele_wiki(repo, archimate_repo):
    _, wiki = archimate_repo
    map_ = wiki / "onderwerpen" / "demo" / "bronduidingen" / "rijksregelgeving"
    map_.mkdir(parents=True)
    (map_ / f"{WET}.md").write_text(BRONDUIDING.replace("## Relevantie", "> Verzonnen zin. (art. 1)\n\n## Relevantie"), encoding="utf-8")
    [melding] = signalen.citaten(wiki)
    assert melding.endswith("(regel Elke claim een bron)") and melding.startswith("onderwerpen/demo/bronduidingen/rijksregelgeving/") and "Verzonnen" in melding
