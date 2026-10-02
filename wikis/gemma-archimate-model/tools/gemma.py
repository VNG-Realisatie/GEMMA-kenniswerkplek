"""Het GEMMA-model als bron: parsen, matchen en `gemma_*`-velden leveren.

Twee formaten, automatisch herkend: het Archi-bronbestand (`.archimate`, voorkeur: met map-id's en profielen, nodig
voor tools/archimate_export.py) en de ArchiMate Open Exchange-export (AMEFF, zonder map-id's). Zonder bestand haalt
`release` het bestand op van `wiki.yaml` `gemma.herkomst`. Het GEMMA-model is
een matchdoel (brontype `model`), geen bron voor begrippen. Het model leest het NOOIT direct; alleen via deze
tool. De match kiest de AI; tools/afleiden.py haalt daarna bij elke run de letterlijke velden op met `velden`.

Gebruik (vanuit de wikimap):
    uv run python tools/gemma.py release --id <bron-id> [--ref <branch|tag>]   # AMEFF ophalen van gemma.herkomst
    uv run python tools/gemma.py release <bestand.xml|.archimate> --id <bron-id>
    uv run python tools/gemma.py zoek <term>
    uv run python tools/gemma.py element <id|naam>
    uv run python tools/gemma.py koppel <ggm-guid>         # GEMMA-element met deze GGM-GUID als eigenschap
    uv run python tools/gemma.py velden <id>                # gemma_*-blok (YAML) voor een elementpagina
    uv run python tools/gemma.py groepering <id>            # groeperingen (beleidsdomein) die dit element aggregeren
    uv run python tools/gemma.py relaties <id>
    uv run python tools/gemma.py kandidaten <naam> [--ggm-guid EAID_…] [--synoniemen a,b]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
PARSED = WIKI_ROOT / "gemma" / "gemma_parsed.json"
TOOL = "tools/gemma.py"
XSI_TYPE = "{http://www.w3.org/2001/XMLSchema-instance}type"
GEMMA_VELDEN = ("gemma_id", "gemma_naam", "gemma_type", "gemma_definitie", "gemma_map", "gemma_eigenschappen")


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


# --- Laden en bevragen ---


def laad(pad: Path = PARSED) -> dict:
    if not pad.exists():
        raise SystemExit(f"Geen geparsed GEMMA-model gevonden ({pad}). Draai eerst: uv run python {TOOL} release --id <bron-id>")
    return gam_gemeen.lees_json_gegenereerd(pad)


def normaliseer_guid(waarde: str) -> str:
    """EAID_0E19C86B_9088_41bd_9DD0_15094426570E en {0E19C86B-9088-41bd-9DD0-15094426570E} → 32 hex, kleine letters."""
    hexdeel = re.sub(r"[^0-9a-fA-F]", "", waarde.removeprefix("EAID_"))
    return hexdeel.lower() if len(hexdeel) == 32 else ""


def koppel(data: dict, ggm_guid: str) -> list[dict]:
    doel = normaliseer_guid(ggm_guid)
    if not doel:
        return []
    return [e for e in data["elementen"].values()
            if any(normaliseer_guid(w) == doel for w in e["eigenschappen"].values())]


def zoek_element(data: dict, sleutel: str) -> list[dict]:
    if sleutel in data["elementen"]:
        return [data["elementen"][sleutel]]
    return [e for e in data["elementen"].values() if e["naam"].lower() == sleutel.lower()]


def zoek(data: dict, term: str) -> list[dict]:
    t = term.lower()
    return [e for e in data["elementen"].values() if t in e["naam"].lower() or t in e["documentatie"].lower()]


def velden(element: dict) -> dict:
    kandidaten = {
        "gemma_id": element["id"],
        "gemma_naam": element["naam"],
        "gemma_type": element["type"],
        "gemma_definitie": element["documentatie"],
        "gemma_map": element["map"],
        "gemma_eigenschappen": dict(element["eigenschappen"]),
    }
    return {k: v for k, v in kandidaten.items() if v}


def relaties(data: dict, element_id: str) -> list[dict]:
    return [r for r in data["relaties"].values() if element_id in (r["bron"], r["doel"])]


def groepering(data: dict, element_id: str) -> list[str]:
    """Namen van Grouping-elementen die dit element aggregeren of bevatten (bijv. het beleidsdomein)."""
    namen = []
    for r in relaties(data, element_id):
        bron = data["elementen"].get(r["bron"])
        if r["doel"] == element_id and r["type"] in ("aggregation-relationship", "composition-relationship") \
                and bron is not None and bron["type"] == "grouping":
            namen.append(bron["naam"])
    return sorted(namen)


# --- Release en verrijken ---


def overzicht_md(data: dict, bron_id: str) -> str:
    per_type: dict[str, int] = {}
    for e in data["elementen"].values():
        per_type[e["type"]] = per_type.get(e["type"], 0) + 1
    release = data.get("model", {}).get("eigenschappen", {}).get("Release", "")
    regels = [f"# GEMMA-model ({bron_id})", "",
              f"Formaat: {data.get('model', {}).get('formaat', '?')}; release: {release or '?'}. "
              f"Elementen: {len(data['elementen'])}; relaties: {len(data['relaties'])}.", ""]
    regels += [f"- {t}: {n}" for t, n in sorted(per_type.items())]
    return "\n".join(regels) + "\n"


def release(bestand: Path | None, bron_id: str, titel: str, wiki_root: Path = WIKI_ROOT,
            ref: str | None = None, pad: str | None = None) -> dict:
    """Neem een versie van het GEMMA-model op. Zonder `bestand` wordt de AMEFF opgehaald van `gemma.herkomst`."""
    from datetime import date

    from llmwiki import paths, sources

    import ggm

    url = weergave = ""
    if bestand is None:
        bestand, url, weergave = gam_gemeen.haal_op(wiki_root, "gemma", bron_id, ref, pad)
    data = parse(bestand)
    repo_root = paths.find_repo_root(wiki_root)
    werk = wiki_root / ".work" / "gemma-release"
    werk.mkdir(parents=True, exist_ok=True)
    overzicht = werk / f"{bron_id}.md"
    overzicht.write_text(overzicht_md(data, bron_id), encoding="utf-8")
    formaat = {"ameff": "ArchiMate Open Exchange (AMEFF)", "archimate": "Archi-bronbestand"}[data["model"]["formaat"]]
    sources.add(repo_root, bron_id, bestand, titel=titel, tags=["gemma"], uitgever="VNG", brontype="model",
                markdown_override=overzicht, beschrijving=f"GEMMA-architectuurmodel ({formaat})",
                versie=data["model"]["eigenschappen"].get("Release", ""),
                url=url, url_pagina=weergave, opgehaald=date.today().isoformat() if url else "")
    gam_gemeen.schrijf_json_gegenereerd(wiki_root / "gemma" / "gemma_parsed.json", data, TOOL)
    gam_gemeen.schrijf_gegenereerd(wiki_root / "gemma" / "overzicht.md", overzicht_md(data, bron_id), TOOL)
    ggm._zet_modelbron(wiki_root, "gemma", bron_id)
    return {"formaat": data["model"]["formaat"], "release": data["model"]["eigenschappen"].get("Release", ""),
            "elementen": len(data["elementen"]), "relaties": len(data["relaties"])}


def kandidaten(data: dict, naam: str, ggm_guid: str | None = None, synoniemen: list[str] = ()) -> dict:
    """Alles voor de match op betekenis: de koppeling via de GGM-guid, elementen met dezelfde naam en zoektreffers,
    elk met type, definitie en groepering (beleidsdomein)."""
    def kort(e: dict) -> dict:
        return {"id": e["id"], "naam": e["naam"], "type": e["type"], "definitie": e["documentatie"],
                "groepering": groepering(data, e["id"])}

    termen = [naam, *synoniemen]
    def woordbegin(e: dict, t: str) -> bool:
        return any(re.search(rf"{re.escape(t)}", x, re.IGNORECASE) for x in [e["naam"], e["documentatie"]])

    treffers = {e["id"]: e for t in termen for e in zoek(data, t) if woordbegin(e, t)}
    return {"via_ggm_guid": [kort(e) for e in koppel(data, ggm_guid)] if ggm_guid else [],
            "naamgenoten": [kort(e) for t in termen for e in zoek_element(data, t)],
            "treffers": [kort(e) for e in treffers.values()][:25]}


# --- CLI ---


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Het GEMMA-model als bron (zie docstring).")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("release")
    r.add_argument("bestand", nargs="?", help="Lokale AMEFF (.xml) of .archimate; zonder dit wordt de AMEFF opgehaald van gemma.herkomst")
    r.add_argument("--id", required=True, help="Bron-id, bijv. 2026-vng-gemma-2026-07-01")
    r.add_argument("--titel", default="GEMMA-architectuurmodel")
    r.add_argument("--ref", help="Andere branch of tag dan gemma.herkomst.ref")
    r.add_argument("--pad", help="Ander pad in de repository dan gemma.herkomst.pad")
    for naam in ("zoek", "element", "koppel", "velden", "groepering", "relaties"):
        sub.add_parser(naam).add_argument("sleutel")
    k = sub.add_parser("kandidaten")
    k.add_argument("naam")
    k.add_argument("--ggm-guid")
    k.add_argument("--synoniemen", default="", help="Komma-gescheiden andere namen")
    a = p.parse_args(argv)

    if a.cmd == "release":
        print(json.dumps(release(Path(a.bestand) if a.bestand else None, a.id, a.titel, ref=a.ref, pad=a.pad),
                         indent=2, ensure_ascii=False))
        return 0
    data = laad()
    if a.cmd == "velden":
        gevonden = zoek_element(data, a.sleutel)
        if len(gevonden) != 1:
            print(f"FOUT: {len(gevonden)} elementen gevonden voor '{a.sleutel}'; gebruik het id", file=sys.stderr)
            return 1
        sys.stdout.write(yaml.safe_dump(velden(gevonden[0]), sort_keys=False, allow_unicode=True))
        return 0
    if a.cmd == "kandidaten":
        resultaat = kandidaten(data, a.naam, a.ggm_guid, [s.strip() for s in a.synoniemen.split(",") if s.strip()])
    else:
        fn = {"zoek": zoek, "element": zoek_element, "koppel": koppel, "groepering": groepering, "relaties": relaties}[a.cmd]
        resultaat = fn(data, a.sleutel)
    print(json.dumps(resultaat, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
