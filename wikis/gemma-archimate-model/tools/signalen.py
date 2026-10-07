"""Signalen bij het afleiden: zachte waarschuwingen over het oordeel, en harde controles op de bronanalyses.

Een waarschuwing noemt de regel uit AGENTS.md bij naam ("regel Naamvorm"). De AI beoordeelt elke waarschuwing
inhoudelijk: oplossen in de beoordeling, of toelichten als de tekst terecht is. Een waarschuwing houdt niets tegen.

Harde controles (fouten) gaan over wat de AI met de hand schrijft buiten de beoordelingen: de bronanalyses (de
domein-lens, schakel in de herleidbaarheid) en de gegenereerde modelmappen `ggm/` en `gemma/`.
"""
from __future__ import annotations

import re
from pathlib import Path

import gam_gemeen
from llmwiki import frontmatter, paths

VERBODEN_ZINNEN = ("structureel buiten scope", "structureel out-of-scope", "structureel geen ggm-match",
                   "per definitie", "ggm modelleert nooit")
REGISTR_RE = re.compile(r"\b\w*registr\w*", re.IGNORECASE)


def _teksten(data: dict) -> list[str]:
    """Alle lopende tekst van de AI in een beoordeling."""
    teksten = [data.get("definitie", ""), data.get("toelichting", "")]
    for veld in ("beschrijving", "grondslag_toelichting", "naamkeuze", "generalisatie"):
        teksten += data.get(veld, [])
    for alineas in data.get("per_onderwerp", {}).values():
        teksten += alineas
    teksten += [a.get("onderbouwing", "") for a in data.get("kenmerken", {}).values()]
    return [t for t in teksten if t]


def per_begrip(bid: str, data: dict, uitkomst: dict, onderwerpnamen: list[str], afgeleid: dict) -> list[str]:
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
        modelnaam = str((afgeleid.get(veld) or {}).get(context) or "").strip()
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


def indeling(alle: dict[str, dict], elementen: dict[str, dict], relaties: list[tuple[str, dict]],
             gemeld: set[str] = frozenset()) -> list[str]:
    """Signalen bij stap 7 (indeling): de plaats in de procesindeling naar taak, afwijkingen van het kennismodel. Een
    element in een procesarchitectuur-terugmelding over het kennismodel (`gemeld`) geeft geen signaal over die afwijking."""
    w = []
    niveau = {b: u.get("procesniveau") for b, u in elementen.items() if u["paginatype"] == "bedrijfsproces"}
    ouders: dict[str, list[str]] = {}
    for van, r in relaties:
        if r["soort"] == "aggregatie" and r["naar"] in elementen and van in elementen:
            ouders.setdefault(r["naar"], []).append(van)
    for bid, n in sorted(niveau.items()):
        boven = [o for o in ouders.get(bid, []) if o in niveau]
        if n == "ketenproces" and not any(niveau[o] in ("taak", "cluster naar soort werk") for o in boven):
            w.append(f"{bid}: hangt onder geen taak: aggregatie vanaf een taak ontbreekt (procesindeling naar taak)")
        if n == "bedrijfsproces" and not any(niveau[o] in ("taak", "cluster naar soort werk", "ketenproces") for o in boven):
            w.append(f"{bid}: hangt onder geen taak of ketenproces: aggregatie ontbreekt (procesindeling naar taak)")
        if n == "deelproces" and not any(niveau[o] == "bedrijfsproces" for o in boven):
            w.append(f"{bid}: deelproces hangt onder geen bedrijfsproces (procesindeling naar taak)")
        if len(boven) > 2:
            w.append(f"{bid}: meer dan twee ouders in de procesindelingen: {', '.join(sorted(boven))}")
        if n == "deelproces" and bid not in gemeld and any(r["soort"] == "realisatie" and (elementen.get(r["naar"]) or {}).get("paginatype") == "dienst"
                                     for van, r in relaties if van == bid):
            w.append(f"{bid}: een deelproces levert een dienst; het kennismodel laat een deelproces een deelservice "
                     "leveren (regel 398): afwijking, voorstel aan het GEMMA-team")
    for bid, u in sorted(elementen.items()):
        if u["paginatype"] == "beleidskader" and not any(
                {(elementen.get(van) or {}).get("paginatype"), (elementen.get(r["naar"]) or {}).get("paginatype")} >= {"product", "beleidskader"}
                and bid in (van, r["naar"]) for van, r in relaties):
            w.append(f"{bid}: geen product heeft dit beleidskader als grondslag; bij voorkeur hangt het aan een product "
                     "(kennismodel regel 595), aan een proces of dienst alleen tijdelijk")
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
    moet zeggen onder welk domein het hoort (besluit 2026-10-05). Het model mag afwijken, mits teruggemeld: een
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
                     "herzien of terugmelden (beoordelingen/procesarchitectuur-terugmeldingen.yaml)")
    for bd, per_domein in sorted(nieuw.items()):
        if len(per_domein) > 1:
            delen = "; ".join(f"{d}: {', '.join(ids)}" for d, ids in sorted(per_domein.items()))
            w.append(f"beleidsdomein '{bd}' (nieuw voor GEMMA): producten en diensten in {len(per_domein)} domeinen "
                     f"({delen}); leg vast hoe GEMMA het indeelt en meld het terug "
                     "(beoordelingen/procesarchitectuur-terugmeldingen.yaml)")
    return w

