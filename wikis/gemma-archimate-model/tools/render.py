"""Render: alle leesbare pagina's van deze wiki uit de beoordelingen.

Invoer (alleen lezen): `beoordelingen/begrippen/<id>.yaml` (het oordeel van de AI, met `status` en `afgeleid` van
tools/afleiden.py), `beoordelingen/onderwerpen/<id>.yaml`, `beoordelingen/terugmeldingen.yaml`, `log.md`, `wiki.yaml`,
de bronanalyses en `sources/index` (titels). Het script oordeelt niet en schrijft nooit in `beoordelingen/`.

Uitvoer (gegenereerd; nooit met de hand bewerken, de pre-commit-controle `--check` vangt dat):

| Bestand | Inhoud |
|---|---|
| `<map van het type>/<taakveld>/<beleidsdomein>/<id>.md` (pad uit `afgeleid.pad`) | Elementpagina |
| `begrippen/<onderwerp>.md` | Begrippenlijst: per begrip de uitkomst, de reden, de herkomst en de GGM-entiteit |
| `analyses/ggm-terugmeldingen.md` | Doorlopende lijst van GGM-terugmeldingen |
| `ter-beoordeling.md` | Wat wacht op akkoord (review), en wat nog moet worden voorgelegd |
| `voortgang.md` | Aantallen per onderwerp, type en status |

Opbouw van een elementpagina (vaste volgorde; een sectie zonder inhoud vervalt): frontmatter (gegevens en de
letterlijke `ggm_*`/`gemma_*`-velden), titel en status, Ter discussie; Betekenis (Definitie, Beschrijving, Per
onderwerp, Synoniemen, Naamkeuze, Homoniemen); Plaats in het model (Typering, Kenmerken alleen met ja, Generalisatie,
Specialisaties, GGM-componenten, Tegenhanger, Relaties uitgaand en inkomend); Herkomst (Bronnen met korte titel,
Afstemming met GGM met de GGM-terugmeldingen, Afstemming met GEMMA, Besluiten redacteur). Een bron heet in links naar
haar `korte_titel` uit de bronanalyse.

Wat de render garandeert: elke bronverwijzing is een link naar de bronanalyse (de domein-lens; een modelbron linkt
naar sources/raw), relaties staan in beide richtingen, er staan geen verwijzingen in de frontmatter en geen links naar
tools of regels, en elke alinea staat op één regel. Twee keer renderen geeft hetzelfde resultaat.

Gebruik (vanuit de wikimap):
    uv run python tools/render.py                    # alles opnieuw maken
    uv run python tools/render.py --check            # pagina's gelijk aan de beoordelingen? (pre-commit)
    uv run python tools/render.py --voorbeeld <id>   # één elementpagina naar het scherm
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import bepaal_type  # noqa: E402
import gam_gemeen  # noqa: E402
from llmwiki import beoordeling, frontmatter, paths  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
ONDERWERPEN = Path("beoordelingen") / "onderwerpen"
TERUGMELDINGEN = Path("beoordelingen") / "terugmeldingen.yaml"
TER_BEOORDELING = Path("ter-beoordeling.md")
VOORTGANG = Path("voortgang.md")
TERUGMELDLIJST = Path("analyses") / "ggm-terugmeldingen.md"
STATUSSEN = ["kandidaat", "review", "goedgekeurd", "afgewezen"]
STATUSREGEL = {
    "kandidaat": "**Status: kandidaat.** Er staat een vraag open voor de redacteur (zie *Ter discussie*).",
    "review": "**Status: review.** Wacht op het akkoord van de redacteur.",
    "goedgekeurd": "**Status: goedgekeurd** door de redacteur.",
}
UITKOMST = {"synoniem": "synoniem", "bron": "bron, geen begrip", "buiten_scope": "buiten scope",
            "buiten_model": "buiten het model", "eigenschap": "eigenschap", "onderdeel": "onderdeel",
            "verwijzing": "verwijzing", "specialisatie": "specialisatie zonder pagina", "geen_element": "geen element",
            "conflict": "tegenstrijdige kenmerken", "herkend": "herkend, geen paginatype", "geen_pagina": "geen pagina"}
ARCHIMATE_NAAM = {t.archimate_type: t.naam for t in bepaal_type.TYPEN}
# De vraag per kenmerk, zonder de aanwijzingen ("Noem ..."): de pagina toont alleen de kenmerken met ja.
VRAAG = {k.sleutel: re.sub(r"\s*Noem [^?.]*[.?]", "", k.vraag).strip() for k in bepaal_type.KENMERKEN}


def _gegenereerd(bron: str) -> str:
    return f"<!-- Gegenereerd door tools/render.py uit {bron}. Wijzig de beoordeling, niet deze pagina. -->"


def _yaml(meta: dict) -> str:
    return yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10**9).strip()


def _pagina(meta: dict, regels: list[str]) -> str:
    body = "\n".join(regels).strip("\n")
    while "\n\n\n" in body:
        body = body.replace("\n\n\n", "\n\n")
    return f"---\n{_yaml(meta)}\n---\n\n{body}\n"


def _cel(tekst) -> str:
    return " ".join(("" if tekst is None else str(tekst)).split()).replace("|", "\\|")


def _tabel(kolommen: list[str], rijen: list[list]) -> list[str]:
    return ["| " + " | ".join(kolommen) + " |", "|" + "---|" * len(kolommen),
            *["| " + " | ".join(_cel(c) for c in rij) + " |" for rij in rijen], ""]


def _sectie(kop: str, regels: list[str]) -> list[str]:
    return [f"## {kop}", "", *regels, ""] if regels else []


class Wiki:
    def __init__(self, wiki_root: Path):
        self.root = wiki_root
        self.yaml = paths.load_wiki_yaml(wiki_root)
        self.repo = paths.find_repo_root(wiki_root)
        self.begrippen = {bid: data for bid, (_, data) in beoordeling.alle(wiki_root, self.yaml).items()}
        self.onderwerpen = {p.stem: beoordeling.laad(p) for p in sorted((wiki_root / ONDERWERPEN).glob("*.yaml"))}
        register = wiki_root / TERUGMELDINGEN
        self.terugmeldingen = beoordeling.laad(register).get("terugmeldingen", []) if register.exists() else []
        log = wiki_root / "log.md"
        self.log = log.read_text(encoding="utf-8") if log.exists() else ""
        self.onderwerp_dir = self.yaml["page_types"].get("onderwerp", {}).get("dir", "begrippen")
        self._titels: dict[str, str] = {}

    def pad(self, bid: str) -> str | None:
        return (self.begrippen.get(bid, {}).get("afgeleid") or {}).get("pad")

    def naam(self, bid: str) -> str:
        return self.begrippen.get(bid, {}).get("begrip", bid)

    def link(self, van: str, bid: str, tekst: str | None = None) -> str:
        """Link vanaf pagina `van` (relatief aan de wiki) naar de pagina van element `bid`; platte tekst zonder pagina."""
        doel = self.pad(bid)
        tekst = (tekst or self.naam(bid)).replace("[", "(").replace("]", ")")
        return f"[{tekst}]({self.rel(van, doel)})" if doel else tekst

    def rel(self, van: str, naar: str | Path) -> str:
        return gam_gemeen.relatief(self.root / van, Path(naar) if Path(naar).is_absolute() else self.root / naar)

    def titel(self, bron_id: str) -> str:
        if bron_id not in self._titels:
            pad = self.repo / "sources" / "index" / f"{bron_id}.md"
            self._titels[bron_id] = frontmatter.read(pad).meta.get("titel", bron_id) if pad.exists() else bron_id
        return self._titels[bron_id]

    def korte_titel(self, bron_id: str) -> str:
        """Linktekst van een bron: `korte_titel` uit de bronanalyse; een modelbron heet GGM of GEMMA."""
        for model in ("ggm", "gemma"):
            if self.yaml.get(model, {}).get("bron") == bron_id:
                return model.upper()
        doel = gam_gemeen.bron_doel(self.root, bron_id)
        binnen = doel is not None and doel.is_relative_to(self.root.resolve())
        return (frontmatter.read(doel).meta.get("korte_titel") if binnen else None) or self.titel(bron_id)

    def bron(self, van: str, bron_id: str, tekst: str | None = None) -> str:
        doel = gam_gemeen.bron_doel(self.root, bron_id)
        return f"[{tekst or bron_id}]({gam_gemeen.relatief(self.root / van, doel)})" if doel else bron_id

    def bronnen(self, van: str, ids: list[str], vindplaats: str | None = None) -> str:
        cel = ", ".join(self.bron(van, b, self.korte_titel(b)) for b in ids)
        return f"{cel} ({vindplaats})" if vindplaats and cel else (vindplaats or cel)

    def tekst(self, van: str, tekst: str) -> str:
        """Lopende tekst van de AI: bron-id's worden links naar de bronanalyse."""
        return gam_gemeen.bronnen_als_link(self.root / van, " ".join(str(tekst).split()), self.root)

    def alineas(self, van: str, alineas) -> list[str]:
        regels = []
        for a in alineas or []:
            regels += [self.tekst(van, a), ""]
        return regels

    def inkomend(self, bid: str) -> list[tuple[str, dict]]:
        return [(van, r) for van, data in sorted(self.begrippen.items()) if self.pad(van)
                for r in data.get("relaties", []) if r["naar"] == bid]

    def gewijzigd_na_akkoord(self, bid: str) -> bool:
        return any(f"] promote | {bid} |" in r for r in self.log.splitlines())


