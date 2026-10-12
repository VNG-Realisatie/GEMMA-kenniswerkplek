"""Signalen bij het beslissen: zachte waarschuwingen over het oordeel, en harde controles op de bronduidingen.

Een waarschuwing noemt de regel uit AGENTS.md of kennismodel/modelleerregels.md bij naam ("regel Naamvorm"). De AI beoordeelt elke waarschuwing
inhoudelijk: oplossen in de beoordeling, of toelichten als de tekst terecht is. Een waarschuwing houdt niets tegen.

Harde controles (fouten) gaan over wat de AI met de hand schrijft buiten de beoordelingen: de bronduidingen (de
bronduiding, schakel in de herleidbaarheid) en de omzettingen van de modellen in `sources/modellen/`.
"""
from __future__ import annotations

import re
from pathlib import Path

import bepaal_type
import gam_gemeen
import kennismodel as km
from llmwiki import frontmatter, modellen, paths, sources

VERBODEN_ZINNEN = ("structureel buiten scope", "structureel out-of-scope", "structureel geen ggm-match",
                   "per definitie", "ggm modelleert nooit")
REGISTR_RE = re.compile(r"\b\w*registr\w*", re.IGNORECASE)


def _teksten(data: dict) -> list[str]:
    """Alle lopende tekst van de AI in een beoordeling."""
    teksten = [data.get("definitie", ""), data.get("toelichting", "")]
    for veld in ("beschrijving", "naamkeuze", "generalisatie"):
        teksten += data.get(veld, [])
    for alineas in data.get("per_onderwerp", {}).values():
        teksten += alineas
    teksten += [a.get("onderbouwing", "") for a in data.get("kenmerken", {}).values()]
    return [t for t in teksten if t]


def per_begrip(bid: str, data: dict, uitkomst: dict, onderwerpnamen: list[str], beslist: dict) -> list[str]:
    w = []
    tekst = "\n".join(_teksten(data))
    laag = tekst.lower()
    for zin in VERBODEN_ZINNEN:
        if zin in laag:
            w.append(f"{bid}: '{zin}': alleen met een concrete, domeinspecifieke reden (regel Geen absolute taal)")
    for woord in sorted({m.group(0) for m in REGISTR_RE.finditer(tekst)}):
        w.append(f"{bid}: '{woord}': is dit een argument voor het type? (regel Beslistabel beslist)")
    if uitkomst["soort"] != "element":
        return w

    naam = data["begrip"]
    definitie = data.get("definitie", "")
    if len(re.findall(r"[.!?](?:\s+[A-Z]|\s*$)", definitie)) > 1:
        w.append(f"{bid}: de definitie lijkt meer dan één zin (regel Begrijpelijk)")
    eerste_woord = naam.split(" ")[0].lower()
    paginatype = uitkomst["paginatype"]
    if paginatype == "bedrijfsproces" and not eerste_woord.endswith(("en", "aan")):  # infinitief: behandelen, toestaan
        w.append(f"{bid}: procesnaam '{naam}' begint niet met een werkwoord, zoals 'Behandelen aanvraag'; het "
                 "zelfstandig naamwoord wordt synoniem (regel Naamvorm)")
    if paginatype == "bedrijfsfunctie" and eerste_woord.endswith("en"):
        w.append(f"{bid}: functienaam '{naam}' lijkt een proces; een functie heet naar het gebied van gedrag, zoals "
                 "'Vergunningverlening' (regel Naamvorm)")
    contexten = {s["context"].lower() for s in data.get("synoniemen", [])}
    if paginatype not in ("bedrijfsproces", "dienst") and contexten & {"beleid", "dagelijks gebruik"} and "wet" not in contexten:
        w.append(f"{bid}: een gangbare term staat als synoniem en geen wetsterm: is de naam de wetsterm? De naam komt uit "
                 "de gangbare taal (regel Bronvoorrang)")
    synoniemen: dict[str, set[str]] = {}
    for s in data.get("synoniemen", []):  # dezelfde naam mag in meer contexten staan (GGM en GEMMA)
        synoniemen.setdefault(s["naam"].strip().lower(), set()).add(s["context"].lower())
    for veld, context in (("ggm", "ggm_entiteit"), ("gemma", "gemma_naam")):
        modelnaam = str((beslist.get(veld) or {}).get(context) or "").strip()
        if modelnaam and modelnaam.lower() != naam.lower() and veld not in synoniemen.get(modelnaam.lower(), set()):
            w.append(f"{bid}: de {veld.upper()}-naam '{modelnaam}' wijkt af van de naam: neem haar op in synoniemen met "
                     f"context '{veld.upper()}' (regel Match op betekenis)")
    if onderwerpnamen:
        patroon = re.compile(rf"\b[Ii]n (?:de |het )?(?:{'|'.join(re.escape(n) for n in onderwerpnamen)})\b|\b[Ii]n dit onderwerp\b")
        algemeen = re.sub(re.escape(naam), "", " ".join([definitie, *data.get("beschrijving", [])]), flags=re.IGNORECASE)
        for m in patroon.finditer(algemeen):
            w.append(f"{bid}: '{m.group(0)}': definitie en beschrijving gaan over het element zelf; wat alleen in één "
                     "onderwerp speelt, hoort onder per_onderwerp (regel Los van het onderwerp)")
    return w


