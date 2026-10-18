"""Beoordelingen van een curatie-wiki: YAML-bestanden met het oordeel van de AI per begrip.

Een beoordeling is de invoer voor de scripts van de wiki: een beslis-script vult `beslist:` en `status:`, een
render-script maakt er leesbare pagina's van. Het akkoord van de redacteur hoort bij de inhoud van de beoordeling
(`inhoud_hash`): alles behalve `status` en `beslist`, want die zetten de scripts, en `besluiten`, want het akkoord keurt
het model goed en niet het verslag van de besluiten. Zo vraagt een andere opmaak, een bijgewerkt model of een opgeschoond
besluit geen nieuw akkoord, en een inhoudelijke wijziging wel.

Waar de beoordelingen staan, zegt `wiki.yaml` `curation.beoordelingen`: een map of een patroon met `*`, relatief aan de
wiki (bijvoorbeeld `onderwerpen/*/beoordelingen`). Het id van een beoordeling is de bestandsnaam en is uniek in de wiki.

Zet `curation.beslist` op een bestandsnaam (bijvoorbeeld `beslist.yaml`), dan staat `beslist:` niet in de beoordeling maar
in een gegenereerd bestand met die naam naast de map met beoordelingen: id → blok, één bestand per map. `alle` voegt het
blok weer toe aan `data`, zodat lezers niets merken; `schrijf` met `wiki_yaml` laat het weg; `schrijf_beslist` schrijft het
bestand. Een `beslist:` dat nog in de beoordeling staat (vóór de migratie) blijft gelden tot er een blok in het bestand staat.
"""
from __future__ import annotations

from pathlib import Path

import yaml

# De C-versie van de veilige loader (libyaml) als die er is: tien keer sneller, dezelfde uitkomst.
SNELLE_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

from . import hashing

SCRIPTVELDEN = ("status", "beslist")
BUITEN_HASH = (*SCRIPTVELDEN, "besluiten")


def patroon(wiki_yaml: dict) -> str | None:
    return (wiki_yaml.get("curation") or {}).get("beoordelingen")


def mappen(wiki_root: Path, wiki_yaml: dict) -> list[Path]:
    """De mappen met beoordelingen: de map of de mappen die het patroon `curation.beoordelingen` aanwijst."""
    rel = patroon(wiki_yaml)
    if not rel:
        return []
    return sorted(p for p in wiki_root.glob(rel) if p.is_dir())


def laad(pad: Path) -> dict:
    data = yaml.load(pad.read_text(encoding="utf-8"), Loader=SNELLE_LOADER) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{pad}: een beoordeling moet een YAML-object zijn")
    return data


def dump(data: dict) -> str:
    """Vaste opmaak: volgorde zoals gegeven, geen regelafbreking binnen een tekst (stabiele diffs)."""
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=10**9, default_flow_style=False)


def beslist_bestand(wiki_yaml: dict | None) -> str | None:
    """De bestandsnaam waarin `beslist` apart staat (`curation.beslist`), of None: dan staat het in de beoordeling."""
    return ((wiki_yaml or {}).get("curation") or {}).get("beslist")


def tekst(data: dict, wiki_yaml: dict | None = None) -> str:
    """De tekst van de beoordeling zoals `schrijf` haar schrijft."""
    if beslist_bestand(wiki_yaml):
        data = {k: v for k, v in data.items() if k != "beslist"}
    return dump(data)


def schrijf(pad: Path, data: dict, wiki_yaml: dict | None = None) -> None:
    """Schrijf een beoordeling; met `wiki_yaml` zonder `beslist` als dat apart staat (`curation.beslist`)."""
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(tekst(data, wiki_yaml), encoding="utf-8", newline="\n")


KOP_BESLIST = "# Gegenereerd door tools/beslissen.py (beslist per beoordeling); niet met de hand bewerken.\n"


def _beslist_pad(map_pad: Path, naam: str) -> Path:
    return map_pad.parent / naam


def _laad_beslist(map_pad: Path, naam: str) -> dict:
    pad = _beslist_pad(map_pad, naam)
    return laad(pad) if pad.exists() else {}


def schrijf_beslist(beoordelingen: dict[str, tuple[Path, dict]], wiki_yaml: dict) -> list[Path]:
    """Schrijf het bestand met `beslist` naast elke map met beoordelingen; alleen als de tekst verandert.
    Geeft de bestanden die zijn bijgewerkt."""
    naam = beslist_bestand(wiki_yaml)
    if not naam:
        return []
    per_map: dict[Path, dict] = {}
    for bid, (pad, data) in beoordelingen.items():
        blok = per_map.setdefault(pad.parent, {})
        if data.get("beslist"):
            blok[bid] = data["beslist"]
    bijgewerkt = []
    for map_pad, blok in sorted(per_map.items()):
        doel = _beslist_pad(map_pad, naam)
        nieuw = KOP_BESLIST + dump(dict(sorted(blok.items())))
        if not doel.exists() or doel.read_text(encoding="utf-8") != nieuw:
            doel.write_text(nieuw, encoding="utf-8", newline="\n")
            bijgewerkt.append(doel)
    return bijgewerkt


def alle(wiki_root: Path, wiki_yaml: dict) -> dict[str, tuple[Path, dict]]:
    """id → (pad, data) voor elke beoordeling; het id is de bestandsnaam zonder extensie."""
    uit: dict[str, tuple[Path, dict]] = {}
    naam = beslist_bestand(wiki_yaml)
    for map_pad in mappen(wiki_root, wiki_yaml):
        blokken = _laad_beslist(map_pad, naam) if naam else {}
        for p in sorted(map_pad.glob("*.yaml")):
            if p.stem in uit:
                raise ValueError(f"beoordeling {p.stem} staat twee keer: {uit[p.stem][0]} en {p}")
            data = laad(p)
            if p.stem in blokken:
                data["beslist"] = blokken[p.stem]
            uit[p.stem] = (p, data)
    return dict(sorted(uit.items()))


def inhoud(data: dict) -> dict:
    return {k: v for k, v in data.items() if k not in SCRIPTVELDEN}


def inhoud_hash(data: dict) -> str:
    return hashing.hash_json({k: v for k, v in data.items() if k not in BUITEN_HASH})


def goedgekeurd_in_log(log_tekst: str, beoordeling_id: str, data: dict) -> bool:
    """Staat er een promotieregel voor dit id met de hash van de huidige inhoud?"""
    from . import logbook

    return logbook.heeft_regel(log_tekst, "promote", beoordeling_id, hashing.short(inhoud_hash(data)))
