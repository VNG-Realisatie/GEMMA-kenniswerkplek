"""Render: alle leesbare pagina's van deze wiki uit de beoordelingen.

Invoer (alleen lezen): `beoordelingen/begrippen/<id>.yaml` (het oordeel van de AI, met `status` en `afgeleid` van
tools/afleiden.py), `beoordelingen/onderwerpen/<id>.yaml`, `beoordelingen/terugmeldingen/ggm.yaml`,
`beoordelingen/terugmeldingen/procesarchitectuur.yaml`, `beoordelingen/terugmeldingen/gemma.yaml`, `beoordelingen/beleidsdomeinen.yaml`, `beoordelingen/besluiten-eerder.yaml`, `log.md`, `wiki.yaml`,
de bronanalyses en `sources/index` (titels). Het script oordeelt niet en schrijft nooit in `beoordelingen/`.

Uitvoer (gegenereerd; nooit met de hand bewerken, de pre-commit-controle `--check` vangt dat):

| Bestand | Inhoud |
|---|---|
| `<map van het type>/<taakveld>/<beleidsdomein>/<id>.md` (pad uit `afgeleid.pad`) | Elementpagina |
| `begrippen/<onderwerp>.md` | Begrippenlijst: per begrip de uitkomst, de reden, de herkomst en de GGM-entiteit |
| `overzichten/<onderwerp>.md` | Overzicht per onderwerp: de views op de indelingen (processen naar kernobject en naar soort werk, ketensamenwerking, objecten, functies, doelgroepen, producten en diensten, beleidskaders) |
| `terugmeldingen/ggm-terugmeldingen.md` | Doorlopende lijst van GGM-terugmeldingen |
| `terugmeldingen/procesarchitectuur-terugmeldingen.md` | Doorlopende lijst van terugmeldingen aan de GEMMA-procesarchitectuur (UPL-lijsten, kennismodel) |
| `terugmeldingen/gemma-terugmeldingen.md` | Doorlopende lijst van terugmeldingen aan het GEMMA-team over het GEMMA-model |
| `besluiten/per-begrip.md` | Besluiten van de redacteur per begrip, per thuisonderwerp, en de eerdere besluiten uit `beoordelingen/besluiten-eerder.yaml` |
| `ter-beoordeling.md` | Wat wacht op akkoord (review), en wat nog moet worden voorgelegd |
| `voortgang.md` | Aantallen per onderwerp, type en status |
| `kennismodel/**` | Het kennismodel uit tools/kennismodel.py (behalve `kennismodel/modelleerregels.md`, met de hand) |

Opbouw van een elementpagina (vaste volgorde; een sectie zonder inhoud vervalt): frontmatter (gegevens en de
letterlijke `ggm_*`/`gemma_*`-velden), titel en status, Ter discussie; Betekenis (Definitie, Beschrijving, Deelprocessen, Per
onderwerp, Synoniemen, Naamkeuze, Homoniemen); Plaats in het model (Typering, Plaats in de indelingen, Kenmerken
alleen met ja, Generalisatie, Specialisaties, GGM-componenten, Tegenhanger, Relaties uitgaand en inkomend); Herkomst (Bronnen met korte titel,
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
import kennismodel  # noqa: E402
from llmwiki import beoordeling, frontmatter, logbook, paths  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
ONDERWERPEN = Path("beoordelingen") / "onderwerpen"
OVERZICHTEN = "overzichten"
TERUGMELDINGEN = Path("beoordelingen") / "terugmeldingen" / "ggm.yaml"
TER_BEOORDELING = Path("ter-beoordeling.md")
VOORTGANG = Path("voortgang.md")
TERUGMELDLIJST = Path("terugmeldingen") / "ggm-terugmeldingen.md"
PA_TERUGMELDINGEN = Path("beoordelingen") / "terugmeldingen" / "procesarchitectuur.yaml"
PA_TERUGMELDLIJST = Path("terugmeldingen") / "procesarchitectuur-terugmeldingen.md"
GEMMA_TERUGMELDINGEN = Path("beoordelingen") / "terugmeldingen" / "gemma.yaml"
GEMMA_TERUGMELDLIJST = Path("terugmeldingen") / "gemma-terugmeldingen.md"
BELEIDSDOMEINEN = Path("beoordelingen") / "beleidsdomeinen.yaml"
BESLUITEN_EERDER = Path("beoordelingen") / "besluiten-eerder.yaml"
BESLUITEN_PER_BEGRIP = Path("besluiten") / "per-begrip.md"
INDELINGSVELDEN = ("afnemer", "domein", "doelgroep", "regelgever")  # waarden zonder verwijzing: ook in de frontmatter

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
ARCHIMATE_NAAM = {t.archimate_type: t.naam for t in bepaal_type.TYPEN if not t.keuze}
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
        pa = wiki_root / PA_TERUGMELDINGEN
        self.pa_terugmeldingen = beoordeling.laad(pa).get("terugmeldingen", []) if pa.exists() else []
        gm = wiki_root / GEMMA_TERUGMELDINGEN
        self.gemma_terugmeldingen = beoordeling.laad(gm).get("terugmeldingen", []) if gm.exists() else []
        bd = wiki_root / BELEIDSDOMEINEN
        self.beleidsdomeinen = {b["beleidsdomein"]: b for b in beoordeling.laad(bd).get("beleidsdomeinen", [])} \
            if bd.exists() else {}
        be = wiki_root / BESLUITEN_EERDER
        self.besluiten_eerder = beoordeling.laad(be).get("besluiten", []) if be.exists() else []
        log = wiki_root / "log.md"
        self.log = log.read_text(encoding="utf-8") if log.exists() else ""
        self.onderwerp_dir = self.yaml["page_types"].get("onderwerp", {}).get("dir", "begrippen")
        self._titels: dict[str, str] = {}
        self._korte_titels: dict[str, str] = {}

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
        if bron_id not in self._korte_titels:
            doel = gam_gemeen.bron_doel(self.root, bron_id)
            binnen = doel is not None and doel.is_relative_to(self.root.resolve())
            self._korte_titels[bron_id] = (frontmatter.read(doel).meta.get("korte_titel") if binnen else None) or self.titel(bron_id)
        return self._korte_titels[bron_id]

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

    def uitkomst(self, bid: str) -> dict:
        return (self.begrippen.get(bid, {}).get("afgeleid") or {}).get("uitkomst") or {}

    def is_element(self, bid: str) -> bool:
        return bool(self.pad(bid)) and self.uitkomst(bid).get("soort") == "element" \
            and self.begrippen[bid].get("status") != "afgewezen"

    def paginatype(self, bid: str) -> str | None:
        return self.uitkomst(bid).get("paginatype") if self.is_element(bid) else None

    def niveau(self, bid: str) -> str | None:
        return self.uitkomst(bid).get("procesniveau") if self.is_element(bid) else None

    def uitgaand(self, bid: str, soort: str) -> list[str]:
        """De elementen waar `bid` een relatie van deze soort naartoe heeft."""
        return [r["naar"] for r in self.begrippen[bid].get("relaties", []) if r["soort"] == soort and self.is_element(r["naar"])]

    def inkomend_van(self, bid: str, soort: str) -> list[str]:
        return [v for v, r in self.inkomend(bid) if r["soort"] == soort and self.is_element(v)]

    def specialisaties_van(self, bid: str) -> list[str]:
        """Begrippen zonder pagina die een specialisatie zijn van dit begrip."""
        naam = self.naam(bid).lower()
        return [b for b, x in sorted(self.begrippen.items())
                if (x.get("afgeleid") or {}).get("uitkomst", {}).get("soort") == "specialisatie"
                and str((x["afgeleid"]["uitkomst"].get("genoemd_begrip") or "")).lower() in (naam, bid)]

    def gewijzigd_na_akkoord(self, bid: str) -> bool:
        return logbook.heeft_regel(self.log, "promote", bid)


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


def _links(w: Wiki, van: str, ids: list[str]) -> str:
    return ", ".join(w.link(van, i) for i in sorted(dict.fromkeys(ids), key=lambda i: w.naam(i).lower()))


def indelingen(w: Wiki, van: str, bid: str, d: dict) -> list[str]:
    """De plaats van het element in de indelingen: boven, onder, kernobject, GEMMA, bediening en gebeurtenissen."""
    u = d["afgeleid"]["uitkomst"]
    regels = []
    if u.get("procesniveau"):
        boven = [v for v in w.inkomend_van(bid, "aggregatie") if w.paginatype(v) == "bedrijfsproces"]
        onder = [n for n in w.uitgaand(bid, "aggregatie") if w.paginatype(n) == "bedrijfsproces"]
        regels.append(f"- **Procesniveau**: {u['procesniveau']}.")
        if boven:
            regels.append(f"- **Procesindeling naar kernobject, onderdeel van**: {_links(w, van, boven)}.")
        if onder:
            regels.append(f"- **Procesindeling naar kernobject, omvat**: {_links(w, van, onder)}.")
    if (u.get("procesniveau") == "levensloopproces" or u.get("paginatype") == "bedrijfsinteractie") \
            and d.get("beleidsdomein"):
        regels.append(f"- **Beleidsdomeinindeling**: beleidsdomein {d['beleidsdomein']}"
                      + (f", taakveld {d['taakveld']}" if d.get("taakveld") else "") + " (van het kernobject).")
    if d.get("kernobject"):
        regels.append(f"- **Kernobject**: {w.link(van, d['kernobject'])}.")
    if u.get("paginatype") == "bedrijfsinteractie":
        partijen = [v for v in w.inkomend_van(bid, "bediening") if w.paginatype(v) == "bedrijfsproces"]
        if partijen:
            regels.append(f"- **Ketensamenwerking, bediend door**: {_links(w, van, partijen)}.")
    if u.get("paginatype") == "bedrijfsproces":
        ketens = [n for n in w.uitgaand(bid, "bediening") if w.paginatype(n) == "bedrijfsinteractie"]
        if ketens:
            regels.append(f"- **Ketensamenwerking, bedient**: {_links(w, van, ketens)}.")
    if u.get("objectniveau"):
        regels.append(f"- **Objectniveau**: {u['objectniveau']}.")
    if u.get("objectniveau") == "kernobject":
        door = [b for b, x in w.begrippen.items() if x.get("kernobject") == bid and w.niveau(b) == "levensloopproces"]
        if door:
            regels.append(f"- **Levensloop bepaald door**: {_links(w, van, door)}.")
        ketens = [b for b, x in w.begrippen.items() if x.get("kernobject") == bid and w.paginatype(b) == "bedrijfsinteractie"
                  and w.is_element(b)]
        if ketens:
            regels.append(f"- **Ketensamenwerking**: {_links(w, van, ketens)}.")
    if u.get("objectniveau") == "subobject":
        van_object = [v for v in w.inkomend_van(bid, "compositie") if w.paginatype(v) == "bedrijfsobject"]
        if van_object:
            regels.append(f"- **Subobject van**: {_links(w, van, van_object)}.")
    if u.get("paginatype") == "bedrijfsobject":
        mutaties = [b for b, x in w.begrippen.items() if x.get("kernobject") == bid and w.niveau(b) == "bedrijfsproces"]
        if mutaties:
            regels.append(f"- **Mutaties door bedrijfsprocessen**: {_links(w, van, mutaties)}.")
    generiek = (d.get("afgeleid") or {}).get("gemma_generiek")
    if d.get("gemma_generiek"):
        naam = (generiek or {}).get("gemma_naam") or d["gemma_generiek"]["id"]
        regels.append(f"- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *{naam}*. "
                      f"{w.tekst(van, d['gemma_generiek']['onderbouwing'])}")
    bediend = w.inkomend_van(bid, "bediening")
    if bediend and u.get("paginatype") == "bedrijfsproces":
        regels.append(f"- **Functie-indeling naar domein, bediend door**: {_links(w, van, [b for b in bediend if w.paginatype(b) == 'bedrijfsfunctie'])}.")
    if u.get("paginatype") in ("bedrijfsfunctie", "product", "dienst"):
        boven = [v for v in w.inkomend_van(bid, "aggregatie") if w.paginatype(v) == "bedrijfsfunctie"]
        onder = [n for n in w.uitgaand(bid, "aggregatie") if w.paginatype(n) in ("bedrijfsfunctie", "product", "dienst")
                 and u.get("paginatype") == "bedrijfsfunctie"]
        if u.get("paginatype") == "product" and d.get("domein"):
            regels.append(f"- **Functie-indeling naar domein**: direct onder de domeingroepering {d['domein']} "
                          "(een functie aggregeert geen product).")
        if boven:
            regels.append(f"- **Functie-indeling naar domein, onderdeel van**: {_links(w, van, boven)}.")
        if onder:
            regels.append(f"- **Functie-indeling naar domein, omvat**: {_links(w, van, onder)}.")
    if u.get("paginatype") == "bedrijfsfunctie" and w.uitgaand(bid, "bediening"):
        regels.append(f"- **Bedient**: {_links(w, van, w.uitgaand(bid, 'bediening'))}.")
    start = [v for v in w.inkomend_van(bid, "triggering") if w.paginatype(v) == "gebeurtenis"]
    eind = [n for n in w.uitgaand(bid, "triggering") if w.paginatype(n) == "gebeurtenis"]
    if u.get("paginatype") == "gebeurtenis":
        start = []
        eind = w.uitgaand(bid, "triggering")
        if eind:
            regels.append(f"- **Start**: {_links(w, van, eind)}.")
    else:
        if start:
            regels.append(f"- **Gestart door gebeurtenis**: {_links(w, van, start)}.")
        if eind:
            regels.append(f"- **Eindigt in gebeurtenis**: {_links(w, van, eind)}.")
    waarden = [f"{k}: {d[k]}" for k in INDELINGSVELDEN if d.get(k)]
    regels += [f"- **{k.split(': ')[0].capitalize()}**: {k.split(': ', 1)[1]}." for k in waarden]
    if d.get("taakveld") or d.get("beleidsdomein"):
        regels.append("- **Beleidsdomeinindeling**: " + ", ".join(x for x in (d.get("taakveld"), d.get("beleidsdomein")) if x) + ".")
    return regels + [""] if regels else []


def specialisaties_per_onderwerp(w: Wiki, van: str, bid: str) -> list[str]:
    """Op een generiek object: de specialisaties zonder pagina, per onderwerp, met de processen die ze noemen (`via`)."""
    per_onderwerp: dict[str, list[str]] = {}
    for sid in w.specialisaties_van(bid):
        s = w.begrippen[sid]
        noemers = [v for v, r in w.inkomend(bid) if r.get("via") == sid and w.is_element(v)]
        regel = f"- **{s['begrip']}**: {w.tekst(van, s.get('definitie') or s.get('toelichting') or '')}"
        if noemers:
            regel += f" Genoemd door {_links(w, van, noemers)}."
        for oid in s.get("onderwerpen", []):
            per_onderwerp.setdefault(oid, []).append(regel)
    regels = []
    for oid, lijst in sorted(per_onderwerp.items()):
        regels += [f"#### {w.onderwerpen.get(oid, {}).get('naam', oid)}", "", *lijst, ""]
    return regels


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
        **({"objectniveau": u["objectniveau"]} if u.get("objectniveau") else {}),
        **({"generiek": True} if u.get("generiek") else {}),
        **{k: d[k] for k in INDELINGSVELDEN if d.get(k)},
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
    homoniemen = _tabel(["Begrip", "Betekenis", "Naamkeuze"], [
        [f"{w.link(van, h['element'], h['begrip']) if h.get('element') else h['begrip']} ({h['waar']})", h["betekenis"],
         h["naamkeuze"]] for h in d.get("homoniemen", [])]) if d.get("homoniemen") else []
    deelprocessen = [*[f"{i}. **{x['naam']}**: {w.tekst(van, x['omschrijving'])} "
                       f"{w.bronnen(van, x.get('bronnen', []), x.get('vindplaats'))}".rstrip()
                       for i, x in enumerate(d.get("deelprocessen", []), 1)], ""] if d.get("deelprocessen") else []
    r += _groep("Betekenis", [
        _sub("Definitie", definitie), _sub("Beschrijving", w.alineas(van, d.get("beschrijving"))),
        _sub("Deelprocessen", deelprocessen),
        _sub("Per onderwerp", per_onderwerp), _sub("Synoniemen", synoniemen),
        _sub("Naamkeuze", w.alineas(van, d.get("naamkeuze"))), _sub("Homoniemen", homoniemen)])

    # Plaats in het model: typering, kenmerken en samenhang met andere elementen.
    ja = [s for s in bepaal_type.SLEUTELS if d["kenmerken"][s]["waarde"] == "ja"]
    kenmerken = [[f"**{bepaal_type.NAAM[s]}**: {VRAAG[s]}",
                  " ".join(x for x in (w.tekst(van, _ja(d["kenmerken"][s]["onderbouwing"])),
                                       w.bronnen(van, d["kenmerken"][s].get("bronnen", []))) if x)] for s in ja]
    nee = len(bepaal_type.SLEUTELS) - len(ja)
    niveau = u.get("procesniveau") or u.get("objectniveau")
    typering = [f"{ARCHIMATE_NAAM.get(u['archimate_type'], u['archimate_type'])}"
                + (f", niveau {niveau}" if niveau else "") + f". Uitkomst van de beslistabel: {u['toelichting']}.", ""]
    specialisaties = [*[f"- **{w.link(van, s['element'], s['naam']) if s.get('element') else s['naam']}**: "
                        f"{w.tekst(van, s['omschrijving'])}"
                        + "".join(f" ({k} {s[k]})" for k in ("ggm_guid", "ggm_attribuut") if s.get(k))
                        for s in d.get("specialisaties", [])], ""] if d.get("specialisaties") else []
    componenten = _tabel(["Component", "GGM-guid", "Toelichting"], [
        [c["naam"], c["guid"], c["toelichting"]] for c in d.get("ggm_componenten", [])]) if d.get("ggm_componenten") else []
    tegenhanger = ([f"{w.link(van, d['tegenhanger']['element'])}: {w.tekst(van, d['tegenhanger']['toelichting'])}", ""]
                   if d.get("tegenhanger") else [])

    def buiten_kennismodel(van_id: str, x: dict) -> bool:
        bron, doel = (kennismodel.sleutel_van(w.uitkomst(b)["archimate_type"]) for b in (van_id, x["naar"]))
        return not kennismodel.toegestaan(bron, x["soort"], doel)

    def relatie(x: dict, van_id: str = bid) -> str:
        soort = ", ".join(v for v in (x["soort"], x.get("kardinaliteit", "")) if v)
        tekst = f"{x['naam']} *{soort}*" if x.get("naam") else soort
        return f"{tekst} (*niet in het kennismodel, gaat niet mee in de export*)" if buiten_kennismodel(van_id, x) else tekst

    def bron_cel(x: dict) -> str:
        cel = w.bronnen(van, x.get("bronnen", []), x.get("vindplaats"))
        ggm_relatie = ", ".join(x.get("ggm_relatie", []))
        return f"{cel}; GGM ({ggm_relatie})" if cel and ggm_relatie else (cel or (f"GGM ({ggm_relatie})" if ggm_relatie else ""))

    kolommen = ["Van", "Relatie", "Naar", "Bron"]
    uitgaand = _tabel(kolommen, [[d["begrip"], relatie(x), w.link(van, x["naar"]), bron_cel(x)]
                                 for x in d.get("relaties", [])]) if d.get("relaties") else []
    inkomend = [[w.link(van, v), relatie(x, v), d["begrip"], bron_cel(x)] for v, x in w.inkomend(bid)]
    relaties = _sub("Uitgaand", uitgaand, 4) + _sub("Inkomend", _tabel(kolommen, inkomend) if inkomend else [], 4)
    specialisaties_zonder_pagina = specialisaties_per_onderwerp(w, van, bid) if u.get("objectniveau") == "generiek" else []
    r += _groep("Plaats in het model", [
        _sub("Typering", typering), _sub("Plaats in de indelingen", indelingen(w, van, bid, d)),
        _sub("Specialisaties per onderwerp", specialisaties_zonder_pagina),
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
            ggm_regels += ["Duplicaten in het GGM:", "", *_tabel(["Entiteit", "Toelichting"], [
                [f"{x.get('entiteit')} ({x.get('beleidsdomein')})",
                 next((y["toelichting"] for y in g.get("duplicaten", []) if y["guid"] == x["guid"]), "")]
                for x in a["ggm_duplicaten"]])]
    meldingen = [m for m in w.terugmeldingen if m.get("element") == bid]
    if meldingen:
        lijst = w.rel(van, TERUGMELDLIJST)
        ggm_regels += ["GGM-terugmeldingen:", "", *[f"- [Nummer {m['nummer']}]({lijst}) ({m['type']}, {m.get('status', 'open')}): "
                                                   f"{_bevinding_regel(w, van, m['bevinding'])}" for m in meldingen], ""]
    g = d["gemma"]
    if gemma:
        gemma_regels = [f"Match **{g['sterkte']}** met GEMMA-element *{gemma['gemma_naam']}* ({gemma.get('gemma_type', '')}). "
                        f"{w.tekst(van, g['onderbouwing'])}", ""]
        if gemma.get("gemma_definitie"):
            gemma_regels += [f"> {_cel(gemma['gemma_definitie'])}", ""]
    else:
        gemma_regels = [f"Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. {w.tekst(van, g['onderbouwing'])}", ""]
    pa = [m for m in w.pa_terugmeldingen if bid in (m.get("elementen") or [])]
    if pa:
        lijst = w.rel(van, PA_TERUGMELDLIJST)
        gemma_regels += ["Procesarchitectuur-terugmeldingen:", "", *[
            f"- [Nummer {m['nummer']}]({lijst}) ({m['type']}, {m.get('status', 'open')}): "
            f"{_bevinding_regel(w, van, m['bevinding'])}"
            for m in pa], ""]
    gm = [m for m in w.gemma_terugmeldingen if bid in (m.get("elementen") or [])]
    if gm:
        lijst = w.rel(van, GEMMA_TERUGMELDLIJST)
        gemma_regels += ["GEMMA-terugmeldingen:", "", *[
            f"- [Nummer {m['nummer']}]({lijst}) ({m['type']}, {m.get('status', 'open')}): "
            f"{_bevinding_regel(w, van, m['bevinding'])}"
            for m in gm], ""]
    besluiten = [f"- {b['datum']}: {w.tekst(van, b['besluit'])}" for b in d.get("besluiten", [])]
    r += _groep("Herkomst", [_sub("Bronnen", bronnen), _sub("Afstemming met GGM", ggm_regels),
                             _sub("Afstemming met GEMMA", gemma_regels), _sub("Besluiten redacteur", besluiten)])
    return _pagina(meta, r)


# --- Begrippenlijst per onderwerp ---


def _begrip_cel(w: Wiki, van: str, bid: str, d: dict) -> str:
    u = d["afgeleid"]["uitkomst"]
    if u["soort"] == "element":
        if d.get("status") == "afgewezen":
            return f"{d['begrip']} *{ARCHIMATE_NAAM.get(u['archimate_type'], u['archimate_type'])}, afgewezen door de redacteur*"
        return f"{w.link(van, bid)} *{ARCHIMATE_NAAM.get(u['archimate_type'], u['archimate_type'])}, {d['status']}*"
    tekst = f"{d['begrip']} *{UITKOMST.get(u['soort'], u['soort'])}*"
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
    r += _sectie("Overzicht", [f"De views op de indelingen staan in het [overzicht]({w.rel(van, f'{OVERZICHTEN}/{oid}.md')}).", ""])
    r += _sectie("Bronnen", [f"- {w.bron(van, b, w.titel(b))}" for b in o.get("bronnen", [])] + [""])
    rijen = []
    for bid, d in sorted(w.begrippen.items(), key=lambda x: x[1]["begrip"].lower()):
        if oid not in d.get("onderwerpen", []) or "afgeleid" not in d:
            continue
        a = d["afgeleid"]
        reden = d.get("toelichting") or a["uitkomst"]["toelichting"]
        t = gam_gemeen.thuis(d)
        if t != oid:
            reden = f"Uit onderwerp [{w.onderwerpen.get(t, {}).get('naam', t)}]({w.rel(van, f'{w.onderwerp_dir}/{t}.md')}). " + reden
        if a.get("open"):
            reden += " Voorleggen: " + "; ".join(a["open"]) + "."
        ggm = (a.get("ggm") or {}).get("ggm_entiteit")
        herkomst = "; ".join(x for x in (a.get("herkomst", ""), f"GGM: {ggm}" if ggm else "") if x)
        rijen.append([_begrip_cel(w, van, bid, d), w.tekst(van, reden), herkomst or "—"])
    r += _sectie("Begrippen", ["Een begrip met een link is een element; cursief staat de uitkomst.", "",
                               *_tabel(["Begrip", "Reden", "Herkomst"], rijen)] if rijen else ["Nog geen begrippen beoordeeld.", ""])
    r += _sectie("Open vragen", [f"- {w.tekst(van, v)}" for v in o.get("open_vragen", [])] + [""] if o.get("open_vragen") else [])
    return _pagina(meta, r)


# --- Overzicht per onderwerp: de views op de indelingen ---


def _proces_regel(w: Wiki, van: str, bid: str, niveau: int) -> list[str]:
    """Een proces in de procesindeling naar kernobject, met kernobject, aanbod, functies en gebeurtenissen."""
    d = w.begrippen[bid]
    details = []
    if d.get("kernobject") and w.is_element(d["kernobject"]):
        details.append(f"kernobject {w.link(van, d['kernobject'])}")
    aanbod = [x for x in w.uitgaand(bid, "realisatie") if w.paginatype(x) in ("dienst", "product")]
    if aanbod:
        details.append(f"levert {_links(w, van, aanbod)}")
    functies = [f for f in w.inkomend_van(bid, "bediening") if w.paginatype(f) == "bedrijfsfunctie"]
    if functies:
        details.append(f"bediend door {_links(w, van, functies)}")
    start = [g for g in w.inkomend_van(bid, "triggering") if w.paginatype(g) == "gebeurtenis"]
    if start:
        details.append(f"gestart door {_links(w, van, start)}")
    eind = [g for g in w.uitgaand(bid, "triggering") if w.paginatype(g) == "gebeurtenis"]
    if eind:
        details.append(f"eindigt in {_links(w, van, eind)}")
    kenmerken = ", ".join(x for x in (w.niveau(bid) or "niveau nog niet vastgesteld",
                                      f"afnemer {d['afnemer']}" if d.get("afnemer") else "") if x)
    regel = f"{'  ' * niveau}- {w.link(van, bid)} *({kenmerken})*" + (f": {'; '.join(details)}" if details else "")
    uit = [regel]
    for kind in sorted(w.uitgaand(bid, "aggregatie"), key=lambda k: w.naam(k).lower()):
        if w.paginatype(kind) == "bedrijfsproces" and w.niveau(kind) != "cluster naar soort werk" and niveau < 6:
            uit += _proces_regel(w, van, kind, niveau + 1)
    return uit


def overzicht(w: Wiki, oid: str) -> str:
    o = w.onderwerpen[oid]
    van = f"{OVERZICHTEN}/{oid}.md"
    meta = {"id": oid, "type": "overzicht", "naam": o["naam"]}
    eigen = sorted((b for b, d in w.begrippen.items() if oid in d.get("onderwerpen", []) and w.is_element(b)),
                   key=lambda b: w.naam(b).lower())
    van_type = lambda t: [b for b in eigen if w.paginatype(b) == t]  # noqa: E731
    r = [f"# Overzicht {o['naam']}", "", _gegenereerd("de beoordelingen van de elementen van dit onderwerp"), "",
         f"De views op de indelingen voor het onderwerp [{o['naam']}](../{w.onderwerp_dir}/{oid}.md). Per element de pagina met de details.", ""]

    processen = van_type("bedrijfsproces")
    clusters = {b for b in processen if w.niveau(b) == "cluster naar soort werk"}
    ouders = {n for b in processen if b not in clusters for n in w.uitgaand(b, "aggregatie")
              if w.paginatype(n) == "bedrijfsproces"}
    wortels = [b for b in processen if b not in ouders and b not in clusters]
    per_domein: dict[tuple[str, str], list[str]] = {}
    for b in wortels:
        d = w.begrippen[b]
        per_domein.setdefault((d.get("taakveld") or "—", d.get("beleidsdomein") or "—"), []).append(b)
    boom = []
    for (taakveld, beleidsdomein), bids in sorted(per_domein.items()):
        bd = w.beleidsdomeinen.get(beleidsdomein)
        tekst = f": {' '.join(w.tekst(van, a) for a in bd['beschrijving'])} Bronnen: {w.bronnen(van, bd['bronnen'])}." \
            if bd else ""
        boom.append(f"- **{beleidsdomein}** *(beleidsdomein, taakveld {taakveld})*{tekst}")
        for b in bids:
            boom += _proces_regel(w, van, b, 1)
    r += _sectie("Procesindeling naar kernobject", [
        "Beleidsdomein (Beleidsdomeinindeling) → levensloopproces per kernobject → bedrijfsproces. Tussen haakjes het "
        "procesniveau.", "", *boom]
        if boom else [])

    keten_regels = []
    for b in van_type("bedrijfsinteractie"):
        d = w.begrippen[b]
        partijen = [v for v in w.inkomend_van(b, "bediening") if w.paginatype(v) == "bedrijfsproces"]
        rollen = [v for v in w.inkomend_van(b, "toewijzing") if w.paginatype(v) in ("rol", "actor", "bedrijfssamenwerking")]
        keten_regels.append(f"- {w.link(van, b)}: kernobject "
                            f"{w.link(van, d['kernobject']) if d.get('kernobject') and w.is_element(d['kernobject']) else '—'}; "
                            f"bediend door {_links(w, van, partijen) or '—'}; uitgevoerd door {_links(w, van, rollen) or '—'}.")
    r += _sectie("Ketensamenwerking", ["Bedrijfsinteracties waarin de bedrijfsprocessen van de partijen samenkomen; het "
                                       "ketenproces erboven is geen element.", "", *keten_regels]
                 if keten_regels else [])

    soort_werk = []
    for b in processen:
        if w.begrippen[b].get("gemma_generiek"):
            generiek = (w.begrippen[b]["afgeleid"].get("gemma_generiek") or {}).get("gemma_naam") or w.begrippen[b]["gemma_generiek"]["id"]
            onder = [n for n in w.uitgaand(b, "aggregatie") if w.paginatype(n) == "bedrijfsproces"]
            soort_werk.append([w.link(van, b), w.niveau(b), generiek, _links(w, van, onder) or "—"])
    r += _sectie("Procesindeling naar soort werk", _tabel(
        ["Proces", "Niveau", "Specialisatie van GEMMA-element", "Bedrijfsprocessen"], soort_werk) if soort_werk else [])

    gebeurtenissen = [[w.link(van, g), _links(w, van, [b for b in processen if g in w.uitgaand(b, "triggering")]) or "—",
                       _links(w, van, w.uitgaand(g, "triggering")) or "—"] for g in van_type("gebeurtenis")]
    r += _sectie("Gebeurtenissen", _tabel(["Gebeurtenis", "Eindpunt van", "Start"], gebeurtenissen) if gebeurtenissen else [])

    objecten = van_type("bedrijfsobject")
    kern = [b for b in objecten if w.uitkomst(b).get("objectniveau") == "kernobject"]
    regels = []
    for b in kern:
        sub = [x for x in objecten if w.uitkomst(x).get("objectniveau") == "subobject" and b in w.inkomend_van(x, "compositie")]
        door = [x for x in processen if w.begrippen[x].get("kernobject") == b and w.niveau(x) == "levensloopproces"]
        regels.append(f"- {w.link(van, b)}: levensloop door {_links(w, van, door) or '—'}"
                      + (f"; subobjecten {_links(w, van, sub)}" if sub else "") + ".")
    generiek = [b for b in objecten if w.uitkomst(b).get("objectniveau") == "generiek"]
    overig = [b for b in objecten if b not in kern and b not in generiek and w.uitkomst(b).get("objectniveau") != "subobject"]
    r += _sectie("Objecten", [*(["**Kernobjecten**", "", *regels, ""] if regels else []),
                              *([f"**Generiek** (verhuizen later naar een algemeen onderwerp): {_links(w, van, generiek)}.", ""] if generiek else []),
                              *([f"**Nog zonder niveau**: {_links(w, van, overig)}.", ""] if overig else [])])

    functies = [[w.link(van, f), _links(w, van, [v for v in w.inkomend_van(f, "aggregatie")
                                                 if w.paginatype(v) == "bedrijfsfunctie"]) or w.begrippen[f].get("domein") or "—",
                 _links(w, van, w.uitgaand(f, "bediening")) or "—"] for f in van_type("bedrijfsfunctie")]
    r += _sectie("Functies", _tabel(["Functie", "Onderdeel van", "Bedient"], functies) if functies else [])

    doelgroepen = []
    for doelgroep in bepaal_type.DOELGROEPEN:
        leden = [b for b in eigen if w.begrippen[b].get("doelgroep") == doelgroep]
        if leden:
            per_type = [f"{t}: {_links(w, van, [b for b in leden if w.paginatype(b) == t])}"
                        for t in ("actor", "rol", "bedrijfssamenwerking", "kanaal") if any(w.paginatype(b) == t for b in leden)]
            doelgroepen.append(f"- **{doelgroep}**: " + "; ".join(per_type) + ".")
    r += _sectie("Doelgroepen", doelgroepen + [""] if doelgroepen else [])

    aanbod = [b for b in eigen if w.paginatype(b) in ("product", "dienst")]
    rijen = [[w.link(van, b), w.paginatype(b), w.begrippen[b].get("domein", "—"),
              _links(w, van, [x for x in w.inkomend_van(b, "aggregatie") if w.paginatype(x) == "bedrijfsfunctie"]) or "—",
              w.begrippen[b].get("afnemer", "—"),
              _links(w, van, [x for x in w.inkomend_van(b, "realisatie") if w.paginatype(x) == "bedrijfsproces"]) or "—"] for b in aanbod]
    r += _sectie("Producten en diensten", _tabel(["Element", "Type", "Domein", "Functie", "Afnemer", "Geleverd door"], rijen) if rijen else [])

    kaders = [[w.link(van, b), w.begrippen[b].get("regelgever", "—"),
               _links(w, van, w.uitgaand(b, "associatie (gericht)") + w.uitgaand(b, "associatie")) or "—"] for b in van_type("beleidskader")]
    r += _sectie("Beleidskaders", _tabel(["Beleidskader", "Regelgever", "Grondslag voor"], kaders) if kaders else [])
    return _pagina(meta, r)


# --- Overzichten ---


TERUGMELDTYPEN = {
    "hiaat": "Concept ontbreekt in het GGM",
    "definitie": "Entiteit bestaat, maar de definitie is onjuist, onvolledig of geen begripsdefinitie",
    "structuur": "Onhandige modellering (overerving, ontbrekende relatie, granulariteit)",
    "scope": "Entiteit hoort niet in dit beleidsdomein of ontbreekt in een ander",
    "duplicaat": "Zelfde concept met meerdere GUID's in verschillende beleidsdomeinen → samenvoegen",
    "homoniem": "Zelfde naam voor een ander concept in een ander beleidsdomein → hernoemen",
    "relatie": "Fout in een exact gematchte relatie (type, richting, kardinaliteit, naam, dubbel)",
}


def _terugmeld_element(w: Wiki, van: str, m: dict) -> str:
    """Het element (link; platte tekst zonder pagina) met tussen haakjes waar het in het GGM staat."""
    entiteit = m.get("entiteit")
    naam = w.naam(m["element"]) if m.get("element") else entiteit or "—"
    element = w.link(van, m["element"]) if m.get("element") else naam
    if not entiteit:
        ggm = f"ontbreekt, past in {m['domein']}"
    elif entiteit == naam:
        ggm = m["domein"]
    else:
        ggm = f"{entiteit}, {m['domein']}"
    return f"{element} (GGM: {ggm})"


def terugmeldlijst(w: Wiki) -> str:
    van = TERUGMELDLIJST.as_posix()
    meta = {"id": "ggm-terugmeldingen", "type": "lijst", "titel": "GGM-terugmeldingen"}
    r = ["# GGM-terugmeldingen", "", _gegenereerd(TERUGMELDINGEN.as_posix()), "",
         "Bevindingen uit de beoordeling van elementen die aan het GGM-beheer worden teruggekoppeld.", ""]
    per_type = []
    for soort, betekenis in TERUGMELDTYPEN.items():
        rijen = [[f"{m['nummer']} {m.get('status', 'open')}", _terugmeld_element(w, van, m), _bevinding_cel(w, van, m["bevinding"])]
                 for m in sorted(w.terugmeldingen, key=lambda m: m["nummer"]) if m["type"] == soort]
        per_type += _sub(soort.capitalize(), [f"{betekenis}.", "", *_tabel(["#", "Element", "Bevinding"], rijen)]) if rijen else []
    r += _sectie("Terugmeldingen", per_type)
    r += _sectie("Status", ["open → gemeld → opgelost of afgewezen (met reden).", ""])
    return _pagina(meta, r)


PA_TYPEN = {
    "indeling": "GEMMA komt tot een andere indeling dan de UPL (taakveld, GEMMA-domein), of een beleidsdomein valt "
                "anders in de GEMMA-domeinen",
    "grondslag": "De grondslag in de UPL is onjuist, te smal of verwijst naar het verkeerde artikel",
    "product": "Een product ontbreekt in de UPL, of hoort samengevoegd of gesplitst",
    "kennismodel": "Het model wijkt af van het kennismodel procesarchitectuur",
}


def _als_lijst(bevinding: str | list[str]) -> list[str]:
    return [bevinding] if isinstance(bevinding, str) else list(bevinding)


def _bevinding_regel(w: Wiki, van: str, bevinding: str | list[str]) -> str:
    """Een bevinding op één regel (elementpagina): de alinea's en lijstitems achter elkaar."""
    return w.tekst(van, " ".join(a.removeprefix("- ") for a in _als_lijst(bevinding)))


