"""Run-State: kladblok per Run in .work/runs/<run-id>/. Zie docs/onderbouwing.md 5.11."""
from __future__ import annotations

import json
import os
import secrets
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import paths, validate

PHASE_ORDER = ["ingest", "assess", "write", "validate"]
PHASE_SCHEMA = {
    "ingest": "source",
    "assess": "assessment",
    "write": "changeset",
    "validate": "validation-report",
}
PHASE_ARTIFACT_FILENAME = {
    "ingest": "source.json",
    "assess": "assessment.json",
    "write": "changeset.json",
    "validate": "validation-report.json",
}


class RunError(RuntimeError):
    pass


def final_phase_for(wiki_yaml: dict) -> str:
    return "publish" if wiki_yaml.get("type") == "sync" else "promote"


def _runs_dir(wiki_root: Path) -> Path:
    return wiki_root / ".work" / "runs"


def run_dir(wiki_root: Path, run_id: str) -> Path:
    return _runs_dir(wiki_root) / run_id


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")


def new_run_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M")
    return f"{stamp}-{secrets.token_hex(2)}"


def log_event(wiki_root: Path, run_id: str, phase: str, event: str, **extra) -> None:
    entry = {
        "tijdstip": datetime.now(timezone.utc).isoformat(),
        "fase": phase,
        "gebeurtenis": event,
        "harness": os.environ.get("LLMWIKI_HARNESS", "onbekend"),
        "model": os.environ.get("LLMWIKI_MODEL", "onbekend"),
        **extra,
    }
    log_path = run_dir(wiki_root, run_id) / "log.jsonl"
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def load_state(wiki_root: Path, run_id: str) -> dict:
    state_path = run_dir(wiki_root, run_id) / "state.json"
    if not state_path.exists():
        raise RunError(f"Onbekende run '{run_id}' (geen state.json in {run_dir(wiki_root, run_id)})")
    return json.loads(state_path.read_text(encoding="utf-8"))


def save_state(wiki_root: Path, state: dict) -> None:
    state["bijgewerkt"] = _now()
    validate.validate_instance(state, "run-state")
    state_path = run_dir(wiki_root, state["run_id"]) / "state.json"
    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def start(wiki_root: Path, wiki_yaml: dict, workflow: str, onderwerp: str | None = None) -> dict:
    run_id = new_run_id()
    rdir = run_dir(wiki_root, run_id)
    (rdir / "changeset").mkdir(parents=True, exist_ok=True)
    (rdir / "input").mkdir(parents=True, exist_ok=True)

    bronnen: list[str] = []
    if onderwerp:
        onderwerp_path = wiki_root / "onderwerpen" / f"{onderwerp}.md"
        if not onderwerp_path.exists():
            raise RunError(f"Onderwerppagina niet gevonden: {onderwerp_path}")
        from . import frontmatter

        bronnen = list(frontmatter.read(onderwerp_path).meta.get("bronnen", []) or [])

    final_phase = final_phase_for(wiki_yaml)
    fasen = {name: {"status": "pending", "artefact": None, "hash": None} for name in PHASE_ORDER}
    fasen[final_phase] = {"status": "pending", "artefact": None, "hash": None}

    state = {
        "run_id": run_id,
        "wiki_key": wiki_yaml.get("key", ""),
        "workflow": workflow,
        "onderwerp": onderwerp,
        "bronnen": bronnen,
        "fasen": fasen,
        "aangemaakt": _now(),
        "bijgewerkt": _now(),
    }
    save_state(wiki_root, state)
    log_event(wiki_root, run_id, "run", "gestart", workflow=workflow, onderwerp=onderwerp)
    return state


def _phase_sequence(state: dict, wiki_yaml: dict) -> list[str]:
    return [*PHASE_ORDER, final_phase_for(wiki_yaml)]


def next_phase(state: dict, wiki_yaml: dict) -> str | None:
    for name in _phase_sequence(state, wiki_yaml):
        if state["fasen"].get(name, {}).get("status") != "done":
            return name
    return None


