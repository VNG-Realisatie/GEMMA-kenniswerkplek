"""Werkpakket: alles wat het beoordelen van een onderwerp nodig heeft, in één bestand, in plaats van losse zoekopdrachten.

Het werkpakket (`.work/werkpakket/<onderwerp>[-<cluster>].md` in de root van de repository, gitignored) bevat:
- het onderwerp: bronnen met brontype, en de besluiten van het onderwerp en zijn beoordelingen;
- de onderwerpen: per onderwerp het niveau en de eerste zin van de omschrijving (regel Thuishoren);
- de begrippen uit de bronduidingen (`## Kernbegrippen`) en de beoordelingen van het onderwerp, met wat de catalogus kent:
  id, type, thuisonderwerp en de GGM- en GEMMA-match; een nieuw begrip met de beoordelingen die het noemen;
- de passages uit `sources/raw/`: het artikel uit de vindplaats, de regel of de kop, of de regel uit de technische index;
- de GGM- en GEMMA-kandidaten (`tools/ggm.py` en `tools/gemma.py kandidaten`), met de beoordeling die een kandidaat al gebruikt;
- de UPL-producten met een wet uit de bronnen als grondslag of een begrip in de naam, en welke beoordeling ze dekt;
- de relatievoorstellen uit de bronduidingen (`tools/relaties.py uit-bronnen`) en de relaties die vervallen;
- de modelleerafspraken voor de typen in het onderwerp, en de terugmeldingen over zijn elementen.

Passages en kandidaten staan er standaard alleen voor de nieuwe begrippen (zonder beoordeling); `--alles` geeft ze voor
alle begrippen. `--cluster <kernobject>` beperkt het werkpakket tot het kernobject, de beoordelingen met dat kernobject
en de begrippen met die naam erin. Het werkpakket is een hulpmiddel om te lezen: de herleidbaarheid loopt via de
bronduidingen, en de beoordeling blijft de plek van het oordeel.

Gebruik (vanuit de wikimap):
    uv run python tools/werkpakket.py <onderwerp> [--cluster <kernobject>] [--alles]
"""
from __future__ import annotations

import argparse
import csv
import functools
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import beoordeling as opzoeken  # noqa: E402
import gam_gemeen  # noqa: E402
import kennismodel  # noqa: E402
import relaties  # noqa: E402
from llmwiki import beoordeling, paths  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
MAX_WOORDEN = 150  # per passage
MAX_PASSAGES = 2  # per begrip
MAX_TREFFERS = 6  # per begrip en model, naast de naamgenoten
MAX_RELATIES = 8  # GEMMA-relaties per naamgenoot
UPL_BRON = re.compile(r"-(vng|logius)-upl-")
RUIS = re.compile(r"^(- (Toon|Maak|Druk|Sla|Vergelijk|Kopieer|Verfijn|\.\.\.)|\[(Wijziging|Vervallen))")
BWBR = re.compile(r"BWBR\d+")
ID_RE = re.compile(r"^(id-[0-9a-f-]{32,36}|EAID_[0-9A-Fa-f_]{36})$")
REGISTERS = {"GGM": gam_gemeen.GGM_TERUGMELDINGEN, "procesarchitectuur": gam_gemeen.PA_TERUGMELDINGEN,
             "GEMMA-team": gam_gemeen.GEMMA_TERUGMELDINGEN}


class Fout(Exception):
    pass


def norm(tekst: str) -> str:
    return " ".join(str(tekst).replace("*", "").lower().split())


def _cel(tekst) -> str:
    return " ".join(str(tekst or "").split()).replace("|", "\\|")


def _kort(tekst, n: int) -> str:
    t = " ".join(str(tekst or "").split())
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


# --- Begrippen: uit de bronduidingen en de beoordelingen ---


@dataclass
class Bronbegrip:
    naam: str
    andere: list[str] = field(default_factory=list)
    vermeldingen: list[tuple[str, str, str]] = field(default_factory=list)  # (bron-id, omschrijving, vindplaats)


def bronbegrippen(wiki: Path, onderwerp: str) -> dict[str, Bronbegrip]:
    """norm(naam) → begrip uit `## Kernbegrippen` van de bronduidingen van het onderwerp, samengevoegd per naam."""
    uit: dict[str, Bronbegrip] = {}
    for pad in gam_gemeen.bronduidingen(wiki, onderwerp):
        for rij in gam_gemeen.tabel(gam_gemeen.sectie(pad.read_text(encoding="utf-8"), "Kernbegrippen")):
            naam = rij.get("Begrip", "").replace("*", "").strip()
            if not naam:
                continue
            b = uit.setdefault(norm(naam), Bronbegrip(naam))
            andere = [a.strip() for a in re.split(r"[;,]", rij.get("Andere termen in deze bron", "")) if a.strip() not in ("", "—", "-")]
            b.andere += [a for a in andere if a not in b.andere]
            b.vermeldingen.append((pad.stem, rij.get("Omschrijving in de bron", ""), rij.get("Vindplaats", "")))
    return uit