def _bevinding_cel(w: Wiki, van: str, bevinding: str | list[str]) -> str:
    """Een bevinding in één tabelcel: alinea's gescheiden door een witregel (<br><br>), een alinea die met '- ' begint
    als lijstitem (• ) op een eigen regel. De bron blijft één regel per tabelrij (regel Schrijfwijze)."""
    cel = ""
    vorige_lijst = False
    for a in _als_lijst(bevinding):
        lijst = a.startswith("- ")
        tekst = ("• " + w.tekst(van, a[2:])) if lijst else w.tekst(van, a)
        if cel:
            cel += "<br>" if lijst and vorige_lijst else "<br><br>" if not lijst else "<br>"
        cel += tekst
        vorige_lijst = lijst
    return cel


def pa_terugmeldlijst(w: Wiki) -> str:
    van = PA_TERUGMELDLIJST.as_posix()
    meta = {"id": "procesarchitectuur-terugmeldingen", "type": "lijst", "titel": "Procesarchitectuur-terugmeldingen"}
    r = ["# Procesarchitectuur-terugmeldingen", "", _gegenereerd(PA_TERUGMELDINGEN.as_posix()), "",
         "Bevindingen voor de werkgroep procesarchitectuur: waar GEMMA tot een andere indeling of modellering komt dan de "
         "UPL-lijsten (producten en diensten, extern en intern) en het kennismodel procesarchitectuur. Het model mag "
         "afwijken van de UPL-indeling, mits de afwijking hier is teruggemeld (besluit redacteur 2026-10-05); een "
         "terugmelding dekt dan het signaal van tools/afleiden.py.", ""]
    per_type = []
    for soort, betekenis in PA_TYPEN.items():
        rijen = [[f"{m['nummer']} {m.get('status', 'open')}",
                  ", ".join([w.link(van, e) for e in m.get("elementen") or []]
                            + ([f"beleidsdomein {m['beleidsdomein']}"] if m.get("beleidsdomein") else [])),
                  _bevinding_cel(w, van, m["bevinding"])]
                 for m in sorted(w.pa_terugmeldingen, key=lambda m: m["nummer"]) if m["type"] == soort]
        per_type += _sub(soort.capitalize(), [f"{betekenis}.", "", *_tabel(["#", "Betreft", "Bevinding"], rijen)]) if rijen else []
    r += _sectie("Terugmeldingen", per_type or ["Nog geen terugmeldingen.", ""])
    r += _sectie("Status", ["open → gemeld → opgelost of afgewezen (met reden).", ""])
    return _pagina(meta, r)


