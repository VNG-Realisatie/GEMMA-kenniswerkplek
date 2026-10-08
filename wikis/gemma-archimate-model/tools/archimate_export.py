"""Export naar Archi: de elementen en relaties van deze wiki als Archi-bestand (`.archimate`), met de id's van GEMMA.

Het bestand is bedoeld om in Archi te bekijken (File › Open) en om in het GEMMA-model te importeren
(File › Import › Another model into selected model): Archi voegt samen op id. Daarom:
- een element met een GEMMA-match (`gemma.id` in de beoordeling) krijgt het GEMMA-id en staat in dezelfde mappen (met
  dezelfde map-id's) als in GEMMA; naam en definitie komen uit de wiki, de GEMMA-eigenschappen gaan letterlijk mee. De
  match is de verantwoordelijkheid van de wiki en de redacteur: de export vertrouwt haar;
- een nieuw element krijgt een vast id (uuid5 van het begrip-id) in de map `wiki-gemma-model`; een volgende export
  werkt het dus bij in plaats van het te verdubbelen;
- een relatie krijgt het id van de GEMMA-relatie van hetzelfde type tussen dezelfde elementen, anders een vast id;
- elk element en elke relatie krijgt `wiki-gemma-model exportdatum`: na de import verwijdert het jArchi-script van de
  skill wat een oudere datum heeft (volledige sync).

Indelingen (analyses/indelingen.md): een element krijgt de eigenschappen procesniveau, objectniveau en zijn indelingsvelden;
een aggregatie tussen processen heeft `indeling` en `procesniveau` ("levensloopproces → bedrijfsproces"), een aggregatie
tussen functies, en van een functie naar een product of dienst, `indeling`; een functie hangt alleen op domeinniveau (GEMMA
type *Bedrijfsfunctie domein*) aan de domeingroepering, daaronder aan haar bovenliggende functie; een product of dienst aan
een functie; een proces zonder GEMMA-match staat in de map `Procesindeling naar kernobject`, een bedrijfsinteractie in de
map `Ketensamenwerking` (zoals in GEMMA); een levensloopproces zonder GEMMA-match krijgt GEMMA type *Bedrijfsproces
(cluster)* en valt, net als een bedrijfsinteractie, in de Beleidsdomeinindeling onder het beleidsdomein van zijn
kernobject; `gemma_generiek` wordt een specialisatie naar het GEMMA-element (dat
letterlijk meegaat); beleidsdomein en domein worden een aggregatie vanuit de bestaande GEMMA-groepering, of vanuit een
nieuwe groepering in de map van de wiki; doelgroep een aggregatie vanuit de GEMMA-rol van de doelgroep (GEMMA type `Groep`).

Een element dat in geen enkele indeling staat, houdt de export tegen (`--check` meldt het ook).

Het kennismodel (wiki.yaml `kennismodel`): de elementen en relaties van de views van het GEMMA-kennismodel in Over GEMMA
(de ArchiMate-concepten die GEMMA gebruikt) gaan mee met de id's van Over GEMMA, in de map `Kennismodel` onder de
wiki-map van hun laag. Ze hangen met een aggregatie aan één groep `Kennismodel` (map `Other / wiki-gemma-model /
Kennismodel`); onder die groep hangen de groepen Bedrijfsarchitectuur, Applicatiearchitectuur, Technische architectuur en
Motivatie, die elk de elementen van hun laag aggregeren (een element van een andere laag hangt aan Kennismodel zelf).

Alleen begrippen met status `goedgekeurd` (akkoord van de redacteur); `--concept` neemt ook kandidaat en review mee,
voor het bekijken, en schrijft naar het kladblok. Het GEMMA-model moet als Archi-bestand zijn ingelezen
(tools/gemma.py release <bestand.archimate>): de AMEFF heeft geen map-id's.

Gebruik (vanuit de wikimap):
    uv run python tools/archimate_export.py [--concept] [--uit <pad>]
    uv run python tools/archimate_export.py --check        # alleen de voorwaarden controleren
"""
from __future__ import annotations

import argparse
import re
import sys
import uuid
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402
import relaties as relatietool  # noqa: E402
import signalen  # noqa: E402
from llmwiki import beoordeling, paths  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT
TOOL = "tools/archimate_export.py"
PREFIX = "wiki-gemma-model"
EXPORT = Path("export") / "gemma-archimate-model.archimate"
RAPPORT = Path("export") / "rapport.md"
CONCEPT = Path(".work") / "export" / "gemma-archimate-model-concept.archimate"
NS = uuid.uuid5(uuid.NAMESPACE_URL, "https://github.com/VNG-Realisatie/GEMMA-kenniswerkplek/wikis/gemma-archimate-model")
ARCHIMATE_NS = "http://www.archimatetool.com/archimate"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
XSI = f"{{{XSI_NS}}}type"
# De vaste bovenste mappen van een Archi-model, in de volgorde van Archi.
BOVENSTE = ("strategy", "business", "application", "technology", "motivation", "implementation_migration", "other",
            "relations", "diagrams")
MOTIVATIE = {"stakeholder", "driver", "assessment", "goal", "outcome", "principle", "requirement", "constraint",
             "meaning", "value"}
# ArchiMate-toegangstype in Archi; zonder attribuut leest Archi "schrijven", dus altijd expliciet.
ACCESS_TYPE = {"schrijven": "0", "lezen": "1", None: "2", "lezen-schrijven": "3"}


def eig(naam: str) -> str:
    return f"{PREFIX} {naam}"


def vast_id(*delen: str) -> str:
    return "id-" + uuid.uuid5(NS, "/".join(delen)).hex


OBJECTEN = Path("beoordelingen") / "objecten.yaml"
BELEIDSDOMEINEN = Path("beoordelingen") / "beleidsdomeinen.yaml"


def object_sleutels(register: dict | None) -> dict[str, str]:
    """Begrip-id → het begrip-id waarvan het Archi-object wordt voortgezet (na hernoemen, samenvoegen of splitsen),
    langs een keten (a → b → c). Zo houdt een element zijn id in Archi en blijven views werken."""
    direct = {o["element"]: o["object_van"] for o in (register or {}).get("objecten", [])}
    uit = {}
    for bid in direct:
        sleutel, gezien = bid, set()
        while sleutel in direct and sleutel not in gezien:
            gezien.add(sleutel)
            sleutel = direct[sleutel]
        uit[bid] = sleutel
    return uit


def vorige_typen(pad: Path) -> dict[str, str]:
    """Id → xsi:type van de elementen in de vorige export; Archi kan het type van een bestaand object niet wijzigen."""
    if not pad.exists():
        return {}
    return {e.get("id"): e.get(XSI) for e in ET.parse(pad).getroot().iter("element")
            if e.get(XSI) and "Relationship" not in e.get(XSI)}


def xsi_type(archimate_type: str) -> str:
    """`business-object` → `archimate:BusinessObject`; omgekeerde van gemma.archimate_type."""
    return "archimate:" + "".join(d.capitalize() for d in archimate_type.split("-"))


def bovenste_map(archimate_type: str) -> str:
    return "motivation" if archimate_type in MOTIVATIE else "business"


def relatie_archimate(soort: str) -> tuple[str, str | None]:
    """'toegang (registreren)' → ('access-relationship', 'schrijven'); 'associatie (gericht)' → ('association-relationship', 'gericht')."""
    naam, _, toevoeging = soort.partition(" (")
    toevoeging = toevoeging.rstrip(")") or None
    if naam == "toegang":
        return "access-relationship", relatietool.toegangstype(toevoeging)
    return relatietool.RELATIES[naam] + "-relationship", toevoeging