def naamindex(alle: dict[str, dict]) -> dict[str, str]:
    """norm(naam, synoniem of id) → beoordeling-id."""
    index: dict[str, str] = {}
    for bid, d in alle.items():
        for naam in [d["begrip"], *(s["naam"] for s in d.get("synoniemen") or [])]:
            index.setdefault(norm(naam), bid)
        index.setdefault(bid, bid)
    return index


def gebruikte_ids(alle: dict[str, dict]) -> dict[str, set[str]]:
    """GEMMA-id of GGM-guid → de beoordelingen die het noemen (match, duplicaat, functie, relatie)."""
    uit: dict[str, set[str]] = {}

    def loop(bid: str, x) -> None:
        if isinstance(x, dict):
            for v in x.values():
                loop(bid, v)
        elif isinstance(x, list):
            for v in x:
                loop(bid, v)
        elif isinstance(x, str) and ID_RE.match(x):
            uit.setdefault(x, set()).add(bid)

    for bid, d in alle.items():
        loop(bid, {k: v for k, v in d.items() if k not in beoordeling.SCRIPTVELDEN})
    return uit


def genoemd_in(alle: dict[str, dict], naam: str, max_n: int = 5) -> list[str]:
    """De beoordelingen waarvan de tekst de naam noemt (als woord)."""
    patroon = re.compile(rf"\b{re.escape(naam)}\b", re.IGNORECASE)
    return [bid for bid, d in alle.items() if patroon.search(_tekst_van(bid, d))][:max_n]


_TEKSTEN: dict[str, str] = {}


def _tekst_van(bid: str, d: dict) -> str:
    if bid not in _TEKSTEN:
        _TEKSTEN[bid] = json.dumps({k: v for k, v in d.items() if k not in beoordeling.SCRIPTVELDEN}, ensure_ascii=False)
    return _TEKSTEN[bid]


def _uitkomst(d: dict) -> dict:
    return (d.get("beslist") or {}).get("uitkomst") or {}


def catalogus(bid: str, d: dict, ggm_data: dict | None, gemma_data: dict | None) -> str:
    """id, type, thuisonderwerp, kernobject en de GGM- en GEMMA-match van een beoordeling, op één regel."""
    u = _uitkomst(d)
    typ = u.get("paginatype") or u.get("archimate_type") or u.get("soort") or "?"
    delen = [f"{bid} ({typ}, thuis {d['onderwerpen'][0]}{', kernobject ' + d['kernobject'] if d.get('kernobject') else ''})"]
    g = d.get("ggm") or {}
    if g.get("guid"):
        naam = ((ggm_data or {}).get("entities", {}).get(g["guid"]) or {}).get("name", g["guid"])
        delen.append(f"GGM {naam} ({g.get('sterkte', '?')})")
    m = d.get("gemma") or {}
    if m.get("id"):
        naam = ((gemma_data or {}).get("elementen", {}).get(m["id"]) or {}).get("naam", m["id"])
        delen.append(f"GEMMA {naam} ({m.get('sterkte', '?')})")
    if d.get("status") == "afgewezen":
        delen.append("afgewezen")
    return "; ".join(delen)


# --- Passages uit sources/raw/ ---


@dataclass
class Passage:
    bron: str
    waar: str
    van: int
    tot: int
    tekst: str


@functools.cache
def _regels(pad: Path) -> tuple[str, ...]:
    return tuple(pad.read_text(encoding="utf-8").splitlines()) if pad.exists() else ()


def _artikelen(vindplaats: str) -> list[str]:
    """De artikelnummers in een vindplaats: 'art. 1:3 lid 3; art. 4:1' → ['1:3', '4:1']; 'art. 4:7–4:9' → ['4:7', '4:9']."""
    uit: list[str] = []
    for m in re.finditer(r"\bart(?:ikel|\.)\s*([^;]+)", vindplaats, re.IGNORECASE):
        deel = re.sub(r"\b(lid|onder|sub|regel)\s*\S+", "", m.group(1))
        uit += [n for n in re.findall(r"\b\d+(?::\d+)?[a-z]?\b", deel) if n not in uit]
    return uit


def _tot_volgende_kop(regels: tuple[str, ...], start: int, max_regels: int = 80) -> int:
    for i in range(start + 1, min(len(regels), start + max_regels)):
        if regels[i].startswith("#"):
            return i
    return min(len(regels), start + max_regels)