STRUCTUREEL = ("voorzitter", "lid van", "deel van", "onderdeel", "omvat", "bevat", "bestaat uit", "maakt deel uit")


def generiek_proces(alle: dict[str, dict], elementen: dict[str, dict], bid: str) -> bool:
    """Een generiek bedrijfsproces: zijn kernobject is een generiek object, dat geen levensloopproces heeft. Het hangt,
    net als een levensloopproces, onder het beleidsdomein van zijn kernobject (Beleidsdomeinindeling)."""
    kern = alle.get(bid, {}).get("kernobject")
    return (elementen.get(bid, {}).get("procesniveau") == "bedrijfsproces"
            and (elementen.get(kern) or {}).get("objectniveau") == "generiek")


def indeling(alle: dict[str, dict], elementen: dict[str, dict], relaties: list[tuple[str, dict]],
             gemeld: set[str] = frozenset()) -> list[str]:
    """Signalen bij stap 7 (indeling): de plaats in de procesindeling naar kernobject, afwijkingen van het kennismodel.
    Een element in een procesarchitectuur-terugmelding over het kennismodel (`gemeld`) geeft geen signaal over die
    afwijking."""
    w = []
    niveau = {b: u.get("procesniveau") for b, u in elementen.items() if u["paginatype"] == "bedrijfsproces"}
    ouders: dict[str, list[str]] = {}
    for van, r in relaties:
        if r["soort"] == "aggregatie" and r["naar"] in elementen and van in elementen:
            ouders.setdefault(r["naar"], []).append(van)
    for bid, n in sorted(niveau.items()):
        boven = [o for o in ouders.get(bid, []) if o in niveau]
        if n == "bedrijfsproces" and not any(niveau[o] == "levensloopproces" for o in boven) \
                and not generiek_proces(alle, elementen, bid):
            w.append(f"{bid}: hangt onder geen levensloopproces: aggregatie vanaf het levensloopproces van het "
                     "kernobject ontbreekt (procesindeling naar kernobject)")
        if len(boven) > 2:
            w.append(f"{bid}: meer dan twee ouders in de procesindelingen: {', '.join(sorted(boven))}")
    for bid, u in sorted(elementen.items()):
        if u["paginatype"] == "bedrijfsinteractie" and bid not in gemeld and not any(
                r["soort"] == "bediening" and r["naar"] == bid and niveau.get(van) in ("levensloopproces", "bedrijfsproces")
                for van, r in relaties):
            w.append(f"{bid}: geen bedrijfsproces bedient deze bedrijfsinteractie; in een ketensamenwerking komen de "
                     "bedrijfsprocessen van de partijen samen (GEMMA Online, Proceshiërarchie)")
        if u["paginatype"] == "beleidskader" and not any(
                {(elementen.get(van) or {}).get("paginatype"), (elementen.get(r["naar"]) or {}).get("paginatype")} & {"product", "dienst"}
                and bid in (van, r["naar"]) for van, r in relaties):
            w.append(f"{bid}: geen dienst of product heeft dit beleidskader als grondslag; bij voorkeur hangt het aan een "
                     "dienst of product (modelleerafspraken Dienst), aan een proces alleen tijdelijk")
        if u.get("generiek") and not alle[bid].get("gemma_generiek"):
            w.append(f"{bid}: generiek, maar geen `gemma_generiek`: specialisatie van een GEMMA-element of voorstel aan GEMMA")
        if u["paginatype"] == "actor":
            for r in alle[bid].get("relaties", []):
                doel = elementen.get(r["naar"])
                if doel and doel["paginatype"] == "actor" and r["soort"].startswith("associatie") \
                        and not any(x in (r.get("naam") or "").lower() for x in STRUCTUREEL):
                    w.append(f"{bid}: relatie '{r.get('naam')}' tussen actoren is geen structuur (deel van, lid van, "
                             "voorzitter van): een handeling loopt via rollen en processen of een gebeurtenis")
    return w


DOMEINFUNCTIE = "Bedrijfsfunctie domein"  # GEMMA type van een functie op domeinniveau (Uitvoering fysieke leefomgeving)


