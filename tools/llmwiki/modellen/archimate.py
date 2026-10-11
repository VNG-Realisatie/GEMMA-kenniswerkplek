"""ArchiMate-modellen als bron: het Archi-bronbestand (`.archimate`) en de ArchiMate Open Exchange-export (AMEFF, `.xml`).

Het formaat wordt herkend aan het root-element. Het resultaat is het JSON-formaat van `sources/modellen/` voor
ArchiMate-modellen (zie FORMAAT.md): `elementen`, `relaties`, `model` en, bij een Archi-bronbestand, `mappen` en
`profielen`.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

XSI_TYPE = "{http://www.w3.org/2001/XMLSchema-instance}type"


def archimate_type(xsi_type: str) -> str:
    """`archimate:BusinessObject` → `business-object`."""
    naam = xsi_type.split(":")[-1]
    return re.sub(r"(?<!^)(?=[A-Z])", "-", naam).lower()


AMEFF_NS = "http://www.opengroup.org/xsd/archimate/3.0/"


def parse(pad: Path) -> dict:
    """Herken het formaat aan het root-element: AMEFF (Open Group-namespace) of Archi (`archimate:model`)."""
    root_tag = next(ET.iterparse(pad, events=("start",)))[1].tag
    return parse_ameff(pad) if root_tag == f"{{{AMEFF_NS}}}model" else parse_archimate(pad)


def parse_ameff(pad: Path) -> dict:
    """ArchiMate Model Exchange File Format (Open Group). Mappen komen uit `organizations`."""
    ns = {"a": AMEFF_NS}
    root = ET.parse(pad).getroot()

    def tekst(el, tag) -> str:
        kind = el.find(f"a:{tag}", ns)
        return (kind.text or "").strip() if kind is not None else ""

    definities = {}
    sectie = root.find("a:propertyDefinitions", ns)
    for d in (list(sectie) if sectie is not None else []):
        definities[d.get("identifier")] = tekst(d, "name") or d.get("identifier")

    def eigenschappen(el) -> dict:
        result = {}
        for p in el.findall("a:properties/a:property", ns):
            waarde = p.find("a:value", ns)
            result[definities.get(p.get("propertyDefinitionRef"), p.get("propertyDefinitionRef"))] = (
                (waarde.text or "").strip() if waarde is not None else "")
        return result

    mappen: dict[str, str] = {}

    def loop(item, mappad: list[str]):
        for kind in item.findall("a:item", ns):
            if kind.get("identifierRef"):
                mappen[kind.get("identifierRef")] = " / ".join(mappad)
            label = kind.find("a:label", ns)
            loop(kind, mappad + [(label.text or "").strip()] if label is not None else mappad)

    organisaties = root.find("a:organizations", ns)
    if organisaties is not None:
        loop(organisaties, [])

    def obj(el, soort) -> dict:
        ident = el.get("identifier", "")
        return {"id": ident, "naam": tekst(el, "name"), "type": soort, "documentatie": tekst(el, "documentation"),
                "eigenschappen": eigenschappen(el), "map": mappen.get(ident, "")}

    elementen, relaties = {}, {}
    sectie = root.find("a:elements", ns)
    for el in (list(sectie) if sectie is not None else []):
        elementen[el.get("identifier")] = obj(el, archimate_type(el.get(XSI_TYPE, "")))
    sectie = root.find("a:relationships", ns)
    for el in (list(sectie) if sectie is not None else []):
        r = obj(el, archimate_type(el.get(XSI_TYPE, "")) + "-relationship")
        r.update(bron=el.get("source", ""), doel=el.get("target", ""))
        relaties[r["id"]] = r
    return {"elementen": elementen, "relaties": relaties,
            "model": {"naam": tekst(root, "name"), "eigenschappen": eigenschappen(root), "formaat": "ameff"}}


def _archi_eigenschappen(el) -> dict:
    return {p.get("key", ""): p.get("value", "") for p in el.findall("property") if p.get("key")}


def parse_archimate(pad: Path) -> dict:
    """Archi-bronbestand (ook het opslagformaat van coArchi 2). Levert naast elementen en relaties ook de mappen
    (met id) en de profielen (specialisaties), die de AMEFF mist; tools/archimate_export.py heeft ze nodig."""
    root = ET.parse(pad).getroot()
    elementen, relaties, mappen = {}, {}, {}

    def loop(folder, mappad: list[str], map_id: str):
        for kind in folder:
            tag = kind.tag.split("}")[-1]
            if tag == "folder":
                doc = kind.find("documentation")
                mappen[kind.get("id", "")] = {"id": kind.get("id", ""), "naam": kind.get("name", ""),
                                              "type": kind.get("type", ""), "ouder": map_id,
                                              "documentatie": (doc.text or "") if doc is not None else "",
                                              "eigenschappen": _archi_eigenschappen(kind)}
                loop(kind, mappad + [kind.get("name", "")], kind.get("id", ""))
            elif tag == "element":
                soort = archimate_type(kind.get(XSI_TYPE, ""))
                doc = kind.find("documentation")
                obj = {
                    "id": kind.get("id", ""),
                    "naam": kind.get("name", ""),
                    "type": soort,
                    "documentatie": (doc.text or "").strip() if doc is not None else "",
                    "eigenschappen": _archi_eigenschappen(kind),
                    "map": " / ".join(m for m in mappad if m),
                    "map_id": map_id,
                }
                if kind.get("profiles"):
                    obj["profiel"] = kind.get("profiles")
                if soort.endswith("-relationship"):
                    obj.update(bron=kind.get("source", ""), doel=kind.get("target", ""))
                    if soort == "access-relationship":
                        obj["toegang"] = int(kind.get("accessType", "0"))
                    if kind.get("directed") == "true":
                        obj["gericht"] = True
                    relaties[obj["id"]] = obj
                elif soort != "diagram-model" and not soort.endswith("-model"):
                    elementen[obj["id"]] = obj

    loop(root, [], "")
    profielen = {p.get("id", ""): {"id": p.get("id", ""), "naam": p.get("name", ""), "concept": p.get("conceptType", "")}
                 for p in root.findall("profile")}
    return {"elementen": elementen, "relaties": relaties, "mappen": mappen,
            "model": {"naam": root.get("name", ""), "id": root.get("id", ""), "eigenschappen": _archi_eigenschappen(root),
                      "profielen": profielen, "formaat": "archimate"}}