@dataclass
class Map:
    id: str
    naam: str
    type: str = ""
    documentatie: str = ""
    eigenschappen: dict = field(default_factory=dict)
    mappen: dict = field(default_factory=dict)       # id → Map
    objecten: list = field(default_factory=list)     # ET.Element


@dataclass
class Uitkomst:
    xml: bytes = b""
    fouten: list[str] = field(default_factory=list)
    gekoppeld: list[dict] = field(default_factory=list)
    nieuw: list[dict] = field(default_factory=list)
    relaties_gekoppeld: int = 0
    relaties_nieuw: int = 0
    overgeslagen: list[str] = field(default_factory=list)
    groeperingen_nieuw: list[str] = field(default_factory=list)
    specialisaties: list[str] = field(default_factory=list)
    indelingen: int = 0
    kennismodel_elementen: int = 0
    kennismodel_relaties: int = 0
    kennismodel_wiki: list[str] = field(default_factory=list)
    zonder_plaats: list[str] = field(default_factory=list)


# --- Voorwaarden ---


def controleer(wiki_root: Path, gemma_data: dict) -> list[str]:
    """Fouten die een export tegenhouden: afleiden met fouten of verouderd, render niet actueel, GEMMA zonder mappen."""
    import afleiden
    import render

    res = afleiden.afleiden(wiki_root, schrijven=False)
    fouten = [f"afleiden: {f}" for f in res.fouten]
    if res.gewijzigd:
        fouten.append(f"afleiden is verouderd voor {', '.join(res.gewijzigd)}: draai eerst 'uv run python tools/afleiden.py'")
    if not res.fouten:
        _, schrijven, verwijderen = render.verschillen(wiki_root)
        if schrijven or verwijderen:
            fouten.append("de pagina's wijken af van de beoordelingen: draai eerst 'uv run python tools/afleiden.py'")
    if gemma_data.get("model", {}).get("formaat") != "archimate" or "mappen" not in gemma_data:
        fouten.append("het GEMMA-model is niet als Archi-bestand ingelezen (geen map-id's): neem een .archimate op met "
                      "'uv run python tools/gemma.py release <bestand.archimate> --id <bron-id>' (skill gemma-archimate-model-gemma-release)")
    return fouten


# --- Opbouw ---


def selectie(begrippen: dict[str, dict], log: str, concept: bool) -> tuple[dict[str, dict], list[str]]:
    """De elementen die meegaan: goedgekeurd (met promotieregel in log.md), of bij concept alles behalve afgewezen."""
    gekozen, fouten = {}, []
    for bid, data in begrippen.items():
        uitkomst = (data.get("afgeleid") or {}).get("uitkomst") or {}
        if uitkomst.get("soort") != "element" or data.get("status") == "afgewezen":
            continue
        if data.get("status") == "goedgekeurd":
            if not beoordeling.goedgekeurd_in_log(log, bid, data):
                fouten.append(f"{bid}: status goedgekeurd zonder overeenkomende regel in log.md")
                continue
        elif not concept:
            continue
        gekozen[bid] = data
    return gekozen, fouten


class Bouwer:
    def __init__(self, gemma_data: dict, tijdstempel: str, concept: bool):
        self.gemma = gemma_data
        self.tijdstempel = tijdstempel
        self.concept = concept
        self.wortel: dict[str, Map] = {}
        self.profielen: set[str] = set()
        bovenste = {m["type"]: m for m in gemma_data.get("mappen", {}).values() if not m["ouder"] and m["type"]}
        for soort in BOVENSTE:
            m = bovenste.get(soort)
            self.wortel[soort] = (Map(m["id"], m["naam"], soort, m["documentatie"], dict(m["eigenschappen"])) if m
                                  else Map(vast_id("map", soort), soort.capitalize(), soort))
        self._index = {m.id: m for m in self.wortel.values()}
        self.meegenomen: set[str] = set()  # GEMMA-elementen die letterlijk meegaan als doel van een relatie
        self.beschreven: set[str] = set()  # GEMMA-groeperingen met de beschrijving uit het register van beleidsdomeinen
        self.relatie_ids: set[str] = set()

    def gemma_map(self, map_id: str) -> Map:
        """De map met dit GEMMA-id, met de hele keten van ouders, zoals in GEMMA."""
        if map_id in self._index:
            return self._index[map_id]
        m = self.gemma["mappen"][map_id]
        ouder = self.gemma_map(m["ouder"])
        kind = Map(m["id"], m["naam"], "", m["documentatie"], dict(m["eigenschappen"]))
        ouder.mappen[kind.id] = kind
        self._index[kind.id] = kind
        return kind

    def eigen_map(self, soort: str, namen: list[str]) -> Map:
        """`<bovenste map> / wiki-gemma-model / <namen…>` met vaste id's."""
        huidig, sleutel = self.wortel[soort], [soort]
        for naam in [PREFIX, *namen]:
            sleutel.append(naam)
            mid = vast_id("map", *sleutel)
            if mid not in huidig.mappen:
                huidig.mappen[mid] = Map(mid, naam)
                self._index[mid] = huidig.mappen[mid]
            huidig = huidig.mappen[mid]
        return huidig

    def gemeen(self, herkomst: str) -> list[tuple[str, str]]:
        return [(eig("herkomst"), herkomst), (eig("exportdatum"), self.tijdstempel),
                (eig("soort export"), "concept" if self.concept else "definitief")]


def _eigenschappen(el: ET.Element, paren: list[tuple[str, str]]) -> None:
    for sleutel, waarde in paren:
        if waarde:
            ET.SubElement(el, "property", {"key": sleutel, "value": waarde})


def _gemma_eigen(eigenschappen: dict) -> list[tuple[str, str]]:
    """De GEMMA-eigenschappen letterlijk, zonder die van een eerdere export (die komen opnieuw)."""
    return [(k, v) for k, v in eigenschappen.items() if not k.startswith(PREFIX + " ")]


def _vind_groepering(gemma_data: dict, gemma_type: str | None, naam: str, map_eindigt: str | None = None) -> dict | None:
    """Een GEMMA-groepering op naam; `gemma_type` is de eigenschap *GEMMA type*, `map_eindigt` de naam van de map."""
    for e in sorted(gemma_data["elementen"].values(), key=lambda x: x["id"]):
        if e["type"] != "grouping" or e["naam"].strip().lower() != naam.strip().lower():
            continue
        if gemma_type and e["eigenschappen"].get("GEMMA type") != gemma_type:
            continue
        if map_eindigt and not e["map"].endswith(map_eindigt):
            continue
        return e
    return None


def _vind_taakveld(gemma_data: dict, taakveld: str) -> dict | None:
    """Het GEMMA-taakveld Iv3 op het nummer vooraan (`0 Bestuur…` → `0`): de naam in de wiki en in GEMMA mag verschillen."""
    nummer = taakveld.split()[:1]
    for e in sorted(gemma_data["elementen"].values(), key=lambda x: x["id"]):
        if (e["type"] == "grouping" and e["eigenschappen"].get("GEMMA type") == "Taakveld Iv3"
                and e["naam"].split()[:1] == nummer):
            return e
    return None