def is_domeinfunctie(data: dict, gemma_data: dict) -> bool:
    """Een functie op domeinniveau: haar GEMMA-match heeft GEMMA type *Bedrijfsfunctie domein*; ze hangt via `domein` aan
    de domeingroepering. Elke andere functie hangt onder een bovenliggende functie."""
    g = gemma_data.get("elementen", {}).get((data.get("gemma") or {}).get("id") or "")
    return g is not None and g["eigenschappen"].get("GEMMA type") == DOMEINFUNCTIE


def beleidsdomein_domeinen(gemma_data: dict) -> dict[str, set[str]]:
    """Beleidsdomein (naam, kleine letters) → de GEMMA-domeinen die het aggregeren of omvatten (groeperingen in de map
    *Domeinen*). Een beleidsdomein kan onder meer domeinen vallen (Erfgoed: Publieksdiensten en Fysieke leefomgeving)."""
    el = gemma_data.get("elementen", {})
    domeinen = {i for i, e in el.items() if e["type"] == "grouping" and e["map"].endswith("Domeinen")}
    uit: dict[str, set[str]] = {}
    for r in gemma_data.get("relaties", {}).values():
        if r["type"] not in ("aggregation-relationship", "composition-relationship") or r["bron"] not in domeinen:
            continue
        doel = el.get(r["doel"])
        if doel and doel["type"] == "grouping" and doel["eigenschappen"].get("GEMMA type") == "Beleidsdomein":
            uit.setdefault(doel["naam"].strip().lower(), set()).add(el[r["bron"]]["naam"])
    return uit


def domein_en_beleidsdomein(alle: dict[str, dict], elementen: dict[str, dict], gemma_data: dict,
                            gemeld: list[dict] = ()) -> list[str]:
    """Signalen bij een product of dienst waarvan het domein (Functie-indeling naar domein) niet past bij de GEMMA-domeinen
    van zijn beleidsdomein (Beleidsdomeinindeling): in GEMMA aggregeert een domein de beleidsdomeinen. Een beleidsdomein
    dat GEMMA niet kent, geeft een signaal als zijn producten en diensten in meer domeinen vallen: het voorstel aan GEMMA
    moet zeggen onder welk domein het hoort. Het model mag afwijken, mits teruggemeld: een
    procesarchitectuur-terugmelding (`gemeld`) met het element of het beleidsdomein dekt het signaal."""
    if not gemma_data:
        return []
    gemelde_elementen = {e for m in gemeld for e in m.get("elementen") or []}
    gemelde_bd = {m["beleidsdomein"].strip().lower() for m in gemeld if m.get("beleidsdomein")}
    bekend = beleidsdomein_domeinen(gemma_data)
    w = []
    nieuw: dict[str, dict[str, list[str]]] = {}
    for bid in sorted(b for b, u in elementen.items() if u["paginatype"] in ("product", "dienst")):
        bd, domein = alle[bid].get("beleidsdomein"), alle[bid].get("domein")
        if not bd or not domein:
            continue
        if bid in gemelde_elementen or bd.strip().lower() in gemelde_bd:
            continue
        domeinen = bekend.get(bd.strip().lower())
        if domeinen is None:
            nieuw.setdefault(bd, {}).setdefault(domein, []).append(bid)
        elif domein not in domeinen:
            w.append(f"{bid}: domein '{domein}' past niet bij beleidsdomein '{bd}', dat in GEMMA onder "
                     f"{', '.join(sorted(domeinen))} valt (Beleidsdomeinindeling tegenover Functie-indeling naar domein); "
                     "herzien of terugmelden (modellen/gemma/terugmeldingen/procesarchitectuur.yaml)")
    for bd, per_domein in sorted(nieuw.items()):
        if len(per_domein) > 1:
            delen = "; ".join(f"{d}: {', '.join(ids)}" for d, ids in sorted(per_domein.items()))
            w.append(f"beleidsdomein '{bd}' (nieuw voor GEMMA): producten en diensten in {len(per_domein)} domeinen "
                     f"({delen}); leg vast hoe GEMMA het indeelt en meld het terug "
                     "(modellen/gemma/terugmeldingen/procesarchitectuur.yaml)")
    return w

