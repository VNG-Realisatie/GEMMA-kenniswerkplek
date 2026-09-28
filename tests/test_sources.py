import pytest

from llmwiki import sources


def test_add_source_creates_raw_and_index(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("# Testbron\n\nInhoud.\n", encoding="utf-8")

    index_path = sources.add(
        root,
        "2026-test-bron",
        original,
        titel="Testbron",
        tags=["demo"],
    )

    assert index_path.exists()
    assert (root / "sources" / "raw" / "2026-test-bron.md").exists()
    entry = sources.read_index_entry(root, "2026-test-bron")
    assert entry["titel"] == "Testbron"
    assert entry["tags"] == ["demo"]


def test_add_source_rejects_duplicate_id(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("# Testbron\n", encoding="utf-8")
    sources.add(root, "2026-test-bron", original, titel="Testbron", tags=["demo"])

    with pytest.raises(sources.SourceExistsError):
        sources.add(root, "2026-test-bron", original, titel="Testbron", tags=["demo"])


def test_add_source_rejects_invalid_id(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("# Testbron\n", encoding="utf-8")
    with pytest.raises(ValueError):
        sources.add(root, "Niet Geldig ID", original, titel="Testbron", tags=["demo"])


def test_list_sources_filters_by_tag(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("# Testbron\n", encoding="utf-8")
    sources.add(root, "2026-test-a", original, titel="A", tags=["demo"])
    sources.add(root, "2026-test-b", original, titel="B", tags=["ander-thema"])

    demo_only = sources.list_sources(root, tags=["demo"])
    assert [e["id"] for e in demo_only] == ["2026-test-a"]

    all_sources = sources.list_sources(root)
    assert {e["id"] for e in all_sources} == {"2026-test-a", "2026-test-b"}