# --- Elementpagina ---


def _ja(onderbouwing: str) -> str:
    """'Ja, ' voor de onderbouwing; een eerste woord als 'De' wordt 'de', een afkorting als 'GGM' blijft staan."""
    o = " ".join(str(onderbouwing).split())
    if len(o) > 1 and o[0].isupper() and not o[1].isupper():
        o = o[0].lower() + o[1:]
    return f"Ja, {o}"


def _sub(kop: str, regels: list[str], niveau: int = 3) -> list[str]:
    return [f"{'#' * niveau} {kop}", "", *regels, ""] if regels else []


def _groep(kop: str, delen: list[list[str]]) -> list[str]:
    """Een hoofdsectie (##) met subsecties (###); zonder inhoud vervalt de hoofdsectie."""
    regels = [x for deel in delen for x in deel]
    return [f"## {kop}", "", *regels] if regels else []


def element_pagina(w: Wiki, bid: str) -> str:
    d = w.begrippen[bid]
    a = d["afgeleid"]
    u = a["uitkomst"]
    van = a["pad"]
    status = d["status"]
    ggm, gemma = a.get("ggm", {}), a.get("gemma", {})
    meta = {
        "id": bid, "type": u["paginatype"], "archimate_type": u["archimate_type"], "status": status,
        "naam": d["begrip"], "onderwerpen": d["onderwerpen"],
        **{k: d[k] for k in ("taakveld", "beleidsdomein") if d.get(k)},
        "definitie": d["definitie"], "grondslag": d["grondslag"],
        "match": {k: d[k]["sterkte"] for k in ("ggm", "gemma") if d.get(k)},
        "data_object": u.get("data_object", "nee"),
        **({"procesniveau": u["procesniveau"]} if u.get("procesniveau") else {}),
        "synoniemen": [f"{s['naam']} ({s['context']})" for s in d.get("synoniemen", [])],
        "bronnen": a.get("bronnen", []), **ggm, **gemma,
    }
    meta = {k: v for k, v in meta.items() if v not in ([], {}, None, "")}

    r = [f"# {d['begrip']}", "", _gegenereerd(f"beoordelingen/begrippen/{bid}.yaml"), "", STATUSREGEL[status], ""]
    discussie = [f"- {w.tekst(van, x)}" for x in a.get("open", []) + d.get("vragen", [])]
    r += _sectie("Ter discussie", discussie + ([""] if discussie else []))

    # Betekenis: wat het begrip is.
    definitie = [w.tekst(van, d["definitie"]), ""]
    if d.get("definitie_formeel"):
        fb = d["definitie_formeel_bron"]
        definitie += [f"> {_cel(d['definitie_formeel'])}", ">", f"> — {w.bron(van, fb['bron'], w.titel(fb['bron']))}, {fb['plaats']}", ""]
    per_onderwerp = []
    for oid, alineas in d.get("per_onderwerp", {}).items():
        onaam = w.onderwerpen.get(oid, {}).get("naam", oid)
        per_onderwerp += _sub(f"[{onaam}]({w.rel(van, f'{w.onderwerp_dir}/{oid}.md')})", w.alineas(van, alineas), 4)
    synoniemen = _tabel(["Synoniem", "Context"], [[s["naam"], s["context"]] for s in d.get("synoniemen", [])]) \
        if d.get("synoniemen") else []
    homoniemen = _tabel(["Begrip", "Betekenis", "Waar", "Naamkeuze"], [
        [w.link(van, h["element"], h["begrip"]) if h.get("element") else h["begrip"], h["betekenis"], h["waar"],
         h["naamkeuze"]] for h in d.get("homoniemen", [])]) if d.get("homoniemen") else []
    r += _groep("Betekenis", [
        _sub("Definitie", definitie), _sub("Beschrijving", w.alineas(van, d.get("beschrijving"))),
        _sub("Per onderwerp", per_onderwerp), _sub("Synoniemen", synoniemen),
        _sub("Naamkeuze", w.alineas(van, d.get("naamkeuze"))), _sub("Homoniemen", homoniemen)])

    # Plaats in het model: typering, kenmerken en samenhang met andere elementen.
    ja = [s for s in bepaal_type.SLEUTELS if d["kenmerken"][s]["waarde"] == "ja"]
    kenmerken = [[f"**{bepaal_type.NAAM[s]}**: {VRAAG[s]}",
                  " ".join(x for x in (w.tekst(van, _ja(d["kenmerken"][s]["onderbouwing"])),
                                       w.bronnen(van, d["kenmerken"][s].get("bronnen", []))) if x)] for s in ja]
    nee = len(bepaal_type.SLEUTELS) - len(ja)
    typering = [f"{ARCHIMATE_NAAM.get(u['archimate_type'], u['archimate_type'])}. "
                f"Uitkomst van de beslistabel: {u['toelichting']}.", ""]
    specialisaties = [*[f"- **{w.link(van, s['element'], s['naam']) if s.get('element') else s['naam']}**: "
                        f"{w.tekst(van, s['omschrijving'])}"
                        + "".join(f" ({k} {s[k]})" for k in ("ggm_guid", "ggm_attribuut") if s.get(k))
                        for s in d.get("specialisaties", [])], ""] if d.get("specialisaties") else []
    componenten = _tabel(["Component", "GGM-guid", "Toelichting"], [
        [c["naam"], c["guid"], c["toelichting"]] for c in d.get("ggm_componenten", [])]) if d.get("ggm_componenten") else []
    tegenhanger = ([f"{w.link(van, d['tegenhanger']['element'])}: {w.tekst(van, d['tegenhanger']['toelichting'])}", ""]
                   if d.get("tegenhanger") else [])

    def relatie(x: dict) -> str:
        soort = ", ".join(v for v in (x["soort"], x.get("kardinaliteit", "")) if v)
        return f"{x['naam']} *{soort}*" if x.get("naam") else soort

    def bron_cel(x: dict) -> str:
        cel = w.bronnen(van, x.get("bronnen", []), x.get("vindplaats"))
        ggm_relatie = ", ".join(x.get("ggm_relatie", []))
        return f"{cel}; GGM ({ggm_relatie})" if cel and ggm_relatie else (cel or (f"GGM ({ggm_relatie})" if ggm_relatie else ""))

    kolommen = ["Van", "Relatie", "Naar", "Bron"]
    uitgaand = _tabel(kolommen, [[d["begrip"], relatie(x), w.link(van, x["naar"]), bron_cel(x)]
                                 for x in d.get("relaties", [])]) if d.get("relaties") else []
    inkomend = [[w.link(van, v), relatie(x), d["begrip"], bron_cel(x)] for v, x in w.inkomend(bid)]
    relaties = _sub("Uitgaand", uitgaand, 4) + _sub("Inkomend", _tabel(kolommen, inkomend) if inkomend else [], 4)
    r += _groep("Plaats in het model", [
        _sub("Typering", typering),
        _sub("Kenmerken", [f"Alleen de kenmerken met ja; de overige {nee} zijn nee.", "",
                           *_tabel(["Kenmerk", "Onderbouwing"], kenmerken)]),
        _sub("Generalisatie", w.alineas(van, d.get("generalisatie"))), _sub("Specialisaties", specialisaties),
        _sub("GGM-componenten", componenten), _sub("Tegenhanger", tegenhanger), _sub("Relaties", relaties)])

    # Herkomst: waar het begrip is gevonden en hoe het aansluit op GGM en GEMMA.
    bronnen = [*w.alineas(van, d.get("grondslag_toelichting")),
               *_tabel(["Korte titel", "Bron"], [[w.bron(van, b, w.korte_titel(b)), w.titel(b)] for b in a.get("bronnen", [])])] \
        if a.get("bronnen") else []
    ggm_regels = []
    if d.get("ggm"):
        g = d["ggm"]
        if ggm:
            ggm_regels = [f"Match **{g['sterkte']}** met GGM-entiteit *{ggm['ggm_entiteit']}* (beleidsdomein "
                          f"{ggm.get('ggm_beleidsdomein', '—')}, taakveld {ggm.get('ggm_taakveld', '—')}). {w.tekst(van, g['onderbouwing'])}", ""]
            if ggm.get("ggm_definitie"):
                ggm_regels += [f"> {_cel(ggm['ggm_definitie'])}", ""]
        else:
            ggm_regels = [f"Geen GGM-entiteit. {w.tekst(van, g['onderbouwing'])}", ""]
        if a.get("ggm_duplicaten"):
            ggm_regels += ["Duplicaten in het GGM:", "", *_tabel(["Entiteit", "Beleidsdomein", "GUID", "Toelichting"], [
                [x.get("entiteit"), x.get("beleidsdomein"), x["guid"],
                 next((y["toelichting"] for y in g.get("duplicaten", []) if y["guid"] == x["guid"]), "")]
                for x in a["ggm_duplicaten"]])]
    meldingen = [m for m in w.terugmeldingen if m.get("element") == bid]
    if meldingen:
        lijst = w.rel(van, TERUGMELDLIJST)
        ggm_regels += ["GGM-terugmeldingen:", "", *[f"- [Nummer {m['nummer']}]({lijst}) ({m['type']}, {m.get('status', 'open')}): "
                                                   f"{w.tekst(van, m['bevinding'])}" for m in meldingen], ""]
    g = d["gemma"]
    if gemma:
        gemma_regels = [f"Match **{g['sterkte']}** met GEMMA-element *{gemma['gemma_naam']}* ({gemma.get('gemma_type', '')}). "
                        f"{w.tekst(van, g['onderbouwing'])}", ""]
        if gemma.get("gemma_definitie"):
            gemma_regels += [f"> {_cel(gemma['gemma_definitie'])}", ""]
    else:
        gemma_regels = [f"Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. {w.tekst(van, g['onderbouwing'])}", ""]
    besluiten = [f"- {b['datum']}: {w.tekst(van, b['besluit'])}" for b in d.get("besluiten", [])]
    r += _groep("Herkomst", [_sub("Bronnen", bronnen), _sub("Afstemming met GGM", ggm_regels),
                             _sub("Afstemming met GEMMA", gemma_regels), _sub("Besluiten redacteur", besluiten)])
    return _pagina(meta, r)


