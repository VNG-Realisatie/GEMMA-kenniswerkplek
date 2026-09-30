import json
from pathlib import Path

import pytest
import yaml

from llmwiki import harness


@pytest.fixture
def harness_repo(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    (root / "pyproject.toml").write_text("[project]\nname='fixture'\n", encoding="utf-8")

    generic_skill = root / ".agents" / "skills" / "wiki-update"
    generic_skill.mkdir(parents=True)
    (generic_skill / "SKILL.md").write_text("---\nname: wiki-update\ndescription: x\n---\nx\n", encoding="utf-8")

    wiki_root = root / "wikis" / "template"
    wiki_root.mkdir(parents=True)
    wiki_yaml = {
        "key": "template",
        "type": "sync",
        "site": {"family": "gemmaonline", "code": "en", "server": "redactie.gemmaonline.nl", "articlepath": "/wiki", "scriptpath": ""},
    }
    (wiki_root / "wiki.yaml").write_text(yaml.safe_dump(wiki_yaml), encoding="utf-8")

    wiki_skill = wiki_root / ".agents" / "skills" / "template-edit"
    wiki_skill.mkdir(parents=True)
    (wiki_skill / "SKILL.md").write_text("---\nname: template-edit\ndescription: x\n---\nx\n", encoding="utf-8")

    return root, wiki_root


def test_check_reports_missing_before_sync(harness_repo):
    root, wiki_root = harness_repo
    problems = harness.check(root)
    assert any("ontbreekt" in p.lower() or "ontbreekt (draai" in p.lower() for p in problems)


def test_sync_then_check_is_clean(harness_repo):
    root, wiki_root = harness_repo
    harness.sync(root)
    assert harness.check(root) == []


def test_check_without_bridges_ignores_missing_bridges(harness_repo):
    root, wiki_root = harness_repo
    harness.sync(root)
    harness._remove_existing(root / ".claude" / "skills" / "wiki-update")
    assert any("Brug ontbreekt" in p for p in harness.check(root))
    assert harness.check(root, bruggen=False) == []


def test_sync_creates_managed_copy_bridge(harness_repo):
    root, wiki_root = harness_repo
    harness.sync(root)
    bridge = root / ".claude" / "skills" / "wiki-update"
    assert not bridge.is_symlink()
    assert (bridge / "SKILL.md").exists()
    marker = json.loads((bridge / ".bridge-source.json").read_text(encoding="utf-8"))
    assert marker["source"] == str(root / ".agents" / "skills" / "wiki-update")
    assert marker["hash"]


def test_remove_existing_uses_rmdir_for_legacy_junction_shape(tmp_path, monkeypatch):
    bridge = tmp_path / "oude-brug"
    bridge.mkdir()
    monkeypatch.setattr(harness, "_is_junction", lambda path: Path(path) == bridge)
    harness._remove_existing(bridge)
    assert not bridge.exists()


def test_mcp_config_generated_for_sync_wiki(harness_repo):
    root, wiki_root = harness_repo
    harness.sync(root)
    config = json.loads((wiki_root / "mediawiki-mcp.config.json").read_text())
    assert config["wikis"]["template"]["server"] == "https://redactie.gemmaonline.nl"
    assert config["readOnly"] is True

    mcp_json = json.loads((wiki_root / ".mcp.json").read_text())
    assert mcp_json["mcpServers"]["mediawiki"]["env"]["CONFIG"] == "mediawiki-mcp.config.json"


def test_check_detects_manual_drift(harness_repo):
    root, wiki_root = harness_repo
    harness.sync(root)
    settings_path = root / ".claude" / "settings.json"
    settings_path.write_text('{"permissions": {"allow": []}}', encoding="utf-8")
    problems = harness.check(root)
    assert any("Wijkt af" in p for p in problems)


def test_check_detects_claude_md(harness_repo):
    root, wiki_root = harness_repo
    (wiki_root / "CLAUDE.md").write_text("x", encoding="utf-8")
    problems = harness.check(root)
    assert any("CLAUDE.md" in p for p in problems)


def test_check_accepts_valid_copy_bridge(harness_repo):
    root, wiki_root = harness_repo
    harness.sync(root)
    assert harness.check(root) == []


def test_check_detects_copy_from_wrong_canonical_source(harness_repo):
    root, wiki_root = harness_repo
    harness.sync(root)
    marker_path = root / ".claude" / "skills" / "wiki-update" / ".bridge-source.json"
    marker = json.loads(marker_path.read_text(encoding="utf-8"))
    marker["source"] = str(root / ".agents" / "skills" / "andere-bron")
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    problems = harness.check(root)
    assert any("verkeerde canonieke bron" in p for p in problems)


def test_check_detects_stale_copy_bridge(harness_repo):
    root, wiki_root = harness_repo
    harness.sync(root)

    # Bron wijzigt na het kopiëren.
    (root / ".agents" / "skills" / "wiki-update" / "SKILL.md").write_text(
        "---\nname: wiki-update\ndescription: gewijzigd\n---\nx\n", encoding="utf-8"
    )
    problems = harness.check(root)
    assert any("Verouderde kopie" in p for p in problems)
