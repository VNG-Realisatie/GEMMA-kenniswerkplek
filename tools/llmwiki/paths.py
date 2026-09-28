"""Padresolutie: repository-root en wiki-root vinden vanuit elke werkmap."""
from __future__ import annotations

from pathlib import Path

import yaml


class NotFoundError(RuntimeError):
    pass


def find_repo_root(start: Path | None = None) -> Path:
    """Zoek omhoog naar de map met pyproject.toml (of .git als terugval)."""
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "pyproject.toml").exists():
            return candidate
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists():
            return candidate
    raise NotFoundError(
        "Geen repository-root gevonden (geen pyproject.toml of .git in "
        f"{current} of een bovenliggende map)."
    )


def find_wiki_root(start: Path | None = None) -> Path:
    """Zoek omhoog naar de map met wiki.yaml."""
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "wiki.yaml").exists():
            return candidate
    raise NotFoundError(
        f"Geen wiki.yaml gevonden vanuit {current}. Draai dit commando vanuit "
        "een wiki-map (bijvoorbeeld wikis/_template-md) of geef --wiki op."
    )


def load_wiki_yaml(wiki_root: Path) -> dict:
    data = yaml.safe_load((wiki_root / "wiki.yaml").read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"wiki.yaml in {wiki_root} is leeg of ongeldig")
    return data