# --- Begrippenlijst per onderwerp ---


def _uitkomst_cel(w: Wiki, van: str, bid: str, d: dict) -> str:
    u = d["afgeleid"]["uitkomst"]
    if u["soort"] == "element":
        if d.get("status") == "afgewezen":
            return f"{ARCHIMATE_NAAM.get(u['archimate_type'], u['archimate_type'])}, afgewezen door de redacteur"
        return f"{w.link(van, bid)} — {ARCHIMATE_NAAM.get(u['archimate_type'], u['archimate_type'])} ({d['status']})"
    tekst = UITKOMST.get(u["soort"], u["soort"])
    verwijzing = d.get("synoniem_van") or u.get("genoemd_begrip")
    if verwijzing:
        doel = next((b for b, x in w.begrippen.items() if x.get("begrip", "").lower() == verwijzing.lower() or b == verwijzing), None)
        tekst += f" van {w.link(van, doel) if doel else verwijzing}"
    return tekst


def begrippenlijst(w: Wiki, oid: str) -> str:
    o = w.onderwerpen[oid]
    van = f"{w.onderwerp_dir}/{oid}.md"
    meta = {"id": oid, "type": "onderwerp", "naam": o["naam"], "status": o.get("status", "in-behandeling"),
            "bronnen": o.get("bronnen", [])}
    if o.get("conclusie"):
        meta["conclusie"] = o["conclusie"]
    r = [f"# {o['naam']}", "", _gegenereerd(f"beoordelingen/onderwerpen/{oid}.yaml en de beoordelingen van de begrippen"), ""]
    r += _sectie("Omschrijving", w.alineas(van, o.get("omschrijving")))
    r += _sectie("Bronnen", [f"- {w.bron(van, b, w.titel(b))}" for b in o.get("bronnen", [])] + [""])
    rijen = []
    for bid, d in sorted(w.begrippen.items(), key=lambda x: x[1]["begrip"].lower()):
        if oid not in d.get("onderwerpen", []) or "afgeleid" not in d:
            continue
        a = d["afgeleid"]
        reden = d.get("toelichting") or a["uitkomst"]["toelichting"]
        if a.get("open"):
            reden += " Voorleggen: " + "; ".join(a["open"]) + "."
        rijen.append([d["begrip"], _uitkomst_cel(w, van, bid, d), w.tekst(van, reden), a.get("herkomst", ""),
                      (a.get("ggm") or {}).get("ggm_entiteit", "—")])
    r += _sectie("Begrippen", _tabel(["Begrip", "Uitkomst", "Reden", "Herkomst", "GGM"], rijen) if rijen else ["Nog geen begrippen beoordeeld.", ""])
    r += _sectie("Open vragen", [f"- {w.tekst(van, v)}" for v in o.get("open_vragen", [])] + [""] if o.get("open_vragen") else [])
    return _pagina(meta, r)


