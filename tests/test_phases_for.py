import pytest

from llmwiki import runs


def test_sync_has_single_pre_gate_phase():
    assert runs.phases_for({"type": "sync"}) == ["validate"]


def test_curation_has_four_pre_gate_phases():
    assert runs.phases_for({"type": "curation"}) == ["ingest", "assess", "write", "validate"]


def test_knowledge_base_rejects_run_machinery():
    with pytest.raises(runs.RunError, match="knowledge-base"):
        runs.phases_for({"type": "knowledge-base"})


def test_unknown_type_rejected():
    with pytest.raises(runs.RunError):
        runs.phases_for({"type": "hybrid"})


def test_run_start_for_knowledge_base_leaves_nothing_on_disk(tmp_path):
    wiki_root = tmp_path / "wiki"
    wiki_root.mkdir()
    with pytest.raises(runs.RunError):
        runs.start(wiki_root, {"type": "knowledge-base", "key": "kb"}, "wiki-kennis-ingest")
    assert not (wiki_root / ".work").exists()