def _als_tekst(regels: tuple[str, ...], van: int, tot: int, max_woorden: int) -> str:
    """Regels [van, tot) als doorlopende tekst: alinea's met ' / ' ertussen, zonder de ruis van wetten.overheid.nl."""
    alineas, huidig = [], []
    for r in regels[van:tot]:
        r = r.strip()
        if not r or RUIS.match(r):
            if huidig:
                alineas.append(" ".join(huidig))
                huidig = []
            continue
        if not r.startswith("#"):
            huidig.append(r)
    if huidig:
        alineas.append(" ".join(huidig))
    woorden = " / ".join(alineas).split()
    return " ".join(woorden[:max_woorden]) + (" …" if len(woorden) > max_woorden else "")


def _index_regel(repo: Path, bron_id: str, naam: str) -> int | None:
    pad = repo / "sources" / "index" / f"{bron_id}.md"
    if not pad.exists():
        return None
    for rij in gam_gemeen.tabel(gam_gemeen.sectie(pad.read_text(encoding="utf-8"), "Begrippen")):
        if norm(rij.get("Begrip", "")) == norm(naam) and rij.get("Regel", "").isdigit():
            return int(rij["Regel"])
    return None


def passages(repo: Path, bron_id: str, naam: str, vindplaats: str, max_woorden: int = MAX_WOORDEN) -> list[Passage]:
    """De passages van een begrip in de tekst van een bron (`sources/raw/<bron-id>.md`): de regels die de vindplaats noemt,
    anders de artikelen of de kop uit de vindplaats, anders de regel uit de technische index (`sources/index/`)."""
    regels = _regels(repo / "sources" / "raw" / f"{bron_id}.md")
    if not regels:
        return []
    gevonden: list[tuple[str, int, int]] = []  # (waar, van, tot), 0-based, tot exclusief
    for m in re.finditer(r"regels? (\d+)(?:\s*[-–]\s*(\d+))?", vindplaats):
        a = int(m.group(1)) - 1
        gevonden.append((f"regel {m.group(0).split()[-1]}", a, int(m.group(2)) if m.group(2) else _tot_volgende_kop(regels, a, 15)))
    if not gevonden:
        for nr in _artikelen(vindplaats):
            kop = re.compile(rf"^#+\s*Artikel\s+{re.escape(nr)}\s*$")
            i = next((i for i, r in enumerate(regels) if kop.match(r)), None)
            if i is not None:
                gevonden.append((f"art. {nr}", i, _tot_volgende_kop(regels, i)))
    if not gevonden:
        for m in re.finditer(r"(?:\bkop|§)\s+([^,;]+)", vindplaats):
            t = m.group(1).strip().lower()
            i = next((i for i, r in enumerate(regels) if r.startswith("#") and t in r.lower()), None)
            if i is not None:
                gevonden.append((f"kop {m.group(1).strip()}", i, _tot_volgende_kop(regels, i)))
    if not gevonden:
        i = _index_regel(repo, bron_id, naam)
        if i is not None:
            a = i - 1
            gevonden.append((f"index, regel {i}", a, _tot_volgende_kop(regels, a, 25)))
    uit = []
    for waar, van, tot in gevonden[:MAX_PASSAGES]:
        tekst = _als_tekst(regels, van, tot, max_woorden)
        if tekst:
            uit.append(Passage(bron_id, waar, van + 1, tot, tekst))
    return uit


# --- Kandidaten in het GGM en het GEMMA-model ---


STOPWOORDEN = {"van", "het", "een", "voor", "door", "naar", "over", "tegen", "onder", "bij", "met", "tot", "aan", "uit"}
GEMMA_TYPEN = ("business-", "product", "contract", "representation", "driver")  # de bedrijfslaag en het beleidskader


def woorden(namen: list[str]) -> list[str]:
    """De woorden uit de namen om op terug te vallen als de hele naam niets vindt: vijf letters of meer, geen stopwoord."""
    uit: list[str] = []
    for n in namen:
        uit += [w for w in re.findall(r"[\w-]+", n.lower()) if len(w) >= 5 and w not in STOPWOORDEN and w not in uit]
    return uit if len(uit) > 1 or not namen or norm(namen[0]) not in uit else []


def _in_naam(naam: str, termen: list[str]) -> bool:
    return any(re.search(rf"\b{re.escape(t)}", naam, re.IGNORECASE) for t in termen)


def _treffers(alle_treffers: list[dict], sleutel: str, termen: list[str], uitsluiten: set[str], id_sleutel: str) -> list[dict]:
    """Treffers op naam vóór treffers in de definitie, zonder de naamgenoten."""
    lijst = list({e[id_sleutel]: e for e in alle_treffers if e[id_sleutel] not in uitsluiten}.values())
    return sorted(lijst, key=lambda e: not _in_naam(e[sleutel], termen))[:MAX_TREFFERS]


