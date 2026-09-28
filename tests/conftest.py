from __future__ import annotations

from pathlib import Path

import pytest
import yaml

WIKI_YAML_TEMPLATE = {
    "key": "demo",
    "type": "curation",
    "sources": {"tags": ["demo"], "exclude_tags": []},
    "page_types": {
        "onderwerp": {"dir": "onderwerpen"},
        "bron": {"dir": "bronnen", "group_by": "onderwerp"},
        "kandidaat": {"dir": "kandidaten", "curated": True},
    },
    "curation": {
        "states": ["kandidaat", "review", "goedgekeurd", "afgewezen"],
        "gated": ["goedgekeurd"],
        "approval": "chat",
        "min_reviewers": 1,
    },
    "work": {"retention_days": 30},
}


@pytest.fixture
def make_repo(tmp_path):
    def _make(approval: str = "chat"):
        root = tmp_path / "repo"
        root.mkdir()
        (root / "pyproject.toml").write_text("[project]\nname = 'fixture'\n", encoding="utf-8")
        (root / "sources" / "raw").mkdir(parents=True)
        (root / "sources" / "index").mkdir(parents=True)

        wiki_root = root / "wikis" / "demo"
        for sub in ("onderwerpen", "bronnen", "kandidaten", "voorstellen", ".work"):
            (wiki_root / sub).mkdir(parents=True)

        wiki_yaml = {**WIKI_YAML_TEMPLATE, "curation": {**WIKI_YAML_TEMPLATE["curation"], "approval": approval}}
        (wiki_root / "wiki.yaml").write_text(yaml.safe_dump(wiki_yaml, sort_keys=False), encoding="utf-8")
        (wiki_root / "log.md").write_text("# Logboek\n", encoding="utf-8")

        return root, wiki_root

    return _make


@pytest.fixture
def repo(make_repo):
    return make_repo()
