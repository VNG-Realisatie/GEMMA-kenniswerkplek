"""Hulpfuncties voor de tests van gemma-archimate-model."""
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WIKI = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import bepaal_type  # noqa: E402,F401

KENMERKEN_BO = {s: "nee" for s in bepaal_type.SLEUTELS if s not in bepaal_type.KEUZE} | {
    s: "ja" for s in ("herkenbaar", "gemeentelijk", "eigen_identiteit", "betekenis_in_onderwerp",
                      "zelfstandige_specialisatie", "onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt")
}
VELDEN_BO = {"vak": "bedrijf/passief"}


def nieuwe_vorm(b: dict) -> dict:
    """Een beoordeling met het hoofdkenmerk en de soort gedrag als kenmerken (ja/nee), in de vorm met keuzevelden: die
    kenmerken worden `vak`, `hoofdkenmerk` en `soort_gedrag`, zoals de omzetting van 2026-10-15 deed."""
    kenmerken = dict(b.get("kenmerken") or {})
    ja = {s for s, a in kenmerken.items() if (a.get("waarde") if isinstance(a, dict) else a) == "ja"}
    hoofd = [s for s in bepaal_type.HOOFDKENMERK if s in ja]
    soort = [s for s in bepaal_type.SOORT_GEDRAG if s in ja]
    beantwoord = any(s in kenmerken for s in bepaal_type.HOOFDKENMERK)
    uit = {k: v for k, v in b.items() if k != "kenmerken"}
    h = hoofd[0] if len(hoofd) == 1 else (bepaal_type.DING if beantwoord and not hoofd else None)
    sg = soort[0] if len(soort) == 1 else None
    vak = bepaal_type.vak_bij(h, sg) if h else None
    if vak and "vak" not in uit:
        uit["vak"] = vak
    if h and (not vak or len(bepaal_type.VAK[vak].hoofdkenmerken) > 1):
        uit.setdefault("hoofdkenmerk", h)
    if sg and (not vak or len(bepaal_type.VAK[vak].soorten) > 1):
        uit.setdefault("soort_gedrag", sg)
    uit["kenmerken"] = {s: a for s, a in kenmerken.items() if s not in bepaal_type.KEUZE}
    return uit


def element_tekst(meta: dict, body: str = "# Titel\n", definitie_bovenaan: bool = True) -> str:
    """Paginatekst; een elementpagina krijgt `## Definitie` als eerste sectie, zoals het sjabloon voorschrijft."""
    import re

    import yaml

    if definitie_bovenaan and meta.get("archimate_type") and "## Definitie" not in body:
        sectie = f"## Definitie\n\n{meta.get('definitie', '')}\n\n"
        eerste = re.search(r"^## ", body, re.M)
        body = body[: eerste.start()] + sectie + body[eerste.start():] if eerste else body.rstrip("\n") + "\n\n" + sectie
    return f"---\n{yaml.safe_dump(meta, sort_keys=False, allow_unicode=True)}---\n\n{body}"


