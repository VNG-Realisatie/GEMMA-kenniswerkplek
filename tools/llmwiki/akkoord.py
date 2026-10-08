"""Akkoord voor een curatie-wiki met beoordelingen (`wiki.yaml` `curation.beoordelingen`).

Geen run, geen voorstelbestand: de redacteur bekijkt de gerenderde pagina's en de wijzigingen in Git, en geeft akkoord
met het woord AKKOORD in de chat. Daarna vraagt het harness nog om één klik op "toestaan" (permissie 'ask' op
`llmwiki promote apply`); die klik is de echte beveiliging.

- `plan` draait het afleid-script van de wiki (`curation.afleiden`, dat ook rendert), kiest de beoordelingen met status
  `review` (optioneel van één onderwerp) en legt hun inhoudshash vast in `.work/akkoord.json`.
- `apply` controleert het akkoordwoord, draait het afleid-script opnieuw en weigert als de selectie of een inhoudshash
  afwijkt van het plan (er is iets gewijzigd na het tonen). Daarna: status `goedgekeurd`, per beoordeling een regel in
  `log.md` met de inhoudshash en de naam van de redacteur (`git config user.name`), en het render-script
  (`curation.render`).

Het akkoord hoort bij de inhoud van de beoordeling (`beoordeling.inhoud_hash`). Een nieuwe opmaak of een bijgewerkt
model raakt die niet; een inhoudelijke wijziging zet het element via het afleid-script terug op `review`.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from . import beoordeling, hashing, logbook, paths

PLAN = Path(".work") / "akkoord.json"
AKKOORD = "AKKOORD"


class AkkoordFout(RuntimeError):
    pass


def van_toepassing(wiki_yaml: dict) -> bool:
    return wiki_yaml.get("type") == "curation" and bool((wiki_yaml.get("curation") or {}).get("beoordelingen"))


def draai_script(wiki_root: Path, wiki_yaml: dict, sleutel: str, *args: str) -> str:
    """Draai `curation.<sleutel>` van de wiki met deze Python; geef de uitvoer, of weiger bij een fout."""
    rel = (wiki_yaml.get("curation") or {}).get(sleutel)
    if not rel:
        raise AkkoordFout(f"wiki.yaml mist curation.{sleutel}")
    r = subprocess.run([sys.executable, str(wiki_root / rel), *args, "--wiki", str(wiki_root)], cwd=wiki_root,
                       capture_output=True, text=True, encoding="utf-8", check=False)
    if r.returncode != 0:
        raise AkkoordFout(f"{rel} {' '.join(args)} gaf een fout:\n{r.stdout}{r.stderr}".rstrip())
    return r.stdout


def te_keuren(wiki_root: Path, wiki_yaml: dict, onderwerp: str | None = None) -> dict[str, tuple[Path, dict]]:
    return {bid: (pad, data) for bid, (pad, data) in beoordeling.alle(wiki_root, wiki_yaml).items()
            if data.get("status") == "review" and (onderwerp is None or onderwerp in data.get("onderwerpen", []))}


def _hashes(selectie: dict[str, tuple[Path, dict]]) -> dict[str, str]:
    return {bid: beoordeling.inhoud_hash(data) for bid, (_, data) in sorted(selectie.items())}


def git_naam(wiki_root: Path) -> str:
    r = subprocess.run(["git", "config", "user.name"], cwd=wiki_root, capture_output=True, text=True, check=False)
    return r.stdout.strip()


def plan(wiki_root: Path, wiki_yaml: dict, onderwerp: str | None = None) -> dict:
    """Afleiden en renderen, dan vastleggen wat bij een akkoord wordt goedgekeurd. Geeft een samenvatting."""
    draai_script(wiki_root, wiki_yaml, "afleiden")
    selectie = te_keuren(wiki_root, wiki_yaml, onderwerp)
    alle = beoordeling.alle(wiki_root, wiki_yaml)
    log = (wiki_root / "log.md").read_text(encoding="utf-8") if (wiki_root / "log.md").exists() else ""
    hashes = _hashes(selectie)
    (wiki_root / PLAN).parent.mkdir(parents=True, exist_ok=True)
    (wiki_root / PLAN).write_text(json.dumps({"onderwerp": onderwerp, "beoordelingen": hashes,
                                              "plan_hash": hashing.hash_json(hashes)}, indent=2), encoding="utf-8")
    return {
        "te_keuren": [{"id": bid, "naam": data.get("begrip", bid),
                       "type": data["afgeleid"]["uitkomst"].get("paginatype"),
                       "eerder_goedgekeurd": logbook.heeft_regel(log, "promote", bid)} for bid, (_, data) in sorted(selectie.items())],
        "voor_te_leggen": sorted(bid for bid, (_, d) in alle.items() if (d.get("afgeleid") or {}).get("open")
                                 and (onderwerp is None or onderwerp in d.get("onderwerpen", []))),
    }


def apply(wiki_root: Path, wiki_yaml: dict, akkoord_woord: str | None, door: str | None = None) -> list[str]:
    """Na het woord AKKOORD: keur de beoordelingen uit het plan goed. Geeft de goedgekeurde id's."""
    approval = (wiki_yaml.get("curation") or {}).get("approval", "chat")
    if approval != "chat":
        raise AkkoordFout("Deze wiki gebruikt beoordelingen; het akkoord gaat in de chat. Zet curation.approval: chat")
    if akkoord_woord != AKKOORD:
        raise AkkoordFout("Het akkoord vereist het letterlijke woord AKKOORD van de redacteur in de chat "
                          "(--akkoord-woord AKKOORD); iets anders ('prima', 'ja hoor') is geen akkoord")
    pad = wiki_root / PLAN
    if not pad.exists():
        raise AkkoordFout("Geen plan gevonden; draai eerst 'llmwiki promote plan' en toon de samenvatting")
    opgeslagen = json.loads(pad.read_text(encoding="utf-8"))
    draai_script(wiki_root, wiki_yaml, "afleiden", "--zonder-render")
    selectie = te_keuren(wiki_root, wiki_yaml, opgeslagen.get("onderwerp"))
    if _hashes(selectie) != opgeslagen["beoordelingen"]:
        raise AkkoordFout("Er is iets gewijzigd sinds de samenvatting (een beoordeling is aangepast, bijgekomen of "
                          "weggevallen). Maak een nieuw plan met 'llmwiki promote plan' en vraag opnieuw akkoord.")
    if not selectie:
        raise AkkoordFout("Er staat niets op review; er is niets om goed te keuren")
    door = door or git_naam(wiki_root) or "redacteur"
    for bid, (bestand, data) in sorted(selectie.items()):
        data["status"] = "goedgekeurd"
        beoordeling.schrijf(bestand, data)
        logbook.append_log(wiki_root, "promote", bid, door, beoordeling.inhoud_hash(data))
    draai_script(wiki_root, wiki_yaml, "render")
    pad.unlink()
    return sorted(selectie)


def wiki_roots(repo_root: Path) -> list[tuple[Path, dict]]:
    """Alle wiki's in de repository die met beoordelingen werken."""
    result = []
    for wiki_root in sorted((repo_root / "wikis").glob("*")):
        if (wiki_root / "wiki.yaml").exists():
            wiki_yaml = paths.load_wiki_yaml(wiki_root)
            if van_toepassing(wiki_yaml):
                result.append((wiki_root, wiki_yaml))
    return result
