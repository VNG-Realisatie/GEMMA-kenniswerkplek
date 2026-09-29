"""Bronbeheer: laag 1 (sources/raw, onveranderlijk) en laag 2 (sources/index, gedeelde intake)."""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from . import frontmatter, hashing

BRON_ID_PATTERN = re.compile(r"^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*$")


class SourceExistsError(RuntimeError):
    pass


class ConversionError(RuntimeError):
    pass


def _raw_dir(repo_root: Path) -> Path:
    return repo_root / "sources" / "raw"


def _index_dir(repo_root: Path) -> Path:
    return repo_root / "sources" / "index"


BRONTYPEN = ("wet", "informatiemodel", "beleid", "overig", "model")


def _convert_pdf(original: Path) -> str:
    try:
        import pymupdf4llm
    except ImportError as exc:
        raise ConversionError(
            "Pdf-conversie vereist de extra 'pdf': draai eenmalig 'uv sync --extra pdf', "
            "of lever zelf een Markdown-versie aan met --markdown <pad>."
        ) from exc
    return pymupdf4llm.to_markdown(str(original))


def _convert_to_markdown(original: Path, url: str = "") -> str:
    suffix = original.suffix.lower()
    if suffix in (".md", ".txt"):
        return original.read_text(encoding="utf-8")
    if suffix in (".html", ".htm"):
        from . import fetch

        return fetch.html_to_markdown(original.read_text(encoding="utf-8", errors="replace"), url)
    if suffix == ".pdf":
        return _convert_pdf(original)
    if shutil.which("pandoc"):
        result = subprocess.run(
            ["pandoc", str(original), "-t", "markdown"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return result.stdout
        raise ConversionError(f"pandoc kon {original} niet converteren: {result.stderr.strip()}")
    raise ConversionError(
        f"Geen conversie beschikbaar voor {original.suffix} en pandoc is niet geïnstalleerd. "
        "Lever zelf een Markdown-versie aan met --markdown <pad>, of installeer pandoc."
    )


def add(
    repo_root: Path,
    bron_id: str,
    original: Path,
    *,
    titel: str,
    tags: list[str],
    uitgever: str = "",
    datum: str = "",
    versie: str = "",
    samenvatting: str = "",
    markdown_override: Path | None = None,
    brontype: str = "",
    beschrijving: str = "",
    url: str = "",
    url_pagina: str = "",
    opgehaald: str = "",
) -> Path:
    if brontype and brontype not in BRONTYPEN:
        raise ValueError(f"Onbekend brontype '{brontype}'; kies uit {', '.join(BRONTYPEN)}")
    if not BRON_ID_PATTERN.match(bron_id):
        raise ValueError(
            f"Ongeldig bron-id '{bron_id}': verwacht '<jaar>-<uitgever>-<korte-titel>', kleine letters en koppeltekens"
        )
    raw_dir = _raw_dir(repo_root)
    index_dir = _index_dir(repo_root)
    raw_dir.mkdir(parents=True, exist_ok=True)
    index_dir.mkdir(parents=True, exist_ok=True)

    existing = list(raw_dir.glob(f"{bron_id}.*"))
    if existing:
        raise SourceExistsError(f"Bron-id '{bron_id}' bestaat al: {existing}")

    original = Path(original)
    # Eerst converteren, dan kopiëren: een mislukte conversie laat niets achter in sources/raw/.
    md_text = (
        markdown_override.read_text(encoding="utf-8") if markdown_override else _convert_to_markdown(original, url)
    )
    dest_original = raw_dir / f"{bron_id}{original.suffix.lower()}"
    shutil.copyfile(original, dest_original)
    dest_md = raw_dir / f"{bron_id}.md"
    if dest_md != dest_original:
        dest_md.write_text(md_text, encoding="utf-8", newline="\n")

    bron_hash = hashing.hash_file(dest_original)

    index_page = frontmatter.Page(
        meta={
            "id": bron_id,
            "titel": titel,
            "uitgever": uitgever,
            "datum": datum,
            "versie": versie,
            "pad": str(dest_original.relative_to(repo_root)),
            "hash": bron_hash,
            "tags": tags,
            **{
                key: value
                for key, value in {
                    "brontype": brontype,
                    "beschrijving": beschrijving,
                    "url": url,
                    "url_pagina": url_pagina,
                    "opgehaald": opgehaald,
                }.items()
                if value
            },
        },
        body=samenvatting or f"# {titel}\n\nNog geen samenvatting.\n",
    )
    index_path = index_dir / f"{bron_id}.md"
    frontmatter.write(index_path, index_page)
    return index_path


def read_index_entry(repo_root: Path, bron_id: str) -> dict:
    path = _index_dir(repo_root) / f"{bron_id}.md"
    if not path.exists():
        raise FileNotFoundError(str(path))
    return frontmatter.read(path).meta


def list_sources(repo_root: Path, tags: list[str] | None = None) -> list[dict]:
    index_dir = _index_dir(repo_root)
    if not index_dir.exists():
        return []
    results = []
    for path in sorted(index_dir.glob("*.md")):
        meta = frontmatter.read(path).meta
        if tags and not (set(meta.get("tags", [])) & set(tags)):
            continue
        results.append(meta)
    return results


def add_from_url(repo_root: Path, bron_id: str, url: str, workdir: Path, **kwargs) -> Path:
    """Haal een bron op via een URL en voeg haar toe (origineel + Markdown-conversie).

    Het origineel wordt eerst in `workdir` gezet (bijv. het kladblok), zodat bij een
    mislukte conversie niets in `sources/raw/` achterblijft.
    """
    from datetime import date

    from . import fetch

    opgehaald = fetch.fetch(url)
    workdir.mkdir(parents=True, exist_ok=True)
    tijdelijk = workdir / f"{bron_id}{fetch.extension_for(opgehaald)}"
    tijdelijk.write_bytes(opgehaald.inhoud)
    markdown_override = kwargs.pop("markdown_override", None)
    if markdown_override is None:
        md_path = workdir / f"{bron_id}.conversie.md"
        md_path.write_text(_convert_to_markdown(tijdelijk, url), encoding="utf-8")
        markdown_override = md_path
    return add(
        repo_root,
        bron_id,
        tijdelijk,
        url=url,
        opgehaald=kwargs.pop("opgehaald", "") or date.today().isoformat(),
        markdown_override=markdown_override,
        **kwargs,
    )
