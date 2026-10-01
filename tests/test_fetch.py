"""Bron ophalen: URL-resolutie, HTML→Markdown, brontype en URL-velden in de intake."""
import pytest

from llmwiki import fetch, sources


def test_ibabs_agenda_document_url_is_resolved():
    url = "https://utrecht.bestuurlijkeinformatie.nl/Agenda/Document/abc?documentId=D1&agendaItemId=A2"
    assert fetch.resolve_url(url) == (
        "https://utrecht.bestuurlijkeinformatie.nl/Document/LoadAgendaItemDocument/D1?agendaItemId=A2"
    )


def test_ibabs_reports_document_url_is_resolved():
    url = "https://utrecht.bestuurlijkeinformatie.nl/Reports/Document/xyz?documentId=D9"
    assert fetch.resolve_url(url) == "https://utrecht.bestuurlijkeinformatie.nl/Document/View/D9"


def test_other_urls_are_unchanged():
    assert fetch.resolve_url("https://example.org/pagina?documentId=1") == "https://example.org/pagina?documentId=1"


HTML = """<html><head><style>.x{}</style><script>var a=1;</script></head><body>
<nav><a href="/">Home</a></nav>
<h1>Verordening parkeren</h1>
<p>Artikel&nbsp;1   begrip.</p>
<ul><li>Eerste</li><li>Tweede</li></ul>
<p>Toon relaties in LiDO</p>
<p>Tekst&eacute;n blijven letterlijk.</p>
<p>Over deze website</p><p>Voettekst die weg moet.</p>
<footer>Copyright</footer>
</body></html>"""


def test_html_to_markdown_keeps_text_and_strips_noise():
    md = fetch.html_to_markdown(HTML)
    assert "# Verordening parkeren" in md
    assert "Artikel 1 begrip." in md
    assert "- Eerste" in md and "- Tweede" in md
    assert "Tekstén blijven letterlijk." in md
    assert "Home" not in md and "var a" not in md and "Copyright" not in md
    assert "Toon relaties in LiDO" not in md
    assert "Voettekst" not in md


def test_wetten_overheid_starts_at_first_chapter():
    html = "<p>Zoeken</p><p>Inhoudsopgave</p><h3>Hoofdstuk 1 Algemeen</h3><p>Artikel 1</p>"
    md = fetch.html_to_markdown(html, "https://wetten.overheid.nl/BWBR0001")
    assert md.startswith("### Hoofdstuk 1 Algemeen")
    assert "Inhoudsopgave" not in md


def test_add_html_source_stores_original_markdown_and_metadata(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "pagina.html"
    original.write_text(HTML, encoding="utf-8")
    sources.add(
        root, "2026-utrecht-parkeren", original, titel="Parkeren", tags=["demo"],
        brontype="wet", url="https://example.org/parkeren", opgehaald="2026-09-29",
    )
    assert (root / "sources" / "raw" / "2026-utrecht-parkeren.html").exists()
    assert "# Verordening parkeren" in (root / "sources" / "raw" / "2026-utrecht-parkeren.md").read_text(encoding="utf-8")
    entry = sources.read_index_entry(root, "2026-utrecht-parkeren")
    assert entry["brontype"] == "wet"
    assert entry["url"] == "https://example.org/parkeren"


def test_unknown_brontype_is_rejected(tmp_path, repo):
    root, wiki_root = repo
    original = tmp_path / "x.md"
    original.write_text("# x\n", encoding="utf-8")
    with pytest.raises(ValueError, match="brontype"):
        sources.add(root, "2026-x-bron", original, titel="x", tags=["demo"], brontype="roman")


def test_failed_pdf_conversion_leaves_nothing_in_raw(tmp_path, repo, monkeypatch):
    root, wiki_root = repo
    original = tmp_path / "doc.pdf"
    original.write_bytes(b"%PDF-1.4 niet echt")

    def kapot(_path):
        raise sources.ConversionError("geen pdf-extra")

    monkeypatch.setattr(sources, "_convert_pdf", kapot)
    with pytest.raises(sources.ConversionError):
        sources.add(root, "2026-x-pdf", original, titel="x", tags=["demo"])
    assert not list((root / "sources" / "raw").glob("2026-x-pdf*"))


def test_add_from_url_uses_fetched_content(tmp_path, repo, monkeypatch):
    root, wiki_root = repo
    monkeypatch.setattr(
        fetch, "fetch", lambda url: fetch.Opgehaald(inhoud=HTML.encode(), content_type="text/html", url=url)
    )
    sources.add_from_url(
        root, "2026-web-parkeren", "https://example.org/p", tmp_path / "werk", titel="P", tags=["demo"], brontype="beleid"
    )
    entry = sources.read_index_entry(root, "2026-web-parkeren")
    assert entry["url"] == "https://example.org/p"
    assert entry["opgehaald"]
    assert (root / "sources" / "raw" / "2026-web-parkeren.html").exists()


def test_raw_text_download_keeps_extension_from_url():
    xml = fetch.Opgehaald(b"<model/>", "text/plain", "https://raw.githubusercontent.com/org/repo/main/export/Over%20GEMMA.xml")
    assert fetch.extension_for(xml) == ".xml"
    tekst = fetch.Opgehaald(b"tekst", "text/plain", "https://example.org/bestand")
    assert fetch.extension_for(tekst) == ".txt"
