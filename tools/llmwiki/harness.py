"""Harness-bindingen: gegenereerde, deterministische bestanden per AI-omgeving,
uit `.agents/skills/` en `wiki.yaml`. Zie docs/onderbouwing.md 5.7/5.15/5.16.

MCP-clientbestanden verwijzen naar een gecommit `mediawiki-mcp.config.json` met
een pad relatief aan de wiki-map (nieuw verificatiepunt V10: of dat relatieve
pad in elke harness oplost). Precedentie tussen overlappende 'allow'/'ask'-
patronen (bv. 'pull*' vs 'pull* --doel *') is een harness-detail dat nog niet
live geverifieerd is.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from . import hashing, paths

MCP_PACKAGE = "@professional-wiki/mediawiki-mcp-server@latest"


# --- Ontdekking ---


def _all_wikis(repo_root: Path) -> list[Path]:
    wikis_dir = repo_root / "wikis"
    if not wikis_dir.exists():
        return []
    return sorted(p for p in wikis_dir.iterdir() if (p / "wiki.yaml").exists())


def _skill_names(skills_dir: Path) -> list[str]:
    if not skills_dir.exists():
        return []
    return sorted(p.name for p in skills_dir.iterdir() if (p / "SKILL.md").exists())


# --- Brug (.claude/skills/) ---


def _hash_dir(source_dir: Path) -> str:
    parts = []
    for path in sorted(source_dir.rglob("*")):
        if path.is_file():
            parts.append(f"{path.relative_to(source_dir)}:{hashing.hash_file(path)}")
    return hashing.hash_text("\n".join(parts))


def _remove_existing(target_dir: Path) -> None:
    if target_dir.is_symlink() or target_dir.is_file():
        target_dir.unlink()
    elif target_dir.exists():
        shutil.rmtree(target_dir)


def bridge_skill(source_dir: Path, target_dir: Path) -> str:
    """Symlink -> Windows-junction -> kopie + .bridge-source.json. Geeft de
    gebruikte methode terug ('symlink', 'junction' of 'copy')."""
    _remove_existing(target_dir)
    target_dir.parent.mkdir(parents=True, exist_ok=True)

    try:
        target_dir.symlink_to(source_dir, target_is_directory=True)
        return "symlink"
    except OSError:
        pass

    if sys.platform == "win32":
        result = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(target_dir), str(source_dir)],
            capture_output=True, text=True, check=False,
        )
        if result.returncode == 0:
            return "junction"

    shutil.copytree(source_dir, target_dir)
    (target_dir / ".bridge-source.json").write_text(
        json.dumps({"source": str(source_dir), "hash": _hash_dir(source_dir)}, indent=2),
        encoding="utf-8",
    )
    return "copy"


def _check_bridge(source_dir: Path, target_dir: Path) -> str | None:
    if target_dir.is_symlink():
        try:
            if target_dir.resolve() != source_dir.resolve():
                return f"Brug wijst naar het verkeerde doel: {target_dir}"
        except OSError:
            return f"Brug is een kapotte symlink: {target_dir}"
        return None
    if not target_dir.exists():
        return f"Brug ontbreekt: {target_dir}"
    marker = target_dir / ".bridge-source.json"
    if not marker.exists():
        return f"Brug is geen symlink en heeft geen .bridge-source.json: {target_dir}"
    info = json.loads(marker.read_text(encoding="utf-8"))
    if info.get("hash") != _hash_dir(source_dir):
        return f"Verouderde kopie: {target_dir} (bron gewijzigd sinds kopiëren)"
    return None


def _bridge_pairs(repo_root: Path) -> list[tuple[Path, Path]]:
    pairs = []
    for name in _skill_names(repo_root / ".agents" / "skills"):
        pairs.append((repo_root / ".agents" / "skills" / name, repo_root / ".claude" / "skills" / name))
    for wiki_root in _all_wikis(repo_root):
        for name in _skill_names(wiki_root / ".agents" / "skills"):
            pairs.append((wiki_root / ".agents" / "skills" / name, wiki_root / ".claude" / "skills" / name))
    return pairs


# --- Permissies (.claude/settings.json) ---

# llmwiki wordt altijd aangeroepen als `uv run python -m llmwiki` (zie tools/llmwiki/__main__.py).
def _llmwiki_regels(*subcommandos: str) -> list[str]:
    return [f"Bash(uv run python -m llmwiki {sub})" for sub in subcommandos]


_CLAUDE_SETTINGS = {
    "permissions": {
        "allow": _llmwiki_regels(
            "workspace-check*", "run *", "validate *", "source *", "lint*", "pull*", "promote plan*", "publish plan*",
        ),
        "ask": _llmwiki_regels("pull* --doel *", "promote apply*", "publish apply*"),
        "deny": [
            "Bash(*pywikibot*)",
            "Edit(voorstellen/**)",
            "Write(voorstellen/**)",
            "Edit(revisies.json)",
            "Write(revisies.json)",
        ],
    }
}


def _vscode_settings(is_wiki: bool) -> dict:
    settings = {"chat.useAgentsMdFile": True}
    if is_wiki:
        settings["chat.useCustomizationsInParentRepositories"] = True
    return settings


def _opencode_settings(is_wiki: bool) -> dict:
    settings: dict = {
        "$schema": "https://opencode.ai/config.json",
        "permission": {
            "bash": {
                "*llmwiki pull* --doel *": "ask",
                "*llmwiki promote apply*": "ask",
                "*llmwiki publish apply*": "ask",
                "*pywikibot*": "deny",
            }
        },
    }
    if is_wiki:
        settings = {"instructions": ["../../AGENTS.md"], **settings}
    return settings


# --- MCP (alleen sync-wiki's) ---


def _mcp_config(wiki_yaml: dict) -> dict:
    site = wiki_yaml["site"]
    server = site["server"]
    if not server.startswith("http"):
        server = f"https://{server}"
    return {
        "readOnly": True,
        "wikis": {
            wiki_yaml["key"]: {
                "sitename": wiki_yaml["key"],
                "server": server,
                "articlepath": site.get("articlepath", "/wiki"),
                "scriptpath": site.get("scriptpath", ""),
                "readOnly": True,
            }
        },
    }


def _needs_mcp(wiki_yaml: dict) -> bool:
    return wiki_yaml.get("type") == "sync" or bool(wiki_yaml.get("exports", {}).get("mediawiki"))


def _mcp_client_blocks(config_rel_path: str) -> dict[str, dict]:
    claude = {"mcpServers": {"mediawiki": {"command": "npx", "args": ["-y", MCP_PACKAGE], "env": {"CONFIG": config_rel_path}}}}
    vscode = {"servers": {"mediawiki": {"type": "stdio", "command": "npx", "args": ["-y", MCP_PACKAGE], "env": {"CONFIG": config_rel_path}}}}
    cursor = {"mcpServers": {"mediawiki": {"command": "npx", "args": ["-y", MCP_PACKAGE], "env": {"CONFIG": config_rel_path}}}}
    return {".mcp.json": claude, ".vscode/mcp.json": vscode, ".cursor/mcp.json": cursor}


# --- Generatie ---


def _write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def _generate_all(repo_root: Path) -> dict[Path, dict]:
    """path -> JSON-content voor alle gegenereerde bestanden (root + elke wiki)."""
    out: dict[Path, dict] = {}
    out[repo_root / ".claude" / "settings.json"] = _CLAUDE_SETTINGS
    out[repo_root / ".vscode" / "settings.json"] = _vscode_settings(is_wiki=False)
    out[repo_root / "opencode.json"] = _opencode_settings(is_wiki=False)

    for wiki_root in _all_wikis(repo_root):
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        out[wiki_root / ".claude" / "settings.json"] = _CLAUDE_SETTINGS
        out[wiki_root / ".vscode" / "settings.json"] = _vscode_settings(is_wiki=True)
        out[wiki_root / "opencode.json"] = _opencode_settings(is_wiki=True)

        if _needs_mcp(wiki_yaml):
            config_name = "mediawiki-mcp.config.json"
            out[wiki_root / config_name] = _mcp_config(wiki_yaml)
            for rel_path, content in _mcp_client_blocks(config_name).items():
                out[wiki_root / rel_path] = content

    return out


def sync(repo_root: Path) -> dict:
    """Schrijft alle harness-bindingen en de skill-brug. Geeft een verslag terug
    (bruggen + hun methode, geschreven bestanden)."""
    verslag = {"bruggen": [], "bestanden": []}
    for source_dir, target_dir in _bridge_pairs(repo_root):
        methode = bridge_skill(source_dir, target_dir)
        verslag["bruggen"].append({"skill": source_dir.name, "doel": str(target_dir), "methode": methode})

    for path, content in _generate_all(repo_root).items():
        _write_json(path, content)
        verslag["bestanden"].append(str(path))

    return verslag


def check(repo_root: Path) -> list[str]:
    """Volledig deterministisch: regenereert alles in het geheugen en
    vergelijkt byte-voor-byte; controleert brug-integriteit; meldt elke
    CLAUDE.md/CLAUDE.local.md op root- of wiki-pad."""
    problems: list[str] = []

    for source_dir, target_dir in _bridge_pairs(repo_root):
        issue = _check_bridge(source_dir, target_dir)
        if issue:
            problems.append(issue)

    for path, expected in _generate_all(repo_root).items():
        if not path.exists():
            problems.append(f"Ontbreekt (draai 'llmwiki harness sync'): {path}")
            continue
        actual = json.loads(path.read_text(encoding="utf-8"))
        if actual != expected:
            problems.append(f"Wijkt af van wat 'llmwiki harness sync' zou schrijven: {path}")

    for candidate in [repo_root, *(_all_wikis(repo_root))]:
        for name in ("CLAUDE.md", "CLAUDE.local.md"):
            if (candidate / name).exists():
                problems.append(
                    f"{candidate / name}: schakelt AGENTS.md uit voor Claude Code. Hernoem of verwijder."
                )

    return problems
