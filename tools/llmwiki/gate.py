"""De publicatiegate: plan/apply voor PROMOTE (curatie) en PUBLISH (sync).

Zie docs/onderbouwing.md 5.13. Smaak A (document) en smaak B (chat) worden hier
gecontroleerd; de echte afdwinging is de goedkeuringsklik van het harness op
`llmwiki promote apply` / `llmwiki publish apply` (permissie 'ask').

Gedeeld tussen curatie en sync: akkoordcontrole (smaak A/B), plan-hash-
vergelijking, `mark_final_done`, `log_event`. Per wiki-soort verschilt alleen
hoe een plan wordt opgebouwd en hoe het na akkoord wordt gematerialiseerd:
curatie kopieert een gestaged bestand en zet een statusveld; sync schrijft via
`sync.push_page` naar de externe site. `knowledge-base` heeft geen materialisatie
-- dat type gebruikt deze module niet.
"""
from __future__ import annotations

import difflib
import json
import subprocess
from pathlib import Path

from . import frontmatter, hashing, logbook, runs, sync as sync_module, validate


class GateError(RuntimeError):
    pass


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")


# --- Curatie: gestaged bestand -> kopie + statusveld ---


def _build_plan_curation(wiki_root: Path, run_id: str, final_phase: str) -> dict:
    rdir = runs.run_dir(wiki_root, run_id)
    changeset = _load_json(rdir / "changeset.json")

    entries = []
    for pagina in changeset["paginas"]:
        staged_path = rdir / "changeset" / pagina["staged_bestand"]
        new_content = staged_path.read_text(encoding="utf-8")
        target_path = wiki_root / pagina["pad"]
        if target_path.exists():
            basis_hash = hashing.hash_file(target_path)
            actie = "wijzigen"
        else:
            basis_hash = None
            actie = "nieuw"
        entries.append(
            {
                "pad": pagina["pad"],
                "actie": actie,
                "basis_hash": basis_hash,
                "nieuwe_hash": hashing.hash_text(new_content),
            }
        )

    body = {"run": run_id, "modus": final_phase, "paginas": entries}
    plan_hash = hashing.hash_json(body)
    return {**body, "plan_hash": plan_hash}


def _diff_lines_curation(wiki_root: Path, run_id: str, plan_obj: dict) -> list[str]:
    rdir = runs.run_dir(wiki_root, run_id)
    changeset = _load_json(rdir / "changeset.json")
    lines = []
    for entry, pagina in zip(plan_obj["paginas"], changeset["paginas"]):
        staged_path = rdir / "changeset" / pagina["staged_bestand"]
        new_content = staged_path.read_text(encoding="utf-8")
        old_content = (wiki_root / pagina["pad"]).read_text(encoding="utf-8") if entry["actie"] == "wijzigen" else ""
        diff = "\n".join(
            difflib.unified_diff(
                old_content.splitlines(), new_content.splitlines(), fromfile="huidig", tofile="voorstel", lineterm=""
            )
        )
        lines += [f"## {entry['pad']} ({entry['actie']})", "```diff", diff or "(geen inhoudelijke wijziging)", "```", ""]
    return lines


def _materialize_curation(wiki_root: Path, wiki_yaml: dict, run_id: str, beoordeeld_door: str, final_phase: str) -> None:
    rdir = runs.run_dir(wiki_root, run_id)
    changeset = _load_json(rdir / "changeset.json")
    page_types = wiki_yaml.get("page_types", {})
    for pagina in changeset["paginas"]:
        staged_path = rdir / "changeset" / pagina["staged_bestand"]
        page = frontmatter.read(staged_path)
        type_def = page_types.get(pagina["type"], {})
        if type_def.get("curated"):
            page.meta["status"] = "goedgekeurd"
        target_path = wiki_root / pagina["pad"]
        frontmatter.write(target_path, page)
        new_hash = hashing.hash_text(target_path.read_text(encoding="utf-8"))
        if type_def.get("curated"):
            logbook.append_log(wiki_root, final_phase, page.meta.get("id", target_path.stem), beoordeeld_door, new_hash)
    logbook.regenerate(wiki_root, wiki_yaml)


# --- Sync: git-gedetecteerde wijzigingen in content/ -> pywikibot-push ---


def _revisions_path(wiki_root: Path, doel: str) -> Path:
    if doel == "site":
        return wiki_root / "revisies.json"
    d = wiki_root / ".work" / "sync"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{doel}.json"


def _load_revisions(wiki_root: Path, doel: str) -> dict:
    path = _revisions_path(wiki_root, doel)
    return _load_json(path) if path.exists() else {}


def _save_revisions(wiki_root: Path, doel: str, data: dict) -> None:
    _write_json(_revisions_path(wiki_root, doel), data)


