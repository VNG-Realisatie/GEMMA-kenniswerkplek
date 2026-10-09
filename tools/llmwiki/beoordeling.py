"""Beoordelingen van een curatie-wiki: YAML-bestanden met het oordeel van de AI per begrip.

Een beoordeling is de invoer voor de scripts van de wiki: een beslis-script vult `beslist:` en `status:`, een
render-script maakt er leesbare pagina's van. Het akkoord van de redacteur hoort bij de inhoud van de beoordeling
(`inhoud_hash`): alles behalve `status` en `beslist`, want die zetten de scripts. Zo vraagt een andere opmaak of een
bijgewerkt model geen nieuw akkoord, en een inhoudelijke wijziging wel.

Waar de beoordelingen staan, zegt `wiki.yaml` `curation.beoordelingen` (een map, relatief aan de wiki).
"""
from __future__ import annotations

from pathlib import Path

import yaml

# De C-versie van de veilige loader (libyaml) als die er is: tien keer sneller, dezelfde uitkomst.
SNELLE_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

from . import hashing

SCRIPTVELDEN = ("status", "beslist")


def map_(wiki_root: Path, wiki_yaml: dict) -> Path | None:
    rel = (wiki_yaml.get("curation") or {}).get("beoordelingen")
    return wiki_root / rel if rel else None


def laad(pad: Path) -> dict:
    data = yaml.load(pad.read_text(encoding="utf-8"), Loader=SNELLE_LOADER) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{pad}: een beoordeling moet een YAML-object zijn")
    return data


def dump(data: dict) -> str:
    """Vaste opmaak: volgorde zoals gegeven, geen regelafbreking binnen een tekst (stabiele diffs)."""
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=10**9, default_flow_style=False)


def schrijf(pad: Path, data: dict) -> None:
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(dump(data), encoding="utf-8", newline="\n")


def alle(wiki_root: Path, wiki_yaml: dict) -> dict[str, tuple[Path, dict]]:
    """id → (pad, data) voor elke beoordeling; het id is de bestandsnaam zonder extensie."""
    map_pad = map_(wiki_root, wiki_yaml)
    if not map_pad or not map_pad.exists():
        return {}
    return {p.stem: (p, laad(p)) for p in sorted(map_pad.glob("*.yaml"))}


def inhoud(data: dict) -> dict:
    return {k: v for k, v in data.items() if k not in SCRIPTVELDEN}


def inhoud_hash(data: dict) -> str:
    return hashing.hash_json(inhoud(data))


def goedgekeurd_in_log(log_tekst: str, beoordeling_id: str, data: dict) -> bool:
    """Staat er een promotieregel voor dit id met de hash van de huidige inhoud?"""
    from . import logbook

    return logbook.heeft_regel(log_tekst, "promote", beoordeling_id, hashing.short(inhoud_hash(data)))
