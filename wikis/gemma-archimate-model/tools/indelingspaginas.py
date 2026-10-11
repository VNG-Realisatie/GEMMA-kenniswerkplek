"""De pagina's van de indelingen: de onderwerpen, de beleidsdomeinen en de bedrijfsfuncties, met dekking.

Een pagina toont een indeling as-is: een overgenomen indeling (beleidsdomeinen, bedrijfsfuncties) letterlijk uit het
GEMMA-model, de ontstane indeling van de onderwerpen uit de afbakeningen, en per knoop de elementen van de wiki eronder.
Zo zijn de gaten te zien die de bronnen nog niet hebben gevonden (ARCHITECTURE.md, sectie 4.4, Dekking). Alles wordt
gegenereerd door tools/render.py, dat de paginatekst, de tellingen en de links maakt; niemand houdt ze met de hand bij.

Een knoop van de functiehiërarchie is een functie die zelf geen element van de wiki is (een knoop zonder beoordeling).
Een element hangt in de hiërarchie op de plek van zijn GEMMA-match (een functie), of onder de bovenliggende functie
(`gemma_functie`, of de aggregatie vanaf een functie van de wiki). Een product hangt aan de domeingroepering.

Gebruik: alleen via tools/render.py (`paginas`).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402
import gemma as gemmatool  # noqa: E402

MAP = "elementpaginas/overig/indelingen"
NAMEN = ("onderwerpen", "beleidsdomeinen", "bedrijfsfuncties")
GEMMA_TYPE_TAAKVELD = "Taakveld Iv3"
GEMMA_TYPE_BELEIDSDOMEIN = "Beleidsdomein"


def pad(naam: str) -> str:
    return f"{MAP}/{naam}.md"


def _koppen(naam: str, titel: str, regels: list[str], bron: str) -> tuple[dict, list[str]]:
    meta = {"id": naam, "type": "indeling", "naam": titel}
    kop = [f"# Indeling: {titel}", "", f"<!-- Gegenereerd door tools/render.py uit {bron}. Wijzig de beoordeling, niet deze pagina. -->", ""]
    return meta, kop + regels


def _links(w, van: str, ids: list[str]) -> str:
    return ", ".join(w.link(van, i) for i in sorted(dict.fromkeys(ids), key=lambda i: w.naam(i).lower()))


def _per_type(w, van: str, ids: list[str]) -> list[str]:
    """Per paginatype een regel met de links."""
    uit = []
    for t in sorted({w.paginatype(i) for i in ids}):
        uit.append(f"**{t}** ({len([i for i in ids if w.paginatype(i) == t])}): "
                   + _links(w, van, [i for i in ids if w.paginatype(i) == t]))
    return uit


def elementen(w) -> list[str]:
    """De elementen van de wiki: wat een pagina heeft en niet is afgewezen."""
    return sorted((b for b in w.begrippen if w.is_element(b)), key=lambda b: w.naam(b).lower())


# --- De onderwerpen (ontstaan uit de bronnen) ---


def onderwerpen_pagina(w) -> tuple[dict, list[str]]:
    van = pad("onderwerpen")
    alle = elementen(w)
    r = ["De ontstane indeling: de thuisonderwerpen (ARCHITECTURE.md, sectie 3.3), van eigen onderwerp naar thematisch "
         "gedeeld onderwerp en Kern. Per onderwerp de elementen met dat onderwerp als thuis; een element heeft er één. "
         "Ze zijn niet leidend: de indelingen worden later geconsolideerd.", ""]
    for niveau in gam_gemeen.NIVEAUS:
        leden = [(oid, o) for oid, o in w.onderwerpen.items() if o.get("niveau") == niveau]
        if not leden:
            continue
        r += [f"## Niveau {niveau}", ""]
        for oid, o in leden:
            eigen = [b for b in alle if gam_gemeen.thuis(w.begrippen[b]) == oid]
            r += [f"### [{o['naam']}]({w.rel(van, gam_gemeen.begrippen_pad(oid))})", "",
                  f"Status: {o.get('status', '—')}. Overzicht: [overzicht]({w.rel(van, gam_gemeen.overzicht_pad(oid))}).", ""]
            r += [f"- {regel}" for regel in _per_type(w, van, eigen)] or ["- nog geen elementen"]
            r.append("")
    return _koppen("onderwerpen", "onderwerpen", r, "de afbakeningen en de beoordelingen")


# --- De beleidsdomeinen (overgenomen uit GEMMA en het register) ---


def _nummer(taakveld: str) -> str:
    return (taakveld or "").split()[:1][0] if (taakveld or "").split() else ""


def beleidsdomeinen_pagina(w, gemma_data: dict) -> tuple[dict, list[str]]:
    van = pad("beleidsdomeinen")
    el = gemma_data["elementen"]
    alle = elementen(w)
    per_bd: dict[str, list[str]] = {}
    for b in alle:
        bd = w.begrippen[b].get("beleidsdomein")
        if bd:
            per_bd.setdefault(bd.strip().lower(), []).append(b)
    taakvelden = sorted((e for e in el.values() if e["eigenschappen"].get("GEMMA type") == GEMMA_TYPE_TAAKVELD),
                        key=lambda e: e["naam"])
    onder: dict[str, list[str]] = {}
    for rel in gemma_data["relaties"].values():
        b, d = el.get(rel["bron"]), el.get(rel["doel"])
        if rel["type"] in gemmatool.FUNCTIEKETEN and b and d and d["eigenschappen"].get("GEMMA type") == GEMMA_TYPE_BELEIDSDOMEIN \
                and b["eigenschappen"].get("GEMMA type") in (GEMMA_TYPE_TAAKVELD, GEMMA_TYPE_BELEIDSDOMEIN):
            onder.setdefault(b["id"], []).append(d["id"])
    gemma_namen = {e["naam"].strip().lower() for e in el.values()
                   if e["eigenschappen"].get("GEMMA type") == GEMMA_TYPE_BELEIDSDOMEIN}
    nieuw_per_taakveld: dict[str, list[str]] = {}
    for naam, bd in sorted(w.beleidsdomeinen.items()):
        if naam.strip().lower() not in gemma_namen:
            nieuw_per_taakveld.setdefault(_nummer(bd.get("taakveld", "")), []).append(naam)
    for b in alle:
        d = w.begrippen[b]
        bd = d.get("beleidsdomein")
        if bd and bd.strip().lower() not in gemma_namen and bd not in w.beleidsdomeinen \
                and bd not in nieuw_per_taakveld.get(_nummer(d.get("taakveld", "")), []):
            nieuw_per_taakveld.setdefault(_nummer(d.get("taakveld", "")), []).append(bd)

    totaal = metinhoud = 0

    def knoop(i: str, diepte: int) -> tuple[list[str], bool]:
        nonlocal totaal, metinhoud
        e = el[i]
        eigen = per_bd.get(e["naam"].strip().lower(), [])
        kinderen = [knoop(k, diepte + 1) for k in sorted(onder.get(i, []), key=lambda k: el[k]["naam"])]
        heeft = bool(eigen) or any(h for _, h in kinderen)
        totaal += 1
        metinhoud += bool(eigen)
        regels = ["  " * diepte + f"- {'**' + e['naam'] + '**' if eigen else e['naam']}"
                  + (f" ({len(eigen)} elementen)" if eigen else "")]
        regels += ["  " * (diepte + 1) + f"- {x}" for x in _per_type(w, van, eigen)]
        for k, _ in kinderen:
            regels += k
        return regels, heeft

    r = []
    for tv in taakvelden:
        regels, _ = [], False
        kinderen = [knoop(k, 1) for k in sorted(onder.get(tv["id"], []), key=lambda k: el[k]["naam"])]
        nummer = _nummer(tv["naam"])
        nieuw = nieuw_per_taakveld.pop(nummer, [])
        r += [f"- **{tv['naam']}** *(taakveld Iv3)*"]
        for k, _ in kinderen:
            r += k
        for naam in nieuw:
            totaal += 1
            eigen = per_bd.get(naam.strip().lower(), [])
            metinhoud += bool(eigen)
            r += [f"  - {'**' + naam + '**' if eigen else naam} *(nieuw: niet in GEMMA)*" + (f" ({len(eigen)} elementen)" if eigen else "")]
            r += [f"    - {x}" for x in _per_type(w, van, eigen)]
    for nummer, namen in sorted(nieuw_per_taakveld.items()):
        r += [f"- **Taakveld {nummer or '—'}** *(niet in GEMMA)*"]
        for naam in namen:
            totaal += 1
            eigen = per_bd.get(naam.strip().lower(), [])
            metinhoud += bool(eigen)
            r += [f"  - {'**' + naam + '**' if eigen else naam} *(nieuw: niet in GEMMA)*"]
            r += [f"    - {x}" for x in _per_type(w, van, eigen)]
    kop = ["De Beleidsdomeinindeling zoals GEMMA haar kent (taakveld Iv3 › beleidsdomein), as-is uit het GEMMA-model, aangevuld "
           "met de beleidsdomeinen die GEMMA niet kent (gemarkeerd). Per beleidsdomein de elementen van de wiki; een vet "
           "beleidsdomein heeft inhoud.", "",
           f"Beleidsdomeinen: {totaal}; met elementen van de wiki: {metinhoud}.", ""]
    return _koppen("beleidsdomeinen", "beleidsdomeinen", kop + r, "het GEMMA-model, het register van beleidsdomeinen en de beoordelingen")


# --- De bedrijfsfuncties (overgenomen uit GEMMA) ---


def plaatsing(w, gemma_data: dict, h: dict) -> tuple[dict[str, list[str]], dict[str, list[str]], list[str]]:
    """(elementen die de knoop zijn, elementen eronder, elementen zonder plek). Een functie met GEMMA-match is de knoop;
    een functie zonder match en een dienst hangen onder de bovenliggende functie (`gemma_functie`, of de aggregatie vanaf een
    functie van de wiki); een product aan de domeingroepering met de naam van zijn domein."""
    el = gemma_data["elementen"]
    wortel_op_naam = {el[i]["naam"]: i for i in h["wortels"]}
    functies = [b for b in elementen(w) if w.paginatype(b) == "bedrijfsfunctie"]
    zelf: dict[str, list[str]] = {}
    for b in functies:
        gid = (w.begrippen[b].get("gemma") or {}).get("id")
        if gid in el:
            zelf.setdefault(gid, []).append(b)
    knoop_van = {b: i for i, bs in zelf.items() for b in bs}

    def ouder(b: str, diepte: int = 0) -> str | None:
        gf = (w.begrippen[b].get("gemma_functie") or {}).get("id")
        if gf in el:
            return gf
        for v in w.inkomend_van(b, "aggregatie"):
            if w.paginatype(v) == "bedrijfsfunctie":
                return knoop_van.get(v) or (ouder(v, diepte + 1) if diepte < 10 else None)
        return None

    onder: dict[str, list[str]] = {}
    zonder: list[str] = []
    for b in elementen(w):
        t = w.paginatype(b)
        if t == "bedrijfsfunctie" and b in knoop_van:
            continue
        if t in ("bedrijfsfunctie", "dienst"):
            o = ouder(b)
            if o:
                onder.setdefault(o, []).append(b)
            elif t == "dienst" or b not in knoop_van:
                zonder.append(b)
        elif t == "product":
            o = wortel_op_naam.get(w.begrippen[b].get("domein") or "")
            if o:
                onder.setdefault(o, []).append(b)
            else:
                zonder.append(b)
    return zelf, onder, zonder


def bedrijfsfuncties_pagina(w, gemma_data: dict) -> tuple[dict, list[str]]:
    van = pad("bedrijfsfuncties")
    el = gemma_data["elementen"]
    h = gemmatool.functiehierarchie(gemma_data)
    zelf, onder, zonder = plaatsing(w, gemma_data, h)
    inhoud: dict[str, bool] = {}

    def heeft_inhoud(i: str, pad_: frozenset = frozenset()) -> bool:
        if i not in inhoud:
            inhoud[i] = bool(zelf.get(i) or onder.get(i)) or any(
                heeft_inhoud(k, pad_ | {i}) for k, _ in h["onder"].get(i, []) if k not in pad_)
        return inhoud[i]

    def regel(i: str, diepte: int) -> list[str]:
        e = el[i]
        eigen, daaronder = zelf.get(i, []), onder.get(i, [])
        vet = heeft_inhoud(i)
        tekst = "  " * diepte + f"- {'**' + e['naam'] + '**' if vet else e['naam']}"
        if eigen:
            tekst += " → " + _links(w, van, eigen)
        regels = [tekst]
        for x in _per_type(w, van, daaronder):
            regels.append("  " * (diepte + 1) + f"- {x}")
        for k, _ in sorted(h["onder"].get(i, []), key=lambda x: el[x[0]]["naam"]):
            regels += regel(k, diepte + 1)
        return regels

    knopen = {i for i in h["onder"]} | {k for kinderen in h["onder"].values() for k, _ in kinderen}
    r = []
    for wortel in h["wortels"]:
        r += [f"## {el[wortel]['naam']}", ""]
        r += [f"- {x}" for x in _per_type(w, van, onder.get(wortel, []))]
        r += regel_(wortel, regel, h, el)
        r.append("")
    if zonder:
        r += ["## Zonder plek in de hiërarchie", "",
              "Functies en diensten die nog niet onder een bovenliggende functie hangen (`gemma_functie` of een aggregatie): "
              + _links(w, van, zonder) + ".", ""]
    kop = ["De functiehiërarchie van het GEMMA-model, as-is (Functie-indeling naar domein): de domeinen, de functies en "
           "subfuncties, zonder beoordeling. Een functie met een pijl is een element van de wiki. Per functie de diensten, "
           "producten en functies van de wiki eronder; een vette functie heeft inhoud, zelf of eronder. Een functie die in "
           "GEMMA onder meer functies hangt, staat onder elk daarvan.", "",
           f"Functies: {len([i for i in knopen if el[i]['type'] == 'business-function'])}; "
           f"met inhoud van de wiki: {len([i for i in knopen if el[i]['type'] == 'business-function' and heeft_inhoud(i)])}.", ""]
    return _koppen("bedrijfsfuncties", "bedrijfsfuncties", kop + r, "het GEMMA-model en de beoordelingen")


def regel_(wortel: str, regel, h: dict, el: dict) -> list[str]:
    uit = []
    for k, _ in sorted(h["onder"].get(wortel, []), key=lambda x: el[x[0]]["naam"]):
        uit += regel(k, 0)
    return uit


def paginas(w, gemma_data: dict | None) -> dict[str, tuple[dict, list[str]]]:
    """Naam → (frontmatter, regels). De pagina's van het GEMMA-model alleen als het model aanwezig is."""
    uit = {"onderwerpen": onderwerpen_pagina(w)}
    if gemma_data:
        uit["beleidsdomeinen"] = beleidsdomeinen_pagina(w, gemma_data)
        uit["bedrijfsfuncties"] = bedrijfsfuncties_pagina(w, gemma_data)
    return uit