GEMMA_TYPEN = {
    "element": "Een GEMMA-element ontbreekt, hoort te vervallen of moet worden herzien",
    "indeling": "GEMMA deelt een element anders in (functie, domein, beleidsdomein, map)",
    "definitie": "De naam of definitie van een GEMMA-element wijkt af of ontbreekt",
    "relatie": "Een relatie in GEMMA ontbreekt, is onjuist of overbodig",
}


def gemma_terugmeldlijst(w: Wiki) -> str:
    van = GEMMA_TERUGMELDLIJST.as_posix()
    meta = {"id": "gemma-terugmeldingen", "type": "lijst", "titel": "GEMMA-terugmeldingen"}
    r = ["# GEMMA-terugmeldingen", "", _gegenereerd(GEMMA_TERUGMELDINGEN.as_posix()), "",
         "Voorstellen voor het GEMMA-team over het GEMMA-model zelf: elementen die ontbreken, vervallen of herzien moeten "
         "worden, en afwijkende indelingen, definities en relaties. De export naar Archi werkt alleen elementen bij die "
         "de wiki kent; wat de wiki laat vervallen, blijft in GEMMA tot het GEMMA-team erover besluit (besluit redacteur "
         "2026-10-08).", ""]
    per_type = []
    for soort, betekenis in GEMMA_TYPEN.items():
        rijen = [[f"{m['nummer']} {m.get('status', 'open')}",
                  ", ".join([w.link(van, e) for e in m.get("elementen") or []]
                            + [f"{g['naam']} (GEMMA)" for g in m.get("gemma_elementen") or []]),
                  _bevinding_cel(w, van, m["bevinding"])]
                 for m in sorted(w.gemma_terugmeldingen, key=lambda m: m["nummer"]) if m["type"] == soort]
        per_type += _sub(soort.capitalize(), [f"{betekenis}.", "", *_tabel(["#", "Betreft", "Bevinding"], rijen)]) if rijen else []
    r += _sectie("Terugmeldingen", per_type or ["Nog geen terugmeldingen.", ""])
    r += _sectie("Status", ["open → gemeld → opgelost of afgewezen (met reden).", ""])
    return _pagina(meta, r)


