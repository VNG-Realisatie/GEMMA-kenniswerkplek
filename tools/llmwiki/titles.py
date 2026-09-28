"""Titel <-> bestandsnaam-mapping voor sync-wiki's (docs/onderbouwing.md 5.13).

Spaties blijven spaties; ':' wordt '§' (Windows staat geen ':' toe in
bestandsnamen); overige verboden tekens worden percent-gecodeerd; '/' wordt een
geneste map; een pagina met subpagina's krijgt haar eigen inhoud in '_index'.
De extensie '.wiki' is alleen voor het wikitext-contentmodel; css/js-pagina's
behouden hun eigen extensie. Bij een hoofdletterongevoelige botsing, een
gereserveerde naam of een pad langer dan 120 tekens krijgt het laatste segment
een hash-suffix; de exacte titel staat dan in het override-blokje van
revisies.json, nooit alleen af te leiden uit het pad.
"""
from __future__ import annotations

import re
import unicodedata

from . import hashing

FORBIDDEN_CHARS = '\\*?"<>|'
RESERVED_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}
MAX_SEGMENT_LENGTH = 120

NAMESPACE_CANONICAL = {
    0: "main",
    6: "file",
    8: "mediawiki",
    10: "template",
    14: "category",
}


def _content_model_extension(contentmodel: str) -> str:
    """Alleen het wikitext-contentmodel krijgt een toegevoegde extensie; een
    css/js-paginatitel bevat de extensie al (bv. 'MediaWiki:Common.css')."""
    return "" if contentmodel in ("sanitized-css", "javascript") else ".wiki"


def _encode_segment(segment: str) -> str:
    segment = unicodedata.normalize("NFC", segment)
    encoded = []
    for ch in segment:
        if ch == ":":
            encoded.append("§")
        elif ch in FORBIDDEN_CHARS:
            encoded.append(f"%{ord(ch):02X}")
        else:
            encoded.append(ch)
    return "".join(encoded)


def _needs_suffix(segment: str) -> bool:
    stem = segment.rsplit(".", 1)[0] if "." in segment else segment
    return stem.upper() in RESERVED_NAMES or len(segment) > MAX_SEGMENT_LENGTH


def title_to_path(
    title: str, namespace: int, contentmodel: str = "wikitext", categorie_pad: list[str] | None = None
) -> str:
    """Zet een MediaWiki-titel om naar een pad relatief aan content/.

    `categorie_pad` (alleen bij `content.layout: category`, zie docs/kluswijzer.md
    Klus 4) nestelt de categoriehiërarchie ónder de naamruimte-map, bv.
    ['Landingspagina'] -> 'main/Landingspagina/Wat is GEMMA.wiki'. Zonder
    categorie_pad ongewijzigd t.o.v. `content.layout: namespace`.
    """
    ns_folder = NAMESPACE_CANONICAL.get(namespace, f"ns{namespace}")
    if ":" in title:
        _, _, rest = title.partition(":")
    else:
        rest = title
    segments = [_encode_segment(s) for s in rest.split("/") if s]
    if not segments:
        segments = ["_index"]

    ext = _content_model_extension(contentmodel)
    last = segments[-1] + ext
    if _needs_suffix(last):
        digest = hashing.short(hashing.hash_text(title))
        stem = segments[-1][: MAX_SEGMENT_LENGTH - len(digest) - 1]
        last = f"{stem}~{digest}{ext}"
    segments[-1] = last

    categorie_segments = [_encode_segment(c) for c in (categorie_pad or [])]
    return "/".join([ns_folder, *categorie_segments, *segments])


def apply_index_convention(paths_by_title: dict[str, str]) -> dict[str, str]:
    """Een pagina die zelf ook subpagina's heeft, krijgt haar inhoud in
    '_index' binnen de map van haar eigen segmenten, in plaats van naast die map
    te staan (bv. 'main/Foo.wiki' + 'main/Foo/Bar.wiki' -> 'main/Foo/_index.wiki'
    + 'main/Foo/Bar.wiki')."""
    result = dict(paths_by_title)
    stems = set()
    for path in paths_by_title.values():
        if "/" in path:
            stems.add(path.rsplit("/", 1)[0])
    for title, path in paths_by_title.items():
        if "." not in path:
            continue
        folder = path.rsplit(".", 1)[0]
        if folder in stems:
            ext = path.rsplit(".", 1)[1]
            result[title] = f"{folder}/_index.{ext}"
    return result