def git_changed_content_paths(wiki_root: Path) -> list[str]:
    """Paden (relatief aan wiki_root) onder content/ met een lokale wijziging."""
    result = subprocess.run(
        ["git", "-C", str(wiki_root), "status", "--porcelain", "--untracked-files=all", "content"],
        capture_output=True,
        text=True,
        check=False,
    )
    paths = []
    for line in result.stdout.splitlines():
        status, rest = line[:2], line[3:]
        if status.strip() in ("M", "A", "AM", "MM", "??"):
            paths.append(rest.strip('"'))
    return paths


def _build_plan_sync(
    wiki_root: Path,
    wiki_yaml: dict,
    run_id: str,
    doel: str,
    paths: list[str],
    titel_overrides: dict[str, str] | None = None,
) -> dict:
    revisies = _load_revisions(wiki_root, doel)
    overrides = titel_overrides or {}
    site = sync_module.get_site(wiki_yaml, doel)

    entries = []
    for pad in paths:
        titel = overrides.get(pad) or (revisies.get(pad) or {}).get("titel")
        if not titel:
            raise GateError(
                f"Geen bekende titel voor '{pad}'. Pull de pagina eerst met 'llmwiki pull', "
                "of geef een titel-override mee."
            )
        try:
            live = sync_module.pull_page(site, titel)
        except sync_module.SyncError:
            live = None
        target_path = wiki_root / pad
        new_text = target_path.read_text(encoding="utf-8")
        entries.append(
            {
                "pad": pad,
                "titel": titel,
                "actie": "wijzigen" if live else "nieuw",
                "basis_revid": live.revid if live else None,
                "nieuwe_hash": hashing.hash_text(new_text),
            }
        )

    body = {"run": run_id, "modus": "publish", "paginas": entries}
    plan_hash = hashing.hash_json(body)
    return {**body, "plan_hash": plan_hash}


def _diff_lines_sync(wiki_root: Path, wiki_yaml: dict, doel: str, plan_obj: dict) -> list[str]:
    site = sync_module.get_site(wiki_yaml, doel)
    lines = []
    for entry in plan_obj["paginas"]:
        new_content = (wiki_root / entry["pad"]).read_text(encoding="utf-8")
        old_content = ""
        if entry["actie"] == "wijzigen":
            try:
                old_content = sync_module.pull_page(site, entry["titel"]).text
            except sync_module.SyncError:
                pass  # live pagina niet op te halen voor het voorstel; toon dan de volledige nieuwe tekst
        diff = "\n".join(
            difflib.unified_diff(
                old_content.splitlines(), new_content.splitlines(), fromfile="live", tofile="voorstel", lineterm=""
            )
        )
        lines += [
            f"## {entry['titel']} ({entry['pad']}, {entry['actie']})",
            "```diff",
            diff or "(geen inhoudelijke wijziging)",
            "```",
            "",
        ]
    return lines


def _materialize_sync(wiki_root: Path, wiki_yaml: dict, run_id: str, doel: str, beoordeeld_door: str, plan_obj: dict) -> None:
    site = sync_module.get_site(wiki_yaml, doel)
    revisies = _load_revisions(wiki_root, doel)
    gelukt: list[str] = []
    try:
        for entry in plan_obj["paginas"]:
            new_text = (wiki_root / entry["pad"]).read_text(encoding="utf-8")
            result = sync_module.push_page(
                site, entry["titel"], new_text, entry["basis_revid"], summary=f"[llm-wiki] run {run_id}"
            )
            revisies[entry["pad"]] = {"titel": entry["titel"], "revid": result.revid}
            _save_revisions(wiki_root, doel, revisies)
            content_hash = hashing.hash_text(new_text)
            logbook.append_log(wiki_root, "publish", entry["titel"], beoordeeld_door, content_hash, doel=doel)
            gelukt.append(entry["pad"])
    except sync_module.SyncError as exc:
        mislukt = [e["pad"] for e in plan_obj["paginas"] if e["pad"] not in gelukt]
        raise GateError(
            f"Publicatie gedeeltelijk gelukt ({len(gelukt)}/{len(plan_obj['paginas'])}): "
            f"gelukt {gelukt}, mislukt/overgeslagen {mislukt}. Oorzaak: {exc}"
        ) from exc


# --- Gedeeld: akkoordcontrole, plan/apply-dispatch ---


