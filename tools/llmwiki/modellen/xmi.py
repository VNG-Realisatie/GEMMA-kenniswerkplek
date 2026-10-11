"""Het GGM als bron: een XMI 2.1-export uit Enterprise Architect.

Het resultaat is het JSON-formaat van `sources/modellen/` voor een UML-gegevensmodel (zie FORMAAT.md): `entities`,
`relations`, `diagrams` en `packages`.
"""
from __future__ import annotations

import html
import re
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"xmi": "http://schema.omg.org/spec/XMI/2.1", "uml": "http://schema.omg.org/spec/UML/2.1"}
XMI_ID = f"{{{NS['xmi']}}}id"
XMI_TYPE = f"{{{NS['xmi']}}}type"
XMI_IDREF = f"{{{NS['xmi']}}}idref"
ENTITEIT_TAGS = ("Toelichting", "Synoniemen", "Herkomst", "Herkomst definitie", "Begrip", "Kwaliteit", "Populatie")


def _kinderen(ouder, tag: str) -> list:
    sectie = ouder.find(tag)
    return list(sectie) if sectie is not None else []


def _schoon_tag(waarde: str) -> str:
    if not waarde:
        return ""
    waarde = waarde.split("#NOTES#")[0]
    return waarde.replace("&#xA;", "\n").strip()


def schoon_tekst(tekst: str) -> str:
    """HTML-tags en -entiteiten weg, witruimte genormaliseerd; verder letterlijk."""
    if not tekst:
        return ""
    tekst = re.sub(r"<[^>]+>", " ", tekst)
    tekst = html.unescape(tekst)
    return re.sub(r"\s+", " ", tekst).strip()


def _multipliciteit(end) -> str:
    def waarde(tag):
        el = end.find(f"{{{NS['uml']}}}{tag}")
        if el is None:
            el = end.find(tag)
        return None if el is None else el.get("value", "")

    onder, boven = waarde("lowerValue"), waarde("upperValue")
    boven = "*" if boven == "-1" else boven
    return f"{onder}..{boven}" if onder and boven else ""


