"""Gedeelde hulpfuncties voor de tools van gemma-archimate-model.

- gegenereerde modelbestanden (ggm/, gemma/) schrijven met een hash-kop, en controleren dat niemand ze met de hand
  wijzigde;
- secties, tabellen en links in Markdown lezen (bronanalyses);
- bronverwijzingen: pagina → bronanalyse (domein-lens) → sources/raw/;
- modelbestanden ophalen van GitHub.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from llmwiki import hashing, paths

WIKI_ROOT = Path(__file__).resolve().parent.parent
GEGENEREERD_PREFIX = "<!-- gegenereerd door "
GEGENEREERD_RE = re.compile(r"^<!-- gegenereerd door (?P<tool>\S+); hash: (?P<hash>[0-9a-f]{64}) -->\n")


def wiki_yaml(wiki_root: Path = WIKI_ROOT) -> dict:
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


def schrijf_json_gegenereerd(pad: Path, data: dict, tool: str) -> None:
    pad.parent.mkdir(parents=True, exist_ok=True)
    inhoud = json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True)
    pad.write_text(
        json.dumps({"_gegenereerd": {"tool": tool, "hash": hashing.hash_text(inhoud)}, "data": data}, ensure_ascii=False, indent=1, sort_keys=True),
        encoding="utf-8",
    )


def lees_json_gegenereerd(pad: Path) -> dict:
    return json.loads(pad.read_text(encoding="utf-8"))["data"]


def controleer_json_gegenereerd(pad: Path) -> str | None:
    geheel = json.loads(pad.read_text(encoding="utf-8"))
    inhoud = json.dumps(geheel.get("data"), ensure_ascii=False, indent=1, sort_keys=True)
    if hashing.hash_text(inhoud) != geheel.get("_gegenereerd", {}).get("hash"):
        return f"{pad}: met de hand gewijzigd; genereer opnieuw met {geheel.get('_gegenereerd', {}).get('tool')}"
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


# --- Bronverwijzingen: pagina → bronanalyse (domein-lens) → sources/raw/ ---

BRON_ID_RE = re.compile(r"\b[0-9]{4}-[a-z0-9]+(?:-[a-z0-9]+)*\b")


def modelbronnen(wiki_root: Path = WIKI_ROOT) -> set[str]:
    y = wiki_yaml(wiki_root)
    return {y.get("ggm", {}).get("bron"), y.get("gemma", {}).get("bron")} - {None}


def bron_doel(wiki_root: Path, bron_id: str) -> Path | None:
    """Waar een verwijzing naar deze bron heen linkt: de bronanalyse. Een modelbron (GGM, GEMMA) heeft geen
    bronanalyse (tools/ggm.py en tools/gemma.py zijn haar lens) en linkt naar haar tekst in sources/raw/. Een bron die
    voor de hele wiki geldt, kan haar bronanalyse in een analyse hebben (`bronanalyse_van`, zoals Over GEMMA)."""
    if bron_id in modelbronnen(wiki_root):
        pad = paths.find_repo_root(wiki_root) / "sources" / "raw" / f"{bron_id}.md"
        return pad.resolve() if pad.exists() else None
    map_ = wiki_root / wiki_yaml(wiki_root).get("page_types", {}).get("bronanalyse", {}).get("dir", "bronanalyses")
    treffers = sorted(map_.glob(f"*/{bron_id}.md"))
    if treffers:
        return treffers[0].resolve()
    from llmwiki import frontmatter

    for pad in sorted((wiki_root / "analyses").glob("*.md")):
        if bron_id in (frontmatter.read(pad).meta.get("bronanalyse_van") or []):
            return pad.resolve()
    return None


def bronnen_als_link(van: Path, tekst: str, wiki_root: Path = WIKI_ROOT) -> str:
    """Zet bron-id's die als platte tekst in `tekst` staan om naar links; bestaande links blijven staan.

    Een id zonder bronanalyse (of een datum die op een id lijkt) blijft platte tekst: de controle meldt het.
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