def ter_beoordeling(w: Wiki) -> str:
    van = TER_BEOORDELING.as_posix()
    meta = {"id": "ter-beoordeling", "type": "lijst", "titel": "Ter beoordeling"}
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


def besluiten_per_begrip(w: Wiki) -> str:
    """Alle besluiten van de redacteur uit de beoordelingen, per thuisonderwerp, en de eerdere besluiten zonder
    overeenkomend besluit in een beoordeling (`beoordelingen/besluiten-eerder.yaml`)."""
    van = BESLUITEN_PER_BEGRIP.as_posix()
    meta = {"id": "per-begrip", "type": "lijst", "titel": "Besluiten per begrip"}
    r = ["# Besluiten per begrip", "", _gegenereerd("de beoordelingen en beoordelingen/besluiten-eerder.yaml"), "",
         "Wat de redacteur over afzonderlijke begrippen besliste. De AI leest deze lijst bij het beoordelen en legt een "
         "besluit dat hier staat niet opnieuw voor; een besluit dat niet meer past bij de criteria wel, met de reden. "
         "Een besluit over één begrip staat in zijn beoordeling (`besluiten:`); besluiten over de werkwijze staan in "
         "[Besluiten over de werkwijze](werkwijze.md).", ""]
    for oid, o in w.onderwerpen.items():
        rijen = []
        for bid, d in w.begrippen.items():
            if gam_gemeen.thuis(d) != oid:
                continue
            a = (d.get("afgeleid") or {}).get("uitkomst", {})
            if w.pad(bid):
                soort = ARCHIMATE_NAAM.get(a.get("archimate_type"), "")
            elif d.get("status") == "afgewezen":
                soort = f"{ARCHIMATE_NAAM.get(a.get('archimate_type'), 'element')}, afgewezen"
            else:
                soort = UITKOMST.get(a.get("soort"), a.get("soort", ""))
            for b in d.get("besluiten") or []:
                rijen.append((str(b.get("datum")), d["begrip"].lower(),
                              [str(b.get("datum")), w.link(van, bid), soort, w.tekst(van, b.get("besluit", "")), b.get("gevolg", "")]))
        rijen.sort(key=lambda x: (x[0], x[1]))
        r += _sectie(o.get("naam", oid), _tabel(["Datum", "Begrip", "Uitkomst", "Besluit", "Gevolg"], [x[2] for x in rijen])
                     if rijen else ["Nog geen besluiten.", ""])
    eerder = [[str(b["datum"]), b["begrip"], w.onderwerpen.get(b["onderwerp"], {}).get("naam", b["onderwerp"]),
               w.tekst(van, b["besluit"]), b.get("stand", "")] for b in w.besluiten_eerder]
    r += _sectie("Eerder", ["Besluiten van vóór de besluiten in de beoordelingen, of over meer begrippen tegelijk, die "
                            "niet ook in een beoordeling staan. De kolom Stand zegt of het besluit nog geldt.", "",
                            *_tabel(["Datum", "Begrip", "Onderwerp", "Besluit", "Stand"], eerder)] if eerder else [])
    return _pagina(meta, r)