def functie_indeling(alle: dict[str, dict], elementen: dict[str, dict], relaties: list[tuple[str, dict]],
                     gemma_data: dict) -> list[str]:
    """Signalen bij de Functie-indeling naar domein: elke functie onder domeinniveau hangt onder één bovenliggende functie,
    in hetzelfde domein en volgens de GEMMA-functieketen; een dienst onder één functie in hetzelfde domein. De bovenliggende
    functie is een element met een aggregatie, of een GEMMA-functie zonder beoordeling (`gemma_functie`, de hiërarchie komt
    as-is uit het model). Een product hangt via `domein` aan de domeingroepering, want ArchiMate laat een functie geen
    product aggregeren."""
    import gemma as gemmatool

    h = gemmatool.functiehierarchie(gemma_data) if gemma_data.get("elementen") else {"onder": {}, "boven": {}, "wortels": []}
    w = []
    functies = {b for b, u in elementen.items() if u["paginatype"] == "bedrijfsfunctie"}

    def gemma_boven(bid: str) -> str | None:
        return (alle[bid].get("gemma_functie") or {}).get("id")

    def gemma_naam(i: str) -> str:
        return gemma_data.get("elementen", {}).get(i, {}).get("naam", i)

    def domein_van_gemma(i: str) -> set[str]:
        return set(gemmatool.functie_domein_namen(gemma_data, h, i)) if gemma_data.get("elementen") else set()

    for bid in sorted(b for b, u in elementen.items() if u["paginatype"] == "product"):
        boven = sorted(van for van, r in relaties if r["soort"] == "aggregatie" and r["naar"] == bid and van in functies)
        if boven or gemma_boven(bid):
            w.append(f"{bid}: product onder een functie ({', '.join(boven) or gemma_naam(gemma_boven(bid))}): een product "
                     "hangt via `domein` aan de domeingroepering (Functie-indeling naar domein)")
    for bid in sorted(b for b, u in elementen.items() if u["paginatype"] == "dienst"):
        boven = sorted(van for van, r in relaties if r["soort"] == "aggregatie" and r["naar"] == bid and van in functies)
        gf = gemma_boven(bid)
        if not boven and not gf:
            w.append(f"{bid}: hangt onder geen functie: aggregatie vanaf een functie of `gemma_functie` ontbreekt "
                     "(Functie-indeling naar domein)")
        if len(boven) + bool(gf) > 1:
            w.append(f"{bid}: meer functies ({', '.join([*boven, *([gemma_naam(gf)] if gf else [])])}): kies die in het eigen domein")
        for ouder in boven:
            if alle[ouder].get("domein") != alle[bid].get("domein"):
                w.append(f"{bid}: domein '{alle[bid].get('domein')}' wijkt af van dat van de functie {ouder} "
                         f"('{alle[ouder].get('domein')}')")
        if gf and domein_van_gemma(gf) and alle[bid].get("domein") not in domein_van_gemma(gf):
            w.append(f"{bid}: domein '{alle[bid].get('domein')}' wijkt af van dat van de functie {gemma_naam(gf)} "
                     f"({', '.join(sorted(domein_van_gemma(gf)))})")
    gemma_id = {b: (alle[b].get("gemma") or {}).get("id") for b in functies}
    gemma_agg = {(r["bron"], r["doel"]) for r in gemma_data.get("relaties", {}).values()
                 if r["type"] in gemmatool.FUNCTIEKETEN}
    for bid in sorted(functies):
        boven = sorted(van for van, r in relaties if r["soort"] == "aggregatie" and r["naar"] == bid and van in functies)
        gf = gemma_boven(bid)
        if is_domeinfunctie(alle[bid], gemma_data):
            if boven or gf:
                w.append(f"{bid}: functie op domeinniveau met een bovenliggende functie "
                         f"({', '.join([*boven, *([gemma_naam(gf)] if gf else [])])}): ze hangt aan de domeingroepering "
                         "(Functie-indeling naar domein)")
            continue
        if not boven and not gf:
            w.append(f"{bid}: hangt onder geen bovenliggende functie: aggregatie vanaf een functie of `gemma_functie` "
                     "ontbreekt (Functie-indeling naar domein)")
        if len(boven) + bool(gf) > 1:
            w.append(f"{bid}: meer bovenliggende functies ({', '.join([*boven, *([gemma_naam(gf)] if gf else [])])}): "
                     "kies die in de keten van het eigen domein")
        for ouder in boven:
            if alle[ouder].get("domein") != alle[bid].get("domein"):
                w.append(f"{bid}: domein '{alle[bid].get('domein')}' wijkt af van dat van de bovenliggende functie "
                         f"{ouder} ('{alle[ouder].get('domein')}')")
            if not gemma_id[ouder]:
                w.append(f"{bid}: de bovenliggende functie {ouder} heeft geen GEMMA-match; een functie wordt geaggregeerd "
                         "door een bestaande GEMMA-functie")
            elif gemma_id[bid] and (gemma_id[ouder], gemma_id[bid]) not in gemma_agg:
                w.append(f"{bid}: in GEMMA aggregeert {ouder} deze functie niet: de wiki volgt de GEMMA-functieketen")
        if gf:
            if domein_van_gemma(gf) and alle[bid].get("domein") not in domein_van_gemma(gf):
                w.append(f"{bid}: domein '{alle[bid].get('domein')}' wijkt af van dat van de bovenliggende functie "
                         f"{gemma_naam(gf)} ({', '.join(sorted(domein_van_gemma(gf)))})")
            if gemma_id[bid] and (gf, gemma_id[bid]) not in gemma_agg:
                w.append(f"{bid}: in GEMMA aggregeert {gemma_naam(gf)} deze functie niet: de wiki volgt de GEMMA-functieketen")
    return w