def ggm_kandidaten(data: dict, naam: str, synoniemen: list[str], gebruikt: dict[str, set[str]]) -> list[str]:
    """Naamgenoten (=) en treffers (~) in het GGM; zonder treffer op de hele naam de treffers op een woord uit de naam (≈)."""
    import ggm

    termen = [naam, *synoniemen]
    k = ggm.kandidaten(data, naam, synoniemen)

    def regel(teken: str, e: dict, n: int) -> str:
        door = sorted(gebruikt.get(e["guid"], ()))
        rel = "".join([f" ↑{', '.join(e['generalisaties'])}" if e["generalisaties"] else "",
                       f" ↓{', '.join(e['specialisaties'][:5])}" if e["specialisaties"] else ""])
        return (f"{teken} {e['entiteit']} [{e['beleidsdomein'] or '-'}] {e['guid']}: {_kort(e['definitie'], n)}{rel}"
                f"{' — gebruikt door ' + ', '.join(door) if door else ''}")

    namen = {e["guid"] for e in k["naamgenoten"]}
    uit = [regel("=", e, 160) for e in k["naamgenoten"]]
    uit += [regel("~", e, 90) for e in _treffers(k["treffers"], "entiteit", termen, namen, "guid")]
    if not uit and (ws := woorden(termen)):
        k2 = ggm.kandidaten(data, ws[0], ws[1:])
        uit += [regel("≈", e, 90) for e in _treffers(k2["naamgenoten"] + k2["treffers"], "entiteit", ws, set(), "guid")
                if _in_naam(e["entiteit"], ws)]
    uit += [f"attribuut: {a['entiteit']} ({a['als']}) [{a['beleidsdomein'] or '-'}] {a['guid']}"
            for a in k["als_attribuut_of_waarde"][:MAX_TREFFERS]]
    return uit


def gemma_kandidaten(data: dict, naam: str, synoniemen: list[str], gebruikt: dict[str, set[str]]) -> list[str]:
    """Naamgenoten (=, met hun relaties) en treffers (~) in het GEMMA-model, alleen de bedrijfslaag en het beleidskader;
    zonder treffer op de hele naam de treffers op een woord uit de naam (≈)."""
    import gemma

    termen = [naam, *synoniemen]
    k = gemma.kandidaten(data, naam, None, synoniemen)

    def regel(teken: str, e: dict, n: int) -> str:
        door = sorted(gebruikt.get(e["id"], ()))
        groep = f" [{', '.join(e['groepering'])}]" if e["groepering"] else ""
        return (f"{teken} {e['naam']} ({e['type']}){groep} {e['id']}: {_kort(e['definitie'], n)}"
                f"{' — gebruikt door ' + ', '.join(door) if door else ''}")

    def bedrijf(lijst: list[dict]) -> list[dict]:
        return [e for e in lijst if e["type"].startswith(GEMMA_TYPEN)]

    uit: list[str] = []
    namen = set()
    for e in k["naamgenoten"]:
        namen.add(e["id"])
        uit.append(regel("=", e, 160))
        rels = [r for r in gemma.relaties(data, e["id"]) if data["elementen"].get(r["bron"], {}).get("type") != "grouping"]
        for r in rels[:MAX_RELATIES]:
            ander = data["elementen"].get(r["doel"] if r["bron"] == e["id"] else r["bron"], {})
            pijl = "→" if r["bron"] == e["id"] else "←"
            uit.append(f"    {pijl} {r['type'].removesuffix('-relationship')} {ander.get('naam', '?')} ({ander.get('type', '?')})")
    uit += [regel("~", e, 90) for e in _treffers(bedrijf(k["treffers"]), "naam", termen, namen, "id")]
    if not uit and (ws := woorden(termen)):
        k2 = gemma.kandidaten(data, ws[0], None, ws[1:])
        uit += [regel("≈", e, 90) for e in _treffers(bedrijf(k2["naamgenoten"] + k2["treffers"]), "naam", ws, set(), "id")
                if _in_naam(e["naam"], ws)]
    return uit


# --- De UPL ---


@dataclass
class UplProduct:
    lijst: str
    nr: str
    naam: str
    grondslag: list[str]
    links: list[str]
    domein: str = ""
    doelgroep: str = ""
    soort: str = ""
    niveau: str = ""
    vlaggen: str = ""


