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


def test_inhoud_koppen_regels_en_woorden(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("# Wet\n\nEen twee.\n\n## Art. 1\n\nDrie vier vijf.\n\n```\n# geen kop\n```\n\n## Art. 2\n\nZes.\n", encoding="utf-8")
    sources.add(root, "2026-test-bron", original, titel="Testbron", tags=["demo"])

    totaal, koppen = sources.inhoud(root, "2026-test-bron")
    assert [(k["kop"], k["regel"]) for k in koppen] == [("Wet", 1), ("Art. 1", 5), ("Art. 2", 13)]
    assert koppen[1]["woorden"] == 8  # tekst plus het codeblok (met de ```-regels) tot art. 2
    assert koppen[0]["woorden"] == totaal - 2
    assert "| → Art. 2 | 13 |" in sources.inhoud_markdown(root, "2026-test-bron")


def test_bronregel_linkt_relatief_naar_laag_1(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("# Testbron\n", encoding="utf-8")
    sources.add(root, "2026-test-bron", original, titel="Testbron", tags=["demo"])

    pagina = root / "wikis" / "demo" / "bronnen" / "onderwerp" / "2026-test-bron.md"
    regel = sources.bronregel(root, "2026-test-bron", pagina)
    assert regel == "Bron: [tekst](../../../../sources/raw/2026-test-bron.md)"


def test_niveau_telt_vanaf_hoogste_kop(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("### Hoofdstuk I\n\n#### Artikel 1\n\nTekst.\n", encoding="utf-8")
    sources.add(root, "2026-test-bron", original, titel="Testbron", tags=["demo"])

    _, koppen = sources.inhoud(root, "2026-test-bron", max_niveau=1)
    assert [k["kop"] for k in koppen] == ["Hoofdstuk I"]


def test_schrijf_inhoud_en_bronregel_zijn_herhaalbaar(tmp_path, repo):
    from llmwiki import frontmatter

    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("# Testbron\n\nTekst.\n", encoding="utf-8")
    sources.add(root, "2026-test-bron", original, titel="Testbron", tags=["demo"])

    index = sources.schrijf_inhoud(root, "2026-test-bron")
    sources.schrijf_inhoud(root, "2026-test-bron")
    assert frontmatter.read(index).body.count("## Inhoud") == 1

    pagina = root / "wikis" / "demo" / "bronnen" / "2026-test-bron.md"
    pagina.parent.mkdir(parents=True, exist_ok=True)
    frontmatter.write(pagina, frontmatter.Page(meta={"id": "2026-test-bron"}, body="# Testbron\n\n## Samenvatting\n\nTekst.\n"))
    sources.schrijf_bronregel(root, "2026-test-bron", pagina)
    sources.schrijf_bronregel(root, "2026-test-bron", pagina)
    assert frontmatter.read(pagina).body.strip() == "# Testbron\n\nBron: [tekst](../../../sources/raw/2026-test-bron.md)\n\n## Samenvatting\n\nTekst."


def test_add_zet_inhoud_in_de_index(tmp_path, repo):
    from llmwiki import frontmatter

    root, wiki_root = repo
    original = tmp_path / "input.md"
    original.write_text("# Testbron\n\n## Deel 1\n\nTekst.\n", encoding="utf-8")
    index = sources.add(root, "2026-test-bron", original, titel="Testbron", tags=["demo"])
    body = frontmatter.read(index).body
    assert "Index nog niet gevuld" in body and "| → Deel 1 | 3 | 1 |" in body