# --- Overzichten ---


def terugmeldlijst(w: Wiki) -> str:
    van = TERUGMELDLIJST.as_posix()
    meta = {"id": "ggm-terugmeldingen", "type": "analyse", "titel": "GGM-terugmeldingen"}
    r = ["# GGM-terugmeldingen", "", _gegenereerd("beoordelingen/terugmeldingen.yaml"), "",
         "Bevindingen uit de beoordeling van elementen die aan het GGM-beheer worden teruggekoppeld.", ""]
    r += _sectie("Terugmeldingen", _tabel(["#", "Domein", "Entiteit", "Type", "Bevinding", "Element", "Status"], [
        [m["nummer"], m["domein"], m.get("entiteit") or "—", m["type"], w.tekst(van, m["bevinding"]),
         w.link(van, m["element"]) if m.get("element") else "—", m.get("status", "open")]
        for m in sorted(w.terugmeldingen, key=lambda m: m["nummer"])]))
    r += _sectie("Typen", _tabel(["Type", "Betekenis"], [
        ["hiaat", "Concept ontbreekt in het GGM"],
        ["definitie", "Entiteit bestaat, maar de definitie is onjuist, onvolledig of geen begripsdefinitie"],
        ["structuur", "Onhandige modellering (overerving, ontbrekende relatie, granulariteit)"],
        ["scope", "Entiteit hoort niet in dit beleidsdomein of ontbreekt in een ander"],
        ["duplicaat", "Zelfde concept met meerdere GUID's in verschillende beleidsdomeinen → samenvoegen"],
        ["homoniem", "Zelfde naam voor een ander concept in een ander beleidsdomein → hernoemen"],
        ["relatie", "Fout in een exact gematchte relatie (type, richting, kardinaliteit, naam, dubbel)"]]))
    r += _sectie("Status", ["open → gemeld → opgelost of afgewezen (met reden).", ""])
    return _pagina(meta, r)


