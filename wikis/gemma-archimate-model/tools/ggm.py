"""Het GGM (Gemeentelijk Gegevensmodel) als bron: parsen, bevragen en `ggm_*`-velden leveren.

Het XMI is de bron van waarheid en wordt NOOIT direct gelezen door het model; alleen via deze tool.
De match kiest de AI (op betekenis); tools/afleiden.py haalt daarna bij elke run de letterlijke velden op met `velden`. Een nieuwe release is dus na `afleiden` vanzelf verwerkt.

Gebruik (vanuit de wikimap):
    uv run python tools/ggm.py release --id <bron-id> [--ref <branch|tag>]    # ophalen van ggm.herkomst (GitHub)
    uv run python tools/ggm.py release <xmi> --id <bron-id>                   # of een lokaal XMI-bestand
    uv run python tools/ggm.py zoek <term>
    uv run python tools/ggm.py entiteit <guid|naam>
    uv run python tools/ggm.py velden <guid>                 # ggm_*-blok (YAML) voor een elementpagina
    uv run python tools/ggm.py naamgenoten <naam>            # dezelfde naam in meerdere beleidsdomeinen
    uv run python tools/ggm.py generalisaties <guid>
    uv run python tools/ggm.py attribuut <term>              # komt de term voor als attribuut of waarde?
    uv run python tools/ggm.py relaties <guid>
    uv run python tools/ggm.py kandidaten <naam> [--synoniemen a,b]  # alles voor de match op betekenis, in één overzicht
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
GGM_DIR = WIKI_ROOT / "ggm"
PARSED = GGM_DIR / "ggm_parsed.json"
TOOL = "tools/ggm.py"

NS = {"xmi": "http://schema.omg.org/spec/XMI/2.1", "uml": "http://schema.omg.org/spec/UML/2.1"}
XMI_ID = f"{{{NS['xmi']}}}id"
XMI_TYPE = f"{{{NS['xmi']}}}type"
XMI_IDREF = f"{{{NS['xmi']}}}idref"
ENTITEIT_TAGS = ("Toelichting", "Synoniemen", "Herkomst", "Herkomst definitie", "Begrip", "Kwaliteit", "Populatie")


# --- Parser (overgezet uit de oude parse_ggm_xmi.py; houdt nu ook deel-geheel vast) ---


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


# --- Laden en bevragen ---


def laad(pad: Path = PARSED) -> dict:
    if not pad.exists():
        raise SystemExit(f"Geen geparsed GGM gevonden ({pad}). Draai eerst: uv run python {TOOL} release --id <bron-id>")
    return gam_gemeen.lees_json_gegenereerd(pad)


def zoek_entiteit(data: dict, sleutel: str) -> list[dict]:
    if sleutel in data["entities"]:
        return [data["entities"][sleutel]]
    return [e for e in data["entities"].values() if e["name"].lower() == sleutel.lower()]


def velden(entiteit: dict) -> dict:
    """Het `ggm_*`-blok voor een elementpagina. Lege velden worden weggelaten."""
    diagrammen = list(dict.fromkeys(entiteit.get("diagram_names", [])))
    kandidaten = {
        "ggm_entiteit": entiteit["name"],
        "ggm_guid": entiteit["id"],
        "ggm_uml_type": entiteit["uml_type"],
        "ggm_beleidsdomein": entiteit.get("beleidsdomein", ""),
        "ggm_taakveld": entiteit.get("taakveld", ""),
        "ggm_diagram": diagrammen,
        "ggm_diagram_ids": list(dict.fromkeys(entiteit.get("diagram_ids", []))),
        "ggm_definitie": schoon_tekst(entiteit.get("documentation", "")),
        "ggm_toelichting": schoon_tekst(entiteit.get("tags", {}).get("Toelichting", "")),
        "ggm_synoniemen": schoon_tekst(entiteit.get("tags", {}).get("Synoniemen", "")),
        "ggm_herkomst": schoon_tekst(entiteit.get("tags", {}).get("Herkomst", "")),
    }
    return {k: v for k, v in kandidaten.items() if v}


GGM_VELDEN = ("ggm_entiteit", "ggm_guid", "ggm_uml_type", "ggm_beleidsdomein", "ggm_taakveld", "ggm_diagram",
              "ggm_diagram_ids", "ggm_definitie", "ggm_toelichting", "ggm_synoniemen", "ggm_herkomst")


def naamgenoten(data: dict, naam: str) -> list[dict]:
    return [e for e in data["entities"].values() if e["name"].lower() == naam.lower()]


def zoek(data: dict, term: str) -> list[dict]:
    t = term.lower()
    return [e for e in data["entities"].values()
            if t in e["name"].lower() or t in e.get("tags", {}).get("Synoniemen", "").lower()
            or t in schoon_tekst(e.get("documentation", "")).lower()]


def generalisaties(data: dict, guid: str) -> dict:
    rels = [r for r in data["relations"].values() if r["uml_type"] == "Generalization"]
    return {"generalisaties": [r["target_id"] for r in rels if r["source_id"] == guid],
            "specialisaties": [r["source_id"] for r in rels if r["target_id"] == guid]}


def attribuut(data: dict, term: str) -> list[dict]:
    t = term.lower()
    return [{"entiteit": e["name"], "guid": e["id"], "beleidsdomein": e.get("beleidsdomein", ""),
             "als": "attribuut" if any(t == a.lower() for a in e["attributes"]) else "waarde"}
            for e in data["entities"].values()
            if any(t == a.lower() for a in e["attributes"]) or any(t == l.lower() for l in e["literals"])]


def relaties(data: dict, guid: str) -> list[dict]:
    return [r for r in data["relations"].values() if guid in (r["source_id"], r["target_id"])]


def geheel_en_deel(relatie: dict) -> tuple[str, str] | None:
    """(geheel-id, deel-id) van een aggregatie; None als het geen aggregatie is.

    EA-conventie: het uiteinde met aggregation≠none (het ruitje) is het geheel.
    """
    if not relatie.get("aggregatie") or not relatie.get("geheel"):
        return None
    if relatie["geheel"] == "source":
        return relatie["source_id"], relatie["target_id"]
    return relatie["target_id"], relatie["source_id"]


# --- Leesbare pagina's en release ---


def _slug(tekst: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", tekst.lower()).strip("-") or "overig"


def structuur_md(data: dict, bron_id: str) -> str:
    domeinen: dict[str, dict[str, int]] = {}
    for e in data["entities"].values():
        if e.get("stereotype") == "Objecttype":
            tv, bd = e.get("taakveld", "(geen taakveld)"), e.get("beleidsdomein", "(geen beleidsdomein)")
            domeinen.setdefault(tv, {}).setdefault(bd, 0)
            domeinen[tv][bd] += 1
    regels = [f"# GGM-structuur ({bron_id})", "",
              f"Objecttypen: {sum(sum(b.values()) for b in domeinen.values())}; relaties: {len(data['relations'])}.", ""]
    for tv in sorted(domeinen):
        regels.append(f"## {tv}")
        regels += [f"- {bd}: {n} objecttypen" for bd, n in sorted(domeinen[tv].items())]
        regels.append("")
    return "\n".join(regels)


def domein_pagina(data: dict, taakveld: str, beleidsdomein: str) -> str:
    ents = sorted((e for e in data["entities"].values()
                   if e.get("taakveld") == taakveld and e.get("beleidsdomein") == beleidsdomein
                   and e.get("stereotype") == "Objecttype"), key=lambda e: e["name"].lower())
    namen = {e["id"]: e["name"] for e in data["entities"].values()}
    regels = [f"# {beleidsdomein}", "", f"Taakveld: {taakveld}. Alleen objecttypen; letterlijke definities uit het GGM.", "",
              "| Objecttype | GUID | Definitie | Attributen |", "|---|---|---|---|"]
    for e in ents:
        definitie = schoon_tekst(e.get("documentation", "")).replace("|", "\\|")
        regels.append(f"| {e['name']} | `{e['id']}` | {definitie} | {', '.join(e['attributes'])} |")
    ids = {e["id"] for e in ents}
    rels = [r for r in data["relations"].values() if r["source_id"] in ids]
    if rels:
        regels += ["", "## Relaties", "", "| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |",
                   "|---|---|---|---|---|---|---|"]
        for r in sorted(rels, key=lambda r: (namen[r["source_id"]], r["uml_type"])):
            soort = r["uml_type"] + (f" ({r['aggregatie']})" if r.get("aggregatie") else "")
            definitie = schoon_tekst(r.get("documentation", "")).replace("|", "\\|")
            regels.append(f"| {r['source_name']} | {soort} | {r['name']} | {r['target_name']} | "
                          f"{r['source_card']} → {r['target_card']} | `{r['id']}` | {definitie} |")
    return "\n".join(regels) + "\n"


def genereer_paginas(data: dict, bron_id: str, ggm_dir: Path = GGM_DIR) -> int:
    for oud in ggm_dir.rglob("*.md"):
        oud.unlink()
    gam_gemeen.schrijf_gegenereerd(ggm_dir / "structuur.md", structuur_md(data, bron_id), TOOL)
    paren = {(e.get("taakveld"), e.get("beleidsdomein")) for e in data["entities"].values()
             if e.get("stereotype") == "Objecttype" and e.get("taakveld")}
    for tv, bd in paren:
        gam_gemeen.schrijf_gegenereerd(ggm_dir / _slug(tv) / f"{_slug(bd)}.md", domein_pagina(data, tv, bd), TOOL)
    return len(paren) + 1


def _zet_modelbron(wiki_root: Path, sleutel: str, bron_id: str) -> None:
    pad = wiki_root / "wiki.yaml"
    tekst = pad.read_text(encoding="utf-8")
    nieuw, n = re.subn(rf"(?m)^({sleutel}:\n  bron:).*$", rf"\1 {bron_id}", tekst)
    if n != 1:
        raise SystemExit(f"wiki.yaml: blok '{sleutel}:' met 'bron:' niet gevonden")
    pad.write_text(nieuw, encoding="utf-8")


def release(xmi: Path | None, bron_id: str, titel: str, wiki_root: Path = WIKI_ROOT,
            ref: str | None = None, pad: str | None = None) -> dict:
    """Neem een GGM-release op. Zonder `xmi` wordt het bestand opgehaald van `ggm.herkomst` in wiki.yaml."""
    from datetime import date

    from llmwiki import paths, sources

    url = weergave = ""
    if xmi is None:
        xmi, url, weergave = gam_gemeen.haal_op(wiki_root, "ggm", bron_id, ref, pad)
    data = parse_xmi(xmi)
    repo_root = paths.find_repo_root(wiki_root)
    werk = wiki_root / ".work" / "ggm-release"
    werk.mkdir(parents=True, exist_ok=True)
    overzicht = werk / f"{bron_id}.md"
    overzicht.write_text(structuur_md(data, bron_id), encoding="utf-8")
    sources.add(repo_root, bron_id, xmi, titel=titel, tags=["ggm"], uitgever="VNG", brontype="informatiemodel",
                markdown_override=overzicht, beschrijving="GGM-release (XMI 2.1)",
                url=url, url_pagina=weergave, opgehaald=date.today().isoformat() if url else "")
    ggm_dir = wiki_root / "ggm"
    gam_gemeen.schrijf_json_gegenereerd(ggm_dir / "ggm_parsed.json", data, TOOL)
    n = genereer_paginas(data, bron_id, ggm_dir)
    _zet_modelbron(wiki_root, "ggm", bron_id)
    return {"entiteiten": len(data["entities"]), "relaties": len(data["relations"]), "paginas": n}


def kandidaten(data: dict, naam: str, synoniemen: list[str] = ()) -> dict:
    """Alles wat de AI nodig heeft om op betekenis te matchen: entiteiten met dezelfde naam (mogelijke homoniemen),
    zoektreffers op naam, synoniem en definitie, en termen die als attribuut of waarde voorkomen. Per entiteit de
    definitie, het beleidsdomein en de generalisaties, zodat de keuze zonder losse vervolgvragen kan."""
    def kort(e: dict) -> dict:
        g = generalisaties(data, e["id"])
        return {"guid": e["id"], "entiteit": e["name"], "beleidsdomein": e.get("beleidsdomein", ""),
                "definitie": schoon_tekst(e.get("documentation", "")),
                "synoniemen": schoon_tekst(e.get("tags", {}).get("Synoniemen", "")),
                "generalisaties": [data["entities"][x]["name"] for x in g["generalisaties"] if x in data["entities"]],
                "specialisaties": [data["entities"][x]["name"] for x in g["specialisaties"] if x in data["entities"]]}

    termen = [naam, *synoniemen]
    def woordbegin(e: dict, t: str) -> bool:
        return any(re.search(rf"{re.escape(t)}", x, re.IGNORECASE) for x in [e["name"], e.get("tags", {}).get("Synoniemen", ""), schoon_tekst(e.get("documentation", ""))])

    treffers = {e["id"]: e for t in termen for e in zoek(data, t) if woordbegin(e, t)}
    return {"naamgenoten": [kort(e) for t in termen for e in naamgenoten(data, t)],
            "treffers": [kort(e) for e in treffers.values()][:25],
            "als_attribuut_of_waarde": [a for t in termen for a in attribuut(data, t)]}


# --- CLI ---


def _print(obj) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Het GGM als bron (zie docstring).")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("release")
    r.add_argument("xmi", nargs="?", help="Lokaal XMI-bestand; zonder dit wordt het opgehaald van ggm.herkomst in wiki.yaml")
    r.add_argument("--id", required=True, help="Bron-id, bijv. 2026-vng-ggm-2-5-1")
    r.add_argument("--titel", default="Gemeentelijk Gegevensmodel (XMI)")
    r.add_argument("--ref", help="Andere branch of tag dan ggm.herkomst.ref")
    r.add_argument("--pad", help="Ander pad in de repository dan ggm.herkomst.pad")
    for naam in ("zoek", "entiteit", "velden", "naamgenoten", "generalisaties", "attribuut", "relaties"):
        sub.add_parser(naam).add_argument("sleutel")
    k = sub.add_parser("kandidaten")
    k.add_argument("naam")
    k.add_argument("--synoniemen", default="", help="Komma-gescheiden andere namen")
    a = p.parse_args(argv)

    if a.cmd == "release":
        _print(release(Path(a.xmi) if a.xmi else None, a.id, a.titel, ref=a.ref, pad=a.pad))
        return 0
    data = laad()
    if a.cmd == "velden":
        gevonden = zoek_entiteit(data, a.sleutel)
        if len(gevonden) != 1:
            print(f"FOUT: {len(gevonden)} entiteiten gevonden voor '{a.sleutel}'; gebruik de GUID", file=sys.stderr)
            return 1
        sys.stdout.write(yaml.safe_dump(velden(gevonden[0]), sort_keys=False, allow_unicode=True))
        return 0
    if a.cmd == "kandidaten":
        _print(kandidaten(data, a.naam, [s.strip() for s in a.synoniemen.split(",") if s.strip()]))
        return 0
    fn = {"zoek": zoek, "entiteit": zoek_entiteit, "naamgenoten": naamgenoten, "generalisaties": generalisaties,
          "attribuut": attribuut, "relaties": relaties}[a.cmd]
    _print(fn(data, a.sleutel))
    return 0


if __name__ == "__main__":
    sys.exit(main())