def functie_indeling(alle: dict[str, dict], elementen: dict[str, dict], relaties: list[tuple[str, dict]],
                     gemma_data: dict) -> list[str]:
    """Signalen bij de Functie-indeling naar domein: elke functie onder domeinniveau wordt geaggregeerd door één
    bovenliggende functie (een element), in hetzelfde domein en volgens de GEMMA-functieketen; een dienst door één
    functie in hetzelfde domein (besluiten 2026-10-04). Een product hangt via `domein` aan de domeingroepering, want
    ArchiMate laat een functie geen product aggregeren (besluit 2026-10-05)."""
    w = []
    functies = {b for b, u in elementen.items() if u["paginatype"] == "bedrijfsfunctie"}
    for bid in sorted(b for b, u in elementen.items() if u["paginatype"] == "product"):
        boven = sorted(van for van, r in relaties if r["soort"] == "aggregatie" and r["naar"] == bid and van in functies)
        if boven:
            w.append(f"{bid}: product onder een functie ({', '.join(boven)}): een product hangt via `domein` aan de "
                     "domeingroepering (Functie-indeling naar domein)")
    for bid in sorted(b for b, u in elementen.items() if u["paginatype"] == "dienst"):
        boven = sorted(van for van, r in relaties if r["soort"] == "aggregatie" and r["naar"] == bid and van in functies)
        if not boven:
            w.append(f"{bid}: hangt onder geen functie: aggregatie vanaf een functie ontbreekt (Functie-indeling naar domein)")
        if len(boven) > 1:
            w.append(f"{bid}: meer functies ({', '.join(boven)}): kies die in het eigen domein")
        for ouder in boven:
            if alle[ouder].get("domein") != alle[bid].get("domein"):
                w.append(f"{bid}: domein '{alle[bid].get('domein')}' wijkt af van dat van de functie {ouder} "
                         f"('{alle[ouder].get('domein')}')")
    gemma_id = {b: (alle[b].get("gemma") or {}).get("id") for b in functies}
    gemma_agg = {(r["bron"], r["doel"]) for r in gemma_data.get("relaties", {}).values()
                 if r["type"] == "aggregation-relationship"}
    for bid in sorted(functies):
        boven = sorted(van for van, r in relaties if r["soort"] == "aggregatie" and r["naar"] == bid and van in functies)
        if is_domeinfunctie(alle[bid], gemma_data):
            if boven:
                w.append(f"{bid}: functie op domeinniveau met een bovenliggende functie ({', '.join(boven)}): ze hangt "
                         "aan de domeingroepering (Functie-indeling naar domein)")
            continue
        if not boven:
            w.append(f"{bid}: hangt onder geen bovenliggende functie: aggregatie vanaf een functie ontbreekt "
                     "(Functie-indeling naar domein)")
        if len(boven) > 1:
            w.append(f"{bid}: meer bovenliggende functies ({', '.join(boven)}): kies die in de keten van het eigen domein")
        for ouder in boven:
            if alle[ouder].get("domein") != alle[bid].get("domein"):
                w.append(f"{bid}: domein '{alle[bid].get('domein')}' wijkt af van dat van de bovenliggende functie "
                         f"{ouder} ('{alle[ouder].get('domein')}')")
            if not gemma_id[ouder]:
                w.append(f"{bid}: de bovenliggende functie {ouder} heeft geen GEMMA-match; een functie wordt geaggregeerd "
                         "door een bestaande GEMMA-functie")
            elif gemma_id[bid] and (gemma_id[ouder], gemma_id[bid]) not in gemma_agg:
                w.append(f"{bid}: in GEMMA aggregeert {ouder} deze functie niet: de wiki volgt de GEMMA-functieketen")
    return w


def over_begrippen(alle: dict[str, dict], uitkomsten: dict[str, dict | None], gemeld: set[str] = frozenset()) -> list[str]:
    w = []
    elementen = {b: u for b, u in uitkomsten.items() if u and u["soort"] == "element"}
    relaties = [(van, r) for van in elementen for r in alle[van].get("relaties", [])]
    for bid, u in elementen.items():
        if u["paginatype"] == "dienst" and not any(r["soort"] == "realisatie" and r["naar"] == bid for _, r in relaties):
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