def parse_xmi(pad: Path) -> dict:
    root = ET.parse(pad).getroot()
    model = root.find("uml:Model", NS)
    extensie = root.find("xmi:Extension", NS)
    packages, entities, relations, generalisaties, diagrams = {}, {}, {}, {}, {}

    def loop(element, parent_id=None):
        for kind in element:
            if kind.tag.split("}")[-1] != "packagedElement":
                continue
            soort, xid, naam = kind.get(XMI_TYPE, ""), kind.get(XMI_ID, ""), kind.get("name", "").strip()
            if soort == "uml:Package":
                packages[xid] = {"id": xid, "name": naam, "parent_id": parent_id}
                loop(kind, xid)
            elif soort in ("uml:Class", "uml:Enumeration"):
                e = {"id": xid, "name": naam, "uml_type": soort.split(":")[1], "package_id": parent_id,
                     "attributes": [], "literals": [], "tags": {}}
                for attr in kind.findall("ownedAttribute"):
                    if not attr.get("association") and attr.get("name"):
                        # Bij een enumeratie exporteert EA de waarden als ownedAttribute.
                        e["literals" if soort == "uml:Enumeration" else "attributes"].append(attr.get("name"))
                for lit in kind.findall(f"{{{NS['uml']}}}ownedLiteral") + kind.findall("ownedLiteral"):
                    if lit.get("name"):
                        e["literals"].append(lit.get("name"))
                for gen in kind.findall(f"{{{NS['uml']}}}Generalization") + kind.findall("generalization"):
                    if gen.get(XMI_ID) and gen.get("general"):
                        generalisaties[gen.get(XMI_ID)] = {"general": gen.get("general"), "specific": xid}
                entities[xid] = e
            elif soort == "uml:Association":
                ends = []
                for end in kind.findall("ownedEnd"):
                    t = end.find("type")
                    ends.append({
                        "id": end.get(XMI_ID, ""),
                        "type_id": t.get(XMI_IDREF, "") if t is not None else end.get("type", ""),
                        "card": _multipliciteit(end),
                        "aggregation": end.get("aggregation", "none"),
                    })
                if len(ends) >= 2:
                    src = next((x for x in ends if "src" in x["id"].lower()), ends[0])
                    dst = next((x for x in ends if "dst" in x["id"].lower() and x is not src), ends[1] if ends[0] is src else ends[0])
                    relations[xid] = {"id": xid, "name": kind.get("name", ""), "uml_type": "Association",
                                      "source_id": src["type_id"], "target_id": dst["type_id"],
                                      "source_card": src["card"], "target_card": dst["card"],
                                      "documentation": "", "tags": {}}

    loop(model)

    if extensie is not None:
        for el in _kinderen(extensie, "elements"):
            idref, props, mdl, tags = el.get(XMI_IDREF, ""), el.find("properties"), el.find("model"), el.find("tags")
            if idref in packages:
                if props is not None:
                    packages[idref]["stereotype"] = props.get("stereotype", "")
                    packages[idref]["documentation"] = props.get("documentation", "")
                if mdl is not None and mdl.get("package") and not packages[idref].get("parent_id"):
                    packages[idref]["parent_id"] = mdl.get("package")
            elif idref in entities and el.get(XMI_TYPE) in ("uml:Class", "uml:Enumeration"):
                e = entities[idref]
                if props is not None:
                    e["documentation"] = props.get("documentation", "")
                    e["stereotype"] = props.get("stereotype", "")
                if mdl is not None and mdl.get("package"):
                    e["package_id"] = mdl.get("package")
                for tag in (tags if tags is not None else []):
                    if tag.get("name") in ENTITEIT_TAGS:
                        e["tags"][tag.get("name")] = _schoon_tag(tag.get("value", ""))

        for conn in _kinderen(extensie, "connectors"):
            idref = conn.get(XMI_IDREF, "")
            rel = relations.setdefault(idref, {"id": idref, "name": "", "uml_type": "", "source_id": "", "target_id": "",
                                               "source_card": "", "target_card": "", "documentation": "", "tags": {}})
            props = conn.find("properties")
            if props is not None:
                rel["uml_type"] = props.get("ea_type", "") or rel["uml_type"]
                if props.get("stereotype"):
                    rel["stereotype"] = props.get("stereotype")
                if props.get("ea_type") == "Aggregation":
                    rel["aggregatie"] = {"Strong": "composite", "Weak": "shared"}.get(props.get("subtype", ""), "shared")
            for kant in ("source", "target"):
                eind = conn.find(kant)
                if eind is None:
                    continue
                if eind.get(XMI_IDREF):
                    rel[f"{kant}_id"] = eind.get(XMI_IDREF)
                t = eind.find("type")
                if t is not None and t.get("aggregation", "none") != "none":
                    rel["aggregatie"] = t.get("aggregation")
                    rel["geheel"] = kant  # EA-conventie: het uiteinde met het ruitje is het geheel
            labels = conn.find("labels")
            if labels is not None:
                rel["name"] = labels.get("mt", "") or rel["name"]
                rel["source_card"] = rel["source_card"] or labels.get("lb", "")
                rel["target_card"] = rel["target_card"] or labels.get("rb", "")
            docs = conn.find("documentation")
            if docs is not None and docs.get("value"):
                rel["documentation"] = docs.get("value")

        for diag in _kinderen(extensie, "diagrams"):
            props, elems = diag.find("properties"), diag.find("elements")
            diagrams[diag.get(XMI_ID, "")] = {
                "id": diag.get(XMI_ID, ""),
                "name": props.get("name", "") if props is not None else "",
                "subjects": [e.get("subject") for e in (elems if elems is not None else []) if e.get("subject")],
            }

    # Pakkethiërarchie → taakveld/beleidsdomein (stereotype Domein/Basismodel, zoals in de oude parser)
    def pad_van(pid):
        pad, gezien = [], set()
        while pid and pid in packages and pid not in gezien:
            gezien.add(pid)
            pad.insert(0, packages[pid])
            pid = packages[pid].get("parent_id")
        return pad

    for e in entities.values():
        pad = pad_van(e.get("package_id"))
        for i, node in enumerate(pad):
            if node.get("stereotype") == "Domein" and i > 0:
                ouder = pad[i - 1]
                if ouder.get("stereotype") == "Domein":
                    e["taakveld"], e["beleidsdomein"] = ouder["name"], node["name"]
                elif ouder.get("stereotype") == "Basismodel":
                    e["taakveld"] = e["beleidsdomein"] = node["name"]

    for did, d in diagrams.items():
        for eid in d["subjects"]:
            if eid in entities:
                entities[eid].setdefault("diagram_ids", []).append(did)
                entities[eid].setdefault("diagram_names", []).append(d["name"])

    for gid, g in generalisaties.items():
        bestaand = relations.get(gid, {})  # naam/stereotype uit de EA-connector blijven behouden
        relations[gid] = {**bestaand, "id": gid, "name": bestaand.get("name", ""), "uml_type": "Generalization",
                          "source_id": g["specific"], "target_id": g["general"],
                          "source_card": "", "target_card": "", "documentation": bestaand.get("documentation", ""),
                          "tags": bestaand.get("tags", {})}

    relations = {rid: r for rid, r in relations.items() if r["source_id"] in entities and r["target_id"] in entities}
    for r in relations.values():
        r["source_name"] = entities[r["source_id"]]["name"]
        r["target_name"] = entities[r["target_id"]]["name"]

    return {"entities": entities, "relations": relations, "diagrams": diagrams,
            "packages": {pid: {k: v for k, v in p.items() if k != "documentation"} for pid, p in packages.items()}}