def _vind_doelgroep(gemma_data: dict, naam: str) -> dict | None:
    """De GEMMA-rol van een doelgroep (*Gemeente*, *Inwoners en ondernemers*, *Ketenpartners*): een rol met de
    eigenschap *GEMMA type* `Groep`, in GEMMA in de map `Business / Bedrijfsrollen`."""
    for e in sorted(gemma_data["elementen"].values(), key=lambda x: x["id"]):
        if (e["type"] == "business-role" and e["naam"].strip().lower() == naam.strip().lower()
                and e["eigenschappen"].get("GEMMA type") == "Groep"):
            return e
    return None


def _stub(b: Bouwer, g: dict) -> None:
    """Het GEMMA-element letterlijk meenemen, zodat een relatie ernaartoe in het bestand een doel heeft."""
    if g["id"] in b.meegenomen:
        return
    b.meegenomen.add(g["id"])
    el = ET.Element("element", {XSI: xsi_type(g["type"]), "name": g["naam"], "id": g["id"]})
    if g.get("profiel"):
        el.set("profiles", g["profiel"])
        b.profielen.update(g["profiel"].split())
    if g.get("documentatie"):
        ET.SubElement(el, "documentation").text = g["documentatie"]
    _eigenschappen(el, _gemma_eigen(g["eigenschappen"]))
    b.gemma_map(g["map_id"]).objecten.append(el)


def _relatie(b: Bouwer, uit: Uitkomst, gemma_relaties: dict, rtype: str, bron: str, doel: str, herkomst: str,
             paren: list[tuple[str, str]], naam: str = "", sleutel: str | None = None) -> None:
    """Een relatie met het id van de GEMMA-relatie van hetzelfde type tussen dezelfde elementen, anders een vast id
    (uit `sleutel`, standaard de herkomst)."""
    bestaand = sorted(gemma_relaties.get((rtype, bron, doel), []), key=lambda x: x["id"])
    g = bestaand[0] if bestaand else None
    rid = g["id"] if g else vast_id("relatie", sleutel or herkomst, rtype, bron, doel)
    if rid in b.relatie_ids:
        return
    b.relatie_ids.add(rid)
    attrs = {XSI: xsi_type(rtype)}
    if naam:
        attrs["name"] = naam
    attrs.update({"id": rid, "source": bron, "target": doel})
    el = ET.Element("element", attrs)
    if g is not None and g.get("documentatie"):
        ET.SubElement(el, "documentation").text = g["documentatie"]
    alle = (_gemma_eigen(g["eigenschappen"]) if g is not None else []) + [
        (eig("id"), herkomst), *b.gemeen("gekoppeld" if g is not None else "nieuw"), *paren]
    _eigenschappen(el, alle)
    if g is not None:
        uit.relaties_gekoppeld += 1
        b.gemma_map(g["map_id"]).objecten.append(el)
    else:
        uit.relaties_nieuw += 1
        b.eigen_map("relations", []).objecten.append(el)


EIGENSCHAPPEN_INDELING = ("afnemer", "domein", "doelgroep", "regelgever", "kernobject", "taakveld", "beleidsdomein")
PROCESINDELING = "Procesindeling naar kernobject"
GEMMA_TYPE_LEVENSLOOP = "Bedrijfsproces (cluster)"  # GEMMA type van de clusters in het processenlandschap


