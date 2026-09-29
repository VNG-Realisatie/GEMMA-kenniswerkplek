from llmwiki import paths, sources, validate


def _write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_valid_page_has_no_errors(repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    page_path = wiki_root / "kandidaten" / "kandidaat-ok.md"
    _write(wiki_root / "onderwerpen" / "x.md", "---\nid: x\ntype: onderwerp\n---\n\nx\n")
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


def test_sync_page_has_no_frontmatter_requirement(tmp_path):
    wiki_yaml = {"type": "sync"}
    page_path = tmp_path / "content" / "main" / "Voorbeeld.wiki"
    _write(page_path, "Gewone wikitext zonder frontmatter.\n[[Categorie:Voorbeeld]]\n")
    errors = validate.validate_page(tmp_path, page_path, wiki_yaml)
    assert errors == []


def test_sync_page_empty_file_is_rejected(tmp_path):
    wiki_yaml = {"type": "sync"}
    page_path = tmp_path / "content" / "main" / "Leeg.wiki"
    _write(page_path, "\n")
    errors = validate.validate_page(tmp_path, page_path, wiki_yaml)
    assert any("leeg bestand" in e for e in errors)


def test_sync_page_leading_space_is_reported(tmp_path):
    wiki_yaml = {"type": "sync"}
    page_path = tmp_path / "content" / "main" / "Indent.wiki"
    _write(page_path, "Normale regel.\n indentatie per ongeluk\n")
    errors = validate.validate_page(tmp_path, page_path, wiki_yaml)
    assert any("preformatted" in e for e in errors)


def test_sync_page_leading_space_in_table_is_allowed(tmp_path):
    wiki_yaml = {"type": "sync"}
    page_path = tmp_path / "content" / "main" / "Tabel.wiki"
    _write(page_path, "{|\n |Cel 1\n|}\n")
    errors = validate.validate_page(tmp_path, page_path, wiki_yaml)
    assert errors == []


def test_dead_relative_link_is_reported(repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    page_path = wiki_root / "kandidaten" / "kandidaat-f.md"
    _write(page_path, "---\nid: kandidaat-f\ntype: kandidaat\nstatus: review\n---\n\nZie [weg](../kandidaten/bestaat-niet.md).\n")
    errors = validate.validate_page(wiki_root, page_path, wiki_yaml)
    assert any("niet-bestaand bestand" in e for e in errors)


def test_external_and_anchor_links_are_not_checked(repo):
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    page_path = wiki_root / "kandidaten" / "kandidaat-g.md"
    _write(
        page_path,
        "---\nid: kandidaat-g\ntype: kandidaat\nstatus: review\n---\n\n[a](https://example.org) [b](#kop) [c](mailto:x@y.nl)\n",
    )
    assert validate.validate_page(wiki_root, page_path, wiki_yaml) == []


def test_staged_page_is_checked_against_target_path(repo):
    """Een gestaged bestand met een vrije naam: id en links gelden t.o.v. het doelpad,
    en andere pagina's uit dezelfde changeset gelden als bestaand."""
    root, wiki_root = repo
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    staged = wiki_root / ".work" / "runs" / "r1" / "changeset" / "vrije-naam.md"
    _write(staged, "---\nid: kandidaat-h\ntype: kandidaat\nstatus: review\n---\n\nZie [i](kandidaat-i.md).\n")
    doel = (wiki_root / "kandidaten" / "kandidaat-h.md").resolve()
    ander = (wiki_root / "kandidaten" / "kandidaat-i.md").resolve()
    errors = validate.validate_page(wiki_root, staged, wiki_yaml, doelpad=doel, bestaande_paden={doel, ander})
    assert errors == []


def test_changeset_context_maps_staged_file(repo):
    import json

    root, wiki_root = repo
    run_dir = wiki_root / ".work" / "runs" / "r2"
    staged = run_dir / "changeset" / "x.md"
    _write(staged, "x")
    (run_dir / "changeset.json").write_text(
        json.dumps({"run": "r2", "paginas": [{"pad": "kandidaten/kandidaat-x.md", "staged_bestand": "x.md", "actie": "nieuw", "type": "kandidaat"}]}),
        encoding="utf-8",
    )
    doelpad, bestaande = validate.changeset_context(wiki_root, run_dir, staged)
    assert doelpad == (wiki_root / "kandidaten" / "kandidaat-x.md").resolve()
    assert doelpad in bestaande


def test_page_type_schema_is_applied_with_relative_ref(repo):
    import json

    import yaml

    root, wiki_root = repo
    (wiki_root / "schemas").mkdir()
    (wiki_root / "schemas" / "basis.schema.json").write_text(
        json.dumps({"$defs": {"naam": {"type": "string", "minLength": 1}}}), encoding="utf-8"
    )
    (wiki_root / "schemas" / "kandidaat.schema.json").write_text(
        json.dumps(
            {
                "type": "object",
                "required": ["naam"],
                "properties": {"naam": {"$ref": "basis.schema.json#/$defs/naam"}, "bijgewerkt": {"type": "string"}},
            }
        ),
        encoding="utf-8",
    )
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    wiki_yaml["page_types"]["kandidaat"]["schema"] = "schemas/kandidaat.schema.json"
    (wiki_root / "wiki.yaml").write_text(yaml.safe_dump(wiki_yaml), encoding="utf-8")

    goed = wiki_root / "kandidaten" / "kandidaat-j.md"
    _write(goed, "---\nid: kandidaat-j\ntype: kandidaat\nstatus: review\nnaam: J\nbijgewerkt: 2026-09-29\n---\n\nx\n")
    assert validate.validate_page(wiki_root, goed, wiki_yaml) == []

    fout = wiki_root / "kandidaten" / "kandidaat-k.md"
    _write(fout, "---\nid: kandidaat-k\ntype: kandidaat\nstatus: review\nnaam: ''\n---\n\nx\n")
    errors = validate.validate_page(wiki_root, fout, wiki_yaml)
    assert any("naam" in e for e in errors)