def _relatie_sleutels(alle: dict[str, dict], uitkomsten: dict[str, dict | None]):
    """(sleutel per element, de relaties als (van, relatie, bron-sleutel, doel-sleutel)) van de elementen met een pagina."""
    sleutel = {b: km.sleutel_van(u["archimate_type"]) for b, u in uitkomsten.items()
               if u and u["soort"] == "element" and not bepaal_type.is_afgewezen(alle[b])}
    return sleutel, [(van, r, sleutel[van], sleutel[r["naar"]]) for van in sleutel
                     for r in alle[van].get("relaties", []) if r["naar"] in sleutel]


def _eronder(bid: str, relaties: list) -> set[str]:
    """Het element en wat eronder ligt: wat het omvat (aggregatie, ook de functieketen) of bedient (bediening), de
    gebeurtenissen die het triggert en zijn specialisaties die een element zijn; ook verder naar beneden."""
    groep, nieuw = {bid}, [bid]
    while nieuw:
        g = nieuw.pop()
        for van, r, _, doel in relaties:
            soort = km.kale_soort(r["soort"])
            onder = (r["naar"] if van == g and (soort in ("aggregatie", "bediening")
                                                 or (soort == "triggering" and doel == "gebeurtenis"))
                     else van if r["naar"] == g and soort == "specialisatie" else None)
            if onder and onder not in groep:
                groep.add(onder)
                nieuw.append(onder)
    return groep


def kennismodel(alle: dict[str, dict], uitkomsten: dict[str, dict | None], zonder: set[str] = frozenset()) -> list[str]:
    """Relaties buiten het kennismodel (geldig in ArchiMate, maar niet toegestaan) en kernrelaties die ontbreken.
    Beide houden niets tegen: de beoordeling legt vast wat de bron zegt, de export filtert op het kennismodel. Een
    kernrelatie telt ook als ze bij iets eronder ligt (`_eronder`): de rol bij een bedrijfsproces onder het
    levensloopproces of de functie, de bediening door een functie in de functieketen, de toegang tot een specialisatie,
    de triggering door een gebeurtenis die het element triggert. Een dienst zonder grondslag (`zonder`) hoeft geen
    kernrelatie te hebben: zij wordt niet uitgewerkt, en haar kenmerken steunen op de bron."""
    sleutel, relaties = _relatie_sleutels(alle, uitkomsten)
    w = []
    for van, r, bron, doel in relaties:
        if km.toegestaan(bron, r["soort"], doel):
            continue
        weg = km.weggefilterd(bron, r["soort"], doel)
        w.append(f"{van}: relatie '{r['soort']}' naar '{r['naar']}' ({bron} → {doel}) staat "
                 + (f"niet in het kennismodel ({weg.reden}); " if weg else "nergens in het kennismodel; ")
                 + "de export laat haar weg (regel Relaties tussen onderwerpen)")
    for bid, d in sorted(alle.items()):
        if bid not in sleutel or bid in zonder:
            continue
        for kenmerk, k in d["kenmerken"].items():
            kern = km.kernrelaties(kenmerk)
            if k["waarde"] != "ja" or not kern:
                continue
            groep = _eronder(bid, relaties)
            if not any((van in groep or r["naar"] in groep) and any(
                    (x.bron, km.kale_soort(x.soort), x.doel) == (bron, km.kale_soort(r["soort"]), doel) for x in kern)
                    for van, r, bron, doel in relaties):
                w.append(f"{bid}: kenmerk {kenmerk} is ja, maar er is geen relatie van de kernrelatie "
                         f"({'; '.join(f'{x.bron} {km.kale_soort(x.soort)} {x.doel}' for x in kern)}) (regel Beslistabel beslist)")
    return w


def over_begrippen(alle: dict[str, dict], uitkomsten: dict[str, dict | None], gemeld: set[str] = frozenset(),
                   zonder: set[str] = frozenset()) -> list[str]:
    """Signalen over de begrippen samen. Een dienst zonder grondslag (`zonder`) wordt door geen proces gerealiseerd."""
    w = []
    elementen = {b: u for b, u in uitkomsten.items() if u and u["soort"] == "element"
                 and not bepaal_type.is_afgewezen(alle[b])}
    relaties = [(van, r) for van in elementen for r in alle[van].get("relaties", [])]
    for bid, u in elementen.items():
        if u["paginatype"] == "dienst" and bid not in zonder and not any(r["soort"] == "realisatie" and r["naar"] == bid for _, r in relaties):
            w.append(f"{bid}: geen proces of functie realiseert deze dienst: proces als kandidaat voorleggen (beslistabel)")
        if u["paginatype"] == "gebeurtenis" and not any(van == bid and r["soort"] == "triggering" for van, r in relaties):
            w.append(f"{bid}: deze gebeurtenis start geen gedrag: proces als kandidaat voorleggen (beslistabel)")
    w += indeling(alle, elementen, relaties, gemeld)
    return w


