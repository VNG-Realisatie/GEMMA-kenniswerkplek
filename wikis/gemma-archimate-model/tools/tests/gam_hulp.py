"""Hulpfuncties voor de tests van gemma-archimate-model."""
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
WIKI = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import bepaal_type  # noqa: E402,F401

# Een bedrijfsobject: het vak, het hoofdkenmerk en de kenmerken die een antwoord nodig hebben (*wordt bewerkt*); de
# andere toetskenmerken zijn standaard ja.
KENMERKEN_BO = {"wordt_bewerkt": "ja"}
VELDEN_BO = {"vak": "bedrijf/passief", "hoofdkenmerk": "object"}

SCOPE_STANDAARD = ("herkenbaar", "gemeentelijk", "betekenis_in_onderwerp")


def maak(ja: set[str], *, nee: tuple = (), bronnen: list[str] | None = None, onderbouwing: str = "test",
         niveau: str | None = None, afhankelijkheid: str | None = None, interactievorm: str | None = None,
         **extra) -> dict:
    """Een beoordeling in de vorm van de beslistabel uit de verzameling kenmerken met ja, zoals de tests ze schrijven.

    Het hoofdkenmerk en de soort gedrag in `ja` worden de keuzevelden `vak`, `hoofdkenmerk` en `soort_gedrag`. Elk
    ander kenmerk in `ja` krijgt het antwoord ja; elk kenmerk van het type dat niet in `ja` staat en een antwoord kan
    krijgen (de scope, de kenmerken van Typeren en de toetskenmerken), krijgt het antwoord nee; `nee` voegt een
    expliciete nee toe. `niveau`, `afhankelijkheid` en `interactievorm` zijn keuzekenmerken."""
    if "per_keer_doorlopen" in ja and not niveau and not afhankelijkheid:
        niveau = "levensloopproces"
    if "gezamenlijk_gedrag" in ja and not interactievorm:
        interactievorm = "estafette"
    hoofd = [s for s in bepaal_type.HOOFDKENMERK if s in ja]
    soort = [s for s in bepaal_type.SOORT_GEDRAG if s in ja]
    h = hoofd[0] if len(hoofd) == 1 else None
    sg = soort[0] if len(soort) == 1 else None
    uit = {k: v for k, v in extra.items()}
    vak = bepaal_type.vak_bij(h, sg) if h else None
    if vak and "vak" not in uit:
        uit["vak"] = vak
    if h and (not vak or len(bepaal_type.VAK[vak].hoofdkenmerken) > 1):
        uit.setdefault("hoofdkenmerk", h)
    if sg and (not vak or len(bepaal_type.VAK[vak].soorten) > 1):
        uit.setdefault("soort_gedrag", sg)

    def antwoord(waarde: str) -> dict:
        a = {"waarde": waarde, "onderbouwing": onderbouwing}
        return {**a, "bronnen": list(bronnen)} if bronnen and waarde == "ja" else a

    kenmerken = {s: antwoord("ja") for s in sorted(ja, key=bepaal_type.SLEUTELS.index)
                 if s in bepaal_type.SLEUTELS and s not in bepaal_type.KEUZE}
    kenmerken |= {s: antwoord("nee") for s in nee}
    for s in SCOPE_STANDAARD:
        kenmerken.setdefault(s, antwoord("nee"))
    if afhankelijkheid:
        kenmerken["afhankelijkheid"] = {"waarde": afhankelijkheid, "onderbouwing": onderbouwing}
    if niveau:
        kenmerken["procesniveau"] = {"waarde": niveau, "onderbouwing": onderbouwing}
    if interactievorm:
        kenmerken["interactievorm"] = {"waarde": interactievorm, "onderbouwing": onderbouwing}
    b = {"begrip": "test", "kenmerken": kenmerken, **uit}
    k, e = bepaal_type.waarden(b), bepaal_type.extra_velden(b)
    if bepaal_type.voorbij_afbakenen(k, e):
        u = bepaal_type._stap_0_tot_3(k, e)
        vragen = bepaal_type.typeren(k, e)
        if u.soort == "element":
            vragen += bepaal_type.typedef(u.paginatype, u.archimate_type, niveau).toets
        for s in vragen:
            if s not in bepaal_type.AFWIJKING:
                kenmerken.setdefault(s, antwoord("nee"))
    for s in SCOPE_STANDAARD:   # de scope die ja is, is het standaardantwoord: alleen een afwijking staat erin
        if kenmerken[s]["waarde"] == "ja" and not bronnen:
            del kenmerken[s]
    return b


def element_tekst(meta: dict, body: str = "# Titel\n", definitie_bovenaan: bool = True) -> str:
    """Paginatekst; een elementpagina krijgt `## Definitie` als eerste sectie, zoals het sjabloon voorschrijft."""
    import re

    import yaml

    if definitie_bovenaan and meta.get("archimate_type") and "## Definitie" not in body:
        sectie = f"## Definitie\n\n{meta.get('definitie', '')}\n\n"
        eerste = re.search(r"^## ", body, re.M)
        body = body[: eerste.start()] + sectie + body[eerste.start():] if eerste else body.rstrip("\n") + "\n\n" + sectie
    return f"---\n{yaml.safe_dump(meta, sort_keys=False, allow_unicode=True)}---\n\n{body}"
