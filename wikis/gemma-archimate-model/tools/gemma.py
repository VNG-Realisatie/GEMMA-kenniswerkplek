"""Het GEMMA-model als bron: parsen, matchen en `gemma_*`-velden leveren.

Twee formaten, automatisch herkend: het Archi-bronbestand (`.archimate`, voorkeur: met map-id's en profielen, nodig
voor tools/archimate_export.py) en de ArchiMate Open Exchange-export (AMEFF, zonder map-id's). Zonder bestand haalt
`release` het bestand op van `wiki.yaml` `gemma.herkomst`. Het GEMMA-model is
een matchdoel (brontype `model`), geen bron voor begrippen. Het model leest het NOOIT direct; alleen via deze
tool. De match kiest de AI; tools/beslissen.py haalt daarna bij elke run de letterlijke velden op met `velden`.

Gebruik (vanuit de wikimap):
    uv run python tools/gemma.py release --id <bron-id> [--ref <branch|tag>]   # AMEFF ophalen van gemma.herkomst
    uv run python tools/gemma.py release <bestand.xml|.archimate> --id <bron-id>
    uv run python tools/gemma.py zoek <term>
    uv run python tools/gemma.py element <id|naam>
    uv run python tools/gemma.py koppel <ggm-guid>         # GEMMA-element met deze GGM-GUID als eigenschap
    uv run python tools/gemma.py velden <id>                # gemma_*-blok (YAML) voor een elementpagina
    uv run python tools/gemma.py groepering <id>            # groeperingen (beleidsdomein) die dit element aggregeren
    uv run python tools/gemma.py functie <id|naam>          # plek in de functiehiërarchie: ouders (tot het domein) en kinderen
    uv run python tools/gemma.py functies                   # de hele functiehiërarchie as-is
    uv run python tools/gemma.py relaties <id>
    uv run python tools/gemma.py kandidaten <naam> [--ggm-guid EAID_…] [--synoniemen a,b]
    uv run python tools/gemma.py kwaliteitsdoelen          # de kwaliteitsdoelen (id, naam, definitie) voor een beleidskader
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
from llmwiki import modellen  # noqa: E402
from llmwiki.modellen.archimate import AMEFF_NS, XSI_TYPE, archimate_type, parse, parse_ameff, parse_archimate  # noqa: E402,F401

WIKI_ROOT = gam_gemeen.WIKI_ROOT
TOOL = "tools/gemma.py"
GEMMA_VELDEN = ("gemma_id", "gemma_naam", "gemma_type", "gemma_definitie", "gemma_map", "gemma_eigenschappen")


# --- Laden en bevragen ---


def laad(pad: Path | None = None) -> dict:
    """Het GEMMA-model: de JSON-omzetting in `sources/modellen/` van de bron die `wiki.yaml` `gemma.bron` noemt."""
    pad = pad or gam_gemeen.model_json(WIKI_ROOT, "gemma")
    if not pad.exists():
        raise SystemExit(f"Geen GEMMA-model gevonden ({pad}). Draai eerst: uv run python {TOOL} release --id <bron-id>")
    return modellen.lees_json(pad)


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


def kwaliteitsdoelen(data: dict) -> list[dict]:
    """De kwaliteitsdoelen van GEMMA (Goal met GEMMA type Kwaliteitsdoel), op naam."""
    return [{"id": e["id"], "naam": e["naam"], "definitie": e["documentatie"]}
            for e in sorted(data["elementen"].values(), key=lambda x: x["naam"])
            if e["type"] == "goal" and e["eigenschappen"].get("GEMMA type") == "Kwaliteitsdoel"]


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


# --- De functiehiërarchie as-is ---

FUNCTIEKETEN = ("aggregation-relationship", "composition-relationship")
DOMEINEN_MAP = "Domeinen"  # de groeperingen onder `Domein en doelgroep`, de wortels van de functiehiërarchie


def functiehierarchie(data: dict) -> dict:
    """De functiehiërarchie van GEMMA letterlijk: de bedrijfsfuncties en de domeingroeperingen erboven, met de aggregaties
    ertussen. Een functie kan onder meer ouders hangen (een DAG). `onder` en `boven`: id → [(id, relatie-id)];
    `wortels`: de domeinen."""
    el = data["elementen"]
    knoop = lambda e: e["type"] == "business-function" or (e["type"] == "grouping" and e["map"].endswith(DOMEINEN_MAP))  # noqa: E731
    onder: dict[str, list[tuple[str, str]]] = {}
    boven: dict[str, list[tuple[str, str]]] = {}
    for r in data["relaties"].values():
        b, d = el.get(r["bron"]), el.get(r["doel"])
        if r["type"] in FUNCTIEKETEN and b and d and knoop(b) and d["type"] == "business-function":
            onder.setdefault(b["id"], []).append((d["id"], r["id"]))
            boven.setdefault(d["id"], []).append((b["id"], r["id"]))
    wortels = sorted((i for i, e in el.items() if e["type"] == "grouping" and e["map"].endswith(DOMEINEN_MAP) and i in onder),
                     key=lambda i: el[i]["naam"])
    return {"onder": onder, "boven": boven, "wortels": wortels}


def functie_tak(h: dict, functie_id: str) -> tuple[set[str], set[str]]:
    """De functie en alles erboven tot en met de domeinen: (knopen, relatie-id's), letterlijk."""
    knopen, relaties, nieuw = {functie_id}, set(), [functie_id]
    while nieuw:
        for ouder, rid in h["boven"].get(nieuw.pop(), []):
            relaties.add(rid)
            if ouder not in knopen:
                knopen.add(ouder)
                nieuw.append(ouder)
    return knopen, relaties


def functie_paden(data: dict, h: dict, functie_id: str) -> list[list[str]]:
    """Alle paden van een domein naar de functie, als lijsten van namen (domein eerst)."""
    el = data["elementen"]
    ouders = h["boven"].get(functie_id, [])
    if not ouders:
        return [[el[functie_id]["naam"]]]
    return sorted(pad + [el[functie_id]["naam"]] for o, _ in ouders for pad in functie_paden(data, h, o))


def functie_domeinen(h: dict, functie_id: str) -> set[str]:
    """De domeingroeperingen (id's) boven een functie."""
    return {i for i in functie_tak(h, functie_id)[0] if i in h["wortels"]}


def functie_domein_namen(data: dict, h: dict, functie_id: str) -> list[str]:
    return sorted(data["elementen"][i]["naam"] for i in functie_domeinen(h, functie_id))


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
    data = parse(bestand)  # alleen voor het overzicht en het resultaat; sources.add zet het model zelf om
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
        return any(re.search(rf"\b{re.escape(t)}", x, re.IGNORECASE) for x in [e["naam"], e["documentatie"]])

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
    for naam in ("zoek", "element", "koppel", "velden", "groepering", "relaties", "functie"):
        sub.add_parser(naam).add_argument("sleutel")
    sub.add_parser("functies")
    k = sub.add_parser("kandidaten")
    k.add_argument("naam")
    k.add_argument("--ggm-guid")
    k.add_argument("--synoniemen", default="", help="Komma-gescheiden andere namen")
    sub.add_parser("kwaliteitsdoelen")
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
    if a.cmd == "functie":
        gevonden = [e for e in zoek_element(data, a.sleutel) if e["type"] == "business-function"]
        if len(gevonden) != 1:
            print(f"FOUT: {len(gevonden)} bedrijfsfuncties gevonden voor '{a.sleutel}'; gebruik het id", file=sys.stderr)
            return 1
        h = functiehierarchie(data)
        el = data["elementen"]
        resultaat = {"id": gevonden[0]["id"], "naam": gevonden[0]["naam"],
                     "paden": [" › ".join(p) for p in functie_paden(data, h, gevonden[0]["id"])],
                     "ouders": [{"id": i, "naam": el[i]["naam"], "relatie": rid} for i, rid in h["boven"].get(gevonden[0]["id"], [])],
                     "kinderen": [{"id": i, "naam": el[i]["naam"], "relatie": rid} for i, rid in h["onder"].get(gevonden[0]["id"], [])]}
    elif a.cmd == "functies":
        h = functiehierarchie(data)
        el = data["elementen"]

        def boom(i: str, diepte: int) -> list[str]:
            regels = ["  " * diepte + f"{el[i]['naam']} ({i})"]
            for k, _ in sorted(h["onder"].get(i, []), key=lambda x: el[x[0]]["naam"]):
                regels += boom(k, diepte + 1)
            return regels
        print("\n".join(r for w in h["wortels"] for r in boom(w, 0)))
        return 0
    elif a.cmd == "kwaliteitsdoelen":
        resultaat = kwaliteitsdoelen(data)
    elif a.cmd == "kandidaten":
        resultaat = kandidaten(data, a.naam, a.ggm_guid, [s.strip() for s in a.synoniemen.split(",") if s.strip()])
    else:
        fn = {"zoek": zoek, "element": zoek_element, "koppel": koppel, "groepering": groepering, "relaties": relaties}[a.cmd]
        resultaat = fn(data, a.sleutel)
    print(json.dumps(resultaat, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