def _gekoppeld(alle: dict[str, dict], a: str, b: str) -> bool:
    """Twee beoordelingen met een gelijke naam zijn verantwoord: de een is `synoniem_van` de ander, of een homoniem."""
    for x, y in ((a, b), (b, a)):
        doel = (alle[x].get("synoniem_van") or "").strip().lower()
        if doel and doel in (y, alle[y]["begrip"].strip().lower()):
            return True
        if any(h.get("element") == y for h in alle[x].get("homoniemen", [])):
            return True
    return False


def modulariteit(alle: dict[str, dict], uitkomsten: dict[str, dict | None], onderwerpen: dict[str, dict],
                 zonder: set[str] = frozenset()) -> list[str]:
    """Signalen voor één model over alle onderwerpen (regels Eén element in het hele model, Thuishoren, Relaties tussen
    onderwerpen). Het thuisonderwerp is het eerste in `onderwerpen`. Een dienst zonder grondslag (`zonder`) mag zonder
    relaties zijn."""
    w = []
    gedeeld = gam_gemeen.gedeelde_onderwerpen(onderwerpen)
    beoordeeld = {b for b, u in uitkomsten.items() if u}
    elementen = {b for b in beoordeeld if uitkomsten[b]["soort"] == "element" and not bepaal_type.is_afgewezen(alle[b])}

    namen: dict[str, set[str]] = {}
    for bid in beoordeeld:
        for naam in [alle[bid]["begrip"], *[s["naam"] for s in alle[bid].get("synoniemen", [])]]:
            namen.setdefault(naam.strip().lower(), set()).add(bid)
    for naam, ids in sorted(namen.items()):
        ids_ = sorted(ids)
        if any(not _gekoppeld(alle, a, b) for i, a in enumerate(ids_) for b in ids_[i + 1:]):
            w.append(f"'{naam}' is naam of synoniem van {', '.join(ids_)}: één begrip (één beoordeling, of "
                     "`synoniem_van`) of een homoniem (`homoniemen`) (regel Eén element in het hele model)")

    for veld, sleutel in (("gemma", "id"), ("ggm", "guid")):
        per_match: dict[str, list[str]] = {}
        for bid in sorted(elementen):
            m = alle[bid].get(veld) or {}
            if m.get(sleutel) and m.get("sterkte") in ("exact", "sterk"):
                per_match.setdefault(m[sleutel], []).append(bid)
        for match, ids_ in sorted(per_match.items()):
            if len(ids_) > 1:
                w.append(f"{', '.join(ids_)}: zelfde {veld.upper()}-match {match} (exact of sterk): één element, of een "
                         "zwakkere match (regel Eén element in het hele model)")

    for bid in sorted(elementen):
        ko = alle[bid].get("kernobject")
        if ko in elementen and not gam_gemeen.is_generiek(alle[ko], uitkomsten[ko], gedeeld)                 and gam_gemeen.thuis(alle[bid]) != gam_gemeen.thuis(alle[ko]):
            w.append(f"{bid}: thuisonderwerp '{gam_gemeen.thuis(alle[bid])}', maar het kernobject {ko} hoort bij "
                     f"'{gam_gemeen.thuis(alle[ko])}' (regel Thuishoren)")

    for bid in sorted(b for b in beoordeeld if uitkomsten[b]["soort"] == "verwijzing"):
        tekst = (alle[bid]["kenmerken"].get("betekenis_in_onderwerp") or {}).get("onderbouwing", "")
        for oid, o in sorted(onderwerpen.items()):
            if oid != gam_gemeen.thuis(alle[bid]) and re.search(
                    rf"\b(?:{re.escape(oid)}|{re.escape(o.get('naam') or oid)})\b", tekst, re.IGNORECASE):
                w.append(f"{bid}: verwijst naar onderwerp '{oid}', dat nu bestaat: beoordeel het daar en zet '{oid}' "
                         "als eerste in onderwerpen (regel Thuishoren)")

    alle_rel = gam_gemeen.relaties_per_onderwerp(alle, elementen)
    for bid in sorted(elementen):
        if not alle_rel[bid] and bid not in zonder:
            w.append(f"{bid}: geen relatie met een ander element (regel Relaties tussen onderwerpen)")
    specifiek = {b for b in elementen if not gam_gemeen.is_generiek(alle[b], uitkomsten[b], gedeeld)}
    for bid, per in sorted(gam_gemeen.relaties_per_onderwerp(alle, specifiek).items()):
        eigen = per.get(gam_gemeen.thuis(alle[bid]), 0)
        for oid, n in sorted(per.items()):
            if oid != gam_gemeen.thuis(alle[bid]) and n > eigen:
                w.append(f"{bid}: {n} relaties met elementen van '{oid}' en {eigen} met het eigen thuisonderwerp "
                         f"'{gam_gemeen.thuis(alle[bid])}': hoort het daar thuis? (regel Thuishoren)")
    return w


