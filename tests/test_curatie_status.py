"""Promotie: alleen `review` wordt `goedgekeurd`; `kandidaat` blijft staan; gestaged
`goedgekeurd` wordt geweigerd. Plus: onderwerpmap uit wiki.yaml en bronvoorrang."""
import json
import tempfile
from pathlib import Path

import pytest
import yaml

from llmwiki import frontmatter, gate, paths, runs, sources


def _page(page_id: str, status: str) -> str:
    return f"---\nid: {page_id}\ntype: kandidaat\nstatus: {status}\nbronnen: []\n---\n\n# {page_id}\n"


def _complete(wiki_root, wiki_yaml, run_id, phase, data):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(data, fh)
        path = Path(fh.name)
    runs.complete(wiki_root, wiki_yaml, run_id, phase, path)
    path.unlink()


def _run_with_pages(wiki_root, wiki_yaml, pages: dict[str, str]) -> str:
    run_id = runs.start(wiki_root, wiki_yaml, "wiki-update")["run_id"]
    rdir = runs.run_dir(wiki_root, run_id)
    _complete(wiki_root, wiki_yaml, run_id, "ingest", {"run": run_id, "bronnen": []})
    _complete(wiki_root, wiki_yaml, run_id, "assess", {"run": run_id, "voorstellen": []})
    entries = []
    for page_id, status in pages.items():
        (rdir / "changeset" / f"{page_id}.md").write_text(_page(page_id, status), encoding="utf-8")
        entries.append({"pad": f"kandidaten/{page_id}.md", "staged_bestand": f"{page_id}.md", "actie": "nieuw", "type": "kandidaat"})
    _complete(wiki_root, wiki_yaml, run_id, "write", {"run": run_id, "paginas": entries})
    _complete(
        wiki_root, wiki_yaml, run_id, "validate",
        {"run": run_id, "controles": [{"naam": "frontmatter", "resultaat": "ok", "ernst": "info"}]},
    )
    return run_id


def test_only_review_pages_are_approved(make_repo):
    root, wiki_root = make_repo(approval="chat")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_with_pages(wiki_root, wiki_yaml, {"klaar": "review", "twijfel": "kandidaat"})

    voorstel = gate.plan(wiki_root, wiki_yaml, run_id)
    body = voorstel.read_text(encoding="utf-8")
    assert "Wordt goedgekeurd" in body and "kandidaten/klaar.md" in body

    gate.apply(wiki_root, wiki_yaml, run_id, akkoord_woord="AKKOORD")

    assert frontmatter.read(wiki_root / "kandidaten" / "klaar.md").meta["status"] == "goedgekeurd"
    assert frontmatter.read(wiki_root / "kandidaten" / "twijfel.md").meta["status"] == "kandidaat"
    log_text = (wiki_root / "log.md").read_text(encoding="utf-8")
    assert "| klaar |" in log_text
    assert "| twijfel |" not in log_text


def test_staged_goedgekeurd_is_rejected(make_repo):
    root, wiki_root = make_repo(approval="chat")
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = _run_with_pages(wiki_root, wiki_yaml, {"zelf-goedgekeurd": "goedgekeurd"})
    with pytest.raises(gate.GateError, match="goedgekeurd"):
        gate.plan(wiki_root, wiki_yaml, run_id)


def _set_wiki_yaml(wiki_root, **updates):
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    wiki_yaml.update(updates)
    (wiki_root / "wiki.yaml").write_text(yaml.safe_dump(wiki_yaml, sort_keys=False), encoding="utf-8")
    return wiki_yaml


def _add_source(root, tmp_path, bron_id, brontype):
    original = tmp_path / f"{bron_id}.md"
    original.write_text(f"# {bron_id}\n", encoding="utf-8")
    sources.add(root, bron_id, original, titel=bron_id, tags=["demo"], brontype=brontype)


def test_onderwerp_dir_comes_from_page_types(repo):
    root, wiki_root = repo
    page_types = paths.load_wiki_yaml(wiki_root)["page_types"]
    page_types["onderwerp"]["dir"] = "begrippen"
    wiki_yaml = _set_wiki_yaml(wiki_root, page_types=page_types)
    (wiki_root / "begrippen").mkdir()
    (wiki_root / "begrippen" / "vergunningen.md").write_text(
        "---\nid: vergunningen\ntype: onderwerp\nbronnen: []\n---\n\nx\n", encoding="utf-8"
    )
    state = runs.start(wiki_root, wiki_yaml, "wiki-update", onderwerp="vergunningen")
    assert state["onderwerp"] == "vergunningen"


def test_bronnen_are_ordered_by_bronvoorrang(repo, tmp_path):
    root, wiki_root = repo
    _add_source(root, tmp_path, "2026-gemeente-nota", "beleid")
    _add_source(root, tmp_path, "2026-vng-ggm", "informatiemodel")
    _add_source(root, tmp_path, "2026-overheid-wet", "rijksregelgeving")
    wiki_yaml = _set_wiki_yaml(wiki_root, bronvoorrang=["rijksregelgeving", "informatiemodel", "beleid", "overig"])
    (wiki_root / "onderwerpen" / "demo.md").write_text(
        "---\nid: demo\ntype: onderwerp\nbronnen: [2026-gemeente-nota, onbekend-id, 2026-vng-ggm, 2026-overheid-wet]\n---\n\nx\n",
        encoding="utf-8",
    )
    state = runs.start(wiki_root, wiki_yaml, "wiki-update", onderwerp="demo")
    assert state["bronnen"] == ["2026-overheid-wet", "2026-vng-ggm", "2026-gemeente-nota", "onbekend-id"]


def test_without_bronvoorrang_order_is_kept(repo, tmp_path):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    assert runs.order_by_bronvoorrang(wiki_root, wiki_yaml, ["b", "a"]) == ["b", "a"]
