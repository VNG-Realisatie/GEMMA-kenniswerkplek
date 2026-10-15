"""Hulp bij de bronduiding: de delen van een wet, een citaat uit de vindplaats en de controle dat citaten letterlijk zijn.

Een citaat in een bronduiding is letterlijke tekst uit `sources/raw/<bron-id>.md` (laag 1), met de vindplaats. Het script
haalt het citaat uit de bron, zodat het niet uit het geheugen komt; de controle (ook een harde controle in
`tools/beslissen.py`) meldt een citaat dat niet letterlijk in de bron staat. Alleen de woorden tellen (de bron breekt regels
af en gebruikt andere leestekens), en `…` of `[…]` in een citaat laat tekst weg.

Gebruik (vanuit de wikimap):
    uv run python tools/bronduiding.py delen <bron-id>
    uv run python tools/bronduiding.py citaat <bron-id> "art. 6 lid 2" [--schrijf <bronduiding.md>]
    uv run python tools/bronduiding.py controleer <bronduiding.md> …
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402
import werkpakket  # noqa: E402
from llmwiki import paths  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
VINDPLAATS = re.compile(r"\s*\((?:vindplaats:\s*)?(?P<plaats>(?:[^()]|\([^()]*\))*)\)\s*$")
WEGLATING = re.compile(r"\s*(?:\[…\]|…|\[\.\.\.\])\s*")
LID = re.compile(r"^(\d+[a-z]?)\s+\S")


class Fout(Exception):
    pass


def norm(tekst: str) -> str:
    """De woorden van de tekst, zonder leestekens, opmaak en opsommingstekens: de bron breekt regels af, zet `_nadruk_` en
    `- ` voor een lijstitem, en gebruikt andere aanhalingstekens dan een citaat."""
    return " ".join(re.findall(r"\w+", tekst.replace("_", " ")))


def raw_pad(repo: Path, bron_id: str) -> Path:
    pad = repo / "sources" / "raw" / f"{bron_id}.md"
    if not pad.exists():
        raise Fout(f"geen brontekst: {pad.relative_to(repo).as_posix()}")
    return pad


def delen(repo: Path, bron_id: str) -> list[tuple[int, str]]:
    """De koppen van de brontekst met regelnummer (1-based), vanaf de titel van de tekst zelf: de menu's van de site vóór
    de titel (`# ...`) vallen weg."""
    regels = werkpakket._regels(raw_pad(repo, bron_id))
    start = next((i for i, r in enumerate(regels) if re.match(r"^# \S", r)), 0)
    return [(i + 1, r) for i, r in enumerate(regels) if i >= start and re.match(r"^#{1,6} \S", r)]


def citaat(repo: Path, bron_id: str, vindplaats: str) -> tuple[str, str]:
    """(tekst, vindplaats) van `art. N [lid M]`. Zonder lid: alle leden van het artikel, na elkaar; met lid: alleen dat lid
    (zonder het lidnummer)."""
    regels = werkpakket._regels(raw_pad(repo, bron_id))
    artikel = werkpakket._artikelen(vindplaats)
    if len(artikel) != 1:
        raise Fout(f"noem één artikel, bijvoorbeeld 'art. 6 lid 2' (kreeg: {vindplaats!r})")
    nr = artikel[0]
    kop = re.compile(rf"^#+\s*Artikel\s+{re.escape(nr)}\s*$")
    i = next((i for i, r in enumerate(regels) if kop.match(r)), None)
    if i is None:
        raise Fout(f"artikel {nr} staat niet in {bron_id} (zie: bronduiding.py delen {bron_id})")
    eind = werkpakket._tot_volgende_kop(regels, i, len(regels))
    alineas: list[str] = []
    huidig: list[str] = []
    for r in regels[i + 1:eind]:
        r = r.strip()
        if not r or werkpakket.RUIS.match(r):
            if huidig:
                alineas.append(" ".join(huidig))
                huidig = []
            continue
        huidig.append(r)
    if huidig:
        alineas.append(" ".join(huidig))
    lid = re.search(r"\blid\s+(\d+[a-z]?)", vindplaats)
    if lid:
        tekst = next((a for a in alineas if (m := LID.match(a)) and m.group(1) == lid.group(1)), None)
        if tekst is None:
            raise Fout(f"artikel {nr} heeft geen lid {lid.group(1)}")
        tekst = re.sub(r"^\d+[a-z]?\s+", "", tekst)
        return tekst, f"art. {nr} lid {lid.group(1)}"
    if not alineas:
        raise Fout(f"artikel {nr} heeft geen tekst in {bron_id}")
    return " ".join(alineas), f"art. {nr}"


def als_regel(tekst: str, plaats: str) -> str:
    return f"> {' '.join(tekst.split())} (vindplaats: {plaats})"


def schrijf(pad: Path, regel: str) -> bool:
    """Zet `regel` onder `## Citaten`, achter de bestaande citaten; False als hij er al staat. De sectie wordt zo nodig gemaakt."""
    tekst = pad.read_text(encoding="utf-8")
    if regel in tekst:
        return False
    m = re.search(r"(?m)^## Citaten\s*$", tekst)
    if not m:
        pad.write_text(tekst.rstrip("\n") + f"\n\n## Citaten\n\n{regel}\n", encoding="utf-8", newline="\n")
        return True
    volgende = re.search(r"(?m)^## ", tekst[m.end():])
    eind = m.end() + volgende.start() if volgende else len(tekst)
    kop, rest = tekst[:eind].rstrip("\n"), tekst[eind:]
    pad.write_text(kop + "\n\n" + regel + "\n" + ("\n" + rest if rest else ""), encoding="utf-8", newline="\n")
    return True


def citaten(body: str) -> list[tuple[str, str]]:
    """(tekst, vindplaats) van elk citaat onder `## Citaten`; een citaat is een alinea met `>`."""
    sectie = gam_gemeen.sectie(body, "Citaten") or ""
    uit = []
    for alinea in re.split(r"\n\s*\n", sectie):
        regels = [r for r in alinea.strip().splitlines() if r.startswith(">")]
        if not regels:
            continue
        tekst = " ".join(r.lstrip("> ").strip() for r in regels)
        m = VINDPLAATS.search(tekst)
        uit.append((tekst[:m.start()] if m else tekst, m.group("plaats") if m else ""))
    return uit


def controleer(repo: Path, bron_ids: list[str], body: str) -> list[str]:
    """Meldingen over de citaten van een bronduiding: elk citaat staat letterlijk in de tekst van een van haar bronnen."""
    bronnen = {}
    for b in bron_ids:
        pad = repo / "sources" / "raw" / f"{b}.md"
        if pad.exists():
            bronnen[b] = f" {norm(pad.read_text(encoding='utf-8'))} "
    if not bronnen:
        return []  # een bron van een model heeft geen brontekst in sources/raw/
    meldingen = []
    for tekst, plaats in citaten(body):
        delen_ = [norm(d) for d in WEGLATING.split(tekst) if norm(d)]
        for bron in bronnen.values():
            positie, ok = 0, bool(delen_)
            for d in delen_:
                gevonden = bron.find(f" {d} ", positie)
                if gevonden < 0:
                    ok = False
                    break
                positie = gevonden + len(d) + 1
            if ok:
                break
        else:
            kort = " ".join(tekst.split())
            meldingen.append(f"citaat staat niet letterlijk in de bron ({plaats or 'zonder vindplaats'}): "
                             f"'{kort[:70]}{'…' if len(kort) > 70 else ''}' (bronduiding.py citaat <bron-id> \"<vindplaats>\")")
            continue
        if not plaats:
            meldingen.append(f"citaat zonder vindplaats: '{' '.join(tekst.split())[:70]}'")
    return meldingen


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--wiki", type=Path, default=WIKI_ROOT)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("delen", help="de koppen van een brontekst met regelnummer")
    p.add_argument("bron")
    p = sub.add_parser("citaat", help="het letterlijke citaat van een artikel of lid")
    p.add_argument("bron")
    p.add_argument("vindplaats")
    p.add_argument("--schrijf", type=Path, help="zet het citaat onder ## Citaten van deze bronduiding")
    p = sub.add_parser("controleer", help="staan de citaten letterlijk in de bron")
    p.add_argument("bronduiding", nargs="+", type=Path)
    a = ap.parse_args(argv)
    repo = paths.find_repo_root(a.wiki)
    try:
        if a.cmd == "delen":
            for nr, kop in delen(repo, a.bron):
                print(f"{nr}\t{kop}")
        elif a.cmd == "citaat":
            tekst, plaats = citaat(repo, a.bron, a.vindplaats)
            regel = als_regel(tekst, plaats)
            if a.schrijf:
                print(f"{a.schrijf}: citaat {plaats} toegevoegd" if schrijf(a.schrijf, regel) else f"{a.schrijf}: citaat {plaats} stond er al")
            else:
                print(regel)
        else:
            from llmwiki import frontmatter

            fouten = 0
            for pad in a.bronduiding:
                page = frontmatter.read(pad)
                for m in controleer(repo, page.meta.get("bronnen") or [], page.body):
                    print(f"{pad}: {m}")
                    fouten += 1
            return 1 if fouten else 0
    except Fout as e:
        print(f"fout: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