def bronduidingen(wiki_root: Path, onderwerpen: dict[str, dict]) -> list[str]:
    """Harde controles op de bronduiding: plaats, eigen bron-id, de regel 'Bron:' naar laag 1 (sources/raw of sources/modellen), de relatietabel,
    en dat de bron in de bronnenlijst van het onderwerp staat."""
    fouten = []
    repo = paths.find_repo_root(wiki_root)
    for pad in sorted(wiki_root.glob("onderwerpen/*/bronduidingen/*.md")) + sorted(wiki_root.glob("modellen/*/bronduidingen/*.md")):
        fouten.append(f"{pad.relative_to(wiki_root).as_posix()}: hoort in een map per brontype, "
                      f"{pad.parent.name}/<brontype>/")
    for pad in gam_gemeen.bronduidingen(wiki_root):
        rel = pad.relative_to(wiki_root).as_posix()
        page = frontmatter.read(pad)
        onderwerp, model, bron_id = page.meta.get("onderwerp"), page.meta.get("model"), page.meta.get("id")
        soort = gam_gemeen.brontype(wiki_root, bron_id) or "zonder-brontype"
        # modellen/<model>/bronduidingen/<brontype>/ of onderwerpen/<onderwerp>/bronduidingen/<brontype>/
        eigenaar = pad.parent.parent.parent.name
        if eigenaar != (model or onderwerp) or pad.parent.name != soort:
            fouten.append(f"{rel}: hoort in {'modellen' if model else 'onderwerpen'}/{model or onderwerp}/bronduidingen/{soort}/")
        if bron_id != pad.stem or bron_id not in (page.meta.get("bronnen") or []):
            fouten.append(f"{rel}: id is de bestandsnaam en staat zelf in bronnen:")
        laag1 = sources.bron_dir(repo, bron_id)
        tekst = {(laag1 / f"{bron_id}.md").resolve(), (laag1 / f"{bron_id}.json").resolve()}  # de tekst, of bij een model de omzetting
        regel = re.search(r"(?m)^Bron: .*$", page.body)
        gelinkt = {gam_gemeen.doel_van_link(pad, m.group("doel")) for m in gam_gemeen.LINK_RE.finditer(regel.group(0))} if regel else set()
        if not tekst & gelinkt:
            fouten.append(f"{rel}: onder de titel ontbreekt 'Bron:' met een link naar de tekst van de bron in laag 1 ({bron_id}.md) "
                          f"(llmwiki source bronregel {bron_id} --van <pad> --schrijf)")
        rijen = gam_gemeen.tabel(gam_gemeen.sectie(page.body, "Relaties"))
        if rijen and not {"Van", "Werkwoord", "Naar", "Vindplaats"} <= set(rijen[0]):
            fouten.append(f"{rel}: de relatietabel mist kolom Van, Werkwoord, Naar of Vindplaats")
        if onderwerp in onderwerpen and bron_id not in onderwerpen[onderwerp].get("bronnen", []):
            fouten.append(f"{rel}: de bron staat niet in de bronnen van onderwerpen/{onderwerp}/afbakening.yaml")
    return fouten


def modelbestanden(wiki_root: Path) -> list[str]:
    """De omzettingen van het GGM en het GEMMA-model in `sources/modellen/` zijn gemaakt door llmwiki en worden niet met
    de hand bewerkt."""
    fouten = []
    for sleutel in ("ggm", "gemma"):
        pad = gam_gemeen.model_json(wiki_root, sleutel)
        melding = modellen.controleer_json(pad) if pad.exists() else None
        if melding:
            fouten.append(melding)
    return fouten


LANDELIJK = ("europese-regelgeving", "rijksregelgeving")
UPL_BRON = re.compile(r"-(vng|logius)-upl-")  # de aangevulde lijsten van GEMMA en de UPL van Logius