def ter_beoordeling(w: Wiki) -> str:
    van = TER_BEOORDELING.as_posix()
    meta = {"id": "ter-beoordeling", "type": "analyse", "titel": "Ter beoordeling"}
    r = ["# Ter beoordeling", "", _gegenereerd("de beoordelingen"), "",
         "Wat wacht op het akkoord van de redacteur. Bekijk per element de pagina en de wijziging in Source Control. "
         "Geef akkoord door in de chat AKKOORD te typen; daarna worden alle elementen hieronder goedgekeurd.", ""]
    review = [(bid, d) for bid, d in sorted(w.begrippen.items(), key=lambda x: x[1]["begrip"].lower()) if d.get("status") == "review"]
    r += _sectie("Wacht op akkoord", _tabel(["Element", "Type", "Onderwerpen", "Nieuw of gewijzigd", "Definitie"], [
        [w.link(van, bid), ARCHIMATE_NAAM.get(d["afgeleid"]["uitkomst"]["archimate_type"], ""), ", ".join(d["onderwerpen"]),
         "gewijzigd na eerder akkoord" if w.gewijzigd_na_akkoord(bid) else "nieuw", d.get("definitie", "")]
        for bid, d in review]) if review else ["Niets.", ""])
    voorleggen = []
    for bid, d in sorted(w.begrippen.items(), key=lambda x: x[1]["begrip"].lower()):
        a = d.get("afgeleid", {})
        vragen = a.get("open", []) + (d.get("vragen", []) if d.get("status") != "goedgekeurd" else [])
        if vragen:
            soort = d.get("status") or UITKOMST.get(a["uitkomst"]["soort"], a["uitkomst"]["soort"])
            voorleggen += [f"**{w.link(van, bid)}** ({soort})", "", *[f"- {w.tekst(van, v)}" for v in vragen], ""]
    r += _sectie("Voor te leggen", voorleggen or ["Niets.", ""])
    return _pagina(meta, r)


