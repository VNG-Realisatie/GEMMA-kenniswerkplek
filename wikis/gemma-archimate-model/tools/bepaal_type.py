"""Bepaal het ArchiMate-elementtype van een begrip uit zijn kenmerken.

Eén bron van waarheid voor de criteria van deze wiki (criteria van 2026-10-01):
- KENMERKEN: de neutrale eigenschappen die het model per begrip één keer beantwoordt (ja/nee), met de vraag die
  bepaalt of het kenmerk van toepassing is, en bij welke aard een ja mag (consistentie);
- TYPEN: per elementtype het kenmerk dat het type bepaalt, de kernrelatie (moet ja), de overige drempelcriteria
  (hoogstens DREMPEL_ONTBREKEND keer nee) en de aanvullingen;
- REGELS: stap 0–4 van de beslistabel (welk begrip, scope, afhankelijkheid, consistentie, type), van boven naar
  beneden; de eerste passende regel beslist en levert het einde of een voorlopig type op;
- stap 5 (drempel) en stap 6 (zelfstandige specialisatie) voor een voorlopig type met een pagina;
- NAREGELS: aanvullingen op de uitkomst (tegenhanger, procesniveau, annotatie, homoniem).

Het model vult de kenmerken in (met onderbouwing en bron-id's); deze tool past de regels toe.
De documentatie in skill `gemma-archimate-model-criteria`, de wikipagina `analyses/beslistabel.md` en
`schemas/beoordeling.schema.json` worden hieruit gegenereerd (`markdown --schrijf`, `schema --schrijf`); een test
bewaakt dat ze gelijk blijven.

Gebruik (vanuit de wikimap):
    uv run python tools/bepaal_type.py evalueer <assessment.json | beoordeling.json> [--schrijf]
    uv run python tools/bepaal_type.py status --uitkomst <uitkomst.json> [--ggm-match sterk] [--grondslag ggm-entiteit]
    uv run python tools/bepaal_type.py markdown [--schrijf]   # documentatie in de criteria-skill en de wiki
    uv run python tools/bepaal_type.py schema [--schrijf]     # schemas/beoordeling.schema.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable

WIKI_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = WIKI_ROOT / "schemas" / "beoordeling.schema.json"
SKILL_PATH = WIKI_ROOT / ".agents" / "skills" / "gemma-archimate-model-criteria" / "SKILL.md"
DOC_PATH = WIKI_ROOT / "analyses" / "beslistabel.md"
CRITERIA_VERSIE = "2026-10-01"

GEEN_AARD = ""  # in `bij`: ja mag ook als het begrip geen aard heeft (een ding)


@dataclass(frozen=True)
class Kenmerk:
    sleutel: str
    naam: str
    groep: str
    vraag: str
    ja: str
    nee: str
    herkomst: str
    bij: frozenset | None = None  # aarden waarbij ja mag; None = altijd


def _bij(*aarden: str) -> frozenset:
    return frozenset(aarden)


GEDRAG_BIJ = _bij("gedrag")
KENMERKEN: list[Kenmerk] = [
    # Poort (alle typen)
    Kenmerk("herkenbaar", "herkenbaar", "Poort",
            "Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam?",
            "het komt in wet, beleid of praktijk voor als zelfstandig begrip (Omgevingsvergunning)",
            "technisch hulpgegeven of constructie van de modelleur (volgnummer van een dossierregel)",
            "ArchiMate (concept in een domein); GEMMA (herkenbaar voor domeinexperts)"),
    Kenmerk("gemeentelijk", "gemeentelijk", "Poort",
            "Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij "
            "(opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)?",
            "de gemeente voert uit, beslist, stelt vast, of is structureel partner (GGD)",
            "alleen context, of de interne zaak van een ketenpartner (behandelend arts)",
            "GEMMA (gemeentelijk perspectief)"),
    Kenmerk("buiten_dit_model", "buiten dit model", "Poort",
            "Is het een doel, waarde, drijfveer, principe, losse norm of eis, vermogen of thema, en geen beleidskader? "
            "Noem het ArchiMate-type.",
            "armoedebestrijding (doel); 'binnen acht weken beslissen' (norm uit één artikel)",
            "bijstandsuitkering; Wet op de lijkbezorging (beleidskader)",
            "ArchiMate (motivatie-, strategie- en overige lagen)"),
    Kenmerk("slechts_eigenschap", "slechts eigenschap", "Poort",
            "Is het alleen een eigenschap, status, waarde, classificatie of indeling van één ander begrip, ook een "
            "doelgroep? Noem dat begrip.",
            "bouwjaar (van Pand); minima (indeling van Inwoner)", "Pand",
            "GEMMA (negatieve toets: eigenschap, status, classificatie)"),
    Kenmerk("eigen_identiteit", "eigen identiteit", "Poort",
            "Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling "
            "daarvan? Noem bij nee dat begrip.",
            "Beschikking; uitgifte van een graf", "ondertekening van een besluit (deelstap)",
            "GEMMA (eigen bestaan; procesarchitectuur: processtap, handeling)"),
    Kenmerk("betekenis_in_onderwerp", "betekenis in onderwerp", "Poort",
            "Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? "
            "Noem bij nee dat onderwerp.",
            "Graf in lijkbezorging", "akte van overlijden in lijkbezorging (hoort bij de burgerlijke stand)",
            "GEMMA (betekenis binnen het onderwerp)"),
    # Aard (precies één ja; handelende partij met hoedanigheid of met samenwerkingsverband mag samen)
    Kenmerk("gedrag", "gedrag", "Aard",
            "Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling?",
            "aanvraag behandelen; verhuizing", "aanvraag", "ArchiMate (gedragselement)"),
    Kenmerk("handelende_partij", "handelende partij", "Aard",
            "Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren?",
            "college van B&W; inwoner", "aanvrager", "GEMMA (definitie Actor)"),
    Kenmerk("hoedanigheid", "hoedanigheid", "Aard",
            "Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de "
            "hoedanigheid waarin een partij optreedt?",
            "aanvrager; houder van de begraafplaats", "gemeenteraad", "ArchiMate (definitie Rol)"),
    Kenmerk("samenwerkingsverband", "samenwerkingsverband", "Aard",
            "Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren?",
            "Zorg- en Veiligheidshuis; GGD (samenwerking van gemeenten)", "GGD-arts",
            "ArchiMate (definitie Bedrijfssamenwerking)"),
    Kenmerk("toegangspunt", "toegangspunt", "Aard",
            "Is het een communicatiekanaal waarlangs een dienst beschikbaar komt?",
            "publieksbalie; gemeentelijke website", "klantcontact", "NORA (definitie Kanaal)"),
    Kenmerk("plaats", "plaats", "Aard",
            "Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven?",
            "stadskantoor als vestigingsplaats", "wijk (indeling)", "ArchiMate (Location)"),
    Kenmerk("aanbod_als_geheel", "aanbod als geheel", "Aard",
            "Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer "
            "wordt geleverd?",
            "bewonersparkeervergunning zoals de productencatalogus haar aanbiedt", "parkeren",
            "GEMMA (definitie Product)"),
    Kenmerk("regeling_als_geheel", "regeling als geheel", "Aard",
            "Is het een concreet benoemde wet, AMvB of verordening als geheel, en niet één artikel of een soort "
            "regeling?",
            "Wet op de lijkbezorging; modelverordening participatie",
            "'verordening' als soort (bedrijfsobject Regeling); artikel 16 (losse norm)",
            "GEMMA (definitie Beleidskader)"),
    # Partij
    Kenmerk("los_van_verantwoordelijkheid", "los van verantwoordelijkheid", "Partij",
            "Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen?",
            "kerkgenootschap; burgemeester", "houder van de begraafplaats",
            "ArchiMate (actor tegenover rol)", _bij("handelende_partij", "hoedanigheid")),
    Kenmerk("eigen_rechtspersoon", "eigen rechtspersoon", "Partij",
            "Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, "
            "vennootschap)?",
            "GGD (openbaar lichaam)", "Zorg- en Veiligheidshuis",
            "besluit redacteur 2026-10-01 (scheidslijn actor en bedrijfssamenwerking)",
            _bij("handelende_partij", "samenwerkingsverband")),
    Kenmerk("vervult_een_rol", "vervult een rol", "Partij",
            "Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol.",
            "kerkgenootschap vervult Houder van de begraafplaats", "partij die alleen genoemd wordt",
            "GEMMA (actor wordt toegewezen aan rol)", _bij("handelende_partij", "samenwerkingsverband")),
    Kenmerk("voert_gedrag_uit", "voert gedrag uit", "Partij",
            "Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het.",
            "Houder van de begraafplaats → Ruimen graf", "rol zonder aanwijsbaar gedrag",
            "GEMMA (rol wordt toegewezen aan functie); besluit redacteur 2026-10-01 (ook aan proces)",
            _bij("hoedanigheid", "samenwerkingsverband")),
    Kenmerk("ontsluit_een_dienst", "ontsluit een dienst", "Partij",
            "Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst.",
            "website → Melding openbare ruimte doen", "kanaal zonder aanwijsbare dienst",
            "GEMMA (kanaal wordt toegewezen aan dienst)", _bij("toegangspunt")),
    # Soort gedrag (bij gedrag precies één ja)
    Kenmerk("per_keer_doorlopen", "per keer doorlopen", "Soort gedrag",
            "Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen?",
            "aanvraag omgevingsvergunning behandelen", "vergunningverlening", "GEMMA (definitie Bedrijfsproces)",
            GEDRAG_BIJ),
    Kenmerk("gegroepeerd_gedrag", "gegroepeerd gedrag", "Soort gedrag",
            "Is het een doorlopende groepering van activiteiten op grond van vergelijkbare middelen, kennis of "
            "competenties, zonder eigen volgorde of doorlooptijd, en niet 'wat de gemeente kan'?",
            "vergunningverlening; belastingheffing", "aanslag opleggen", "GEMMA (definitie Bedrijfsfunctie)",
            GEDRAG_BIJ),
    Kenmerk("toestandsverandering", "toestandsverandering", "Soort gedrag",
            "Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat "
            "gevolgen heeft?",
            "verhuizing; aanvraag ontvangen; beslistermijn verstreken", "verhuizing doorgeven",
            "GEMMA (definitie Gebeurtenis)", GEDRAG_BIJ),
    Kenmerk("aangeboden_gedrag", "aangeboden gedrag", "Soort gedrag",
            "Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de "
            "behoefte van de afnemer en los van hoe zij wordt uitgevoerd?",
            "melding openbare ruimte doen", "melding afhandelen", "NORA (definitie Dienst)", GEDRAG_BIJ),
    Kenmerk("gezamenlijk_gedrag", "gezamenlijk gedrag", "Soort gedrag",
            "Kan het alleen door twee of meer partijen samen worden uitgevoerd?",
            "keukentafelgesprek; hoorzitting", "beschikking opstellen", "ArchiMate (Business Interaction)",
            GEDRAG_BIJ),
    # Gedrag (drempel)
    Kenmerk("toegewezen_partij", "toegewezen partij", "Gedrag",
            "Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol.",
            "Ruimen graf (Houder van de begraafplaats)", "draagvlak creëren",
            "ArchiMate (toewijzing van rol aan gedrag)", GEDRAG_BIJ),
    Kenmerk("gebruikt_objecten", "gebruikt objecten", "Gedrag",
            "Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag "
            "aanwijsbare bedrijfsobjecten? Noem object en handeling.",
            "Inspraak (registreert zienswijze)", "burgerberaad",
            "ArchiMate (toegang van gedrag tot object); besluit redacteur 2026-10-01 (handelingen)", GEDRAG_BIJ),
    Kenmerk("aanleiding", "aanleiding", "Gedrag",
            "Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die.",
            "overheidsparticipatie (verzoek ingediend)", "kennisdeling",
            "ArchiMate (triggering); GEMMA (procesarchitectuur)", GEDRAG_BIJ),
    Kenmerk("benoembaar_resultaat", "benoembaar resultaat", "Gedrag",
            "Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: "
            "wat krijgt de afnemer? Noem het.",
            "opgraving (opgegraven lijk)", "informeren",
            "GEMMA (definities Bedrijfsproces en Product: resultaat, waarde voor de afnemer)",
            _bij("gedrag", "aanbod_als_geheel")),
    Kenmerk("komt_herhaald_voor", "komt herhaald voor", "Gedrag",
            "Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende "
            "gevallen, en is het geen eenmalig project of voorval?",
            "inspraak (per ontwerpbesluit); overlijden", "invoeren van de participatieverordening",
            "GEMMA (proces als herhaalbare werkwijze)", GEDRAG_BIJ),
    Kenmerk("eigen_normering", "eigen normering", "Gedrag",
            "Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? "
            "Noem het artikel.",
            "inspraak (afdeling 3.4 Awb)", "burgerberaad (vormvrij)", "GEMMA (proces met eigen spelregels)",
            GEDRAG_BIJ),
    Kenmerk("stabiel_over_tijd", "stabiel over tijd", "Gedrag",
            "Blijft deze groepering bestaan als de organisatie of de werkwijze verandert?",
            "participatie; belastingheffing", "projectteam Omgevingswet",
            "ArchiMate en GEMMA (bedrijfsfunctiemodel)", GEDRAG_BIJ),
    Kenmerk("afnemer", "afnemer", "Gedrag",
            "Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die.",
            "melding openbare ruimte doen (inwoner)", "interne registratiestap",
            "NORA (definitie Dienst); GEMMA (definitie Product, rol Klant)", _bij("gedrag", "aanbod_als_geheel")),
    Kenmerk("gerealiseerd_door", "gerealiseerd door", "Gedrag",
            "Is er een proces of functie aanwijsbaar dat de dienst uitvoert? Noem het.",
            "Onderhoud van graven (gerealiseerd door het proces dat graven onderhoudt)",
            "dienst zonder aanwijsbare uitvoering", "GEMMA (proces en functie realiseren dienst)", GEDRAG_BIJ),
    Kenmerk("leidt_tot_gedrag", "leidt tot gedrag", "Gedrag",
            "Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het.",
            "Overlijden → Uitvoeren lijkbezorging", "voorval zonder gemeentelijk gevolg",
            "GEMMA (gebeurtenis triggert proces)", GEDRAG_BIJ),
    Kenmerk("bijdrage_aan_groter_proces", "bijdrage aan groter proces", "Gedrag",
            "Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat "
            "het eindresultaat levert? Noem dat proces.",
            "toetsen indieningsvereisten (in behandelen aanvraag)", "behandelen aanvraag (levert het besluit zelf)",
            "GEMMA (definitie Deelproces)", GEDRAG_BIJ),
    # Passief
    Kenmerk("onderscheidbare_exemplaren", "onderscheidbare exemplaren", "Passief",
            "Zijn de afzonderlijke exemplaren van elkaar te onderscheiden?",
            "aanvraag (elke aanvraag apart)", "gemeentefonds (er is er één)", "GEMMA (kan in meervoud bestaan)"),
    Kenmerk("levenscyclus", "levenscyclus", "Passief",
            "Ontstaan, veranderen en eindigen de exemplaren?",
            "vergunning (verleend, gewijzigd, ingetrokken)", "kadastrale gemeentecode", "GEMMA (eigen levenscyclus)"),
    Kenmerk("wordt_bewerkt", "wordt bewerkt", "Passief",
            "Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of "
            "verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag.",
            "aanvraag (geregistreerd, beoordeeld)", "preventieakkoord (alleen beleidsmatig)",
            "GEMMA (proces en functie benaderen bedrijfsobject)"),
    Kenmerk("afspraak", "afspraak", "Passief",
            "Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit "
            "of regeling?",
            "subsidieovereenkomst; uitvoeringsovereenkomst", "subsidiebeschikking; verordening",
            "GEMMA (definitie Afspraak)", _bij(GEEN_AARD)),
    Kenmerk("waarneembare_vorm", "waarneembare vorm", "Passief",
            "Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt "
            "vastgelegd of overgebracht? Noem dat begrip.",
            "aanslagbiljet (van Aanslag); register van begraven lijken", "aanslag", "ArchiMate (Representation)",
            _bij(GEEN_AARD)),
    Kenmerk("omvat_diensten_en_afspraken", "omvat diensten en afspraken", "Passief",
            "Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze.",
            "parkeervergunning (dienst parkeren, voorwaarden)", "losse dienst",
            "GEMMA (product bundelt dienst en afspraak)", _bij("aanbod_als_geheel")),
    Kenmerk("geautomatiseerd_verwerkt", "geautomatiseerd verwerkt", "Passief",
            "Wordt het als gegevensstructuur geautomatiseerd verwerkt?",
            "zaak in het zaaksysteem", "keukentafelgesprek", "GEMMA (definitie Data-object)"),
    # Beleidskader
    Kenmerk("landelijk", "landelijk", "Beleidskader",
            "Is het rijks- of EU-regelgeving (wet, AMvB, EU-verordening), of een VNG-modelverordening, en geen "
            "regeling van één gemeente?",
            "Wet op de lijkbezorging; AVG; modelverordening", "beheersverordening van één gemeente (blijft bron)",
            "besluit redacteur 2026-10-01", _bij("regeling_als_geheel")),
    Kenmerk("in_werking", "in werking", "Beleidskader",
            "Is de regeling geldend recht, of als modelverordening actueel?",
            "Archiefwet 1995", "ingetrokken wet", "besluit redacteur 2026-10-01", _bij("regeling_als_geheel")),
    Kenmerk("is_grondslag_voor", "is grondslag voor", "Beleidskader",
            "Geeft de regeling de gemeente een taak, bevoegdheid of plicht, die zij uitvoert in een aanwijsbaar "
            "proces, dienst of product? Noem het artikel en het gedrag.",
            "Wet op de lijkbezorging art. 28 → Verlenen grafrecht", "BW boek 2, gebruikt voor één definitie",
            "GEMMA (beleidskader geeft grondslag; product heeft associatie met beleidskader)",
            _bij("regeling_als_geheel")),
    # Specialisatie (alle typen met een pagina)
    Kenmerk("zelfstandige_specialisatie", "zelfstandige specialisatie", "Specialisatie",
            "Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met "
            "eigen gegevens, regels of werkwijze? Noem het bredere begrip; is er geen breder begrip, dan ja.",
            "Omgevingsvergunning naast Vergunning (eigen wet en procedure); Houder van het crematorium naast Houder "
            "van de begraafplaats (eigen plichten)",
            "vergunning tot opgraving (variant van Vergunning); aanvrager van een vergunning tot opgraving "
            "(variant van Aanvrager)",
            "GEMMA (zelfstandig ding waar beleid op gemaakt wordt; specialisatie)"),
]

SLEUTELS = [k.sleutel for k in KENMERKEN]
NAAM = {k.sleutel: k.naam for k in KENMERKEN}
KENMERK = {k.sleutel: k for k in KENMERKEN}
GROEPEN = list(dict.fromkeys(k.groep for k in KENMERKEN))
GROEP_ALS = {
    "Poort": "Altijd.",
    "Aard": "Altijd. Precies één ja; alleen *handelende partij* met *hoedanigheid* of met *samenwerkingsverband* mag samen.",
    "Partij": "Alleen bij *handelende partij*, *hoedanigheid*, *samenwerkingsverband* of *toegangspunt*.",
    "Soort gedrag": "Alleen bij *gedrag*. Precies één ja.",
    "Gedrag": "Alleen bij *gedrag*; *afnemer* en *benoembaar resultaat* ook bij *aanbod als geheel*.",
    "Passief": "Bij een ding (geen aard); *onderscheidbare exemplaren*, *levenscyclus*, *wordt bewerkt* en "
               "*geautomatiseerd verwerkt* bij elk begrip; *omvat diensten en afspraken* bij *aanbod als geheel*.",
    "Beleidskader": "Alleen bij *regeling als geheel*.",
    "Specialisatie": "Altijd, als het type een pagina heeft.",
}
AARD = ["gedrag", "handelende_partij", "hoedanigheid", "samenwerkingsverband", "toegangspunt", "plaats",
        "aanbod_als_geheel", "regeling_als_geheel"]
SOORT_GEDRAG = [k.sleutel for k in KENMERKEN if k.groep == "Soort gedrag"]

@dataclass(frozen=True)
class Typedef:
    paginatype: str | None
    archimate_type: str
    naam: str  # GEMMA-naam
    laag: str  # pagina | herkend | geen pagina
    bepaald_door: str
    bep: dict  # kenmerk → ja/nee (voor de documentatie)
    kern: str | None = None
    drempel: tuple = ()
    aanvulling: dict = field(default_factory=dict)
    voorbeeld: str = ""
    kort: str = ""


TEGENHANGER = {"onderscheidbare_exemplaren": "tegenhanger", "levenscyclus": "tegenhanger", "wordt_bewerkt": "tegenhanger"}
TYPEN: list[Typedef] = [
    Typedef("bedrijfsobject", "business-object", "Bedrijfsobject", "pagina",
            "geen aard (een ding); *afspraak* en *waarneembare vorm* nee", {"afspraak": "nee", "waarneembare_vorm": "nee"},
            "wordt_bewerkt", ("onderscheidbare_exemplaren", "levenscyclus"),
            {"geautomatiseerd_verwerkt": "annotatie data-object"}, "Graf; Aanvraag; Vergunning", "Obj"),
    Typedef("bedrijfsobject", "contract", "Afspraak", "pagina", "*afspraak*",
            {"afspraak": "ja", "waarneembare_vorm": "nee"}, "wordt_bewerkt",
            ("onderscheidbare_exemplaren", "levenscyclus"), {"geautomatiseerd_verwerkt": "annotatie data-object"},
            "Uitvoeringsovereenkomst; Grafrecht", "Afspr"),
    Typedef("product", "product", "Product", "pagina", "*aanbod als geheel*", {"aanbod_als_geheel": "ja"},
            "omvat_diensten_en_afspraken", ("afnemer", "benoembaar_resultaat"), {},
            "bewonersparkeervergunning in de productencatalogus", "Prod"),
    Typedef("dienst", "business-service", "Dienst", "pagina", "*gedrag* en *aangeboden gedrag*",
            {"gedrag": "ja", "aangeboden_gedrag": "ja"}, "gerealiseerd_door", ("afnemer", "benoembaar_resultaat"), {},
            "Onderhoud van graven", "Dienst"),
    Typedef("bedrijfsproces", "business-process", "Bedrijfsproces", "pagina", "*gedrag* en *per keer doorlopen*",
            {"gedrag": "ja", "per_keer_doorlopen": "ja"}, "toegewezen_partij",
            ("gebruikt_objecten", "aanleiding", "benoembaar_resultaat", "komt_herhaald_voor", "eigen_normering"),
            {"bijdrage_aan_groter_proces": "ja: procesniveau deelproces"},
            "Ruimen graf; Uitvoeren inspraakprocedure", "Proc"),
    Typedef("bedrijfsfunctie", "business-function", "Bedrijfsfunctie", "pagina", "*gedrag* en *gegroepeerd gedrag*",
            {"gedrag": "ja", "gegroepeerd_gedrag": "ja"}, "toegewezen_partij",
            ("gebruikt_objecten", "stabiel_over_tijd"), {}, "Lijkbezorging; Participatie", "Func"),
    Typedef("gebeurtenis", "business-event", "Gebeurtenis", "pagina", "*gedrag* en *toestandsverandering*",
            {"gedrag": "ja", "toestandsverandering": "ja"}, "leidt_tot_gedrag", ("komt_herhaald_voor",), {},
            "Overlijden; Verval van het grafrecht", "Gebt"),
    Typedef("actor", "business-actor", "Actor", "pagina",
            "*handelende partij* met *los van verantwoordelijkheid*; of *samenwerkingsverband* met *eigen rechtspersoon*",
            {"handelende_partij": "ja", "los_van_verantwoordelijkheid": "ja", "samenwerkingsverband": "ja",
             "eigen_rechtspersoon": "ja"}, "vervult_een_rol", (), dict(TEGENHANGER),
            "College van B&W; Kerkgenootschap; GGD", "Actor"),
    Typedef("rol", "business-role", "Rol", "pagina", "*hoedanigheid*, niet *los van verantwoordelijkheid*",
            {"hoedanigheid": "ja", "los_van_verantwoordelijkheid": "nee"}, "voert_gedrag_uit", (), dict(TEGENHANGER),
            "Houder van de begraafplaats; Rechthebbende op het graf", "Rol"),
    Typedef("bedrijfssamenwerking", "business-collaboration", "Bedrijfssamenwerking", "pagina",
            "*samenwerkingsverband* zonder *eigen rechtspersoon*",
            {"samenwerkingsverband": "ja", "eigen_rechtspersoon": "nee"}, "voert_gedrag_uit", (), {},
            "Zorg- en Veiligheidshuis", "Samw"),
    Typedef("kanaal", "business-interface", "Kanaal", "pagina", "*toegangspunt*", {"toegangspunt": "ja"},
            "ontsluit_een_dienst", (), {}, "publieksbalie; gemeentelijke website (centrale set)", "Kan"),
    Typedef("beleidskader", "driver", "Beleidskader", "pagina", "*regeling als geheel* en *landelijk*",
            {"regeling_als_geheel": "ja", "landelijk": "ja"}, "is_grondslag_voor", ("in_werking",), {},
            "Wet op de lijkbezorging; Archiefwet; AVG", "Bkad"),
    Typedef(None, "business-interaction", "Interaction", "herkend", "*gedrag* en *gezamenlijk gedrag*",
            {"gedrag": "ja", "gezamenlijk_gedrag": "ja"}, None, (), {}, "keukentafelgesprek (voorleggen)", "Inter"),
    Typedef(None, "representation", "Representatie", "geen pagina", "*waarneembare vorm*",
            {"waarneembare_vorm": "ja"}, None, (), {}, "register van begraven lijken (vermelden bij Graf)", "Repr"),
    Typedef(None, "location", "Locatie", "geen pagina", "*plaats*", {"plaats": "ja"}, None, (), {},
            "stadskantoor als vestigingsplaats", "Loc"),
]
TYPE = {(t.paginatype, t.archimate_type): t for t in TYPEN}
PAGINATYPEN = sorted({t.paginatype for t in TYPEN if t.paginatype})
DREMPEL_ONTBREKEND = 1
GEDRAGSTYPE = {"per_keer_doorlopen": "business-process", "gegroepeerd_gedrag": "business-function",
               "toestandsverandering": "business-event", "aangeboden_gedrag": "business-service",
               "gezamenlijk_gedrag": "business-interaction"}

# Extra velden in een beoordeling (geen kenmerken): nodig bij bepaalde uitkomsten.
EXTRA_VELDEN = {
    "synoniem_van": "Stap 0: het element (of het begrip in deze run) waarvan dit woord een synoniem is",
    "homoniem_van": "Stap 0: het andere begrip met dezelfde naam, en waar het voorkomt (wiki, GGM, GEMMA-model, bron)",
    "genoemd_begrip": "Het begrip waarvan dit een eigenschap, onderdeel, bredere specialisatie of waarneembare vorm is",
    "archimate_buiten_model": "Het ArchiMate-type buiten dit model (Goal, Outcome, Principle, Requirement, Constraint, "
                              "Value, Capability, Grouping …)",
}


@dataclass
class Uitkomst:
    # element | herkend | geen_pagina | synoniem | bron | buiten_scope | buiten_model | eigenschap | onderdeel
    # | verwijzing | specialisatie | geen_element | conflict
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
    procesniveau: str | None = None
    typeregel: int | None = None  # regel uit stap 4 die het voorlopige type gaf (bij uitkomsten van stap 5 en 6)


def _ja(k: dict, sleutel: str) -> bool:
    return k[sleutel] == "ja"


def _aard(k: dict) -> set[str]:
    return {s for s in AARD if _ja(k, s)}


def _soorten(k: dict) -> list[str]:
    return [s for s in SOORT_GEDRAG if _ja(k, s)]


def _namen(sleutels) -> str:
    return ", ".join(f"*{NAAM[s]}*" for s in sleutels)


def _past_niet(k: dict) -> list[str]:
    """Kenmerken die ja zijn maar niet bij de aard van het begrip passen (stap 3)."""
    aard = _aard(k)
    fout = []
    for km in KENMERKEN:
        if km.bij is None or not _ja(k, km.sleutel):
            continue
        if not (aard & km.bij or (GEEN_AARD in km.bij and not aard)):
            fout.append(km.sleutel)
    return fout


@dataclass(frozen=True)
class Regel:
    stap: str
    als: str
    dan: str
    test: Callable[[dict, dict], bool]
    uitkomst: Callable[[dict, dict, int], Uitkomst]


def _element(nr, archimate_type, toelichting, paginatype=None, **kw) -> Uitkomst:
    t = next(t for t in TYPEN if t.archimate_type == archimate_type and (paginatype is None or t.paginatype == paginatype))
    soort = {"pagina": "element", "herkend": "herkend", "geen pagina": "geen_pagina"}[t.laag]
    u = Uitkomst(soort, nr, toelichting, paginatype=t.paginatype, archimate_type=archimate_type, **kw)
    if t.laag == "herkend":
        u.voorleggen = True
        u.redenen.append(f"{t.naam} heeft in deze wiki geen paginatype")
    return u


def _conflict(nr, reden) -> Uitkomst:
    return Uitkomst("conflict", nr, "Tegenstrijdige kenmerken", voorleggen=True, redenen=[reden])


def _partij(k, e, nr):
    if _ja(k, "los_van_verantwoordelijkheid"):
        return _element(nr, "business-actor", "Partij en hoedanigheid, los van de verantwoordelijkheid")
    return _element(nr, "business-role", "Partij en hoedanigheid, gebonden aan de verantwoordelijkheid")


def _samenwerking(k, e, nr):
    if _ja(k, "eigen_rechtspersoon"):
        return _element(nr, "business-actor", "Samenwerkingsverband met eigen rechtspersoon")
    return _element(nr, "business-collaboration", "Samenwerkingsverband zonder eigen rechtspersoon")


def _gedrag(k, e, nr):
    (soort,) = _soorten(k)
    return _element(nr, GEDRAGSTYPE[soort], f"Gedrag, {_namen([soort])}")


def _kanaal(k, e, nr):
    u = _element(nr, "business-interface", "Toegangspunt")
    u.voorleggen = True
    u.redenen.append("kanalen vormen één centrale set: koppelen aan een bestaand kanaal, een nieuw kanaal alleen na "
                     "besluit van de redacteur")
    return u


def _regeling(k, e, nr):
    if _ja(k, "landelijk"):
        return _element(nr, "driver", "Regeling als geheel, landelijk")
    return Uitkomst("bron", nr, "Regeling van één gemeente: blijft bron, geen element")


REGELS: list[Regel] = [
    Regel("0 Welk begrip", "`synoniem_van` ingevuld",
          "synoniem: geen pagina; het woord naar `synoniemen` van het element, met context",
          lambda k, e: bool(e.get("synoniem_van")),
          lambda k, e, nr: Uitkomst("synoniem", nr, "Ander woord voor een bestaand begrip",
                                    genoemd_begrip=e.get("synoniem_van"))),
    Regel("1 Scope", "niet *herkenbaar* of niet *gemeentelijk*", "buiten scope, met reden",
          lambda k, e: not (_ja(k, "herkenbaar") and _ja(k, "gemeentelijk")),
          lambda k, e, nr: Uitkomst("buiten_scope", nr, "Niet herkenbaar of niet gemeentelijk",
                                    redenen=[f"{NAAM[s]}: nee" for s in ("herkenbaar", "gemeentelijk") if not _ja(k, s)])),
    Regel("1 Scope", "*buiten dit model*", "buiten dit model, met het ArchiMate-type",
          lambda k, e: _ja(k, "buiten_dit_model"),
          lambda k, e, nr: Uitkomst("buiten_model", nr, "Buiten dit model", archimate_type=e.get("archimate_buiten_model"))),
    Regel("2 Afhankelijk", "*slechts eigenschap*", "eigenschap van het genoemde begrip; geen pagina",
          lambda k, e: _ja(k, "slechts_eigenschap"),
          lambda k, e, nr: Uitkomst("eigenschap", nr, "Eigenschap, status of indeling van een ander begrip",
                                    genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("2 Afhankelijk", "niet *eigen identiteit*", "onderdeel van het genoemde begrip; geen pagina, relaties naar het geheel",
          lambda k, e: not _ja(k, "eigen_identiteit"),
          lambda k, e, nr: Uitkomst("onderdeel", nr, "Onderdeel of deelstap van een ander begrip",
                                    genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("2 Afhankelijk", "niet *betekenis in onderwerp*",
          "verwijzing in de begrippenlijst; beoordelen in het onderwerp waar het hoort",
          lambda k, e: not _ja(k, "betekenis_in_onderwerp"),
          lambda k, e, nr: Uitkomst("verwijzing", nr, "Hoort bij een ander onderwerp")),
    Regel("3 Consistentie", "een kenmerk is ja dat niet bij de aard past (zie *alleen bij* per groep)",
          "conflict: voorleggen",
          lambda k, e: bool(_past_niet(k)),
          lambda k, e, nr: _conflict(nr, f"Past niet bij de aard: {_namen(_past_niet(k))}")),
    Regel("4 Type", "*handelende partij* en *hoedanigheid*", "*los van verantwoordelijkheid*: ja Actor, nee Rol",
          lambda k, e: _aard(k) == {"handelende_partij", "hoedanigheid"}, _partij),
    Regel("4 Type", "*samenwerkingsverband* (eventueel met *handelende partij*)",
          "*eigen rechtspersoon*: ja Actor, nee Bedrijfssamenwerking",
          lambda k, e: "samenwerkingsverband" in _aard(k) and _aard(k) <= {"samenwerkingsverband", "handelende_partij"},
          _samenwerking),
    Regel("4 Type", "andere combinatie van meer dan één aard", "conflict: voorleggen",
          lambda k, e: len(_aard(k)) > 1,
          lambda k, e, nr: _conflict(nr, f"Meer dan één aard: {_namen(sorted(_aard(k)))}")),
    Regel("4 Type", "*handelende partij*", "Actor; conflict als niet *los van verantwoordelijkheid*",
          lambda k, e: _aard(k) == {"handelende_partij"},
          lambda k, e, nr: _element(nr, "business-actor", "Handelende partij") if _ja(k, "los_van_verantwoordelijkheid")
          else _conflict(nr, "Handelende partij, maar niet los van de verantwoordelijkheid: mogelijk een rol")),
    Regel("4 Type", "*hoedanigheid*", "Rol; conflict als *los van verantwoordelijkheid*",
          lambda k, e: _aard(k) == {"hoedanigheid"},
          lambda k, e, nr: _element(nr, "business-role", "Hoedanigheid") if not _ja(k, "los_van_verantwoordelijkheid")
          else _conflict(nr, "Hoedanigheid, maar los van de verantwoordelijkheid: mogelijk een actor")),
    Regel("4 Type", "*aanbod als geheel*", "Product",
          lambda k, e: _aard(k) == {"aanbod_als_geheel"},
          lambda k, e, nr: _element(nr, "product", "Aanbod als geheel")),
    Regel("4 Type", "*toegangspunt*", "Kanaal: koppelen aan de centrale set; voorleggen",
          lambda k, e: _aard(k) == {"toegangspunt"}, _kanaal),
    Regel("4 Type", "*plaats*", "Locatie: geen pagina",
          lambda k, e: _aard(k) == {"plaats"},
          lambda k, e, nr: _element(nr, "location", "Fysieke plaats")),
    Regel("4 Type", "*regeling als geheel*", "*landelijk*: ja Beleidskader, nee bron (geen element)",
          lambda k, e: _aard(k) == {"regeling_als_geheel"}, _regeling),
    Regel("4 Type", "*gedrag* en precies één soort gedrag",
          "Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis of Dienst; *gezamenlijk gedrag*: Interaction, voorleggen",
          lambda k, e: _aard(k) == {"gedrag"} and len(_soorten(k)) == 1, _gedrag),
    Regel("4 Type", "*gedrag*, maar geen of meer dan één soort gedrag", "conflict: voorleggen",
          lambda k, e: _aard(k) == {"gedrag"},
          lambda k, e, nr: _conflict(nr, f"Soort gedrag niet eenduidig: {_namen(_soorten(k)) or 'geen'}")),
    Regel("4 Type", "geen aard, *waarneembare vorm*", "Representatie: geen pagina; vermelden bij het genoemde object",
          lambda k, e: _ja(k, "waarneembare_vorm"),
          lambda k, e, nr: _element(nr, "representation", "Waarneembare vorm", genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("4 Type", "geen aard, *afspraak*", "Afspraak (Contract)",
          lambda k, e: _ja(k, "afspraak"),
          lambda k, e, nr: _element(nr, "contract", "Passief, afspraak")),
    Regel("4 Type", "geen aard, overig", "Bedrijfsobject",
          lambda k, e: True,
          lambda k, e, nr: _element(nr, "business-object", "Passief")),
]
EERSTE_DREMPELREGEL = len(REGELS) + 1  # stap 5: kernrelatie; +1: overige drempel
EERSTE_SPECIALISATIEREGEL = EERSTE_DREMPELREGEL + 2

DREMPEL_REGELS = [
    ("5 Drempel", "kernrelatie van het type nee", "geen element: voorleggen met de ontbrekende relatie"),
    ("5 Drempel", f"meer dan {DREMPEL_ONTBREKEND} van de overige drempelcriteria nee",
     "geen element: voorleggen met de ontbrekende criteria"),
]
SPECIALISATIE = [
    ("6 Specialisatie", "niet *zelfstandige specialisatie*, met `genoemd_begrip`",
     "specialisatie zonder pagina; relaties naar het genoemde, bredere begrip"),
    ("6 Specialisatie", "niet *zelfstandige specialisatie*, zonder `genoemd_begrip`", "voorleggen: noem het bredere begrip"),
    ("6 Specialisatie", "anders", "element van het voorlopige type"),
]
NAREGELS = [
    ("Aanvulling", "`homoniem_van` ingevuld", "voorleggen: naamkeuze; `## Homoniemen` bij beide; bij een GGM-homoniem een terugmelding"),
    ("Aanvulling", "Actor of Rol met *onderscheidbare exemplaren*, *levenscyclus* en *wordt bewerkt*",
     "ook een bedrijfsobjectpagina (tegenhanger)"),
    ("Aanvulling", "Bedrijfsproces met *bijdrage aan groter proces*", "procesniveau deelproces, onder het genoemde bedrijfsproces"),
    ("Aanvulling", "*geautomatiseerd verwerkt*", "annotatie `data_object: ja`"),
    ("Signaal (controle)", "Dienst zonder realiserend proces of functie met pagina; Gebeurtenis zonder gestart gedrag met pagina",
     "waarschuwing: proces als kandidaat voorleggen"),
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


def _stap_0_tot_4(k: dict, extra: dict) -> Uitkomst:
    for nr, regel in enumerate(REGELS, start=1):
        if regel.test(k, extra):
            return regel.uitkomst(k, extra, nr)
    raise AssertionError("de laatste regel past altijd")


def _stap_5_en_6(u: Uitkomst, k: dict, extra: dict) -> Uitkomst:
    t = TYPE[(u.paginatype, u.archimate_type)]
    overig = list(t.drempel)
    ontbrekend = [s for s in overig if not _ja(k, s)]
    score = f"kern ja, {len(overig) - len(ontbrekend)}/{len(overig)}" if overig else "kern ja"
    if t.kern and not _ja(k, t.kern):
        return Uitkomst("geen_element", EERSTE_DREMPELREGEL, f"Kernrelatie ontbreekt voor {t.naam}",
                        archimate_type=u.archimate_type, voorleggen=True, typeregel=u.regel,
                        redenen=[f"{NAAM[t.kern]}: nee"] + [f"{NAAM[s]}: nee" for s in ontbrekend])
    if len(ontbrekend) > DREMPEL_ONTBREKEND:
        return Uitkomst("geen_element", EERSTE_DREMPELREGEL + 1, f"Drempel niet gehaald voor {t.naam} ({score})",
                        archimate_type=u.archimate_type, voorleggen=True, typeregel=u.regel,
                        redenen=[f"{NAAM[s]}: nee" for s in ontbrekend])
    if ontbrekend:
        score += f", ontbreekt: {_namen(ontbrekend)}"
    if not _ja(k, "zelfstandige_specialisatie"):
        if extra.get("genoemd_begrip"):
            return Uitkomst("specialisatie", EERSTE_SPECIALISATIEREGEL, f"Specialisatie zonder pagina ({score})",
                            archimate_type=u.archimate_type, genoemd_begrip=extra["genoemd_begrip"], typeregel=u.regel)
        return Uitkomst("geen_element", EERSTE_SPECIALISATIEREGEL + 1, f"Niet zelfstandig ({score})",
                        archimate_type=u.archimate_type, voorleggen=True, typeregel=u.regel,
                        redenen=["zelfstandige specialisatie: nee, maar het bredere begrip (genoemd_begrip) ontbreekt"])
    u2 = Uitkomst("element", EERSTE_SPECIALISATIEREGEL + 2, f"{u.toelichting} ({score})", paginatype=u.paginatype,
                  archimate_type=u.archimate_type, typeregel=u.regel, voorleggen=u.voorleggen, redenen=list(u.redenen))
    return u2


def evalueer(beoordeling: dict) -> Uitkomst:
    fouten = controleer(beoordeling)
    if fouten:
        raise BeoordelingFout(fouten)
    k = waarden(beoordeling)
    extra = {s: beoordeling.get(s) for s in EXTRA_VELDEN}
    uitkomst = _stap_0_tot_4(k, extra)
    if uitkomst.soort == "element":
        uitkomst = _stap_5_en_6(uitkomst, k, extra)

    if uitkomst.soort in ("eigenschap", "onderdeel", "geen_pagina") and uitkomst.archimate_type != "location" \
            and not extra.get("genoemd_begrip"):
        uitkomst.voorleggen = True
        uitkomst.redenen.append("genoemd begrip ontbreekt")
    if extra.get("homoniem_van") and uitkomst.soort not in ("synoniem",):
        uitkomst.voorleggen = True
        uitkomst.redenen.append(f"homoniem van {extra['homoniem_van']}: naamkeuze voorleggen")
    if uitkomst.paginatype in ("actor", "rol") and all(_ja(k, s) for s in TEGENHANGER):
        uitkomst.tegenhanger = "bedrijfsobject"
    if uitkomst.paginatype == "bedrijfsproces":
        uitkomst.procesniveau = "deelproces" if _ja(k, "bijdrage_aan_groter_proces") else "bedrijfsproces"
    if _ja(k, "geautomatiseerd_verwerkt"):
        uitkomst.data_object = "ja"
    return uitkomst


GRONDSLAGEN = ("ggm-entiteit", "ggm-afgeleid", "procesobject", "regelgeving", "bron")
REDEN_REGELGEVING = "grondslag regelgeving: altijd voorleggen"
REDEN_GEEN_GGM = "gegevensobject zonder sterke GGM-match"


def voor_te_leggen(uitkomst: Uitkomst | dict, ggm_match: str | None = None, grondslag: str | None = None) -> list[str]:
    """De redenen waarom de redacteur over dit begrip moet beslissen (leeg: de AI mag het zelf afhandelen)."""
    u = uitkomst if isinstance(uitkomst, dict) else asdict(uitkomst)
    redenen = list(u["redenen"]) or (["voorleggen"] if u["voorleggen"] else [])
    if u["soort"] == "element":
        if grondslag == "regelgeving":
            redenen.append(REDEN_REGELGEVING)
        if u["data_object"] == "ja" and ggm_match not in ("exact", "sterk"):
            redenen.append(REDEN_GEEN_GGM)
    return redenen


def open_redenen(redenen: list[str], besluiten: list[dict] | None) -> list[str]:
    """Redenen die geen besluit van de redacteur dekt. Een besluit dekt de redenen die het noemt."""
    gedekt = {r for b in besluiten or [] for r in b.get("redenen", [])}
    return [r for r in redenen if r not in gedekt]


def voorgestelde_status(uitkomst: Uitkomst | dict, ggm_match: str | None = None, grondslag: str | None = None,
                        besluiten: list[dict] | None = None) -> str | None:
    """`review` als niets meer voorgelegd hoeft te worden; `kandidaat` als er een reden open staat; `afgewezen` als
    het laatste besluit van de redacteur `afwijzen` is.

    Geen pagina (synoniem, bron, buiten scope, eigenschap, onderdeel, verwijzing, specialisatie, geen element,
    conflict, herkend, geen pagina) → None.
    """
    u = uitkomst if isinstance(uitkomst, dict) else asdict(uitkomst)
    if u["soort"] != "element":
        return None
    if besluiten and besluiten[-1].get("gevolg") == "afwijzen":
        return "afgewezen"
    if open_redenen(voor_te_leggen(u, ggm_match, grondslag), besluiten):
        return "kandidaat"
    return "review"


# --- Generatie: documentatie (criteria-skill, wikipagina) en het beoordeling-schema ---

CODE = {"T": "bepaalt het type", "x": "moet nee zijn voor dit type", "K": "kernrelatie: moet ja zijn",
        "D": "telt in de drempel (hoogstens één nee)", "P": "poort: geldt voor alle typen",
        "S": "specialisatieniveau", "A": "aanvulling (tegenhanger, procesniveau, annotatie)"}


def _codes() -> dict[str, dict[str, str]]:
    m = {s: {} for s in SLEUTELS}
    for i, t in enumerate(TYPEN):
        for km in KENMERKEN:
            if km.groep == "Poort":
                m[km.sleutel][i] = "P"
        if t.laag == "pagina":
            m["zelfstandige_specialisatie"][i] = "S"
        for s, w in t.bep.items():
            m[s][i] = "T" if w == "ja" else "x"
        if t.kern:
            m[t.kern][i] = "K"
        for s in t.drempel:
            m[s][i] = "D"
        for s in t.aanvulling:
            m[s].setdefault(i, "A")
    return m


def _cel(tekst: str) -> str:
    return tekst.replace("|", "\\|")


def doc_stap0() -> list[str]:
    return ["### Stap 0: welk begrip?", "",
            "Vóór de kenmerken: bepaal welk begrip bedoeld is. Synoniemen en homoniemen zijn geen kenmerken van een "
            "begrip, maar verhoudingen tussen een woord en een begrip.", "",
            "| Veld | Vraag | Uitkomst |", "|---|---|---|",
            "| `synoniem_van` | Is dit een ander woord voor een begrip dat al een element is, of in deze run wordt "
            "beoordeeld? Noem dat element en de context van het woord. | synoniem: geen pagina; het woord naar de "
            "synoniemen van het element |",
            "| `homoniem_van` | Bestaat dezelfde naam al voor een ander begrip, in de wiki, het GGM, het GEMMA-model of "
            "een bron? Noem dat begrip en waar het voorkomt. | door naar de kenmerken; naamkeuze voorleggen |", ""]


def doc_vragenlijst() -> list[str]:
    regels = ["### Kenmerken: vragenlijst in volgorde van beoordelen", "",
              "Beantwoord alle vragen, ook die niet bij de aard van het begrip passen (dan nee). Bij \"Noem …\" hoort bij "
              "ja een concreet begrip, artikel of relatie uit de bronnen; zonder zo'n verwijzing is het antwoord nee.", ""]
    nr = 0
    for groep in GROEPEN:
        regels += [f"**{groep}.** {GROEP_ALS[groep]}", ""]
        for km in (k for k in KENMERKEN if k.groep == groep):
            nr += 1
            regels.append(f"{nr}. {km.vraag} (*{km.naam}*)")
        regels.append("")
    return regels


def doc_naslag() -> list[str]:
    regels = ["### Kenmerken: naslag per groep", ""]
    for groep in GROEPEN:
        regels += [f"**{groep}.** {GROEP_ALS[groep]}", "", "| Kenmerk | Voorbeelden en herkomst |", "|---|---|"]
        regels += [f"| **{km.naam}**: {_cel(km.vraag)} | Ja: {_cel(km.ja)}. Nee: {_cel(km.nee)}. Herkomst: {_cel(km.herkomst)}. |"
                   for km in KENMERKEN if km.groep == groep]
        regels.append("")
    return regels


def doc_matrix() -> list[str]:
    m = _codes()
    kop = [t.kort for t in TYPEN]
    regels = ["### Beslistabel vanuit de kenmerken", "",
              "Per kenmerk: bij welke typen het telt, en hoe. "
              + " · ".join(f"**{c}** {t}" for c, t in CODE.items()) + ".", "",
              "Typen: " + " · ".join(f"{t.kort} = {t.naam}" + ("" if t.laag == "pagina" else f" ({t.laag})")
                                     for t in TYPEN) + ".", "",
              "| Kenmerk | " + " | ".join(kop) + " |", "|---|" + "---|" * len(kop)]
    for groep in GROEPEN:
        regels.append(f"| **{groep}** |" + " |" * len(kop))
        for km in (k for k in KENMERKEN if k.groep == groep):
            regels.append(f"| {km.naam} | " + " | ".join(m[km.sleutel].get(i, "") for i in range(len(TYPEN))) + " |")
    regels.append("")
    return regels


def doc_per_type() -> list[str]:
    regels = ["### Beslistabel per elementtype", "",
              "Voor elk type gelden eerst stap 0 en de poorten, daarna de toets op *zelfstandige specialisatie*. "
              f"Van de overige drempelcriteria mag er hoogstens {DREMPEL_ONTBREKEND} nee zijn.", ""]
    for t in TYPEN:
        kop = f"**Wanneer is iets een {t.naam.lower()}?**" + ("" if t.laag == "pagina" else f" ({t.laag})")
        regels += [kop, "", f"- Type volgt uit: {t.bepaald_door}."]
        if t.kern:
            regels.append(f"- Moet ja zijn: *{NAAM[t.kern]}*.")
        if t.drempel:
            regels.append(f"- Hoogstens één nee: {_namen(t.drempel)}.")
        if t.aanvulling:
            regels.append("- Daarna: " + "; ".join(dict.fromkeys(
                f"{v} ({_namen([s])})" if v != "tegenhanger" else "tegenhanger bij *onderscheidbare exemplaren*, "
                "*levenscyclus* en *wordt bewerkt*" for s, v in t.aanvulling.items())) + ".")
        if t.paginatype == "kanaal":
            regels.append("- Kanalen vormen één centrale set: koppelen aan een bestaand kanaal; een nieuw kanaal alleen na besluit van de redacteur.")
        regels += [f"- Voorbeeld: {t.voorbeeld}.", ""]
    return regels


def doc_stappen() -> list[str]:
    regels = ["### Stappentabel", "",
              "Stap 0–4 van boven naar beneden: de eerste passende regel beslist en levert het einde of een voorlopig "
              "type op. Een voorlopig type met een pagina gaat door naar stap 5 (drempel) en stap 6 (zelfstandige "
              "specialisatie). Daarna gelden de aanvullingen.", "",
              "| Nr | Stap | Als | Dan |", "|---|---|---|---|"]
    regels += [f"| {i} | {r.stap} | {_cel(r.als)} | {_cel(r.dan)} |" for i, r in enumerate(REGELS, start=1)]
    regels += [f"| {EERSTE_DREMPELREGEL + i} | {s} | {_cel(a)} | {_cel(d)} |" for i, (s, a, d) in enumerate(DREMPEL_REGELS)]
    regels += [f"| {EERSTE_SPECIALISATIEREGEL + i} | {s} | {_cel(a)} | {_cel(d)} |" for i, (s, a, d) in enumerate(SPECIALISATIE)]
    regels += [f"| — | {s} | {_cel(a)} | {_cel(d)} |" for s, a, d in NAREGELS]
    regels.append("")
    return regels


def markdown(doel: str = "skill") -> str:
    """De gegenereerde documentatie. `skill`: alles; `wiki`: zonder de stappentabel."""
    delen = doc_stap0() + doc_vragenlijst() + doc_naslag() + doc_per_type() + doc_matrix()
    if doel == "skill":
        delen += doc_stappen()
    return "\n".join(delen).rstrip("\n") + "\n"


BEGIN = "<!-- BEGIN gegenereerd uit de beslistabel; niet met de hand bewerken -->"
EINDE = "<!-- EINDE gegenereerd -->"


def vervang_blok(tekst: str, blok: str) -> str:
    patroon = re.compile(r"<!-- BEGIN gegenereerd[^>]*-->.*?<!-- EINDE gegenereerd -->", re.S)
    if not patroon.search(tekst):
        raise ValueError("geen gegenereerd blok gevonden")
    return patroon.sub(lambda _: f"{BEGIN}\n{blok}{EINDE}", tekst, count=1)


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
    tekst = {"type": "string", "minLength": 1}
    alineas = {"type": "array", "items": tekst, "description": "Alinea's; elke alinea op één regel"}
    id_ = {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}
    bron_ids = {"type": "array", "items": {"type": "string", "pattern": "^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*$"}}
    sterkte = {"enum": ["exact", "sterk", "partieel", "zwak", "geen"]}

    def obj(required: list[str], **props) -> dict:
        return {"type": "object", "required": required, "properties": props, "additionalProperties": False}

    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "beoordeling",
        "description": "Beoordeling van één begrip (beoordelingen/begrippen/<id>.yaml): het oordeel van de AI. "
                       "`status` en `afgeleid` vullen de scripts (tools/afleiden.py, llmwiki promote); nooit zelf "
                       "invullen. Gegenereerd door tools/bepaal_type.py schema.",
        "type": "object",
        "required": ["begrip", "onderwerpen", "kenmerken"],
        "properties": {
            "begrip": {**tekst, "description": "De naam: de gangbare term uit beleid en praktijk"},
            "onderwerpen": {"type": "array", "minItems": 1, "items": id_},
            "kenmerken": {
                "type": "object",
                "required": SLEUTELS,
                "properties": {s: {"$ref": "#/$defs/antwoord"} for s in SLEUTELS},
                "additionalProperties": False,
            },
            **{s: {"type": "string", "description": d} for s, d in EXTRA_VELDEN.items()},
            "toelichting": {**tekst, "description": "Waarom deze uitkomst, voor de begrippenlijst (vooral bij een "
                                                    "begrip zonder pagina)"},
            "definitie": {**tekst, "maxLength": 160, "not": {"pattern": "(?i)gelijk aan (het |de )?(ggm|gemma)"},
                          "description": "Herkenbare definitie: één zin, hoogstens 160 tekens; gaat naar GEMMA"},
            "definitie_formeel": {**tekst, "description": "Letterlijk uit de hoogst gerangschikte bron, alleen bij "
                                                          "een wezenlijk verschil"},
            "definitie_formeel_bron": obj(["bron", "plaats"], bron=tekst, plaats=tekst),
            "beschrijving": alineas,
            "per_onderwerp": {"type": "object", "propertyNames": {"pattern": id_["pattern"]},
                              "additionalProperties": alineas},
            "synoniemen": {"type": "array", "items": obj(["naam", "context"], naam=tekst, context=tekst)},
            "taakveld": tekst,
            "beleidsdomein": tekst,
            "grondslag": {"enum": list(GRONDSLAGEN)},
            "grondslag_toelichting": {**alineas, "description": "Bij regelgeving de juridische bron, bij "
                                                                "procesobject het proces, bij ggm-afgeleid de afleiding"},
            "ggm": obj(["sterkte", "onderbouwing"], guid={"type": "string", "pattern": "^EAID_"}, sterkte=sterkte,
                       onderbouwing=tekst,
                       duplicaten={"type": "array", "items": obj(["guid", "toelichting"],
                                                                 guid={"type": "string", "pattern": "^EAID_"},
                                                                 toelichting=tekst)}),
            "gemma": obj(["sterkte", "onderbouwing"], id=tekst, sterkte=sterkte, onderbouwing=tekst),
            "naamkeuze": alineas,
            "homoniemen": {"type": "array", "items": obj(["begrip", "betekenis", "waar", "naamkeuze"], begrip=tekst,
                                                         betekenis=tekst, waar=tekst, naamkeuze=tekst, element=id_)},
            "generalisatie": alineas,
            "specialisaties": {"type": "array", "items": obj(["naam", "omschrijving"], naam=tekst, omschrijving=tekst,
                                                             element=id_, ggm_guid=tekst, ggm_attribuut=tekst)},
            "ggm_componenten": {"type": "array", "items": obj(["naam", "guid", "toelichting"], naam=tekst,
                                                              guid={"type": "string", "pattern": "^EAID_"},
                                                              toelichting=tekst)},
            "tegenhanger": obj(["element", "toelichting"], element=id_, toelichting=tekst),
            "relaties": {"type": "array", "items": obj(
                ["soort", "naar", "grondslag"],
                soort={"type": "string", "pattern": r"^(associatie|associatie \(gericht\)|aggregatie|compositie|"
                                                    r"specialisatie|toewijzing|toegang \([a-zë-]+\)|triggering|"
                                                    r"stroom|realisatie|bediening)$"},
                naar=id_, naam=tekst, kardinaliteit=tekst, grondslag={"enum": ["ggm-exact", "ggm-afgeleid", "bron"]},
                ggm_relatie={"type": "array", "items": {"type": "string", "pattern": "^EAID_"}},
                bronnen=bron_ids, vindplaats=tekst)},
            "bronnen": {**bron_ids, "description": "Bronnen naast die in kenmerken en relaties, bijv. de algemene "
                                                   "bron van de beschrijving"},
            "vragen": {"type": "array", "items": tekst, "description": "Open vragen aan de redacteur"},
            "besluiten": {"type": "array", "items": obj(
                ["datum", "besluit", "gevolg"], datum={"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
                besluit=tekst, gevolg={"enum": ["opnemen", "afwijzen", "verwerkt"]},
                redenen={"type": "array", "items": tekst,
                         "description": "De voorgelegde redenen (uit afgeleid.voor_te_leggen) die dit besluit dekt"})},
            "status": {"enum": ["kandidaat", "review", "goedgekeurd", "afgewezen"],
                       "description": "Door tools/afleiden.py en llmwiki promote; niet zelf invullen"},
            "afgeleid": {"type": "object", "description": "Door tools/afleiden.py; niet zelf invullen"},
        },
        "additionalProperties": False,
        "$defs": {
            "antwoord": antwoord,
        },
    }


# --- CLI ---


def _beoordelingen(data: dict) -> list[tuple[str, dict]]:
    """Accepteert een assessment (voorstellen met `beoordeling`) of één beoordeling."""
    if "voorstellen" in data:
        return [(v.get("doel", "?"), v["beoordeling"]) for v in data["voorstellen"] if "beoordeling" in v]
    return [(data.get("begrip", "?"), data)]


def schrijf_documentatie() -> list[Path]:
    geschreven = []
    for pad, doel in ((SKILL_PATH, "skill"), (DOC_PATH, "wiki")):
        tekst = pad.read_text(encoding="utf-8")
        nieuw = vervang_blok(tekst, markdown(doel))
        if nieuw != tekst:
            pad.write_text(nieuw, encoding="utf-8", newline="\n")
            geschreven.append(pad)
    return geschreven


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_eval = sub.add_parser("evalueer", help="Pas de beslistabel toe op een assessment of beoordeling")
    p_eval.add_argument("bestand")
    p_eval.add_argument("--schrijf", action="store_true", help="Zet de uitkomst terug in het bestand (veld 'uitkomst')")
    p_status = sub.add_parser("status", help="Voorgestelde status voor een uitkomst")
    p_status.add_argument("--uitkomst", required=True)
    p_status.add_argument("--ggm-match")
    p_status.add_argument("--grondslag", choices=GRONDSLAGEN)
    p_md = sub.add_parser("markdown", help="Documentatie voor de criteria-skill en de wikipagina")
    p_md.add_argument("--schrijf", action="store_true", help="Werk de gegenereerde blokken in skill en wikipagina bij")
    p_md.add_argument("--doel", choices=["skill", "wiki"], default="skill")
    p_schema = sub.add_parser("schema", help="Beoordeling-schema")
    p_schema.add_argument("--schrijf", action="store_true", help=f"Schrijf naar {SCHEMA_PATH.relative_to(WIKI_ROOT)}")
    args = parser.parse_args(argv)

    if args.cmd == "markdown":
        if args.schrijf:
            for pad in schrijf_documentatie():
                print(f"Bijgewerkt: {pad.relative_to(WIKI_ROOT)}")
            return 0
        sys.stdout.write(markdown(args.doel))
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