def _vng_lijst(bron_id: str, data: dict) -> list[UplProduct]:
    blad = next((w for w in data["data"]["werkbladen"] if w["naam"].strip() == "Producten en diensten"), None)
    if not blad or not blad["rijen"]:
        return []
    kop = {k: norm(v) for k, v in blad["rijen"][0]["cellen"].items()}

    def kolommen(*voorwaarden) -> list[str]:
        return [k for k, v in kop.items() if any(f(v) for f in voorwaarden)]

    naam = kolommen(lambda v: v.startswith("uniformeproduct"))
    labels = kolommen(lambda v: "grond" in v and "label" in v)
    links = kolommen(lambda v: v.startswith("grondslaglink"))
    domein = kolommen(lambda v: v.startswith("gemma domein"))
    soort = kolommen(lambda v: v in ("soort product", "type"))
    niveau = kolommen(lambda v: v.startswith(("specifiek/generiek", "generiek/specif")))
    uit = []
    for rij in blad["rijen"][1:]:
        c = {k: " ".join(str(v).split()) for k, v in rij["cellen"].items()}
        if not naam or not c.get(naam[0]):
            continue
        doelgroep = "/".join(x for x, k in (("burger", "E"), ("bedrijf", "F")) if kop.get(k, "").startswith(x) and c.get(k))
        uit.append(UplProduct(bron_id, c.get("A", ""), c[naam[0]], [c[k] for k in labels if c.get(k)],
                              [c[k] for k in links if c.get(k)], c.get(domein[0], "") if domein else "", doelgroep,
                              c.get(soort[0], "") if soort else "", c.get(niveau[0], "") if niveau else ""))
    return uit


def _logius_lijst(bron_id: str, pad: Path) -> list[UplProduct]:
    """De gemeentelijke producten uit de UPL van Logius (een rij per grondslag), met de vlaggen aanvraag, subsidie,
    melding, verplichting, autonomie en medebewind."""
    uit: dict[str, UplProduct] = {}
    with pad.open(encoding="utf-8") as f:
        for rij in csv.DictReader(f):
            if rij.get("Gemeente") != "X":
                continue
            naam = rij["UniformeProductnaam"].strip()
            p = uit.setdefault(norm(naam), UplProduct(bron_id, "", naam, [], []))
            p.doelgroep = "/".join(x for x in ("burger", "bedrijf") if rij.get(x.capitalize()))
            p.vlaggen = ", ".join(k.lower() for k in ("Aanvraag", "Subsidie", "Melding", "Verplichting", "Autonomie", "Medebewind")
                                  if rij.get(k))
            if rij.get("Grondslaglabel") and rij["Grondslaglabel"] not in p.grondslag:
                p.grondslag.append(rij["Grondslaglabel"])
            p.links += [x for x in (rij.get("Grondslag"), rij.get("Grondslaglink")) if x]
    return list(uit.values())


def upl_producten(wiki: Path, repo: Path) -> list[UplProduct]:
    """De producten uit de UPL-lijsten met een bronduiding in `modellen/upl/`: de lijsten van de VNG met nummer, domein en
    soort, aangevuld met de vlaggen uit de UPL van Logius, en de gemeentelijke producten die alleen Logius kent."""
    producten: list[UplProduct] = []
    logius: list[UplProduct] = []
    for pad in sorted(wiki.glob("modellen/upl/bronduidingen/*/*.md")):
        bron = repo / "sources" / "modellen" / pad.stem
        if bron.with_suffix(".csv").exists() and "logius-upl-actueel" in pad.stem:
            logius += _logius_lijst(pad.stem, bron.with_suffix(".csv"))
        elif bron.with_suffix(".json").exists() and "vng-upl" in pad.stem:
            producten += _vng_lijst(pad.stem, json.loads(bron.with_suffix(".json").read_text(encoding="utf-8")))
    vng = {norm(p.naam): p for p in producten}
    for lp in logius:
        if norm(lp.naam) in vng:
            vng[norm(lp.naam)].vlaggen = lp.vlaggen
        else:
            producten.append(lp)
    return producten


def wetten(repo: Path, bronnen: list[str]) -> list[tuple[str, set[str]]]:
    """(titel, BWBR-nummers) van de bronnen die regelgeving zijn, uit de technische index."""
    from llmwiki import sources

    uit = []
    for b in bronnen:
        try:
            meta = sources.read_index_entry(repo, b)
        except FileNotFoundError:
            continue
        if not str(meta.get("brontype", "")).endswith("regelgeving"):
            continue
        titel = re.sub(r"\s*\(.*?\)\s*$", "", str(meta.get("titel", ""))).strip()
        uit.append((titel, set(BWBR.findall(str(meta.get("url", ""))))))
    return uit