def _samenhang(w: Wiki) -> list[str]:
    """Per onderwerp de elementen die er thuishoren, die het uit andere onderwerpen gebruikt, en de relaties binnen het
    onderwerp en met andere onderwerpen (regels Thuishoren en Relaties tussen onderwerpen)."""
    elementen = {b for b, d in w.begrippen.items() if d.get("status") and d["status"] != "afgewezen"}
    per = gam_gemeen.relaties_per_onderwerp(w.begrippen, elementen)
    rijen = []
    for oid, o in w.onderwerpen.items():
        eigen = [b for b in elementen if gam_gemeen.thuis(w.begrippen[b]) == oid]
        gebruikt = [b for b in elementen if oid in w.begrippen[b]["onderwerpen"][1:]]
        binnen = sum(per[b].get(oid, 0) for b in eigen) // 2
        andere: dict[str, int] = {}
        for b in eigen:
            for ander, n in per[b].items():
                if ander != oid:
                    andere[ander] = andere.get(ander, 0) + n
        rijen.append([o["naam"], len(eigen), len(gebruikt), binnen,
                      ", ".join(f"{w.onderwerpen.get(a, {}).get('naam', a)} {n}" for a, n in sorted(andere.items())) or "—"])
    return ["Het thuisonderwerp is het eerste onderwerp van een element. Relaties tellen tussen elementen, in beide "
            "richtingen; weinig relaties met andere onderwerpen is een goede grens.", "",
            *_tabel(["Onderwerp", "Elementen", "Gebruikt uit andere", "Relaties binnen", "Relaties met andere"], rijen)]


