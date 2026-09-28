import json

import pytest

from llmwiki import frontmatter, gate, paths, runs


KANDIDAAT_CONTENT = """---
id: kandidaat-test
type: kandidaat
status: review
onderwerp: demo-onderwerp
bronnen: []
---

# Kandidaat test

Een testkandidaat.
"""


def _run_through_validate(wiki_root, wiki_yaml) -> str:
    state = runs.start(wiki_root, wiki_yaml, "wiki-update")
    run_id = state["run_id"]
    rdir = runs.run_dir(wiki_root, run_id)

    _complete(wiki_root, wiki_yaml, run_id, "ingest", {"run": run_id, "bronnen": []})
    _complete(
        wiki_root,
        wiki_yaml,
        run_id,
        "assess",
        {
            "run": run_id,
            "voorstellen": [
                {
                    "doel": "kandidaten/kandidaat-test.md",
                    "soort": "nieuw",
                    "motivering": "test",
                    "bronnen": [],
                }
            ],
        },
    )

    staged = rdir / "changeset" / "kandidaat-test.md"
    staged.write_text(KANDIDAAT_CONTENT, encoding="utf-8")
    _complete(
        wiki_root,
        wiki_yaml,
        run_id,
        "write",
        {
            "run": run_id,
            "paginas": [
                {
                    "pad": "kandidaten/kandidaat-test.md",
                    "staged_bestand": "kandidaat-test.md",
                    "actie": "nieuw",
                    "type": "kandidaat",
                }
            ],
        },
    )

    _complete(
        wiki_root,
        wiki_yaml,
        run_id,
        "validate",
        {"run": run_id, "controles": [{"naam": "frontmatter", "resultaat": "ok", "ernst": "info"}]},
    )
    return run_id


def _complete(wiki_root, wiki_yaml, run_id, phase, data, tmp_dir=None):
    import tempfile
    from pathlib import Path

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(data, fh)
        path = Path(fh.name)
    runs.complete(wiki_root, wiki_yaml, run_id, phase, path)
    path.unlink()


def test_plan_then_apply_with_akkoord_succeeds(make_repo):
    root, wiki_root = make_repo(approval="chat")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_through_validate(wiki_root, wiki_yaml)

    voorstel_path = gate.plan(wiki_root, wiki_yaml, run_id)
    assert voorstel_path.exists()

    gate.apply(wiki_root, wiki_yaml, run_id, akkoord_woord="AKKOORD")

    result = frontmatter.read(wiki_root / "kandidaten" / "kandidaat-test.md")
    assert result.meta["status"] == "goedgekeurd"
    log_text = (wiki_root / "log.md").read_text(encoding="utf-8")
    assert "kandidaat-test" in log_text


def test_apply_rejects_wrong_word(make_repo):
    root, wiki_root = make_repo(approval="chat")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_through_validate(wiki_root, wiki_yaml)
    gate.plan(wiki_root, wiki_yaml, run_id)

    with pytest.raises(gate.GateError):
        gate.apply(wiki_root, wiki_yaml, run_id, akkoord_woord="Prima")

    assert not (wiki_root / "kandidaten" / "kandidaat-test.md").exists()


def test_apply_document_mode_requires_ja(make_repo):
    root, wiki_root = make_repo(approval="document")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_through_validate(wiki_root, wiki_yaml)
    gate.plan(wiki_root, wiki_yaml, run_id)

    with pytest.raises(gate.GateError):
        gate.apply(wiki_root, wiki_yaml, run_id)


def test_apply_document_mode_requires_naam(make_repo):
    root, wiki_root = make_repo(approval="document")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_through_validate(wiki_root, wiki_yaml)
    gate.plan(wiki_root, wiki_yaml, run_id)

    voorstel_path = wiki_root / "voorstellen" / f"{run_id}.md"
    page = frontmatter.read(voorstel_path)
    page.meta["akkoord_voor_publicatie"] = "ja"
    page.meta["beoordeeld_door"] = ""
    frontmatter.write(voorstel_path, page)

    with pytest.raises(gate.GateError):
        gate.apply(wiki_root, wiki_yaml, run_id)


def test_apply_document_mode_rejects_stale_plan_hash(make_repo):
    root, wiki_root = make_repo(approval="document")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_through_validate(wiki_root, wiki_yaml)
    gate.plan(wiki_root, wiki_yaml, run_id)

    voorstel_path = wiki_root / "voorstellen" / f"{run_id}.md"
    page = frontmatter.read(voorstel_path)
    page.meta["akkoord_voor_publicatie"] = "ja"
    page.meta["beoordeeld_door"] = "M. Jansen"
    page.meta["plan_hash"] = "verouderd0"
    frontmatter.write(voorstel_path, page)

    with pytest.raises(gate.GateError):
        gate.apply(wiki_root, wiki_yaml, run_id)


def test_apply_document_mode_succeeds_with_valid_approval(make_repo):
    root, wiki_root = make_repo(approval="document")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_through_validate(wiki_root, wiki_yaml)
    gate.plan(wiki_root, wiki_yaml, run_id)

    voorstel_path = wiki_root / "voorstellen" / f"{run_id}.md"
    page = frontmatter.read(voorstel_path)
    page.meta["akkoord_voor_publicatie"] = "ja"
    page.meta["beoordeeld_door"] = "M. Jansen"
    frontmatter.write(voorstel_path, page)

    gate.apply(wiki_root, wiki_yaml, run_id)
    result = frontmatter.read(wiki_root / "kandidaten" / "kandidaat-test.md")
    assert result.meta["status"] == "goedgekeurd"


def test_apply_detects_page_changed_since_plan(make_repo):
    root, wiki_root = make_repo(approval="chat")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_through_validate(wiki_root, wiki_yaml)
    gate.plan(wiki_root, wiki_yaml, run_id)

    # Simuleer dat de pagina in de werkboom is aangepast ná het maken van het plan.
    conflicting = wiki_root / "kandidaten" / "kandidaat-test.md"
    conflicting.parent.mkdir(parents=True, exist_ok=True)
    conflicting.write_text(KANDIDAAT_CONTENT + "\nExtra regel.\n", encoding="utf-8")

    with pytest.raises(gate.GateError):
        gate.apply(wiki_root, wiki_yaml, run_id, akkoord_woord="AKKOORD")


def test_plan_rejects_when_validation_has_errors(make_repo):
    root, wiki_root = make_repo(approval="chat")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    state = runs.start(wiki_root, wiki_yaml, "wiki-update")
    run_id = state["run_id"]
    rdir = runs.run_dir(wiki_root, run_id)

    _complete(wiki_root, wiki_yaml, run_id, "ingest", {"run": run_id, "bronnen": []})
    _complete(wiki_root, wiki_yaml, run_id, "assess", {"run": run_id, "voorstellen": []})
    staged = rdir / "changeset" / "kandidaat-test.md"
    staged.write_text(KANDIDAAT_CONTENT, encoding="utf-8")
    _complete(
        wiki_root,
        wiki_yaml,
        run_id,
        "write",
        {"run": run_id, "paginas": [{"pad": "kandidaten/kandidaat-test.md", "staged_bestand": "kandidaat-test.md", "actie": "nieuw", "type": "kandidaat"}]},
    )
    _complete(
        wiki_root,
        wiki_yaml,
        run_id,
        "validate",
        {"run": run_id, "controles": [{"naam": "frontmatter", "resultaat": "fout", "ernst": "fout", "melding": "test"}]},
    )

    with pytest.raises(gate.GateError):
        gate.plan(wiki_root, wiki_yaml, run_id)