def bouw(gemma_data: dict, begrippen: dict[str, dict], gemma_bron: str, tijdstempel: str, concept: bool = False,
         log: str = "", wiki_yaml: dict | None = None, objecten: dict | None = None,
         vorige: dict[str, str] | None = None, kennismodel: dict | None = None,
         beleidsdomeinen: dict[str, dict] | None = None) -> Uitkomst:
    uit = Uitkomst()
    sleutels = object_sleutels(objecten)
    sleutel = lambda bid: sleutels.get(bid, bid)  # noqa: E731
    gekozen, uit.fouten = selectie(begrippen, log, concept)
    b = Bouwer(gemma_data, tijdstempel, concept)
    page_types = (wiki_yaml or {}).get("page_types", {})
    ids: dict[str, str] = {}

    for bid, data in sorted(gekozen.items()):
        afgeleid = data["afgeleid"]
        atype = afgeleid["uitkomst"]["archimate_type"]
        gemma_id = (data.get("gemma") or {}).get("id")
        g = gemma_data["elementen"].get(gemma_id) if gemma_id else None
        if gemma_id and g is None:
            uit.fouten.append(f"{bid}: GEMMA-id {gemma_id} staat niet in het ingelezen GEMMA-model")
            continue
        if g is not None and g["type"] != atype:
            uit.fouten.append(f"{bid}: type {atype} wijkt af van GEMMA ({g['type']}, {gemma_id}); Archi kan het type "
                              "van een bestaand element niet wijzigen bij een import. Leg dit voor aan de redacteur.")
            continue
        eid = gemma_id or vast_id("element", sleutel(bid))
        if eid in (vorige or {}) and vorige[eid] != xsi_type(atype):
            uit.fouten.append(f"{bid}: zet het Archi-object van '{sleutel(bid)}' voort, maar het type wijzigt "
                              f"({vorige[eid]} → {xsi_type(atype)}); Archi kan het type van een bestaand object niet "
                              "wijzigen bij een import. Leg dit voor aan de redacteur (beoordelingen/objecten.yaml).")
            continue
        ids[bid] = eid
        el = ET.Element("element", {XSI: xsi_type(atype), "name": data["begrip"], "id": eid})
        if g is not None and g.get("profiel"):
            el.set("profiles", g["profiel"])
            b.profielen.update(g["profiel"].split())
        if data.get("definitie"):
            ET.SubElement(el, "documentation").text = data["definitie"]
        paren = _gemma_eigen(g["eigenschappen"]) if g is not None else []
        if g is None and afgeleid["uitkomst"].get("procesniveau") == "levensloopproces":
            paren.append(("GEMMA type", GEMMA_TYPE_LEVENSLOOP))
        paren += [(eig("id"), bid), *b.gemeen("gekoppeld" if g is not None else "nieuw"),
                  (eig("status"), data.get("status", "")),
                  (eig("GEMMA-match"), (data.get("gemma") or {}).get("sterkte", "") if g is not None else ""),
                  (eig("bronnen"), "; ".join(afgeleid.get("bronnen", []))),
                  (eig("beschrijving"), "\n\n".join(data.get("beschrijving", []))),
                  (eig("synoniemen"), "; ".join(f"{s['naam']} ({s['context']})" if s.get("context") else s["naam"]
                                                for s in data.get("synoniemen", []))),
                  (eig("pagina"), afgeleid.get("pad", "")),
                  (eig("procesniveau"), afgeleid["uitkomst"].get("procesniveau") or ""),
                  (eig("objectniveau"), afgeleid["uitkomst"].get("objectniveau") or ""),
                  (eig("generiek"), "ja" if afgeleid["uitkomst"].get("generiek") else ""),
                  *[(eig(k), data.get(k, "")) for k in EIGENSCHAPPEN_INDELING]]
        if g is not None:
            vorige_naam = g["naam"] if g["naam"] != data["begrip"] else g["eigenschappen"].get(eig("vorige naam"), "")
            vorige_def = (g["documentatie"] if g["documentatie"] != (data.get("definitie") or "").strip()
                          else g["eigenschappen"].get(eig("vorige definitie"), ""))
            paren += [(eig("vorige naam"), vorige_naam), (eig("vorige definitie"), vorige_def)]
            uit.gekoppeld.append({"id": bid, "naam": data["begrip"], "gemma_naam": g["naam"],
                                  "definitie_gewijzigd": g["documentatie"] != (data.get("definitie") or "").strip()})
            doel = b.gemma_map(g["map_id"])
        else:
            uit.nieuw.append({"id": bid, "naam": data["begrip"]})
            map_naam = Path(page_types.get(afgeleid["uitkomst"].get("paginatype"), {}).get("dir", atype)).name.capitalize()
            if afgeleid["uitkomst"].get("paginatype") == "bedrijfsproces":
                map_naam = PROCESINDELING
            if afgeleid["uitkomst"].get("paginatype") == "bedrijfsinteractie":
                map_naam = "Ketensamenwerking"
            submappen = page_types.get(afgeleid["uitkomst"].get("paginatype"), {}).get("submappen", ["taakveld", "beleidsdomein"])
            doel = b.eigen_map(bovenste_map(atype), [n for n in (map_naam, *(data.get(s) for s in submappen)) if n])
        _eigenschappen(el, paren)
        doel.objecten.append(el)

    gemma_relaties: dict[tuple, list[dict]] = {}
    for r in gemma_data["relaties"].values():
        gemma_relaties.setdefault((r["type"], r["bron"], r["doel"]), []).append(r)
    for bid, data in sorted(gekozen.items()):
        if bid not in ids:
            continue
        for i, r in enumerate(data.get("relaties", [])):
            if r["naar"] not in ids:
                uit.overgeslagen.append(f"{data['begrip']} → {r['naar']} ({r['soort']}): het doel gaat niet mee in deze export")
                continue
            rtype, toevoeging = relatie_archimate(r["soort"])
            bron_id, doel_id = ids[bid], ids[r["naar"]]
            bestaand = sorted((x for x in gemma_relaties.get((rtype, bron_id, doel_id), [])
                               if rtype != "access-relationship" or x.get("toegang", 0) == int(ACCESS_TYPE[toevoeging])),
                              key=lambda x: x["id"])
            g = bestaand[0] if bestaand else None
            rid = g["id"] if g else vast_id("relatie", sleutel(bid), r["soort"], sleutel(r["naar"]), r.get("naam", ""))
            b.relatie_ids.add(rid)
            attrs = {XSI: xsi_type(rtype)}
            if r.get("naam"):
                attrs["name"] = r["naam"]
            attrs.update({"id": rid, "source": bron_id, "target": doel_id})
            if rtype == "access-relationship":
                attrs["accessType"] = ACCESS_TYPE[toevoeging]
            if rtype == "association-relationship" and toevoeging == "gericht":
                attrs["directed"] = "true"
            el = ET.Element("element", attrs)
            if g is not None and g.get("documentatie"):
                ET.SubElement(el, "documentation").text = g["documentatie"]
            paren = _gemma_eigen(g["eigenschappen"]) if g is not None else []
            paren += [(eig("id"), f"{bid}#{i + 1}"), *b.gemeen("gekoppeld" if g is not None else "nieuw"),
                      (eig("grondslag"), r.get("grondslag", "")), (eig("bronnen"), "; ".join(r.get("bronnen", []))),
                      (eig("vindplaats"), r.get("vindplaats", ""))]
            bron_u, doel_u = data["afgeleid"]["uitkomst"], gekozen[r["naar"]]["afgeleid"]["uitkomst"]
            if rtype == "aggregation-relationship" and bron_u.get("paginatype") == doel_u.get("paginatype") == "bedrijfsproces":
                paren += [(eig("indeling"), PROCESINDELING),
                          (eig("procesniveau"), f"{bron_u.get('procesniveau')} → {doel_u.get('procesniveau')}")]
            if rtype == "aggregation-relationship" and bron_u.get("paginatype") == "bedrijfsproces" \
                    and doel_u.get("paginatype") == "gebeurtenis":
                paren.append((eig("indeling"), PROCESINDELING))
            if rtype == "aggregation-relationship" and bron_u.get("paginatype") == "bedrijfsfunctie" \
                    and doel_u.get("paginatype") in ("bedrijfsfunctie", "product", "dienst"):
                paren.append((eig("indeling"), "Functie-indeling naar domein"))
            if r.get("via"):
                paren.append((eig("specialisatie"), (begrippen.get(r["via"]) or {}).get("begrip", r["via"])))
            _eigenschappen(el, paren)
            if g is not None:
                uit.relaties_gekoppeld += 1
                b.gemma_map(g["map_id"]).objecten.append(el)
            else:
                uit.relaties_nieuw += 1
                b.eigen_map("relations", []).objecten.append(el)

    _gemma_specialisaties(b, uit, gemma_data, gekozen, ids, gemma_relaties, sleutels)
    _indelingen(b, uit, gemma_data, gekozen, ids, gemma_relaties, sleutels, beleidsdomeinen)
    if kennismodel:
        _kennismodel(b, uit, kennismodel)
    uit.zonder_plaats = _zonder_plaats(b, gekozen, ids)
    uit.xml = _serialiseer(b, gemma_bron)
    return uit


def _gemma_specialisaties(b: Bouwer, uit: Uitkomst, gemma_data: dict, gekozen: dict, ids: dict, gemma_relaties: dict,
                          sleutels: dict[str, str] | None = None) -> None:
    """`gemma_generiek`: een specialisatie naar een generiek GEMMA-element, dat letterlijk meegaat."""
    for bid, data in sorted(gekozen.items()):
        generiek = data.get("gemma_generiek")
        if not generiek or bid not in ids:
            continue
        g = gemma_data["elementen"].get(generiek["id"])
        atype = data["afgeleid"]["uitkomst"]["archimate_type"]
        if g is None:
            uit.fouten.append(f"{bid}: gemma_generiek {generiek['id']} staat niet in het ingelezen GEMMA-model")
            continue
        if g["type"] != atype:
            uit.fouten.append(f"{bid}: gemma_generiek {g['naam']} is een {g['type']}, het begrip een {atype}: een "
                              "specialisatie heeft hetzelfde type. Leg dit voor aan de redacteur.")
            continue
        if g["id"] not in ids.values():
            _stub(b, g)
        indeling = "Procesindeling naar soort werk" if atype == "business-process" else "Specialisatie van een generiek GEMMA-element"
        _relatie(b, uit, gemma_relaties, "specialization-relationship", ids[bid], g["id"], f"{bid}#gemma_generiek",
                 [(eig("indeling"), indeling), (eig("onderbouwing"), generiek.get("onderbouwing", ""))],
                 sleutel=f"{(sleutels or {}).get(bid, bid)}#gemma_generiek")
        uit.specialisaties.append(f"{data['begrip']} → {g['naam']}")


# De indelingen die een element in een bestaande GEMMA-groepering plaatsen: paginatype → (indeling, soort).
BELEIDSDOMEIN_TYPEN = ("bedrijfsobject", "product", "dienst", "beleidskader")
DOMEIN_TYPEN = ("bedrijfsfunctie", "product", "dienst")
# Een levensloopproces en een bedrijfsinteractie vallen ook in de Beleidsdomeinindeling, onder het beleidsdomein van hun
# kernobject: daarboven staat in de Procesindeling naar kernobject niets (besluit 2026-10-08).
DOELGROEP_TYPEN = ("actor", "rol", "bedrijfssamenwerking", "kanaal")


