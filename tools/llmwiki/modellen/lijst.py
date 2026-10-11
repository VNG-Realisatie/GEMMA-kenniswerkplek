"""Lijsten als bron: een Excel-werkmap (`.xlsx`) of een CSV-bestand (`.csv`), zoals de Uniforme Productnamenlijst (UPL).

De werkmap wordt zonder extra bibliotheek gelezen (een xlsx is een zip met XML). Het resultaat is het JSON-formaat van
`sources/modellen/` voor een lijst (zie FORMAAT.md): per werkblad de niet-lege rijen, met per rij de niet-lege cellen
onder hun kolomletter. De celinhoud staat letterlijk in het JSON (een getal als de tekst waarin Excel het bewaart).
Een CSV is één werkblad, met de naam van het bestand zonder extensie.
"""
from __future__ import annotations

import csv
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"


def _tekst(el: ET.Element | None) -> str:
    """De tekst van een `<si>` of `<is>`: alle `<t>` (ook in `<r>`-stukken), niet de fonetische `<rPh>`."""
    if el is None:
        return ""
    delen = []
    for kind in el:
        tag = kind.tag.split("}")[-1]
        if tag == "t":
            delen.append(kind.text or "")
        elif tag == "r":
            delen += [t.text or "" for t in kind.findall(f"{{{MAIN}}}t")]
    return "".join(delen)


def parse_xlsx(pad: Path) -> dict:
    with zipfile.ZipFile(pad) as z:
        gedeeld: list[str] = []
        if "xl/sharedStrings.xml" in z.namelist():
            gedeeld = [_tekst(si) for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall(f"{{{MAIN}}}si")]
        doelen = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels")).findall(f"{{{PKG_REL}}}Relationship")}
        werkbladen = []
        for blad in ET.fromstring(z.read("xl/workbook.xml")).find(f"{{{MAIN}}}sheets"):
            doel = doelen[blad.get(f"{{{REL}}}id")].lstrip("/")
            bestand = doel if doel.startswith("xl/") else f"xl/{doel}"
            rijen = []
            for rij in ET.fromstring(z.read(bestand)).iter(f"{{{MAIN}}}row"):
                cellen = {}
                for c in rij.findall(f"{{{MAIN}}}c"):
                    soort = c.get("t")
                    if soort == "inlineStr":
                        waarde = _tekst(c.find(f"{{{MAIN}}}is"))
                    else:
                        v = c.find(f"{{{MAIN}}}v")
                        waarde = (v.text or "") if v is not None else ""
                        if soort == "s" and waarde:
                            waarde = gedeeld[int(waarde)]
                    if waarde.strip():
                        cellen[re.match(r"[A-Z]+", c.get("r", "")).group(0)] = waarde
                if cellen:
                    rijen.append({"rij": int(rij.get("r", len(rijen) + 1)), "cellen": cellen})
            werkbladen.append({"naam": blad.get("name", ""), "rijen": rijen})
    return {"werkbladen": werkbladen}


def kolomletter(index: int) -> str:
    """De kolomletter zoals in Excel: 0 → A, 25 → Z, 26 → AA."""
    letters = ""
    index += 1
    while index:
        index, rest = divmod(index - 1, 26)
        letters = chr(ord("A") + rest) + letters
    return letters


def parse_csv(pad: Path) -> dict:
    """Een CSV (UTF-8, eventueel met BOM; scheidingsteken komma) als één werkblad. Het rijnummer is het nummer van het
    record, te beginnen bij 1 voor de kop; een cel met een regelovergang telt als één record."""
    rijen = []
    with Path(pad).open(encoding="utf-8-sig", newline="") as f:
        for nummer, record in enumerate(csv.reader(f), start=1):
            cellen = {kolomletter(i): waarde for i, waarde in enumerate(record) if waarde.strip()}
            if cellen:
                rijen.append({"rij": nummer, "cellen": cellen})
    return {"werkbladen": [{"naam": Path(pad).stem, "rijen": rijen}]}