def find_open_run(wiki_root: Path) -> str | None:
    runs_dir = _runs_dir(wiki_root)
    if not runs_dir.exists():
        return None
    candidates = sorted((p.name for p in runs_dir.iterdir() if p.is_dir()), reverse=True)
    return candidates[0] if candidates else None


def complete(wiki_root: Path, wiki_yaml: dict, run_id: str, phase: str, data_path: Path | None) -> dict:
    state = load_state(wiki_root, run_id)
    expected = next_phase(state, wiki_yaml)
    if phase != expected:
        raise RunError(f"Fase '{phase}' is niet aan de beurt; verwacht '{expected}'")

    artefact_rel = None
    artefact_hash = None
    if phase in PHASE_SCHEMA:
        if data_path is None:
            raise RunError(f"Fase '{phase}' vereist een artefact (--data <bestand>.json)")
        instance = json.loads(Path(data_path).read_text(encoding="utf-8"))
        validate.validate_instance(instance, PHASE_SCHEMA[phase])
        if phase == "write":
            for pagina in instance.get("paginas", []):
                staged = run_dir(wiki_root, run_id) / "changeset" / pagina["staged_bestand"]
                if not staged.exists():
                    raise RunError(f"Gestaged bestand ontbreekt: {staged}")
        dest = run_dir(wiki_root, run_id) / PHASE_ARTIFACT_FILENAME[phase]
        dest.write_text(json.dumps(instance, indent=2, ensure_ascii=False), encoding="utf-8")
        artefact_rel = dest.name
        from . import hashing

        artefact_hash = hashing.hash_file(dest)

    state["fasen"].setdefault(phase, {})
    state["fasen"][phase] = {"status": "done", "artefact": artefact_rel, "hash": artefact_hash}
    save_state(wiki_root, state)
    log_event(wiki_root, run_id, phase, "afgerond")
    return state


def mark_final_done(wiki_root: Path, run_id: str, final_phase: str, artefact: str, artefact_hash: str) -> dict:
    state = load_state(wiki_root, run_id)
    state["fasen"][final_phase] = {"status": "done", "artefact": artefact, "hash": artefact_hash}
    save_state(wiki_root, state)
    return state


def abandon(wiki_root: Path, run_id: str) -> None:
    """Verwijdert het kladblok van een run. Er zijn nooit bestanden buiten .work/ voor
    de laatste fase (publish/promote apply); dus dit laat niets achter in de wiki."""
    d = run_dir(wiki_root, run_id)
    if not d.exists():
        raise RunError(f"Onbekende run '{run_id}'")
    shutil.rmtree(d)


def close(wiki_root: Path, run_id: str, besluit: str) -> None:
    log_event(wiki_root, run_id, "run", "gesloten_zonder_publicatie", besluit=besluit)
    state = load_state(wiki_root, run_id)
    state["besluit"] = besluit
    state_path = run_dir(wiki_root, run_id) / "state.json"
    raw = json.loads(state_path.read_text(encoding="utf-8"))
    raw["besluit"] = besluit
    state_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")


def list_runs(wiki_root: Path) -> list[str]:
    runs_dir = _runs_dir(wiki_root)
    if not runs_dir.exists():
        return []
    return sorted(p.name for p in runs_dir.iterdir() if p.is_dir())


def is_finished(wiki_root: Path, wiki_yaml: dict, run_id: str) -> bool:
    state = load_state(wiki_root, run_id)
    return next_phase(state, wiki_yaml) is None or "besluit" in state


def prune(wiki_root: Path, wiki_yaml: dict, retention_days: int) -> list[str]:
    removed = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=retention_days)
    for run_id in list_runs(wiki_root):
        try:
            state = load_state(wiki_root, run_id)
        except RunError:
            continue
        finished = next_phase(state, wiki_yaml) is None or "besluit" in state
        if not finished:
            continue
        updated = datetime.strptime(state["bijgewerkt"], "%Y-%m-%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        if updated < cutoff:
            shutil.rmtree(run_dir(wiki_root, run_id))
            voorstel = wiki_root / "voorstellen" / f"{run_id}.md"
            if voorstel.exists():
                voorstel.unlink()
            removed.append(run_id)
    return removed