def _indelingen(b: Bouwer, uit: Uitkomst, gemma_data: dict, gekozen: dict, ids: dict, gemma_relaties: dict,
                sleutels: dict[str, str] | None = None, beleidsdomeinen: dict[str, dict] | None = None) -> None:
    """Aggregaties vanuit de GEMMA-groepering van de Beleidsdomeinindeling en de Functie-indeling naar domein, en vanuit
    de GEMMA-rol van de Doelgroepindeling; een beleidsdomein dat GEMMA niet kent wordt een nieuwe groepering onder het
    taakveld. De beschrijving uit het register van beleidsdomeinen wordt de documentatie van een nieuwe groepering, en
    bij een GEMMA-groepering een wiki-eigenschap: de documentatie van GEMMA blijft (besluit redacteur 2026-10-08)."""
    nieuwe: dict[str, str] = {}
    register = beleidsdomeinen or {}

    def aggregatie(groep_id: str, element: str, indeling: str, bid: str, gemma_groep: dict | None = None) -> None:
        if gemma_groep is not None and groep_id not in ids.values():
            _stub(b, gemma_groep)
        _relatie(b, uit, gemma_relaties, "aggregation-relationship", groep_id, element, f"{bid}#{indeling}",
                 [(eig("indeling"), indeling)], sleutel=f"{(sleutels or {}).get(bid, bid)}#{indeling}")
        uit.indelingen += 1

    for bid, data in sorted(gekozen.items()):
        if bid not in ids:
            continue
        paginatype = data["afgeleid"]["uitkomst"].get("paginatype")
        element = ids[bid]
        beleidsdomein = data.get("beleidsdomein")
        bovenaan = paginatype == "bedrijfsinteractie" or (
            paginatype == "bedrijfsproces" and data["afgeleid"]["uitkomst"].get("procesniveau") == "levensloopproces")
        if (paginatype in BELEIDSDOMEIN_TYPEN or bovenaan) and beleidsdomein:
            groep = _vind_groepering(gemma_data, "Beleidsdomein", beleidsdomein)
            if groep is None:
                if beleidsdomein not in nieuwe:
                    gid = vast_id("groepering", "beleidsdomein", beleidsdomein)
                    nieuwe[beleidsdomein] = gid
                    taakveld = data.get("taakveld")
                    el = ET.Element("element", {XSI: "archimate:Grouping", "name": beleidsdomein, "id": gid})
                    bd = register.get(beleidsdomein) or {}
                    if bd.get("beschrijving"):
                        ET.SubElement(el, "documentation").text = "\n\n".join(bd["beschrijving"])
                    _eigenschappen(el, [("GEMMA type", "Beleidsdomein"), (eig("id"), f"beleidsdomein:{beleidsdomein}"),
                                        *b.gemeen("nieuw"), (eig("taakveld"), taakveld or ""),
                                        (eig("bronnen"), "; ".join(bd.get("bronnen", [])))])
                    b.eigen_map("other", ["Beleidsdomeinindeling", taakveld] if taakveld else ["Beleidsdomeinindeling"]).objecten.append(el)
                    uit.groeperingen_nieuw.append(f"{beleidsdomein} (taakveld {taakveld or '—'})")
                    ouder = _vind_taakveld(gemma_data, taakveld) if taakveld else None
                    if ouder is not None:
                        _stub(b, ouder)
                        _relatie(b, uit, gemma_relaties, "aggregation-relationship", ouder["id"], gid,
                                 f"beleidsdomein:{beleidsdomein}", [(eig("indeling"), "Beleidsdomeinindeling")])
                aggregatie(nieuwe[beleidsdomein], element, "Beleidsdomeinindeling", bid)
            else:
                aggregatie(groep["id"], element, "Beleidsdomeinindeling", bid, groep)
                bd = register.get(beleidsdomein) or {}
                if bd.get("beschrijving") and groep["id"] not in b.beschreven:
                    b.beschreven.add(groep["id"])
                    obj = next((o for m in b.wortel.values() for o in _alle_objecten(m) if o.get("id") == groep["id"]), None)
                    if obj is not None:
                        _eigenschappen(obj, [(eig("beschrijving"), "\n\n".join(bd["beschrijving"])),
                                             (eig("bronnen"), "; ".join(bd.get("bronnen", [])))])
        if paginatype in DOMEIN_TYPEN and paginatype != "product" and not signalen.is_domeinfunctie(data, gemma_data):
            # een dienst of functie onder domeinniveau: de aggregatie vanaf de (bovenliggende) functie, een relatie in
            # de beoordeling; een product en een functie op domeinniveau hangen aan de domeingroepering
            if not any(r["soort"] == "aggregatie" and r["naar"] == bid and ids.get(van)
                       and gekozen[van]["afgeleid"]["uitkomst"].get("paginatype") == "bedrijfsfunctie"
                       for van in gekozen for r in gekozen[van].get("relaties", [])):
                uit.overgeslagen.append(f"{data['begrip']}: geen plaats in de Functie-indeling naar domein (geen "
                                        "(bovenliggende) functie in deze export)")
        elif paginatype in DOMEIN_TYPEN and data.get("domein"):
            groep = _vind_groepering(gemma_data, None, data["domein"], "Domeinen")
            if groep is None:
                uit.overgeslagen.append(f"{data['begrip']}: domein '{data['domein']}' bestaat niet als groepering in GEMMA")
            else:
                aggregatie(groep["id"], element, "Functie-indeling naar domein", bid, groep)
        if paginatype in DOELGROEP_TYPEN and data.get("doelgroep"):
            rol = _vind_doelgroep(gemma_data, data["doelgroep"])
            if rol is None:
                uit.overgeslagen.append(f"{data['begrip']}: doelgroep '{data['doelgroep']}' bestaat niet als rol in GEMMA")
            else:
                aggregatie(rol["id"], element, "Doelgroepindeling", bid, rol)



# --- Kennismodel ---

KENNISMODEL_LAGEN = {"Strategy": "strategy", "Business": "business", "Application": "application",
                     "Technology & Physical": "technology", "Motivation": "motivation", "Other": "other"}
AMEFF_TOEGANG = {"Write": "0", "Read": "1", "Access": "2", "ReadWrite": "3"}  # zonder attribuut: Write
KENNISMODEL_GROEP = "Kennismodel"
WIKI_GROEP = "Kennismodel-wiki"
TOEGANG_NAAM = {v: k for k, v in ACCESS_TYPE.items() if k} | {"2": "toegang"}
# Typen met meer dan één concept in het kennismodel: het concept waar de wiki-relaties aan hangen.
CONCEPT_VOORKEUR = {"driver": "Beleidskader", "grouping": "Groep", "business-role": "Rol", "requirement": "Implicatie"}
# Typen die de wiki gebruikt en die ook Over GEMMA niet kent: een eigen concept in de groep Kennismodel-wiki.
WIKI_CONCEPT = {"business-interaction": (
    "Bedrijfsinteractie", "Gezamenlijk gedrag van twee of meer partijen of rollen, zoals een ketensamenwerking waarin de "
    "bedrijfsprocessen van de partijen samenkomen (GEMMA Online, Proceshiërarchie; in het GEMMA-model het element "
    "Ketensamenwerking). Het GEMMA-kennismodel kent het type (nog) niet.")}
# Laag → groep onder de groep Kennismodel; elementen van een andere laag (strategie, overig) hangen aan Kennismodel zelf.
KENNISMODEL_DEELGROEPEN = {"business": "Bedrijfsarchitectuur", "application": "Applicatiearchitectuur",
                           "technology": "Technische architectuur", "motivation": "Motivatie"}


