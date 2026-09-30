"""Bepaal het ArchiMate-elementtype van een begrip uit zijn kenmerken.

Eén bron van waarheid voor de criteria van deze wiki:
- KENMERKEN: de neutrale eigenschappen die het model per begrip één keer beantwoordt (ja/nee);
- REGELS: stap 1–3 van de beslistabel (scope, afhankelijkheid, aard), van boven naar beneden; de eerste passende
  regel beslist en levert het einde of een voorlopig type op;
- DREMPELS: stap 4, per voorlopig type de getelde criteria (hoogstens DREMPEL_ONTBREKEND keer nee);
- SPECIALISATIE: stap 5, het specialisatieniveau (zelfstandig beleidsbegrip of variant van een breder begrip);
- NAREGELS: aanvullingen op de uitkomst (tegenhanger, annotatie).

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
            "Kennen domeinexperts dit als eigen begrip?",
            "ArchiMate (concept in een domein) + GEMMA (BO-criterium herkenbaar voor domeinexperts)",
            "Omgevingsvergunning", "Technisch volgnummer van een dossierregel"),
    Kenmerk("gemeentelijk", "gemeentelijk", "Scope",
            "Ziet, doet of beslist de gemeente hierover? Bij een externe partij: werkt de gemeente er structureel mee samen "
            "(opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht), en is zij meer dan context?",
            "GEMMA (gemeentelijk perspectief; ketenpartners alleen als context)",
            "Parkeervergunning; GGD (gemeenschappelijke regeling)", "Interne werkvoorraad van het UWV; behandelend arts"),
    Kenmerk("buiten_kernlagen", "buiten kernlagen", "Scope",
            "Is het een thema, doel, waarde, drijfveer, principe, losse norm of eis, of een vermogen? Noem welk ArchiMate-type",
            "ArchiMate (motivatie-, strategie- en overige lagen)",
            "Armoedebestrijding (doel); leefbaarheid (waarde); 'binnen 8 weken beslissen' (norm)", "Bijstandsuitkering"),
    # Zelfstandigheid (alle elementtypen)
    Kenmerk("betekenis_in_onderwerp", "betekenis in onderwerp", "Zelfstandigheid",
            "Speelt het in dit onderwerp een eigen rol, en niet alleen als terloopse vermelding of als begrip dat primair "
            "bij een ander onderwerp hoort?",
            "GEMMA (BO-criterium betekenis binnen het onderwerp)",
            "Graf (lijkbezorging)", "Akte van overlijden (hoort bij de burgerlijke stand)"),
    Kenmerk("slechts_eigenschap", "slechts eigenschap", "Zelfstandigheid",
            "Is het alleen een eigenschap, status, waarde, classificatie of indeling (ook een doelgroep) van één ander "
            "begrip? Noem dat begrip",
            "GEMMA (negatieve toets: eigenschap, status, classificatie)",
            "Bouwjaar (van Pand); status van een aanvraag; minima (indeling van Inwoner)", "Pand"),
    Kenmerk("eigen_identiteit", "eigen identiteit", "Zelfstandigheid",
            "Bestaat het zelfstandig, en niet alleen als onderdeel of deelstap van één ander begrip? Noem dat begrip",
            "GEMMA (BO-criterium eigen bestaan; actorvraag eigen identiteit)",
            "Beschikking; uitgifte van een graf", "Ondertekening van een besluit (deelstap)"),
    Kenmerk("relaties", "relaties", "Zelfstandigheid",
            "Heeft het in de bronnen aanwijsbare relaties met andere begrippen? Bij een partij: gedrag dat zij uitvoert en "
            "objecten die zij houdt of beheert. Noem ze in de onderbouwing",
            "GEMMA (BO-criterium relaties; actor- en rolvragen toewijsbaar aan gedrag, gekoppeld aan taken)",
            "Kerkgenootschap (houdt een bijzondere begraafplaats)", "Begrip dat alleen in een opsomming voorkomt"),
    Kenmerk("zelfstandig_beleidsbegrip", "zelfstandig beleidsbegrip", "Zelfstandigheid",
            "Herkent de gemeente dit als apart soort ding naast zijn generalisatie, met eigen gegevens of een eigen "
            "behandeling, op het detailniveau van GEMMA? Nee als het een variant is van een breder herkenbaar begrip; "
            "noem dat begrip",
            "GEMMA (beslisvraag: zelfstandig ding waar beleid op gemaakt wordt)",
            "Omgevingsvergunning; parkeervergunning", "Vergunning tot opgraving (variant van een vergunning)"),
    # Aard
    Kenmerk("gedrag", "gedrag", "Aard",
            "Beschrijft het iets wat gedaan wordt of gebeurt, en niet een ding, partij of plaats?",
            "ArchiMate (gedragselement)",
            "Aanvraag behandelen; verhuizing", "Aanvraag"),
    Kenmerk("handelende_partij", "handelende partij", "Aard",
            "Is het een persoon, organisatie of organisatie-eenheid (ook extern of generiek) die zelf kan handelen?",
            "ArchiMate Business Actor (actorvragen zelfstandig gedrag; persoon, organisatie of eenheid)",
            "College van B&W; inwoner; woningcorporatie", "Aanvrager"),
    Kenmerk("hoedanigheid", "hoedanigheid", "Aard",
            "Is het een verantwoordelijkheid waaraan een partij wordt toegewezen, of de hoedanigheid waarin een partij optreedt in een handeling of gebeurtenis?",
            "ArchiMate Business Role (rolvragen verantwoordelijkheid; actor toewijsbaar)",
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
    # Partij
    Kenmerk("los_van_verantwoordelijkheid", "los van verantwoordelijkheid", "Partij",
            "Bestaat de partij los van de taak of verantwoordelijkheid die zij hier heeft, zodat zij ook andere rollen kan "
            "vervullen? Ja: actor; nee: rol. Nee als het geen partij of verantwoordelijkheid is",
            "ArchiMate Actor/Role (actorvragen meerdere rollen, blijft bestaan als verantwoordelijkheden veranderen; "
            "rolvraag geen eigen identiteit)",
            "Kerkgenootschap; burgemeester", "Houder van de begraafplaats"),
    Kenmerk("meerdere_vervullers", "meerdere vervullers", "Partij",
            "Kan deze verantwoordelijkheid door verschillende partijen worden vervuld? Nee als het geen verantwoordelijkheid is",
            "ArchiMate Business Role (rolvraag door meerdere actoren vervulbaar)",
            "Houder van de begraafplaats (gemeente of kerkgenootschap)", "Burgemeester"),
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
    # Gedrag (drempel voor proces en functie; nee als het geen gedrag is)
    Kenmerk("toegewezen_partij", "toegewezen partij", "Gedrag",
            "Is er een actor of rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem die. "
            "Nee als het geen gedrag is",
            "ArchiMate (assignment van actor of rol aan gedrag)",
            "Ruiming (houder van de begraafplaats)", "Draagvlak creëren (niemand aanwijsbaar)"),
    Kenmerk("gebruikt_objecten", "gebruikt objecten", "Gedrag",
            "Leest, maakt of wijzigt het gedrag aanwijsbare bedrijfsobjecten? Noem ze. Nee als het geen gedrag is",
            "ArchiMate (access van gedrag naar passief element)",
            "Inspraak (ontwerpbesluit, zienswijze)", "Burgerberaad (geen vast object)"),
    Kenmerk("aanleiding", "aanleiding", "Gedrag",
            "Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die. Nee als het geen gedrag is",
            "ArchiMate (triggering) + GEMMA (procesarchitectuur: een proces start bij een gebeurtenis)",
            "Overheidsparticipatie (verzoek ingediend)", "Kennisdeling"),
    Kenmerk("benoembaar_resultaat", "benoembaar resultaat", "Gedrag",
            "Levert het een concreet, benoembaar resultaat op (besluit, product, verslag, afspraak)? Nee als het geen "
            "gedrag is",
            "ArchiMate Business Process (achieves a specific result) + GEMMA (proces levert product of besluit)",
            "Opgraving (opgegraven lijk)", "Informeren"),
    Kenmerk("herhaald_uitgevoerd", "herhaald uitgevoerd", "Gedrag",
            "Wordt het regelmatig en voor verschillende gevallen doorlopen, en is het geen eenmalig project? Nee als "
            "het geen gedrag is",
            "GEMMA (proces als herhaalbare werkwijze; tegenhanger van onderscheidbare exemplaren)",
            "Inspraak (per ontwerpbesluit)", "Invoeren van de participatieverordening (eenmalig)"),
    Kenmerk("eigen_normering", "eigen normering", "Gedrag",
            "Gelden er eigen regels, termijnen of bevoegdheden voor, uit wet, verordening of beleidsregel? Noem ze. "
            "Nee als het geen gedrag is",
            "GEMMA (proces met eigen spelregels; tegenhanger van levenscyclus)",
            "Inspraak (afdeling 3.4 Awb)", "Burgerberaad (vormvrij)"),
    Kenmerk("stabiel_over_tijd", "stabiel over tijd", "Gedrag",
            "Blijft deze groepering van gedrag bestaan als de organisatie-inrichting of werkwijze verandert? Nee als "
            "het geen gedrag is",
            "ArchiMate Business Function (stabiel, los van de organisatie) + GEMMA (bedrijfsfunctiemodel)",
            "Participatie; belastingheffing", "Projectteam Omgevingswet"),
    # Passief
    Kenmerk("onderscheidbare_exemplaren", "onderscheidbare exemplaren", "Passief",
            "Zijn de afzonderlijke exemplaren van elkaar te onderscheiden?",
            "GEMMA (BO-criterium kan in meervoud bestaan)",
            "Aanvraag (elke aanvraag apart)", "Gemeentefonds (er is er één)"),
    Kenmerk("levenscyclus", "levenscyclus", "Passief",
            "Ontstaan, veranderen en eindigen de exemplaren?",
            "GEMMA (BO-criterium eigen levenscyclus)",
            "Vergunning (verleend, gewijzigd, ingetrokken)", "Kadastrale gemeentecode"),
    Kenmerk("wordt_bewerkt", "wordt bewerkt", "Passief",
            "Wordt het concreet door gemeentelijk gedrag gebruikt, gemaakt of gewijzigd (operationeel, en niet alleen beleidsmatig)?",
            "ArchiMate (access-relatie) + GEMMA (abstractieniveau operationeel)",
            "Aanvraag (ontvangen, beoordeeld)", "Preventieakkoord (alleen beleidsmatig)"),
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

# Stap 4: per voorlopig paginatype de criteria die worden geteld. `herkenbaar` en `gemeentelijk` (stap 1) en
# `eigen_identiteit` (stap 2) zijn al harde poorten. Hoogstens DREMPEL_ONTBREKEND criteria mogen nee zijn.
DREMPEL_ONTBREKEND = 1
BASIS = ["betekenis_in_onderwerp", "relaties"]
DREMPELS: list[tuple[str, tuple[str, ...], list[str]]] = [
    ("Bedrijfsobject, Contract", ("bedrijfsobject",), BASIS + ["onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt"]),
    ("Product", ("product",), BASIS + ["onderscheidbare_exemplaren"]),
    ("Actor", ("actor",), BASIS),
    ("Rol", ("rol",), BASIS + ["meerdere_vervullers"]),
    # Bij proces en functie vervangen toegewezen partij en gebruikt objecten het brede kenmerk relaties.
    ("Proces", ("bedrijfsproces",), ["betekenis_in_onderwerp", "toegewezen_partij", "gebruikt_objecten", "aanleiding",
                                      "benoembaar_resultaat", "herhaald_uitgevoerd", "eigen_normering"]),
    ("Functie", ("bedrijfsfunctie",), ["betekenis_in_onderwerp", "toegewezen_partij", "gebruikt_objecten",
                                        "stabiel_over_tijd"]),
    ("Gebeurtenis, Dienst", ("bedrijfsgebeurtenis", "bedrijfsdienst"), BASIS),
]

# Extra velden in een beoordeling (geen kenmerken): nodig bij bepaalde uitkomsten.
EXTRA_VELDEN = {
    "genoemd_begrip": "Het begrip waarvan dit een eigenschap, onderdeel, variant (specialisatie) of waarneembare vorm is",
    "archimate_buiten_model": "Het ArchiMate-type buiten de kernlagen (Goal, Outcome, Driver, Principle, Requirement, Constraint, Value, Capability, Grouping …)",
}


@dataclass
class Uitkomst:
    # element | herkend | buiten_scope | buiten_model | eigenschap | onderdeel | specialisatie | geen_element | conflict
    soort: str
    regel: int
    toelichting: str
    paginatype: str | None = None
    archimate_type: str | None = None
    voorleggen: bool = False
    redenen: list[str] = field(default_factory=list)
    tegenhanger: str | None = None
    data_object: str = "nee"
    genoemd_begrip: str | None = None
    typeregel: int | None = None  # regel uit stap 3 die het voorlopige type gaf (bij uitkomsten van stap 4 en 5)


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
        return _herkend(13, archimate_type, f"Gedrag, {_namen([soort])}")
    return _element(13, paginatype, archimate_type, f"Gedrag, {_namen([soort])}")


def _partij(k: dict) -> Uitkomst:
    if _ja(k, "los_van_verantwoordelijkheid"):
        return _element(5, "actor", "business-actor", "Partij en hoedanigheid, los van de verantwoordelijkheid")
    return _element(5, "rol", "business-role", "Partij en hoedanigheid, gebonden aan de verantwoordelijkheid")


REGELS: list[Regel] = [
    Regel("1 Scope", "niet *herkenbaar* of niet *gemeentelijk*", "buiten scope, met reden",
          lambda k, e: not (_ja(k, "herkenbaar") and _ja(k, "gemeentelijk")),
          lambda k, e: Uitkomst("buiten_scope", 1, "Niet herkenbaar of niet gemeentelijk",
                                redenen=[f"{NAAM[s]}: nee" for s in ("herkenbaar", "gemeentelijk") if not _ja(k, s)])),
    Regel("1 Scope", "*buiten kernlagen*", "buiten dit model, met het ArchiMate-type (Goal, Driver, Capability …)",
          lambda k, e: _ja(k, "buiten_kernlagen"),
          lambda k, e: Uitkomst("buiten_model", 2, "Buiten de kernlagen van dit model",
                                archimate_type=e.get("archimate_buiten_model"))),
    Regel("2 Afhankelijk", "*slechts eigenschap*", "eigenschap, status of indeling van het genoemde begrip; geen pagina",
          lambda k, e: _ja(k, "slechts_eigenschap"),
          lambda k, e: Uitkomst("eigenschap", 3, "Eigenschap, status of indeling van een ander begrip",
                                genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("2 Afhankelijk", "niet *eigen identiteit*",
          "onderdeel of deelstap van het genoemde begrip; geen pagina, relaties opgetild",
          lambda k, e: not _ja(k, "eigen_identiteit"),
          lambda k, e: Uitkomst("onderdeel", 4, "Onderdeel of deelstap van een ander begrip",
                                genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("3 Aard", "*handelende partij* én *hoedanigheid* (verder geen aard)",
          "*los van verantwoordelijkheid* ja → Actor, nee → Rol",
          lambda k, e: _aard(k) == {"handelende_partij", "hoedanigheid"},
          lambda k, e: _partij(k)),
    Regel("3 Aard", "meer dan één aard (behalve actor + rol)", "conflict: voorleggen",
          lambda k, e: len(_aard(k)) > 1,
          lambda k, e: _conflict(6, f"Meer dan één aard: {_namen(sorted(_aard(k)))}")),
    Regel("3 Aard", "*handelende partij*", "Actor; conflict als niet *los van verantwoordelijkheid* (mogelijk rol)",
          lambda k, e: _aard(k) == {"handelende_partij"},
          lambda k, e: _element(7, "actor", "business-actor", "Handelende partij")
          if _ja(k, "los_van_verantwoordelijkheid")
          else _conflict(7, "Handelende partij, maar niet los van de verantwoordelijkheid: mogelijk een rol")),
    Regel("3 Aard", "*hoedanigheid*", "Rol; conflict als *los van verantwoordelijkheid* (mogelijk actor)",
          lambda k, e: _aard(k) == {"hoedanigheid"},
          lambda k, e: _element(8, "rol", "business-role", "Hoedanigheid")
          if not _ja(k, "los_van_verantwoordelijkheid")
          else _conflict(8, "Hoedanigheid, maar los van de verantwoordelijkheid: mogelijk een actor")),
    Regel("3 Aard", "*aanbod als geheel*", "Product",
          lambda k, e: _aard(k) == {"aanbod_als_geheel"},
          lambda k, e: _element(9, "product", "product", "Aanbod als geheel")),
    Regel("3 Aard", "*samenwerkingsverband*", "Business Collaboration: herkend, voorleggen",
          lambda k, e: _aard(k) == {"samenwerkingsverband"},
          lambda k, e: _herkend(10, "business-collaboration", "Samenwerkingsverband")),
    Regel("3 Aard", "*toegangspunt*", "Business Interface: herkend, voorleggen",
          lambda k, e: _aard(k) == {"toegangspunt"},
          lambda k, e: _herkend(11, "business-interface", "Toegangspunt")),
    Regel("3 Aard", "*plaats*", "Location: herkend, voorleggen",
          lambda k, e: _aard(k) == {"plaats"},
          lambda k, e: _herkend(12, "location", "Plaats")),
    Regel("3 Gedrag", "*gedrag* en precies één van *per keer doorlopen* / *gegroepeerd gedrag* / "
          "*toestandsverandering* / *aangeboden gedrag* / *gezamenlijk gedrag*",
          "Business Process / Function / Event / Service / Interaction (Interaction: herkend, voorleggen)",
          lambda k, e: _aard(k) == {"gedrag"} and len(_gedragssoorten(k)) == 1,
          _gedrag_uitkomst),
    Regel("3 Gedrag", "*gedrag*, maar geen of meer dan één soort gedrag", "conflict: voorleggen",
          lambda k, e: _aard(k) == {"gedrag"},
          lambda k, e: _conflict(14, f"Soort gedrag niet eenduidig: {_namen(_gedragssoorten(k)) or 'geen'}")),
    Regel("3 Passief", "geen aard, maar wel een soort gedrag", "conflict: voorleggen (tegenstrijdige antwoorden)",
          lambda k, e: bool(_gedragssoorten(k)),
          lambda k, e: _conflict(15, f"Geen gedrag, maar wel {_namen(_gedragssoorten(k))}")),
    Regel("3 Passief", "*waarneembare vorm*", "Representation van het genoemde begrip: herkend, voorleggen",
          lambda k, e: _ja(k, "waarneembare_vorm"),
          lambda k, e: _herkend(16, "representation", "Waarneembare vorm", genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("3 Passief", "*afspraak*", "Contract",
          lambda k, e: _ja(k, "afspraak"),
          lambda k, e: _element(17, "bedrijfsobject", "contract", "Passief, afspraak")),
    Regel("3 Passief", "overig passief begrip",
          "Business Object (een wet of verordening als geheel: grondslag governance-object)",
          lambda k, e: True,
          lambda k, e: _element(18, "bedrijfsobject", "business-object", "Passief")),
]

EERSTE_DREMPELREGEL = len(REGELS) + 1
SPECIALISATIE = [
    ("niet *zelfstandig beleidsbegrip*, met `genoemd_begrip`",
     "specialisatie zonder pagina van het genoemde, herkenbare bredere begrip; relaties opgetild"),
    ("niet *zelfstandig beleidsbegrip*, zonder `genoemd_begrip`", "voorleggen: noem het bredere begrip"),
    ("anders", "element van het voorlopige type"),
]
EERSTE_SPECIALISATIEREGEL = EERSTE_DREMPELREGEL + len(DREMPELS)

NAREGELS = [
    ("Tegenhanger", "Actor of Rol met *onderscheidbare exemplaren* + *levenscyclus* + *wordt bewerkt*",
     "ook een bedrijfsobjectpagina (tegenhanger); bij gedrag nooit: het resultaat is dan een apart begrip"),
    ("Annotatie", "*geautomatiseerd verwerkt*", "`data_object: ja` (voedt het hiaat-signaal richting GGM)"),
]


def _drempel(paginatype: str) -> tuple[int, list[str]]:
    for i, (_, typen, criteria) in enumerate(DREMPELS):
        if paginatype in typen:
            return EERSTE_DREMPELREGEL + i, criteria
    raise KeyError(paginatype)


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


def _stap_1_tot_3(k: dict, extra: dict) -> Uitkomst:
    for regel in REGELS:
        if regel.test(k, extra):
            return regel.uitkomst(k, extra)
    raise AssertionError("de laatste regel past altijd")


def _stap_4_en_5(u: Uitkomst, k: dict, extra: dict) -> Uitkomst:
    """Drempel en specialisatieniveau voor een voorlopig type met een paginatype."""
    nr, criteria = _drempel(u.paginatype)
    ontbrekend = [s for s in criteria if not _ja(k, s)]
    score = f"{len(criteria) - len(ontbrekend)}/{len(criteria)}"
    if len(ontbrekend) > DREMPEL_ONTBREKEND:
        return Uitkomst("geen_element", nr, f"Drempel niet gehaald voor {u.archimate_type} ({score})",
                        archimate_type=u.archimate_type, voorleggen=True, typeregel=u.regel,
                        redenen=[f"{NAAM[s]}: nee" for s in ontbrekend])
    if ontbrekend:
        score += f", ontbreekt: {_namen(ontbrekend)}"
    if not _ja(k, "zelfstandig_beleidsbegrip"):
        if extra.get("genoemd_begrip"):
            return Uitkomst("specialisatie", EERSTE_SPECIALISATIEREGEL, f"Variant van een breder begrip ({score})",
                            archimate_type=u.archimate_type, genoemd_begrip=extra["genoemd_begrip"], typeregel=u.regel)
        return Uitkomst("geen_element", EERSTE_SPECIALISATIEREGEL + 1, f"Niet zelfstandig ({score})",
                        archimate_type=u.archimate_type, voorleggen=True, typeregel=u.regel,
                        redenen=["zelfstandig beleidsbegrip: nee, maar het bredere begrip (genoemd_begrip) ontbreekt"])
    return Uitkomst("element", EERSTE_SPECIALISATIEREGEL + 2, f"{u.toelichting} ({score})",
                    paginatype=u.paginatype, archimate_type=u.archimate_type, typeregel=u.regel)


def evalueer(beoordeling: dict) -> Uitkomst:
    fouten = controleer(beoordeling)
    if fouten:
        raise BeoordelingFout(fouten)
    k = waarden(beoordeling)
    extra = {s: beoordeling.get(s) for s in EXTRA_VELDEN}

    uitkomst = _stap_1_tot_3(k, extra)
    if uitkomst.soort == "element":
        uitkomst = _stap_4_en_5(uitkomst, k, extra)

    if uitkomst.soort in ("eigenschap", "onderdeel") and not extra.get("genoemd_begrip"):
        uitkomst.voorleggen = True
        uitkomst.redenen.append("genoemd begrip ontbreekt")
    if uitkomst.paginatype in ("actor", "rol") and all(
        _ja(k, s) for s in ("onderscheidbare_exemplaren", "levenscyclus", "wordt_bewerkt")
    ):
        uitkomst.tegenhanger = "bedrijfsobject"
    if _ja(k, "geautomatiseerd_verwerkt"):
        uitkomst.data_object = "ja"
    return uitkomst


def voorgestelde_status(uitkomst: Uitkomst | dict, ggm_match: str | None = None, grondslag: str | None = None) -> str | None:
    """`review` alleen als de AI het zelfstandig mag afhandelen; anders `kandidaat`.

    Geen pagina (buiten scope, eigenschap, onderdeel, specialisatie, geen element, conflict, herkend) → None.
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
        "Stap 1–3 van boven naar beneden: de eerste passende regel beslist en levert het einde of een voorlopig type "
        "op. Een voorlopig type met een paginatype gaat door naar stap 4 (drempel) en stap 5 (specialisatieniveau). "
        "Daarna gelden de aanvullingen.",
        "",
        "| Nr | Stap | Als | Dan |",
        "|---|---|---|---|",
    ]
    regels += [f"| {i} | {r.stap} | {r.als} | {r.dan} |" for i, r in enumerate(REGELS, start=1)]
    regels += [
        "",
        f"**Stap 4 — Drempel.** Per voorlopig type de getelde criteria; hoogstens {DREMPEL_ONTBREKEND} nee. "
        "*herkenbaar*, *gemeentelijk* en *eigen identiteit* zijn al harde poorten in stap 1 en 2. "
        "Meer nee → geen element, voorleggen met de ontbrekende criteria.",
        "",
        "| Nr | Type | Getelde criteria |",
        "|---|---|---|",
    ]
    regels += [f"| {EERSTE_DREMPELREGEL + i} | {naam} | {_namen(criteria)} |" for i, (naam, _, criteria) in enumerate(DREMPELS)]
    regels += ["", "**Stap 5 — Specialisatieniveau** (alle typen met een paginatype)", "", "| Nr | Als | Dan |", "|---|---|---|"]
    regels += [f"| {EERSTE_SPECIALISATIEREGEL + i} | {als} | {dan} |" for i, (als, dan) in enumerate(SPECIALISATIE)]
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
            SCHEMA_PATH.write_text(tekst, encoding="utf-8", newline="\n")
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
