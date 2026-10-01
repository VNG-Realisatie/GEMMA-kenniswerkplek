"""Een bron ophalen via een URL en HTML deterministisch omzetten naar Markdown.

De omzetting bewaart de tekst letterlijk: alleen opmaakruis (scripts, stijlen,
navigatie, voettekst, bekende knoppenteksten) verdwijnt. Er wordt niets samengevat
of herschreven; een bron in `sources/raw/` moet een getrouwe kopie zijn.
"""
from __future__ import annotations

import re
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

USER_AGENT = "llmwiki-source-add/0.1 (+https://github.com/)"

# Tags waarvan de hele inhoud wordt overgeslagen.
SKIP_TAGS = {"script", "style", "nav", "footer", "noscript", "template"}
HEADING_TAGS = {"h1": "#", "h2": "##", "h3": "###", "h4": "####", "h5": "#####", "h6": "######"}
BLOCK_TAGS = {"p", "div", "section", "article", "table", "tr", "ul", "ol", "blockquote", "main"}

# Regels die als geheel worden verwijderd (knoppen- en navigatieteksten, o.a. wetten.overheid.nl).
NOISE_LINES = {
    "Toon relaties in LiDO",
    "Maak een permanente link",
    "Toon wetstechnische informatie",
    "Druk het regelingonderdeel af",
    "Sla het regelingonderdeel op",
    "-",
}
# Vanaf deze markers is de rest voettekst.
FOOTER_MARKERS = ("Permanente link naar versie", "Exporteer regeling", "Keuze afdrukken", "Over deze website")


class FetchError(RuntimeError):
    pass


@dataclass
class Opgehaald:
    inhoud: bytes
    content_type: str
    url: str


# Extensies van tekstbestanden die als text/plain worden geserveerd, maar hun eigen extensie houden.
TEKST_EXTENSIES = (".xml", ".json", ".csv", ".md", ".txt", ".yaml", ".yml")


def resolve_url(url: str) -> str:
    """Zet bekende weergave-URL's om naar de directe download-URL.

    iBabs (`*.bestuurlijkeinformatie.nl`): documentpagina's zijn niet direct te downloaden.
    - `/Agenda/Document/{id}?documentId=X&agendaItemId=Y` → `/Document/LoadAgendaItemDocument/X?agendaItemId=Y`
    - `/Reports/Document/{id}?documentId=X` → `/Document/View/X`
    """
    parsed = urlparse(url)
    if not parsed.netloc.endswith("bestuurlijkeinformatie.nl"):
        return url
    query = parse_qs(parsed.query)
    document_id = (query.get("documentId") or [None])[0]
    if not document_id:
        return url
    base = f"{parsed.scheme}://{parsed.netloc}"
    if parsed.path.startswith("/Agenda/Document/"):
        agenda_item = (query.get("agendaItemId") or [None])[0]
        suffix = f"?agendaItemId={agenda_item}" if agenda_item else ""
        return f"{base}/Document/LoadAgendaItemDocument/{document_id}{suffix}"
    if parsed.path.startswith("/Reports/Document/"):
        return f"{base}/Document/View/{document_id}"
    return url


def fetch(url: str, timeout: int = 60) -> Opgehaald:
    resolved = resolve_url(url)
    # Accept en Accept-Language: servers die op inhoudstype of taal onderhandelen (bijv. het Publicatiebureau van de EU)
    # leveren anders metadata of een andere taal in plaats van de tekst.
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
        "Accept-Language": "nl,en;q=0.5",
    }
    request = urllib.request.Request(resolved, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 (bewust: bron ophalen)
            return Opgehaald(
                inhoud=response.read(),
                content_type=response.headers.get_content_type(),
                url=response.geturl(),
            )
    except OSError as exc:
        raise FetchError(f"Ophalen van {resolved} mislukt: {exc}") from exc


def extension_for(opgehaald: Opgehaald) -> str:
    if opgehaald.content_type == "application/pdf" or opgehaald.inhoud[:5] == b"%PDF-":
        return ".pdf"
    if opgehaald.content_type in ("text/markdown", "text/x-markdown"):
        return ".md"
    if opgehaald.content_type == "text/plain":
        # Een ruwe download (bijv. raw.githubusercontent.com) is altijd text/plain; neem dan de extensie uit de URL.
        url_ext = Path(urlparse(opgehaald.url).path).suffix.lower()
        return url_ext if url_ext in TEKST_EXTENSIES else ".txt"
    return ".html"


class _MarkdownParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in HEADING_TAGS:
            self.parts.append(f"\n\n{HEADING_TAGS[tag]} ")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "br":
            self.parts.append("\n")
        elif tag in BLOCK_TAGS:
            self.parts.append("\n\n")
        elif tag in ("td", "th"):
            self.parts.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag in HEADING_TAGS or tag in BLOCK_TAGS:
            self.parts.append("\n\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)


def html_to_markdown(html: str, url: str = "") -> str:
    parser = _MarkdownParser()
    parser.feed(html)
    parser.close()
    text = "".join(parser.parts)

    lines = []
    for raw_line in text.splitlines():
        line = re.sub(r"[ \t ]+", " ", raw_line).strip()
        if line in NOISE_LINES or re.fullmatch(r"-\s*", line):
            continue
        if any(line.startswith(marker) for marker in FOOTER_MARKERS):
            break
        lines.append(line)

    if "wetten.overheid.nl" in url:
        for i, line in enumerate(lines):
            if line.startswith("### Hoofdstuk"):
                lines = lines[i:]
                break

    result = "\n".join(lines)
    result = re.sub(r"\n{3,}", "\n\n", result).strip()
    return result + "\n"