def voortgang(w: Wiki) -> str:
    meta = {"id": "voortgang", "type": "analyse", "titel": "Voortgang"}
    r = ["# Voortgang", "", _gegenereerd("de beoordelingen"), ""]
    rijen = []
    for oid, o in w.onderwerpen.items():
        eigen = [d for d in w.begrippen.values() if oid in d.get("onderwerpen", [])]
        rijen.append([f"[{o['naam']}]({w.onderwerp_dir}/{oid}.md)", o.get("status", "in-behandeling"), len(eigen),
                      sum(1 for d in eigen if d.get("status"))])
    r += _sectie("Onderwerpen", _tabel(["Onderwerp", "Status", "Begrippen", "Elementen"], rijen))
    typen: dict[str, dict[str, int]] = {}
    for d in w.begrippen.values():
        if d.get("status"):
            t = typen.setdefault(d["afgeleid"]["uitkomst"]["paginatype"], {})
            t[d["status"]] = t.get(d["status"], 0) + 1
    r += _sectie("Elementen per type en status", _tabel(["Type", *STATUSSEN], [
        [t, *[typen[t].get(s, 0) for s in STATUSSEN]] for t in sorted(typen)]) if typen else ["Nog geen elementen.", ""])
    per_status: dict[str, int] = {}
    for m in w.terugmeldingen:
        per_status[m.get("status", "open")] = per_status.get(m.get("status", "open"), 0) + 1
    r += _sectie("GGM-terugmeldingen", [f"[{len(w.terugmeldingen)} terugmeldingen]({TERUGMELDLIJST.as_posix()}): "
                                        + ", ".join(f"{k} {v}" for k, v in sorted(per_status.items())) + ".", ""])
    return _pagina(meta, r)


