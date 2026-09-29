"""Gedeelde hulpfuncties voor de tools van gemma-archimate-model.

- elementpagina's vinden en lezen (paginatypen met `curated: true` uit wiki.yaml);
- gegenereerde bestanden schrijven met een hash-kop, en controleren dat niemand ze met de hand wijzigde;
- een gewijzigde pagina stagen in het kladblok van een run (changeset), zodat ook tool-wijzigingen
  via de promotiegate lopen.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from llmwiki import frontmatter, hashing, paths, runs

WIKI_ROOT = Path(__file__).resolve().parent.parent
GEGENEREERD_PREFIX = "<!-- gegenereerd door "
GEGENEREERD_RE = re.compile(r"^<!-- gegenereerd door (?P<tool>\S+); hash: (?P<hash>[0-9a-f]{64}) -->\n")


@dataclass
class Element:
    pad: Path
    paginatype: str
    meta: dict
    body: str

    @property
    def id(self) -> str:
        return self.meta.get("id", self.pad.stem)


def wiki_yaml(wiki_root: Path = WIKI_ROOT) -> dict:
    return paths.load_wiki_yaml(wiki_root)


def element_types(wiki_yaml_data: dict) -> dict[str, dict]:
    return {naam: d for naam, d in wiki_yaml_data.get("page_types", {}).items() if d.get("curated")}


def elementen(wiki_root: Path = WIKI_ROOT) -> list[Element]:
    result = []
    for paginatype, definitie in element_types(wiki_yaml(wiki_root)).items():
        map_ = wiki_root / definitie["dir"]
        if not map_.exists():
            continue
        for pad in sorted(map_.rglob("*.md")):
            page = frontmatter.read(pad)
            result.append(Element(pad, paginatype, page.meta, page.body))
    return result


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


# --- Stagen in een run ---


def stage(wiki_root: Path, run_id: str, doel: Path, page: frontmatter.Page, paginatype: str) -> Path:
    """Zet een (gewijzigde) pagina in de changeset van een run en werkt changeset.json bij.

    Een pagina die op `goedgekeurd` stond, gaat terug naar `review`: alleen `promote apply` keurt goed.
    """
    rdir = runs.run_dir(wiki_root, run_id)
    if not rdir.exists():
        raise FileNotFoundError(f"Run {run_id} bestaat niet")
    if page.meta.get("status") == "goedgekeurd":
        page.meta["status"] = "review"
    rel = doel.resolve().relative_to(wiki_root.resolve()).as_posix()
    staged_naam = rel.replace("/", "__")
    frontmatter.write(rdir / "changeset" / staged_naam, page)

    cs_pad = rdir / "changeset-concept.json"
    changeset = json.loads(cs_pad.read_text(encoding="utf-8")) if cs_pad.exists() else {"run": run_id, "paginas": []}
    changeset["paginas"] = [p for p in changeset["paginas"] if p["pad"] != rel]
    changeset["paginas"].append(
        {"pad": rel, "staged_bestand": staged_naam, "actie": "wijzigen" if doel.exists() else "nieuw", "type": paginatype}
    )
    cs_pad.write_text(json.dumps(changeset, indent=2, ensure_ascii=False), encoding="utf-8")
    return rdir / "changeset" / staged_naam


# --- Modelvelden (ggm_*/gemma_*) vergelijken en stagen ---


def modelverschillen(wiki_root: Path, sleutelveld: str, veldnamen: tuple[str, ...], zoek, velden_van) -> list[dict]:
    """Elementen waarvan de modelvelden afwijken van het huidige model.

    `zoek(sleutel)` geeft het modelobject of None; `velden_van(obj)` geeft de verwachte velden.
    """
    result = []
    for el in elementen(wiki_root):
        sleutel = el.meta.get(sleutelveld)
        if not sleutel:
            continue
        obj = zoek(sleutel)
        if obj is None:
            result.append({"element": el.id, "pad": str(el.pad), "melding": f"{sleutelveld} {sleutel} bestaat niet meer in het model"})
            continue
        verwacht = velden_van(obj)
        huidig = {k: el.meta[k] for k in veldnamen if k in el.meta}
        if huidig != verwacht:
            result.append({"element": el.id, "pad": str(el.pad),
                           "velden": sorted(k for k in set(huidig) | set(verwacht) if huidig.get(k) != verwacht.get(k)),
                           "verwacht": verwacht})
    return result


def modelverrijk(wiki_root: Path, lijst: list[dict], veldnamen: tuple[str, ...], run_id: str | None) -> list[dict]:
    """Met een run-id: zet de verwachte modelvelden in een gestagede kopie van elke afwijkende pagina."""
    if not run_id:
        return lijst
    for v in lijst:
        if "verwacht" not in v:
            continue
        pad = Path(v["pad"])
        page = frontmatter.read(pad)
        for k in veldnamen:
            page.meta.pop(k, None)
        page.meta.update(v["verwacht"])
        v["gestaged"] = str(stage(wiki_root, run_id, pad, page, page.meta.get("type")))
    return lijst


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


def element_index(wiki_root: Path = WIKI_ROOT) -> dict[str, Element]:
    return {el.id: el for el in elementen(wiki_root)}


def doel_van_link(van: Path, doel: str) -> Path:
    from urllib.parse import unquote

    return (van.parent / unquote(doel.split("#", 1)[0])).resolve()


def relatief(van: Path, naar: Path) -> str:
    import os

    return Path(os.path.relpath(naar.resolve(), van.resolve().parent)).as_posix()
