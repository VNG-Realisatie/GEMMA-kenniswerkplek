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
import re
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


def _wordt_goedgekeurd(wiki_yaml: dict, pagina: dict, staged_path: Path) -> bool:
    """Alleen een gecureerde pagina die de AI op `review` zette, wordt bij promotie goedgekeurd.

    Een `kandidaat` (moet nog worden voorgelegd) of `afgewezen` wordt ongewijzigd geschreven.
    Een gestagede `goedgekeurd` is nooit toegestaan: die status zet alleen `promote apply`.
    """
    type_def = wiki_yaml.get("page_types", {}).get(pagina["type"], {})
    if not type_def.get("curated"):
        return False
    status = frontmatter.read(staged_path).meta.get("status")
    if status == "goedgekeurd":
        raise GateError(
            f"{pagina['pad']}: gestaged met status 'goedgekeurd'. Zet de pagina op 'review' "
            "(of laat haar op 'kandidaat'); alleen 'promote apply' keurt goed."
        )
    return status == "review"


def _build_plan_curation(wiki_root: Path, wiki_yaml: dict, run_id: str, final_phase: str) -> dict:
    rdir = runs.run_dir(wiki_root, run_id)
    changeset = _load_json(rdir / "changeset.json")

    entries = []
    for pagina in changeset["paginas"]:
        staged_path = rdir / "changeset" / pagina["staged_bestand"]
        new_content = staged_path.read_text(encoding="utf-8")
        goedkeuren = _wordt_goedgekeurd(wiki_yaml, pagina, staged_path)
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
                "goedkeuren": goedkeuren,
            }
        )

    body = {"run": run_id, "modus": final_phase, "paginas": entries}
    plan_hash = hashing.hash_json(body)
    return {**body, "plan_hash": plan_hash}


def _curation_contents(wiki_root: Path, run_id: str, plan_obj: dict) -> dict[str, tuple[str, str]]:
    """pad → (huidige inhoud, voorgestelde inhoud) voor elke pagina in het plan."""
    rdir = runs.run_dir(wiki_root, run_id)
    changeset = _load_json(rdir / "changeset.json")
    inhoud = {}
    for entry, pagina in zip(plan_obj["paginas"], changeset["paginas"]):
        new_content = (rdir / "changeset" / pagina["staged_bestand"]).read_text(encoding="utf-8")
        old_content = (wiki_root / pagina["pad"]).read_text(encoding="utf-8") if entry["actie"] == "wijzigen" else ""
        inhoud[entry["pad"]] = (old_content, new_content)
    return inhoud


def _materialize_curation(
    wiki_root: Path, wiki_yaml: dict, run_id: str, beoordeeld_door: str, final_phase: str, besluiten: dict[str, str]
) -> None:
    rdir = runs.run_dir(wiki_root, run_id)
    changeset = _load_json(rdir / "changeset.json")
    for pagina in changeset["paginas"]:
        if besluiten[pagina["pad"]] == "overslaan":
            continue
        staged_path = rdir / "changeset" / pagina["staged_bestand"]
        goedkeuren = _wordt_goedgekeurd(wiki_yaml, pagina, staged_path)
        page = frontmatter.read(staged_path)
        if goedkeuren:
            page.meta["status"] = "goedgekeurd"
        target_path = wiki_root / pagina["pad"]
        frontmatter.write(target_path, page)
        new_hash = hashing.hash_text(target_path.read_text(encoding="utf-8"))
        if goedkeuren:
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


def _sync_contents(wiki_root: Path, wiki_yaml: dict, doel: str, plan_obj: dict) -> dict[str, tuple[str, str]]:
    """pad → (live inhoud, voorgestelde inhoud) voor elke pagina in het plan."""
    site = sync_module.get_site(wiki_yaml, doel)
    inhoud = {}
    for entry in plan_obj["paginas"]:
        new_content = (wiki_root / entry["pad"]).read_text(encoding="utf-8")
        old_content = ""
        if entry["actie"] == "wijzigen":
            try:
                old_content = sync_module.pull_page(site, entry["titel"]).text
            except sync_module.SyncError:
                pass  # live pagina niet op te halen voor het voorstel; toon dan de volledige nieuwe tekst
        inhoud[entry["pad"]] = (old_content, new_content)
    return inhoud


