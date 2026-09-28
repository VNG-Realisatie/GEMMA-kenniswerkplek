import json

import pytest

from llmwiki import paths, runs


def _set(wiki_root, path, content):
    (wiki_root / path).parent.mkdir(parents=True, exist_ok=True)
    (wiki_root / path).write_text(content, encoding="utf-8")


def test_run_start_sets_first_phase_pending(repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    state = runs.start(wiki_root, wiki_yaml, "wiki-update")
    assert runs.next_phase(state, wiki_yaml) == "ingest"
    assert state["fasen"]["promote"]["status"] == "pending"


def test_complete_out_of_order_is_rejected(repo, tmp_path):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    state = runs.start(wiki_root, wiki_yaml, "wiki-update")

    data = tmp_path / "assessment.json"
    data.write_text(json.dumps({"run": state["run_id"], "voorstellen": []}), encoding="utf-8")

    with pytest.raises(runs.RunError):
        runs.complete(wiki_root, wiki_yaml, state["run_id"], "assess", data)


def test_complete_ingest_then_assess(repo, tmp_path):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    state = runs.start(wiki_root, wiki_yaml, "wiki-update")
    run_id = state["run_id"]

    source_data = tmp_path / "source.json"
    source_data.write_text(json.dumps({"run": run_id, "bronnen": []}), encoding="utf-8")
    state = runs.complete(wiki_root, wiki_yaml, run_id, "ingest", source_data)
    assert state["fasen"]["ingest"]["status"] == "done"
    assert runs.next_phase(state, wiki_yaml) == "assess"

    assess_data = tmp_path / "assessment.json"
    assess_data.write_text(json.dumps({"run": run_id, "voorstellen": []}), encoding="utf-8")
    state = runs.complete(wiki_root, wiki_yaml, run_id, "assess", assess_data)
    assert runs.next_phase(state, wiki_yaml) == "write"


def test_abandon_leaves_nothing_outside_workdir(repo, tmp_path):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    state = runs.start(wiki_root, wiki_yaml, "wiki-update")
    run_id = state["run_id"]

    before = {p for p in wiki_root.rglob("*") if ".work" not in p.parts}

    runs.abandon(wiki_root, run_id)

    after = {p for p in wiki_root.rglob("*") if ".work" not in p.parts}
    assert before == after
    assert not runs.run_dir(wiki_root, run_id).exists()

    with pytest.raises(runs.RunError):
        runs.abandon(wiki_root, run_id)
