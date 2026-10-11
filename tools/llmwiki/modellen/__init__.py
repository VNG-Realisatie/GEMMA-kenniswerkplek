"""Modellen en lijsten als bron: de omzetting naar JSON (laag 1, `sources/modellen/`).

Een model (ArchiMate, XMI) of lijst (xlsx, csv) staat in `sources/modellen/` als origineel met een omzetting met dezelfde
naam: `<bron-id>.<ext>` en `<bron-id>.json`, zoals een pdf in `sources/raw/` een Markdown-omzetting heeft. De omzetting
is gereedschap van llmwiki; elke wiki leest de JSON en maakt een eigen bronduiding. Het formaat staat in FORMAAT.md.
"""
from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path

from . import archimate, lijst, xmi
from .. import hashing

TOOL = "llmwiki.modellen"
XMI_NS = "http://schema.omg.org/spec/XMI/2.1"


def herken(pad: Path) -> str | None:
    """De vorm van een modelbestand: `archimate`, `xmi` of `lijst`; None als het geen model of lijst is (dan is het een
    document voor `sources/raw/`)."""
    suffix = Path(pad).suffix.lower()
    if suffix == ".archimate":
        return "archimate"
    if suffix in (".xlsx", ".csv"):
        return "lijst"
    if suffix == ".xml":
        try:
            root_tag = next(ET.iterparse(pad, events=("start",)))[1].tag
        except (ET.ParseError, StopIteration):
            return None
        if root_tag == f"{{{archimate.AMEFF_NS}}}model":
            return "archimate"
        if root_tag == f"{{{XMI_NS}}}XMI":
            return "xmi"
    return None


def converteer(pad: Path, vorm: str | None = None) -> tuple[str, dict]:
    """(vorm, data) van een modelbestand."""
    vorm = vorm or herken(pad)
    if vorm == "archimate":
        return vorm, archimate.parse(pad)
    if vorm == "xmi":
        return vorm, xmi.parse_xmi(pad)
    if vorm == "lijst":
        return vorm, lijst.parse_csv(pad) if Path(pad).suffix.lower() == ".csv" else lijst.parse_xlsx(pad)
    raise ValueError(f"{pad}: geen herkend model of lijst (archimate, xmi, xlsx of csv)")


def _inhoud(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True)


def schrijf_json(pad: Path, vorm: str, data: dict) -> None:
    pad.parent.mkdir(parents=True, exist_ok=True)
    kop = {"tool": TOOL, "vorm": vorm, "hash": hashing.hash_text(_inhoud(data))}
    pad.write_text(json.dumps({"_gegenereerd": kop, "data": data}, ensure_ascii=False, indent=1, sort_keys=True),
                   encoding="utf-8", newline="\n")


def lees_json(pad: Path) -> dict:
    """De `data` van een omzetting."""
    return json.loads(Path(pad).read_text(encoding="utf-8"))["data"]


def controleer_json(pad: Path) -> str | None:
    """None als de omzetting ongewijzigd is sinds het omzetten, anders een melding."""
    geheel = json.loads(Path(pad).read_text(encoding="utf-8"))
    if hashing.hash_text(_inhoud(geheel.get("data"))) != (geheel.get("_gegenereerd") or {}).get("hash"):
        return f"{pad}: met de hand gewijzigd; zet het origineel opnieuw om"
    return None
