"""Lezen en schrijven van YAML-frontmatter in Markdown-paginabestanden."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

FRONTMATTER_DELIM = "---"


@dataclass
class Page:
    meta: dict
    body: str

    def dump(self) -> str:
        yaml_text = yaml.safe_dump(self.meta, sort_keys=False, allow_unicode=True).strip()
        body = self.body.lstrip(chr(10))
        if body and not body.endswith(chr(10)):
            body += chr(10)
        return f"{FRONTMATTER_DELIM}\n{yaml_text}\n{FRONTMATTER_DELIM}\n\n{body}"


def parse(text: str) -> Page:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_DELIM:
        return Page(meta={}, body=text)
    try:
        end = lines[1:].index(FRONTMATTER_DELIM) + 1
    except ValueError as exc:
        raise ValueError("Ongesloten YAML-frontmatter (geen tweede '---' gevonden)") from exc
    yaml_text = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1 :])
    meta = yaml.safe_load(yaml_text) or {}
    if not isinstance(meta, dict):
        raise ValueError("Frontmatter moet een YAML-object (mapping) zijn")
    return Page(meta=meta, body=body)


def read(path: Path) -> Page:
    return parse(path.read_text(encoding="utf-8"))


def write(path: Path, page: Page) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page.dump(), encoding="utf-8", newline="\n")
