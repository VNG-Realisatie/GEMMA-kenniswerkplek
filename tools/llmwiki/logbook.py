"""log.md (alleen aanvullen) en voortgang.md (gegenereerd). Aantallen per status
in voortgang.md komen uit `wiki_yaml["page_types"]`, een curation/knowledge-base
concept; bij een sync-wiki (geen page_types) blijft die sectie leeg.

log.md is één tabel met een rij per gebeurtenis: `| Datum | Actie | Id | Door | Hash |`, bij een sync-wiki
`| Datum | Actie | Pagina | Doel | Door | Hash |`. `lees_log` leest ook het oudere formaat met één kop per
gebeurtenis (`## [datum] actie | id | [doel |] door | hash`), zodat een omgezet log inhoudelijk te vergelijken is."""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from . import frontmatter, hashing, paths, runs


@dataclass(frozen=True)
class Logregel:
    datum: str
    actie: str
    id: str
    door: str
    hash: str
    doel: str = ""


_OUDE_REGEL = re.compile(r"^## \[(?P<datum>[^\]]+)\] (?P<rest>.+)$")
_KOLOMNAMEN = {"datum": "datum", "actie": "actie", "id": "id", "pagina": "id", "doel": "doel", "door": "door",
               "hash": "hash"}


def kolommen(sync: bool) -> list[str]:
    return ["Datum", "Actie", "Pagina", "Doel", "Door", "Hash"] if sync else ["Datum", "Actie", "Id", "Door", "Hash"]


def _cellen(regel: str) -> list[str]:
    return [c.strip() for c in regel.strip().strip("|").split("|")]


def lees_log(tekst: str) -> list[Logregel]:
    """Alle gebeurtenissen in volgorde, uit tabelrijen en uit koppen van het oude formaat."""
    regels: list[Logregel] = []
    kop: list[str] | None = None
    for regel in tekst.splitlines():
        oud = _OUDE_REGEL.match(regel)
        if oud:
            delen = [d.strip() for d in oud["rest"].split(" | ")]
            if len(delen) == 4:
                regels.append(Logregel(oud["datum"], delen[0], delen[1], delen[2], delen[3]))
            elif len(delen) == 5:
                regels.append(Logregel(oud["datum"], delen[0], delen[1], delen[3], delen[4], doel=delen[2]))
            continue
        if not regel.lstrip().startswith("|"):
            continue
        cellen = _cellen(regel)
        namen = [_KOLOMNAMEN.get(c.lower()) for c in cellen]
        if "datum" in namen and "hash" in namen:
            kop = namen
            continue
        if kop is None or all(set(c) <= set("-: ") for c in cellen) or len(cellen) != len(kop):
            continue
        velden = {naam: waarde for naam, waarde in zip(kop, cellen) if naam}
        regels.append(Logregel(velden.get("datum", ""), velden.get("actie", ""), velden.get("id", ""),
                               velden.get("door", ""), velden.get("hash", ""), velden.get("doel", "")))
    return regels


def heeft_regel(tekst: str, actie: str, pagina_id: str, hash_kort: str | None = None) -> bool:
    """Staat er een gebeurtenis `actie` voor `pagina_id` (en, als gegeven, met deze korte hash)?"""
    return any(r.actie == actie and r.id == pagina_id and (hash_kort is None or r.hash == hash_kort)
               for r in lees_log(tekst))


def _is_sync(wiki_root: Path) -> bool:
    try:
        return paths.load_wiki_yaml(wiki_root).get("type") == "sync"
    except (OSError, ValueError):
        return False


def tabelkop(sync: bool) -> str:
    namen = kolommen(sync)
    return "| " + " | ".join(namen) + " |\n" + "|" + "---|" * len(namen) + "\n"


def tabelrij(r: Logregel, sync: bool) -> str:
    cellen = [r.datum, r.actie, r.id, r.doel, r.door, r.hash] if sync else [r.datum, r.actie, r.id, r.door, r.hash]
    return "| " + " | ".join(cellen) + " |\n"


def append_log(
    wiki_root: Path, actie: str, pagina_id: str, beoordeeld_door: str, content_hash: str, doel: str | None = None
) -> None:
    """`doel` is het sync-publicatiedoel (bv. 'site' of 'staging'); curation/
    knowledge-base kennen geen testdoelen en laten dit weg. Zet de tabelkop erboven als die er nog niet staat."""
    log_path = wiki_root / "log.md"
    tekst = log_path.read_text(encoding="utf-8") if log_path.exists() else "# Logboek\n"
    kop = next((_cellen(r) for r in tekst.splitlines() if r.lstrip().startswith("|") and _cellen(r)[:1] == ["Datum"]),
               None)
    toevoeging = ""
    if kop is None:
        sync = _is_sync(wiki_root) or bool(doel)
        toevoeging += ("" if tekst.endswith("\n\n") else "\n" if tekst.endswith("\n") else "\n\n") + tabelkop(sync)
    else:
        sync = "Doel" in kop
    regel = Logregel(date.today().isoformat(), actie, pagina_id, beoordeeld_door, hashing.short(content_hash),
                     doel or "")
    toevoeging += tabelrij(regel, sync)
    if not log_path.exists():
        log_path.write_text(tekst, encoding="utf-8")
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(toevoeging)


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
