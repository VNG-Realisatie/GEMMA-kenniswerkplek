"""Relaties tussen elementen: kandidaten uit het GGM en uit de bronanalyses, en de toets aan ArchiMate.

Een relatie staat in de beoordeling van het bronelement (`relaties:` in beoordelingen/begrippen/<id>.yaml); het
render-script zet haar op de pagina, met de inkomende kant op de pagina van het doel. Deze tool doet voorstellen; de AI
kiest, geeft een herkenbare naam en schrijft ze in de beoordeling. tools/beslissen.py toetst elke relatie.

Relatie (`soort`): associatie, associatie (gericht), aggregatie, compositie, specialisatie, toewijzing,
toegang (<handeling> of <verantwoordelijkheid>), triggering, stroom, realisatie, bediening.
Toegang van gedrag tot een object heeft een handeling, toegang van een rol of bedrijfssamenwerking een
verantwoordelijkheid; de vaste namen en het ArchiMate-toegangstype staan in het kennismodel (tools/kennismodel.py),
net als welke relaties tussen de typen in het kennismodel van de wiki staan. Deze tool toetst de geldigheid in
ArchiMate (`archimate_geldig`), aangescherpt met de GEMMA-modelleerafspraken (`toegestaan`).
Grondslag: ggm-exact | ggm-afgeleid | bron. `ggm_relatie`: de GUID's, leeg bij `bron`. `bronnen`: verplicht bij
`bron`, bij `ggm-*` de bronnen die de relatie bevestigen.

Relaties uit de bronnen komen uit de tabel `## Relaties` van de bronanalyses (Van | Werkwoord | Naar | Vindplaats):
de begrippen worden opgelost via de beoordelingen (naam of synoniem), een eigenschap, onderdeel of specialisatie
zonder pagina wordt opgetild naar het genoemde begrip, en de typen van beide kanten plus het werkwoord bepalen de
soort relatie.

Gebruik (vanuit de wikimap, na tools/beslissen.py):
    uv run python tools/relaties.py voorstel <element-id>      # kandidaten als YAML voor `relaties:`
    uv run python tools/relaties.py uit-bronnen [<onderwerp>]  # alle relaties uit de bronanalyses, met wat vervalt
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
import kennismodel  # noqa: E402
from kennismodel import HANDELINGEN, VERANTWOORDELIJKHEDEN, toegangstype  # noqa: E402,F401
from llmwiki import beoordeling, paths  # noqa: E402

WIKI_ROOT = gam_gemeen.WIKI_ROOT

RELATIES = kennismodel.RELATIETYPEN  # Nederlandse relatienaam → ArchiMate-relatie
TOEGANG = tuple(HANDELINGEN) + tuple(VERANTWOORDELIJKHEDEN)
GRONDSLAGEN = ("ggm-exact", "ggm-afgeleid", "bron")
KOLOMMEN = ["Relatie", "Naar", "Naam", "Kardinaliteit", "Grondslag", "GGM-relatie", "Bron"]
BRON_ID_RE = gam_gemeen.BRON_ID_RE

ACTIEF = {"business-actor", "business-role", "business-collaboration", "business-interface"}
MOTIVATIE = {"driver", "goal"}
GEDRAG = {"business-process", "business-function", "business-event", "business-service", "business-interaction"}
PASSIEF = {"business-object", "contract", "representation"}
SAMENGESTELD = {"product"}
GROEPERING = {"grouping"}

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
    ("serving", "samengesteld", "actief"),  # Product → bediening → Klant (kennismodel regel 596)
    ("influence", "motivatie", "motivatie"),
    ("composition", "groepering", "*"), ("aggregation", "groepering", "*"),  # een groepering groepeert elk concept
}
STERKTE = {"composition": 3, "aggregation": 2, "association": 1}
DEEL_GEHEEL_WERKWOORDEN = ("bevat", "bestaat uit", "omvat", "onderdeel van", "deel van", "maakt deel uit van",
                           "heeft als onderdeel", "is samengesteld uit")


def categorie(archimate_type: str) -> str:
    for naam, typen in (("actief", ACTIEF), ("gedrag", GEDRAG), ("passief", PASSIEF), ("samengesteld", SAMENGESTELD),
                        ("motivatie", MOTIVATIE), ("groepering", GROEPERING)):
        if archimate_type in typen:
            return naam
    return "onbekend"


def archimate_geldig(relatie: str, bron_type: str, doel_type: str) -> bool:
    """De relatie is geldig in ArchiMate (de conservatieve deelverzameling in TOEGESTAAN)."""
    if relatie == "specialization":
        return bron_type == doel_type or {bron_type, doel_type} == {"business-object", "contract"}
    cb, cd = categorie(bron_type), categorie(doel_type)
    return any(r == relatie and b in ("*", cb) and d in ("*", cd) for r, b, d in TOEGESTAAN if b != "zelfde")


def toegestaan(relatie: str, bron_type: str, doel_type: str) -> bool:
    """ArchiMate-toets, aangescherpt met de GEMMA-modelleerafspraken; die staan in het kennismodel als weggefilterd.

    Een actor hangt alleen via een rol aan gedrag en objecten; een kanaal is toegewezen aan een dienst en bedient een
    rol; een functie bedient een proces (geen aggregatie); een dienst heeft geen toegang tot een object en krijgt geen
    rol toegewezen.
    """
    if relatie == "specialization":
        return archimate_geldig(relatie, bron_type, doel_type)
    cb, cd = categorie(bron_type), categorie(doel_type)
    if relatie == "assignment" and cb == cd == "actief":
        # Tussen twee partijen alleen: een actor vervult een rol.
        return (bron_type, doel_type) == ("business-actor", "business-role")
    if bron_type == "business-actor" and relatie in ("assignment", "access"):
        return False
    if bron_type == "business-interface":
        return relatie == "association" or (relatie, doel_type) in {
            ("assignment", "business-service"), ("serving", "business-role")}
    if relatie == "assignment" and cb == "actief" and doel_type == "business-service":
        return False
    if relatie in ("aggregation", "composition") and (bron_type, doel_type) == ("business-function", "business-process"):
        return False
    if relatie == "access" and bron_type == "business-service":
        return False
    return archimate_geldig(relatie, bron_type, doel_type)


# --- De elementen: uit de beoordelingen ---


def begrippen(wiki_root: Path = WIKI_ROOT) -> dict[str, dict]:
    """id → beoordeling, voor elke beoordeling die al is afgeleid (tools/beslissen.py)."""
    alle = beoordeling.alle(wiki_root, paths.load_wiki_yaml(wiki_root))
    return {bid: data for bid, (_, data) in alle.items() if (data.get("beslist") or {}).get("uitkomst")}


def _uitkomst(data: dict) -> dict:
    return data["beslist"]["uitkomst"]


def elementen(begrippen_: dict[str, dict]) -> dict[str, dict]:
    """De begrippen die een elementpagina krijgen."""
    return {bid: d for bid, d in begrippen_.items()
            if _uitkomst(d)["soort"] == "element" and d.get("status") != "afgewezen"}


# --- Afleiden uit het GGM (relaties afleiden uit een keten, geen beslissen) ---


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


def ggm_toewijzing(elementen_: dict[str, dict]) -> dict[str, tuple[str, str]]:
    """GGM-GUID → (element-id, hoe): 'eigen', 'duplicaat', 'specialisatie' of 'component'.

    Specialisaties zonder pagina en GGM-componenten worden opgetild naar het element dat ze draagt.
    """
    toewijzing = {}
    for bid, d in elementen_.items():
        ggm = d.get("ggm") or {}
        if ggm.get("guid"):
            toewijzing[ggm["guid"]] = (bid, "eigen")
        for dup in ggm.get("duplicaten", []):
            toewijzing.setdefault(dup["guid"], (bid, "duplicaat"))
        for s in d.get("specialisaties", []):
            if s.get("ggm_guid") and not s.get("element"):
                toewijzing.setdefault(s["ggm_guid"], (bid, "specialisatie"))
        for c in d.get("ggm_componenten", []):
            toewijzing.setdefault(c["guid"], (bid, "component"))
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
    toewijzing = ggm_toewijzing(elementen(begrippen(wiki_root)))
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
TRIGGER_WW = ("leidt tot", "zet in gang", "start", "is aanleiding voor", "wordt gevolgd door")
TRIGGER_OMGEKEERD = ("volgt op", "is het gevolg van")
STROOM_WW = ("levert aan", "geeft door aan", "stuurt naar", "draagt over aan")
VERVULLEN_WW = ("vervult", "treedt op als", "fungeert als", "is aangewezen als", "neemt de rol")
# Werkwoord → handeling (gedrag op een object); de eerste passende handeling in deze volgorde wint.
HANDELING_WW = {
    "vernietigen": ("vernietigt",),
    "overbrengen": ("brengt over",),
    "bewaren": ("bewaart", "archiveert"),
    "beëindigen": ("beëindigt", "trekt in", "heft op", "verklaart vervallen", "doet vervallen"),
    "verstrekken": ("verstrekt", "levert aan", "zendt", "stuurt", "maakt bekend", "publiceert"),
    "bijwerken": ("wijzigt", "actualiseert", "verlengt", "werkt bij", "onderhoudt", "ruimt", "graaft op", "bezorgt",
                  "zet bij", "verstrooit", "schrijft over", "geschiedt in"),
    "registreren": ("levert op", "maakt", "stelt vast", "stelt op", "neemt", "legt vast", "verleent", "weigert",
                    "registreert", "produceert", "genereert", "ontvangt", "leidt tot", "vestigt"),
    "raadplegen": ("vereist", "gebruikt", "raadpleegt", "toetst", "beoordeelt", "controleert", "leest", "bekijkt",
                   "betreft", "begint met", "schouwt", "geschiedt op"),
}
# Werkwoord → verantwoordelijkheid (rol op een object); volgorde: specifiek vóór algemeen.
VERANTWOORDELIJKHEID_WW = {
    "bronhouder": ("houdt bij",),
    "toezichthouder": ("houdt toezicht", "ziet toe"),
    "houder": ("houdt in stand", "houdt", "heeft het uitsluitend recht"),
    "beheerder": ("beheert", "heeft de dagelijkse leiding", "draagt zorg voor", "onderhoudt"),
    "afnemer": ("ontvangt", "gebruikt", "raadpleegt"),
    "partij": ("heeft", "sluit", "legt met"),
}


def _bevat(werkwoord: str, lijst) -> bool:
    return any(w in werkwoord for w in lijst)


def handeling_van(werkwoord: str) -> str:
    for handeling, lijst in HANDELING_WW.items():
        if _bevat(werkwoord, lijst):
            return handeling
    return "bijwerken"


def verantwoordelijkheid_van(werkwoord: str, doel_type: str) -> str | None:
    for naam, lijst in VERANTWOORDELIJKHEID_WW.items():
        if naam == "partij" and doel_type != "contract":
            continue
        if _bevat(werkwoord, lijst):
            return naam
    return None


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
        return handeling_van(ww)

    if _bevat(w, SPECIALISATIE_WW) and toegestaan("specialization", bron_type, doel_type):
        return uit("specialization", "'is een' tussen gelijke typen")
    if _bevat(w, DEEL_GEHEEL_OMGEKEERD):
        return uit("aggregation", "deel-geheel (A is deel van B)", omgedraaid=True)
    if _bevat(w, SAMENSTELLING_WW):
        return uit("composition", "samenstelling")
    if (_bevat(w, DEEL_GEHEEL_WERKWOORDEN) and cb != "gedrag") or (bron_type == "product" and cd in ("gedrag", "passief")):
        return uit("aggregation", "deel-geheel")
    if cb == cd == "actief":
        if _bevat(w, VERVULLEN_WW):
            return uit("assignment", "actor vervult rol")
        if bron_type == "business-interface" and doel_type == "business-role":
            return uit("serving", "kanaal bedient rol")
        return uit("association", f"'{w}' tussen partijen is geen toewijzing; associatie", gericht=True)
    if bron_type == "business-actor" and cd in ("gedrag", "passief"):
        return uit("association", "een actor hangt via een rol aan gedrag en objecten; associatie, rol voorleggen",
                   gericht=True)
    if bron_type == "business-interface" and doel_type == "business-service":
        return uit("assignment", "kanaal ontsluit dienst")
    if cb == "actief" and cd == "gedrag" and doel_type != "business-service":
        return uit("assignment", "partij voert uit")
    if cb == "actief" and cd == "passief":
        naam = verantwoordelijkheid_van(w, doel_type)
        if naam:
            return uit("access", f"verantwoordelijkheid {naam}", toegang=naam)
        return uit("association", f"'{w}' is een handeling van de rol: koppel via het proces (toewijzing)", gericht=True)
    if cb == "gedrag" and cd == "passief" and bron_type not in ("business-event", "business-service"):
        return uit("access", "gedrag gebruikt of maakt een object", toegang=toegang_van(w))
    if cb == "passief" and cd == "gedrag" and doel_type not in ("business-event", "business-service"):
        return uit("access", "object wordt door gedrag gebruikt of gemaakt", omgedraaid=True, toegang=toegang_van(w))
    if _bevat(w, TRIGGER_OMGEKEERD) and cb == cd == "gedrag":
        return uit("triggering", "A volgt op B", omgedraaid=True)
    if cb == cd == "gedrag":
        if bron_type == "business-event" or doel_type == "business-event" or _bevat(w, TRIGGER_WW):
            return uit("triggering", "gebeurtenis of opeenvolging")
        if (bron_type, doel_type) == ("business-function", "business-process"):
            return uit("serving", "functie bedient proces")
        if doel_type == "business-service" and bron_type != "business-service":
            return uit("realization", "gedrag realiseert een dienst")
        if bron_type == "business-service":
            return uit("serving", "dienst bedient gedrag")
        if _bevat(w, STROOM_WW):
            return uit("flow", "overdracht tussen gedrag")
    if bron_type == "business-service" and cd == "actief":
        return uit("serving", "dienst bedient een partij")
    return uit("association", "geen specifiekere relatie herkend", gericht=True)


def bronrelaties(wiki_root: Path = WIKI_ROOT, onderwerp: str | None = None) -> list[dict]:
    """De rijen van `## Relaties` in de bronanalyses: {van, werkwoord, naar, bronnen, vindplaats}."""
    rijen = []
    for pad in gam_gemeen.bronanalyses(wiki_root, onderwerp or "*"):
        for rij in gam_gemeen.tabel(gam_gemeen.sectie(pad.read_text(encoding="utf-8"), "Relaties")):
            if rij.get("Van") and rij.get("Naar"):
                rijen.append({"van": rij["Van"], "werkwoord": rij.get("Werkwoord", ""), "naar": rij["Naar"],
                              "bronnen": [pad.stem], "vindplaats": rij.get("Vindplaats", "")})
    return rijen


def uit_bronnen(rijen: list[dict], begrippen_: dict[str, dict]) -> tuple[list[Kandidaat], list[dict]]:
    """Relaties uit de bronnen ({van, werkwoord, naar, bronnen, vindplaats}) naar ArchiMate.

    Een begrip wordt opgelost via de beoordelingen (naam, synoniem of id). Is het een eigenschap, onderdeel of
    specialisatie zonder pagina, dan wordt de relatie opgetild naar het genoemde begrip; is het geen element (buiten
    scope, geen element, conflict, herkend, afgewezen), dan vervalt de relatie. Geeft (kandidaten, vervallen).
    """
    index: dict[str, str] = {}
    for bid, d in begrippen_.items():
        for naam in [d.get("begrip", ""), *[s["naam"] for s in d.get("synoniemen", [])]]:
            index.setdefault(naam.strip().lower(), bid)
        index.setdefault(bid, bid)

    def los_op(naam: str, diepte: int = 0) -> tuple[tuple[str, str] | None, str]:
        bid = index.get(naam.strip().lower())
        if bid is None:
            return None, f"'{naam}' is geen beoordeeld begrip"
        d = begrippen_[bid]
        u = _uitkomst(d)
        if u["soort"] == "element" and d.get("status") != "afgewezen":
            return (bid, u["archimate_type"]), ""
        if u["soort"] in ("eigenschap", "onderdeel", "specialisatie") and u.get("genoemd_begrip") and diepte < 3:
            doel, reden = los_op(u["genoemd_begrip"], diepte + 1)
            return doel, reden or f"opgetild van '{naam}' naar '{u['genoemd_begrip']}'"
        return None, f"'{naam}' is geen element ({'afgewezen' if d.get('status') == 'afgewezen' else u['soort']})"

    kandidaten: dict[tuple, Kandidaat] = {}
    vervallen = []
    for r in rijen:
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


def als_relatie(k: Kandidaat) -> dict:
    """Een kandidaat in het formaat van `relaties:` in een beoordeling."""
    terug = {v: n for n, v in RELATIES.items()}
    soort = terug[k.relatie]
    if k.relatie == "association" and k.gericht:
        soort += " (gericht)"
    if k.relatie == "access":
        soort += f" ({k.toegang or 'bijwerken'})"
    r = {"soort": soort, "naar": k.doel, "naam": k.naam, "kardinaliteit": k.kardinaliteit, "grondslag": k.grondslag,
         "ggm_relatie": k.ggm_relaties, "bronnen": k.bronnen, "vindplaats": k.vindplaats}
    return {s: w for s, w in r.items() if w not in ("", [], None)}


def yaml_voorstel(element_id: str, kandidaten: list[Kandidaat]) -> str:
    """Uitgaande kandidaten als YAML voor `relaties:`; inkomende als commentaar (die horen bij het andere element)."""
    regels = ["relaties:"]
    for k in kandidaten:
        if k.bron != element_id:
            continue
        uitleg = [x for x in (k.toelichting, k.terugmelding and f"terugmelden: {k.terugmelding}") if x]
        if uitleg:
            regels.append(f"# {'; '.join(uitleg)}")
        regels += ["  " + r for r in beoordeling.dump([als_relatie(k)]).rstrip("\n").split("\n")]
    inkomend = [k for k in kandidaten if k.doel == element_id]
    if inkomend:
        regels.append("# Inkomend (hoort in de beoordeling van het andere element):")
        regels += [f"#   {k.bron} -> {als_relatie(k)['soort']} ({k.naam or 'zonder naam'})" for k in inkomend]
    return "\n".join(regels) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Relaties tussen elementen (zie docstring).")
    p.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("voorstel").add_argument("element")
    sub.add_parser("uit-bronnen").add_argument("onderwerp", nargs="?")
    a = p.parse_args(argv)
    alle = begrippen(a.wiki)

    if a.cmd == "uit-bronnen":
        kandidaten, vervallen = uit_bronnen(bronrelaties(a.wiki, a.onderwerp), alle)
        print(json.dumps({"kandidaten": [{"van": k.bron, **als_relatie(k), "toelichting": k.toelichting} for k in kandidaten],
                          "vervallen": vervallen}, indent=2, ensure_ascii=False))
        return 0
    if a.element not in elementen(alle):
        print(f"'{a.element}' is (nog) geen afgeleid element; draai eerst tools/beslissen.py")
        return 1
    import ggm

    ggm_pad = a.wiki / "ggm" / "ggm_parsed.json"
    kandidaten = voorstel(a.element, ggm.laad(ggm_pad), a.wiki) if ggm_pad.exists() else []
    uit, _ = uit_bronnen(bronrelaties(a.wiki), alle)
    kandidaten = combineer(kandidaten, [k for k in uit if a.element in (k.bron, k.doel)])
    sys.stdout.write(yaml_voorstel(a.element, kandidaten))
    return 0


if __name__ == "__main__":
    sys.exit(main())
