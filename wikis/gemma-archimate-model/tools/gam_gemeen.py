"""Gedeelde hulpfuncties voor de tools van gemma-archimate-model.

- gegenereerde bestanden schrijven met een hash-kop, en controleren dat niemand ze met de hand wijzigde;
- secties, tabellen en links in Markdown lezen (bronduidingen);
- bronverwijzingen: pagina → bronduiding → laag 1 (sources/raw/ of sources/modellen/);
- modelbestanden ophalen van GitHub;
- onderwerpen als één model: thuisonderwerp en relaties tussen onderwerpen (regels Thuishoren, Relaties tussen
  onderwerpen).
"""
from __future__ import annotations

import copy
import functools
import json
import re
from pathlib import Path

from llmwiki import hashing, paths

WIKI_ROOT = Path(__file__).resolve().parent.parent
# Plattegrond (ARCHITECTURE.md, 6.1): per onderwerp alles bij elkaar, per model zijn bronduidingen, indelingen en terugmeldingen
ONDERWERPEN = Path("onderwerpen")
GGM_TERUGMELDINGEN = Path("modellen/ggm/terugmeldingen.yaml")
GGM_TERUGMELDLIJST = Path("modellen/ggm/terugmeldingen.md")
PA_TERUGMELDINGEN = Path("modellen/gemma/terugmeldingen/procesarchitectuur.yaml")
PA_TERUGMELDLIJST = Path("modellen/gemma/terugmeldingen/procesarchitectuur.md")
GEMMA_TERUGMELDINGEN = Path("modellen/gemma/terugmeldingen/gemma-team.yaml")
GEMMA_TERUGMELDLIJST = Path("modellen/gemma/terugmeldingen/gemma-team.md")
BELEIDSDOMEINEN = Path("modellen/gemma/indelingen/beleidsdomeinen.yaml")
GEGENEREERD_PREFIX = "<!-- gegenereerd door "
NIVEAUS = ("eigen", "thematisch", "kern")  # `niveau` van een onderwerp in de onderwerpen-indeling (regel Thuishoren)
GEDEELD = ("thematisch", "kern")  # `niveau` van een onderwerp dat elementen voor meer onderwerpen houdt
GEGENEREERD_RE = re.compile(r"^<!-- gegenereerd door (?P<tool>\S+); hash: (?P<hash>[0-9a-f]{64}) -->\n")


def wiki_yaml(wiki_root: Path = WIKI_ROOT) -> dict:
    """wiki.yaml, één keer per proces gelezen (de render vraagt haar per bronverwijzing op); een kopie, zodat een
    aanroeper de gedeelde versie niet kan wijzigen."""
    return copy.deepcopy(_wiki_yaml(Path(wiki_root).resolve()))


@functools.cache
def _wiki_yaml(wiki_root: Path) -> dict:
    return paths.load_wiki_yaml(wiki_root)


# --- Gegenereerde bestanden ---


def schrijf_gegenereerd(pad: Path, inhoud: str, tool: str) -> None:
    pad.parent.mkdir(parents=True, exist_ok=True)
    kop = f"{GEGENEREERD_PREFIX}{tool}; hash: {hashing.hash_text(inhoud)} -->\n"
    pad.write_text(kop + inhoud, encoding="utf-8", newline="\n")


def controleer_gegenereerd(pad: Path) -> str | None:
    """None als het bestand ongewijzigd is sinds het genereren, anders een melding."""
    tekst = pad.read_text(encoding="utf-8")
    m = GEGENEREERD_RE.match(tekst)
    if not m:
        return f"{pad}: gegenereerd bestand zonder geldige kop"
    if hashing.hash_text(tekst[m.end():]) != m.group("hash"):
        return f"{pad}: met de hand gewijzigd; genereer opnieuw met {m.group('tool')}"
    return None


# --- Body: secties, tabellen en links ---

LINK_RE = re.compile(r"\[(?P<tekst>[^\]]*)\]\((?P<doel>[^)\s]+)\)")


def sectie(body: str, kop: str) -> str | None:
    """Tekst onder `## <kop>` tot de volgende `## `-kop (None als de sectie ontbreekt)."""
    m = re.search(rf"(?m)^## {re.escape(kop)}\s*$", body)
    if not m:
        return None
    rest = body[m.end():]
    volgende = re.search(r"(?m)^## ", rest)
    return rest[: volgende.start()] if volgende else rest


