"""llmwiki workspace-check: werkplekcontrole (docs/onderbouwing.md 5.17).

Controleert Python-omgeving, harness-bindingen (via harness.check()), CLAUDE.md-
uitschakeling, pywikibot-/MCP-gereedheid voor sync-wiki's, en onafgeronde runs.
"""
from __future__ import annotations

import importlib.util
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
        return ["Pakket 'pywikibot' ontbreekt voor sync-wiki's. Draai 'uv sync --extra mediawiki'."]
    return []


def _check_pywikibot_family(repo_root: Path) -> list[str]:
    if importlib.util.find_spec("pywikibot") is None:
        return []  # al gemeld via _check_mediawiki_extra
    findings = []
    for wiki_root in _find_wiki_roots(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        family_name = wiki_yaml.get("site", {}).get("family")
        if not family_name:
            continue
        try:
            import pywikibot

            pywikibot.family.Family.load(family_name)
        except Exception:
            findings.append(
                f"Pywikibot-family '{family_name}' (wiki '{wiki_root.name}') niet geregistreerd. Zie README."
            )
    return findings


def _check_npx(repo_root: Path) -> list[str]:
    needs_mcp = any(paths.load_wiki_yaml(w).get("type") == "sync" for w in _find_wiki_roots(repo_root))
    if needs_mcp and shutil.which("npx") is None:
        return ["'npx' (Node.js) niet gevonden; nodig voor de MediaWiki-MCP-server."]
    return []


def _mcp_registration_notes(repo_root: Path) -> list[str]:
    notes = []
    for wiki_root in _find_wiki_roots(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        if wiki_yaml.get("type") != "sync":
            continue
        config_path = wiki_root / "mediawiki-mcp.config.json"
        if not config_path.exists():
            notes.append(f"{wiki_root.name}: mediawiki-mcp.config.json ontbreekt, draai 'llmwiki harness sync'.")
            continue
        rel = config_path.relative_to(wiki_root)
        notes.append(
            f"{wiki_root.name}: registreer de MCP-server eenmalig per machine (indien nog niet gedaan): "
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
        "pywikibot_family": _check_pywikibot_family(repo_root),
        "npx": _check_npx(repo_root),
        "onafgeronde_runs": _check_unfinished_runs(repo_root),
        "opgeschoond": [],
        "opmerkingen": _mcp_registration_notes(repo_root),
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
        result["claude_md"] or result["mediawiki_extra"] or result["pywikibot_family"] or result["npx"]
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
        ("pywikibot_family", "Pywikibot-family"),
        ("npx", "npx"),
        ("onafgeronde_runs", "Onafgeronde runs"),
        ("opgeschoond", "Opgeschoond"),
    ):
        for item in result[key]:
            lines.append(f"- [{label}] {item}")
    for opmerking in result["opmerkingen"]:
        lines.append(f"(opmerking) {opmerking}")
    return "\n".join(lines)
