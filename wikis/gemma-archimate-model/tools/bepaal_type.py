"""Bepaal het ArchiMate-elementtype van een begrip uit zijn kenmerken.

Eén bron van waarheid voor de criteria van deze wiki:
- KENMERKEN: de neutrale eigenschappen die het model per begrip één keer beantwoordt (ja/nee);
- REGELS: de beslistabel (= de criteria), van boven naar beneden, de eerste passende regel beslist;
- NAREGELS: aanvullingen op de uitkomst (voorleggen, tegenhanger, annotatie).

Het model vult de kenmerken in (met onderbouwing en bron-id's); deze tool past de regels toe.
De tabellen in skill `gemma-archimate-model-criteria` en `schemas/beoordeling.schema.json`
worden hieruit gegenereerd (`--markdown`, `--schema`); een test bewaakt dat ze gelijk blijven.

Gebruik (vanuit de wikimap):
    uv run python tools/bepaal_type.py evalueer <assessment.json | beoordeling.json>
    uv run python tools/bepaal_type.py status --uitkomst <uitkomst.json> [--ggm-match sterk] [--grondslag ggm-entiteit]
    uv run python tools/bepaal_type.py markdown      # tabellen voor de criteria-skill
    uv run python tools/bepaal_type.py schema        # schemas/beoordeling.schema.json
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable

WIKI_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = WIKI_ROOT / "schemas" / "beoordeling.schema.json"


@dataclass(frozen=True)
class Kenmerk:
    sleutel: str
    naam: str
    groep: str
    vraag: str
    herkomst: str
    voorbeeld: str
    tegenvoorbeeld: str


KENMERKEN: list[Kenmerk] = [
    # Scope
    Kenmerk("herkenbaar", "herkenbaar", "Scope",
            "Kennen domeinexperts dit als eigen begrip binnen het onderwerp?",
            "ArchiMate (concept in een domein) + GEMMA",
            "Omgevingsvergunning", "Technisch volgnummer van een dossierregel"),
    Kenmerk("gemeentelijk", "gemeentelijk", "Scope",
            "Ziet, doet of beslist de gemeente hierover, of werkt zij rechtstreeks samen met deze partij?",
            "GEMMA",
            "Parkeervergunning; GGD (directe samenwerking)", "Interne werkvoorraad van het UWV"),
    Kenmerk("buiten_kernlagen", "buiten kernlagen", "Scope",
            "Is het een thema, doel, waarde, drijfveer, principe, losse norm of eis, of een vermogen? Noem welk ArchiMate-type",
            "ArchiMate (motivatie-, strategie- en overige lagen)",
            "Armoedebestrijding (doel); leefbaarheid (waarde); 'binnen 8 weken beslissen' (norm)", "Bijstandsuitkering"),
    # Afhankelijkheid
    Kenmerk("slechts_eigenschap", "slechts eigenschap", "Afhankelijkheid",
            "Is het alleen een eigenschap, status, waarde of indeling van één ander begrip? Noem dat begrip",
            "GEMMA",
            "Bouwjaar (van Pand); status van een aanvraag", "Pand"),
    # Aard
    Kenmerk("gedrag", "gedrag", "Aard",
            "Beschrijft het iets wat gedaan wordt of gebeurt, en niet een ding, partij of plaats?",
            "ArchiMate (gedragselement)",
            "Aanvraag behandelen; verhuizing", "Aanvraag"),
    Kenmerk("handelende_partij", "handelende partij", "Aard",
            "Is het een persoon, organisatie of organisatie-eenheid (ook extern of generiek) die zelf kan handelen?",
            "ArchiMate Business Actor",
            "College van B&W; inwoner; woningcorporatie", "Aanvrager"),
    Kenmerk("hoedanigheid", "hoedanigheid", "Aard",
            "Is het een verantwoordelijkheid waaraan een partij wordt toegewezen, of de hoedanigheid waarin een partij optreedt in een handeling of gebeurtenis?",
            "ArchiMate Business Role",
            "Aanvrager; belastingplichtige; heffingsambtenaar", "Gemeenteraad"),
    Kenmerk("samenwerkingsverband", "samenwerkingsverband", "Aard",
            "Is het een verband van twee of meer partijen dat samen gedrag uitvoert?",
            "ArchiMate Business Collaboration",
            "Zorg- en Veiligheidshuis; samenwerkingsverband passend onderwijs", "GGD"),
    Kenmerk("toegangspunt", "toegangspunt", "Aard",
            "Is het een punt waarlangs een dienst beschikbaar komt (loket, website, telefoonnummer, kanaal)?",
            "ArchiMate Business Interface",
            "Publieksbalie; gemeentelijke website", "Klantcontact"),
    Kenmerk("plaats", "plaats", "Aard",
            "Is het een fysieke plaats als zodanig, en niet een gebiedsindeling als gegevensconcept?",
            "ArchiMate Location",
            "Stadskantoor als vestigingsplaats", "Wijk (gebiedsindeling)"),
    Kenmerk("aanbod_als_geheel", "aanbod als geheel", "Aard",
            "Is het een samenhangend pakket van diensten en/of objecten dat met voorwaarden als geheel aan afnemers wordt aangeboden?",
            "ArchiMate Product",
            "Bewonersparkeervergunning zoals aangeboden in de productencatalogus", "Parkeren"),
    # Soort gedrag
    Kenmerk("per_keer_doorlopen", "per keer doorlopen", "Soort gedrag",
            "Is het een reeks activiteiten die per keer wordt doorlopen en een benoembaar resultaat oplevert?",
            "ArchiMate Business Process",
            "Aanvraag omgevingsvergunning behandelen", "Vergunningverlening"),
    Kenmerk("gegroepeerd_gedrag", "gegroepeerd gedrag", "Soort gedrag",
            "Is het een doorlopende groepering van gedrag, ingedeeld naar benodigde kennis of middelen, zonder eigen volgorde of doorlooptijd? (Niet: 'wat de gemeente kan'; dat is een vermogen)",
            "ArchiMate Business Function",
            "Vergunningverlening; belastingheffing", "Aanslag opleggen"),
    Kenmerk("toestandsverandering", "toestandsverandering", "Soort gedrag",
            "Is het een ogenblikkelijke toestandsverandering die gedrag start of afsluit, van binnen of buiten de gemeente?",
            "ArchiMate Business Event",
            "Verhuizing; aanvraag ontvangen; beslistermijn verstreken", "Verhuizing doorgeven"),
    Kenmerk("aangeboden_gedrag", "aangeboden gedrag", "Soort gedrag",
            "Is het expliciet beschreven gedrag dat aan de omgeving wordt aangeboden, vanuit de waarde voor de afnemer en los van hoe het wordt uitgevoerd?",
            "ArchiMate Business Service",
            "Melding openbare ruimte doen", "Melding afhandelen"),
    Kenmerk("gezamenlijk_gedrag", "gezamenlijk gedrag", "Soort gedrag",
            "Is het gedrag dat alleen door twee of meer partijen samen wordt uitgevoerd?",
            "ArchiMate Business Interaction",
            "Keukentafelgesprek; hoorzitting bezwaarcommissie", "Beschikking opstellen"),
    # Passief
    Kenmerk("eigen_identiteit", "eigen identiteit", "Passief",
            "Bestaat het zelfstandig, niet alleen als onderdeel van één ander ding?",
            "GEMMA",
            "Beschikking", "Ondertekening van een besluit"),
    Kenmerk("onderscheidbare_exemplaren", "onderscheidbare exemplaren", "Passief",
            "Zijn de afzonderlijke exemplaren van elkaar te onderscheiden?",
            "GEMMA",
            "Aanvraag (elke aanvraag apart)", "Gemeentefonds (er is er één)"),
    Kenmerk("levenscyclus", "levenscyclus", "Passief",
            "Ontstaan, veranderen en eindigen de exemplaren?",
            "GEMMA",
            "Vergunning (verleend, gewijzigd, ingetrokken)", "Kadastrale gemeentecode"),
    Kenmerk("wordt_bewerkt", "wordt bewerkt", "Passief",
            "Wordt het door gemeentelijk gedrag gebruikt, gemaakt of gewijzigd (behandeld, besloten, geleverd)?",
            "ArchiMate (access-relatie)",
            "Aanvraag (ontvangen, beoordeeld)", "Begrip dat in geen enkel gemeentelijk gedrag voorkomt"),
    Kenmerk("afspraak", "afspraak", "Passief",
            "Is het een tweezijdige afspraak met rechten en plichten, en geen eenzijdig besluit of regeling?",
            "ArchiMate Contract",
            "Subsidieovereenkomst; convenant", "Subsidiebeschikking (eenzijdig); verordening"),
    Kenmerk("waarneembare_vorm", "waarneembare vorm", "Passief",
            "Is het de vorm (document, formulier, bericht) waarin informatie van een ander begrip wordt overgebracht? Noem dat begrip",
            "ArchiMate Representation",
            "Aanslagbiljet (vorm van Aanslag); aanvraagformulier", "Aanslag"),
    Kenmerk("geautomatiseerd_verwerkt", "geautomatiseerd verwerkt", "Passief",
            "Is het een gegevensstructuur voor geautomatiseerde verwerking?",
            "ArchiMate Data Object (applicatielaag)",
            "Zaak in het zaaksysteem", "Keukentafelgesprek"),
]

SLEUTELS = [k.sleutel for k in KENMERKEN]
NAAM = {k.sleutel: k.naam for k in KENMERKEN}

AARD = ["gedrag", "handelende_partij", "hoedanigheid", "samenwerkingsverband", "toegangspunt", "plaats", "aanbod_als_geheel"]
GEDRAGSSOORTEN = {
    "per_keer_doorlopen": ("bedrijfsproces", "business-process"),
    "gegroepeerd_gedrag": ("bedrijfsfunctie", "business-function"),
    "toestandsverandering": ("bedrijfsgebeurtenis", "business-event"),
    "aangeboden_gedrag": ("bedrijfsdienst", "business-service"),
    "gezamenlijk_gedrag": (None, "business-interaction"),  # herkend, nog geen paginatype
}
PASSIEF_VERPLICHT = ["eigen_identiteit", "onderscheidbare_exemplaren", "wordt_bewerkt"]

# Extra velden in een beoordeling (geen kenmerken): nodig bij bepaalde uitkomsten.
EXTRA_VELDEN = {
    "genoemd_begrip": "Het begrip waarvan dit een eigenschap of waarneembare vorm is",
    "archimate_buiten_model": "Het ArchiMate-type buiten de kernlagen (Goal, Outcome, Driver, Principle, Requirement, Constraint, Value, Capability, Grouping …)",
    "benoemde_partij": "ja/nee: bij 'handelende partij' én 'hoedanigheid': is het een benoemde persoon, organisatie of eenheid?",
}


@dataclass
class Uitkomst:
    soort: str  # element | herkend | buiten_scope | buiten_model | eigenschap | geen_element | conflict
    regel: int
    toelichting: str
    paginatype: str | None = None
    archimate_type: str | None = None
    voorleggen: bool = False
    redenen: list[str] = field(default_factory=list)
    tegenhanger: str | None = None
    data_object: str = "nee"
    genoemd_begrip: str | None = None


def _ja(k: dict, sleutel: str) -> bool:
    return k[sleutel] == "ja"


def _aard(k: dict) -> set[str]:
    return {s for s in AARD if _ja(k, s)}


def _gedragssoorten(k: dict) -> list[str]:
    return [s for s in GEDRAGSSOORTEN if _ja(k, s)]


def _namen(sleutels) -> str:
    return ", ".join(f"*{NAAM[s]}*" for s in sleutels)


@dataclass(frozen=True)
class Regel:
    stap: str
    als: str
    dan: str
    test: Callable[[dict, dict], bool]
    uitkomst: Callable[[dict, dict], Uitkomst]


def _element(nr, paginatype, archimate_type, toelichting, **kw) -> Uitkomst:
    return Uitkomst("element", nr, toelichting, paginatype=paginatype, archimate_type=archimate_type, **kw)


def _herkend(nr, archimate_type, toelichting, **kw) -> Uitkomst:
    return Uitkomst("herkend", nr, toelichting, archimate_type=archimate_type, voorleggen=True,
                    redenen=[f"{archimate_type} heeft in deze wiki nog geen paginatype"], **kw)


def _conflict(nr, reden) -> Uitkomst:
    return Uitkomst("conflict", nr, "Tegenstrijdige kenmerken", voorleggen=True, redenen=[reden])


def _gedrag_uitkomst(k: dict, extra: dict) -> Uitkomst:
    (soort,) = _gedragssoorten(k)
    paginatype, archimate_type = GEDRAGSSOORTEN[soort]
    if paginatype is None:
        return _herkend(12, archimate_type, f"Gedrag, {_namen([soort])}")
    return _element(12, paginatype, archimate_type, f"Gedrag, {_namen([soort])}")


def _passief_ontbrekend(k: dict) -> list[str]:
    return [s for s in PASSIEF_VERPLICHT if not _ja(k, s)]


REGELS: list[Regel] = [
    Regel("1 Scope", "niet *herkenbaar* of niet *gemeentelijk*", "buiten scope, met reden",
          lambda k, e: not (_ja(k, "herkenbaar") and _ja(k, "gemeentelijk")),
          lambda k, e: Uitkomst("buiten_scope", 1, "Niet herkenbaar of niet gemeentelijk",
                                redenen=[f"{NAAM[s]}: nee" for s in ("herkenbaar", "gemeentelijk") if not _ja(k, s)])),
    Regel("1 Scope", "*buiten kernlagen*", "buiten dit model, met het ArchiMate-type (Goal, Driver, Capability …)",
          lambda k, e: _ja(k, "buiten_kernlagen"),
          lambda k, e: Uitkomst("buiten_model", 2, "Buiten de kernlagen van dit model",
                                archimate_type=e.get("archimate_buiten_model"))),
    Regel("2 Afhankelijk", "*slechts eigenschap*", "eigenschap of specialisatie zonder pagina van het genoemde begrip",
          lambda k, e: _ja(k, "slechts_eigenschap"),
          lambda k, e: Uitkomst("eigenschap", 3, "Eigenschap of specialisatie zonder eigen pagina",
                                genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("3 Aard", "*handelende partij* én *hoedanigheid* (verder geen aard)",
          "Actor als het een benoemde persoon/organisatie/eenheid is, anders Rol",
          lambda k, e: _aard(k) == {"handelende_partij", "hoedanigheid"},
          lambda k, e: _element(4, "actor", "business-actor", "Benoemde partij")
          if e.get("benoemde_partij") == "ja" else _element(4, "rol", "business-role", "Hoedanigheid, geen benoemde partij")),
    Regel("3 Aard", "meer dan één aard (behalve actor + rol)", "conflict: voorleggen",
          lambda k, e: len(_aard(k)) > 1,
          lambda k, e: _conflict(5, f"Meer dan één aard: {_namen(sorted(_aard(k)))}")),
    Regel("3 Aard", "*handelende partij*", "Business Actor",
          lambda k, e: _aard(k) == {"handelende_partij"},
          lambda k, e: _element(6, "actor", "business-actor", "Handelende partij")),
    Regel("3 Aard", "*hoedanigheid*", "Business Role",
          lambda k, e: _aard(k) == {"hoedanigheid"},
          lambda k, e: _element(7, "rol", "business-role", "Hoedanigheid")),
    Regel("3 Aard", "*aanbod als geheel*", "Product",
          lambda k, e: _aard(k) == {"aanbod_als_geheel"},
          lambda k, e: _element(8, "product", "product", "Aanbod als geheel")),
    Regel("3 Aard", "*samenwerkingsverband*", "Business Collaboration: herkend, voorleggen",
          lambda k, e: _aard(k) == {"samenwerkingsverband"},
          lambda k, e: _herkend(9, "business-collaboration", "Samenwerkingsverband")),
    Regel("3 Aard", "*toegangspunt*", "Business Interface: herkend, voorleggen",
          lambda k, e: _aard(k) == {"toegangspunt"},
          lambda k, e: _herkend(10, "business-interface", "Toegangspunt")),
    Regel("3 Aard", "*plaats*", "Location: herkend, voorleggen",
          lambda k, e: _aard(k) == {"plaats"},
          lambda k, e: _herkend(11, "location", "Plaats")),
    Regel("4 Gedrag", "*gedrag* en precies één van *per keer doorlopen* / *gegroepeerd gedrag* / "
          "*toestandsverandering* / *aangeboden gedrag* / *gezamenlijk gedrag*",
          "Business Process / Function / Event / Service / Interaction (Interaction: herkend, voorleggen)",
          lambda k, e: _aard(k) == {"gedrag"} and len(_gedragssoorten(k)) == 1,
          _gedrag_uitkomst),
    Regel("4 Gedrag", "*gedrag*, maar geen of meer dan één soort gedrag", "conflict: voorleggen",
          lambda k, e: _aard(k) == {"gedrag"},
          lambda k, e: _conflict(13, f"Soort gedrag niet eenduidig: {_namen(_gedragssoorten(k)) or 'geen'}")),
    Regel("5 Passief", "geen aard, maar wel een soort gedrag", "conflict: voorleggen (tegenstrijdige antwoorden)",
          lambda k, e: bool(_gedragssoorten(k)),
          lambda k, e: _conflict(14, f"Geen gedrag, maar wel {_namen(_gedragssoorten(k))}")),
    Regel("5 Passief", "*waarneembare vorm*", "Representation van het genoemde begrip: herkend, voorleggen",
          lambda k, e: _ja(k, "waarneembare_vorm"),
          lambda k, e: _herkend(15, "representation", "Waarneembare vorm", genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("5 Passief", "*eigen identiteit* + *onderscheidbare exemplaren* + *wordt bewerkt* + *afspraak*", "Contract",
          lambda k, e: not _passief_ontbrekend(k) and _ja(k, "afspraak"),
          lambda k, e: _element(16, "bedrijfsobject", "contract", "Passief, afspraak")),
    Regel("5 Passief", "*eigen identiteit* + *onderscheidbare exemplaren* + *wordt bewerkt*",
          "Business Object (een wet of verordening als geheel: grondslag governance-object)",
          lambda k, e: not _passief_ontbrekend(k),
          lambda k, e: _element(17, "bedrijfsobject", "business-object", "Passief")),
    Regel("5 Passief", "één van *eigen identiteit*, *onderscheidbare exemplaren*, *wordt bewerkt* ontbreekt",
          "geen element; noem het ontbrekende kenmerk",
          lambda k, e: True,
          lambda k, e: Uitkomst("geen_element", 18, "Passief, maar niet zelfstandig genoeg",
                                redenen=[f"{NAAM[s]}: nee" for s in _passief_ontbrekend(k)])),
]

NAREGELS = [
    ("Na regel 16/17", "geen *levenscyclus*", "voorleggen"),
    ("6 Tegenhanger", "Actor of Rol met *onderscheidbare exemplaren* + *levenscyclus* + *wordt bewerkt*",
     "ook een bedrijfsobjectpagina (tegenhanger); bij gedrag nooit: het resultaat is dan een apart begrip"),
    ("7 Annotatie", "*geautomatiseerd verwerkt*", "`data_object: ja` (voedt het hiaat-signaal richting GGM)"),
]


class BeoordelingFout(ValueError):
    def __init__(self, fouten: list[str]):
        self.fouten = fouten
        super().__init__("; ".join(fouten))


def controleer(beoordeling: dict) -> list[str]:
    """Structurele controle van een beoordeling (aanvullend op het JSON-schema)."""
    fouten = []
    kenmerken = beoordeling.get("kenmerken", {})
    ontbrekend = [s for s in SLEUTELS if s not in kenmerken]
    if ontbrekend:
        fouten.append(f"kenmerken niet beantwoord: {', '.join(NAAM[s] for s in ontbrekend)}")
    for sleutel, antwoord in kenmerken.items():
        if sleutel not in NAAM:
            fouten.append(f"onbekend kenmerk '{sleutel}'")
        elif not isinstance(antwoord, dict) or antwoord.get("waarde") not in ("ja", "nee"):
            fouten.append(f"kenmerk '{NAAM[sleutel]}': waarde moet 'ja' of 'nee' zijn")
        elif not str(antwoord.get("onderbouwing", "")).strip():
            fouten.append(f"kenmerk '{NAAM[sleutel]}': onderbouwing ontbreekt")
    return fouten


def waarden(beoordeling: dict) -> dict[str, str]:
    return {s: beoordeling["kenmerken"][s]["waarde"] for s in SLEUTELS}


def evalueer(beoordeling: dict) -> Uitkomst:
    fouten = controleer(beoordeling)
    if fouten:
        raise BeoordelingFout(fouten)
    k = waarden(beoordeling)
    extra = {s: beoordeling.get(s) for s in EXTRA_VELDEN}

    for regel in REGELS:
        if regel.test(k, extra):
            uitkomst = regel.uitkomst(k, extra)
            break

    if uitkomst.soort == "eigenschap" and not extra.get("genoemd_begrip"):
        uitkomst.voorleggen = True
        uitkomst.redenen.append("genoemd begrip ontbreekt")
    if uitkomst.regel == 4 and extra.get("benoemde_partij") not in ("ja", "nee"):
        uitkomst.voorleggen = True
        uitkomst.redenen.append("'benoemde_partij' (ja/nee) ontbreekt bij handelende partij + hoedanigheid")
    if uitkomst.regel in (16, 17) and not _ja(k, "levenscyclus"):
        uitkomst.voorleggen = True
        uitkomst.redenen.append("levenscyclus: nee")
    if uitkomst.paginatype in ("actor", "rol") and all(
        _ja(k, s) for s in ("onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt")
    ):
        uitkomst.tegenhanger = "bedrijfsobject"
    if _ja(k, "geautomatiseerd_verwerkt"):
        uitkomst.data_object = "ja"
    return uitkomst


def voorgestelde_status(uitkomst: Uitkomst | dict, ggm_match: str | None = None, grondslag: str | None = None) -> str | None:
    """`review` alleen als de AI het zelfstandig mag afhandelen; anders `kandidaat`.

    Geen pagina (buiten scope, eigenschap, geen element, conflict, herkend) → None.
    """
    u = uitkomst if isinstance(uitkomst, dict) else asdict(uitkomst)
    if u["soort"] != "element":
        return None
    if u["voorleggen"]:
        return "kandidaat"
    if grondslag == "governance-object":
        return "kandidaat"
    if u["data_object"] == "ja" and ggm_match not in ("exact", "sterk"):
        return "kandidaat"
    return "review"


# --- Generatie: tabellen voor de criteria-skill en het beoordeling-schema ---


def markdown() -> str:
    regels = ["### Kenmerken", ""]
    for groep in dict.fromkeys(k.groep for k in KENMERKEN):
        regels += [f"**{groep}**", "", "| Kenmerk | Vraag | Herkomst | Voorbeeld | Tegenvoorbeeld |", "|---|---|---|---|---|"]
        regels += [
            f"| {k.naam} | {k.vraag} | {k.herkomst} | {k.voorbeeld} | {k.tegenvoorbeeld} |"
            for k in KENMERKEN if k.groep == groep
        ]
        regels.append("")
    regels += [
        "### Beslistabel (= de criteria)",
        "",
        "Van boven naar beneden; de eerste passende regel beslist. Daarna gelden de aanvullingen.",
        "",
        "| Nr | Stap | Als | Dan |",
        "|---|---|---|---|",
    ]
    regels += [f"| {i} | {r.stap} | {r.als} | {r.dan} |" for i, r in enumerate(REGELS, start=1)]
    regels += ["", "**Aanvullingen**", "", "| Stap | Als | Dan |", "|---|---|---|"]
    regels += [f"| {stap} | {als} | {dan} |" for stap, als, dan in NAREGELS]
    return "\n".join(regels) + "\n"


def schema() -> dict:
    antwoord = {
        "type": "object",
        "required": ["waarde", "onderbouwing"],
        "properties": {
            "waarde": {"enum": ["ja", "nee"]},
            "onderbouwing": {"type": "string", "minLength": 1},
            "bronnen": {"type": "array", "items": {"type": "string"}},
        },
        "additionalProperties": False,
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "beoordeling",
        "description": "Beoordeling van één begrip: alle kenmerken één keer beantwoord (gegenereerd door tools/bepaal_type.py schema).",
        "type": "object",
        "required": ["begrip", "kenmerken"],
        "properties": {
            "begrip": {"type": "string", "minLength": 1},
            "onderwerp": {"type": "string"},
            "kenmerken": {
                "type": "object",
                "required": SLEUTELS,
                "properties": {s: {"$ref": "#/$defs/antwoord"} for s in SLEUTELS},
                "additionalProperties": False,
            },
            "genoemd_begrip": {"type": "string", "description": EXTRA_VELDEN["genoemd_begrip"]},
            "archimate_buiten_model": {"type": "string", "description": EXTRA_VELDEN["archimate_buiten_model"]},
            "benoemde_partij": {"enum": ["ja", "nee"], "description": EXTRA_VELDEN["benoemde_partij"]},
            "uitkomst": {"type": "object", "description": "Door bepaal_type.py ingevuld; niet zelf invullen"},
        },
        "additionalProperties": False,
        "$defs": {
            "antwoord": antwoord,
            "kenmerkwaarden": {
                "type": "object",
                "description": "Kenmerken zoals vastgelegd op een elementpagina (alleen ja/nee; onderbouwing in de body)",
                "required": SLEUTELS,
                "properties": {s: {"enum": ["ja", "nee"]} for s in SLEUTELS},
                "additionalProperties": False,
            },
        },
    }


# --- CLI ---


def _beoordelingen(data: dict) -> list[tuple[str, dict]]:
    """Accepteert een assessment (voorstellen met `beoordeling`) of één beoordeling."""
    if "voorstellen" in data:
        return [(v.get("doel", "?"), v["beoordeling"]) for v in data["voorstellen"] if "beoordeling" in v]
    return [(data.get("begrip", "?"), data)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_eval = sub.add_parser("evalueer", help="Pas de beslistabel toe op een assessment of beoordeling")
    p_eval.add_argument("bestand")
    p_eval.add_argument("--schrijf", action="store_true", help="Zet de uitkomst terug in het bestand (veld 'uitkomst')")
    p_status = sub.add_parser("status", help="Voorgestelde status voor een uitkomst")
    p_status.add_argument("--uitkomst", required=True)
    p_status.add_argument("--ggm-match")
    p_status.add_argument("--grondslag")
    sub.add_parser("markdown", help="Tabellen voor de criteria-skill")
    p_schema = sub.add_parser("schema", help="Beoordeling-schema")
    p_schema.add_argument("--schrijf", action="store_true", help=f"Schrijf naar {SCHEMA_PATH.relative_to(WIKI_ROOT)}")
    args = parser.parse_args(argv)

    if args.cmd == "markdown":
        sys.stdout.write(markdown())
        return 0
    if args.cmd == "schema":
        tekst = json.dumps(schema(), indent=2, ensure_ascii=False) + "\n"
        if args.schrijf:
            SCHEMA_PATH.write_text(tekst, encoding="utf-8")
            print(f"Geschreven: {SCHEMA_PATH}")
        else:
            sys.stdout.write(tekst)
        return 0
    if args.cmd == "status":
        uitkomst = json.loads(Path(args.uitkomst).read_text(encoding="utf-8"))
        print(voorgestelde_status(uitkomst, args.ggm_match, args.grondslag))
        return 0

    pad = Path(args.bestand)
    data = json.loads(pad.read_text(encoding="utf-8"))
    resultaten, fout = [], False
    for doel, beoordeling in _beoordelingen(data):
        try:
            uitkomst = asdict(evalueer(beoordeling))
        except BeoordelingFout as exc:
            fout = True
            resultaten.append({"doel": doel, "fouten": exc.fouten})
            continue
        resultaten.append({"doel": doel, "uitkomst": uitkomst})
        if args.schrijf:
            beoordeling["uitkomst"] = uitkomst
    if args.schrijf and not fout:
        pad.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(resultaten, indent=2, ensure_ascii=False))
    return 1 if fout else 0


if __name__ == "__main__":
    sys.exit(main())
