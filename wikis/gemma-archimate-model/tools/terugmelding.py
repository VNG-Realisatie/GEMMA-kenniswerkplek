"""GGM-terugmeldingen: één doorlopende lijst (`analyses/ggm-terugmeldingen.md`), aangevuld ná het schrijven
van een element. Nooit een nieuw bestand, altijd een rij erbij; volgnummer en vaste waarden bewaakt deze tool.

De rij wordt gestaged in de run (changeset), net als de elementpagina's, en komt pas via promotie in de wiki.

Gebruik (vanuit de wikimap):
    uv run python tools/terugmelding.py add --run <run-id> --type <type> --domein <beleidsdomein>
        --entiteit <GGM-entiteit of -> --bevinding "<tekst>" [--element <element-id>]
    uv run python tools/terugmelding.py lijst
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402
from llmwiki import frontmatter, runs  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
PAD = Path("analyses") / "ggm-terugmeldingen.md"
TYPEN = {
    "hiaat": "Concept ontbreekt in het GGM",
    "definitie": "Entiteit bestaat, maar de definitie is onjuist, onvolledig of geen begripsdefinitie",
    "structuur": "Onhandige modellering (overerving, ontbrekende relatie, granulariteit)",
    "scope": "Entiteit hoort niet in dit beleidsdomein of ontbreekt in een ander",
    "duplicaat": "Zelfde concept met meerdere GUID's in verschillende beleidsdomeinen → samenvoegen",
    "homoniem": "Zelfde naam voor een ander concept in een ander beleidsdomein → hernoemen",
    "relatie": "Fout in een exact gematchte relatie (type, richting, kardinaliteit, naam, dubbel)",
}
STATUSSEN = ("open", "gemeld", "opgelost", "afgewezen")
KOLOMMEN = ["#", "Domein", "Entiteit", "Type", "Bevinding", "Element", "Status"]


def nieuwe_pagina() -> frontmatter.Page:
    typen = "\n".join(f"| {t} | {o} |" for t, o in TYPEN.items())
    body = (
        "# GGM-terugmeldingen\n\n"
        "Bevindingen uit de beoordeling van elementen die aan het GGM-beheer worden teruggekoppeld. "
        "Rijen worden alleen toegevoegd; de status wordt bijgewerkt.\n\n"
        "## Terugmeldingen\n\n| " + " | ".join(KOLOMMEN) + " |\n|" + "---|" * len(KOLOMMEN) + "\n\n"
        f"## Typen\n\n| Type | Betekenis |\n|---|---|\n{typen}\n\n"
        "## Status\n\nopen → gemeld → opgelost of afgewezen (met reden).\n"
    )
    return frontmatter.Page(meta={"id": "ggm-terugmeldingen", "type": "analyse", "titel": "GGM-terugmeldingen"}, body=body)


def _concept(wiki_root: Path, run_id: str) -> dict:
    pad = runs.run_dir(wiki_root, run_id) / "changeset-concept.json"
    return json.loads(pad.read_text(encoding="utf-8")) if pad.exists() else {"paginas": []}


def huidige_pagina(wiki_root: Path, run_id: str) -> frontmatter.Page:
    """De gestagede versie in deze run, anders die in de werkboom, anders een nieuwe."""
    for p in _concept(wiki_root, run_id)["paginas"]:
        if p["pad"] == PAD.as_posix():
            return frontmatter.read(runs.run_dir(wiki_root, run_id) / "changeset" / p["staged_bestand"])
    if (wiki_root / PAD).exists():
        return frontmatter.read(wiki_root / PAD)
    return nieuwe_pagina()


def element_pad(wiki_root: Path, run_id: str, element_id: str) -> Path | None:
    for el in gam_gemeen.elementen(wiki_root):
        if el.id == element_id:
            return el.pad
    for p in _concept(wiki_root, run_id)["paginas"]:
        staged = runs.run_dir(wiki_root, run_id) / "changeset" / p["staged_bestand"]
        if staged.exists() and frontmatter.read(staged).meta.get("id") == element_id:
            return wiki_root / p["pad"]
    return None


def rijen(page: frontmatter.Page) -> list[dict]:
    return gam_gemeen.tabel(gam_gemeen.sectie(page.body, "Terugmeldingen"))


def voeg_toe(wiki_root: Path, run_id: str, soort: str, domein: str, entiteit: str, bevinding: str,
             element_id: str | None = None) -> dict:
    if soort not in TYPEN:
        raise ValueError(f"Onbekend type '{soort}'; kies uit {', '.join(TYPEN)}")
    if not bevinding.strip():
        raise ValueError("Bevinding is leeg")
    page = huidige_pagina(wiki_root, run_id)
    nummers = [int(r["#"]) for r in rijen(page) if r.get("#", "").isdigit()]
    nummer = max(nummers, default=0) + 1

    element_cel = ""
    if element_id:
        pad = element_pad(wiki_root, run_id, element_id)
        if pad is None:
            raise ValueError(f"Element '{element_id}' niet gevonden (werkboom of changeset van deze run)")
        element_cel = f"[{element_id}]({gam_gemeen.relatief(wiki_root / PAD, pad)})"

    def cel(tekst: str) -> str:
        return tekst.replace("|", "\\|").replace("\n", " ").strip()

    rij = f"| {nummer} | {cel(domein)} | {cel(entiteit) or '—'} | {soort} | {cel(bevinding)} | {element_cel} | open |"
    sectie = gam_gemeen.sectie(page.body, "Terugmeldingen")
    tabelregels = [r for r in sectie.splitlines() if r.strip().startswith("|")]
    nieuwe_sectie = sectie.replace(tabelregels[-1], tabelregels[-1] + "\n" + rij, 1)
    page.body = page.body.replace(sectie, nieuwe_sectie, 1)
    gam_gemeen.stage(wiki_root, run_id, wiki_root / PAD, page, "analyse")
    return {"nummer": nummer, "rij": rij}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="GGM-terugmeldingen (zie docstring).")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("--run", required=True)
    a.add_argument("--type", required=True, choices=list(TYPEN))
    a.add_argument("--domein", required=True)
    a.add_argument("--entiteit", default="—")
    a.add_argument("--bevinding", required=True)
    a.add_argument("--element")
    sub.add_parser("lijst")
    args = p.parse_args(argv)
    if args.cmd == "lijst":
        pad = WIKI_ROOT / PAD
        print(json.dumps(rijen(frontmatter.read(pad)) if pad.exists() else [], indent=2, ensure_ascii=False))
        return 0
    try:
        print(json.dumps(voeg_toe(WIKI_ROOT, args.run, args.type, args.domein, args.entiteit, args.bevinding, args.element),
                         indent=2, ensure_ascii=False))
    except (ValueError, FileNotFoundError) as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