def tabel(tekst: str | None) -> list[dict[str, str]]:
    """Eerste Markdown-tabel in `tekst` als lijst van {kolom: cel}. Een '\\|' in een cel blijft staan."""
    if not tekst:
        return []
    regels = [r.strip() for r in tekst.splitlines() if r.strip().startswith("|")]
    if len(regels) < 2:
        return []

    def cellen(regel: str) -> list[str]:
        delen = re.split(r"(?<!\\)\|", regel.strip().strip("|"))
        return [d.strip().replace("\\|", "|") for d in delen]

    kolommen = cellen(regels[0])
    rijen = []
    for regel in regels[2:]:
        waarden = cellen(regel)
        rijen.append({k: (waarden[i] if i < len(waarden) else "") for i, k in enumerate(kolommen)})
    return rijen


def link(cel: str) -> tuple[str, str] | None:
    m = LINK_RE.search(cel or "")
    return (m.group("tekst"), m.group("doel")) if m else None


def doel_van_link(van: Path, doel: str) -> Path:
    from urllib.parse import unquote

    return (van.parent / unquote(doel.split("#", 1)[0])).resolve()


def relatief(van: Path, naar: Path) -> str:
    import os

    return Path(os.path.relpath(naar.resolve(), van.resolve().parent)).as_posix()


# --- Bronverwijzingen: pagina → bronduiding → laag 1 (sources/raw/ of sources/modellen/) ---

BRON_ID_RE = re.compile(r"\b[0-9]{4}-[a-z0-9]+(?:-[a-z0-9]+)*\b")


def model_json(wiki_root: Path, sleutel: str) -> Path:
    """De JSON-omzetting in `sources/modellen/` van het model dat `wiki.yaml` `<sleutel>.bron` noemt (`ggm` of `gemma`)."""
    bron = (wiki_yaml(wiki_root).get(sleutel) or {}).get("bron")
    return paths.find_repo_root(wiki_root) / "sources" / "modellen" / f"{bron}.json"


def modelbronnen(wiki_root: Path = WIKI_ROOT) -> set[str]:
    y = wiki_yaml(wiki_root)
    return {y.get("ggm", {}).get("bron"), y.get("gemma", {}).get("bron")} - {None}


def bronduidingen(wiki_root: Path = WIKI_ROOT, onderwerp: str = "*") -> list[Path]:
    """De bronduidingen: `onderwerpen/<onderwerp>/bronduidingen/<brontype>/<bron-id>.md`, en bij `onderwerp` `*` ook die
    van de modellen: `modellen/<model>/bronduidingen/<brontype>/<bron-id>.md`."""
    gevonden = list(wiki_root.glob(f"onderwerpen/{onderwerp}/bronduidingen/*/*.md"))
    if onderwerp == "*":
        gevonden += wiki_root.glob("modellen/*/bronduidingen/*/*.md")
    return sorted(gevonden)


def brontype(wiki_root: Path, bron_id: str) -> str | None:
    """Het brontype van een bron uit de intake (`sources/index/<bron-id>.md`)."""
    from llmwiki import sources

    try:
        return sources.read_index_entry(paths.find_repo_root(wiki_root), bron_id).get("brontype")
    except FileNotFoundError:
        return None


def bron_doel(wiki_root: Path, bron_id: str) -> Path | None:
    """Waar een verwijzing naar deze bron heen linkt: de bronduiding. Een modelbron (GGM, GEMMA) heeft geen
    bronduiding (tools/ggm.py en tools/gemma.py zijn haar lens) en linkt naar haar tekst in laag 1. Een bron van
    een model of die voor de hele wiki geldt (Over GEMMA, de GEMMA-procesarchitectuur) heeft haar bronduiding in
    `modellen/<model>/bronduidingen/`."""
    if bron_id in modelbronnen(wiki_root):
        from llmwiki import sources

        repo = paths.find_repo_root(wiki_root)
        pad = sources.bron_dir(repo, bron_id) / f"{bron_id}.md"
        return pad.resolve() if pad.exists() else None
    treffers = [p for p in bronduidingen(wiki_root) if p.stem == bron_id]
    return treffers[0].resolve() if treffers else None


def bronnen_als_link(van: Path, tekst: str, wiki_root: Path = WIKI_ROOT) -> str:
    """Zet bron-id's die als platte tekst in `tekst` staan om naar links; bestaande links blijven staan.

    Een id zonder bronduiding (of een datum die op een id lijkt) blijft platte tekst: de controle meldt het.
    """
    def vervang(m: re.Match) -> str:
        doel = bron_doel(wiki_root, m.group(0))
        return f"[{m.group(0)}]({relatief(van, doel)})" if doel else m.group(0)

    delen, vorige = [], 0
    for m in LINK_RE.finditer(tekst):
        delen += [BRON_ID_RE.sub(vervang, tekst[vorige:m.start()]), m.group(0)]
        vorige = m.end()
    return "".join(delen) + BRON_ID_RE.sub(vervang, tekst[vorige:])