def modulariteit(alle: dict[str, dict], uitkomsten: dict[str, dict | None], onderwerpen: dict[str, dict]) -> list[str]:
    """Signalen voor één model over alle onderwerpen (regels Eén element in het hele model, Thuishoren, Relaties tussen
    onderwerpen; besluit 2026-10-06). Het thuisonderwerp is het eerste in `onderwerpen`."""
    w = []
    beoordeeld = {b for b, u in uitkomsten.items() if u}
    elementen = {b for b in beoordeeld if uitkomsten[b]["soort"] == "element"}

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
        if ko in elementen and not gam_gemeen.is_generiek(alle[ko], uitkomsten[ko])                 and gam_gemeen.thuis(alle[bid]) != gam_gemeen.thuis(alle[ko]):
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
        if not alle_rel[bid]:
            w.append(f"{bid}: geen relatie met een ander element (regel Relaties tussen onderwerpen)")
    specifiek = {b for b in elementen if not gam_gemeen.is_generiek(alle[b], uitkomsten[b])}
    for bid, per in sorted(gam_gemeen.relaties_per_onderwerp(alle, specifiek).items()):
        eigen = per.get(gam_gemeen.thuis(alle[bid]), 0)
        for oid, n in sorted(per.items()):
            if oid != gam_gemeen.thuis(alle[bid]) and n > eigen:
                w.append(f"{bid}: {n} relaties met elementen van '{oid}' en {eigen} met het eigen thuisonderwerp "
                         f"'{gam_gemeen.thuis(alle[bid])}': hoort het daar thuis? (regel Thuishoren)")
    return w


def bronanalyses(wiki_root: Path, onderwerpen: dict[str, dict]) -> list[str]:
    """Harde controles op de domein-lens: plaats, eigen bron-id, de regel 'Bron:' naar sources/raw, de relatietabel,
    en dat de bron in de bronnenlijst van het onderwerp staat."""
    fouten = []
    repo = paths.find_repo_root(wiki_root)
    map_ = wiki_root / paths.load_wiki_yaml(wiki_root)["page_types"].get("bronanalyse", {}).get("dir", "bronanalyses")
    for pad in sorted(map_.glob("*/*.md")):
        rel = pad.relative_to(wiki_root).as_posix()
        page = frontmatter.read(pad)
        onderwerp, bron_id = page.meta.get("onderwerp"), page.meta.get("id")
        if pad.parent.name != onderwerp:
            fouten.append(f"{rel}: hoort in {map_.name}/{onderwerp}/")
        if bron_id != pad.stem or bron_id not in (page.meta.get("bronnen") or []):
            fouten.append(f"{rel}: id is de bestandsnaam en staat zelf in bronnen:")
        tekst = (repo / "sources" / "raw" / f"{bron_id}.md").resolve()
        regel = re.search(r"(?m)^Bron: .*$", page.body)
        gelinkt = {gam_gemeen.doel_van_link(pad, m.group("doel")) for m in gam_gemeen.LINK_RE.finditer(regel.group(0))} if regel else set()
        if tekst not in gelinkt:
            fouten.append(f"{rel}: onder de titel ontbreekt 'Bron:' met een link naar sources/raw/{bron_id}.md "
                          f"(llmwiki source bronregel {bron_id} --van <pad> --schrijf)")
        rijen = gam_gemeen.tabel(gam_gemeen.sectie(page.body, "Relaties"))
        if rijen and not {"Van", "Werkwoord", "Naar", "Vindplaats"} <= set(rijen[0]):
            fouten.append(f"{rel}: de relatietabel mist kolom Van, Werkwoord, Naar of Vindplaats")
        if onderwerp in onderwerpen and bron_id not in onderwerpen[onderwerp].get("bronnen", []):
            fouten.append(f"{rel}: de bron staat niet in de bronnen van beoordelingen/onderwerpen/{onderwerp}.yaml")
    return fouten


def modelmappen(wiki_root: Path) -> list[str]:
    """`ggm/` en `gemma/` zijn gegenereerd door tools/ggm.py en tools/gemma.py en worden niet met de hand bewerkt."""
    fouten = []
    for map_ in ("ggm", "gemma"):
        for pad in sorted((wiki_root / map_).rglob("*")):
            melding = None
            if pad.suffix == ".md":
                melding = gam_gemeen.controleer_gegenereerd(pad)
            elif pad.suffix == ".json":
                melding = gam_gemeen.controleer_json_gegenereerd(pad)
            if melding:
                fouten.append(f"{pad.relative_to(wiki_root).as_posix()}: {melding}")
    return fouten
