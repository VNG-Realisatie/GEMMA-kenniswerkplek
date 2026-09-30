"""llmwiki workspace-check: werkplekcontrole (docs/onderbouwing.md 5.17).

Controleert Python-omgeving, harness-bindingen (via harness.check()), CLAUDE.md-
uitschakeling, pywikibot-/MCP-gereedheid voor sync-wiki's, en onafgeronde runs.
"""
from __future__ import annotations

import importlib.util
import os
import shutil
from pathlib import Path

from . import harness, paths, runs


def _find_wiki_roots(repo_root: Path) -> list[Path]:
    wikis_dir = repo_root / "wikis"
    if not wikis_dir.exists():
        return []
    return [p for p in wikis_dir.iterdir() if (p / "wiki.yaml").exists()]


def _check_python_env() -> list[str]:
    missing = [mod for mod in ("jsonschema", "yaml") if importlib.util.find_spec(mod) is None]
    if missing:
        return [f"Python-afhankelijkheden ontbreken: {missing}. Draai 'uv sync'."]
    return []


def _split_harness_findings(findings: list[str]) -> tuple[list[str], list[str]]:
    """(claude_md_issues, overige_harness_issues) -- CLAUDE.md is een handeling
    van de gebruiker; de rest lost 'llmwiki harness sync' vanzelf op."""
    claude_md, overig = [], []
    for f in findings:
        (claude_md if "CLAUDE.md" in f else overig).append(f)
    return claude_md, overig


def _check_mediawiki_extra(repo_root: Path) -> list[str]:
    if not any(paths.load_wiki_yaml(w).get("type") == "sync" for w in _find_wiki_roots(repo_root)):
        return []
    if importlib.util.find_spec("pywikibot") is None:
        return ["Pakket 'pywikibot' ontbreekt voor sync-wiki's. Draai 'uv sync'."]
    return []


def _doelen(wiki_yaml: dict) -> dict[str, dict]:
    return {"site": wiki_yaml.get("site", {}), **(wiki_yaml.get("test_targets") or {})}