def laad_kennismodel(pad: Path, views: list[str]) -> dict:
    """De elementen en relaties die in de genoemde views van Over GEMMA (AMEFF) voorkomen, in het formaat van
    gemma.parse_ameff, met per relatie het toegangstype en of een associatie gericht is."""
    import gemma

    model = gemma.parse_ameff(pad)
    ns = {"a": gemma.AMEFF_NS}
    root = ET.parse(pad).getroot()
    gevonden = set()
    elementen, relaties = {}, {}
    for view in root.findall("a:views/a:diagrams/a:view", ns):
        naam = view.find("a:name", ns)
        if naam is None or (naam.text or "").strip() not in views:
            continue
        gevonden.add(naam.text.strip())
        for node in view.iter(f"{{{gemma.AMEFF_NS}}}node"):
            if node.get("elementRef") in model["elementen"]:
                elementen[node.get("elementRef")] = model["elementen"][node.get("elementRef")]
        for con in view.iter(f"{{{gemma.AMEFF_NS}}}connection"):
            if con.get("relationshipRef") in model["relaties"]:
                relaties[con.get("relationshipRef")] = dict(model["relaties"][con.get("relationshipRef")])
    for r in root.findall("a:relationships/a:relationship", ns):
        if r.get("identifier") in relaties:
            relaties[r.get("identifier")]["toegang"] = AMEFF_TOEGANG.get(r.get("accessType") or "Write", "0")
            relaties[r.get("identifier")]["gericht"] = r.get("isDirected") == "true"
    relaties = {k: r for k, r in relaties.items() if r["bron"] in elementen and r["doel"] in elementen}
    alle = model["elementen"]
    driehoeken = {(r["type"], alle[r["bron"]]["type"], alle[r["doel"]]["type"]) for r in model["relaties"].values()
                  if r["bron"] in alle and r["doel"] in alle}
    return {"elementen": elementen, "relaties": relaties, "ontbrekende_views": sorted(set(views) - gevonden),
            "model_elementen": alle, "model_relatietypen": driehoeken}


def _kennismodel(b: Bouwer, uit: Uitkomst, kennismodel: dict) -> None:
    """Het kennismodel: elementen en relaties met de id's van Over GEMMA, en een groep die ze allemaal aggregeert."""
    herkomst = (eig("herkomst"), "kennismodel")
    exportdatum = [p for p in b.gemeen("kennismodel") if p[0] != eig("herkomst")]

    def eigen(e: dict) -> list[tuple[str, str]]:
        return [(k, v) for k, v in e["eigenschappen"].items() if not k.startswith(PREFIX + " ")]

    laag_van: dict[str, str] = {}
    for eid, e in sorted(kennismodel["elementen"].items()):
        el = ET.Element("element", {XSI: xsi_type(e["type"]), "name": e["naam"], "id": eid})
        if e["documentatie"]:
            ET.SubElement(el, "documentation").text = e["documentatie"]
        _eigenschappen(el, [*eigen(e), (eig("id"), f"kennismodel:{eid}"), herkomst, *exportdatum])
        laag = KENNISMODEL_LAGEN.get(e["map"].split(" / ")[0], bovenste_map(e["type"]))
        laag_van[eid] = laag
        b.eigen_map(laag, [KENNISMODEL_GROEP]).objecten.append(el)
        uit.kennismodel_elementen += 1
    for rid, r in sorted(kennismodel["relaties"].items()):
        attrs = {XSI: xsi_type(r["type"])}
        if r["naam"]:
            attrs["name"] = r["naam"]
        attrs.update({"id": rid, "source": r["bron"], "target": r["doel"]})
        if r["type"] == "access-relationship":
            attrs["accessType"] = r["toegang"]
        if r["type"] == "association-relationship" and r["gericht"]:
            attrs["directed"] = "true"
        el = ET.Element("element", attrs)
        if r["documentatie"]:
            ET.SubElement(el, "documentation").text = r["documentatie"]
        _eigenschappen(el, [*eigen(r), (eig("id"), f"kennismodel:{rid}"), herkomst, *exportdatum])
        b.eigen_map("relations", [KENNISMODEL_GROEP]).objecten.append(el)
        uit.kennismodel_relaties += 1

    def groep(gid: str, naam: str, documentatie: str) -> None:
        el = ET.Element("element", {XSI: "archimate:Grouping", "name": naam, "id": gid})
        ET.SubElement(el, "documentation").text = documentatie
        _eigenschappen(el, [(eig("id"), f"kennismodel:{naam}"), herkomst, *exportdatum])
        b.eigen_map("other", [KENNISMODEL_GROEP]).objecten.append(el)

    def aggregeer(van: str, naar: str) -> None:
        rid = vast_id("relatie", "kennismodel", van, naar)
        rel = ET.Element("element", {XSI: "archimate:AggregationRelationship", "id": rid, "source": van, "target": naar})
        _eigenschappen(rel, [(eig("id"), f"kennismodel#{naar}"), herkomst, *exportdatum])
        b.relatie_ids.add(rid)
        b.eigen_map("relations", [KENNISMODEL_GROEP]).objecten.append(rel)

    gid = vast_id("groepering", "kennismodel")
    wiki_gid = vast_id("groepering", "kennismodel", "wiki")
    groep(gid, KENNISMODEL_GROEP,
          "Het GEMMA-kennismodel (Over GEMMA): de ArchiMate-concepten die GEMMA gebruikt, in groepen per architectuurlaag.")
    deel = {laag: vast_id("groepering", "kennismodel", laag) for laag in KENNISMODEL_DEELGROEPEN}
    for laag, naam in KENNISMODEL_DEELGROEPEN.items():
        if any(l == laag for l in laag_van.values()):
            groep(deel[laag], naam, f"Kennismodel: de concepten van de {naam.lower()}. Selecteer de groep of haar elementen.")
            aggregeer(gid, deel[laag])
    for eid in sorted(kennismodel["elementen"]):
        aggregeer(deel.get(laag_van[eid], gid), eid)
    _kennismodel_wiki(b, uit, kennismodel, wiki_gid, gid, groep, aggregeer, eigen, [herkomst, *exportdatum])


