"""Harde regelovergangen binnen alinea's verwijderen (Markdown), zie AGENTS.md sectie Schrijfwijze.

Een alinea, lijstitem of regel in een blockquote staat op één regel; de viewer bepaalt de kolombreedte.
Ongemoeid blijven: frontmatter, codeblokken (``` en ~~~), tabellen, koppen, horizontale lijnen, HTML-regels,
lege regels en bewuste regelovergangen (twee spaties of een backslash aan het eind van de regel).
"""
from __future__ import annotations

import re
from pathlib import Path

LIJSTITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
LIJN_RE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,}|={3,})\s*$")

# Buiten de omzetting: letterlijke bronnen, werkkopieën van externe sites, logboeken en kladblok.
UITGESLOTEN_DELEN = {".work", ".git", ".venv", "node_modules", "voorstellen", "Prompt en antwoorden", ".claude", ".obsidian"}
UITGESLOTEN_NAMEN = {"log.md", "voortgang.md"}


def _is_blok(regel: str) -> bool:
    """Regel die nooit met een vorige of volgende regel wordt samengevoegd."""
    s = regel.lstrip()
    return (not s or s.startswith(("#", "|", "<")) or FENCE_RE.match(regel) is not None
            or LIJN_RE.match(regel) is not None)


def _bewuste_overgang(regel: str) -> bool:
    return regel.endswith("  ") or regel.rstrip().endswith("\\")


def _quote_inhoud(regel: str) -> str | None:
    s = regel.lstrip()
    return s[1:].lstrip() if s.startswith(">") else None


def ontvouw(tekst: str) -> str:
    regels = tekst.split("\n")
    uit: list[str] = []
    start = 0
    if regels and regels[0].strip() == "---":
        for i in range(1, len(regels)):
            if regels[i].strip() == "---":
                uit.extend(regels[: i + 1])
                start = i + 1
                break

    fence: str | None = None
    for regel in regels[start:]:
        if fence:
            uit.append(regel)
            m = FENCE_RE.match(regel)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and regel.strip() == m.group(1):
                fence = None
            continue
        m = FENCE_RE.match(regel)
        if m:
            fence = m.group(1)
            uit.append(regel)
            continue

        vorige = uit[-1] if len(uit) > start else None
        if vorige is None or _is_blok(vorige) or _is_blok(regel) or _bewuste_overgang(vorige):
            uit.append(regel)
            continue

        vorige_quote, quote = _quote_inhoud(vorige), _quote_inhoud(regel)
        if vorige_quote is not None or quote is not None:
            # Alleen binnen dezelfde blockquote samenvoegen: beide regels hebben tekst en de nieuwe regel begint geen blok.
            if vorige_quote and quote and not _is_blok(vorige_quote) and not _is_blok(quote) and not LIJSTITEM_RE.match(quote):
                uit[-1] = vorige.rstrip() + " " + quote
            else:
                uit.append(regel)
            continue

        if LIJSTITEM_RE.match(regel):
            uit.append(regel)
            continue
        uit[-1] = vorige.rstrip() + " " + regel.strip()
    return "\n".join(uit)


def bestanden(repo_root: Path) -> list[Path]:
    """Markdown-bestanden waarvoor de regel geldt (zie UITGESLOTEN_*; plus sources/raw en wikis/*/content)."""
    result = []
    for pad in sorted(repo_root.rglob("*.md")):
        rel = pad.relative_to(repo_root)
        delen = set(rel.parts)
        verborgen = any(d.startswith(".") and d != ".agents" for d in rel.parts[:-1])
        if verborgen or delen & UITGESLOTEN_DELEN or pad.name in UITGESLOTEN_NAMEN:
            continue
        if rel.parts[:2] == ("sources", "raw") or (len(rel.parts) > 2 and rel.parts[0] == "wikis" and rel.parts[2] == "content"):
            continue
        result.append(pad)
    return result


def te_ontvouwen(repo_root: Path) -> list[Path]:
    return [p for p in bestanden(repo_root) if ontvouw(p.read_text(encoding="utf-8")) != p.read_text(encoding="utf-8")]