def _check_family_bestanden(repo_root: Path) -> list[str]:
    """Elke family uit wiki.yaml moet als bestand in de wiki-map staan (llmwiki meldt het aan bij pywikibot)."""
    findings = []
    for wiki_root in _find_wiki_roots(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        for naam in sorted({d["family"] for d in _doelen(wiki_yaml).values() if d.get("family")}):
            if not (wiki_root / "families" / f"{naam}_family.py").exists():
                findings.append(f"{wiki_root.name}: families/{naam}_family.py ontbreekt (servers van family '{naam}').")
    return findings


def _inlog_notes(repo_root: Path) -> list[str]:
    """Opmerking per doel waarvoor inloggegevens ontbreken; alleen pull/publish naar dat doel heeft ze nodig."""
    notes = []
    for wiki_root in _find_wiki_roots(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        if wiki_yaml.get("type") != "sync" or wiki_root.name.startswith("_"):
            continue
        for doel, target in _doelen(wiki_yaml).items():
            namen = [n for blok in ("inlog", "http_toegang") for n in (target.get(blok) or {}).values()]
            ontbrekend = [n for n in namen if not os.environ.get(n, "").strip()]
            if ontbrekend:
                notes.append(
                    f"{wiki_root.name}, doel '{doel}': omgevingsvariabele(n) {', '.join(ontbrekend)} niet gezet; "
                    f"alleen nodig als je met wikis/{wiki_root.name} werkt (pull/publish naar dit doel). "
                    "Zie README, 'Inloggen op GEMMA Online'."
                )
    return notes


def _npx_notes(repo_root: Path) -> list[str]:
    """Opmerking als npx ontbreekt: alleen de sync-wiki's gebruiken de MediaWiki-MCP-server, dus het blokkeert niets."""
    sync_wikis = [w.name for w in _find_wiki_roots(repo_root) if paths.load_wiki_yaml(w).get("type") == "sync" and not w.name.startswith("_")]
    if sync_wikis and shutil.which("npx") is None:
        return [
            f"'npx' (Node.js) niet gevonden; alleen nodig voor de MediaWiki-MCP-server als je met "
            f"{', '.join(f'wikis/{n}' for n in sync_wikis)} werkt."
        ]
    return []


def _mcp_registration_notes(repo_root: Path) -> list[str]:
    notes = []
    for wiki_root in _find_wiki_roots(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        if wiki_yaml.get("type") != "sync" or wiki_root.name.startswith("_"):
            continue
        config_path = wiki_root / "mediawiki-mcp.config.json"
        if not config_path.exists():
            notes.append(f"{wiki_root.name}: mediawiki-mcp.config.json ontbreekt, draai 'llmwiki harness sync'.")
            continue
        rel = config_path.relative_to(wiki_root)
        notes.append(
            f"{wiki_root.name}: als je met wikis/{wiki_root.name} werkt, registreer de MCP-server eenmalig per machine (indien nog niet gedaan): "
            f"claude mcp add mediawiki -e CONFIG={rel} -- npx -y {harness.MCP_PACKAGE}"
        )
    return notes


def _check_unfinished_runs(repo_root: Path) -> list[str]:
    findings = []
    for wiki_root in _find_wiki_roots(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        if wiki_yaml.get("type") == "knowledge-base":
            continue
        for run_id in runs.list_runs(wiki_root):
            try:
                if not runs.is_finished(wiki_root, wiki_yaml, run_id):
                    findings.append(f"Onafgeronde run '{run_id}' in {wiki_root.name}; hervat met 'llmwiki run resume {run_id}'")
            except runs.RunError:
                continue
    return findings


def check(repo_root: Path, fix: bool = False) -> dict:
    if fix:
        harness.sync(repo_root)

    claude_md, harness_bindingen = _split_harness_findings(harness.check(repo_root))

    result = {
        "status": "ok",
        "python_omgeving": _check_python_env(),
        "harness_bindingen": harness_bindingen,
        "claude_md": claude_md,
        "mediawiki_extra": _check_mediawiki_extra(repo_root),
        "family_bestanden": _check_family_bestanden(repo_root),
        "onafgeronde_runs": _check_unfinished_runs(repo_root),
        "opgeschoond": [],
        "opmerkingen": _inlog_notes(repo_root) + _npx_notes(repo_root) + _mcp_registration_notes(repo_root),
    }

    if fix:
        for wiki_root in _find_wiki_roots(repo_root):
            wiki_yaml = paths.load_wiki_yaml(wiki_root)
            if wiki_yaml.get("type") == "knowledge-base":
                continue
            retention = wiki_yaml.get("work", {}).get("retention_days", 30)
            removed = runs.prune(wiki_root, wiki_yaml, retention)
            result["opgeschoond"].extend(f"{wiki_root.name}/{r}" for r in removed)

    herstelbaar = bool(result["python_omgeving"] or result["harness_bindingen"])
    actie_gebruiker = bool(
        result["claude_md"] or result["mediawiki_extra"] or result["family_bestanden"]
    )
    if actie_gebruiker:
        result["status"] = "actie gebruiker"
    elif herstelbaar:
        result["status"] = "herstelbaar"
    else:
        result["status"] = "ok"
    return result


def format_text(result: dict) -> str:
    lines = [f"Status: {result['status']}"]
    for key, label in (
        ("python_omgeving", "Python-omgeving"),
        ("harness_bindingen", "Harness-bindingen"),
        ("claude_md", "CLAUDE.md"),
        ("mediawiki_extra", "pywikibot"),
        ("family_bestanden", "Family-bestand"),
        ("onafgeronde_runs", "Onafgeronde runs"),
        ("opgeschoond", "Opgeschoond"),
    ):
        for item in result[key]:
            lines.append(f"- [{label}] {item}")
    for opmerking in result["opmerkingen"]:
        lines.append(f"(opmerking) {opmerking}")
    return "\n".join(lines)