def _kennismodel_wiki(b: Bouwer, uit: Uitkomst, kennismodel: dict, wiki_gid: str, gid: str, groep, aggregeer, eigen,
                      gemeen: list[tuple[str, str]]) -> None:
    """Wat de inhoud van de wiki gebruikt en het kennismodel niet heeft, in de groep Kennismodel-wiki: een elementtype
    zonder concept (het concept uit Over GEMMA, als dat er één heeft) en een relatie van een type tussen twee typen die het
    kennismodel niet kent (een relatie tussen de concepten, per toegangstype één)."""
    typen: dict[str, str] = {}
    relaties = []
    for m in b.wortel.values():
        for o in _alle_objecten(m):
            if any(p.get("key") == eig("herkomst") and p.get("value") == "kennismodel" for p in o.findall("property")):
                continue
            if o.get("source"):
                relaties.append(o)
            else:
                typen[o.get("id")] = o.get(XSI).split(":")[1]
    soort = lambda x: re.sub(r"(?<!^)(?=[A-Z])", "-", x).lower()  # noqa: E731
    typen = {i: soort(t) for i, t in typen.items()}
    concept: dict[str, str] = {}  # elementtype → id van het concept in het kennismodel
    for t in sorted(set(typen.values())):
        kandidaten = sorted((e for e in kennismodel["elementen"].items() if e[1]["type"] == t), key=lambda x: x[1]["naam"])
        voorkeur = [e for e in kandidaten if e[1]["naam"] == CONCEPT_VOORKEUR.get(t)]
        if len(kandidaten) == 1 or voorkeur:
            concept[t] = (voorkeur or kandidaten)[0][0]
    nieuw: dict[str, str] = {}
    nieuwe_namen: dict[str, str] = {}
    for t in sorted(set(typen.values()) - set(concept)):
        kandidaten = [(i, e) for i, e in kennismodel["model_elementen"].items() if e["type"] == t]
        if not kandidaten and t in WIKI_CONCEPT:
            # Over GEMMA kent het type niet (business-interaction): een eigen concept van de wiki
            naam, documentatie = WIKI_CONCEPT[t]
            kandidaten = [(vast_id("kennismodel-wiki", t), {"naam": naam, "documentatie": documentatie, "map": "",
                                                            "eigenschappen": {}})]
        if len(kandidaten) != 1:
            uit.fouten.append(f"kennismodel: het type {t} heeft geen concept in het kennismodel en Over GEMMA heeft er "
                              f"{len(kandidaten)}; kies er één in CONCEPT_VOORKEUR")
            continue
        i, e = kandidaten[0]
        el = ET.Element("element", {XSI: xsi_type(t), "name": e["naam"], "id": i})
        if e["documentatie"]:
            ET.SubElement(el, "documentation").text = e["documentatie"]
        _eigenschappen(el, [*eigen(e), (eig("id"), f"kennismodel:{i}"), (eig("herkomst"), "kennismodel-wiki"), *gemeen[1:]])
        laag = KENNISMODEL_LAGEN.get(e["map"].split(" / ")[0], bovenste_map(t))
        b.eigen_map(laag, [KENNISMODEL_GROEP]).objecten.append(el)
        concept[t] = nieuw[t] = i
        nieuwe_namen[i] = e["naam"]
        uit.kennismodel_wiki.append(f"element {e['naam']} ({t})")
    bekend = {(r["type"], kennismodel["elementen"][r["bron"]]["type"], kennismodel["elementen"][r["doel"]]["type"])
              for r in kennismodel["relaties"].values()}
    groepen: dict[tuple, list] = {}
    for r in relaties:
        rtype = soort(r.get(XSI).split(":")[1].replace("Relationship", "")) + "-relationship"
        bron, doel = typen.get(r.get("source")), typen.get(r.get("target"))
        if bron is None or doel is None or (rtype, bron, doel) in bekend or bron not in concept or doel not in concept:
            continue
        toegang = r.get("accessType") if rtype == "access-relationship" else None
        groepen.setdefault((rtype, bron, doel, toegang), []).append(r)
    namen = {i: e["naam"] for i, e in kennismodel["model_elementen"].items()} | nieuwe_namen
    if not groepen and not nieuw:
        return
    groep(wiki_gid, WIKI_GROEP, "Wat de inhoud van de wiki gebruikt en het GEMMA-kennismodel (nog) niet heeft: elementtypen "
                                "en relaties tussen de concepten. Zie de map Kennismodel-wiki voor de relaties.")
    aggregeer(gid, wiki_gid)
    for t, i in nieuw.items():
        aggregeer(wiki_gid, i)
    for (rtype, bron, doel, toegang), lijst in sorted(groepen.items(), key=lambda x: tuple(map(str, x[0]))):
        rid = vast_id("relatie", "kennismodel-wiki", rtype, concept[bron], concept[doel], toegang or "")
        attrs = {XSI: xsi_type(rtype), "id": rid, "source": concept[bron], "target": concept[doel]}
        if toegang is not None:
            attrs["accessType"] = toegang
        if rtype == "association-relationship" and any(r.get("directed") == "true" for r in lijst):
            attrs["directed"] = "true"
        el = ET.Element("element", attrs)
        in_og = (rtype, bron, doel) in kennismodel["model_relatietypen"]
        ET.SubElement(el, "documentation").text = (
            f"De wiki gebruikt deze relatie {len(lijst)}× tussen {namen[concept[bron]]} en {namen[concept[doel]]}; het "
            "kennismodel heeft haar niet" + (" (Over GEMMA heeft haar wel in een andere view)." if in_og else "."))
        _eigenschappen(el, [(eig("id"), f"kennismodel-wiki#{rtype}:{bron}>{doel}:{toegang or ''}"),
                            (eig("herkomst"), "kennismodel-wiki"), *gemeen[1:], (eig("gebruikt in"), str(len(lijst))),
                            (eig("in Over GEMMA"), "ja, andere view" if in_og else "nee")])
        b.eigen_map("relations", [KENNISMODEL_GROEP, WIKI_GROEP]).objecten.append(el)
        b.relatie_ids.add(rid)
        uit.kennismodel_wiki.append(f"relatie {rtype.replace('-relationship', '')} {namen[concept[bron]]} → "
                                    f"{namen[concept[doel]]}{' (' + TOEGANG_NAAM[toegang] + ')' if toegang else ''}, "
                                    f"{len(lijst)}×{'' if in_og else ', niet in Over GEMMA'}")


def _alle_objecten(m: Map):
    yield from m.objecten
    for kind in m.mappen.values():
        yield from _alle_objecten(kind)


def _indeling_van(obj: ET.Element) -> str | None:
    return next((p.get("value") for p in obj.findall("property") if p.get("key") == eig("indeling")), None)


def _zonder_plaats(b: Bouwer, gekozen: dict, ids: dict) -> list[str]:
    """De elementen die in geen enkele indeling staan (besluit 2026-10-04: alles wordt ingedeeld, geen wezen). Een
    element staat in een indeling als een aggregatie met een indeling naar haar wijst of als zij een specialisatie met een
    indeling heeft. Een levensloopproces en een bedrijfsinteractie staan in de Beleidsdomeinindeling (besluit
    2026-10-08)."""
    geplaatst = set()
    for m in b.wortel.values():
        for r in _alle_objecten(m):
            indeling, rtype = _indeling_van(r), r.get(XSI)
            if indeling is None:
                continue
            if rtype == "archimate:AggregationRelationship":
                geplaatst.add(r.get("target"))
            elif rtype == "archimate:SpecializationRelationship":
                geplaatst.add(r.get("source"))
    zonder = []
    for bid, data in sorted(gekozen.items()):
        eid = ids.get(bid)
        if eid is None or eid in geplaatst:
            continue
        zonder.append(data["begrip"])
    return zonder


def _map_xml(m: Map, ouder: ET.Element) -> None:
    attrs = {"name": m.naam, "id": m.id}
    if m.type:
        attrs["type"] = m.type
    el = ET.SubElement(ouder, "folder", attrs)
    for kind in sorted(m.mappen.values(), key=lambda x: (x.naam.lower(), x.id)):
        _map_xml(kind, el)
    for obj in sorted(m.objecten, key=lambda x: x.get("id")):
        el.append(obj)
    if m.documentatie:
        ET.SubElement(el, "documentation").text = m.documentatie
    _eigenschappen(el, list(m.eigenschappen.items()))