def upl_dekking(alle: dict[str, dict]) -> dict[tuple[str, str], set[str]]:
    """(lijst, nummer) → de beoordelingen die die UPL-lijst als bron noemen met 'nr. <nummer>'."""
    uit: dict[tuple[str, str], set[str]] = {}
    for bid, d in alle.items():
        tekst = _tekst_van(bid, d)
        for lijst in set(re.findall(r"\b\d{4}-vng-upl-[a-z-]+", tekst)):
            for nr in re.findall(r"\bnr\.\s*(\d+)", tekst):
                uit.setdefault((lijst, nr), set()).add(bid)
    return uit


def upl_selectie(producten: list[UplProduct], wetten_: list[tuple[str, set[str]]], begripnamen: list[str]) -> list[tuple[UplProduct, str]]:
    """(product, reden): de producten met een wet uit de bronnen als grondslag, of met een begrip in de naam."""
    uit = []
    for p in producten:
        reden = []
        for titel, bwbr in wetten_:
            if any(b in link for b in bwbr for link in p.links) or (titel and any(titel.lower() in g.lower() for g in p.grondslag)):
                reden.append(f"grondslag {titel}")
        namen = [n for n in begripnamen if len(n) >= 4 and re.search(rf"\b{re.escape(n)}", p.naam, re.IGNORECASE)]
        if namen:
            reden.append(f"naam: {', '.join(namen[:3])}")
        if reden:
            uit.append((p, "; ".join(reden)))
    return uit


# --- Het werkpakket ---


@dataclass
class Begrip:
    naam: str
    bid: str | None
    bron: Bronbegrip | None


def _cluster(kern: str, alle: dict[str, dict], index: dict[str, str]) -> tuple[set[str], list[str]]:
    """(beoordelingen, namen) van een cluster: het kernobject, de beoordelingen met dat kernobject, en de namen van het
    kernobject om bronbegrippen op te vangen."""
    bid = index.get(norm(kern)) or index.get(kern)
    if bid is None:
        raise Fout(f"kernobject '{kern}' is geen beoordeling; zoek met tools/beoordeling.py zoek")
    d = alle[bid]
    leden = {bid} | {b for b, x in alle.items() if x.get("kernobject") == bid}
    return leden, [norm(d["begrip"]), *(norm(s["naam"]) for s in d.get("synoniemen") or [])]


def begrippen_van(onderwerp: str, alle: dict[str, dict], bron: dict[str, Bronbegrip], index: dict[str, str],
                  cluster: tuple[set[str], list[str]] | None = None) -> list[Begrip]:
    uit: list[Begrip] = []
    gezien: set[str] = set()
    for n, b in bron.items():
        bid = index.get(n) or next((index[norm(a)] for a in b.andere if norm(a) in index), None)
        uit.append(Begrip(b.naam, bid, b))
        if bid:
            gezien.add(bid)
    for bid, d in alle.items():
        if onderwerp in d["onderwerpen"] and bid not in gezien:
            uit.append(Begrip(d["begrip"], bid, None))
    if cluster:
        leden, namen = cluster
        uit = [b for b in uit if b.bid in leden or any(n in norm(b.naam) for n in namen)]
    return sorted(uit, key=lambda b: (b.bid is not None, norm(b.naam)))