def _materialize_sync(
    wiki_root: Path, wiki_yaml: dict, run_id: str, doel: str, beoordeeld_door: str, plan_obj: dict, besluiten: dict[str, str]
) -> None:
    site = sync_module.get_site(wiki_yaml, doel)
    revisies = _load_revisions(wiki_root, doel)
    gelukt: list[str] = []
    try:
        for entry in plan_obj["paginas"]:
            if besluiten[entry["pad"]] == "overslaan":
                continue
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
        mislukt = [e["pad"] for e in plan_obj["paginas"] if e["pad"] not in gelukt and besluiten[e["pad"]] != "overslaan"]
        raise GateError(
            f"Publicatie gedeeltelijk gelukt ({len(gelukt)}/{len(plan_obj['paginas'])}): "
            f"gelukt {gelukt}, mislukt/overgeslagen {mislukt}. Oorzaak: {exc}"
        ) from exc


# --- Gedeeld: het voorstel als leesbaar plan met een besluit per pagina ---
#
# Het voorstel is een gewoon Markdown-bestand, zodat elk harness en elke editor het kan tonen en de
# redacteur het zelf kan bewerken. Per pagina staat één tabelrij met de kolommen Besluit en Opmerking;
# de volledige tekst en de diffs staan apart in `<run-id>-details.md`. De plan-hash dekt alleen de
# inhoud, niet de besluiten: de redacteur mag besluiten en opmerkingen wijzigen zonder het plan te
# breken, en `apply` voert uit wat er op het moment van het akkoord staat.

AANPASSEN = "aanpassen"
OVERSLAAN = "overslaan"
KOLOMMEN = ["Element", "Status", "Samenvatting", "Besluit", "Opmerking"]
# Eerste cel: [naam](<concept> "doelpad")<br>actie · type. De link opent de voorgestelde tekst (bij curatie het
# gestagede bestand in de run, dat al bestaat); de linktitel is het doelpad en de sleutel van de rij.
_ELEMENT_LINK = re.compile(r'\]\(<[^>]*>\s+"([^"]+)"\)')


def _opties(final_phase: str, entry: dict) -> list[str]:
    """Toegestane besluiten voor een pagina; de eerste is de standaard."""
    if final_phase == "publish":
        return ["publiceren", OVERSLAAN, AANPASSEN]
    if entry.get("goedkeuren"):
        return ["goedkeuren", OVERSLAAN, AANPASSEN]
    return ["schrijven", OVERSLAAN, AANPASSEN]


def _cel(tekst: str) -> str:
    return " ".join(str(tekst).split()).replace("|", "\\|")


def _secties(markdown: str) -> dict[str, str]:
    """Koptekst → inhoud, voor Markdown (`## Kop`) en wikitext (`== Kop ==`)."""
    secties: dict[str, list[str]] = {"(begin)": []}
    huidig = "(begin)"
    for regel in markdown.splitlines():
        kop = regel.strip()
        if kop.startswith("#") or (kop.startswith("==") and kop.endswith("==")):
            huidig = kop.strip("#= ").strip()
            secties.setdefault(huidig, [])
        else:
            secties[huidig].append(regel)
    return {k: "\n".join(v).strip() for k, v in secties.items()}


def _samenvatting(old: str, new: str, actie: str) -> tuple[dict, str, list[str]]:
    """(frontmatter, samenvatting in één regel, open vragen uit '## Ter discussie')."""
    page = frontmatter.parse(new)
    meta = page.meta
    tekst = meta.get("definitie") or meta.get("beschrijving") or meta.get("samenvatting") or ""
    if not tekst:
        eerste = [r.strip() for r in page.body.splitlines() if r.strip() and not r.lstrip().startswith(("#", "|", "=", "-", "{", "<"))]
        tekst = eerste[0] if eerste else ""
    if len(tekst) > 200:
        tekst = tekst[:197].rstrip() + "…"
    if actie == "wijzigen":
        oud, nieuw = _secties(frontmatter.parse(old).body), _secties(page.body)
        gewijzigd = [k for k in nieuw if k != "(begin)" and oud.get(k) != nieuw[k]]
        weg = [k for k in oud if k not in nieuw]
        delen = []
        if frontmatter.parse(old).meta != meta:
            delen.append("gegevens")
        delen += gewijzigd + [f"{k} (vervalt)" for k in weg]
        tekst = f"Wijzigt: {', '.join(delen) or 'alleen opmaak'}. {tekst}".strip()
    vragen = [r.strip()[2:] for r in _secties(page.body).get("Ter discussie", "").splitlines() if r.strip().startswith("- ")]
    return meta, tekst, vragen