def _grondslag(alle: dict[str, dict], elementen: dict[str, dict], brontype):
    """(elementen zonder vervallen, landelijk(b), upl(b)): of een element een landelijke wettelijke grondslag heeft (een
    bron van `europese-regelgeving` of `rijksregelgeving`, of een relatie *is grondslag voor* van een beleidskader van de
    EU of het Rijk), en of het een UPL-dienst is (de UPL als bron)."""
    elementen = {b: u for b, u in elementen.items() if alle[b].get("status") != "afgewezen"}
    gegrond = {r["naar"] for b, u in elementen.items()
               if u["paginatype"] == "beleidskader" and alle[b].get("regelgever") in ("EU", "rijk")
               for r in alle[b].get("relaties", []) if r.get("naam") == "is grondslag voor"}

    def bronnen(b: str) -> set[str]:
        data = alle[b]
        ids = set((data.get("beslist") or {}).get("bronnen", []))
        for r in data.get("relaties", []):
            ids |= set(r.get("bronnen") or [])
        return ids

    def landelijk(b: str) -> bool:
        return b in gegrond or any(brontype(i) in LANDELIJK for i in bronnen(b))

    def upl(b: str) -> bool:
        return elementen[b]["paginatype"] in ("product", "dienst") and any(UPL_BRON.search(i) for i in bronnen(b))

    return elementen, landelijk, upl


def zonder_grondslag(alle: dict[str, dict], elementen: dict[str, dict], brontype) -> set[str]:
    """De hoek *zonder grondslag* (regel Wettelijke grondslag): een UPL-dienst zonder landelijke wettelijke grondslag. Zo'n
    dienst wordt uitgewerkt voor zover mogelijk (een element met pagina, zonder processen, objecten, gebeurtenissen of
    rollen), teruggemeld aan de procesarchitectuur en niet geëxporteerd. Een VNG-modelverordening is nooit grondslag."""
    elementen, landelijk, upl = _grondslag(alle, elementen, brontype)
    return {b for b in elementen if upl(b) and not landelijk(b)}


def wettelijke_grondslag(alle: dict[str, dict], elementen: dict[str, dict], brontype) -> tuple[list[str], list[str]]:
    """Regel Wettelijke grondslag. `brontype` geeft per bron-id het brontype.

    Fout: een relatie *is grondslag voor* vanuit een VNG-modelverordening (een VNG-modelverordening is nooit
    grondslag; die relatie heet *werkt uit voor*); en een bedrijfsproces dat een dienst zonder grondslag realiseert
    (`zonder_grondslag`; zo'n dienst wordt niet uitgewerkt).
    Signaal: een element zonder landelijke wettelijke bron (`_grondslag`), behalve een UPL-dienst, een bedrijfsfunctie en
    een beleidskader. Een vervallen element (status `afgewezen`) telt niet mee."""
    fouten, signalen_ = [], []
    elementen, landelijk, upl = _grondslag(alle, elementen, brontype)
    for b, u in sorted(elementen.items()):
        if u["paginatype"] != "beleidskader":
            continue
        for r in alle[b].get("relaties", []):
            if r.get("naam") != "is grondslag voor":
                continue
            if alle[b].get("regelgever") == "VNG-modelverordening":
                fouten.append(f"{b}: een VNG-modelverordening is nooit grondslag; noem de relatie naar '{r['naar']}' 'werkt uit voor' "
                              "(regel Wettelijke grondslag)")
    zonder = zonder_grondslag(alle, elementen, brontype)
    for b, u in sorted(elementen.items()):
        if u["paginatype"] in ("beleidskader", "bedrijfsfunctie") or landelijk(b) or upl(b):
            continue
        signalen_.append(f"{b}: geen landelijke wettelijke bron (europese-regelgeving of rijksregelgeving); "
                         "voeg de wet met artikel toe, of het element blijft niet (regel Wettelijke grondslag)")
    for b, u in sorted(elementen.items()):
        if u["paginatype"] != "bedrijfsproces":
            continue
        for r in alle[b].get("relaties", []):
            if r["soort"] == "realisatie" and r["naar"] in zonder:
                fouten.append(f"{b}: realiseert UPL-dienst '{r['naar']}' zonder landelijke grondslag; zo'n dienst "
                              "wordt niet uitgewerkt in processen (regel Wettelijke grondslag)")
    return fouten, signalen_


def zonder_grondslag_terugmelding(zonder: set[str], pa_meldingen: list[dict]) -> list[str]:
    """Signaal: een dienst zonder grondslag zonder procesarchitectuur-terugmelding (regel Wettelijke grondslag)."""
    gemeld = {e for m in pa_meldingen for e in m.get("elementen") or []}
    return [f"{b}: UPL-dienst zonder landelijke grondslag zonder procesarchitectuur-terugmelding; meld haar terug als "
            "geen wettelijke taak (regel Wettelijke grondslag)" for b in sorted(zonder - gemeld)]
