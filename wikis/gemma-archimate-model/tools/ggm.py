"""Het GGM (Gemeentelijk Gegevensmodel) als bron: parsen, bevragen en `ggm_*`-velden leveren.

Het XMI is de bron van waarheid en wordt NOOIT direct gelezen door het model; alleen via deze tool.
De match kiest de AI (op betekenis); tools/beslissen.py haalt daarna bij elke run de letterlijke velden op met `velden`. Een nieuwe release is dus na `beslissen` vanzelf verwerkt.

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
from llmwiki import modellen  # noqa: E402
from llmwiki.modellen.xmi import parse_xmi, schoon_tekst  # noqa: E402,F401

WIKI_ROOT = gam_gemeen.WIKI_ROOT
TOOL = "tools/ggm.py"


# --- Laden en bevragen ---


def laad(pad: Path | None = None) -> dict:
    """Het GGM: de JSON-omzetting in `sources/modellen/` van de bron die `wiki.yaml` `ggm.bron` noemt."""
    pad = pad or gam_gemeen.model_json(WIKI_ROOT, "ggm")
    if not pad.exists():
        raise SystemExit(f"Geen GGM gevonden ({pad}). Draai eerst: uv run python {TOOL} release --id <bron-id>")
    return modellen.lees_json(pad)


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
    sources.add(repo_root, bron_id, xmi, titel=titel, tags=["ggm"], uitgever="VNG", brontype="model",
                markdown_override=overzicht, beschrijving="GGM-release (XMI 2.1)",
                url=url, url_pagina=weergave, opgehaald=date.today().isoformat() if url else "")
    _zet_modelbron(wiki_root, "ggm", bron_id)
    return {"entiteiten": len(data["entities"]), "relaties": len(data["relations"])}


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
