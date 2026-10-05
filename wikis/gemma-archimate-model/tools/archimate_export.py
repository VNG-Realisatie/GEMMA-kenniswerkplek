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
een aggregatie tussen processen heeft `indeling` en `procesniveau` ("taak → bedrijfsproces"), een aggregatie tussen
functies, en van een functie naar een product of dienst, `indeling`; een functie hangt alleen op domeinniveau (GEMMA type
*Bedrijfsfunctie domein*) aan de domeingroepering, daaronder aan haar bovenliggende functie; een product of dienst aan een functie; een proces zonder GEMMA-match
staat in de map `Procesindeling naar taak`; `gemma_generiek` wordt een specialisatie naar het GEMMA-element (dat
letterlijk meegaat); beleidsdomein en domein worden een aggregatie vanuit de bestaande GEMMA-groepering, of vanuit een
nieuwe groepering in de map van de wiki; doelgroep een aggregatie vanuit de GEMMA-rol van de doelgroep (GEMMA type `Groep`).

Een element dat in geen enkele indeling staat, houdt de export tegen (`--check` meldt het ook).

Alleen begrippen met status `goedgekeurd` (akkoord van de redacteur); `--concept` neemt ook kandidaat en review mee,
voor het bekijken, en schrijft naar het kladblok. Het GEMMA-model moet als Archi-bestand zijn ingelezen
(tools/gemma.py release <bestand.archimate>): de AMEFF heeft geen map-id's.

Gebruik (vanuit de wikimap):
    uv run python tools/archimate_export.py [--concept] [--uit <pad>]
    uv run python tools/archimate_export.py --check        # alleen de voorwaarden controleren