def _vorige_besluiten(voorstel_path: Path, oud_plan_path: Path) -> tuple[dict[str, tuple[str, str]], dict[str, str]]:
    """(besluiten, inhoud-hashes) uit het vorige voorstel; 'aanpassen' telt niet mee, die pagina is herzien."""
    if not (voorstel_path.exists() and oud_plan_path.exists()):
        return {}, {}
    try:
        oud_plan = _load_json(oud_plan_path)
        rijen = _lees_tabel(voorstel_path.read_text(encoding="utf-8"))
    except (ValueError, KeyError, json.JSONDecodeError):
        return {}, {}
    hashes = {e["pad"]: e.get("nieuwe_hash") for e in oud_plan.get("paginas", [])}
    return {pad: (b, o) for pad, (b, o) in rijen.items() if b != AANPASSEN}, hashes


def _render_plan(
    run_id: str, final_phase: str, plan_obj: dict, inhoud: dict[str, tuple[str, str]], links: dict[str, str], vorige: dict, oude_hashes: dict
) -> tuple[list[str], list[str]]:
    """(regels van het plan, regels van het detailbestand); `links`: pad → link vanuit voorstellen/ naar de voorgestelde tekst."""
    groepen: dict[str, list[str]] = {"goed": [], "overig": []}
    vragen_per_pagina: list[tuple[str, list[str]]] = []
    details = [f"# Details bij voorstel {run_id}", "", "Volledige wijziging per pagina. Beoordelen en besluiten doe je in het voorstel zelf.", ""]
    for entry in plan_obj["paginas"]:
        pad, actie = entry["pad"], entry["actie"]
        old, new = inhoud[pad]
        meta, samenvatting, vragen = _samenvatting(old, new, actie) if final_phase != "publish" else ({}, "", [])
        if final_phase == "publish":
            regels_oud, regels_nieuw = old.splitlines(), new.splitlines()
            verschil = sum(1 for r in difflib.ndiff(regels_oud, regels_nieuw) if r[:1] in "+-")
            samenvatting = "Nieuwe pagina." if actie == "nieuw" else f"{verschil} regels gewijzigd."
        naam = entry.get("titel") or meta.get("naam") or meta.get("titel") or meta.get("id") or Path(pad).stem
        opties = _opties(final_phase, entry)
        besluit, opmerking = opties[0], ""
        if pad in vorige and oude_hashes.get(pad) == entry.get("nieuwe_hash") and vorige[pad][0] in opties:
            besluit, opmerking = vorige[pad]
        soort = " · ".join(x for x in (actie, meta.get("type", "")) if x)
        element = f"[{str(naam).replace('[', '(').replace(']', ')')}](<{links[pad]}> \"{pad}\")<br>{soort}"
        rij = [element, meta.get("status", ""), samenvatting, besluit, opmerking]
        groep = "goed" if entry.get("goedkeuren") or final_phase == "publish" else "overig"
        groepen[groep].append("| " + " | ".join(_cel(c) for c in rij) + " |")
        if vragen:
            vragen_per_pagina.append((naam, vragen))
        diff = "\n".join(difflib.unified_diff(old.splitlines(), new.splitlines(), fromfile="huidig", tofile="voorstel", lineterm=""))
        details += [f"## {naam} (`{pad}`, {actie})", "", "```diff", diff or "(geen inhoudelijke wijziging)", "```", ""]

    kop = "| " + " | ".join(KOLOMMEN) + " |\n|" + "---|" * len(KOLOMMEN)
    werkwoord = "gepubliceerd" if final_phase == "publish" else "geschreven"
    lines = [
        f"# Voorstel {run_id}",
        "",
        f"Modus: {final_phase}. {len(plan_obj['paginas'])} pagina's. Volledige tekst en diffs: [details]({run_id}-details.md).",
        "",
        "## Zo beoordeel je dit plan",
        "",
        "1. Loop de tabellen door. Pas per pagina de kolom **Besluit** aan als je het niet eens bent met de standaard:",
        f"   - `goedkeuren` of `schrijven`/`publiceren` (standaard): de pagina wordt {werkwoord}; bij `goedkeuren` krijgt ze status goedgekeurd;",
        f"   - `{OVERSLAAN}`: de pagina wordt niet {werkwoord}; het concept vervalt met de run;",
        f"   - `{AANPASSEN}`: de pagina gaat terug naar de Agent; zet in **Opmerking** wat er anders moet.",
        "2. Schrijf algemene opmerkingen onder *Opmerkingen*.",
        f"3. Staat er nergens `{AANPASSEN}`: zet bovenaan `akkoord_voor_publicatie: ja` en je naam in `beoordeeld_door`, en vraag de Agent het plan uit te voeren. "
        f"Staat er wel `{AANPASSEN}`, vraag de Agent dan de opmerkingen te verwerken; je krijgt een nieuw plan, waarin je eerdere besluiten voor ongewijzigde pagina's bewaard blijven.",
        "",
    ]
    if final_phase == "publish":
        lines += ["## Wordt gepubliceerd", "", kop, *groepen["goed"], ""]
    else:
        lines += ["## Wordt goedgekeurd", "", "Status review → goedgekeurd, met een regel in het logboek.", "", kop, *(groepen["goed"] or [])]
        if not groepen["goed"]:
            lines.append("| (geen) |" + " |" * (len(KOLOMMEN) - 1))
        lines += ["", "## Wordt geschreven zonder goedkeuring", "", "Kandidaten (nog voor te leggen), afgewezen pagina's en pagina's van een niet-gecureerd type.", "", kop, *(groepen["overig"] or [])]
        if not groepen["overig"]:
            lines.append("| (geen) |" + " |" * (len(KOLOMMEN) - 1))
        lines.append("")
    if vragen_per_pagina:
        lines += ["## Ter beslissing", "", "Open vragen uit de pagina's zelf (sectie *Ter discussie*). Beantwoord ze in de kolom Opmerking, met `aanpassen`, of laat ze open voor later.", ""]
        for naam, vragen in vragen_per_pagina:
            lines += [f"**{naam}**", *[f"- {v}" for v in vragen], ""]
    lines += ["## Opmerkingen", "", "(Schrijf hier algemene opmerkingen voor de Agent.)", ""]
    return lines, details


