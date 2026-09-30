"""Inloggegevens en npx zijn alleen nodig voor werk met een sync-wiki: ze blokkeren de werkplek niet."""
import yaml

from llmwiki import workspace_check


def _repo_met_sync_wiki(tmp_path):
    root = tmp_path / "repo"
    wiki_root = root / "wikis" / "gemma"
    wiki_root.mkdir(parents=True)
    (root / "pyproject.toml").write_text("[project]\nname='fixture'\n", encoding="utf-8")
    wiki_yaml = {
        "key": "gemma",
        "type": "sync",
        "site": {"family": "gemmaonline", "code": "redactie", "server": "https://redactie.gemmaonline.nl", "inlog": {"gebruiker": "TEST_GEMMA_USER"}},
    }
    (wiki_root / "wiki.yaml").write_text(yaml.safe_dump(wiki_yaml), encoding="utf-8")
    return root


def test_npx_ontbreekt_is_een_opmerking(tmp_path, monkeypatch):
    root = _repo_met_sync_wiki(tmp_path)
    monkeypatch.setattr(workspace_check.shutil, "which", lambda naam: None)
    notes = workspace_check._npx_notes(root)
    assert len(notes) == 1 and "alleen nodig" in notes[0] and "wikis/gemma" in notes[0]


def test_ontbrekende_inlog_is_een_opmerking_voor_die_wiki(tmp_path, monkeypatch):
    root = _repo_met_sync_wiki(tmp_path)
    monkeypatch.delenv("TEST_GEMMA_USER", raising=False)
    notes = workspace_check._inlog_notes(root)
    assert notes and all("alleen nodig als je met wikis/gemma werkt" in n for n in notes)


def test_zonder_npx_en_inlog_blokkeert_de_werkplek_niet(tmp_path, monkeypatch):
    root = _repo_met_sync_wiki(tmp_path)
    (root / "wikis" / "gemma" / "families").mkdir()
    (root / "wikis" / "gemma" / "families" / "gemmaonline_family.py").write_text("", encoding="utf-8")
    monkeypatch.setattr(workspace_check.shutil, "which", lambda naam: None)
    monkeypatch.delenv("TEST_GEMMA_USER", raising=False)
    result = workspace_check.check(root)
    assert result["status"] != "actie gebruiker"
    assert any("npx" in o for o in result["opmerkingen"])
    assert any("TEST_GEMMA_USER" in o for o in result["opmerkingen"])
