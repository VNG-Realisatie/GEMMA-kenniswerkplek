"""Zet de beoordelingen om van de oude beslistabel naar de nieuwe (plan 2026-10-18, stap 5).

Eenmalig. Het script vertaalt de kenmerken van de oude beslistabel naar de keuzekenmerken van de nieuwe, zonder de
inhoud te veranderen: *slechts eigenschap*, *eigen identiteit*, *zelfstandige specialisatie*, *invoer van een ander*, *deel
van object* en *bijdrage aan groter proces* worden de waarde van *afhankelijkheid*; *omvat levensloop*, *klant tot klant*
en *groepeert processen* worden *procesniveau*; *afspraak* en *waarneembare vorm* worden een waarde van `hoofdkenmerk`
(object, afspraak, representatie). De kenmerken die vervallen (V5, V6) gaan eruit, de onderbouwing en de bronnen van wat
vervangen wordt gaan mee naar het keuzekenmerk, en de bronnen die anders verloren gaan komen in `bronnen` van de
beoordeling (A1). Daarna krijgen de relatiekenmerken hun tegenpartij uit de relaties (V10) en valt weg wat het
standaardantwoord heeft.

Gebruik (vanuit de wikimap):
    uv run python tools/omzetten_beslistabel.py            # laat zien wat er zou veranderen
    uv run python tools/omzetten_beslistabel.py --schrijf  # schrijf de beoordelingen
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import bepaal_type as bt  # noqa: E402
import beoordeling as beoordelingtool  # noqa: E402
import gam_gemeen  # noqa: E402
from llmwiki import beoordeling  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT

# De kenmerken van de oude beslistabel die niet meer bestaan, en hun standaardantwoord.
OUD_STANDAARD = {"herkenbaar": "ja", "gemeentelijk": "ja", "buiten_dit_model": "nee", "slechts_eigenschap": "nee",
                 "eigen_identiteit": "ja", "betekenis_in_onderwerp": "ja", "zelfstandige_specialisatie": "ja",
                 "generiek": "nee"}
VERVALLEN = ("slechts_eigenschap", "eigen_identiteit", "zelfstandige_specialisatie", "deel_van_object",
             "invoer_van_een_ander", "bijdrage_aan_groter_proces", "klant_tot_klant", "omvat_levensloop",
             "groepeert_processen", "afspraak", "waarneembare_vorm", "eigen_besluit", "eigen_normering", "levert_aanbod",
             "leidt_tot_gebeurtenis")
PROCES_ANNOTATIE = ("komt_herhaald_voor", "gebruikt_objecten")  # vervallen bij een proces en een interactie
TEGENHANGER = ("onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt")  # vervallen bij een actor en een rol
INTERACTIEVORM = {"bezorgen-stoffelijk-overschot": "estafette"}  # besluit 2026-10-08 van de redacteur


def _a(kenmerken: dict, sleutel: str) -> dict:
    a = kenmerken.get(sleutel)
    return a if isinstance(a, dict) else {"waarde": OUD_STANDAARD.get(sleutel, "nee")}


def _ja(kenmerken: dict, sleutel: str) -> bool:
    return _a(kenmerken, sleutel)["waarde"] == "ja"


def _keuze(waarde: str, *bronnen_van: dict, tekst: str | None = None) -> dict:
    """Een keuzekenmerk met de onderbouwing en de bronnen van de kenmerken die het vervangt."""
    teksten = [a["onderbouwing"] for a in bronnen_van if a.get("onderbouwing") and
               not str(a["onderbouwing"]).startswith(beoordelingtool.STANDAARD_NEE)]
    bronnen = list(dict.fromkeys(b for a in bronnen_van for b in a.get("bronnen") or []))
    uit = {"waarde": waarde, "onderbouwing": tekst or " ".join(dict.fromkeys(teksten)) or "—"}
    return {**uit, **({"bronnen": bronnen} if bronnen else {})}


def omzetten(bid: str, d: dict) -> tuple[dict, list[str]]:
    """De nieuwe beoordeling en de meldingen over wat niet eenduidig is."""
    meld: list[str] = []
    oud = d.get("kenmerken") or {}
    nieuw = {k: v for k, v in d.items()}
    kenmerken = dict(oud)
    hoofd = d.get("hoofdkenmerk")
    vak = d.get("vak")
    soort = d.get("soort_gedrag")
    afwijkt = {s: v for s, v in OUD_STANDAARD.items() if _a(oud, s)["waarde"] != v}
    voorbij_scope = not d.get("synoniem_van") and not {"herkenbaar", "gemeentelijk", "buiten_dit_model",
                                                       "betekenis_in_onderwerp"} & set(afwijkt)
    is_proces = voorbij_scope and vak == "bedrijf/gedrag-intern" and soort in ("per_keer_doorlopen", "groepeert_processen")
    is_interactie = voorbij_scope and vak == "bedrijf/gedrag-intern" and soort == "gezamenlijk_gedrag"
    is_passief = vak == "bedrijf/passief" or hoofd == "ding"
    # --- afhankelijkheid (V1)
    afh: dict | None = None
    if voorbij_scope:
        if _ja(oud, "slechts_eigenschap"):
            afh = _keuze("eigenschap", _a(oud, "slechts_eigenschap"))
        elif not _ja(oud, "eigen_identiteit"):
            afh = _keuze("onderdeel", _a(oud, "eigen_identiteit"))
        elif not _ja(oud, "zelfstandige_specialisatie"):
            afh = _keuze("variant", _a(oud, "zelfstandige_specialisatie"))
        elif is_passief and _ja(oud, "invoer_van_een_ander") and not _ja(oud, "generiek"):
            afh = _keuze("invoer_van_een_ander", _a(oud, "invoer_van_een_ander"))
        elif is_passief and _ja(oud, "deel_van_object"):
            afh = _keuze("onderdeel", _a(oud, "deel_van_object"))
        elif is_proces and soort == "per_keer_doorlopen" and not _ja(oud, "omvat_levensloop") \
                and _ja(oud, "bijdrage_aan_groter_proces") and not _ja(oud, "klant_tot_klant"):
            afh = _keuze("deelproces", _a(oud, "bijdrage_aan_groter_proces"), _a(oud, "klant_tot_klant"))
    if afh:
        kenmerken["afhankelijkheid"] = afh

    # --- procesniveau (V2)
    if is_proces and not (afh and afh["waarde"] != "zelfstandig"):
        if soort == "groepeert_processen":
            niveau = _keuze("cluster naar soort werk", _a(oud, "omvat_processen"),
                            tekst=_a(oud, "omvat_processen").get("onderbouwing") or "Groepering van bedrijfsprocessen van één soort werk.")
        elif _ja(oud, "omvat_levensloop"):
            niveau = _keuze("levensloopproces", _a(oud, "omvat_levensloop"))
        elif _ja(oud, "bijdrage_aan_groter_proces") and _ja(oud, "klant_tot_klant"):
            niveau = _keuze("bedrijfsproces", _a(oud, "klant_tot_klant"), _a(oud, "bijdrage_aan_groter_proces"))
        else:
            niveau = None
            meld.append("procesniveau niet te bepalen (geen levensloop en geen bijdrage aan een groter proces)")
        if niveau:
            kenmerken["procesniveau"] = niveau
        if soort == "groepeert_processen":
            nieuw["soort_gedrag"] = "per_keer_doorlopen"

    # --- interactievorm (V8)
    if is_interactie and bid in INTERACTIEVORM:
        decision = next((b["besluit"] for b in d.get("besluiten") or [] if b["besluit"].startswith("Estafette")), "")
        kenmerken["interactievorm"] = {"waarde": INTERACTIEVORM[bid], "onderbouwing": decision or "Besluit van de redacteur."}
    elif is_interactie:
        meld.append("interactievorm ontbreekt")

    # --- hoofdkenmerk bij een ding (V7)
    if is_passief:
        if hoofd == "ding" or not hoofd:
            if _ja(oud, "afspraak"):
                nieuw["hoofdkenmerk"] = "afspraak"
            elif _ja(oud, "waarneembare_vorm"):
                nieuw["hoofdkenmerk"] = "representatie"
            else:
                nieuw["hoofdkenmerk"] = "object"
    # --- vervallen kenmerken (V5, V6)
    bron_oud = list(dict.fromkeys(b for a in oud.values() if isinstance(a, dict) for b in a.get("bronnen") or []))
    for s in VERVALLEN:
        kenmerken.pop(s, None)
    if is_proces or is_interactie:
        for s in PROCES_ANNOTATIE:
            kenmerken.pop(s, None)
    if vak == "bedrijf/actief-intern" or hoofd in ("handelende_partij", "hoedanigheid", "samenwerkingsverband"):
        for s in TEGENHANGER:
            kenmerken.pop(s, None)
    nieuw["kenmerken"] = kenmerken

    if hoofd == "samenwerkingsverband":  # *los van verantwoordelijkheid* geldt niet voor een verband
        kenmerken.pop("los_van_verantwoordelijkheid", None)
    # --- wat niet bij het type hoort, valt weg; een onderdeel dat een subobject kan worden, houdt zijn toetskenmerken
    tijdelijk = {**nieuw, "kenmerken": {s: a for s, a in kenmerken.items() if s != "afhankelijkheid"}
                 if afh and afh["waarde"] == "onderdeel" and is_passief else kenmerken}
    k, extra = bt.waarden(tijdelijk), bt.extra_velden(tijdelijk)
    toegestaan: set = set()
    if bt.voorbij_afbakenen(k, extra):
        u = bt._stap_0_tot_3(k, extra)
        if u.soort == "element":
            t = bt.typedef(u.paginatype, u.archimate_type, k.get("procesniveau"))
            toegestaan = {*t.toets, *bt.typeren(k, extra)}
    for s in [s for s in kenmerken if s in bt.KENMERK and bt.KENMERK[s].groep in ("Toets", "Partij en regeling")
              and s not in toegestaan]:
        kenmerken.pop(s)
    # --- bronnen: de hoofdbron eerst (A1); zonder lijst uit de bronnen van de kenmerken, naar frequentie
    nieuw["kenmerken"] = kenmerken
    frequentie = Counter(b for a in oud.values() if isinstance(a, dict) for b in a.get("bronnen") or [])
    if not nieuw.get("bronnen") and frequentie:
        nieuw["bronnen"] = [b for b, _ in frequentie.most_common()]
    rest = bron_oud
    gebruikt = set(nieuw.get("bronnen") or [])
    for a in kenmerken.values():
        gebruikt |= set(a.get("bronnen") or [])
    for r in nieuw.get("relaties") or []:
        gebruikt |= set(r.get("bronnen") or [])
    for x in (*(nieuw.get("deelprocessen") or []), *(nieuw.get("kwaliteitsdoelen") or [])):
        gebruikt |= set(x.get("bronnen") or [])
    gebruikt |= set((nieuw.get("gemma_functie") or {}).get("bronnen") or [])
    if (nieuw.get("definitie_formeel_bron") or {}).get("bron"):
        gebruikt.add(nieuw["definitie_formeel_bron"]["bron"])
    verloren = [b for b in rest if b not in gebruikt]
    if verloren:
        nieuw["bronnen"] = list(dict.fromkeys([*(nieuw.get("bronnen") or []), *verloren]))
    return _in_volgorde(nieuw), meld


def _in_volgorde(d: dict) -> dict:
    """De sleutels in dezelfde volgorde als het bestand; `hoofdkenmerk` komt na `vak`."""
    if "hoofdkenmerk" not in d:
        return d
    uit: dict = {}
    for k, v in d.items():
        if k == "hoofdkenmerk":
            continue
        uit[k] = v
        if k == "vak":
            uit["hoofdkenmerk"] = d["hoofdkenmerk"]
    if "hoofdkenmerk" not in uit:
        uit = {"begrip": d["begrip"], "hoofdkenmerk": d["hoofdkenmerk"], **{k: v for k, v in uit.items() if k != "begrip"}}
    return uit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--schrijf", action="store_true")
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    wiki_yaml = gam_gemeen.wiki_yaml(args.wiki)
    alle = beoordeling.alle(args.wiki, wiki_yaml)
    nieuw: dict[str, dict] = {}
    meldingen: list[str] = []
    for bid, (pad, d) in alle.items():
        nieuw[bid], m = omzetten(bid, d)
        meldingen += [f"{bid}: {x}" for x in m]
    context = {b: {**d, "beslist": alle[b][1].get("beslist")} for b, d in nieuw.items()}
    for bid, d in nieuw.items():
        genormaliseerd, open_ = beoordelingtool.normaliseer_data(d, bid, context)
        nieuw[bid] = genormaliseerd
        context[bid] = {**genormaliseerd, "beslist": alle[bid][1].get("beslist")}
        meldingen += [f"{bid}: {x}" for x in open_]
    fouten = []
    for bid, d in nieuw.items():
        f = bt.controleer(d)
        fouten += [f"{bid}: {x}" for x in f]
    veranderd = [b for b in nieuw if {k: v for k, v in nieuw[b].items() if k != "beslist"} !=
                 {k: v for k, v in alle[b][1].items() if k != "beslist"}]
    print(f"{len(veranderd)} van {len(nieuw)} beoordelingen veranderen; {len(fouten)} fouten; {len(meldingen)} meldingen.")
    for m in meldingen:
        print("melding:", m)
    for f in fouten:
        print("fout:", f)
    woorden = lambda ds: sum(len(str(a.get("onderbouwing", "")).split()) for d in ds for a in (d.get("kenmerken") or {}).values()  # noqa: E731
                             if isinstance(a, dict))
    print(f"woorden in de onderbouwing van de kenmerken: {woorden(d for _, d in alle.values())} → {woorden(nieuw.values())}")
    print("kenmerken per beoordeling:", sum(len(d.get('kenmerken') or {}) for _, d in alle.values()), "→",
          sum(len(d.get('kenmerken') or {}) for d in nieuw.values()))
    if args.schrijf:
        if fouten:
            print("Niets geschreven: eerst de fouten oplossen.")
            return 1
        for bid in veranderd:
            beoordeling.schrijf(alle[bid][0], nieuw[bid], wiki_yaml)
        print(f"{len(veranderd)} beoordelingen geschreven. Draai tools/beslissen.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
