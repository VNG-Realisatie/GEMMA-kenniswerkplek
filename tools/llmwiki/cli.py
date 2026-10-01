"""Command-line interface voor llmwiki. Zie ARCHITECTURE.md en docs/onderbouwing.md."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from . import akkoord, __version__, gate, harness, lint, logbook, paths, runs, sources, sync as sync_module, validate, workspace_check


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


def cmd_ontvouw(args) -> int:
    from . import markdown

    repo_root = _repo_root()
    paden = [Path(p).resolve() for p in args.paden] if args.paden else markdown.te_ontvouwen(repo_root)
    gewijzigd = []
    for pad in paden:
        oud = pad.read_text(encoding="utf-8")
        nieuw = markdown.ontvouw(oud)
        if nieuw != oud:
            gewijzigd.append(pad)
            if args.schrijf:
                pad.write_text(nieuw, encoding="utf-8", newline="\n")
    for pad in gewijzigd:
        print(f"{'aangepast' if args.schrijf else 'te ontvouwen'}: {pad.relative_to(repo_root) if pad.is_relative_to(repo_root) else pad}")
    if not gewijzigd:
        print("llmwiki ontvouw: geen harde regelovergangen gevonden")
    return 1 if gewijzigd and not args.schrijf else 0


def cmd_validate(args) -> int:
    if args.schema == "page":
        wiki_root = _wiki_root(args)
        wiki_yaml = paths.load_wiki_yaml(wiki_root)
        doelpad, bestaande = None, set()
        if args.run:
            doelpad, bestaande = validate.changeset_context(
                wiki_root, runs.run_dir(wiki_root, args.run), Path(args.bestand)
            )
        errors = validate.validate_page(
            wiki_root, Path(args.bestand), wiki_yaml, doelpad=doelpad, bestaande_paden=bestaande
        )
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
    if bool(args.bestand) == bool(args.url):
        print("FOUT: geef precies één van <bestand> of --url op", file=sys.stderr)
        return 1
    kwargs = dict(
        titel=args.titel,
        tags=[t.strip() for t in tags if t.strip()],
        uitgever=args.uitgever or "",
        datum=args.datum or "",
        versie=args.versie or "",
        brontype=args.brontype or "",
        beschrijving=args.beschrijving or "",
        url_pagina=args.url_pagina or "",
        markdown_override=Path(args.markdown) if args.markdown else None,
    )
    try:
        if args.url:
            werkmap = repo_root / ".work" / "source-add"
            index_path = sources.add_from_url(repo_root, args.id, args.url, werkmap, **kwargs)
        else:
            index_path = sources.add(repo_root, args.id, Path(args.bestand), **kwargs)
    except (sources.SourceExistsError, sources.ConversionError, ValueError) as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # FetchError e.d.: in gewone taal melden, geen traceback
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    print(f"Bron toegevoegd: {index_path}")
    return 0


def cmd_source_list(args) -> int:
    repo_root = _repo_root()
    tags = args.tags.split(",") if args.tags else None
    for entry in sources.list_sources(repo_root, tags):
        print(f"{entry['id']}\t{entry.get('brontype', '-')}\t{entry.get('titel', '')}\t{entry.get('tags', [])}")
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


def cmd_source_inhoud(args) -> int:
    try:
        if args.schrijf:
            print(f"Inhoud bijgewerkt: {sources.schrijf_inhoud(_repo_root(), args.id, args.niveau)}")
        else:
            sys.stdout.reconfigure(encoding="utf-8")
            print(sources.inhoud_markdown(_repo_root(), args.id, args.niveau), end="")
    except FileNotFoundError as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
    return 0


def cmd_source_bronregel(args) -> int:
    try:
        if args.schrijf:
            sources.schrijf_bronregel(_repo_root(), args.id, Path(args.van))
            print(f"Bronregel gezet: {args.van}")
        else:
            sys.stdout.reconfigure(encoding="utf-8")
            print(sources.bronregel(_repo_root(), args.id, Path(args.van)))
    except (FileNotFoundError, ValueError) as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1
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


def _parse_titel_overrides(pairs: list[str] | None) -> dict[str, str]:
    overrides = {}
    for pair in pairs or []:
        pad, _, titel = pair.partition("=")
        if not titel:
            raise SystemExit(f"--titel verwacht pad=Titel, kreeg: {pair!r}")
        overrides[pad] = titel
    return overrides


def _akkoord_command(wiki_root: Path, wiki_yaml: dict, args, action: str) -> int:
    """promote voor een curatie-wiki met beoordelingen: geen run, akkoord in de chat (zie akkoord.py)."""
    try:
        if action == "plan":
            s = akkoord.plan(wiki_root, wiki_yaml, getattr(args, "onderwerp", None))
            print(f"Klaar voor akkoord: {len(s['te_keuren'])} element(en) op review.")
            for e in s["te_keuren"]:
                print(f"- {e['naam']} ({e['type']}){', eerder goedgekeurd en gewijzigd' if e['eerder_goedgekeurd'] else ', nieuw'}")
            if s["voor_te_leggen"]:
                print(f"Nog voor te leggen (blijft buiten dit akkoord): {', '.join(s['voor_te_leggen'])}.")
            print("Overzicht: ter-beoordeling.md. Bekijk de pagina's en de wijzigingen in Source Control; "
                  "het akkoord is het woord AKKOORD in de chat.")
        else:
            ids = akkoord.apply(wiki_root, wiki_yaml, args.akkoord_woord)
            print(f"Goedgekeurd: {', '.join(ids)}. Vastgelegd in log.md; pagina's opnieuw gerenderd.")
    except akkoord.AkkoordFout as exc:
        print(f"GEWEIGERD: {exc}", file=sys.stderr)
        return 1
    return 0


def _gate_command(args, action: str) -> int:
    wiki_root = _wiki_root(args)
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    command = args.command  # "promote" or "publish"
    if command == "promote" and akkoord.van_toepassing(wiki_yaml):
        return _akkoord_command(wiki_root, wiki_yaml, args, action)
    if not getattr(args, "run", None):
        print("GEWEIGERD: --run <run-id> is verplicht", file=sys.stderr)
        return 1
    doel = getattr(args, "doel", None) or "site"
    try:
        if action == "plan":
            path = gate.plan(
                wiki_root,
                wiki_yaml,
                args.run,
                doel=doel,
                paths=getattr(args, "pad", None) or None,
                titel_overrides=_parse_titel_overrides(getattr(args, "titel", None)),
            )
            print(f"Voorstel klaar: {path}")
        else:
            path = gate.apply(wiki_root, wiki_yaml, args.run, akkoord_woord=args.akkoord_woord, doel=doel)
            print(f"{command} toegepast, voorstel: {path}")
    except (gate.GateError, runs.RunError, sync_module.SyncError, validate.ValidationFailed) as exc:
        print(f"GEWEIGERD: {exc}", file=sys.stderr)
        return 1
    return 0


def _revisions_path(wiki_root: Path, doel: str) -> Path:
    return wiki_root / "revisies.json" if doel == "site" else wiki_root / ".work" / "sync" / f"{doel}.json"


def _doelmap(wiki_root: Path, doel: str) -> Path:
    """Waar een pull de opgehaalde bestanden neerzet. Het hoofddoel vult de werkkopie content/; een testdoel
    (bv. staging, een oudere kopie) schrijft naar .work/sync/<doel>/ en overschrijft de werkkopie dus nooit.
    De revisies blijven per doel gesleuteld op het content/-pad, zodat publish naar dat doel ze vindt."""
    return wiki_root if doel == "site" else wiki_root / ".work" / "sync" / doel


def _load_revisions(wiki_root: Path, doel: str) -> dict:
    path = _revisions_path(wiki_root, doel)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _save_revisions(wiki_root: Path, doel: str, revisions: dict) -> None:
    path = _revisions_path(wiki_root, doel)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(revisions, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8", newline="\n")


def _has_uncommitted_changes(wiki_root: Path, pad: str) -> bool:
    status = subprocess.run(
        ["git", "-C", str(wiki_root), "status", "--porcelain", "--", pad],
        capture_output=True, text=True, check=False,
    ).stdout
    return bool(status.strip())


def _categorie_voorrang_path(wiki_root: Path) -> Path:
    return wiki_root / "content" / ".categorie-voorrang.json"


def _load_categorie_voorrang(wiki_root: Path) -> list[str]:
    path = _categorie_voorrang_path(wiki_root)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


def _geef_voorrang(wiki_root: Path, categorie: str) -> None:
    """Eenmaal gekozen (automatisch bij precies 1 categorie, of expliciet via
    --categorie) krijgt een categorie voorrang bij een volgende, op zichzelf
    ambigue pagina. Alleen platte namen (geen '/'-nesting via --categorie),
    want dat is wat page_categories() teruggeeft om tegen te vergelijken."""
    if "/" in categorie:
        return
    voorrang = _load_categorie_voorrang(wiki_root)
    if categorie not in voorrang:
        voorrang.append(categorie)
        _categorie_voorrang_path(wiki_root).write_text(
            json.dumps(voorrang, indent=2, ensure_ascii=False), encoding="utf-8"
        )


def _resolve_categorie_pad(
    wiki_root: Path, site, wiki_yaml: dict, titel: str, categorie_arg: str | None
) -> list[str] | None:
    """0 categorieën -> geen categoriemap; 1 -> automatisch; meer -> beslist
    voorrang (content/.categorie-voorrang.json) als precies één van de
    categorieën al voorrang heeft; anders (of bij >=2 voorrangscategorieën)
    vereist het --categorie (navragen, niet gokken; zie AGENTS.md wikis/gemma-online).
    Een nieuw opgeloste categorie krijgt zelf voorrang voor de volgende keer."""
    if wiki_yaml.get("content", {}).get("layout") != "category":
        if categorie_arg:
            raise sync_module.SyncError("--categorie is alleen van toepassing bij content.layout: category in wiki.yaml")
        return None
    if categorie_arg:
        _geef_voorrang(wiki_root, categorie_arg.split("/")[0])
        return categorie_arg.split("/")

    categorieen = sync_module.page_categories(site, titel)
    if not categorieen:
        return None
    if len(categorieen) == 1:
        _geef_voorrang(wiki_root, categorieen[0])
        return [categorieen[0]]

    voorrang = _load_categorie_voorrang(wiki_root)
    treffers = [c for c in categorieen if c in voorrang]
    if len(treffers) == 1:
        return [treffers[0]]

    detail = f" -- {len(treffers)} daarvan hebben al voorrang: {', '.join(treffers)}" if len(treffers) > 1 else ""
    raise sync_module.SyncError(
        f"'{titel}' heeft {len(categorieen)} categorieën ({', '.join(categorieen)}); "
        f"geef er één mee met --categorie (evt. genest: 'Boven/Onder'){detail}"
    )


def cmd_pull(args) -> int:
    wiki_root = _wiki_root(args)
    wiki_yaml = paths.load_wiki_yaml(wiki_root)
    doel = args.doel or "site"
    try:
        site = sync_module.get_site(wiki_yaml, doel)
    except sync_module.SyncError as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1

    if args.categorieboom:
        return _pull_categorieboom(wiki_root, wiki_yaml, site, doel, args)

    from . import titles as titles_module

    try:
        categorie_pad = _resolve_categorie_pad(wiki_root, site, wiki_yaml, args.titel, args.categorie)
        result = sync_module.pull_page(site, args.titel)
    except sync_module.SyncError as exc:
        print(f"FOUT: {exc}", file=sys.stderr)
        return 1

    pad = "content/" + titles_module.title_to_path(result.title, result.namespace, result.contentmodel, categorie_pad)
    target = _doelmap(wiki_root, doel) / pad
    if doel == "site" and target.exists() and not args.force and _has_uncommitted_changes(wiki_root, pad):
        print(f"FOUT: {pad} heeft niet-gecommitteerde wijzigingen; gebruik --force om te overschrijven", file=sys.stderr)
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(result.text, encoding="utf-8", newline="\n")

    revisions = _load_revisions(wiki_root, doel)
    revisions[pad] = {"titel": result.title, "revid": result.revid}
    _save_revisions(wiki_root, doel, revisions)

    print(f"Opgehaald: {target.relative_to(wiki_root).as_posix()}")
    return 0


def _pull_categorieboom(wiki_root: Path, wiki_yaml: dict, site, doel: str, args) -> int:
    """Haalt Categorie:<root> en al haar subcategorieën recursief op (bulk-
    import), inclusief subpagina's (harde link, altijd mee, ongeacht status of
    eigen categorie). `--skip-if-match <regex>` is generiek: llmwiki kent geen
    wiki-specifieke velden zoals GEMMA's Redactiestatus, een wiki-Skill geeft
    dat patroon desgewenst mee. Een titel die al bekend is op een ánder pad
    (bv. via een eerdere --titel/--categorieboom-pull, zoals een pagina met
    meerdere categorieën die zowel los als via deze boom wordt gevonden)
    wordt nooit gedupliceerd naar een tweede plek -- overgeslagen, gemeld als
    'elders bekend'. Nog niet gebouwd: die bestaande plek automatisch
    verplaatsen als de categorisering op de site wijzigt (bekende beperking)."""
    import re

    from . import titles as titles_module

    if wiki_yaml.get("content", {}).get("layout") != "category":
        print("FOUT: --categorieboom vereist content.layout: category in wiki.yaml", file=sys.stderr)
        return 1
    toegestane_namespaces = set(wiki_yaml.get("content", {}).get("namespaces", [0]))
    skip_re = re.compile(args.skip_if_match) if args.skip_if_match else None

    resultaten: dict[str, sync_module.PageResult] = {}
    mislukt: list[str] = []

    def _haal_op(titel: str) -> sync_module.PageResult | None:
        if titel not in resultaten:
            try:
                resultaten[titel] = sync_module.pull_page(site, titel)
            except sync_module.SyncError as exc:
                mislukt.append(f"{titel}: {exc}")
                return None
        return resultaten[titel]

    categorie_pad_by_titel: dict[str, list[str]] = {}
    overgeslagen_status: list[str] = []
    for entry in sync_module.category_tree(site, args.categorieboom):
        if entry.namespace not in toegestane_namespaces or entry.titel in categorie_pad_by_titel:
            continue
        result = _haal_op(entry.titel)
        if result is None:
            continue
        if skip_re and skip_re.search(result.text):
            overgeslagen_status.append(entry.titel)
            continue
        categorie_pad_by_titel[entry.titel] = entry.categorie_pad
        for sub_titel in sync_module.subpage_titles(site, entry.titel):
            if sub_titel not in categorie_pad_by_titel:
                categorie_pad_by_titel[sub_titel] = entry.categorie_pad

    paden_by_titel = {}
    for titel, categorie_pad in categorie_pad_by_titel.items():
        result = _haal_op(titel)
        if result is None:
            continue
        paden_by_titel[titel] = titles_module.title_to_path(
            titel, result.namespace, result.contentmodel, categorie_pad
        )
    paden_by_titel = titles_module.apply_index_convention(paden_by_titel)

    revisions = _load_revisions(wiki_root, doel)
    bekend_pad_by_titel = {info.get("titel"): pad for pad, info in revisions.items()}
    geschreven, overgeslagen_lokaal, overgeslagen_elders = [], [], []
    for titel, pad_rel in sorted(paden_by_titel.items()):
        pad = "content/" + pad_rel
        bekend_pad = bekend_pad_by_titel.get(titel)
        if bekend_pad and bekend_pad != pad:
            overgeslagen_elders.append(f"{titel} (al op {bekend_pad}, niet gedupliceerd naar {pad})")
            continue
        target = _doelmap(wiki_root, doel) / pad
        if doel == "site" and target.exists() and not args.force and _has_uncommitted_changes(wiki_root, pad):
            overgeslagen_lokaal.append(pad)
            continue
        result = resultaten[titel]
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(result.text, encoding="utf-8", newline="\n")
            revisions[pad] = {"titel": result.title, "revid": result.revid}
        bekend_pad_by_titel[titel] = pad
        geschreven.append(pad)

    if not args.dry_run:
        _save_revisions(wiki_root, doel, revisions)

    label = "Zou ophalen" if args.dry_run else "Opgehaald"
    for pad in geschreven:
        print(f"{label}: {pad}")
    for titel in overgeslagen_status:
        print(f"Overgeslagen (skip-if-match): {titel}")
    for melding in overgeslagen_elders:
        print(f"Overgeslagen (elders bekend): {melding}")
    for pad in overgeslagen_lokaal:
        print(f"Overgeslagen (niet-gecommitteerde lokale wijzigingen, gebruik --force): {pad}")
    for msg in mislukt:
        print(f"MISLUKT: {msg}", file=sys.stderr)
    print(
        f"Totaal: {len(geschreven)} {'te halen' if args.dry_run else 'opgehaald'}, "
        f"{len(overgeslagen_status) + len(overgeslagen_elders) + len(overgeslagen_lokaal)} overgeslagen, {len(mislukt)} mislukt"
    )
    return 1 if mislukt else 0


def cmd_harness_sync(args) -> int:
    repo_root = _repo_root()
    verslag = harness.sync(repo_root)
    print(f"Brug: {len(verslag['bruggen'])} skill(s), gegenereerd: {len(verslag['bestanden'])} bestand(en)")
    for brug in verslag["bruggen"]:
        print(f"  {brug['skill']} -> {brug['doel']} ({brug['methode']})")
    return 0


def cmd_harness_check(args) -> int:
    repo_root = _repo_root()
    problems = harness.check(repo_root, bruggen=not args.zonder_bruggen)
    if problems:
        for p in problems:
            print(f"FOUT: {p}", file=sys.stderr)
        return 1
    print("llmwiki harness check: geen problemen gevonden")
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
    if akkoord.van_toepassing(wiki_yaml):
        print(akkoord.draai_script(wiki_root, wiki_yaml, "render").strip())
        return 0
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


def cmd_precommit_render(args) -> int:
    """Elke gegenereerde pagina is gelijk aan wat het render-script van de wiki uit de beoordelingen maakt."""
    fouten = 0
    for wiki_root, wiki_yaml in akkoord.wiki_roots(_repo_root()):
        try:
            akkoord.draai_script(wiki_root, wiki_yaml, "render", "--check")
        except akkoord.AkkoordFout as exc:
            print(f"FOUT: {exc}", file=sys.stderr)
            fouten += 1
    return 1 if fouten else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="llmwiki")
    parser.add_argument("--version", action="store_true", help="Toon de versie en stop")
    sub = parser.add_subparsers(dest="command")

    def add_wiki_arg(p):
        p.add_argument("--wiki", help="Pad naar de wiki-map (standaard: omhoog zoeken vanaf de werkmap)")

    p_lint = sub.add_parser("lint", help="Controleer skills en afhankelijkheidsrichting")
    p_lint.set_defaults(func=cmd_lint)

    p_ontvouw = sub.add_parser("ontvouw", help="Verwijder harde regelovergangen binnen alinea's en lijstitems (Markdown)")
    p_ontvouw.add_argument("paden", nargs="*", help="Bestanden; standaard alle Markdown waarvoor de regel geldt")
    p_ontvouw.add_argument("--schrijf", action="store_true", help="Pas de bestanden aan (anders alleen melden)")
    p_ontvouw.set_defaults(func=cmd_ontvouw)

    p_validate = sub.add_parser("validate", help="Valideer een artefact tegen een schema")
    p_validate.add_argument("bestand")
    p_validate.add_argument(
        "--schema", required=True,
        help="Schemanaam, of 'page' voor een pagina van deze wiki (wikitext bij sync, Markdown bij curation/knowledge-base)",
    )
    p_validate.add_argument(
        "--run",
        help="Run-id: een gestaged bestand wordt dan beoordeeld op zijn doelpad uit changeset.json "
        "(id-controle, relatieve links; andere pagina's uit dezelfde changeset gelden als bestaand)",
    )
    add_wiki_arg(p_validate)
    p_validate.set_defaults(func=cmd_validate)

    p_source = sub.add_parser("source", help="Bronbeheer")
    source_sub = p_source.add_subparsers(dest="source_command", required=True)

    p_source_add = source_sub.add_parser("add")
    p_source_add.add_argument("bestand", nargs="?", help="Lokaal bestand (pdf, docx, html, md); of gebruik --url")
    p_source_add.add_argument("--url", help="Haal de bron op via deze URL (letterlijke kopie, geen samenvatting)")
    p_source_add.add_argument("--url-pagina", dest="url_pagina", help="Pagina waarop de link naar deze bron stond")
    p_source_add.add_argument("--brontype", choices=list(sources.BRONTYPEN))
    p_source_add.add_argument("--beschrijving", default="", help="Korte beschrijving, max. 1 zin")
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

    p_source_inhoud = source_sub.add_parser("inhoud", help="Inhoudsopgave van laag 1 (koppen, regelnummers, woorden) voor de index")
    p_source_inhoud.add_argument("id")
    p_source_inhoud.add_argument("--niveau", type=int, default=3, help="Diepste kopniveau (standaard 3)")
    p_source_inhoud.add_argument("--schrijf", action="store_true", help="Zet de sectie '## Inhoud' in sources/index/<id>.md")
    p_source_inhoud.set_defaults(func=cmd_source_inhoud)

    p_source_bronregel = source_sub.add_parser("bronregel", help="Linkregel naar laag 1 voor een domein-lens")
    p_source_bronregel.add_argument("id")
    p_source_bronregel.add_argument("--van", required=True, help="Pad van de pagina waarin de regel komt")
    p_source_bronregel.add_argument("--schrijf", action="store_true", help="Zet de regel onder de titel van de pagina --van")
    p_source_bronregel.set_defaults(func=cmd_source_bronregel)

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

    p_pull = sub.add_parser("pull", help="Haal een pagina op van een sync-wiki")
    add_wiki_arg(p_pull)
    p_pull_bron = p_pull.add_mutually_exclusive_group(required=True)
    p_pull_bron.add_argument("--titel", help="Eén pagina")
    p_pull_bron.add_argument(
        "--categorieboom",
        help="Bulk: deze categorie en al haar subcategorieën/leden/subpagina's (content.layout: category)",
    )
    p_pull.add_argument(
        "--categorie",
        help="Bij --titel en content.layout: category: forceer/kies de categoriemap (evt. genest 'Boven/Onder'); "
        "verplicht als de pagina meer dan één categorie heeft",
    )
    p_pull.add_argument(
        "--skip-if-match",
        help="Alleen bij --categorieboom: sla een categorielid over als zijn wikitext dit regex-patroon bevat "
        "(bv. een wiki-specifiek archiefstatusveld); subpagina's worden nooit op basis hiervan overgeslagen",
    )
    p_pull.add_argument("--dry-run", action="store_true", help="Alleen bij --categorieboom: toon wat er zou gebeuren")
    p_pull.add_argument("--doel", help="Naam uit wiki.yaml test_targets, standaard het hoofddoel; "
                        "een testdoel schrijft naar .work/sync/<doel>/, niet naar de werkkopie content/")
    p_pull.add_argument("--force", action="store_true")
    p_pull.set_defaults(func=cmd_pull)

    for name in ("promote", "publish"):
        p_gate = sub.add_parser(name, help=f"{name}-gate (plan/apply)")
        gate_sub = p_gate.add_subparsers(dest="gate_command", required=True)

        p_plan = gate_sub.add_parser("plan")
        add_wiki_arg(p_plan)
        p_plan.add_argument("--run", help="Run-id; niet bij een curatie-wiki met beoordelingen")
        p_plan.add_argument("--onderwerp", help="(curatie met beoordelingen) alleen de beoordelingen van dit onderwerp")
        p_plan.add_argument("--doel", help="(sync) naam uit wiki.yaml test_targets, standaard het hoofddoel")
        p_plan.add_argument("--pad", action="append", help="(sync) expliciet content-pad i.p.v. git-detectie; herhaalbaar")
        p_plan.add_argument("--titel", action="append", metavar="pad=Titel", help="(sync) titel-override voor een nieuw pad; herhaalbaar")
        p_plan.set_defaults(func=lambda args: _gate_command(args, "plan"), command=name)

        p_apply = gate_sub.add_parser("apply")
        add_wiki_arg(p_apply)
        p_apply.add_argument("--run", help="Run-id; niet bij een curatie-wiki met beoordelingen")
        p_apply.add_argument("--akkoord-woord", dest="akkoord_woord")
        p_apply.add_argument("--doel", help="(sync) naam uit wiki.yaml test_targets, standaard het hoofddoel")
        p_apply.set_defaults(func=lambda args: _gate_command(args, "apply"), command=name)

    p_harness = sub.add_parser("harness", help="Harness-bindingen genereren/controleren")
    harness_sub = p_harness.add_subparsers(dest="harness_command", required=True)
    p_harness_sync = harness_sub.add_parser("sync")
    p_harness_sync.set_defaults(func=cmd_harness_sync)
    p_harness_check = harness_sub.add_parser("check")
    p_harness_check.add_argument(
        "--zonder-bruggen", action="store_true",
        help="Sla de controle van de skillbruggen in .claude/skills/ over (gitignored; voor CI)",
    )
    p_harness_check.set_defaults(func=cmd_harness_check)

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
    p_pc_render = precommit_sub.add_parser("render-check", help="Gegenereerde pagina's gelijk aan de beoordelingen")
    p_pc_render.set_defaults(func=cmd_precommit_render)

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