# --- Alles ---


def render(wiki_root: Path = WIKI_ROOT) -> dict[str, str]:
    """Relatief pad → inhoud van elk gegenereerd bestand."""
    w = Wiki(wiki_root)
    uit = {}
    for bid, d in w.begrippen.items():
        if w.pad(bid) and d.get("status"):
            uit[w.pad(bid)] = element_pagina(w, bid)
    for oid in w.onderwerpen:
        uit[f"{w.onderwerp_dir}/{oid}.md"] = begrippenlijst(w, oid)
    uit[TERUGMELDLIJST.as_posix()] = terugmeldlijst(w)
    uit[TER_BEOORDELING.as_posix()] = ter_beoordeling(w)
    uit[VOORTGANG.as_posix()] = voortgang(w)
    return uit


def beheerd(wiki_root: Path) -> set[str]:
    """Bestaande bestanden die de render beheert: alle pagina's in de mappen van de elementtypen en de begrippenlijsten."""
    y = paths.load_wiki_yaml(wiki_root)
    mappen = [d["dir"] for d in y["page_types"].values() if d.get("curated")]
    mappen.append(y["page_types"].get("onderwerp", {}).get("dir", "begrippen"))
    return {p.relative_to(wiki_root).as_posix() for m in mappen for p in (wiki_root / m).rglob("*.md")}


