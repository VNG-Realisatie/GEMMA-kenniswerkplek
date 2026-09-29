from llmwiki import frontmatter, lint


def test_sources_immutable_flags_modified_raw_file():
    errors = lint.check_sources_immutable(None, ["sources/raw/2026-test.md", "docs/kluswijzer.md"])
    assert len(errors) == 1
    assert "sources/raw/2026-test.md" in errors[0]


def test_goedgekeurd_guard_flags_manual_status_change(repo):
    root, wiki_root = repo
    page_path = wiki_root / "kandidaten" / "kandidaat-manual.md"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page = frontmatter.Page(
        meta={"id": "kandidaat-manual", "type": "kandidaat", "status": "goedgekeurd"},
        body="Handmatig op goedgekeurd gezet, zonder promote apply.\n",
    )
    frontmatter.write(page_path, page)

    errors = lint.check_goedgekeurd_guard(root)
    assert any("kandidaat-manual" in e for e in errors)


def test_goedgekeurd_guard_accepts_page_recorded_in_log(repo):
    from llmwiki import hashing, logbook

    root, wiki_root = repo
    page_path = wiki_root / "kandidaten" / "kandidaat-ok.md"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page = frontmatter.Page(
        meta={"id": "kandidaat-ok", "type": "kandidaat", "status": "goedgekeurd"},
        body="Via promote apply.\n",
    )
    frontmatter.write(page_path, page)
    content_hash = hashing.hash_text(page_path.read_text(encoding="utf-8"))
    logbook.append_log(wiki_root, "promote", "kandidaat-ok", "M. Jansen", content_hash)

    errors = lint.check_goedgekeurd_guard(root)
    assert errors == []


def test_goedgekeurd_guard_checks_nested_directories(repo):
    root, wiki_root = repo
    page_path = wiki_root / "kandidaten" / "taakveld" / "beleidsdomein" / "kandidaat-diep.md"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter.write(
        page_path,
        frontmatter.Page(meta={"id": "kandidaat-diep", "type": "kandidaat", "status": "goedgekeurd"}, body="x\n"),
    )
    errors = lint.check_goedgekeurd_guard(root)
    assert any("kandidaat-diep" in e for e in errors)
