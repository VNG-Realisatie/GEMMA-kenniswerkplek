from llmwiki import paths, sources, validate


def _write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_valid_page_has_no_errors(repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    page_path = wiki_root / "kandidaten" / "kandidaat-ok.md"
    _write(
        page_path,
        "---\nid: kandidaat-ok\ntype: kandidaat\nstatus: review\nbronnen: []\n---\n\nInhoud met [link](../onderwerpen/x.md).\n",
    )
    errors = validate.validate_page(wiki_root, page_path, wiki_yaml)
    assert errors == []


def test_id_mismatch_is_reported(repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    page_path = wiki_root / "kandidaten" / "kandidaat-a.md"
    _write(page_path, "---\nid: kandidaat-b\ntype: kandidaat\nstatus: review\n---\n\nx\n")
    errors = validate.validate_page(wiki_root, page_path, wiki_yaml)
    assert any("komt niet overeen" in e for e in errors)


def test_wikilink_is_rejected(repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    page_path = wiki_root / "kandidaten" / "kandidaat-c.md"
    _write(page_path, "---\nid: kandidaat-c\ntype: kandidaat\nstatus: review\n---\n\nZie [[Andere pagina]].\n")
    errors = validate.validate_page(wiki_root, page_path, wiki_yaml)
    assert any("wikilinks" in e for e in errors)


def test_bron_outside_scope_is_rejected(tmp_path, repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    original = tmp_path / "input.md"
    original.write_text("# Bron\n", encoding="utf-8")
    sources.add(root, "2026-ander-thema", original, titel="Ander thema", tags=["ander-thema"])

    page_path = wiki_root / "kandidaten" / "kandidaat-d.md"
    _write(
        page_path,
        "---\nid: kandidaat-d\ntype: kandidaat\nstatus: review\nbronnen: [2026-ander-thema]\n---\n\nx\n",
    )
    errors = validate.validate_page(wiki_root, page_path, wiki_yaml)
    assert any("buiten de scope" in e for e in errors)


def test_unknown_bron_is_rejected(repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    page_path = wiki_root / "kandidaten" / "kandidaat-e.md"
    _write(
        page_path,
        "---\nid: kandidaat-e\ntype: kandidaat\nstatus: review\nbronnen: [onbestaand-id]\n---\n\nx\n",
    )
    errors = validate.validate_page(wiki_root, page_path, wiki_yaml)
    assert any("bestaat niet" in e for e in errors)