def verschillen(wiki_root: Path = WIKI_ROOT) -> tuple[dict[str, str], list[str], list[str]]:
    """(gegenereerd, te schrijven, te verwijderen)."""
    uit = render(wiki_root)
    schrijven = [p for p, inhoud in uit.items()
                 if not (wiki_root / p).exists() or (wiki_root / p).read_text(encoding="utf-8") != inhoud]
    verwijderen = sorted(beheerd(wiki_root) - set(uit))
    return uit, sorted(schrijven), verwijderen


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="Alleen controleren; fout als een pagina afwijkt")
    parser.add_argument("--voorbeeld", metavar="ID", help="Eén elementpagina naar het scherm")
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.voorbeeld:
        w = Wiki(args.wiki)
        if not w.pad(args.voorbeeld):
            print(f"'{args.voorbeeld}' heeft geen elementpagina (geen element, of nog niet afgeleid)")
            return 1
        sys.stdout.write(element_pagina(w, args.voorbeeld))
        return 0
    uit, schrijven, verwijderen = verschillen(args.wiki)
    if args.check:
        for p in schrijven:
            print(f"wijkt af van de beoordelingen: {p}")
        for p in verwijderen:
            print(f"hoort bij geen beoordeling: {p}")
        if schrijven or verwijderen:
            print("Draai 'uv run python tools/afleiden.py' en wijzig pagina's nooit met de hand.")
            return 1
        return 0
    for p in schrijven:
        doel = args.wiki / p
        doel.parent.mkdir(parents=True, exist_ok=True)
        doel.write_text(uit[p], encoding="utf-8", newline="\n")
    for p in verwijderen:
        (args.wiki / p).unlink()
    print(f"Gerenderd: {len(schrijven)} bestand(en) geschreven, {len(verwijderen)} verwijderd.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