"""
from __future__ import annotations

import argparse
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
             paren: list[tuple[str, str]], naam: str = "") -> None:
    """Een relatie met het id van de GEMMA-relatie van hetzelfde type tussen dezelfde elementen, anders een vast id."""
    bestaand = sorted(gemma_relaties.get((rtype, bron, doel), []), key=lambda x: x["id"])
    g = bestaand[0] if bestaand else None
    rid = g["id"] if g else vast_id("relatie", herkomst, rtype, bron, doel)
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


def bouw(gemma_data: dict, begrippen: dict[str, dict], gemma_bron: str, tijdstempel: str, concept: bool = False,
         log: str = "", wiki_yaml: dict | None = None) -> Uitkomst:
    uit = Uitkomst()
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
        eid = gemma_id or vast_id("element", bid)
        ids[bid] = eid
        el = ET.Element("element", {XSI: xsi_type(atype), "name": data["begrip"], "id": eid})
        if g is not None and g.get("profiel"):
            el.set("profiles", g["profiel"])
            b.profielen.update(g["profiel"].split())
        if data.get("definitie"):
            ET.SubElement(el, "documentation").text = data["definitie"]
        paren = _gemma_eigen(g["eigenschappen"]) if g is not None else []
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
                map_naam = "Procesindeling naar taak"
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
            rid = g["id"] if g else vast_id("relatie", bid, r["soort"], r["naar"], r.get("naam", ""))
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
                paren += [(eig("indeling"), "Procesindeling naar taak"),
                          (eig("procesniveau"), f"{bron_u.get('procesniveau')} → {doel_u.get('procesniveau')}")]
            if rtype == "aggregation-relationship" and bron_u.get("paginatype") == "bedrijfsproces" \
                    and doel_u.get("paginatype") == "gebeurtenis":
                paren.append((eig("indeling"), "Procesindeling naar taak"))
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

    _gemma_specialisaties(b, uit, gemma_data, gekozen, ids, gemma_relaties)
    _indelingen(b, uit, gemma_data, gekozen, ids, gemma_relaties)
    uit.zonder_plaats = _zonder_plaats(b, gekozen, ids)
    uit.xml = _serialiseer(b, gemma_bron)
    return uit


def _gemma_specialisaties(b: Bouwer, uit: Uitkomst, gemma_data: dict, gekozen: dict, ids: dict, gemma_relaties: dict) -> None:
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
                 [(eig("indeling"), indeling), (eig("onderbouwing"), generiek.get("onderbouwing", ""))])
        uit.specialisaties.append(f"{data['begrip']} → {g['naam']}")


# De indelingen die een element in een bestaande GEMMA-groepering plaatsen: paginatype → (indeling, soort).
BELEIDSDOMEIN_TYPEN = ("bedrijfsobject", "product", "dienst", "beleidskader")
DOMEIN_TYPEN = ("bedrijfsfunctie", "product", "dienst")
# Een taak (procescluster) valt ook in de Beleidsdomeinindeling: boven haar staat in de Procesindeling naar taak niets.
DOELGROEP_TYPEN = ("actor", "rol", "bedrijfssamenwerking", "kanaal")


def _indelingen(b: Bouwer, uit: Uitkomst, gemma_data: dict, gekozen: dict, ids: dict, gemma_relaties: dict) -> None:
    """Aggregaties vanuit de GEMMA-groepering van de Beleidsdomeinindeling en de Functie-indeling naar domein, en vanuit
    de GEMMA-rol van de Doelgroepindeling; een beleidsdomein dat GEMMA niet kent wordt een nieuwe groepering onder het
    taakveld."""
    nieuwe: dict[str, str] = {}

    def aggregatie(groep_id: str, element: str, indeling: str, bid: str, gemma_groep: dict | None = None) -> None:
        if gemma_groep is not None and groep_id not in ids.values():
            _stub(b, gemma_groep)
        _relatie(b, uit, gemma_relaties, "aggregation-relationship", groep_id, element, f"{bid}#{indeling}",
                 [(eig("indeling"), indeling)])
        uit.indelingen += 1

    for bid, data in sorted(gekozen.items()):
        if bid not in ids:
            continue
        paginatype = data["afgeleid"]["uitkomst"].get("paginatype")
        element = ids[bid]
        beleidsdomein = data.get("beleidsdomein")
        taak = paginatype == "bedrijfsproces" and data["afgeleid"]["uitkomst"].get("procesniveau") == "taak"
        if (paginatype in BELEIDSDOMEIN_TYPEN or taak) and beleidsdomein:
            groep = _vind_groepering(gemma_data, "Beleidsdomein", beleidsdomein)
            if groep is None:
                if beleidsdomein not in nieuwe:
                    gid = vast_id("groepering", "beleidsdomein", beleidsdomein)
                    nieuwe[beleidsdomein] = gid
                    taakveld = data.get("taakveld")
                    el = ET.Element("element", {XSI: "archimate:Grouping", "name": beleidsdomein, "id": gid})
                    _eigenschappen(el, [("GEMMA type", "Beleidsdomein"), (eig("id"), f"beleidsdomein:{beleidsdomein}"),
                                        *b.gemeen("nieuw"), (eig("taakveld"), taakveld or "")])
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



def _alle_objecten(m: Map):
    yield from m.objecten
    for kind in m.mappen.values():
        yield from _alle_objecten(kind)


def _indeling_van(obj: ET.Element) -> str | None:
    return next((p.get("value") for p in obj.findall("property") if p.get("key") == eig("indeling")), None)


def _zonder_plaats(b: Bouwer, gekozen: dict, ids: dict) -> list[str]:
    """De elementen die in geen enkele indeling staan (besluit 2026-10-04: alles wordt ingedeeld, geen wezen). Een
    element staat in een indeling als een aggregatie met een indeling naar haar wijst of als zij een specialisatie met een
    indeling heeft. Een taak staat in de Beleidsdomeinindeling (besluit 2026-10-04)."""
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
    uit = Uitkomst() if fouten else bouw(gemma_data, begrippen, gemma_bron, tijdstempel, args.concept, log, wiki_yaml)
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
    sys.exit(main())
