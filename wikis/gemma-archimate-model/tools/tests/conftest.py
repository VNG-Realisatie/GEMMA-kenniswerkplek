"""Fixtures voor de tools van gemma-archimate-model: een tijdelijke repository met deze wiki
(wiki.yaml + schemas) en een paar bronnen in sources/index."""
import shutil
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gam_hulp import WIKI  # noqa: E402


@pytest.fixture
def archimate_repo(tmp_path):
    from llmwiki import sources

    root = tmp_path / "repo"
    (root / "sources" / "raw").mkdir(parents=True)
    (root / "sources" / "index").mkdir(parents=True)
    (root / "pyproject.toml").write_text("[project]\nname='fixture'\n", encoding="utf-8")
    wiki = root / "wikis" / "gemma-archimate-model"
    wiki.mkdir(parents=True)
    shutil.copy(WIKI / "wiki.yaml", wiki / "wiki.yaml")
    shutil.copytree(WIKI / "schemas", wiki / "schemas")
    (wiki / "log.md").write_text("# Logboek\n", encoding="utf-8")
    for bron_id, brontype in [
        ("2026-overheid-gemeentewet", "wet"),
        ("2026-vng-ggm", "informatiemodel"),
        ("2026-utrecht-nota", "beleid"),
    ]:
        original = tmp_path / f"{bron_id}.md"
        original.write_text(f"# {bron_id}\n", encoding="utf-8")
        sources.add(root, bron_id, original, titel=bron_id, tags=["test"], brontype=brontype)
    return root, wiki
