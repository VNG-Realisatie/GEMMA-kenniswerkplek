"""llmwiki lint: skillregels en afhankelijkheidsrichting (docs/onderbouwing.md 5.4, 5.7)."""
from __future__ import annotations

import re
from pathlib import Path

from . import frontmatter

ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "disable-model-invocation"}
MAX_LINES = 500


def _wiki_keys(repo_root: Path) -> list[str]:
    wikis_dir = repo_root / "wikis"
    if not wikis_dir.exists():
        return []
    return [p.name for p in wikis_dir.iterdir() if p.is_dir() and not p.name.startswith("_")]


def _discover_skills(repo_root: Path) -> dict[str, dict]:
    """name -> {path, scope, meta}"""
    skills: dict[str, dict] = {}

    def _scan(skills_dir: Path, expected_scope: str):
        if not skills_dir.exists():
            return
        for skill_dir in sorted(skills_dir.iterdir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            page = frontmatter.read(skill_md)
            skills[page.meta.get("name", skill_dir.name)] = {
                "path": skill_md,
                "dir_name": skill_dir.name,
                "scope": expected_scope,
                "meta": page.meta,
                "line_count": len(skill_md.read_text(encoding="utf-8").splitlines()),
            }

    _scan(repo_root / ".agents" / "skills", "core")
    for key in _wiki_keys(repo_root):
        _scan(repo_root / "wikis" / key / ".agents" / "skills", key)

    return skills


def run_lint(repo_root: Path) -> list[str]:
    errors: list[str] = []
    skills = _discover_skills(repo_root)
    wiki_keys = _wiki_keys(repo_root)

    for name, info in skills.items():
        meta = info["meta"]
        path = info["path"]

        if meta.get("name") != info["dir_name"]:
            errors.append(f"{path}: name '{meta.get('name')}' moet gelijk zijn aan de map '{info['dir_name']}'")

        unknown_fields = set(meta.keys()) - ALLOWED_FIELDS
        if unknown_fields:
            errors.append(f"{path}: niet-toegestane frontmattervelden {sorted(unknown_fields)}")

        if info["line_count"] >= MAX_LINES:
            errors.append(f"{path}: SKILL.md heeft {info['line_count']} regels (limiet {MAX_LINES})")

        scope = info["scope"]
        if scope == "core":
            if not name.startswith("wiki-"):
                errors.append(f"{path}: generieke skill '{name}' moet beginnen met 'wiki-'")
        else:
            if not name.startswith(f"{scope}-"):
                errors.append(f"{path}: wiki-skill '{name}' moet beginnen met '{scope}-'")

        if scope == "core":
            text = path.read_text(encoding="utf-8")
            if "wikis/" in text:
                errors.append(f"{path}: generieke skill verwijst naar een pad onder 'wikis/' (verboden, regel 5.4)")
            for key in wiki_keys:
                if re.search(rf"\b{re.escape(key)}-", text):
                    errors.append(f"{path}: generieke skill lijkt naar wiki-specifieke skill '{key}-...' te verwijzen")

        requires = (meta.get("metadata") or {}).get("requires-skills", "")
        for dep in requires.split():
            if dep not in skills:
                errors.append(f"{path}: requires-skills noemt onbekende skill '{dep}'")
                continue
            dep_scope = skills[dep]["scope"]
            if scope == "core" and dep_scope != "core":
                errors.append(f"{path}: generieke skill mag niet afhangen van wiki-skill '{dep}'")

    from . import markdown

    for pad in markdown.te_ontvouwen(repo_root):
        errors.append(
            f"{pad.relative_to(repo_root)}: harde regelovergang binnen een alinea of lijstitem (AGENTS.md, Schrijfwijze); "
            "herstel met 'llmwiki ontvouw --schrijf'"
        )

    names = [meta["meta"].get("name") for meta in skills.values()]
    duplicates = {n for n in names if names.count(n) > 1}
    if duplicates:
        errors.append(f"Dubbele skillnamen gevonden: {sorted(duplicates)}")

    return errors


# --- Pre-commit checks ---


def check_sources_immutable(repo_root: Path, changed_paths: list[str]) -> list[str]:
    """changed_paths: paden (relatief aan repo_root) die gewijzigd/verwijderd zijn (geen toevoeging)."""
    errors = []
    for rel_path in changed_paths:
        if rel_path.startswith("sources/raw/"):
            errors.append(f"{rel_path}: bestanden in sources/raw/ mogen alleen worden toegevoegd, nooit gewijzigd of verwijderd")
    return errors


def check_log_alleen_aanvullen(repo_root: Path, vorige: dict[str, str]) -> list[str]:
    """Elk logboek begint met dezelfde gebeurtenissen als de vorige versie (`vorige`: pad relatief aan
    repo_root → tekst, meestal uit HEAD). Vergelijkt de inhoud, niet de opmaak: een omzetting van het oude
    kopformaat naar de tabel mag, een gewijzigde of verwijderde gebeurtenis niet."""
    from . import logbook

    errors = []
    for rel_path, oude_tekst in sorted(vorige.items()):
        pad = repo_root / rel_path
        oud = logbook.lees_log(oude_tekst)
        nieuw = logbook.lees_log(pad.read_text(encoding="utf-8")) if pad.exists() else []
        if nieuw[:len(oud)] != oud:
            eerste = next((i for i, (a, b) in enumerate(zip(oud, nieuw)) if a != b), min(len(oud), len(nieuw)))
            errors.append(f"{rel_path}: het logboek is alleen aan te vullen; gebeurtenis {eerste + 1} "
                          "is gewijzigd of verwijderd (alleen 'llmwiki promote apply' of 'publish apply' schrijft hier)")
    return errors


def check_goedgekeurd_guard(repo_root: Path) -> list[str]:
    """Elke pagina (of, bij een wiki met beoordelingen, elke beoordeling) met status 'goedgekeurd' moet een
    overeenkomende regel in log.md hebben, met de hash van de inhoud."""
    from . import akkoord, beoordeling, hashing, logbook, paths

    errors = []
    for wiki_root in (repo_root / "wikis").glob("*"):
        wiki_yaml_path = wiki_root / "wiki.yaml"
        if not wiki_yaml_path.exists():
            continue
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        log_path = wiki_root / "log.md"
        log_text = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
        if akkoord.van_toepassing(wiki_yaml):
            for bid, (pad, data) in beoordeling.alle(wiki_root, wiki_yaml).items():
                if data.get("status") == "goedgekeurd" and not beoordeling.goedgekeurd_in_log(log_text, bid, data):
                    errors.append(f"{pad}: status 'goedgekeurd' zonder overeenkomende regel in {log_path} "
                                  "(alleen 'llmwiki promote apply' keurt goed)")
            continue
        for type_name, type_def in wiki_yaml.get("page_types", {}).items():
            if not type_def.get("curated"):
                continue
            page_dir = wiki_root / type_def["dir"]
            if not page_dir.exists():
                continue
            for page_path in sorted(page_dir.rglob("*.md")):
                page = frontmatter.read(page_path)
                if page.meta.get("status") != "goedgekeurd":
                    continue
                page_id = page.meta.get("id", page_path.stem)
                content_hash = hashing.short(hashing.hash_text(page_path.read_text(encoding="utf-8")))
                if not any(r.id == page_id and r.hash == content_hash for r in logbook.lees_log(log_text)):
                    errors.append(
                        f"{page_path}: status 'goedgekeurd' zonder overeenkomende regel in {log_path} "
                        "(gebruik 'llmwiki promote apply', zet dit niet handmatig)"
                    )
    return errors