def _lees_tabel(tekst: str) -> dict[str, tuple[str, str]]:
    """pad → (besluit, opmerking) uit de tabelrijen van een voorstel."""
    rijen = {}
    for regel in frontmatter.parse(tekst).body.splitlines():
        regel = regel.strip()
        if not regel.startswith("|"):
            continue
        cellen = [c.strip() for c in regel.strip("|").split("|")]
        link = _ELEMENT_LINK.search(cellen[0])
        if len(cellen) < len(KOLOMMEN) or not link:
            continue
        besluit = cellen[3].strip("`*_ ").lower()
        rijen[link.group(1)] = (besluit, cellen[4])
    return rijen


def _besluiten(voorstel_path: Path, final_phase: str, plan_obj: dict, inhoud: dict[str, tuple[str, str]]) -> dict[str, str]:
    """Leest en toetst de besluiten; weigert bij een ontbrekende rij, een onbekend besluit of 'aanpassen'."""
    rijen = _lees_tabel(voorstel_path.read_text(encoding="utf-8"))
    besluiten, aanpassen, fouten = {}, [], []
    for entry in plan_obj["paginas"]:
        pad = entry["pad"]
        if pad not in rijen:
            fouten.append(f"rij voor '{pad}' ontbreekt in het voorstel")
            continue
        besluit, opmerking = rijen[pad]
        opties = _opties(final_phase, entry)
        if besluit not in opties:
            fouten.append(f"'{pad}': besluit '{besluit}' is niet toegestaan (kies uit {', '.join(opties)})")
        elif besluit == AANPASSEN:
            aanpassen.append(f"- {pad}: {opmerking or '(geen opmerking)'}")
        besluiten[pad] = besluit
    if fouten:
        raise GateError("Het voorstel is niet uit te voeren:\n" + "\n".join(fouten))
    if aanpassen:
        raise GateError(
            "Het plan bevat pagina's met besluit 'aanpassen'. Verwerk eerst de opmerkingen en maak een nieuw plan:\n"
            + "\n".join(aanpassen)
        )
    # Een pagina overslaan mag geen link breken in een pagina die wel wordt geschreven.
    overgeslagen = {pad for pad, b in besluiten.items() if b == OVERSLAAN and not any(e["pad"] == pad and e["actie"] == "wijzigen" for e in plan_obj["paginas"])}
    for pad, besluit in besluiten.items():
        if besluit == OVERSLAAN:
            continue
        for doel in overgeslagen:
            if f"{Path(doel).name})" in inhoud[pad][1] or f"{Path(doel).stem}]]" in inhoud[pad][1]:
                raise GateError(
                    f"'{pad}' linkt naar '{doel}', dat wordt overgeslagen. Kies voor beide 'aanpassen' of laat '{doel}' schrijven."
                )
    return besluiten


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
        inhoud = _sync_contents(wiki_root, wiki_yaml, doel, plan_obj)
        links = {e["pad"]: f"../{e['pad']}" for e in plan_obj["paginas"]}
    else:
        plan_obj = _build_plan_curation(wiki_root, wiki_yaml, run_id, final_phase)
        inhoud = _curation_contents(wiki_root, run_id, plan_obj)
        changeset = _load_json(runs.run_dir(wiki_root, run_id) / "changeset.json")
        staged = runs.run_dir(wiki_root, run_id).relative_to(wiki_root).as_posix() + "/changeset/"
        links = {p["pad"]: f"../{staged}{p['staged_bestand']}" for p in changeset["paginas"]}

    validate.validate_instance(plan_obj, "publish-plan")

    rdir = runs.run_dir(wiki_root, run_id)
    plan_path = rdir / f"{final_phase}-plan.json"
    voorstellen_dir = wiki_root / "voorstellen"
    voorstellen_dir.mkdir(parents=True, exist_ok=True)
    voorstel_path = voorstellen_dir / f"{run_id}.md"
    vorige, oude_hashes = _vorige_besluiten(voorstel_path, plan_path)
    body_lines, detail_lines = _render_plan(run_id, final_phase, plan_obj, inhoud, links, vorige, oude_hashes)
    _write_json(plan_path, plan_obj)
    (voorstellen_dir / f"{run_id}-details.md").write_text("\n".join(detail_lines) + "\n", encoding="utf-8", newline="\n")
    voorstel_page = frontmatter.Page(
        meta={
            "run": run_id,
            "plan_hash": plan_obj["plan_hash"],
            "akkoord_voor_publicatie": "nee",
            "beoordeeld_door": "",
        },
        body="\n".join(body_lines),
    )
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
        live_plan = _build_plan_curation(wiki_root, wiki_yaml, run_id, final_phase)

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
        inhoud = _sync_contents(wiki_root, wiki_yaml, doel, stored_plan)
    else:
        inhoud = _curation_contents(wiki_root, run_id, stored_plan)
    besluiten = _besluiten(voorstel_path, final_phase, stored_plan, inhoud)

    if final_phase == "publish":
        _materialize_sync(wiki_root, wiki_yaml, run_id, doel, beoordeeld_door, stored_plan, besluiten)
    else:
        _materialize_curation(wiki_root, wiki_yaml, run_id, beoordeeld_door, final_phase, besluiten)

    runs.mark_final_done(wiki_root, run_id, final_phase, plan_path.name, stored_plan["plan_hash"])
    overgeslagen = sorted(pad for pad, b in besluiten.items() if b == OVERSLAAN)
    runs.log_event(wiki_root, run_id, final_phase, "toegepast", beoordeeld_door=beoordeeld_door, overgeslagen=overgeslagen)
    return voorstel_path
