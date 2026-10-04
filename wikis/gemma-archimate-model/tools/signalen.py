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
    if paginatype == "bedrijfsproces" and not eerste_woord.endswith("en"):
        w.append(f"{bid}: procesnaam '{naam}' begint niet met een werkwoord, zoals 'Behandelen aanvraag'; het "
                 "zelfstandig naamwoord wordt synoniem (regel Naamvorm)")
    if paginatype == "bedrijfsfunctie" and eerste_woord.endswith("en"):
        w.append(f"{bid}: functienaam '{naam}' lijkt een proces; een functie heet naar het gebied van gedrag, zoals "
                 "'Vergunningverlening' (regel Naamvorm)")
    contexten = {s["context"].lower() for s in data.get("synoniemen", [])}
    if paginatype not in ("bedrijfsproces", "dienst") and contexten & {"beleid", "dagelijks gebruik"} and "wet" not in contexten:
        w.append(f"{bid}: een gangbare term staat als synoniem en geen wetsterm: is de naam de wetsterm? De naam komt uit "
                 "de gangbare taal (regel Bronvoorrang)")
    synoniemen = {s["naam"].strip().lower(): s["context"].lower() for s in data.get("synoniemen", [])}
    for veld, context in (("ggm", "ggm_entiteit"), ("gemma", "gemma_naam")):
        modelnaam = str((afgeleid.get(veld) or {}).get(context) or "").strip()
        if modelnaam and modelnaam.lower() != naam.lower() and synoniemen.get(modelnaam.lower()) != veld:
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


def indeling(alle: dict[str, dict], elementen: dict[str, dict], relaties: list[tuple[str, dict]]) -> list[str]:
    """Signalen bij stap 7 (indeling): de plaats in de procesindeling naar taak, afwijkingen van het kennismodel."""
    w = []
    niveau = {b: u.get("procesniveau") for b, u in elementen.items() if u["paginatype"] == "bedrijfsproces"}
    ouders: dict[str, list[str]] = {}
    for van, r in relaties:
        if r["soort"] == "aggregatie" and r["naar"] in elementen and van in elementen:
            ouders.setdefault(r["naar"], []).append(van)
    for bid, n in sorted(niveau.items()):
        boven = [o for o in ouders.get(bid, []) if o in niveau]
        if n in ("bedrijfsproces", "ketenproces") and not any(niveau[o] in ("taak", "cluster naar soort werk") for o in boven):
            w.append(f"{bid}: hangt onder geen taak: aggregatie vanaf een taak ontbreekt (procesindeling naar taak)")
        if n == "deelproces" and not any(niveau[o] in ("bedrijfsproces", "ketenproces") for o in boven):
            w.append(f"{bid}: deelproces hangt onder geen bedrijfs- of ketenproces (procesindeling naar taak)")
        if len(boven) > 2:
            w.append(f"{bid}: meer dan twee ouders in de procesindelingen: {', '.join(sorted(boven))}")
        if n == "deelproces" and any(r["soort"] == "realisatie" and (elementen.get(r["naar"]) or {}).get("paginatype") == "dienst"
                                     for van, r in relaties if van == bid):
            w.append(f"{bid}: een deelproces levert een dienst; het kennismodel laat een deelproces een deelservice "
                     "leveren (regel 398): afwijking, voorstel aan het GEMMA-team")
        if n == "ketenproces":
            eigen = set(alle[bid].get("onderwerpen", []))
            for deel in boven_van(bid, relaties, niveau, "deelproces"):
                if not eigen & set(alle[deel].get("onderwerpen", [])):
                    w.append(f"{bid}: ketenproces met deelproces '{deel}' uit een andere taak: afwijking van het "
                             "kennismodel (regel 590)")
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


def boven_van(bid: str, relaties: list[tuple[str, dict]], niveau: dict[str, str | None], welk: str) -> list[str]:
    return [r["naar"] for van, r in relaties if van == bid and r["soort"] == "aggregatie" and niveau.get(r["naar"]) == welk]


def over_begrippen(alle: dict[str, dict], uitkomsten: dict[str, dict | None]) -> list[str]:
    w = []
    elementen = {b: u for b, u in uitkomsten.items() if u and u["soort"] == "element"}
    relaties = [(van, r) for van in elementen for r in alle[van].get("relaties", [])]
    for bid, u in elementen.items():
        if u["paginatype"] == "dienst" and not any(r["soort"] == "realisatie" and r["naar"] == bid for _, r in relaties):
            w.append(f"{bid}: geen proces of functie realiseert deze dienst: proces als kandidaat voorleggen (beslistabel)")
        if u["paginatype"] == "gebeurtenis" and not any(van == bid and r["soort"] == "triggering" for van, r in relaties):
            w.append(f"{bid}: deze gebeurtenis start geen gedrag: proces als kandidaat voorleggen (beslistabel)")
    w += indeling(alle, elementen, relaties)
    bij: dict[str, list[str]] = {}
    for bid in elementen:
        for s in alle[bid].get("synoniemen", []):
            bij.setdefault(s["naam"].strip().lower(), []).append(bid)
    for naam, ids in sorted(bij.items()):
        if len(ids) > 1:
            w.append(f"synoniem '{naam}' staat bij meer elementen ({', '.join(ids)}): homoniem of fout")
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