def maak(wiki: Path, onderwerp: str, cluster: str | None = None, alles: bool = False) -> tuple[str, dict[str, int]]:
    """Het werkpakket als Markdown, met het aantal regels per sectie."""
    import gemma
    import ggm

    afb = gam_gemeen.afbakeningen(wiki)
    if onderwerp not in afb:
        raise Fout(f"onderwerp '{onderwerp}' bestaat niet: {', '.join(afb)}")
    repo = paths.find_repo_root(wiki)
    alle = {bid: d for bid, (_, d) in beoordeling.alle(wiki, gam_gemeen.wiki_yaml(wiki)).items()}
    _TEKSTEN.clear()
    index = naamindex(alle)
    ggm_pad, gemma_pad = gam_gemeen.model_json(wiki, "ggm"), gam_gemeen.model_json(wiki, "gemma")
    ggm_data = ggm.laad(ggm_pad) if ggm_pad.exists() else None
    gemma_data = gemma.laad(gemma_pad) if gemma_pad.exists() else None
    gebruikt = gebruikte_ids(alle)
    cl = _cluster(cluster, alle, index) if cluster else None
    lijst = begrippen_van(onderwerp, alle, bronbegrippen(wiki, onderwerp), index, cl)
    ons = {b.bid for b in lijst if b.bid}
    a = afb[onderwerp]
    secties: dict[str, list[str]] = {}

    # Onderwerp en besluiten
    from llmwiki import sources

    def brontype(b: str) -> str:
        try:
            return sources.read_index_entry(repo, b).get("brontype", "?")
        except FileNotFoundError:
            return "?"

    bronnen = list(dict.fromkeys([*(a.get("bronnen") or []), *(p.stem for p in gam_gemeen.bronduidingen(wiki, onderwerp))]))
    kort = {b: f"B{i}" for i, b in enumerate(bronnen, 1)}
    regels = [f"{a.get('naam', onderwerp)} ({a.get('niveau', '?')}, {a.get('status', '?')}).", "", "Bronnen:", "",
              *(f"- {kort[b]}: {b} ({brontype(b)})" for b in bronnen), "", "Besluiten (zonder de herziene):", ""]
    besluiten = [r for r in opzoeken.besluiten(wiki, onderwerp) if "[stand: herzien" not in r]
    if cl:
        besluiten = [r for r in besluiten if r.startswith(f"[{onderwerp}]") or r.split("]")[0][1:] in ons]
    regels += [f"- {r}" for r in besluiten] or ["- geen"]
    secties["Onderwerp"] = regels
    elders = {norm(b["begrip"]): b.get("datum", "") for b in a.get("besluiten") or [] if b.get("begrip")}

    secties["Onderwerpen"] = [f"- {oid} ({o.get('niveau', '?')}): {_kort(re.split(r'(?<=\.)\s(?=[A-Z])', str((o.get('omschrijving') or [''])[0]))[0], 220)}"
                              for oid, o in afb.items()]

    # Begrippen
    regels = ["| Begrip | In de bron | Vindplaats | Catalogus |", "|---|---|---|---|"]
    for b in lijst:
        if b.bron:
            inbron = "; ".join(f"{o} ({kort.get(bron, bron)})" for bron, o, _ in b.bron.vermeldingen)
            if b.bron.andere:
                inbron += f"; ook: {', '.join(b.bron.andere)}"
            vind = "; ".join(f"{v} ({kort.get(bron, bron)})" for bron, _, v in b.bron.vermeldingen if v)
        else:
            inbron, vind = alle[b.bid].get("definitie") or "", "-"
        if b.bid:
            cat = catalogus(b.bid, alle[b.bid], ggm_data, gemma_data)
        else:
            cat = "nieuw" + (f"; besluit onderwerp {elders[norm(b.naam)]}" if norm(b.naam) in elders else "") \
                + (f"; genoemd in {', '.join(g)}" if (g := genoemd_in(alle, b.naam)) else "")
        regels.append(f"| {_cel(b.naam)} | {_cel(_kort(inbron, 300))} | {_cel(vind)} | {_cel(cat)} |")
    secties["Begrippen"] = regels

    te_doen = [b for b in lijst if b.bron and (alles or not b.bid)]

    # Passages
    regels = []
    for b in te_doen:
        ps = [p for bron, _, v in b.bron.vermeldingen for p in passages(repo, bron, b.naam, v)]
        regels.append(f"- **{b.naam}**")
        regels += [f"  - {kort.get(p.bron, p.bron)}, {p.waar} (regel {p.van}–{p.tot}): {p.tekst}" for p in ps] \
            or ["  - geen passage gevonden"]
    secties["Passages"] = regels

    # Kandidaten
    for titel, data, functie in (("GGM-kandidaten", ggm_data, ggm_kandidaten), ("GEMMA-kandidaten", gemma_data, gemma_kandidaten)):
        regels = []
        if data is None:
            regels.append("Model niet gevonden; draai de release-skill.")
        for b in te_doen if data is not None else []:
            regels.append(f"- **{b.naam}**")
            regels += [f"  {r}" for r in functie(data, b.naam, b.bron.andere, gebruikt)] or ["  geen"]
        secties[titel] = regels

    # UPL
    namen = [n for b in lijst for n in [b.naam, *(b.bron.andere if b.bron else [])]]
    wetten_ = [] if cl else wetten(repo, a.get("bronnen") or [])
    dekking = upl_dekking(alle)
    regels = ["| Lijst | Nr | Product | Grondslag | Domein | Doelgroep | Soort | Niveau | Logius | Waarom | In de wiki |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for p, reden in upl_selectie(upl_producten(wiki, repo), wetten_, namen):
        door = set(dekking.get((p.lijst, p.nr), set())) | ({index[norm(p.naam)]} if norm(p.naam) in index else set())
        lijstnaam = "logius" if "logius" in p.lijst else "intern" if "intern" in p.lijst else "extern"
        regels.append(f"| {lijstnaam} | {p.nr or '-'} | {_cel(p.naam)} | {_cel(_kort('; '.join(p.grondslag), 120))} | {_cel(p.domein)} | "
                      f"{p.doelgroep} | {_cel(p.soort)} | {_cel(p.niveau)} | {p.vlaggen} | {_cel(reden)} | {', '.join(sorted(door)) or '-'} |")
    secties["UPL"] = regels

    # Relaties
    afgeleid = {bid: d for bid, d in alle.items() if _uitkomst(d)}
    kandidaten, vervallen = relaties.uit_bronnen(relaties.bronrelaties(wiki, onderwerp), afgeleid)
    regels = []
    for k in kandidaten:
        if cl and not {k.bron, k.doel} & ons:
            continue
        r = relaties.als_relatie(k)
        staat = any(x.get("naar") == k.doel and x.get("soort") == r["soort"] for x in alle[k.bron].get("relaties") or [])
        regels.append(f"- {k.bron} → {r['soort']} → {k.doel} ({k.naam or 'zonder naam'}) | {k.vindplaats} | "
                      f"{', '.join(kort.get(b, b) for b in k.bronnen)}{' | staat al in de beoordeling' if staat else ''}")
    regels += ["", "Vervallen (een kant is geen element):", ""]
    for v in vervallen:
        if cl and not any(n in norm(v["van"]) or n in norm(v["naar"]) for n in cl[1]):
            continue
        regels.append(f"- {v['van']} — {v['werkwoord']} → {v['naar']} | {v['vindplaats']}: {v['reden']}")
    secties["Relatievoorstellen"] = regels

    # Modelleerafspraken
    typen = sorted({_uitkomst(alle[b]).get("paginatype") for b in ons} - {None})
    regels = ["- kennismodel/modelleerregels.md (altijd)"]
    for t in typen:
        regels += [f"- {t}: kennismodel/{e.laag}/{e.sleutel}-modelleerafspraken.md" for e in kennismodel.ELEMENTTYPEN if e.paginatype == t]
    secties["Modelleerafspraken"] = regels

    # Terugmeldingen
    regels = []
    for naam, pad in REGISTERS.items():
        if not (wiki / pad).exists():
            continue
        for m in (yaml.safe_load((wiki / pad).read_text(encoding="utf-8")) or {}).get("terugmeldingen") or []:
            elementen = [m["element"]] if m.get("element") else list(m.get("elementen") or [])
            if not set(elementen) & ons:
                continue
            onderwerp_van = m.get("entiteit") or m.get("beleidsdomein") or ""
            bevinding = m.get("bevinding") or [""]
            eerste = bevinding[0] if isinstance(bevinding, list) else bevinding
            regels.append(f"- {naam} nr {m.get('nummer', 'nieuw')} ({m.get('type', '?')}, {m.get('status', 'open')}): "
                          f"{', '.join(elementen)}{' — ' + onderwerp_van if onderwerp_van else ''}: {_kort(eerste, 140)}")
    secties["Terugmeldingen"] = regels or ["- geen"]

    kop = f"# Werkpakket {onderwerp}{' — cluster ' + cluster if cluster else ''}"
    uitleg = ("Gemaakt door tools/werkpakket.py; niet bewerken, niet committen. Passages en kandidaten staan hier voor "
              f"{'alle begrippen' if alles else 'de nieuwe begrippen'}. GGM en GEMMA: '=' is een naamgenoot, '~' een "
              "treffer op naam, synoniem of definitie, '≈' een "
              "treffer op een woord uit de naam (alleen als de hele naam niets vindt).")
    tekst = "\n\n".join([kop, uitleg, *(f"## {s}\n\n" + "\n".join(r) for s, r in secties.items())]) + "\n"
    return tekst, {s: sum(1 for x in r if x.startswith(("- ", "| ", "  "))) for s, r in secties.items()}


def pad_van(wiki: Path, onderwerp: str, cluster: str | None) -> Path:
    naam = f"{onderwerp}-{cluster}" if cluster else onderwerp
    return paths.find_repo_root(wiki) / ".work" / "werkpakket" / f"{naam}.md"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    parser.add_argument("onderwerp")
    parser.add_argument("--cluster", help="kernobject (id, naam of synoniem)")
    parser.add_argument("--alles", action="store_true", help="passages en kandidaten ook voor begrippen met een beoordeling")
    a = parser.parse_args(argv)
    try:
        tekst, tellingen = maak(a.wiki, a.onderwerp, a.cluster, a.alles)
    except Fout as exc:
        print(f"fout: {exc}")
        return 1
    pad = pad_van(a.wiki, a.onderwerp, a.cluster)
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(tekst, encoding="utf-8")
    print(f"{pad.relative_to(paths.find_repo_root(a.wiki))}: {len(tekst.split())} woorden")
    print("; ".join(f"{s} {n}" for s, n in tellingen.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
