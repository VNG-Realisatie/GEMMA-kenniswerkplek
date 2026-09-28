"""Schemavalidatie (JSON Schema 2020-12), Markdown-paginavalidatie (curation/
knowledge-base) en wikitext-paginavalidatie (sync)."""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from . import frontmatter, paths, sources

SCHEMA_DIR = Path(__file__).parent / "schemas"

_KNOWN_SCHEMAS = {
    "source": "source.schema.json",
    "source-index": "source-index.schema.json",
    "assessment": "assessment.schema.json",
    "changeset": "changeset.schema.json",
    "validation-report": "validation-report.schema.json",
    "publish-plan": "publish-plan.schema.json",
    "approval": "approval.schema.json",
    "page-meta": "page-meta.schema.json",
    "run-state": "run-state.schema.json",
}


class ValidationFailed(ValueError):
    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("; ".join(errors))


def schema_path(name: str) -> Path:
    if name not in _KNOWN_SCHEMAS:
        raise KeyError(f"Onbekend schema '{name}'. Bekend: {sorted(_KNOWN_SCHEMAS)}")
    return SCHEMA_DIR / _KNOWN_SCHEMAS[name]


def load_schema(name: str) -> dict:
    return json.loads(schema_path(name).read_text(encoding="utf-8"))


def validate_instance(instance: dict, schema_name: str) -> None:
    schema = load_schema(schema_name)
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        raise ValidationFailed([f"{'.'.join(str(p) for p in e.path)}: {e.message}" for e in errors])


def validate_file(path: Path, schema_name: str) -> None:
    instance = json.loads(path.read_text(encoding="utf-8"))
    validate_instance(instance, schema_name)


# --- Paginavalidatie: vorm hangt af van de wiki-soort (wiki.yaml `type`) ---

WIKILINK_PATTERN = "[["


def validate_page(wiki_root: Path, page_path: Path, wiki_yaml: dict) -> list[str]:
    """Valideert één pagina. Geeft een lijst leesbare foutmeldingen terug (leeg = geldig).

    Een sync-wiki bevat kale MediaWiki-wikitext (geen frontmatter, content/ is een
    directe werkkopie van de site); curation/knowledge-base gebruiken Markdown met
    frontmatter. De vorm van de controle volgt daarom `wiki_yaml["type"]`.
    """
    if wiki_yaml.get("type") == "sync":
        return _validate_sync_page(page_path)
    return _validate_markdown_page(wiki_root, page_path, wiki_yaml)


# --- Wikitext-paginavalidatie (sync) ---

PREFORMATTED_SAFE_PREFIXES = ("{|", "|}", "|", "!", "*", "#", ";", ":")


def _validate_sync_page(page_path: Path) -> list[str]:
    """Generieke MediaWiki-wikitext-controles; geen kennis van één specifieke
    wiki (zie AGENTS.md 'Grenzen') — alleen wat voor elke MediaWiki-site geldt."""
    errors: list[str] = []
    text = page_path.read_text(encoding="utf-8")
    if not text.strip():
        errors.append(f"{page_path}: leeg bestand")
        return errors

    template_depth = 0
    in_pre = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        if "<pre" in line:
            in_pre = True
        if line.startswith(" ") and not in_pre and template_depth == 0:
            content = line.lstrip(" ")
            if not content.startswith(PREFORMATTED_SAFE_PREFIXES):
                errors.append(
                    f"{page_path}:{line_no}: regel begint met spatie(s); "
                    "MediaWiki rendert dit als preformatted-blok"
                )
        template_depth = max(0, template_depth + line.count("{{") - line.count("}}"))
        if "</pre>" in line:
            in_pre = False
    return errors


# --- Markdown-paginavalidatie (curation/knowledge-base) ---


def _validate_markdown_page(wiki_root: Path, page_path: Path, wiki_yaml: dict) -> list[str]:
    errors: list[str] = []
    page = frontmatter.read(page_path)
    meta = page.meta

    expected_id = page_path.stem
    if meta.get("id") != expected_id:
        errors.append(f"{page_path}: id '{meta.get('id')}' komt niet overeen met bestandsnaam '{expected_id}'")

    page_type = meta.get("type")
    page_types = wiki_yaml.get("page_types", {})
    type_def = page_types.get(page_type)
    if type_def is None:
        errors.append(f"{page_path}: onbekend paginatype '{page_type}' (niet in wiki.yaml page_types)")

    if type_def and type_def.get("curated"):
        curation = wiki_yaml.get("curation", {})
        states = curation.get("states", [])
        status = meta.get("status")
        if status not in states:
            errors.append(f"{page_path}: status '{status}' niet in curation.states {states}")

    tags = set(wiki_yaml.get("sources", {}).get("tags", []))
    exclude_tags = set(wiki_yaml.get("sources", {}).get("exclude_tags", []))
    for bron_id in meta.get("bronnen", []) or []:
        try:
            entry = sources.read_index_entry(paths.find_repo_root(wiki_root), bron_id)
        except FileNotFoundError:
            errors.append(f"{page_path}: bron '{bron_id}' bestaat niet in sources/index/")
            continue
        entry_tags = set(entry.get("tags", []))
        if tags and not (entry_tags & tags):
            errors.append(f"{page_path}: bron '{bron_id}' valt buiten de scope (tags {tags}) van deze wiki")
        if entry_tags & exclude_tags:
            errors.append(f"{page_path}: bron '{bron_id}' heeft een uitgesloten tag {exclude_tags}")

    if WIKILINK_PATTERN in page.body:
        errors.append(f"{page_path}: gebruik geen [[wikilinks]], alleen relatieve Markdown-links")

    for line_no, line in enumerate(page.body.splitlines(), start=1):
        pos = 0
        while True:
            start = line.find("](", pos)
            if start == -1:
                break
            end = line.find(")", start)
            if end == -1:
                break
            target = line[start + 2 : end]
            if target.startswith(("http://", "https://", "#")):
                pos = end + 1
                continue
            if target.startswith("/") or (len(target) > 1 and target[1] == ":"):
                errors.append(f"{page_path}:{line_no}: absoluut pad in link '{target}', gebruik een relatief pad")
            pos = end + 1

    return errors
