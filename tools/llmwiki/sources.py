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
            "Pdf-conversie vereist de groep 'pdf': draai 'uv sync', "
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
            "pad": dest_original.relative_to(repo_root).as_posix(),
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
        body=samenvatting or f"# {titel}\n\nIndex nog niet gevuld: volg skill wiki-intake.\n",
    )
    index_path = index_dir / f"{bron_id}.md"
    frontmatter.write(index_path, index_page)
    if dest_md.exists():
        schrijf_inhoud(repo_root, bron_id)
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


# --- Laag 1 vanuit een pagina: herleidbaarheid en inhoudsopgave ---


def raw_paden(repo_root: Path, bron_id: str) -> tuple[Path | None, Path | None]:
    """(Markdown-versie, origineel) van een bron in sources/raw/; None als het bestand ontbreekt.

    Is het origineel zelf Markdown, dan is het origineel None (het is de Markdown-versie).
    """
    meta = read_index_entry(repo_root, bron_id)
    md = _raw_dir(repo_root) / f"{bron_id}.md"
    origineel = repo_root / meta["pad"] if meta.get("pad") else None
    return (md if md.exists() else None,
            origineel if origineel and origineel != md and origineel.exists() else None)


def bronregel(repo_root: Path, bron_id: str, van: Path) -> str:
    """Linkregel van een pagina (domein-lens) naar laag 1: de tekst, het origineel en de online bron.

    `van` is het pad van de pagina waarin de regel komt; de links zijn relatief daaraan.
    """
    import os

    meta = read_index_entry(repo_root, bron_id)
    md, origineel = raw_paden(repo_root, bron_id)
    if md is None and origineel is None:
        raise FileNotFoundError(f"bron '{bron_id}' heeft geen bestand in sources/raw/")

    def rel(doel: Path) -> str:
        return Path(os.path.relpath(doel.resolve(), Path(van).resolve().parent)).as_posix()

    delen = []
    if md:
        delen.append(f"[tekst]({rel(md)})")
    if origineel:
        delen.append(f"[origineel ({origineel.suffix.lstrip('.')})]({rel(origineel)})")
    if meta.get("url"):
        delen.append(f"[online]({meta['url']})")
    return "Bron: " + " · ".join(delen)


_KOP_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def inhoud(repo_root: Path, bron_id: str, max_niveau: int = 3) -> tuple[int, list[dict]]:
    """Inhoudsopgave van de Markdown-versie in laag 1: (totaal aantal woorden, koppen).

    Elke kop t/m `max_niveau` met regelnummer (1-based) en het aantal woorden tot de volgende
    kop van gelijk of hoger niveau; niveau 1 is de hoogste kop in de tekst. Codeblokken worden overgeslagen. Deterministisch: dit is
    het deel van de index dat het gereedschap maakt, niet het Model.
    """
    md, _ = raw_paden(repo_root, bron_id)
    if md is None:
        raise FileNotFoundError(f"bron '{bron_id}' heeft geen Markdown-versie in sources/raw/")
    regels = md.read_text(encoding="utf-8").splitlines()
    koppen, in_code = [], False
    for nr, regel in enumerate(regels, start=1):
        if regel.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        m = None if in_code else _KOP_RE.match(regel)
        if m:
            koppen.append({"niveau": len(m.group(1)), "kop": m.group(2).replace("|", r"\|"), "regel": nr})
    # Niveau telt vanaf de hoogste kop in de tekst: conversies beginnen niet altijd bij '#'.
    hoogste = min((k["niveau"] for k in koppen), default=1)
    for k in koppen:
        k["niveau"] -= hoogste - 1
    koppen = [k for k in koppen if k["niveau"] <= max_niveau]
    woorden_per_regel = [len(r.split()) for r in regels]
    for i, k in enumerate(koppen):
        einde = next((v["regel"] for v in koppen[i + 1:] if v["niveau"] <= k["niveau"]), len(regels) + 1)
        k["woorden"] = sum(woorden_per_regel[k["regel"]:einde - 1])
    return sum(woorden_per_regel), koppen


def inhoud_markdown(repo_root: Path, bron_id: str, max_niveau: int = 3) -> str:
    """De inhoudsopgave als sectie `## Inhoud` voor sources/index/<bron-id>.md."""
    totaal, koppen = inhoud(repo_root, bron_id, max_niveau)
    kop = f"## Inhoud\n\nTekst: `sources/raw/{bron_id}.md`, {totaal} woorden. Regel = regelnummer in die tekst.\n\n"
    if not koppen:
        return kop + "De tekst heeft geen koppen.\n"
    rijen = ["| Kop | Regel | Woorden |", "|---|---|---|"]
    rijen += [f"| {'→ ' * (k['niveau'] - 1)}{k['kop']} | {k['regel']} | {k['woorden']} |" for k in koppen]
    return kop + "\n".join(rijen) + "\n"


def _vervang_sectie(body: str, kop: str, nieuw: str) -> str:
    """Vervang `## <kop>` tot de volgende `## `-kop door `nieuw`; ontbreekt de sectie, dan achteraan."""
    m = re.search(rf"(?m)^## {re.escape(kop)}\s*$", body)
    if not m:
        return body.rstrip("\n") + "\n\n" + nieuw
    rest = body[m.end():]
    volgende = re.search(r"(?m)^## ", rest)
    return body[: m.start()] + nieuw + ("\n" + rest[volgende.start():] if volgende else "")


def schrijf_inhoud(repo_root: Path, bron_id: str, max_niveau: int = 3) -> Path:
    """Zet of vervang de sectie `## Inhoud` in sources/index/<bron-id>.md."""
    pad = _index_dir(repo_root) / f"{bron_id}.md"
    page = frontmatter.read(pad)
    page.body = _vervang_sectie(page.body, "Inhoud", inhoud_markdown(repo_root, bron_id, max_niveau))
    frontmatter.write(pad, page)
    return pad


def schrijf_bronregel(repo_root: Path, bron_id: str, pagina: Path) -> None:
    """Zet of vervang de regel `Bron: …` direct onder de `# `-titel van een pagina (domein-lens)."""
    page = frontmatter.read(pagina)
    regel = bronregel(repo_root, bron_id, pagina)
    body = re.sub(r"(?m)^Bron: .*\n\n?", "", page.body, count=1)
    titel = re.search(r"(?m)^# .+\n", body)
    if titel is None:
        raise ValueError(f"{pagina}: geen '# '-titel om de bronregel onder te zetten")
    page.body = body[: titel.end()] + "\n" + regel + "\n" + body[titel.end():]
    frontmatter.write(pagina, page)


