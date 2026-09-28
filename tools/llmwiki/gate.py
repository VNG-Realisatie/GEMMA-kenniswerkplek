"""De publicatiegate: plan/apply voor PROMOTE (type B/C) en PUBLISH (type A, nog niet geïmplementeerd).

Zie docs/onderbouwing.md 5.13. Smaak A (document) en smaak B (chat) worden hier
gecontroleerd; de echte afdwinging is de goedkeuringsklik van het harness op
`llmwiki promote apply` / `llmwiki publish apply` (permissie 'ask', Klus 2).
"""
from __future__ import annotations

import difflib
import json
from pathlib import Path

from . import frontmatter, hashing, logbook, runs, validate


class GateError(RuntimeError):
    pass


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _build_plan(wiki_root: Path, run_id: str, final_phase: str) -> dict:
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


def plan(wiki_root: Path, wiki_yaml: dict, run_id: str) -> Path:
    state = runs.load_state(wiki_root, run_id)
    final_phase = runs.final_phase_for(wiki_yaml)
    if final_phase == "publish":
        raise NotImplementedError(
            "MediaWiki-publicatie vereist de harness-integratie en MCP-koppeling uit Klus 2, "
            "die in deze inrichting nog niet is gebouwd. Zie docs/kluswijzer.md, Klus 2."
        )
    if state["fasen"].get("validate", {}).get("status") != "done":
        raise GateError("VALIDATE moet zijn afgerond voordat een voorstel kan worden gemaakt")
    report = _load_json(runs.run_dir(wiki_root, run_id) / "validation-report.json")
    fouten = [c for c in report["controles"] if c["ernst"] == "fout"]
    if fouten:
        raise GateError(f"VALIDATE bevat {len(fouten)} fout(en); los ze op voor een voorstel wordt gemaakt")

    plan_obj = _build_plan(wiki_root, run_id, final_phase)
    validate.validate_instance(plan_obj, "publish-plan")

    rdir = runs.run_dir(wiki_root, run_id)
    plan_path = rdir / f"{final_phase}-plan.json"
    plan_path.write_text(json.dumps(plan_obj, indent=2, ensure_ascii=False), encoding="utf-8")

    voorstellen_dir = wiki_root / "voorstellen"
    voorstellen_dir.mkdir(parents=True, exist_ok=True)
    changeset = _load_json(rdir / "changeset.json")
    body_lines = [f"# Voorstel {run_id}", "", f"Modus: {final_phase}", ""]
    for entry, pagina in zip(plan_obj["paginas"], changeset["paginas"]):
        staged_path = rdir / "changeset" / pagina["staged_bestand"]
        new_content = staged_path.read_text(encoding="utf-8")
        old_content = (wiki_root / pagina["pad"]).read_text(encoding="utf-8") if entry["actie"] == "wijzigen" else ""
        diff = "\n".join(
            difflib.unified_diff(
                old_content.splitlines(), new_content.splitlines(), fromfile="huidig", tofile="voorstel", lineterm=""
            )
        )
        body_lines += [f"## {entry['pad']} ({entry['actie']})", "```diff", diff or "(geen inhoudelijke wijziging)", "```", ""]

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
) -> Path:
    final_phase = runs.final_phase_for(wiki_yaml)
    if final_phase == "publish":
        raise NotImplementedError(
            "MediaWiki-publicatie vereist Klus 2 (nog niet gebouwd in deze inrichting)."
        )

    rdir = runs.run_dir(wiki_root, run_id)
    plan_path = rdir / f"{final_phase}-plan.json"
    if not plan_path.exists():
        raise GateError(f"Geen {final_phase}-plan gevonden; draai eerst 'llmwiki {final_phase} plan --run {run_id}'")
    stored_plan = _load_json(plan_path)

    live_plan = _build_plan(wiki_root, run_id, final_phase)
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

    runs.mark_final_done(wiki_root, run_id, final_phase, plan_path.name, stored_plan["plan_hash"])
    logbook.regenerate(wiki_root, wiki_yaml)
    runs.log_event(wiki_root, run_id, final_phase, "toegepast", beoordeeld_door=beoordeeld_door)
    return voorstel_path
