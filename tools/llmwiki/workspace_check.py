"""llmwiki workspace-check: beperkte werkplekcontrole (zonder de Klus-2 harness-brug).

Zie docs/onderbouwing.md 5.17. Deze versie controleert wat zonder harness-bindingen
kan: Python-omgeving, CLAUDE.md-uitschakeling, credentialnamen, onafgeronde runs en
opruimen. De Claude Code-brug (`.claude/skills/`) en MCP-configuratie horen bij
Klus 2 en worden hier nog niet gegenereerd of gecontroleerd.
"""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path

from . import paths, runs


def _find_wiki_roots(repo_root: Path) -> list[Path]:
    wikis_dir = repo_root / "wikis"
    if not wikis_dir.exists():
        return []
    return [p for p in wikis_dir.iterdir() if (p / "wiki.yaml").exists()]


def _check_claude_md(repo_root: Path) -> list[str]:
    findings = []
    candidates = [repo_root, *(_find_wiki_roots(repo_root))]
    for root in candidates:
        for name in ("CLAUDE.md", "CLAUDE.local.md"):
            if (root / name).exists():
                findings.append(
                    f"{root / name}: dit bestand schakelt AGENTS.md uit voor Claude Code. "
                    "Hernoem of verwijder het."
                )
    return findings


def _check_python_env() -> list[str]:
    missing = [mod for mod in ("jsonschema", "yaml") if importlib.util.find_spec(mod) is None]
    if missing:
        return [f"Python-afhankelijkheden ontbreken: {missing}. Draai 'uv sync'."]
    return []


def _check_credentials(repo_root: Path) -> list[str]:
    findings = []
    for wiki_root in _find_wiki_roots(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        if wiki_yaml.get("type") != "sync":
            continue
        key = wiki_yaml.get("key", wiki_root.name).upper()
        for suffix in ("USER", "PASSWORD"):
            var = f"MW_{key}_{suffix}"
            if not os.environ.get(var):
                findings.append(f"Omgevingsvariabele {var} ontbreekt voor wiki '{wiki_root.name}'")
    return findings


def _check_unfinished_runs(repo_root: Path) -> list[str]:
    findings = []
    for wiki_root in _find_wiki_roots(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        for run_id in runs.list_runs(wiki_root):
            try:
                if not runs.is_finished(wiki_root, wiki_yaml, run_id):
                    findings.append(f"Onafgeronde run '{run_id}' in {wiki_root.name}; hervat met 'llmwiki run resume {run_id}'")
            except runs.RunError:
                continue
    return findings


def check(repo_root: Path, fix: bool = False) -> dict:
    result = {
        "status": "ok",
        "python_omgeving": _check_python_env(),
        "claude_md": _check_claude_md(repo_root),
        "credentials": _check_credentials(repo_root),
        "onafgeronde_runs": _check_unfinished_runs(repo_root),
        "opgeschoond": [],
        "opmerkingen": [
            "De Claude Code-brug en MCP-configuratie (Klus 2) zijn in deze inrichting nog niet gebouwd.",
        ],
    }

    if fix:
        for wiki_root in _find_wiki_roots(repo_root):
            wiki_yaml = paths.load_wiki_yaml(wiki_root)
            retention = wiki_yaml.get("work", {}).get("retention_days", 30)
            removed = runs.prune(wiki_root, wiki_yaml, retention)
            result["opgeschoond"].extend(f"{wiki_root.name}/{r}" for r in removed)

    herstelbaar = bool(result["python_omgeving"])
    actie_gebruiker = bool(result["claude_md"] or result["credentials"])
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
        ("claude_md", "CLAUDE.md"),
        ("credentials", "Credentials"),
        ("onafgeronde_runs", "Onafgeronde runs"),
        ("opgeschoond", "Opgeschoond"),
    ):
        for item in result[key]:
            lines.append(f"- [{label}] {item}")
    for opmerking in result["opmerkingen"]:
        lines.append(f"(opmerking) {opmerking}")
    return "\n".join(lines)