def voortgang(w: Wiki) -> str:
    meta = {"id": "voortgang", "type": "lijst", "titel": "Voortgang"}
    r = ["# Voortgang", "", _gegenereerd("de beoordelingen"), ""]
    rijen = []
    for oid, o in w.onderwerpen.items():
        eigen = [d for d in w.begrippen.values() if oid in d.get("onderwerpen", [])]
        rijen.append([f"[{o['naam']}]({w.onderwerp_dir}/{oid}.md)", o.get("status", "in-behandeling"), len(eigen),
                      sum(1 for d in eigen if d.get("status"))])
    r += _sectie("Onderwerpen", _tabel(["Onderwerp", "Status", "Begrippen", "Elementen"], rijen))
    r += _sectie("Samenhang tussen onderwerpen", _samenhang(w))
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
    pa_status: dict[str, int] = {}
    for m in w.pa_terugmeldingen:
        pa_status[m.get("status", "open")] = pa_status.get(m.get("status", "open"), 0) + 1
    if w.pa_terugmeldingen:
        r += _sectie("Procesarchitectuur-terugmeldingen", [
            f"[{len(w.pa_terugmeldingen)} terugmeldingen]({PA_TERUGMELDLIJST.as_posix()}): "
            + ", ".join(f"{k} {v}" for k, v in sorted(pa_status.items())) + ".", ""])
    gm_status: dict[str, int] = {}
    for m in w.gemma_terugmeldingen:
        gm_status[m.get("status", "open")] = gm_status.get(m.get("status", "open"), 0) + 1
    if w.gemma_terugmeldingen:
        r += _sectie("GEMMA-terugmeldingen", [
            f"[{len(w.gemma_terugmeldingen)} terugmeldingen]({GEMMA_TERUGMELDLIJST.as_posix()}): "
            + ", ".join(f"{k} {v}" for k, v in sorted(gm_status.items())) + ".", ""])
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
        uit[f"{OVERZICHTEN}/{oid}.md"] = overzicht(w, oid)
    uit[TERUGMELDLIJST.as_posix()] = terugmeldlijst(w)
    uit[PA_TERUGMELDLIJST.as_posix()] = pa_terugmeldlijst(w)
    if w.gemma_terugmeldingen:
        uit[GEMMA_TERUGMELDLIJST.as_posix()] = gemma_terugmeldlijst(w)
    uit[BESLUITEN_PER_BEGRIP.as_posix()] = besluiten_per_begrip(w)
    uit[TER_BEOORDELING.as_posix()] = ter_beoordeling(w)
    uit[VOORTGANG.as_posix()] = voortgang(w)
    uit.update(kennismodel.paginas())
    return uit


def beheerd(wiki_root: Path) -> set[str]:
    """Bestaande bestanden die de render beheert: alle pagina's in de mappen van de elementtypen en de begrippenlijsten."""
    y = paths.load_wiki_yaml(wiki_root)
    mappen = [d["dir"] for d in y["page_types"].values() if d.get("curated")]
    mappen.append(y["page_types"].get("onderwerp", {}).get("dir", "begrippen"))
    mappen += [OVERZICHTEN, kennismodel.MAP]
    handmatig = {f"{kennismodel.MAP}/{n}" for n in kennismodel.HANDMATIG}
    return {p.relative_to(wiki_root).as_posix() for m in mappen for p in (wiki_root / m).rglob("*.md")} - handmatig


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