def plan(
    wiki_root: Path,
    wiki_yaml: dict,
    run_id: str,
    *,
    doel: str = "site",
    paths: list[str] | None = None,
    titel_overrides: dict[str, str] | None = None,
) -> Path:
    state = runs.load_state(wiki_root, run_id)
    final_phase = runs.final_phase_for(wiki_yaml)
    if state["fasen"].get("validate", {}).get("status") != "done":
        raise GateError("VALIDATE moet zijn afgerond voordat een voorstel kan worden gemaakt")
    report = _load_json(runs.run_dir(wiki_root, run_id) / "validation-report.json")
    fouten = [c for c in report["controles"] if c["ernst"] == "fout"]
    if fouten:
        raise GateError(f"VALIDATE bevat {len(fouten)} fout(en); los ze op voor een voorstel wordt gemaakt")

    if final_phase == "publish":
        wijzigingen = paths if paths is not None else git_changed_content_paths(wiki_root)
        if not wijzigingen:
            raise GateError("Geen wijzigingen onder content/ gevonden om te publiceren")
        plan_obj = _build_plan_sync(wiki_root, wiki_yaml, run_id, doel, wijzigingen, titel_overrides)
        diff_lines = _diff_lines_sync(wiki_root, wiki_yaml, doel, plan_obj)
    else:
        plan_obj = _build_plan_curation(wiki_root, run_id, final_phase)
        diff_lines = _diff_lines_curation(wiki_root, run_id, plan_obj)

    validate.validate_instance(plan_obj, "publish-plan")

    rdir = runs.run_dir(wiki_root, run_id)
    plan_path = rdir / f"{final_phase}-plan.json"
    _write_json(plan_path, plan_obj)

    voorstellen_dir = wiki_root / "voorstellen"
    voorstellen_dir.mkdir(parents=True, exist_ok=True)
    body_lines = [f"# Voorstel {run_id}", "", f"Modus: {final_phase}", ""] + diff_lines
    voorstel_page = frontmatter.Page(
        meta={
            "run": run_id,
            "plan_hash": plan_obj["plan_hash"],
            "akkoord_voor_publicatie": "nee",
            "beoordeeld_door": "",
        },
        body="\n".join(body_lines),
    )
    voorstel_path = voorstellen_dir / f"{run_id}.md"
    frontmatter.write(voorstel_path, voorstel_page)
    runs.log_event(wiki_root, run_id, final_phase, "voorstel_aangemaakt", plan_hash=plan_obj["plan_hash"])
    return voorstel_path


def apply(
    wiki_root: Path,
    wiki_yaml: dict,
    run_id: str,
    *,
    akkoord_woord: str | None = None,
    doel: str = "site",
) -> Path:
    final_phase = runs.final_phase_for(wiki_yaml)
    rdir = runs.run_dir(wiki_root, run_id)
    plan_path = rdir / f"{final_phase}-plan.json"
    if not plan_path.exists():
        raise GateError(f"Geen {final_phase}-plan gevonden; draai eerst 'llmwiki {final_phase} plan --run {run_id}'")
    stored_plan = _load_json(plan_path)

    if final_phase == "publish":
        paths = [e["pad"] for e in stored_plan["paginas"]]
        titel_overrides = {e["pad"]: e["titel"] for e in stored_plan["paginas"]}
        live_plan = _build_plan_sync(wiki_root, wiki_yaml, run_id, doel, paths, titel_overrides)
    else:
        live_plan = _build_plan_curation(wiki_root, run_id, final_phase)

    if live_plan["plan_hash"] != stored_plan["plan_hash"]:
        raise GateError(
            "Een pagina is gewijzigd sinds het voorstel is gemaakt (plan-hash komt niet overeen). "
            f"Maak opnieuw een voorstel: llmwiki {final_phase} plan --run {run_id}"
        )

    voorstel_path = wiki_root / "voorstellen" / f"{run_id}.md"
    if not voorstel_path.exists():
        raise GateError(f"Geen publicatievoorstel gevonden op {voorstel_path}")
    approval = frontmatter.read(voorstel_path).meta
    validate.validate_instance(approval, "approval")
    if approval["plan_hash"] != stored_plan["plan_hash"]:
        raise GateError(
            "Het akkoord hoort bij een verouderde plan-hash. Maak een nieuw voorstel en vraag opnieuw akkoord."
        )

    approval_mode = wiki_yaml.get("curation", wiki_yaml.get("publish", {})).get("approval", "document")
    beoordeeld_door = approval.get("beoordeeld_door", "")
    if approval_mode == "document":
        if approval.get("akkoord_voor_publicatie") != "ja":
            raise GateError("Voorstel staat nog op 'nee'; de redacteur moet eerst akkoord geven in het document")
        if not beoordeeld_door.strip():
            raise GateError("'beoordeeld_door' is leeg; een akkoord zonder naam telt niet")
    elif approval_mode == "chat":
        if akkoord_woord != "AKKOORD":
            raise GateError(
                "Smaak B vereist het letterlijke woord AKKOORD van de redacteur in de chat "
                "(--akkoord-woord AKKOORD); iets anders ('prima', 'ja hoor') is geen akkoord"
            )
        beoordeeld_door = beoordeeld_door or "chat"
    else:
        raise GateError(f"Onbekende approval-modus '{approval_mode}' in wiki.yaml")

    if final_phase == "publish":
        _materialize_sync(wiki_root, wiki_yaml, run_id, doel, beoordeeld_door, stored_plan)
    else:
        _materialize_curation(wiki_root, wiki_yaml, run_id, beoordeeld_door, final_phase)

    runs.mark_final_done(wiki_root, run_id, final_phase, plan_path.name, stored_plan["plan_hash"])
    runs.log_event(wiki_root, run_id, final_phase, "toegepast", beoordeeld_door=beoordeeld_door)
    return voorstel_path