def _serialiseer(b: Bouwer, gemma_bron: str) -> bytes:
    ET.register_namespace("xsi", XSI_NS)
    ET.register_namespace("archimate", ARCHIMATE_NS)
    naam = f"CONCEPT – {PREFIX}" if b.concept else PREFIX
    model = ET.Element(f"{{{ARCHIMATE_NS}}}model", {"name": naam, "id": vast_id("model"), "version": "5.0.0"})
    for soort in BOVENSTE:
        _map_xml(b.wortel[soort], model)
    ET.SubElement(model, "purpose").text = ("Export van de wiki gemma-archimate-model (GEMMA-kenniswerkplek) voor import "
                                            "in het GEMMA-model; zie de skill gemma-archimate-model-archimate-export.")
    _eigenschappen(model, [(eig("exportdatum"), b.tijdstempel), (eig("soort export"), "concept" if b.concept else "definitief"),
                           (eig("GEMMA-bron"), gemma_bron)])
    profielen = b.gemma.get("model", {}).get("profielen", {})
    for pid in sorted(b.profielen):
        p = profielen[pid]
        ET.SubElement(model, "profile", {"name": p["naam"], "id": p["id"], "conceptType": p["concept"]})
    ET.indent(model, space="  ")
    return ET.tostring(model, encoding="UTF-8", xml_declaration=True) + b"\n"


# --- Rapport en CLI ---


def rapport_md(uit: Uitkomst, tijdstempel: str, gemma_bron: str, concept: bool) -> str:
    regels = [f"# Export naar Archi ({'concept' if concept else 'definitief'})", "",
              f"Exportdatum: {tijdstempel}. GEMMA-bron: {gemma_bron}. Elementen: {len(uit.gekoppeld)} gekoppeld aan GEMMA, "
              f"{len(uit.nieuw)} nieuw. Relaties: {uit.relaties_gekoppeld} gekoppeld, {uit.relaties_nieuw} nieuw, "
              f"{len(uit.overgeslagen)} overgeslagen. Indelingen: {uit.indelingen} aggregaties vanuit een groepering, "
              f"{len(uit.specialisaties)} specialisaties naar een GEMMA-element.", ""]
    if uit.kennismodel_elementen:
        regels += [f"Kennismodel: {uit.kennismodel_elementen} elementen en {uit.kennismodel_relaties} relaties uit Over GEMMA, "
                   f"samengebracht in de groep {KENNISMODEL_GROEP} met een groep per laag (map Other / {PREFIX} / {KENNISMODEL_GROEP}).", ""]
    if uit.kennismodel_wiki:
        regels += [f"## Kennismodel-wiki", "",
                   "Wat de inhoud van de wiki gebruikt en het kennismodel niet heeft; de groep Kennismodel-wiki.", ""]
        regels += [f"- {x}" for x in uit.kennismodel_wiki] + [""]
    gewijzigd = [e for e in uit.gekoppeld if e["naam"] != e["gemma_naam"] or e["definitie_gewijzigd"]]
    if gewijzigd:
        regels += ["## Wijzigt een GEMMA-element", "", "| Begrip | Naam in GEMMA | Definitie gewijzigd |", "|---|---|---|"]
        regels += [f"| {e['naam']} | {e['gemma_naam']} | {'ja' if e['definitie_gewijzigd'] else 'nee'} |" for e in gewijzigd]
        regels.append("")
    if uit.specialisaties:
        regels += ["## Specialisaties naar een GEMMA-element", "",
                   "Het GEMMA-element gaat letterlijk mee, zonder wiki-eigenschappen; er wordt niets in gewijzigd.", ""]
        regels += [f"- {x}" for x in sorted(uit.specialisaties)] + [""]
    if uit.groeperingen_nieuw:
        regels += ["## Nieuwe groeperingen", "",
                   "Beleidsdomeinen die GEMMA niet kent; ze komen in de map van de wiki, onder het GEMMA-taakveld als dat bestaat.", ""]
        regels += [f"- {x}" for x in sorted(uit.groeperingen_nieuw)] + [""]
    if uit.nieuw:
        regels += ["## Nieuw in GEMMA", ""] + [f"- {e['naam']}" for e in sorted(uit.nieuw, key=lambda e: e["naam"].lower())] + [""]
    if uit.overgeslagen:
        regels += ["## Overgeslagen relaties", ""] + [f"- {o}" for o in uit.overgeslagen] + [""]
    return "\n".join(regels)


def main(argv: list[str] | None = None) -> int:
    import gemma

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--concept", action="store_true", help="Ook kandidaat en review, alleen om te bekijken")
    parser.add_argument("--uit", type=Path, help="Ander uitvoerbestand")
    parser.add_argument("--check", action="store_true", help="Alleen de voorwaarden controleren")
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    gemma_data = gemma.laad(args.wiki / "gemma" / "gemma_parsed.json")
    fouten = controleer(args.wiki, gemma_data)
    wiki_yaml = paths.load_wiki_yaml(args.wiki)
    gemma_bron = (wiki_yaml.get("gemma") or {}).get("bron", "")
    tijdstempel = datetime.now().isoformat(timespec="seconds")
    begrippen = {bid: data for bid, (_, data) in beoordeling.alle(args.wiki, wiki_yaml).items()}
    log = (args.wiki / "log.md").read_text(encoding="utf-8") if (args.wiki / "log.md").exists() else ""
    objecten = beoordeling.laad(args.wiki / OBJECTEN) if (args.wiki / OBJECTEN).exists() else None
    beleidsdomeinen = {x["beleidsdomein"]: x for x in beoordeling.laad(args.wiki / BELEIDSDOMEINEN).get("beleidsdomeinen", [])} \
        if (args.wiki / BELEIDSDOMEINEN).exists() else None
    vorige = vorige_typen(args.wiki / EXPORT)
    kennismodel = None
    km_config = wiki_yaml.get("kennismodel") or {}
    if km_config:
        km_pad = paths.find_repo_root(args.wiki) / "sources" / "raw" / f"{km_config['bron']}.xml"
        if km_pad.exists():
            kennismodel = laad_kennismodel(km_pad, km_config["views"])
            fouten += [f"kennismodel: view '{v}' staat niet in {km_pad.name}" for v in kennismodel["ontbrekende_views"]]
        else:
            fouten.append(f"kennismodel: bron {km_pad} ontbreekt (wiki.yaml kennismodel.bron)")
    uit = Uitkomst() if fouten else bouw(gemma_data, begrippen, gemma_bron, tijdstempel, args.concept, log, wiki_yaml,
                                         objecten, vorige, kennismodel, beleidsdomeinen)
    fouten += uit.fouten
    fouten += [f"{naam}: geen plaats in een indeling (elk element staat in minstens één indeling)" for naam in uit.zonder_plaats]
    for f in fouten:
        print(f"fout: {f}")
    if fouten:
        print(f"{len(fouten)} fout(en): er is niets geschreven.")
        return 1
    rapport = rapport_md(uit, tijdstempel, gemma_bron, args.concept)
    if args.check:
        print(rapport)
        print("Voorwaarden in orde; er is niets geschreven.")
        return 0
    doel = args.uit or args.wiki / (CONCEPT if args.concept else EXPORT)
    doel.parent.mkdir(parents=True, exist_ok=True)
    doel.write_bytes(uit.xml)
    if not args.concept and not args.uit:
        gam_gemeen.schrijf_gegenereerd(args.wiki / RAPPORT, rapport, TOOL)
    print(rapport)
    print(f"Geschreven: {doel}")
    return 0


if __name__ == "__main__":
    # Het rapport bevat pijltjes; de Windows-console (cp1252) kan die niet afdrukken.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
