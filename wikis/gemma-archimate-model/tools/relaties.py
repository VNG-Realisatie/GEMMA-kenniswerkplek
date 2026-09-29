"""Relaties tussen elementen: afleiden uit het GGM, toetsen aan ArchiMate, lezen uit de pagina's.

Een relatie staat één keer, als rij in `## Relaties` op de pagina van het bronelement, met een
relatieve link naar het doelelement (Obsidian toont de omgekeerde kant als backlink):

    | Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie | Bron |
    |---|---|---|---|---|---|---|
    | compositie | [Onderdeel beschikking](onderdeel-beschikking.md) | bevat | 1 → 1..* | ggm-exact | EAID_… | 2026-overheid-awb (art. 1:3) |

Relatie: associatie, associatie (gericht), aggregatie, compositie, specialisatie, toewijzing,
toegang (lezen|schrijven|lezen-schrijven), triggering, stroom, realisatie, bediening.
Grondslag: ggm-exact | ggm-afgeleid | bron. GGM-relatie: één of meer GUID's (komma-gescheiden), leeg bij `bron`.
Bron: bron-id's met vindplaats; verplicht bij `bron`, bij `ggm-*` de bronnen die de relatie bevestigen.

Relaties worden samen met de elementen gevonden: de bronanalyse noemt relaties tussen begrippen (werkwoord +
vindplaats), ASSESS neemt ze op bij de voorstellen, en `uit-bronnen` zet ze om naar ArchiMate op basis van de
uitkomst van beide begrippen (optillen of laten vervallen, zoals bij het GGM). `voorstel --bronnen` voegt ze
samen met de kandidaten uit het GGM.

Gebruik (vanuit de wikimap):
    uv run python tools/relaties.py uit-bronnen <assessment.json>        # relaties uit de bronnen, naar ArchiMate
    uv run python tools/relaties.py voorstel <element-id> [--bronnen <assessment.json>] [--markdown]
    uv run python tools/relaties.py inkomend <element-id>                # relaties die naar dit element wijzen
    uv run python tools/relaties.py lees <pagina.md>                     # de relatietabel als JSON
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gam_gemeen  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT

# Nederlandse relatienaam → ArchiMate-relatie
RELATIES = {
    "associatie": "association",
    "aggregatie": "aggregation",
    "compositie": "composition",
    "specialisatie": "specialization",
    "toewijzing": "assignment",
    "toegang": "access",
    "triggering": "triggering",
    "stroom": "flow",
    "realisatie": "realization",
    "bediening": "serving",
}
TOEGANG = ("lezen", "schrijven", "lezen-schrijven")
GRONDSLAGEN = ("ggm-exact", "ggm-afgeleid", "bron")
KOLOMMEN = ["Relatie", "Naar", "Naam", "Kardinaliteit", "Grondslag", "GGM-relatie", "Bron"]
BRON_ID_RE = re.compile(r"\b[0-9]{4}-[a-z0-9]+(?:-[a-z0-9]+)*\b")

ACTIEF = {"business-actor", "business-role", "business-collaboration", "business-interface"}
GEDRAG = {"business-process", "business-function", "business-event", "business-service", "business-interaction"}
PASSIEF = {"business-object", "contract", "representation"}
SAMENGESTELD = {"product"}

# Deelverzameling van de ArchiMate-relatietabel voor de business-laag (conservatief).
# (relatie, categorie bron, categorie doel); 'zelfde' = hetzelfde ArchiMate-type.
TOEGESTAAN = {
    ("association", "*", "*"),
    ("specialization", "zelfde", "zelfde"),
    ("composition", "passief", "passief"), ("aggregation", "passief", "passief"),
    ("composition", "actief", "actief"), ("aggregation", "actief", "actief"),
    ("composition", "gedrag", "gedrag"), ("aggregation", "gedrag", "gedrag"),
    ("composition", "samengesteld", "*"), ("aggregation", "samengesteld", "*"),
    ("assignment", "actief", "actief"), ("assignment", "actief", "gedrag"),
    ("access", "gedrag", "passief"), ("access", "actief", "passief"),
    ("triggering", "gedrag", "gedrag"), ("flow", "gedrag", "gedrag"),
    ("realization", "gedrag", "gedrag"), ("realization", "passief", "passief"),
    ("serving", "gedrag", "gedrag"), ("serving", "gedrag", "actief"),
}
STERKTE = {"composition": 3, "aggregation": 2, "association": 1}
DEEL_GEHEEL_WERKWOORDEN = ("bevat", "bestaat uit", "omvat", "onderdeel van", "deel van", "maakt deel uit van",
                           "heeft als onderdeel", "is samengesteld uit")


def categorie(archimate_type: str) -> str:
    for naam, typen in (("actief", ACTIEF), ("gedrag", GEDRAG), ("passief", PASSIEF), ("samengesteld", SAMENGESTELD)):
        if archimate_type in typen:
            return naam
    return "onbekend"


def toegestaan(relatie: str, bron_type: str, doel_type: str) -> bool:
    if relatie == "specialization":
        return bron_type == doel_type or {bron_type, doel_type} == {"business-object", "contract"}
    cb, cd = categorie(bron_type), categorie(doel_type)
    return any(r == relatie and b in ("*", cb) and d in ("*", cd) for r, b, d in TOEGESTAAN if b != "zelfde")


# --- Relatietabel op een pagina ---


@dataclass
class Relatie:
    relatie: str  # ArchiMate-relatie
    naar: str  # doel-id (of het linkdoel als dat niet te herleiden is)
    naam: str = ""
    kardinaliteit: str = ""
    grondslag: str = ""
    ggm_relaties: list[str] = field(default_factory=list)
    gericht: bool = False
    toegang: str | None = None
    bronnen: list[str] = field(default_factory=list)
    fouten: list[str] = field(default_factory=list)


def lees_tabel(pad: Path, body: str, index_op_pad: dict[Path, str]) -> list[Relatie]:
    result = []
    for rij in gam_gemeen.tabel(gam_gemeen.sectie(body, "Relaties")):
        fouten = []
        label = rij.get("Relatie", "").strip().lower()
        m = re.fullmatch(r"(?P<soort>[a-z]+)(?:\s*\((?P<extra>[a-z-]+)\))?", label)
        soort = m.group("soort") if m else label
        extra = m.group("extra") if m else None
        if soort not in RELATIES:
            fouten.append(f"onbekende relatie '{label}'")
        gericht = soort == "associatie" and extra == "gericht"
        toegang = extra if soort == "toegang" else None
        if soort == "toegang" and toegang not in TOEGANG:
            fouten.append(f"toegang zonder geldige soort ({'/'.join(TOEGANG)})")
        gelinkt = gam_gemeen.link(rij.get("Naar", ""))
        if gelinkt is None:
            fouten.append("kolom 'Naar' bevat geen link")
            naar = rij.get("Naar", "")
        else:
            doelpad = gam_gemeen.doel_van_link(pad, gelinkt[1])
            naar = index_op_pad.get(doelpad, gelinkt[1])
            if doelpad not in index_op_pad:
                fouten.append(f"link '{gelinkt[1]}' wijst niet naar een elementpagina")
        grondslag = rij.get("Grondslag", "").strip()
        if grondslag not in GRONDSLAGEN:
            fouten.append(f"grondslag '{grondslag}' onbekend ({', '.join(GRONDSLAGEN)})")
        ggm = [g.strip() for g in rij.get("GGM-relatie", "").split(",") if g.strip()]
        if grondslag.startswith("ggm") and not ggm:
            fouten.append("grondslag ggm-* zonder GGM-relatie")
        bronnen = BRON_ID_RE.findall(rij.get("Bron", ""))
        if grondslag == "bron" and not bronnen:
            fouten.append("grondslag bron zonder bron-id in kolom 'Bron'")
        result.append(Relatie(RELATIES.get(soort, soort), naar, rij.get("Naam", ""), rij.get("Kardinaliteit", ""),
                              grondslag, ggm, gericht, toegang, bronnen, fouten))
    return result


def index_op_pad(elementen: list) -> dict[Path, str]:
    return {el.pad.resolve(): el.id for el in elementen}


def alle_relaties(wiki_root: Path = WIKI_ROOT) -> dict[str, list[Relatie]]:
    elementen = gam_gemeen.elementen(wiki_root)
    op_pad = index_op_pad(elementen)
    return {el.id: lees_tabel(el.pad, el.body, op_pad) for el in elementen}


def inkomend(element_id: str, wiki_root: Path = WIKI_ROOT) -> list[dict]:
    return [{"van": bron, **asdict(r)} for bron, rels in alle_relaties(wiki_root).items() for r in rels if r.naar == element_id]


# --- Afleiden uit het GGM ---


def _grens(waarde: str) -> int | str | None:
    if waarde == "*":
        return "*"
    return int(waarde) if waarde.isdigit() else None


def _mult(m: str) -> tuple | None:
    m = (m or "").strip()
    if not m:
        return None
    onder, _, boven = m.partition("..")
    boven = boven or onder
    o, b = _grens(onder), _grens(boven)
    return None if o is None or b is None else (o, b)


def samengestelde_multipliciteit(a: str, b: str) -> str:
    """Multipliciteit langs twee schakels: ondergrenzen vermenigvuldigen, bovengrens * zodra één * is."""
    ma, mb = _mult(a), _mult(b)
    if ma is None or mb is None:
        return ""
    onder = ma[0] * mb[0] if "*" not in (ma[0], mb[0]) else "*"
    boven = "*" if "*" in (ma[1], mb[1]) else ma[1] * mb[1]
    return f"{onder}..{boven}"


def is_deel_geheel_naam(naam: str) -> bool:
    n = (naam or "").strip().lower()
    return not n or any(w in n for w in DEEL_GEHEEL_WERKWOORDEN)


def archimate_van_ggm(rel: dict) -> dict:
    """ArchiMate-relatie voor één GGM-relatie: {relatie, bron, doel, gericht, terugmelding}.

    Volgt de mapping in ARCHITECTURE.md (Relaties): specialisatie, compositie/aggregatie alleen bij een
    deel-geheel-naam, anders (gerichte) associatie; een onjuist gebruikte aggregatie is een terugmeldkandidaat.
    """
    import ggm

    soort = rel["uml_type"]
    if soort == "Generalization":
        return {"relatie": "specialization", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": False, "terugmelding": None}
    if rel.get("aggregatie"):
        paar = ggm.geheel_en_deel(rel)
        if paar is None:
            return {"relatie": "association", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": True,
                    "terugmelding": "aggregatie zonder herkenbaar geheel (richting deel-geheel onbekend)"}
        if is_deel_geheel_naam(rel.get("name", "")):
            relatie = "composition" if rel["aggregatie"] == "composite" else "aggregation"
            return {"relatie": relatie, "bron": paar[0], "doel": paar[1], "gericht": False, "terugmelding": None}
        return {"relatie": "association", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": True,
                "terugmelding": f"aggregatie gebruikt voor '{rel.get('name')}': geen deel-geheel-relatie"}
    if soort == "Abstraction":
        if (rel.get("name") or "").strip().lower() in ("is een", "is a"):
            return {"relatie": "specialization", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": False,
                    "terugmelding": "specialisatie gemodelleerd als Abstraction"}
        return {"relatie": "association", "bron": rel["source_id"], "doel": rel["target_id"], "gericht": True,
                "terugmelding": "Abstraction zonder duidelijke betekenis"}
    return {"relatie": "association", "bron": rel["source_id"], "doel": rel["target_id"],
            "gericht": bool((rel.get("name") or "").strip()), "terugmelding": None}


def ggm_toewijzing(elementen: list) -> dict[str, tuple[str, str]]:
    """GGM-GUID → (element-id, hoe): 'eigen', 'duplicaat', 'specialisatie' of 'component'.

    Specialisaties zonder pagina en GGM-componenten worden opgetild naar het element dat ze draagt
    (`## Specialisaties`- en `## GGM-componenten`-tabellen met kolom 'GGM-guid').
    """
    toewijzing = {}
    for el in elementen:
        if el.meta.get("ggm_guid"):
            toewijzing[el.meta["ggm_guid"]] = (el.id, "eigen")
        for dup in el.meta.get("ggm_duplicaat_entiteiten", []) or []:
            toewijzing.setdefault(dup.get("guid"), (el.id, "duplicaat"))
        for kop, hoe in (("Specialisaties", "specialisatie"), ("GGM-componenten", "component")):
            for rij in gam_gemeen.tabel(gam_gemeen.sectie(el.body, kop)):
                guid = rij.get("GGM-guid", "").strip("` ")
                if guid and gam_gemeen.link(rij.get(next(iter(rij)), "")) is None:
                    toewijzing.setdefault(guid, (el.id, hoe))
    return toewijzing


@dataclass
class Kandidaat:
    relatie: str
    bron: str
    doel: str
    naam: str
    kardinaliteit: str
    grondslag: str
    ggm_relaties: list[str]
    gericht: bool = False
    terugmelding: str | None = None
    toelichting: str = ""
    toegang: str | None = None
    bronnen: list[str] = field(default_factory=list)
    vindplaats: str = ""


def _kaart(rel: dict, eind: str) -> str:
    return rel["source_card"] if eind == rel["source_id"] else rel["target_card"]


def voorstel(element_id: str, data: dict, wiki_root: Path = WIKI_ROOT) -> list[Kandidaat]:
    """Kandidaat-relaties uit het GGM voor één element (uitgaand én inkomend), na optillen en ketenen."""
    elementen = gam_gemeen.elementen(wiki_root)
    toewijzing = ggm_toewijzing(elementen)
    eigen_guids = {g for g, (e, _) in toewijzing.items() if e == element_id}
    entiteiten, relaties_ggm = data["entities"], list(data["relations"].values())

    def is_enum(guid: str) -> bool:
        return entiteiten.get(guid, {}).get("uml_type") == "Enumeration"

    kandidaten: dict[tuple, Kandidaat] = {}

    def voeg_toe(k: Kandidaat) -> None:
        if k.bron == k.doel:
            return  # lus na optillen
        sleutel = (k.relatie, k.bron, k.doel)
        if sleutel in kandidaten:  # samenvoegen
            kandidaten[sleutel].ggm_relaties += [g for g in k.ggm_relaties if g not in kandidaten[sleutel].ggm_relaties]
            return
        kandidaten[sleutel] = k

    for rel in relaties_ggm:
        if not ({rel["source_id"], rel["target_id"]} & eigen_guids):
            continue
        hier = rel["source_id"] if rel["source_id"] in eigen_guids else rel["target_id"]
        daar = rel["target_id"] if hier == rel["source_id"] else rel["source_id"]
        if is_enum(daar):
            continue  # typering/waardelijst: eigenschap, geen relatie
        a = archimate_van_ggm(rel)
        opgetild = toewijzing.get(hier, ("", ""))[1] != "eigen"

        if daar in toewijzing:
            ander, hoe = toewijzing[daar]
            if a["relatie"] == "specialization" and (opgetild or hoe != "eigen"):
                continue  # specialisatie wordt niet opgetild of geketend
            bron = element_id if a["bron"] == hier else ander
            doel = ander if bron == element_id else element_id
            voeg_toe(Kandidaat(a["relatie"], bron, doel, rel.get("name", ""),
                               f"{_kaart(rel, a['bron']) or '?'} → {_kaart(rel, a['doel']) or '?'}",
                               "ggm-exact" if not opgetild and hoe == "eigen" else "ggm-afgeleid",
                               [rel["id"]], a["gericht"], a["terugmelding"] if not opgetild and hoe == "eigen" else None,
                               "" if hoe == "eigen" and not opgetild else f"opgetild ({hoe if hoe != 'eigen' else 'eigen zijde'})"))
            continue

        # Keten A–X–B via een niet-opgenomen X (één tussenstap)
        if a["relatie"] == "specialization":
            continue
        for rel2 in relaties_ggm:
            if rel2["id"] == rel["id"] or daar not in (rel2["source_id"], rel2["target_id"]):
                continue
            verder = rel2["target_id"] if rel2["source_id"] == daar else rel2["source_id"]
            if verder not in toewijzing or toewijzing[verder][0] == element_id or is_enum(verder):
                continue
            a2 = archimate_van_ggm(rel2)
            if a2["relatie"] == "specialization":
                continue
            zwakste = min((a["relatie"], a2["relatie"]), key=lambda r: STERKTE.get(r, 1))
            zwakste = zwakste if zwakste in STERKTE else "association"
            kaart_b = samengestelde_multipliciteit(_kaart(rel, daar), _kaart(rel2, verder))
            kaart_a = samengestelde_multipliciteit(_kaart(rel2, daar), _kaart(rel, hier))
            voeg_toe(Kandidaat(zwakste, element_id, toewijzing[verder][0],
                               f"{rel.get('name', '')} / {rel2.get('name', '')}".strip(" /"),
                               f"{kaart_a or '?'} → {kaart_b or '?'}", "ggm-afgeleid", [rel["id"], rel2["id"]],
                               zwakste == "association", None,
                               f"via {entiteiten.get(daar, {}).get('name', daar)} (niet opgenomen)"))
    return sorted(kandidaten.values(), key=lambda k: (k.bron != element_id, k.relatie, k.doel))


# --- Relaties uit de bronnen ---

SPECIALISATIE_WW = ("is een soort", "is een bijzondere vorm van", "is een vorm van", "is een")
DEEL_GEHEEL_OMGEKEERD = ("maakt deel uit van", "is onderdeel van", "onderdeel van", "deel van")
SAMENSTELLING_WW = ("bestaat uit", "is samengesteld uit")
SCHRIJVEN_WW = ("maakt", "stelt vast", "neemt", "legt vast", "wijzigt", "beëindigt", "verleent", "weigert", "trekt in",
                "registreert", "produceert", "levert op", "genereert", "actualiseert")
LEZEN_WW = ("gebruikt", "raadpleegt", "toetst", "beoordeelt", "controleert", "leest", "bekijkt")
TRIGGER_WW = ("leidt tot", "zet in gang", "start", "is aanleiding voor", "wordt gevolgd door")
TRIGGER_OMGEKEERD = ("volgt op", "is het gevolg van")
STROOM_WW = ("levert aan", "geeft door aan", "stuurt naar", "draagt over aan")


def _bevat(werkwoord: str, lijst) -> bool:
    return any(w in werkwoord for w in lijst)


def van_bron(bron_type: str, doel_type: str, werkwoord: str) -> dict:
    """ArchiMate-relatie voor een relatie uit een bron: 'A <werkwoord> B', gegeven de ArchiMate-typen van A en B.

    De typen van de elementen bepalen de relatie (toewijzing, toegang, triggering, realisatie, bediening);
    het werkwoord bepaalt richting, deel-geheel, specialisatie en lezen/schrijven. Wat niet in de ArchiMate-
    tabel past, wordt een gerichte associatie. Uitkomst: {relatie, gericht, toegang, omgedraaid, reden}.
    """
    w = (werkwoord or "").strip().lower()
    cb, cd = categorie(bron_type), categorie(doel_type)

    def uit(relatie, reden, omgedraaid=False, gericht=False, toegang=None):
        b, d = (doel_type, bron_type) if omgedraaid else (bron_type, doel_type)
        if not toegestaan(relatie, b, d):
            return {"relatie": "association", "gericht": True, "toegang": None, "omgedraaid": False,
                    "reden": f"{relatie} past niet tussen {bron_type} en {doel_type}; associatie"}
        return {"relatie": relatie, "gericht": gericht, "toegang": toegang, "omgedraaid": omgedraaid, "reden": reden}

    def toegang_van(ww):
        return "schrijven" if _bevat(ww, SCHRIJVEN_WW) else "lezen" if _bevat(ww, LEZEN_WW) else "lezen-schrijven"

    if _bevat(w, SPECIALISATIE_WW) and toegestaan("specialization", bron_type, doel_type):
        return uit("specialization", "'is een' tussen gelijke typen")
    if _bevat(w, DEEL_GEHEEL_OMGEKEERD):
        return uit("aggregation", "deel-geheel (A is deel van B)", omgedraaid=True)
    if _bevat(w, SAMENSTELLING_WW):
        return uit("composition", "samenstelling")
    if (_bevat(w, DEEL_GEHEEL_WERKWOORDEN) and cb != "gedrag") or (bron_type == "product" and cd in ("gedrag", "passief")):
        return uit("aggregation", "deel-geheel")
    if cb == "actief" and cd in ("actief", "gedrag") and doel_type != "business-interface":
        return uit("assignment", "partij voert uit of vervult")
    if cb == "gedrag" and cd == "passief" and bron_type != "business-event":
        return uit("access", "gedrag gebruikt of maakt een object", toegang=toegang_van(w))
    if cb == "passief" and cd == "gedrag" and doel_type != "business-event":
        return uit("access", "object wordt door gedrag gebruikt of gemaakt", omgedraaid=True, toegang=toegang_van(w))
    if _bevat(w, TRIGGER_OMGEKEERD) and cb == cd == "gedrag":
        return uit("triggering", "A volgt op B", omgedraaid=True)
    if cb == cd == "gedrag":
        if bron_type == "business-event" or doel_type == "business-event" or _bevat(w, TRIGGER_WW):
            return uit("triggering", "gebeurtenis of opeenvolging")
        if doel_type == "business-service" and bron_type != "business-service":
            return uit("realization", "gedrag realiseert een dienst")
        if bron_type == "business-service":
            return uit("serving", "dienst bedient gedrag")
        if _bevat(w, STROOM_WW):
            return uit("flow", "overdracht tussen gedrag")
    if bron_type == "business-service" and cd == "actief":
        return uit("serving", "dienst bedient een partij")
    return uit("association", "geen specifiekere relatie herkend", gericht=True)


def _begrippen_uit_assessment(assessment: dict) -> dict[str, dict]:
    """begrip (kleine letters) → uitkomst + element-id (bestandsnaam van het doel) uit de ASSESS-voorstellen."""
    index = {}
    for v in assessment.get("voorstellen", []):
        b = v.get("beoordeling") or {}
        u = b.get("uitkomst")
        if b.get("begrip") and u:
            index[b["begrip"].strip().lower()] = {**u, "id": Path(v["doel"]).stem if u["soort"] == "element" else None}
    return index


def uit_bronnen(assessment: dict, wiki_root: Path = WIKI_ROOT) -> tuple[list[Kandidaat], list[dict]]:
    """Relaties uit `voorstellen[*].relaties` ({van, werkwoord, naar, bronnen, vindplaats}) naar ArchiMate.

    Een begrip wordt opgelost via de uitkomst van de beslistabel (ASSESS) of een bestaand element (naam of id).
    Is een begrip een eigenschap of specialisatie zonder pagina, dan wordt de relatie opgetild naar het genoemde
    begrip; is het geen element (buiten scope, geen element, conflict, herkend), dan vervalt de relatie.
    Geeft (kandidaten, vervallen).
    """
    begrippen = _begrippen_uit_assessment(assessment)
    bestaand = {}
    for el in gam_gemeen.elementen(wiki_root):
        bestaand[el.id] = bestaand[str(el.meta.get("naam", "")).lower()] = (el.id, el.meta.get("archimate_type", ""))

    def los_op(naam: str, diepte: int = 0) -> tuple[tuple[str, str] | None, str]:
        sleutel = naam.strip().lower()
        u = begrippen.get(sleutel)
        if u is None:
            gevonden = bestaand.get(sleutel) or bestaand.get(naam.strip())
            return (gevonden, "") if gevonden else (None, f"'{naam}' is geen beoordeeld begrip of bestaand element")
        if u["soort"] == "element":
            return (u["id"], u["archimate_type"]), ""
        if u["soort"] == "eigenschap" and u.get("genoemd_begrip") and diepte < 3:
            doel, reden = los_op(u["genoemd_begrip"], diepte + 1)
            return doel, reden or f"opgetild van '{naam}' naar '{u['genoemd_begrip']}'"
        return None, f"'{naam}' is geen element ({u['soort']})"

    kandidaten: dict[tuple, Kandidaat] = {}
    vervallen = []
    for v in assessment.get("voorstellen", []):
        for r in v.get("relaties", []) or []:
            (van, reden_van), (naar, reden_naar) = los_op(r["van"]), los_op(r["naar"])
            if van is None or naar is None:
                vervallen.append({**r, "reden": "; ".join(x for x in (reden_van, reden_naar) if x and "opgetild" not in x)})
                continue
            a = van_bron(van[1], naar[1], r.get("werkwoord", ""))
            bron, doel = (naar[0], van[0]) if a["omgedraaid"] else (van[0], naar[0])
            if bron == doel:
                vervallen.append({**r, "reden": "lus na optillen"})
                continue
            sleutel = (a["relatie"], bron, doel)
            toelichting = "; ".join(x for x in (reden_van, reden_naar, a["reden"]) if x)
            if sleutel in kandidaten:
                k = kandidaten[sleutel]
                k.bronnen += [b for b in r.get("bronnen", []) if b not in k.bronnen]
                continue
            kandidaten[sleutel] = Kandidaat(a["relatie"], bron, doel, r.get("werkwoord", ""), "", "bron", [],
                                            a["gericht"], None, toelichting, a["toegang"], list(r.get("bronnen", [])),
                                            r.get("vindplaats", ""))
    return list(kandidaten.values()), vervallen


def combineer(ggm_kandidaten: list[Kandidaat], bron_kandidaten: list[Kandidaat]) -> list[Kandidaat]:
    """Een bronrelatie tussen dezelfde elementen als een GGM-kandidaat bevestigt die (bron-id's erbij);
    anders komt ze erbij met grondslag `bron`. Wijkt het relatietype af, dan staat dat in de toelichting."""
    result = list(ggm_kandidaten)
    for b in bron_kandidaten:
        gelijk = [g for g in result if g.grondslag != "bron" and {g.bron, g.doel} == {b.bron, b.doel}]
        if not gelijk:
            result.append(b)
            continue
        for g in gelijk:
            g.bronnen += [x for x in b.bronnen if x not in g.bronnen]
            g.vindplaats = g.vindplaats or b.vindplaats
            if g.relatie != b.relatie:
                g.toelichting = "; ".join(x for x in (g.toelichting, f"bron noemt {b.relatie} ('{b.naam}')") if x)
    return result


def markdown_rijen(element_id: str, kandidaten: list[Kandidaat], wiki_root: Path = WIKI_ROOT) -> str:
    index = gam_gemeen.element_index(wiki_root)
    terug = {v: k for k, v in RELATIES.items()}
    van = index[element_id].pad
    regels = ["| " + " | ".join(KOLOMMEN) + " |", "|" + "---|" * len(KOLOMMEN)]
    for k in kandidaten:
        if k.bron != element_id:
            continue
        doel = index.get(k.doel)
        naar = f"[{doel.meta.get('naam', k.doel)}]({gam_gemeen.relatief(van, doel.pad)})" if doel else k.doel
        label = terug[k.relatie] + (" (gericht)" if k.gericht and k.relatie == "association" else "")
        if k.relatie == "access":
            label += f" ({k.toegang or 'lezen-schrijven'})"
        bron = ", ".join(k.bronnen) + (f" ({k.vindplaats})" if k.vindplaats else "")
        regels.append(f"| {label} | {naar} | {k.naam} | {k.kardinaliteit} | {k.grondslag} | {', '.join(k.ggm_relaties)} | {bron} |")
    return "\n".join(regels) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Relaties tussen elementen (zie docstring).")
    sub = p.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("voorstel")
    v.add_argument("element")
    v.add_argument("--bronnen", help="assessment.json: voeg de relaties uit de bronnen toe")
    v.add_argument("--markdown", action="store_true", help="Alleen uitgaande relaties, als tabelrijen voor ## Relaties")
    sub.add_parser("uit-bronnen").add_argument("assessment")
    sub.add_parser("inkomend").add_argument("element")
    sub.add_parser("lees").add_argument("pagina")
    a = p.parse_args(argv)

    if a.cmd == "uit-bronnen":
        kandidaten, vervallen = uit_bronnen(json.loads(Path(a.assessment).read_text(encoding="utf-8")))
        print(json.dumps({"kandidaten": [asdict(k) for k in kandidaten], "vervallen": vervallen}, indent=2, ensure_ascii=False))
        return 0
    if a.cmd == "voorstel":
        import ggm

        kandidaten = voorstel(a.element, ggm.laad()) if ggm.PARSED.exists() else []
        if a.bronnen:
            uit, _ = uit_bronnen(json.loads(Path(a.bronnen).read_text(encoding="utf-8")))
            kandidaten = combineer(kandidaten, [k for k in uit if a.element in (k.bron, k.doel)])
        if a.markdown:
            sys.stdout.write(markdown_rijen(a.element, kandidaten))
        else:
            print(json.dumps([asdict(k) for k in kandidaten], indent=2, ensure_ascii=False))
        return 0
    if a.cmd == "inkomend":
        print(json.dumps(inkomend(a.element), indent=2, ensure_ascii=False))
        return 0
    from llmwiki import frontmatter

    pad = Path(a.pagina).resolve()
    rels = lees_tabel(pad, frontmatter.read(pad).body, index_op_pad(gam_gemeen.elementen()))
    print(json.dumps([asdict(r) for r in rels], indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
