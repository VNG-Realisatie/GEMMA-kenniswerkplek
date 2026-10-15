"""Afronden in één commando, na het akkoord van de redacteur (stap 16 en 17 van skill gemma-archimate-model-update).

`llmwiki promote apply` blijft een los commando, voor de klik van de redacteur. Daarna draait dit script, in deze
volgorde en met een stop bij de eerste fout:
1. het akkoord is vastgelegd: `log.md` is gewijzigd en nog niet gecommit (anders weigert het script);
2. `commit-check` op het bericht (een bericht zonder geldige prefix stopt hier, vóór de export);
3. `archimate_export.py --check`, dan `archimate_export.py`;
4. `render.py --check` en `llmwiki lint`;
5. `git add` van de wikimap en de commit met het bericht.

Het script zet geen akkoordvelden en geen status; het bevestigt een akkoord dat er al is.

Gebruik (vanuit de wikimap):
    uv run python tools/afronden.py --bericht "update: Besluitvorming verwerkt (12 elementen)"
    uv run python tools/afronden.py --bericht "…" --droog      # alleen tonen wat er zou draaien
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
TOOLS = Path(__file__).resolve().parent


class Gestopt(Exception):
    pass


def _run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)


def repo_root(wiki: Path) -> Path:
    return wiki.resolve().parents[1]


def akkoord_vastgelegd(wiki: Path, run=_run) -> bool:
    """`promote apply` schrijft het akkoord in log.md: gewijzigd in de werkboom, nog niet gecommit."""
    r = run(["git", "status", "--porcelain", "--", str((wiki / "log.md").resolve())], repo_root(wiki))
    return r.returncode == 0 and bool(r.stdout.strip())


def stappen(wiki: Path, bericht_bestand: Path) -> list[tuple[str, list[str]]]:
    py = sys.executable
    return [
        ("berichtcontrole", [py, "-m", "llmwiki", "commit-check", str(bericht_bestand)]),
        ("export-check", [py, str(TOOLS / "archimate_export.py"), "--check"]),
        ("export", [py, str(TOOLS / "archimate_export.py")]),
        ("render-check", [py, str(TOOLS / "render.py"), "--check"]),
        ("lint", [py, "-m", "llmwiki", "lint"]),
    ]


def afronden(wiki: Path, bericht: str, droog: bool = False, run=_run) -> list[str]:
    """Voer de stappen uit; geeft de meldingen. Gooit `Gestopt` bij de eerste fout, zonder te committen."""
    bericht = bericht.strip()
    if not bericht:
        raise Gestopt("geef --bericht: <prefix>: één of twee zinnen")
    root = repo_root(wiki)
    uit: list[str] = []
    if not akkoord_vastgelegd(wiki, run):
        raise Gestopt("geen vastgelegd akkoord: log.md is niet gewijzigd. Draai eerst `llmwiki promote apply` (alleen na "
                      "het woord AKKOORD van de redacteur).")
    uit.append("akkoord: log.md is gewijzigd")
    with tempfile.TemporaryDirectory() as tmp:
        bestand = Path(tmp) / "bericht.txt"
        bestand.write_text(bericht + "\n", encoding="utf-8")
        for naam, cmd in stappen(wiki, bestand):
            if droog:
                uit.append(f"{naam}: {' '.join(cmd[:4])} …")
                continue
            r = run(cmd, wiki if "tools" in cmd[1] else root)
            if r.returncode != 0:
                raise Gestopt(f"{naam} mislukt, niet gecommit:\n{(r.stdout + r.stderr).strip()}")
            uit.append(f"{naam}: ok")
        if droog:
            return uit + ["commit: git add + commit (droog: niets uitgevoerd)"]
        for naam, cmd in (("add", ["git", "add", "-A", "--", str(wiki.resolve())]), ("commit", ["git", "commit", "-m", bericht])):
            r = run(cmd, root)
            if r.returncode != 0:
                raise Gestopt(f"git {naam} mislukt:\n{(r.stdout + r.stderr).strip()}")
    return uit + ["commit: gedaan"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--bericht", required=True, help="Commitbericht: <prefix>: één of twee zinnen")
    parser.add_argument("--droog", action="store_true", help="Alleen tonen wat er zou draaien")
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    a = parser.parse_args(argv)
    try:
        print("\n".join(afronden(a.wiki, a.bericht, a.droog)))
    except Gestopt as exc:
        print(f"gestopt: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