# --- Modelbestanden ophalen van GitHub (wiki.yaml `<sleutel>.herkomst`) ---


def herkomst_urls(herkomst: dict, ref: str | None = None, pad: str | None = None) -> tuple[str, str]:
    """(download-URL, weergave-URL) voor een bestand in een GitHub-repository (repository, ref, pad)."""
    from urllib.parse import quote

    repository, ref, pad = herkomst["repository"], ref or herkomst["ref"], pad or herkomst["pad"]
    return (f"https://raw.githubusercontent.com/{repository}/{ref}/{quote(pad)}",
            f"https://github.com/{repository}/blob/{ref}/{quote(pad)}")


def haal_op(wiki_root: Path, sleutel: str, bron_id: str, ref: str | None = None, pad: str | None = None) -> tuple[Path, str, str]:
    """Download het modelbestand van `wiki.yaml` `<sleutel>.herkomst` naar het kladblok.

    Geeft (bestand, download-URL, weergave-URL). De extensie volgt het pad in de repository.
    """
    from llmwiki import fetch

    herkomst = (wiki_yaml(wiki_root).get(sleutel) or {}).get("herkomst")
    if not herkomst:
        raise SystemExit(f"wiki.yaml mist {sleutel}.herkomst (repository, ref, pad); geef anders een lokaal bestand op")
    url, weergave = herkomst_urls(herkomst, ref, pad)
    extensie = Path(pad or herkomst["pad"]).suffix or ".bin"
    doel = wiki_root / ".work" / f"{sleutel}-release" / f"{bron_id}{extensie}"
    doel.parent.mkdir(parents=True, exist_ok=True)
    doel.write_bytes(fetch.fetch(url, timeout=300).inhoud)
    return doel, url, weergave


# --- Onderwerpen als één model ---


def afbakening_pad(onderwerp: str) -> Path:
    return ONDERWERPEN / onderwerp / "afbakening.yaml"


def begrippen_pad(onderwerp: str) -> str:
    return (ONDERWERPEN / onderwerp / "begrippen.md").as_posix()


def overzicht_pad(onderwerp: str) -> str:
    return (ONDERWERPEN / onderwerp / "overzicht.md").as_posix()


def afbakeningen(wiki_root: Path = WIKI_ROOT) -> dict[str, dict]:
    """onderwerp → afbakening (`onderwerpen/<onderwerp>/afbakening.yaml`: naam, niveau, omschrijving, bronnen, besluiten)."""
    from llmwiki import beoordeling

    return {p.parent.name: beoordeling.laad(p) for p in sorted((wiki_root / ONDERWERPEN).glob("*/afbakening.yaml"))}


def thuis(data: dict) -> str:
    """Het thuisonderwerp van een beoordeling: het eerste in `onderwerpen` (regel Thuishoren)."""
    return data["onderwerpen"][0]


def gedeelde_onderwerpen(onderwerpen: dict[str, dict]) -> set[str]:
    """De thematisch gedeelde onderwerpen en Kern: `niveau` thematisch of kern (regel Thuishoren)."""
    return {oid for oid, o in onderwerpen.items() if (o or {}).get("niveau") in GEDEELD}


def is_generiek(data: dict, uitkomst: dict | None, gedeeld: set[str] = frozenset()) -> bool:
    """Generiek element (kenmerk *generiek*) of thuis in een thematisch gedeeld onderwerp of Kern (`gedeeld`): telt
    niet mee voor de koppeling."""
    u = uitkomst or {}
    return thuis(data) in gedeeld or bool(u.get("generiek")) or u.get("objectniveau") == "generiek"


def relaties_per_onderwerp(alle: dict[str, dict], elementen: set[str]) -> dict[str, dict[str, int]]:
    """Per element het aantal relaties (beide richtingen) met elementen, naar het thuisonderwerp van de andere kant."""
    uit: dict[str, dict[str, int]] = {b: {} for b in elementen}
    for van in sorted(elementen):
        for r in alle[van].get("relaties", []):
            naar = r["naar"]
            if naar not in elementen or naar == van:
                continue
            uit[van][thuis(alle[naar])] = uit[van].get(thuis(alle[naar]), 0) + 1
            uit[naar][thuis(alle[van])] = uit[naar].get(thuis(alle[van]), 0) + 1
    return uit
