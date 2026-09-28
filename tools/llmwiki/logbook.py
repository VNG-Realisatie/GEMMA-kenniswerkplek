"""log.md (alleen aanvullen) en voortgang.md (gegenereerd). Aantallen per status
in voortgang.md komen uit `wiki_yaml["page_types"]`, een curation/knowledge-base
concept; bij een sync-wiki (geen page_types) blijft die sectie leeg."""
from __future__ import annotations

from datetime import date
from pathlib import Path

from . import frontmatter, hashing, runs


def append_log(wiki_root: Path, actie: str, pagina_id: str, beoordeeld_door: str, content_hash: str) -> None:
    log_path = wiki_root / "log.md"
    line = f"## [{date.today().isoformat()}] {actie} | {pagina_id} | {beoordeeld_door} | {hashing.short(content_hash)}\n"
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(line)


def _iter_pages(wiki_root: Path, wiki_yaml: dict):
    for type_name, type_def in wiki_yaml.get("page_types", {}).items():
        page_dir = wiki_root / type_def["dir"]
        if not page_dir.exists():
            continue
        for path in sorted(page_dir.rglob("*.md")):
            yield type_name, path, frontmatter.read(path).meta


def regenerate(wiki_root: Path, wiki_yaml: dict) -> Path:
    counts: dict[str, dict[str, int]] = {}
    waiting_review = []
    for type_name, path, meta in _iter_pages(wiki_root, wiki_yaml):
        status = meta.get("status", "-")
        counts.setdefault(type_name, {}).setdefault(status, 0)
        counts[type_name][status] += 1
        if status == "review":
            waiting_review.append(meta.get("id", path.stem))

    open_runs = []
    for run_id in runs.list_runs(wiki_root):
        try:
            state = runs.load_state(wiki_root, run_id)
        except runs.RunError:
            continue
        if runs.next_phase(state, wiki_yaml) is not None and "besluit" not in state:
            open_runs.append(run_id)

    lines = ["# Voortgang", "", f"Gegenereerd: {date.today().isoformat()}", "", "## Open runs"]
    lines += [f"- {r}" for r in open_runs] or ["- (geen)"]
    lines += ["", "## Aantallen per status"]
    for type_name, status_counts in sorted(counts.items()):
        lines.append(f"- {type_name}: " + ", ".join(f"{k}={v}" for k, v in sorted(status_counts.items())))
    lines += ["", "## Wacht op review"]
    lines += [f"- {p}" for p in waiting_review] or ["- (geen)"]
    lines.append("")

    out_path = wiki_root / "voortgang.md"
    out_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return out_path
