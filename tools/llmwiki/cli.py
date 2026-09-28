"""Command-line interface voor llmwiki. Zie ARCHITECTURE.md en docs/onderbouwing.md."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from . import __version__, gate, lint, logbook, paths, runs, sources, validate, workspace_check


def _wiki_root(args) -> Path:
    start = Path(args.wiki) if getattr(args, "wiki", None) else Path.cwd()
    return paths.find_wiki_root(start)


def _repo_root() -> Path:
    return paths.find_repo_root()


def cmd_version(args) -> int:
    print(__version__)
    return 0


def cmd_lint(args) -> int:
    errors = lint.run_lint(_repo_root())
    if errors:
        for err in errors:
            print(f"FOUT: {err}", file=sys.stderr)
        return 1
    print("llmwiki lint: geen problemen gevonden")
    return 0


def cmd_validate(args) -> int:
    if args.schema == "page":
        wiki_root = _wiki_root(args)
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        errors = validate.validate_page(wiki_root, Path(args.bestand), wiki_yaml)
        if errors:
            for err in errors:
                print(f"FOUT: {err}", file=sys.stderr)
            return 1
        print(f"{args.bestand}: geldige pagina")
        return 0
    try:
        validate.validate_file(Path(args.bestand), args.schema)
    except validate.ValidationFailed as exc:
        for err in exc.errors:
            print(f"FOUT: {err}", file=sys.stderr)
        return 1
    print(f"{args.bestand}: geldig volgens schema '{args.schema}'")
    return 0


def cmd_source_add(args) -> int:
    repo_root = _repo_root()
    tags = args.tags.split(",") if args.tags else []
    try:
        index_path = sources.add(
            repo_root,
            args.id,
            Path(args.bestand),
            titel=args.titel,
            tags=[t.strip() for t in tags if t.strip()],
            uitgever=args.uitgever or "",
            datum=args.datum or "",
            versie=args.versie or "",
            markdown_override=Path(args.markdown) if args.markdown else None,
        )
    except (sources.SourceExistsError, sources.ConversionError, ValueError) as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    print(f"Bron toegevoegd: {index_path}")
    return 0


def cmd_source_list(args) -> int:
    repo_root = _repo_root()
    tags = args.tags.split(",") if args.tags else None
    for entry in sources.list_sources(repo_root, tags):
        print(f"{entry['id']}\t{entry.get('titel', '')}\t{entry.get('tags', [])}")
    return 0


def cmd_source_show(args) -> int:
    repo_root = _repo_root()
    try:
        entry = sources.read_index_entry(repo_root, args.id)
    except FileNotFoundError:
        print(f"FOUT: onbekende bron '{args.id}'", file=sys.stderr)
        return 1
    print(json.dumps(entry, indent=2, ensure_ascii=False))
    return 0


def cmd_run_start(args) -> int:
    wiki_root = _wiki_root(args)
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    try:
        state = runs.start(wiki_root, wiki_yaml, args.workflow, onderwerp=args.onderwerp)
    except runs.RunError as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    print(f"Run gestart: {state['run_id']}")
    return 0


def cmd_run_status(args) -> int:
    wiki_root = _wiki_root(args)
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    run_id = args.run or runs.find_open_run(wiki_root)
    if run_id is None:
        print("Geen runs gevonden.")
        return 0
    state = runs.load_state(wiki_root, run_id)
    nxt = runs.next_phase(state, wiki_yaml)
    print(f"Run: {run_id}")
    print(f"Volgende fase: {nxt or '(afgerond)'}")
    for naam, info in state["fasen"].items():
        print(f"  {naam}: {info['status']}")
    return 0


def cmd_run_complete(args) -> int:
    wiki_root = _wiki_root(args)
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    try:
        runs.complete(wiki_root, wiki_yaml, args.run, args.phase, Path(args.data) if args.data else None)
    except (runs.RunError, validate.ValidationFailed) as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    print(f"Fase '{args.phase}' afgerond voor run {args.run}")
    return 0


def cmd_run_resume(args) -> int:
    return cmd_run_status(args)


def cmd_run_close(args) -> int:
    wiki_root = _wiki_root(args)
    try:
        runs.close(wiki_root, args.run, args.besluit)
    except runs.RunError as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    print(f"Run {args.run} gesloten zonder publicatie: {args.besluit}")
    return 0


def cmd_run_abandon(args) -> int:
    wiki_root = _wiki_root(args)
    try:
        runs.abandon(wiki_root, args.run)
    except runs.RunError as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    print(f"Run {args.run} afgebroken; kladblok verwijderd, wiki ongewijzigd.")
    return 0


def cmd_run_prune(args) -> int:
    wiki_root = _wiki_root(args)
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    retention = wiki_yaml.get("work", {}).get("retention_days", 30)
    removed = runs.prune(wiki_root, wiki_yaml, retention)
    print(f"Opgeschoond: {removed}" if removed else "Niets om op te schonen")
    return 0


def _gate_command(args, action: str) -> int:
    wiki_root = _wiki_root(args)
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    command = args.command  # "promote" or "publish"
    try:
        if action == "plan":
            path = gate.plan(wiki_root, wiki_yaml, args.run)
            print(f"Voorstel klaar: {path}")
        else:
            path = gate.apply(wiki_root, wiki_yaml, args.run, akkoord_woord=args.akkoord_woord)
            print(f"{command} toegepast, voorstel: {path}")
    except NotImplementedError as exc:
        print(f"NOG NIET BESCHIKBAAR: {exc}", file=sys.stderr)
        return 2
    except (gate.GateError, runs.RunError, validate.ValidationFailed) as exc:
        print(f"GEWEIGERD: {exc}", file=sys.stderr)
        return 1
    return 0


def cmd_workspace_check(args) -> int:
    repo_root = _repo_root()
    result = workspace_check.check(repo_root, fix=args.fix)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(workspace_check.format_text(result))
    return 0 if result["status"] != "actie gebruiker" else 1


def cmd_voortgang(args) -> int:
    wiki_root = _wiki_root(args)
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    path = logbook.regenerate(wiki_root, wiki_yaml)
    print(f"Bijgewerkt: {path}")
    return 0


def _git_changed_paths(repo_root: Path, statuses: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-status"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    changed = []
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2 and parts[0][0] in statuses:
            changed.append(parts[-1])
    return changed


def cmd_precommit_sources(args) -> int:
    repo_root = _repo_root()
    changed = _git_changed_paths(repo_root, "MD")
    errors = lint.check_sources_immutable(repo_root, changed)
    for err in errors:
        print(f"FOUT: {err}", file=sys.stderr)
    return 1 if errors else 0


def cmd_precommit_goedgekeurd(args) -> int:
    repo_root = _repo_root()
    errors = lint.check_goedgekeurd_guard(repo_root)
    for err in errors:
        print(f"FOUT: {err}", file=sys.stderr)
    return 1 if errors else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="llmwiki")
    parser.add_argument("--version", action="store_true", help="Toon de versie en stop")
    sub = parser.add_subparsers(dest="command")

    def add_wiki_arg(p):
        p.add_argument("--wiki", help="Pad naar de wiki-map (standaard: omhoog zoeken vanaf de werkmap)")

    p_lint = sub.add_parser("lint", help="Controleer skills en afhankelijkheidsrichting")
    p_lint.set_defaults(func=cmd_lint)

    p_validate = sub.add_parser("validate", help="Valideer een artefact tegen een schema")
    p_validate.add_argument("bestand")
    p_validate.add_argument("--schema", required=True, help="Schemanaam, of 'page' voor een Markdown-pagina")
    add_wiki_arg(p_validate)
    p_validate.set_defaults(func=cmd_validate)

    p_source = sub.add_parser("source", help="Bronbeheer")
    source_sub = p_source.add_subparsers(dest="source_command", required=True)

    p_source_add = source_sub.add_parser("add")
    p_source_add.add_argument("bestand")
    p_source_add.add_argument("--id", required=True)
    p_source_add.add_argument("--titel", required=True)
    p_source_add.add_argument("--tags", default="")
    p_source_add.add_argument("--uitgever", default="")
    p_source_add.add_argument("--datum", default="")
    p_source_add.add_argument("--versie", default="")
    p_source_add.add_argument("--markdown", help="Vooraf geconverteerd Markdown-bestand, indien geen automatische conversie mogelijk is")
    p_source_add.set_defaults(func=cmd_source_add)

    p_source_list = source_sub.add_parser("list")
    p_source_list.add_argument("--tags", default="")
    p_source_list.set_defaults(func=cmd_source_list)

    p_source_show = source_sub.add_parser("show")
    p_source_show.add_argument("id")
    p_source_show.set_defaults(func=cmd_source_show)

    p_run = sub.add_parser("run", help="Run-State beheren")
    run_sub = p_run.add_subparsers(dest="run_command", required=True)

    p_run_start = run_sub.add_parser("start")
    add_wiki_arg(p_run_start)
    p_run_start.add_argument("--workflow", required=True)
    p_run_start.add_argument("--onderwerp")
    p_run_start.set_defaults(func=cmd_run_start)

    p_run_status = run_sub.add_parser("status")
    add_wiki_arg(p_run_status)
    p_run_status.add_argument("--run")
    p_run_status.set_defaults(func=cmd_run_status)

    p_run_complete = run_sub.add_parser("complete")
    add_wiki_arg(p_run_complete)
    p_run_complete.add_argument("phase")
    p_run_complete.add_argument("--run", required=True)
    p_run_complete.add_argument("--data")
    p_run_complete.set_defaults(func=cmd_run_complete)

    p_run_resume = run_sub.add_parser("resume")
    add_wiki_arg(p_run_resume)
    p_run_resume.add_argument("run")
    p_run_resume.set_defaults(func=lambda args: cmd_run_status(argparse.Namespace(wiki=args.wiki, run=args.run)))

    p_run_close = run_sub.add_parser("close")
    add_wiki_arg(p_run_close)
    p_run_close.add_argument("run")
    p_run_close.add_argument("--besluit", required=True)
    p_run_close.set_defaults(func=cmd_run_close)

    p_run_abandon = run_sub.add_parser("abandon")
    add_wiki_arg(p_run_abandon)
    p_run_abandon.add_argument("run")
    p_run_abandon.set_defaults(func=cmd_run_abandon)

    p_run_prune = run_sub.add_parser("prune")
    add_wiki_arg(p_run_prune)
    p_run_prune.set_defaults(func=cmd_run_prune)

    for name in ("promote", "publish"):
        p_gate = sub.add_parser(name, help=f"{name}-gate (plan/apply)")
        gate_sub = p_gate.add_subparsers(dest="gate_command", required=True)

        p_plan = gate_sub.add_parser("plan")
        add_wiki_arg(p_plan)
        p_plan.add_argument("--run", required=True)
        p_plan.set_defaults(func=lambda args: _gate_command(args, "plan"), command=name)

        p_apply = gate_sub.add_parser("apply")
        add_wiki_arg(p_apply)
        p_apply.add_argument("--run", required=True)
        p_apply.add_argument("--akkoord-woord", dest="akkoord_woord")
        p_apply.set_defaults(func=lambda args: _gate_command(args, "apply"), command=name)

    p_workspace_check = sub.add_parser("workspace-check", help="Werkplekcontrole")
    p_workspace_check.add_argument("--json", action="store_true")
    p_workspace_check.add_argument("--fix", action="store_true")
    p_workspace_check.set_defaults(func=cmd_workspace_check)

    p_voortgang = sub.add_parser("voortgang", help="Regenereer voortgang.md")
    add_wiki_arg(p_voortgang)
    p_voortgang.set_defaults(func=cmd_voortgang)

    p_precommit = sub.add_parser("precommit", help="Controles voor de pre-commit-hook")
    precommit_sub = p_precommit.add_subparsers(dest="precommit_command", required=True)
    p_pc_sources = precommit_sub.add_parser("sources-immutable")
    p_pc_sources.set_defaults(func=cmd_precommit_sources)
    p_pc_goedgekeurd = precommit_sub.add_parser("goedgekeurd-guard")
    p_pc_goedgekeurd.set_defaults(func=cmd_precommit_goedgekeurd)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.version:
        return cmd_version(args)
    if not getattr(args, "func", None):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
