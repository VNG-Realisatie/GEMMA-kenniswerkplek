"""Bepaal het ArchiMate-elementtype van een begrip uit zijn keuzekenmerken en kenmerken.

Eén bron van waarheid voor de beslistabel van deze wiki, in vier fasen (Afbakenen, Typeren, Onderbouwen, Indelen) en
zeven stappen (0 tot en met 6):
- KENMERKEN: de ja/nee-kenmerken, met de vraag, een voorbeeld en de herkomst. Een *relatiekenmerk* (RELATIONEEL) beweert
  een relatie en noemt zijn tegenpartij in `naar`; een *toetskenmerk* hoort bij een type en moet ja zijn (een
  standaardantwoord, STANDAARD, hoeft niet te worden geschreven; alleen een afwijking staat in de beoordeling);
- KEUZEKENMERKEN: kenmerken met een waardenlijst, één waarde met onderbouwing en bron (*afhankelijkheid*,
  *procesniveau*, *interactievorm*), en de keuzevelden `vak`, `hoofdkenmerk` en `soort_gedrag`;
- VAKKEN: de ArchiMate-matrix (laag, aspect, intern of extern), met per vak de hoofdkenmerken en de soorten gedrag;
- TYPEN: per elementtype de toetskenmerken (stap 5);
- REGELS: stap 0 tot en met 3 van boven naar beneden (welk begrip, scope, afhankelijk, type en niveau); de eerste
  passende regel beslist en levert het einde of een voorlopig type op; daarna stap 5 (toetskenmerken) en stap 6
  (indeling: procesniveau en objectniveau, met de context van alle begrippen in `indeling`). Stap 4 (grondslag) doet
  tools/beslissen.py, want ze leest de brontypen van de bronnen.

Het model kiest de keuzekenmerken en beantwoordt de relatiekenmerken (`pad`: Typeren en Onderbouwen, met onderbouwing en
bron-id's, of bij een relatiekenmerk de tegenpartij in `naar`); een kenmerk in Afbakenen en Indelen alleen bij een
afwijking. Buiten het pad leidt deze tool het standaardantwoord af (meestal nee), en ze past de regels toe. De
elementtypen zelf (naam, ArchiMate-type, paginatype), hun eigenschappen en indelingen staan in het kennismodel
(tools/kennismodel.py). `schemas/beoordeling.schema.json` wordt hieruit gegenereerd (`schema --schrijf`); de vragen per
fase geeft `vragen`, en de matrix, de vragenlijst met voorbeelden en de stappentabel staan in
`kennismodel/kenmerken-en-beslistabel.md` (gegenereerd door tools/kennismodel.py). Een test bewaakt dat ze gelijk blijven.

Gebruik (vanuit de wikimap):
    uv run python tools/bepaal_type.py evalueer <assessment.json | beoordeling.json> [--schrijf]
    uv run python tools/bepaal_type.py vragen [<id>] [--type <paginatype>]   # de vragen voor de volgende fase
    uv run python tools/bepaal_type.py status --uitkomst <uitkomst.json> [--ggm-match sterk]
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

sys.path.insert(0, str(Path(__file__).resolve().parent))

import kennismodel as km  # noqa: E402
from kennismodel import AFNEMERS, DOELGROEPEN, DOMEINEN, REGELGEVERS, VERPLICHT, WAARDEN  # noqa: E402,F401

WIKI_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = WIKI_ROOT / "schemas" / "beoordeling.schema.json"
CRITERIA_VERSIE = "2026-10-18"


@dataclass(frozen=True)
class Kenmerk:
    sleutel: str
    naam: str
    groep: str
    vraag: str
    ja: str
    nee: str
    herkomst: str
    bij: frozenset | None = None  # hoofdkenmerken waarbij ja mag; None = altijd


def _bij(*aarden: str) -> frozenset:
    return frozenset(aarden)


GEDRAG_BIJ = _bij("gedrag")
OBJECT_BIJ = _bij("object", "afspraak")
KENMERKEN: list[Kenmerk] = [
    # Scope (stap 1, alleen een afwijking)
    Kenmerk("herkenbaar", "herkenbaar", "Scope",
            "Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam?",
            "het komt in wet, beleid of praktijk voor als zelfstandig begrip (Omgevingsvergunning)",
            "technisch hulpgegeven of constructie van de modelleur (volgnummer van een dossierregel)",
            "ArchiMate (concept in een domein); GEMMA (herkenbaar voor domeinexperts)"),
    Kenmerk("gemeentelijk", "gemeentelijk", "Scope",
            "Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij "
            "(opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)?",
            "de gemeente voert uit, beslist, stelt vast, of is structureel partner (GGD; behandelende arts via de overlegplicht met de lijkschouwer)",
            "alleen context (gedeputeerde staten als beroepsinstantie), of de interne zaak van een ketenpartner (de medische behandeling door de arts)",
            "GEMMA (gemeentelijk perspectief)"),
    Kenmerk("buiten_dit_model", "buiten dit model", "Scope",
            "Is het een doel, waarde, drijfveer, principe, losse norm of eis, opgave of thema, en geen beleidskader? "
            "Noem het ArchiMate-type.",
            "armoedebestrijding (doel); 'binnen acht weken beslissen' (norm uit één artikel)",
            "bijstandsuitkering; Wet op de lijkbezorging (beleidskader)",
            "ArchiMate (motivatie-, strategie- en overige lagen)"),
    Kenmerk("betekenis_in_onderwerp", "betekenis in onderwerp", "Scope",
            "Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij "
            "een ander onderwerp? Noem bij nee het onderwerp waar het thuishoort.",
            "Graf in lijkbezorging", "akte van overlijden in lijkbezorging (hoort bij de burgerlijke stand)",
            "GEMMA (betekenis binnen het onderwerp)"),
    # Hoofdkenmerk (keuzeveld `hoofdkenmerk`: één waarde)
    Kenmerk("gedrag", "gedrag", "Hoofdkenmerk",
            "Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling?",
            "aanvraag behandelen; verhuizing", "aanvraag", "ArchiMate (gedragselement)"),
    Kenmerk("handelende_partij", "handelende partij", "Hoofdkenmerk",
            "Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren?",
            "college van B&W; inwoner", "aanvrager", "GEMMA (definitie Actor)"),
    Kenmerk("hoedanigheid", "hoedanigheid", "Hoofdkenmerk",
            "Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de "
            "hoedanigheid waarin een partij optreedt?",
            "aanvrager; houder van de begraafplaats", "gemeenteraad", "ArchiMate (definitie Rol)"),
    Kenmerk("samenwerkingsverband", "samenwerkingsverband", "Hoofdkenmerk",
            "Is het een (ook tijdelijke) samenstelling van twee of meer partijen of rollen die samen gedrag uitvoeren?",
            "Zorg- en Veiligheidshuis; GGD (samenwerking van gemeenten)", "GGD-arts",
            "ArchiMate (definitie Bedrijfssamenwerking)"),
    Kenmerk("toegangspunt", "toegangspunt", "Hoofdkenmerk",
            "Is het een communicatiekanaal waarlangs een dienst beschikbaar komt?",
            "publieksbalie; gemeentelijke website", "klantcontact", "NORA (Kanalen)"),
    Kenmerk("plaats", "plaats", "Hoofdkenmerk",
            "Is het een fysieke plaats als zodanig, en geen gebiedsindeling als gegeven?",
            "stadskantoor als vestigingsplaats", "wijk (indeling)", "ArchiMate (Location)"),
    Kenmerk("aanbod_als_geheel", "aanbod als geheel", "Hoofdkenmerk",
            "Is het een gebundeld aanbod van diensten met bijbehorende afspraken, dat als geheel aan een afnemer "
            "wordt geleverd?",
            "bewonersparkeervergunning zoals de productencatalogus haar aanbiedt", "parkeren; één UPL-item als zodanig (een dienst)",
            "GEMMA (definitie Product)"),
    Kenmerk("regeling_als_geheel", "regeling als geheel", "Hoofdkenmerk",
            "Is het een concreet benoemde wet, AMvB, ministeriële regeling of verordening als geheel, en niet één "
            "artikel, een soort regeling of een richtlijn?",
            "Wet op de lijkbezorging; modelverordening participatie",
            "'verordening' als soort (bedrijfsobject Regeling); artikel 16 (losse norm); Circulaire adresonderzoek BRP "
            "(richtlijn, blijft bron)",
            "GEMMA (definitie Beleidskader)"),
    Kenmerk("vermogen", "vermogen", "Hoofdkenmerk",
            "Beschrijft het wat de gemeente moet kunnen om haar opgaven waar te maken, waarin zij investeert en wat met "
            "haar strategische opgaven verandert, los van hoe, door wie, in welke volgorde en met welk kanaal of "
            "systeem?",
            "Identiteit vaststellen", "Aanvraag controleren op volledigheid (te concreet: een processtap)",
            "GEMMA (definitie Capability); wiki (kader Capability, functie en proces)"),
    Kenmerk("object", "object", "Hoofdkenmerk",
            "Is het een ding waarover de gemeente gegevens vastlegt of dat zij verstrekt, en geen afspraak of "
            "waarneembare vorm van een ander begrip?",
            "Graf; Aanvraag; Vergunning", "aanslagbiljet (de vorm van Aanslag); subsidieovereenkomst (een afspraak)",
            "ArchiMate (Business Object)"),
    Kenmerk("afspraak", "afspraak", "Hoofdkenmerk",
            "Is het een overeenkomst tussen twee of meer partijen met rechten en plichten, en geen eenzijdig besluit "
            "of regeling?",
            "subsidieovereenkomst; uitvoeringsovereenkomst", "subsidiebeschikking; verordening",
            "GEMMA (definitie Afspraak)"),
    Kenmerk("representatie", "representatie", "Hoofdkenmerk",
            "Is het de vorm (document, formulier, register, bericht) waarin informatie van een ander begrip wordt "
            "vastgelegd of overgebracht? Noem dat begrip in `genoemd_begrip`.",
            "aanslagbiljet (van Aanslag); register van begraven lijken", "aanslag", "ArchiMate (Representation)"),
    # Soort gedrag (keuzeveld `soort_gedrag`, bij gedrag)
    Kenmerk("per_keer_doorlopen", "per keer doorlopen", "Soort gedrag",
            "Is het een proces: een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen, "
            "of een groepering van zulke processen naar soort werk (een cluster)?",
            "aanvraag omgevingsvergunning behandelen; Behandelen vergunningaanvragen lijkbezorging (cluster)",
            "vergunningverlening; Verzorgen lijkbezorging (een groepering naar taak is het beleidsdomein, geen proces)",
            "GEMMA (definitie Bedrijfsproces en Procescluster, regel 409 en 419-420; processenlandschap naar soort "
            "werk); wiki (geen taak)", GEDRAG_BIJ),
    Kenmerk("gegroepeerd_gedrag", "gegroepeerd gedrag", "Soort gedrag",
            "Is het een doorlopende groepering van werk dat de organisatie uitvoert, op grond van vergelijkbare "
            "middelen, kennis of competenties, zonder eigen volgorde of doorlooptijd? Wat de gemeente moet kunnen, "
            "strategisch, is een capability (vak strategie).",
            "vergunningverlening; belastingheffing", "aanslag opleggen (proces)", "GEMMA (definitie Bedrijfsfunctie)",
            GEDRAG_BIJ),
    Kenmerk("toestandsverandering", "toestandsverandering", "Soort gedrag",
            "Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat "
            "gevolgen heeft?",
            "verhuizing; aanvraag ontvangen; beslistermijn verstreken", "verhuizing doorgeven",
            "GEMMA (definitie Gebeurtenis)", GEDRAG_BIJ),
    Kenmerk("aangeboden_gedrag", "aangeboden gedrag", "Soort gedrag",
            "Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de "
            "behoefte van de afnemer en los van hoe zij wordt uitgevoerd?",
            "melding openbare ruimte doen", "melding afhandelen", "NORA (Dienstverlening)", GEDRAG_BIJ),
    Kenmerk("gezamenlijk_gedrag", "gezamenlijk gedrag", "Soort gedrag",
            "Kan het alleen door twee of meer partijen samen worden uitgevoerd, zoals een ketensamenwerking waarin de "
            "bedrijfsprocessen van de partijen samenkomen?",
            "Bezorgen stoffelijk overschot (ketensamenwerking van gemeente, arts en uitvaartondernemer); "
            "keukentafelgesprek", "beschikking opstellen; Treffen maatregel bij besmet lijk (de GGD adviseert alleen)",
            "ArchiMate (Business Interaction); GEMMA Online, Proceshiërarchie (ketensamenwerking als "
            "bedrijfsinteractie)", GEDRAG_BIJ),
    # Partij en regeling (stap 3)
    Kenmerk("los_van_verantwoordelijkheid", "los van verantwoordelijkheid", "Partij en regeling",
            "Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen?",
            "kerkgenootschap; burgemeester", "houder van de begraafplaats",
            "ArchiMate (actor tegenover rol)", _bij("handelende_partij", "hoedanigheid")),
    Kenmerk("eigen_rechtspersoon", "eigen rechtspersoon", "Partij en regeling",
            "Heeft het verband of de organisatie eigen rechtspersoonlijkheid (openbaar lichaam, stichting, "
            "vennootschap)?",
            "GGD (openbaar lichaam)", "Zorg- en Veiligheidshuis",
            "wiki (scheidslijn actor en bedrijfssamenwerking)",
            _bij("handelende_partij", "samenwerkingsverband")),
    Kenmerk("soort_partij", "soort partij", "Partij en regeling",
            "Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten "
            "geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk "
            "maar één keer bestaat.",
            "Gemeente; College van B&W; Kerkgenootschap; Rijk, Provincie en Waterschap (de bestuurslaag als "
            "geheel, ook al is er maar één Rijk)",
            "gemeente Utrecht, provincie Utrecht (één exemplaar, niet elke gemeente heeft ermee te maken); een "
            "afzonderlijk ministerie of rijksdienst (minister van BZK, IND) is geen eigen actor maar staat in de "
            "beschrijving van Rijk",
            "GEMMA (referentiemodel voor alle gemeenten); wiki (Rijk)",
            _bij("handelende_partij", "samenwerkingsverband")),
    Kenmerk("landelijk", "landelijk", "Partij en regeling",
            "Geldt het voor alle gemeenten: Europese regelgeving of rijksregelgeving (EU-verordening, wet, AMvB, "
            "ministeriële regeling) of een VNG-modelverordening van gemeentelijke regelgeving, en geen regeling of "
            "beleid van één gemeente?",
            "Wet op de lijkbezorging; AVG; modelverordening",
            "beheersverordening of beleidsnota van één gemeente (blijft bron)",
            "GEMMA (definitie Beleidskader); wiki", _bij("regeling_als_geheel")),
    # Toetskenmerken (stap 5): een relatiekenmerk (†) met zijn tegenpartij, of een standaardantwoord ja
    Kenmerk("toegewezen_partij", "toegewezen partij", "Toets",
            "Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? Noem de rol.",
            "Ruimen graf (Houder van de begraafplaats)", "draagvlak creëren",
            "ArchiMate (toewijzing van rol aan gedrag)", GEDRAG_BIJ),
    Kenmerk("aanleiding", "aanleiding", "Toets",
            "Start het door een aanwijsbare gebeurtenis, verzoek of termijn? Noem die.",
            "overheidsparticipatie (verzoek ingediend)", "kennisdeling",
            "ArchiMate (triggering); GEMMA (procesarchitectuur)", GEDRAG_BIJ),
    Kenmerk("benoembaar_resultaat", "benoembaar resultaat", "Toets",
            "Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: "
            "wat krijgt de afnemer? Noem het.",
            "opgraving (opgegraven lijk)", "informeren",
            "GEMMA (definities Bedrijfsproces en Product: resultaat, waarde voor de afnemer)",
            _bij("gedrag", "aanbod_als_geheel")),
    Kenmerk("omvat_processen", "omvat processen", "Toets",
            "Omvat het minstens twee bedrijfsprocessen van dezelfde soort werk? Noem ze.",
            "Behandelen vergunningaanvragen lijkbezorging (Verlenen verlof tot begraving of crematie, Opgraven "
            "stoffelijk overschot)", "een proces met één stap",
            "GEMMA (procescluster aggregeert bedrijfsprocessen, regel 419-420)", GEDRAG_BIJ),
    Kenmerk("bedient_gedrag", "bedient gedrag", "Toets",
            "Ondersteunt de functie aanwijsbaar een proces? Noem het.",
            "Exploiteren van begraafplaatsen bedient Ruimen graf", "functie zonder aanwijsbaar proces",
            "GEMMA (functie bedient proces, regel 597 en 604)", GEDRAG_BIJ),
    Kenmerk("gebruikt_objecten", "gebruikt objecten", "Toets",
            "Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag "
            "aanwijsbare bedrijfsobjecten? Noem object en handeling.",
            "Inspraak (registreert zienswijze)", "burgerberaad",
            "ArchiMate (toegang van gedrag tot object); wiki (handelingen)", GEDRAG_BIJ),
    Kenmerk("in_functie_indeling", "in functie-indeling", "Toets",
            "Heeft de functie een plaats in de Functie-indeling naar domein: onder een bovenliggende GEMMA-functie, of "
            "op domeinniveau onder het domein? Noem de bovenliggende functie of het domein.",
            "Exploiteren van begraafplaatsen (onder Exploitatie fysieke leefomgeving)", "Lijkbezorging als functie",
            "GEMMA (Functie-indeling naar domein)", GEDRAG_BIJ),
    Kenmerk("stabiel_over_tijd", "stabiel over tijd", "Toets",
            "Blijft het bestaan als de organisatie, de werkwijze of de systemen veranderen, en is het geen opgave met "
            "een einde?",
            "participatie; belastingheffing; Identiteit vaststellen",
            "projectteam Omgevingswet; invoering van de Omgevingswet (een opgave)",
            "ArchiMate en GEMMA (bedrijfsfunctiemodel); wiki (kader Capability)", _bij("gedrag", "vermogen")),
    Kenmerk("leidt_tot_gedrag", "leidt tot gedrag", "Toets",
            "Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? Noem het.",
            "Overlijden → Uitvoeren lijkbezorging", "voorval zonder gemeentelijk gevolg",
            "GEMMA (gebeurtenis triggert proces)", GEDRAG_BIJ),
    Kenmerk("komt_herhaald_voor", "komt herhaald voor", "Toets",
            "Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval?",
            "overlijden; aanvraag ontvangen", "invoeren van de participatieverordening",
            "GEMMA (gebeurtenis als herhaalbaar voorval)", GEDRAG_BIJ),
    Kenmerk("gerealiseerd_door", "gerealiseerd door", "Toets",
            "Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen "
            "realiseert? Noem ze.",
            "Onderhoud van graven (gerealiseerd door het proces dat graven onderhoudt); Personen registreren "
            "(Bevolkingsadministratie bijhouding, Burgerlijke stand diensten)",
            "dienst of vermogen zonder aanwijsbare uitvoering",
            "GEMMA (proces en functie realiseren dienst; functie realiseert capability)", _bij("gedrag", "vermogen")),
    Kenmerk("afnemer", "afnemer", "Toets",
            "Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? Noem die.",
            "melding openbare ruimte doen (inwoner)", "interne registratiestap",
            "NORA (Dienstverlening); GEMMA (definitie Product, rol Klant)", _bij("gedrag", "aanbod_als_geheel")),
    Kenmerk("omvat_diensten_en_afspraken", "omvat diensten en afspraken", "Toets",
            "Bestaat het aanbod uit aanwijsbare diensten en de afspraken die erbij horen? Noem ze.",
            "parkeervergunning (dienst parkeren, voorwaarden)", "losse dienst",
            "GEMMA (product bundelt dienst en afspraak)", _bij("aanbod_als_geheel")),
    Kenmerk("zelfstandig_aanbod", "zelfstandig aanbod", "Toets",
            "Wordt het onder een eigen naam aangeboden, en niet als variant of tarief van een ander product?",
            "bewonersparkeervergunning", "bezoekersparkeervergunning als tarief van parkeervergunning",
            "UPL (één naam per aanbod)", _bij("aanbod_als_geheel")),
    Kenmerk("wordt_bewerkt", "wordt bewerkt", "Toets",
            "Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of "
            "verstrekt, operationeel en niet alleen beleidsmatig? Noem het gedrag.",
            "aanvraag (geregistreerd, beoordeeld)", "preventieakkoord (alleen beleidsmatig)",
            "GEMMA (proces en functie benaderen bedrijfsobject)", OBJECT_BIJ),
    Kenmerk("onderscheidbare_exemplaren", "onderscheidbare exemplaren", "Toets",
            "Zijn de afzonderlijke exemplaren van elkaar te onderscheiden?",
            "aanvraag (elke aanvraag apart)", "gemeentefonds (er is er één)", "GEMMA (kan in meervoud bestaan)",
            OBJECT_BIJ),
    Kenmerk("levenscyclus", "levenscyclus", "Toets",
            "Ontstaan, veranderen en eindigen de exemplaren?",
            "vergunning (verleend, gewijzigd, ingetrokken)", "kadastrale gemeentecode", "GEMMA (eigen levenscyclus)",
            OBJECT_BIJ),
    Kenmerk("vervult_een_rol", "vervult een rol", "Toets",
            "Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? Noem de rol.",
            "kerkgenootschap vervult Houder van de begraafplaats", "partij die alleen genoemd wordt",
            "GEMMA (actor wordt toegewezen aan rol)", _bij("handelende_partij", "samenwerkingsverband")),
    Kenmerk("voert_gedrag_uit", "voert gedrag uit", "Toets",
            "Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? Noem het.",
            "Houder van de begraafplaats → Ruimen graf", "rol zonder aanwijsbaar gedrag",
            "GEMMA (rol wordt toegewezen aan functie); wiki (ook aan proces)",
            _bij("hoedanigheid", "samenwerkingsverband")),
    Kenmerk("ontsluit_een_dienst", "ontsluit een dienst", "Toets",
            "Komt via dit kanaal aanwijsbaar een gemeentelijke dienst beschikbaar? Noem de dienst.",
            "website → Melding openbare ruimte doen", "kanaal zonder aanwijsbare dienst",
            "GEMMA (kanaal wordt toegewezen aan dienst)", _bij("toegangspunt")),
    Kenmerk("is_grondslag_voor", "is grondslag voor", "Toets",
            "Geeft de regeling de gemeente een taak, bevoegdheid of plicht, of werkt de VNG-modelverordening die uit, "
            "in een aanwijsbaar proces, dienst of product? Noem het artikel of de paragraaf en het gedrag.",
            "Wet op de lijkbezorging art. 28 → Verlenen grafrecht", "BW boek 2, gebruikt voor één definitie",
            "GEMMA (beleidskader geeft grondslag; product heeft associatie met beleidskader)",
            _bij("regeling_als_geheel")),
    Kenmerk("in_werking", "in werking", "Toets",
            "Is de regeling geldend recht, of als modelverordening actueel?",
            "Archiefwet 1995", "ingetrokken wet", "wiki", _bij("regeling_als_geheel")),
    Kenmerk("beoordeelbaar", "beoordeelbaar", "Toets",
            "Kun je er volwassenheid of ontwikkelbehoefte van bepalen en er apart in investeren? Noem de "
            "investeringsvraag.",
            "Identiteit vaststellen (fraudebestrijding, biometrie)", "Dienstverlening (te breed)",
            "wiki (kader Capability: beoordeelbaar)", _bij("vermogen")),
    Kenmerk("onderscheidend", "onderscheidend", "Toets",
            "Is het af te grenzen van de andere capabilities, zonder dat een functie er voor een deel in valt? Noem de "
            "naaste capability.",
            "Personen registreren naast Identiteit vaststellen", "Burgers helpen naast Dienstverlening",
            "wiki (kader Capability: onderscheidend)", _bij("vermogen")),
    # Indeling (stap 6, alleen een afwijking)
    Kenmerk("generiek", "generiek", "Indeling",
            "Komt het met dezelfde betekenis in veel onderwerpen voor?",
            "Besluit; Beschikking; aanvraag ontvangen; Klant", "Graf; Ruimen graf",
            "wiki (abstractieniveau; GEMMA generieke elementen)"),
]

SLEUTELS = [k.sleutel for k in KENMERKEN]
NAAM = {k.sleutel: k.naam for k in KENMERKEN}
# Kenmerken die op de plek in een GEMMA-indeling kunnen steunen (`gemma_relatie`) in plaats van op een bron: de wiki
# volgt de indelingen van GEMMA, en het model is daar matchdoel (ARCHITECTURE.md, secties 4.4 en 6.4).
GEMMA_KENMERKEN = ("in_functie_indeling",)
KENMERK = {k.sleutel: k for k in KENMERKEN}
GROEPEN = list(dict.fromkeys(k.groep for k in KENMERKEN))
HOOFDKENMERK = [k.sleutel for k in KENMERKEN if k.groep == "Hoofdkenmerk"]
SOORT_GEDRAG = [k.sleutel for k in KENMERKEN if k.groep == "Soort gedrag"]
KEUZE = frozenset(HOOFDKENMERK) | frozenset(SOORT_GEDRAG)  # kenmerken die een keuzeveld zijn, niet in `kenmerken`


@dataclass(frozen=True)
class Keuzekenmerk:
    """Een kenmerk met een waardenlijst: precies één waarde, met een onderbouwing en bron, in `kenmerken`."""
    sleutel: str
    naam: str
    stap: int
    vraag: str
    waarden: tuple  # (waarde, criterium)
    standaard: str | None
    herkomst: str


KEUZEKENMERKEN: list[Keuzekenmerk] = [
    Keuzekenmerk("afhankelijkheid", "afhankelijkheid", 2,
                 "Is het begrip zelfstandig, of hangt het af van één ander begrip? Noem bij een afwijking dat begrip in "
                 "`genoemd_begrip`.",
                 (("zelfstandig", "eigen betekenis, eigen gegevens, regels of werkwijze (standaard)"),
                  ("eigenschap", "alleen een eigenschap, status, waarde, classificatie of indeling van het genoemde "
                                 "begrip, ook een doelgroep (bouwjaar van Pand; minima als indeling van Inwoner)"),
                  ("onderdeel", "onderdeel, deelstap of handeling van het genoemde begrip, zonder eigen bedrijfsproces, "
                                "dat ermee ontstaat en eindigt (grafbedekking van Graf; ondertekening van een besluit)"),
                  ("deelproces", "deel van het genoemde bedrijfsproces, niet klant tot klant: geen eigen aanleiding van "
                                 "buiten en geen eigen resultaat voor de klant (toetsen indieningsvereisten in behandelen "
                                 "aanvraag)"),
                  ("variant", "specialisatie van het genoemde begrip, van hetzelfde type, zonder eigen gegevens, regels "
                              "of werkwijze (vergunning tot opgraving naast Vergunning)"),
                  ("invoer_van_een_ander", "maakt en beheert een andere partij, de gemeente ontvangt of raadpleegt het "
                                           "alleen (verklaring van overlijden van de arts of lijkschouwer)")),
                 "zelfstandig", "GEMMA (eigen bestaan; negatieve toets: eigenschap, status, classificatie; "
                                "procesarchitectuur: processtap, handeling; zelfstandig ding waar beleid op gemaakt "
                                "wordt); wiki (abstractieniveau)"),
    Keuzekenmerk("procesniveau", "procesniveau", 3,
                 "Welk niveau heeft het proces in de procesindeling naar kernobject? Noem bij een levensloopproces of "
                 "bedrijfsproces het kernobject in `kernobject`.",
                 (("levensloopproces", "het gedrag over de hele levensloop van één exemplaar van het kernobject, van "
                                       "ontstaan tot einde, of binnen een ketensamenwerking het deel dat één partij uitvoert "
                                       "(Beheren grafrechten)"),
                  ("bedrijfsproces", "klant tot klant: begint bij een aanleiding van buiten het proces, loopt door tot "
                                     "het resultaat voor die klant, en doet een mutatie in de levensloop van het "
                                     "kernobject (Verlenen grafrecht)"),
                  ("cluster naar soort werk", "een groepering van bedrijfsprocessen van één soort werk, niet per geval "
                                              "doorlopen; `gemma_generiek` is verplicht (Behandelen vergunningaanvragen "
                                              "lijkbezorging)")),
                 None, "GEMMA Online, Proceshiërarchie (bedrijfsproces klant-tot-klant, PH 81; deelproces, PH 83; "
                       "cluster van bedrijfsprocessen over één thema, PH 91); wiki (levensloopproces; één per partij "
                       "binnen een ketensamenwerking)"),
    Keuzekenmerk("interactievorm", "interactievorm", 3,
                 "Hoe werken de partijen samen in de bedrijfsinteractie?",
                 (("estafette", "ketensamenwerking: elke partij is verantwoordelijk voor haar eigen deel (Bezorgen "
                                "stoffelijk overschot)"),
                  ("orkestratie", "één partij is verantwoordelijk voor het geheel; de gemeente levert een dienst aan "
                                  "derden (Beheren Nederlanderschap)")),
                 None, "GEMMA Online, Proceshiërarchie (ketensamenwerking als bedrijfsinteractie); ArchiMate "
                       "(Business Interaction)"),
]
KEUZEKENMERK = {k.sleutel: k for k in KEUZEKENMERKEN}
AFHANKELIJKHEID = [w for w, _ in KEUZEKENMERK["afhankelijkheid"].waarden]
PROCESNIVEAUS = [w for w, _ in KEUZEKENMERK["procesniveau"].waarden]
CLUSTER = "cluster naar soort werk"
INTERACTIEVORMEN = [w for w, _ in KEUZEKENMERK["interactievorm"].waarden]
for _k in KEUZEKENMERKEN:
    NAAM[_k.sleutel] = _k.naam

# Zonder antwoord geldt het standaardantwoord: de scope is doorlopen (stap 1), het begrip is zelfstandig (stap 2), een
# toetskenmerk dat geen relatie is, is ja (stap 5), en *generiek* is nee (stap 6). Elk ander kenmerk is nee. Alleen een
# afwijking staat in de beoordeling.
TOETS_STANDAARD_JA = ("benoembaar_resultaat", "afnemer", "stabiel_over_tijd", "komt_herhaald_voor", "zelfstandig_aanbod",
                      "onderscheidbare_exemplaren", "levenscyclus", "in_werking")
STANDAARD = {"herkenbaar": "ja", "gemeentelijk": "ja", "buiten_dit_model": "nee", "betekenis_in_onderwerp": "ja",
             "generiek": "nee", "afhankelijkheid": "zelfstandig", **{s: "ja" for s in TOETS_STANDAARD_JA}}
SCOPE = [k.sleutel for k in KENMERKEN if k.groep == "Scope"]
TOETS = [k.sleutel for k in KENMERKEN if k.groep == "Toets"]

GROEP_ALS = {
    "Scope": "Stap 1, alleen een afwijking: zonder antwoord is de scope doorlopen (*herkenbaar*, *gemeentelijk* en "
             "*betekenis in onderwerp* ja, *buiten dit model* nee), en steunt zij op de bronnen van de beoordeling. Het "
             "begrip valt af bij de eerste die afwijkt.",
    "Hoofdkenmerk": "Stap 3, het keuzeveld `hoofdkenmerk`: één waarde uit het vak; valt weg als het vak er maar één "
                    "heeft.",
    "Soort gedrag": "Stap 3, het keuzeveld `soort_gedrag`, alleen bij *gedrag*: één waarde uit het vak; valt weg bij "
                    "gedrag extern (*aangeboden gedrag*).",
    "Partij en regeling": "Stap 3, alleen bij *handelende partij*, *hoedanigheid* of *samenwerkingsverband* (*eigen "
                          "rechtspersoon* en *soort partij*; *los van verantwoordelijkheid* alleen als afwijking: het "
                          "volgt uit het hoofdkenmerk) en bij *regeling als geheel* (*landelijk*).",
    "Toets": "Stap 5: de toetskenmerken van het type (zie de tabel per type). Een relatiekenmerk (†) is altijd ja of nee, "
             "met de tegenpartij; de andere zijn standaard ja en staan alleen als nee in de beoordeling. Alle moeten ja "
             "zijn; een nee wordt voorgelegd.",
    "Indeling": "Stap 6, alleen een afwijking: zonder antwoord is een bedrijfsobject niet generiek.",
}

LAAGNAAM = {"bedrijf": "bedrijfslaag", "applicatie": "applicatielaag", "technologie": "technologielaag",
            "strategie": "strategielaag", "motivatie": "motivatie", "overig": "overig"}


@dataclass(frozen=True)
class Vak:
    """Een vak van de ArchiMate-matrix: laag, aspect en intern of extern, met de hoofdkenmerken en soorten gedrag."""
    sleutel: str
    laag: str
    aspect: str
    extern: bool | None  # None: het aspect kent geen intern en extern
    hoofdkenmerken: tuple
    soorten: tuple = ()

    @property
    def typen(self) -> str:
        """De elementtypen in het vak, uit het kennismodel."""
        return ", ".join([e.naam for e in km.ELEMENTTYPEN if e.vak == self.sleutel]
                         + [f"{z.naam} (geen pagina)" for z in km.ZONDER_ELEMENT if z.vak == self.sleutel])

    @property
    def label(self) -> str:
        delen = [LAAGNAAM[self.laag], self.aspect, {True: "extern", False: "intern"}.get(self.extern, "")]
        return ", ".join(d for d in delen if d)


VAKKEN: list[Vak] = [
    Vak("bedrijf/actief-intern", "bedrijf", "actief", False, ("handelende_partij", "hoedanigheid", "samenwerkingsverband")),
    Vak("bedrijf/actief-extern", "bedrijf", "actief", True, ("toegangspunt",)),
    Vak("bedrijf/gedrag-intern", "bedrijf", "gedrag", False, ("gedrag",),
        ("per_keer_doorlopen", "gegroepeerd_gedrag", "toestandsverandering", "gezamenlijk_gedrag")),
    Vak("bedrijf/gedrag-extern", "bedrijf", "gedrag", True, ("gedrag",), ("aangeboden_gedrag",)),
    Vak("bedrijf/passief", "bedrijf", "passief", None, ("object", "afspraak", "representatie")),
    Vak("bedrijf/samengesteld", "bedrijf", "samengesteld", None, ("aanbod_als_geheel",)),
    Vak("strategie/gedrag", "strategie", "gedrag", None, ("vermogen",)),
    Vak("motivatie", "motivatie", "", None, ("regeling_als_geheel",)),
    Vak("overig/samengesteld", "overig", "samengesteld", None, ("plaats",)),
]
VAK = {v.sleutel: v for v in VAKKEN}
KEUZEVELDEN = {
    "vak": "Stap 3, eerste keuze: het vak in de ArchiMate-matrix (laag, aspect, intern of extern)",
    "hoofdkenmerk": "Stap 3: het dominante kenmerk binnen het vak; alleen nodig als het vak er meer heeft",
    "soort_gedrag": "Stap 3, bij gedrag: de soort gedrag binnen het vak; alleen nodig als het vak er meer heeft",
}

# Relatiekenmerken: een ja/nee-kenmerk dat een relatie beweert (O3). Het kenmerk blijft de bewering en noemt zijn
# tegenpartij in `naar`: het id van een element, of naam en type van een element dat (nog) niet bestaat; het script vult het
# id als de relatie bestaat (tools/beoordeling.py normaliseer). Bestaat de relatie, dan steunt het kenmerk op haar bron;
# anders heeft het een eigen onderbouwing en bron. Per kenmerk: de richting vanuit het begrip (uit: de relatie staat in
# deze beoordeling; in: in die van de tegenpartij), de relatiesoorten en de typen van de tegenpartij (paginatypen; leeg:
# elk type).
RELATIONEEL = {
    "vervult_een_rol": ("uit", ("toewijzing",), ("rol",)),
    "voert_gedrag_uit": ("uit", ("toewijzing",), ("bedrijfsproces", "bedrijfsfunctie", "bedrijfsinteractie")),
    "ontsluit_een_dienst": ("uit", ("toewijzing",), ("dienst",)),
    "toegewezen_partij": ("in", ("toewijzing",), ("rol", "actor", "bedrijfssamenwerking")),
    "gebruikt_objecten": ("uit", ("toegang",), ("bedrijfsobject",)),
    "aanleiding": ("in", ("triggering",), ()),
    "gerealiseerd_door": ("in", ("realisatie",), ("bedrijfsproces", "bedrijfsfunctie")),
    "leidt_tot_gedrag": ("uit", ("triggering",), ("bedrijfsproces", "bedrijfsinteractie")),
    "omvat_processen": ("uit", ("aggregatie",), ("bedrijfsproces",)),
    "bedient_gedrag": ("uit", ("bediening",), ("bedrijfsproces",)),
    "in_functie_indeling": ("in", ("aggregatie",), ("bedrijfsfunctie",)),
    "wordt_bewerkt": ("in", ("toegang",), ("bedrijfsproces", "bedrijfsfunctie", "bedrijfsinteractie")),
    "omvat_diensten_en_afspraken": ("uit", ("aggregatie",), ("dienst", "bedrijfsobject")),
    "is_grondslag_voor": ("uit", ("associatie",), ()),
}
# Het kenmerk waarvan het script in stap 5 zijn relatie toetst bestaat niet: een kernrelatie is een relatiekenmerk onder
# de toetskenmerken van een type.


def hoofdkenmerk(beoordeling: dict) -> str | None:
    """Het hoofdkenmerk: het veld, of het enige hoofdkenmerk van het vak."""
    if beoordeling.get("hoofdkenmerk"):
        return beoordeling["hoofdkenmerk"]
    v = VAK.get(beoordeling.get("vak") or "")
    return v.hoofdkenmerken[0] if v and len(v.hoofdkenmerken) == 1 else None


def soort_gedrag(beoordeling: dict) -> str | None:
    """De soort gedrag: het veld, of de enige soort van het vak."""
    if beoordeling.get("soort_gedrag"):
        return beoordeling["soort_gedrag"]
    v = VAK.get(beoordeling.get("vak") or "")
    return v.soorten[0] if v and len(v.soorten) == 1 else None


def vak_bij(hoofd: str | None, soort: str | None = None) -> str | None:
    """Het vak waarin dit hoofdkenmerk (en deze soort gedrag) valt; None als dat niet eenduidig is."""
    kandidaten = [v.sleutel for v in VAKKEN if hoofd in v.hoofdkenmerken and (not v.soorten or soort in v.soorten)]
    return kandidaten[0] if len(kandidaten) == 1 else None


def _vak_conflict(beoordeling: dict) -> str | None:
    """Past het hoofdkenmerk of de soort gedrag niet bij het vak? (stap 3)"""
    v = VAK.get(beoordeling.get("vak") or "")
    if not v:
        return None
    hoofd, soort = hoofdkenmerk(beoordeling), soort_gedrag(beoordeling)
    if hoofd and hoofd not in v.hoofdkenmerken:
        return f"hoofdkenmerk *{NAAM.get(hoofd, hoofd)}* past niet bij het vak {v.label}"
    if soort and soort not in v.soorten:
        return f"soort gedrag *{NAAM[soort]}* past niet bij het vak {v.label}"
    return None


@dataclass(frozen=True)
class Typedef:
    paginatype: str | None
    archimate_type: str
    naam: str  # GEMMA-naam (uit het kennismodel)
    laag: str  # pagina | herkend | geen pagina
    bepaald_door: str
    bep: dict  # kenmerk → ja/nee (voor de documentatie)
    toets: tuple = ()  # de toetskenmerken (stap 5); een relatiekenmerk (RELATIONEEL) is een kernrelatie
    voorbeeld: str = ""
    kort: str = ""
    expliciet: tuple = ()  # toetskenmerken die altijd een antwoord nodig hebben, ook als ze een standaardantwoord kennen
    niveau: str | None = None  # procesniveau dat dit type kiest uit de typen met hetzelfde paginatype en ArchiMate-type


TYPEN: list[Typedef] = [
    Typedef(*km.typevelden("bedrijfsobject"), "pagina", "*object*", {"object": "ja"},
            ("wordt_bewerkt", "onderscheidbare_exemplaren", "levenscyclus"), "Graf; Aanvraag; Vergunning", "Obj"),
    Typedef(*km.typevelden("afspraak"), "pagina", "*afspraak*", {"afspraak": "ja"},
            ("wordt_bewerkt", "onderscheidbare_exemplaren", "levenscyclus"), "Uitvoeringsovereenkomst; Grafrecht",
            "Afspr"),
    Typedef(*km.typevelden("product"), "pagina", "*aanbod als geheel*", {"aanbod_als_geheel": "ja"},
            ("omvat_diensten_en_afspraken", "zelfstandig_aanbod", "afnemer", "benoembaar_resultaat"),
            "bewonersparkeervergunning in de productencatalogus", "Prod"),
    Typedef(*km.typevelden("dienst"), "pagina", "*gedrag* en *aangeboden gedrag*",
            {"gedrag": "ja", "aangeboden_gedrag": "ja"}, ("gerealiseerd_door", "afnemer", "benoembaar_resultaat"),
            "Onderhoud van graven", "Dienst"),
    Typedef(*km.typevelden("bedrijfsproces"), "pagina", "*gedrag* en *per keer doorlopen*",
            {"gedrag": "ja", "per_keer_doorlopen": "ja"}, ("toegewezen_partij", "aanleiding", "benoembaar_resultaat"),
            "Beheren grafrechten (levensloopproces); Verlenen grafrecht (bedrijfsproces)", "Proc"),
    Typedef(*km.typevelden("bedrijfsproces")[:2], "Procescluster", "pagina",
            "*gedrag* en *per keer doorlopen*, procesniveau *cluster naar soort werk*",
            {"gedrag": "ja", "per_keer_doorlopen": "ja"}, ("omvat_processen",),
            "Behandelen vergunningaanvragen lijkbezorging (cluster naar soort werk)", "Clus", niveau=CLUSTER),
    Typedef(*km.typevelden("bedrijfsfunctie"), "pagina", "*gedrag* en *gegroepeerd gedrag*",
            {"gedrag": "ja", "gegroepeerd_gedrag": "ja"},
            ("bedient_gedrag", "gebruikt_objecten", "in_functie_indeling", "stabiel_over_tijd"),
            "Exploiteren van begraafplaatsen; Burgerlijke stand diensten", "Func"),
    Typedef(*km.typevelden("gebeurtenis"), "pagina", "*gedrag* en *toestandsverandering*",
            {"gedrag": "ja", "toestandsverandering": "ja"}, ("leidt_tot_gedrag", "komt_herhaald_voor"),
            "Overlijden; Verval van het grafrecht", "Gebt"),
    Typedef(*km.typevelden("actor"), "pagina",
            "*handelende partij* met *los van verantwoordelijkheid*; of *samenwerkingsverband* met *eigen rechtspersoon*",
            {"handelende_partij": "ja", "los_van_verantwoordelijkheid": "ja", "samenwerkingsverband": "ja",
             "eigen_rechtspersoon": "ja"}, ("vervult_een_rol",), "College van B&W; Kerkgenootschap; GGD", "Actor"),
    Typedef(*km.typevelden("rol"), "pagina", "*hoedanigheid*, niet *los van verantwoordelijkheid*",
            {"hoedanigheid": "ja", "los_van_verantwoordelijkheid": "nee"}, ("voert_gedrag_uit",),
            "Houder van de begraafplaats; Rechthebbende op het graf", "Rol"),
    Typedef(*km.typevelden("bedrijfssamenwerking"), "pagina",
            "*samenwerkingsverband* zonder *eigen rechtspersoon*",
            {"samenwerkingsverband": "ja", "eigen_rechtspersoon": "nee"}, ("voert_gedrag_uit",),
            "Zorg- en Veiligheidshuis", "Samw"),
    Typedef(*km.typevelden("kanaal"), "pagina", "*toegangspunt*", {"toegangspunt": "ja"}, ("ontsluit_een_dienst",),
            "publieksbalie; gemeentelijke website (centrale set)", "Kan"),
    Typedef(*km.typevelden("beleidskader"), "pagina", "*regeling als geheel* en *landelijk*",
            {"regeling_als_geheel": "ja", "landelijk": "ja"}, ("is_grondslag_voor", "in_werking"),
            "Wet op de lijkbezorging; Archiefwet; AVG", "Bkad"),
    Typedef(*km.typevelden("bedrijfsinteractie"), "pagina",
            "*gedrag* en *gezamenlijk gedrag*", {"gedrag": "ja", "gezamenlijk_gedrag": "ja"},
            ("toegewezen_partij", "aanleiding", "benoembaar_resultaat"),
            "Bezorgen stoffelijk overschot (ketensamenwerking)", "Inter"),
    Typedef(*km.typevelden("capability"), "pagina", "*vermogen*", {"vermogen": "ja"},
            ("gerealiseerd_door", "beoordeelbaar", "onderscheidend", "stabiel_over_tijd"),
            "Identiteit vaststellen; Personen registreren", "Cap",
            expliciet=("beoordeelbaar", "onderscheidend", "stabiel_over_tijd")),
    Typedef(*km.typevelden("representatie"), "geen pagina", "*representatie*",
            {"representatie": "ja"}, (), "register van begraven lijken (vermelden bij Graf)", "Repr"),
    Typedef(*km.typevelden("locatie"), "geen pagina", "*plaats*", {"plaats": "ja"}, (),
            "stadskantoor als vestigingsplaats", "Loc"),
]


def typedef(paginatype: str | None, archimate_type: str, niveau: str | None = None) -> Typedef:
    """Het type bij een paginatype en ArchiMate-type; bij meer typen kiest het procesniveau (`niveau`)."""
    kandidaten = [t for t in TYPEN if (t.paginatype, t.archimate_type) == (paginatype, archimate_type)]
    for t in kandidaten:
        if t.niveau and t.niveau == niveau:
            return t
    return next(t for t in kandidaten if not t.niveau)


PAGINATYPEN = sorted({t.paginatype for t in TYPEN if t.paginatype})
GEDRAGSTYPE = {"per_keer_doorlopen": "business-process",
               "gegroepeerd_gedrag": "business-function",
               "toestandsverandering": "business-event", "aangeboden_gedrag": "business-service",
               "gezamenlijk_gedrag": "business-interaction"}

# Extra velden in een beoordeling (geen kenmerken): nodig bij bepaalde uitkomsten.
EXTRA_VELDEN = {
    "synoniem_van": "Stap 0: het element (of het begrip in deze run) waarvan dit woord een synoniem is",
    "homoniem_van": "Stap 0: het andere begrip met dezelfde naam, en waar het voorkomt (wiki, GGM, GEMMA-model, bron)",
    "genoemd_begrip": "Het begrip waarvan dit afhangt (eigenschap, onderdeel, deelproces, variant, invoer van een ander: "
                      "de naam van het begrip) of waarvan dit de representatie is",
    "archimate_buiten_model": "Het ArchiMate-type buiten dit model (Goal, Outcome, Principle, Requirement, Constraint, "
                              "Value, Capability, Grouping …)",
    "kernobject": "Stap 3 en 6: het bedrijfsobject waarvan dit proces de levensloop omvat (levensloopproces), waarin het "
                  "een mutatie doet (bedrijfsproces), of dat door de keten gaat (bedrijfsinteractie)",
}
# Indelingsvelden (AFNEMERS, DOMEINEN, DOELGROEPEN, REGELGEVERS, WAARDEN, VERPLICHT): zie het kennismodel.


def submap(data: dict, veld: str) -> str | None:
    """De waarde van een submap uit wiki.yaml `page_types.<type>.submappen`: een veld, of de groep in de
    Grondslagindeling."""
    return km.grondslaggroep(data) if veld == "grondslag" else data.get(veld)


def verplichte_velden(uitkomst: dict) -> tuple:
    """De indelingsvelden die bij deze uitkomst verplicht zijn; bij een proces hangt dat af van het procesniveau."""
    if uitkomst.get("paginatype") == "bedrijfsproces":
        return ("afnemer",) if uitkomst.get("procesniveau") in ("levensloopproces", "bedrijfsproces") else ()
    return VERPLICHT.get(uitkomst.get("paginatype"), ())


def ontbrekende_velden(beoordeling: dict, uitkomst: dict) -> list[str]:
    """De verplichte indelingsvelden die nog niet zijn ingevuld: een reden om voor te leggen, geen fout (regel Navragen)."""
    return [v for v in verplichte_velden(uitkomst) if not beoordeling.get(v)]


def controleer_indelingsvelden(beoordeling: dict, uitkomst: dict) -> list[str]:
    """Fouten in de waarden van de indelingsvelden."""
    fouten = []
    for veld, toegestaan in WAARDEN.items():
        if beoordeling.get(veld) and beoordeling[veld] not in toegestaan:
            fouten.append(f"'{veld}' is '{beoordeling[veld]}'; kies uit {', '.join(toegestaan)}")
    return fouten


@dataclass
class Uitkomst:
    # element | herkend | geen_pagina | synoniem | bron | buiten_scope | buiten_model | eigenschap | onderdeel
    # | verwijzing | specialisatie | geen_element | geen_grondslag | conflict
    soort: str
    regel: int
    toelichting: str
    paginatype: str | None = None
    archimate_type: str | None = None
    voorleggen: bool = False
    redenen: list[str] = field(default_factory=list)
    genoemd_begrip: str | None = None
    procesniveau: str | None = None
    objectniveau: str | None = None
    generiek: bool = False
    typeregel: int | None = None  # regel uit stap 3 die het voorlopige type gaf (bij uitkomsten van stap 5)


def _ja(k: dict, sleutel: str) -> bool:
    return k[sleutel] == "ja"


def _aard(k: dict) -> set[str]:
    """Het hoofdkenmerk als verzameling."""
    return {s for s in HOOFDKENMERK if _ja(k, s)}


def _soorten(k: dict) -> list[str]:
    return [s for s in SOORT_GEDRAG if _ja(k, s)]


def _namen(sleutels) -> str:
    return ", ".join(f"*{NAAM[s]}*" for s in sleutels)


def _past_niet(k: dict, e: dict) -> list[str]:
    """Kenmerken met een expliciet antwoord ja die niet bij het hoofdkenmerk van het begrip passen (stap 3)."""
    aard = _aard(k)
    return [km_.sleutel for km_ in KENMERKEN if km_.bij is not None and km_.sleutel in e.get("expliciet_ja", ())
            and not aard & km_.bij]


@dataclass(frozen=True)
class Regel:
    stap: str
    als: str
    dan: str
    test: Callable[[dict, dict], bool]
    uitkomst: Callable[[dict, dict, int], Uitkomst]


def _element(nr, archimate_type, toelichting, paginatype=None, **kw) -> Uitkomst:
    t = next(t for t in TYPEN if t.archimate_type == archimate_type and not t.niveau
             and (paginatype is None or t.paginatype == paginatype))
    soort = {"pagina": "element", "herkend": "herkend", "geen pagina": "geen_pagina"}[t.laag]
    u = Uitkomst(soort, nr, toelichting, paginatype=t.paginatype, archimate_type=archimate_type, **kw)
    if t.laag == "herkend":
        u.voorleggen = True
        u.redenen.append(f"{t.naam} heeft in deze wiki geen paginatype")
    return u


def _conflict(nr, reden) -> Uitkomst:
    return Uitkomst("conflict", nr, "Tegenstrijdige kenmerken", voorleggen=True, redenen=[reden])


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
    return Uitkomst("bron", nr, "Regeling of beleid van één gemeente: blijft bron, geen element")


def _afhankelijk(soort, toelichting, archimate_type=None):
    return lambda k, e, nr: Uitkomst(soort, nr, toelichting, archimate_type=archimate_type,
                                     genoemd_begrip=e.get("genoemd_begrip"))


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
    Regel("1 Scope", "niet *betekenis in onderwerp*",
          "verwijzing in de begrippenlijst; beoordelen in het onderwerp waar het hoort",
          lambda k, e: not _ja(k, "betekenis_in_onderwerp"),
          lambda k, e, nr: Uitkomst("verwijzing", nr, "Hoort bij een ander onderwerp")),
    Regel("2 Afhankelijk", "*afhankelijkheid* eigenschap", "eigenschap van het genoemde begrip; geen pagina",
          lambda k, e: k["afhankelijkheid"] == "eigenschap",
          _afhankelijk("eigenschap", "Eigenschap, status of indeling van een ander begrip")),
    Regel("2 Afhankelijk", "*afhankelijkheid* onderdeel",
          "onderdeel van het genoemde begrip; geen pagina, relaties naar het geheel; een bedrijfsobject dat kernobject is "
          "van een bedrijfsproces wordt in stap 6 een subobject",
          lambda k, e: k["afhankelijkheid"] == "onderdeel",
          _afhankelijk("onderdeel", "Onderdeel of deelstap van een ander begrip")),
    Regel("2 Afhankelijk", "*afhankelijkheid* deelproces",
          "deelproces of processtap van het genoemde bedrijfsproces; geen pagina, de tekst naar zijn `deelprocessen`",
          lambda k, e: k["afhankelijkheid"] == "deelproces",
          _afhankelijk("onderdeel", "Deelproces of processtap: een deel van een bedrijfsproces, niet klant tot klant",
                       "business-process")),
    Regel("2 Afhankelijk", "*afhankelijkheid* invoer van een ander",
          "onderdeel: geen pagina; vermelden bij het genoemde proces",
          lambda k, e: k["afhankelijkheid"] == "invoer_van_een_ander",
          _afhankelijk("onderdeel", "Invoer van een ander: de gemeente ontvangt of raadpleegt het alleen")),
    Regel("2 Afhankelijk", "*afhankelijkheid* variant",
          "specialisatie zonder pagina; relaties naar het genoemde, bredere begrip van hetzelfde type",
          lambda k, e: k["afhankelijkheid"] == "variant",
          _afhankelijk("specialisatie", "Specialisatie zonder pagina: een variant van een breder begrip")),
    Regel("3 Type en niveau", "het hoofdkenmerk of de soort gedrag past niet bij het vak, of een kenmerk is ja dat niet "
          "bij het hoofdkenmerk past (zie *alleen bij* per groep)", "conflict: voorleggen",
          lambda k, e: bool(e.get("vak_conflict") or _past_niet(k, e)),
          lambda k, e, nr: _conflict(nr, e.get("vak_conflict")
                                     or f"Past niet bij het hoofdkenmerk: {_namen(_past_niet(k, e))}")),
    Regel("3 Type en niveau", "*samenwerkingsverband*", "*eigen rechtspersoon*: ja Actor, nee Bedrijfssamenwerking",
          lambda k, e: _aard(k) == {"samenwerkingsverband"}, _samenwerking),
    Regel("3 Type en niveau", "*handelende partij*", "Actor; conflict als niet *los van verantwoordelijkheid*",
          lambda k, e: _aard(k) == {"handelende_partij"},
          lambda k, e, nr: _element(nr, "business-actor", "Handelende partij") if _ja(k, "los_van_verantwoordelijkheid")
          else _conflict(nr, "Handelende partij, maar niet los van de verantwoordelijkheid: mogelijk een rol")),
    Regel("3 Type en niveau", "*hoedanigheid*", "Rol; conflict als *los van verantwoordelijkheid*",
          lambda k, e: _aard(k) == {"hoedanigheid"},
          lambda k, e, nr: _element(nr, "business-role", "Hoedanigheid") if not _ja(k, "los_van_verantwoordelijkheid")
          else _conflict(nr, "Hoedanigheid, maar los van de verantwoordelijkheid: mogelijk een actor")),
    Regel("3 Type en niveau", "*aanbod als geheel*", "Product",
          lambda k, e: _aard(k) == {"aanbod_als_geheel"},
          lambda k, e, nr: _element(nr, "product", "Aanbod als geheel")),
    Regel("3 Type en niveau", "*toegangspunt*", "Kanaal: koppelen aan de centrale set; voorleggen",
          lambda k, e: _aard(k) == {"toegangspunt"}, _kanaal),
    Regel("3 Type en niveau", "*plaats*", "Locatie: geen pagina",
          lambda k, e: _aard(k) == {"plaats"},
          lambda k, e, nr: _element(nr, "location", "Fysieke plaats")),
    Regel("3 Type en niveau", "*regeling als geheel*", "*landelijk*: ja Beleidskader, nee bron (geen element)",
          lambda k, e: _aard(k) == {"regeling_als_geheel"}, _regeling),
    Regel("3 Type en niveau", "*vermogen*", "Capability",
          lambda k, e: _aard(k) == {"vermogen"},
          lambda k, e, nr: _element(nr, "capability", "Vermogen")),
    Regel("3 Type en niveau", "*gedrag*", "naar de soort gedrag: Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Dienst of "
          "Bedrijfsinteractie",
          lambda k, e: _aard(k) == {"gedrag"} and len(_soorten(k)) == 1, _gedrag),
    Regel("3 Type en niveau", "*representatie*", "Representatie: geen pagina; vermelden bij het genoemde object",
          lambda k, e: _ja(k, "representatie"),
          lambda k, e, nr: _element(nr, "representation", "Representatie", genoemd_begrip=e.get("genoemd_begrip"))),
    Regel("3 Type en niveau", "*afspraak*", "Afspraak (Contract)",
          lambda k, e: _ja(k, "afspraak"),
          lambda k, e, nr: _element(nr, "contract", "Passief, afspraak")),
    Regel("3 Type en niveau", "*object*", "Bedrijfsobject",
          lambda k, e: True,
          lambda k, e, nr: _element(nr, "business-object", "Passief, object")),
]
EERSTE_NIVEAUREGEL = len(REGELS) + 1  # stap 3, na het type: soort partij, procesniveau en interactievorm
EERSTE_TOETSREGEL = EERSTE_NIVEAUREGEL + 2  # stap 5
EERSTE_INDELINGSREGEL = EERSTE_TOETSREGEL + 1  # stap 6

NIVEAU_REGELS = [
    ("3 Type en niveau", "Actor of Bedrijfssamenwerking, niet *soort partij*",
     "geen element: voorleggen; het element geldt niet voor alle gemeenten"),
    ("3 Type en niveau", "Bedrijfsproces", "*procesniveau*: levensloopproces, bedrijfsproces of cluster naar soort werk; "
                                           "het cluster krijgt de toetskenmerken van een Procescluster"),
]
TOETS_REGELS = [
    ("5 Toetskenmerken", "een toetskenmerk van het type is nee, of een capability heeft minder dan twee functies",
     "geen element: voorleggen met de kenmerken die nee zijn"),
]
INDELING = [
    ("6 Indeling", "procesniveau cluster naar soort werk", "`gemma_generiek` verplicht, anders voorleggen: een taak is "
                                                          "geen procesniveau, de groepering naar taak is het "
                                                          "beleidsdomein"),
    ("6 Indeling", "procesniveau levensloopproces", "`kernobject` verplicht. Per kernobject één levensloopproces, met het "
                                                     "beleidsdomein van het kernobject; meer alleen als ze samen een "
                                                     "bedrijfsinteractie met dat kernobject bedienen, elk het deel van "
                                                     "één partij"),
    ("6 Indeling", "procesniveau bedrijfsproces", "`kernobject` verplicht; geaggregeerd door één levensloopproces"),
    ("6 Indeling", "bedrijfsinteractie", "`kernobject` verplicht; het beleidsdomein van het kernobject"),
    ("6 Indeling", "bedrijfsobject met *generiek*", "objectniveau generiek (thuis in een thematisch gedeeld onderwerp of "
                                                    "Kern)"),
    ("6 Indeling", "gebeurtenis, rol of dienst met *generiek*", "specialisatie van een generiek GEMMA-element (exacte "
                                                                  "match)"),
    ("6 Indeling", "bedrijfsobject dat `kernobject` is van een levensloopproces", "objectniveau kernobject; per kernobject "
                                                                                    "één levensloopproces, of één per partij "
                                                                                    "in een ketensamenwerking"),
    ("6 Indeling", "bedrijfsobject met *afhankelijkheid* onderdeel dat `kernobject` is van een bedrijfsproces",
     "objectniveau subobject (het script beoordeelt het dan als element)"),
    ("6 Indeling", "ander bedrijfsobject", "voorleggen: geen proces bepaalt zijn levensloop"),
]
NAREGELS = [
    ("Stap 4 Grondslag", "geen landelijke bron (`europese-regelgeving`, `rijksregelgeving`) bij een element, behalve een "
                         "UPL-dienst, een bedrijfsfunctie, een beleidskader en een capability die volgt wat zij omvat",
     "geen grondslag: stop. Een UPL-dienst zonder grondslag staat in de hoek zonder grondslag (tools/beslissen.py)"),
    ("Aanvulling", "`homoniem_van` ingevuld", "voorleggen: naamkeuze; `## Homoniemen` bij beide; bij een GGM-homoniem een terugmelding"),
    ("Aanvulling", "Bedrijfsobject, afspraak, rol, actor of gebeurtenis met een GGM-match, of met sterkte geen en een "
                   "GGM-terugmelding hiaat", "het data-object *<naam>-data* (tools/beslissen.py); `data_objecten` voor "
                   "een extra GGM-entiteit"),
    ("Signaal (controle)", "Dienst zonder realiserend proces of functie met pagina; Gebeurtenis zonder gestart gedrag met pagina",
     "waarschuwing: proces als kandidaat voorleggen"),
    ("Signaal (controle)", "Functie onder domeinniveau of dienst zonder (bovenliggende) functie, met meer "
     "(bovenliggende) functies, met een ander domein, of een functie buiten de GEMMA-functieketen; product onder een "
     "functie",
     "waarschuwing: de (bovenliggende) functie wordt een element met een aggregatie naar de functie of de dienst; een "
     "functie met GEMMA type *Bedrijfsfunctie domein* en een product hangen via `domein` aan de domeingroepering"),
    ("Signaal (controle)", "Product of dienst waarvan het domein niet past bij de GEMMA-domeinen van zijn beleidsdomein; "
     "een beleidsdomein dat GEMMA niet kent met producten en diensten in meer domeinen",
     "waarschuwing: domein of beleidsdomein herzien, of het verschil voorleggen als voorstel aan het GEMMA-team"),
]


class BeoordelingFout(ValueError):
    def __init__(self, fouten: list[str]):
        self.fouten = fouten
        super().__init__("; ".join(fouten))


# --- Het pad: de keuzekenmerken en kenmerken die de beslistabel voor dit begrip leest ---
#
# Afbakenen (stap 0 tot en met 2): de afwijkingen in de scope en de *afhankelijkheid*, met een stop als het begrip
# afvalt. Typeren (stap 3): de keuzevelden (vak, hoofdkenmerk, soort gedrag), de kenmerken van het hoofdkenmerk (*eigen
# rechtspersoon*, *soort partij*, *landelijk*) en de keuzekenmerken *procesniveau* en *interactievorm*. Onderbouwen
# (stap 5): de toetskenmerken van het type. Indelen (stap 6): *generiek*. Een kenmerk buiten het pad hoeft niet in de
# beoordeling: het script leidt het standaardantwoord af (STANDAARD, anders nee). Elk ander kenmerk op het pad staat er
# expliciet in, met een onderbouwing, of bij een relatiekenmerk met de tegenpartij in `naar`.

TYPEGROEP = (  # (hoofdkenmerken, kenmerken die een antwoord nodig hebben, kenmerken met alleen een afwijking)
    ({"handelende_partij"}, ("soort_partij",), ("los_van_verantwoordelijkheid",)),
    ({"hoedanigheid"}, (), ("los_van_verantwoordelijkheid",)),
    ({"samenwerkingsverband"}, ("eigen_rechtspersoon", "soort_partij"), ()),
    ({"regeling_als_geheel"}, ("landelijk",), ()),
)
ELK_ELEMENT = ("generiek",)


def antwoord(kenmerken: dict, sleutel: str) -> dict:
    """Het antwoord op een kenmerk als object; een ontbrekend kenmerk heeft het standaardantwoord (meestal nee)."""
    a = kenmerken.get(sleutel)
    return a if isinstance(a, dict) else {"waarde": STANDAARD.get(sleutel, None if sleutel in KEUZEKENMERK else "nee")}


def antwoorden(beoordeling: dict) -> dict[str, dict]:
    """De kenmerken die in de beoordeling staan, elk als object."""
    kenmerken = beoordeling.get("kenmerken") or {}
    return {s: antwoord(kenmerken, s) for s in kenmerken}


def regelvorm(beoordeling: dict) -> list[str]:
    """De kenmerken die nog in de schrijfvorm van één regel staan (`ja — onderbouwing [bron]`)."""
    return [s for s, a in (beoordeling.get("kenmerken") or {}).items() if isinstance(a, str)]


def naar_ids(a: dict) -> list[str]:
    """De tegenpartijen in `naar` die een element-id zijn (geen naam en type)."""
    return [x for x in a.get("naar") or [] if isinstance(x, str)]


def relaties_bij(bid: str, sleutel: str, ander: str, alle: dict[str, dict]) -> list[dict]:
    """De relaties die het relatiekenmerk `sleutel` van `bid` met tegenpartij `ander` uitwerken: in de richting en
    met een soort uit RELATIONEEL, in de beoordeling van `bid` (uit) of van `ander` (in)."""
    richting, soorten, _ = RELATIONEEL[sleutel]
    van, naar = (bid, ander) if richting == "uit" else (ander, bid)
    return [r for r in (alle.get(van) or {}).get("relaties") or []
            if r["naar"] == naar and r["soort"].split(" (")[0] in soorten]


def steunt_op_relatie(bid: str, sleutel: str, a: dict, alle: dict[str, dict]) -> bool:
    """Steunt het kenmerk op een relatie met een bron of een GEMMA-relatie (regel Elke claim een bron)?"""
    return any(r.get("bronnen") or r.get("gemma_relatie")
               for ander in naar_ids(a) for r in relaties_bij(bid, sleutel, ander, alle))


# Kenmerken van een capability die op een oordeel met onderbouwing steunen als er geen landelijke richtlijn is (K6)
ORDEEL_ZONDER_BRON = ("beoordeelbaar", "onderscheidend")
MIN_FUNCTIES_CAPABILITY = 2  # K3: een capability is een element als ten minste twee bedrijfsfuncties haar realiseren


def _realiserende_functies(beoordeling: dict) -> int:
    """Het aantal tegenpartijen van *gerealiseerd door*: een element-id, of een nog niet bestaande bedrijfsfunctie
    (naam en type). Of een id een bedrijfsfunctie is, volgt uit de relatie (tools/beslissen.py)."""
    a = antwoord(beoordeling.get("kenmerken") or {}, "gerealiseerd_door")
    return sum(1 for x in a.get("naar") or [] if isinstance(x, str) or x.get("type") == "bedrijfsfunctie")


def extra_velden(beoordeling: dict) -> dict:
    extra = {s: beoordeling.get(s) for s in EXTRA_VELDEN}
    extra["soort_werk_van"] = (beoordeling.get("gemma_generiek") or {}).get("id")
    extra["vak_conflict"] = _vak_conflict(beoordeling)
    extra["realiserende_functies"] = _realiserende_functies(beoordeling)
    extra["expliciet_ja"] = frozenset(s for s, a in antwoorden(beoordeling).items() if a["waarde"] == "ja")
    return extra


def _scope(k: dict, extra: dict) -> list[str]:
    """De scope tot en met de stop; *herkenbaar* en *gemeentelijk* altijd samen (samen de reden van buiten scope)."""
    if extra.get("synoniem_van"):
        return []
    pad = ["herkenbaar", "gemeentelijk"]
    if not (_ja(k, "herkenbaar") and _ja(k, "gemeentelijk")):
        return pad
    for sleutel, stop in (("buiten_dit_model", "ja"), ("betekenis_in_onderwerp", "nee")):
        pad.append(sleutel)
        if k[sleutel] == stop:
            return pad
    return pad


def voorbij_afbakenen(k: dict, extra: dict) -> bool:
    """Is het begrip een eigen element-kandidaat: geen synoniem, binnen de scope en zelfstandig (stap 0 tot en met 2)?"""
    return not extra.get("synoniem_van") and len(_scope(k, extra)) == len(SCOPE) \
        and k["betekenis_in_onderwerp"] == "ja" and k["afhankelijkheid"] == "zelfstandig"


voorbij_poort = voorbij_afbakenen  # de oude naam


def typeren(k: dict, extra: dict) -> list[str]:
    """De kenmerken van Typeren die naast de keuzevelden horen bij dit hoofdkenmerk."""
    aard = _aard(k)
    uit: list[str] = []
    for aarden, nodig, afwijking in TYPEGROEP:
        if aard & aarden:
            uit += [s for s in (*nodig, *afwijking) if s not in uit]
    return uit


def open_keuzevelden(beoordeling: dict) -> list[str]:
    """De keuzevelden van Typeren die nodig zijn maar ontbreken: het vak, het hoofdkenmerk als het vak er meer heeft, de
    soort gedrag bij gedrag. Een begrip dat in Afbakenen afvalt, heeft ze niet nodig."""
    if not voorbij_afbakenen(waarden(beoordeling), extra_velden(beoordeling)):
        return []
    uit = [] if beoordeling.get("vak") else ["vak"]
    hoofd = hoofdkenmerk(beoordeling)
    if not hoofd:
        uit.append("hoofdkenmerk")
    if hoofd == "gedrag" and not soort_gedrag(beoordeling):
        uit.append("soort_gedrag")
    return uit


def fase_b_type(t: Typedef) -> list[str]:
    """De kenmerken van een type met een pagina: de toetskenmerken en de afwijking van stap 6."""
    return list(dict.fromkeys((*t.toets, *ELK_ELEMENT)))


def pad(k: dict, extra: dict) -> tuple[list[str], list[str]]:
    """(Afbakenen en Typeren, Onderbouwen en Indelen): de kenmerken die de beslistabel leest, bij deze waarden; ook de
    keuzekenmerken *afhankelijkheid*, *procesniveau* en *interactievorm*."""
    a = [*_scope(k, extra), *(["afhankelijkheid"] if not extra.get("synoniem_van") else [])]
    if not voorbij_afbakenen(k, extra):
        return a, []
    a = a + typeren(k, extra)
    u = _stap_0_tot_3(k, extra)
    if u.soort != "element":  # afgevallen, of een type zonder pagina: geen Onderbouwen
        return a, []
    t = typedef(u.paginatype, u.archimate_type, k.get("procesniveau"))
    sleutel = {"bedrijfsproces": "procesniveau", "bedrijfsinteractie": "interactievorm"}.get(u.paginatype)
    if sleutel and (k.get(sleutel) or all(_ja(k, s) for s in t.toets)):  # zonder keuze eerst de toets van het type
        a.append(sleutel)
    return a, fase_b_type(t)


AFWIJKING = ("los_van_verantwoordelijkheid",)  # het standaardantwoord volgt uit het hoofdkenmerk: alleen een afwijking


def te_beantwoorden(sleutels, expliciet=()) -> list[str]:
    """De kenmerken die een antwoord nodig hebben: die zonder standaardantwoord, en de expliciete van het type."""
    return [s for s in sleutels if (s not in STANDAARD and s not in AFWIJKING) or s in expliciet]


def _expliciet(k: dict, extra: dict) -> tuple:
    u = _stap_0_tot_3(k, extra)
    if u.soort != "element":
        return ()
    return typedef(u.paginatype, u.archimate_type, k.get("procesniveau")).expliciet


GROEPLABEL = {"handelende_partij": "Alleen bij handelende partij of hoedanigheid",
              "samenwerkingsverband": "Alleen bij samenwerkingsverband",
              "regeling_als_geheel": "Alleen bij regeling als geheel"}
SCHRIJFVORM = ("Schrijf de keuzevelden bovenaan (`vak:`, `hoofdkenmerk:`, `soort_gedrag:`). Schrijf per kenmerk één regel "
               "onder `kenmerken:`: `sleutel: ja — onderbouwing [bron-id, …]` (een plek in een GEMMA-indeling: "
               "`[id-…]`, het id van de GEMMA-relatie); een nee: `sleutel: nee — onderbouwing`; een keuzekenmerk: "
               "`afhankelijkheid: variant — onderbouwing [bron-id]`; tussen aanhalingstekens als de tekst `: ` of ` #` "
               "bevat. Een relatiekenmerk (†) met ja noemt zijn tegenpartij: `sleutel: {waarde: ja, naar: [<id>]}` als de "
               "relatie er is (die draagt de bron; `tools/beoordeling.py normaliseer` vult het id), anders met "
               "onderbouwing en bronnen en in `naar` de naam en het type (`{naam: …, type: <paginatype>}`). Een "
               "kenmerk in Afbakenen en Indelen alleen bij een afwijking, een toetskenmerk dat geen relatie is alleen "
               "bij een nee. Daarna: tools/beoordeling.py normaliseer <id>.")
AFBAKENEN = ("Afbakenen (stap 1 en 2), alleen een afwijking: zonder antwoord is de scope doorlopen en het begrip zelfstandig, "
             "en steunt zij op de bronnen van de beoordeling. Het begrip valt af bij de eerste die afwijkt (herkenbaar of "
             "gemeentelijk nee; buiten dit model ja; betekenis in onderwerp nee), daarna bij *afhankelijkheid*; noem de "
             "afwijking met onderbouwing en bron.")


def _vraagregel(sleutel: str) -> str:
    k = KENMERK[sleutel]
    teken = " †" if sleutel in RELATIONEEL else ""
    standaard = " (standaard ja)" if STANDAARD.get(sleutel) == "ja" else ""
    return f"- `{sleutel}`{teken}{standaard}: {k.vraag} Ja: {k.ja}. Nee: {k.nee}."


def _keuzeregels(sleutel: str) -> list[str]:
    k = KEUZEKENMERK[sleutel]
    return [f"- `{sleutel}`: {k.vraag}", *(f"  - `{w}`: {c}" for w, c in k.waarden)]


def _vakregel(v: Vak) -> str:
    if len(v.hoofdkenmerken) == 1:
        k = KENMERK[v.hoofdkenmerken[0]]
        return f"- `{v.sleutel}` ({v.label}; {v.typen}): {k.vraag} Ja: {k.ja}. Nee: {k.nee}."
    if v.hoofdkenmerken[0] == "object":
        return f"- `{v.sleutel}` ({v.label}; {v.typen}): een ding; kies het hoofdkenmerk object, afspraak of representatie."
    return f"- `{v.sleutel}` ({v.label}; {v.typen}): een partij; kies het hoofdkenmerk."


def type_van(paginatype: str) -> Typedef:
    """Het type bij een paginatype; `procescluster` is het bedrijfsproces met procesniveau cluster."""
    if paginatype == "procescluster":
        return next(t for t in TYPEN if t.niveau == CLUSTER)
    for t in TYPEN:
        if t.paginatype == paginatype and not t.niveau:
            return t
    raise ValueError(f"onbekend paginatype '{paginatype}'; kies uit {', '.join(PAGINATYPEN)} of procescluster")


def vragen(beoordeling: dict | None = None, paginatype: str | None = None) -> list[str]:
    """De vragen voor de volgende fase: de keuzevelden en de kenmerken op het pad die nog niet beantwoord zijn, met de
    voorbeelden. Afbakenen en Typeren zolang een keuzeveld of een kenmerk van het hoofdkenmerk open is, daarna
    Onderbouwen voor het type."""
    if paginatype:
        t = type_van(paginatype)
        return [f"Onderbouwen, {t.naam}: de toetskenmerken van het type; een relatiekenmerk (†) met de tegenpartij, de "
                "andere standaard ja (alleen een nee schrijven).",
                *map(_vraagregel, fase_b_type(t)), "", SCHRIJFVORM]
    beoordeling = beoordeling or {}
    kenmerken = beoordeling.get("kenmerken") or {}
    extra = extra_velden(beoordeling)
    if extra.get("synoniem_van"):
        return ["Synoniem (stap 0): geen kenmerken."]
    open_ = lambda sleutels, expliciet=(): [s for s in te_beantwoorden(sleutels, expliciet) if s not in kenmerken]  # noqa: E731
    k = waarden(beoordeling)
    a, b = pad(k, extra)
    velden = open_keuzevelden(beoordeling)
    if velden:
        intern = VAK["bedrijf/actief-intern"].hoofdkenmerken
        uit = [AFBAKENEN, *map(_vraagregel, SCOPE), "", *_keuzeregels("afhankelijkheid"), "",
               "Typeren (stap 3). Vak (`vak`): de eerste keuze, het vak in de ArchiMate-matrix.", *map(_vakregel, VAKKEN), "",
               "Hoofdkenmerk (`hoofdkenmerk`): alleen bij `bedrijf/actief-intern` en `bedrijf/passief`, één van:",
               *map(_vraagregel, (*intern, "object", "afspraak", "representatie")), "",
               "Soort gedrag (`soort_gedrag`): alleen bij `bedrijf/gedrag-intern`, één van (bij `bedrijf/gedrag-extern` "
               "is het *aangeboden gedrag*):", *map(_vraagregel, VAK["bedrijf/gedrag-intern"].soorten)]
        aard = _aard(k)
        for aarden, nodig, afwijking in TYPEGROEP:
            if open_(nodig) and (not hoofdkenmerk(beoordeling) or aard & aarden):
                uit += ["", GROEPLABEL.get(min(aarden), "Alleen bij hoedanigheid") + ":", *map(_vraagregel, open_(nodig))]
        return uit + ["", "Bij een bedrijfsproces: `procesniveau`; bij een bedrijfsinteractie: `interactievorm`.",
                      *_keuzeregels("procesniveau"), *_keuzeregels("interactievorm"), "", SCHRIJFVORM]
    if open_(a):
        return ["Typeren, de kenmerken van het hoofdkenmerk en de keuzekenmerken:",
                *[r for s in open_(a) for r in (_keuzeregels(s) if s in KEUZEKENMERK else [_vraagregel(s)])],
                "", SCHRIJFVORM]
    u = _stap_0_tot_3(k, extra)
    if not b:
        return [f"Geen Onderbouwen: uitkomst {u.soort} (regel {u.regel}). Draai tools/beslissen.py."]
    t = typedef(u.paginatype, u.archimate_type, k.get("procesniveau"))
    if not open_(b, t.expliciet):
        return [f"Alle kenmerken op het pad van {t.naam} zijn beantwoord. Draai tools/beslissen.py."]
    return [f"Onderbouwen, {t.naam}: de toetskenmerken van het type; een relatiekenmerk (†) met de tegenpartij, de "
            "andere standaard ja (alleen een nee schrijven).",
            *map(_vraagregel, open_(b, t.expliciet)), "", SCHRIJFVORM]


def controleer(beoordeling: dict) -> list[str]:
    """Structurele controle van een beoordeling (aanvullend op het JSON-schema), en het pad: de keuzevelden zijn
    ingevuld, en elk kenmerk op het pad zonder standaardantwoord staat er expliciet in, met een onderbouwing of (bij een
    relatiekenmerk met ja) een tegenpartij in `naar`."""
    fouten = []
    kenmerken = beoordeling.get("kenmerken") or {}
    for sleutel, a in kenmerken.items():
        if sleutel not in NAAM:
            fouten.append(f"onbekend kenmerk '{sleutel}'")
        elif sleutel in KEUZE:
            veld = "soort_gedrag" if sleutel in SOORT_GEDRAG else "hoofdkenmerk"
            fouten.append(f"'{NAAM[sleutel]}' is geen kenmerk meer maar een keuze: zet het in `{veld}`")
        elif isinstance(a, str):
            fouten.append(f"kenmerk '{NAAM[sleutel]}' staat in de schrijfvorm van één regel; draai "
                          "tools/beoordeling.py normaliseer")
        elif sleutel in KEUZEKENMERK:
            waarden_ = [w for w, _ in KEUZEKENMERK[sleutel].waarden]
            if not isinstance(a, dict) or a.get("waarde") not in waarden_:
                fouten.append(f"keuzekenmerk '{NAAM[sleutel]}': waarde moet {', '.join(waarden_)} zijn")
            elif a["waarde"] != KEUZEKENMERK[sleutel].standaard and not str(a.get("onderbouwing", "")).strip():
                fouten.append(f"keuzekenmerk '{NAAM[sleutel]}': onderbouwing ontbreekt")
            elif a.get("naar"):
                fouten.append(f"keuzekenmerk '{NAAM[sleutel]}': `naar` alleen bij een relatiekenmerk")
        elif not isinstance(a, dict) or a.get("waarde") not in ("ja", "nee"):
            fouten.append(f"kenmerk '{NAAM[sleutel]}': waarde moet 'ja' of 'nee' zijn")
        elif a.get("naar") and sleutel not in RELATIONEEL:
            fouten.append(f"kenmerk '{NAAM[sleutel]}': `naar` alleen bij een relatiekenmerk")
        elif a.get("naar") and a["waarde"] != "ja":
            fouten.append(f"kenmerk '{NAAM[sleutel]}': `naar` alleen bij ja")
        elif not str(a.get("onderbouwing", "")).strip() and not (a.get("naar") and len(naar_ids(a)) == len(a["naar"])):
            fouten.append(f"kenmerk '{NAAM[sleutel]}': onderbouwing ontbreekt" + (
                " (een tegenpartij met naam en type heeft een onderbouwing en bron)" if a.get("naar") else ""))
    if fouten:
        return fouten
    k, extra = waarden(beoordeling), extra_velden(beoordeling)
    for veld in open_keuzevelden(beoordeling):
        fouten.append(f"keuzeveld `{veld}` ontbreekt (tools/bepaal_type.py vragen)")
    a, b = pad(k, extra)
    ontbrekend = [s for s in te_beantwoorden(a + b, _expliciet(k, extra)) if s not in kenmerken]
    if ontbrekend:
        fouten.append(f"kenmerken op het pad niet beantwoord: {', '.join(NAAM[s] for s in ontbrekend)} "
                      "(tools/bepaal_type.py vragen)")
    if not voorbij_afbakenen(k, extra):
        return fouten
    u = _stap_0_tot_3(k, extra)
    if u.soort == "element":
        t = typedef(u.paginatype, u.archimate_type, k.get("procesniveau"))
        buiten = [s for s in kenmerken if s in KENMERK and KENMERK[s].groep in ("Toets", "Partij en regeling")
                  and s not in (*t.toets, *typeren(k, extra))]
        if buiten:
            fouten.append(f"kenmerken die niet bij het type {t.naam} horen: {', '.join(NAAM[s] for s in buiten)}; haal "
                          "ze weg")
    return fouten


def waarden(beoordeling: dict) -> dict[str, str]:
    """De waarde van elk kenmerk: het hoofdkenmerk en de soort gedrag uit de keuzevelden, de antwoorden, en buiten het
    pad het standaardantwoord (meestal nee). Bij een keuzekenmerk de gekozen waarde."""
    kenmerken = beoordeling.get("kenmerken") or {}
    k = {s: antwoord(kenmerken, s)["waarde"] for s in (*SLEUTELS, *KEUZEKENMERK)}
    for s in (hoofdkenmerk(beoordeling), soort_gedrag(beoordeling)):
        if s in k:
            k[s] = "ja"
    if "los_van_verantwoordelijkheid" not in kenmerken:  # volgt uit het hoofdkenmerk
        k["los_van_verantwoordelijkheid"] = "ja" if k["handelende_partij"] == "ja" else "nee"
    return k


def _stap_0_tot_3(k: dict, extra: dict) -> Uitkomst:
    for nr, regel in enumerate(REGELS, start=1):
        if regel.test(k, extra):
            return regel.uitkomst(k, extra, nr)
    raise AssertionError("de laatste regel past altijd")


def _stap_3_niveau(u: Uitkomst, k: dict, extra: dict) -> Uitkomst:
    """Stap 3, na het type: een partij geldt voor alle gemeenten (*soort partij*), en een bedrijfsproces heeft een
    *procesniveau*."""
    if u.paginatype in ("actor", "bedrijfssamenwerking") and not _ja(k, "soort_partij"):
        return Uitkomst("geen_element", EERSTE_NIVEAUREGEL, f"Geen soort partij voor alle gemeenten ({u.toelichting})",
                        archimate_type=u.archimate_type, voorleggen=True, typeregel=u.regel,
                        redenen=[f"{NAAM['soort_partij']}: nee"])
    if u.paginatype == "bedrijfsproces":
        u.procesniveau = k["procesniveau"]  # None: de toets van stap 5 valt dan af, anders vraagt controleer het niveau
        u.typeregel = u.regel
        u.regel = EERSTE_NIVEAUREGEL + 1
    return u


def _stap_5(u: Uitkomst, k: dict, extra: dict) -> Uitkomst:
    """Stap 5: elk toetskenmerk van het type is ja."""
    t = typedef(u.paginatype, u.archimate_type, u.procesniveau)
    nee = [s for s in t.toets if not _ja(k, s)]
    te_weinig = t.paginatype == "capability" and _ja(k, "gerealiseerd_door") \
        and extra.get("realiserende_functies", 0) < MIN_FUNCTIES_CAPABILITY
    if nee or te_weinig:
        redenen = [f"{NAAM[s]}: nee" for s in nee]
        if te_weinig:
            redenen.append(f"{NAAM['gerealiseerd_door']}: minder dan {MIN_FUNCTIES_CAPABILITY} bedrijfsfuncties; een "
                           "capability die samenvalt met één functie is geen element: de functie volstaat")
        return Uitkomst("geen_element", EERSTE_TOETSREGEL, f"Toetskenmerk ontbreekt voor {t.naam}",
                        archimate_type=u.archimate_type, voorleggen=True, typeregel=u.typeregel or u.regel,
                        redenen=redenen)
    return Uitkomst("element", EERSTE_TOETSREGEL, f"{u.toelichting} ({len(t.toets)} toetskenmerken ja)",
                    paginatype=u.paginatype, archimate_type=u.archimate_type, typeregel=u.typeregel or u.regel,
                    procesniveau=u.procesniveau, voorleggen=u.voorleggen, redenen=list(u.redenen))


def _indeling(u: Uitkomst, n: int) -> Uitkomst:
    u.regel = EERSTE_INDELINGSREGEL + n
    return u


def _niveau_proces(u: Uitkomst, k: dict, extra: dict) -> Uitkomst:
    """Stap 6, proces: de samenhang van het gekozen procesniveau met het kernobject en de soort werk. Procesniveaus
    volgens GEMMA Online, Proceshiërarchie."""
    if u.procesniveau == CLUSTER:
        if not extra.get("soort_werk_van"):
            u.procesniveau = None
            u.voorleggen = True
            u.redenen.append("groepering van processen zonder soort werk (gemma_generiek): een taak is geen "
                             "procesniveau; de groepering naar taak is het beleidsdomein")
        return _indeling(u, 0)
    if not extra.get("kernobject"):
        u.voorleggen = True
        u.redenen.append("kernobject ontbreekt: noem het object waarvan dit proces de levensloop omvat" if
                         u.procesniveau == "levensloopproces" else
                         "kernobject ontbreekt: noem het object waarin dit bedrijfsproces een mutatie doet")
    return _indeling(u, 1 if u.procesniveau == "levensloopproces" else 2)


def _stap_6(u: Uitkomst, k: dict, extra: dict) -> Uitkomst:
    if u.paginatype == "bedrijfsproces":
        u = _niveau_proces(u, k, extra)
    if u.paginatype == "bedrijfsinteractie":
        _indeling(u, 3)
        if not extra.get("kernobject"):
            u.voorleggen = True
            u.redenen.append("kernobject ontbreekt: noem het object dat door de keten gaat")
    if u.soort == "element" and u.paginatype == "bedrijfsobject" and _ja(k, "generiek"):
        u.objectniveau = "generiek"
        _indeling(u, 4)
    if u.soort == "element" and u.paginatype in ("gebeurtenis", "rol", "dienst") and _ja(k, "generiek"):
        u.generiek = True
    return u


def evalueer(beoordeling: dict) -> Uitkomst:
    fouten = controleer(beoordeling)
    if fouten:
        raise BeoordelingFout(fouten)
    k = waarden(beoordeling)
    extra = extra_velden(beoordeling)
    uitkomst = _stap_0_tot_3(k, extra)
    if uitkomst.soort == "element":
        uitkomst = _stap_3_niveau(uitkomst, k, extra)
    if uitkomst.soort == "element":
        uitkomst = _stap_5(uitkomst, k, extra)
    if uitkomst.soort == "element":
        uitkomst = _stap_6(uitkomst, k, extra)
    if uitkomst.soort == "element":
        for veld in ontbrekende_velden(beoordeling, asdict(uitkomst)):
            uitkomst.voorleggen = True
            uitkomst.redenen.append(f"indelingsveld ontbreekt: {veld}")

    if uitkomst.soort in ("eigenschap", "onderdeel", "specialisatie", "geen_pagina") \
            and uitkomst.archimate_type != "location" and not extra.get("genoemd_begrip"):
        uitkomst.voorleggen = True
        uitkomst.redenen.append("genoemd begrip ontbreekt")
    if extra.get("homoniem_van") and uitkomst.soort not in ("synoniem",):
        uitkomst.voorleggen = True
        uitkomst.redenen.append(f"homoniem van {extra['homoniem_van']}: naamkeuze voorleggen")
    return uitkomst


def is_afgewezen(beoordeling: dict) -> bool:
    """Het laatste besluit van de redacteur is `afwijzen`: het begrip is geen element meer in het model."""
    besluiten = beoordeling.get("besluiten") or []
    return bool(besluiten) and besluiten[-1].get("gevolg") == "afwijzen"


def _begripnamen(beoordelingen: dict[str, dict]) -> dict[str, str]:
    """Het id bij de naam, het id en de synoniemen van elk begrip (kleine letters)."""
    namen: dict[str, str] = {}
    for b, d in sorted(beoordelingen.items()):
        for naam in (b, d.get("begrip", ""), *(s["naam"] for s in d.get("synoniemen") or [])):
            namen.setdefault(naam.lower(), b)
    return namen


def _als_element(d: dict) -> Uitkomst | None:
    """De uitkomst van een begrip met *afhankelijkheid* onderdeel alsof het zelfstandig was (stap 6: een subobject)."""
    kenmerken = {s: a for s, a in (d.get("kenmerken") or {}).items() if s != "afhankelijkheid"}
    try:
        return evalueer({**d, "kenmerken": kenmerken})
    except BeoordelingFout:
        return None


def indeling(beoordelingen: dict[str, dict], uitkomsten: dict[str, dict | None]) -> list[str]:
    """Stap 6 met context: het objectniveau (kernobject, subobject of onderdeel), de toets van de afhankelijkheid en de
    controle op `kernobject`.

    Wijzigt `uitkomsten` ter plekke; levert fouten (per `id: tekst`). De procesindeling naar kernobject is strikt
    hiërarchisch: per kernobject precies één levensloopproces, met het taakveld en
    beleidsdomein van dat kernobject; meer alleen als ze allemaal een bedrijfsinteractie met dat kernobject bedienen
    (elk het deel van één partij in de ketensamenwerking); een levensloopproces aggregeert geen levensloopproces; een
    bedrijfsproces hangt
    onder hoogstens één levensloopproces en noemt het object waarin het een mutatie doet. Een bedrijfsinteractie noemt
    het object dat door de keten gaat, met het beleidsdomein van dat object. Een bedrijfsobject met *afhankelijkheid*
    onderdeel dat kernobject is van een bedrijfsproces, is een subobject. Een deelproces hangt af van een bestaand
    bedrijfsproces, een variant van een bestaand element van hetzelfde type: anders voorleggen."""
    fouten = []
    kernobject_van: dict[str, str] = {}
    afgewezen = {b for b, d in beoordelingen.items() if is_afgewezen(d)}
    niveau = {b: u["procesniveau"] for b, u in uitkomsten.items()
              if u and u["soort"] == "element" and u["paginatype"] == "bedrijfsproces" and b not in afgewezen}
    interacties = {b for b, u in uitkomsten.items()
                   if u and u["soort"] == "element" and u["paginatype"] == "bedrijfsinteractie" and b not in afgewezen}

    # De afhankelijkheid: het genoemde begrip bestaat, en bij een variant heeft het hetzelfde type.
    namen = _begripnamen(beoordelingen)
    for bid, u in sorted(uitkomsten.items()):
        if not u or u["soort"] not in ("onderdeel", "specialisatie"):
            continue
        waarde = antwoord(beoordelingen[bid].get("kenmerken") or {}, "afhankelijkheid")["waarde"]
        if waarde not in ("deelproces", "variant"):
            continue
        doel = namen.get(str(u.get("genoemd_begrip") or "").lower())
        d_u = uitkomsten.get(doel) if doel else None
        if not d_u or d_u["soort"] != "element":
            reden = (f"{waarde} van '{u.get('genoemd_begrip')}', dat geen element is: een {waarde} hangt af van een "
                     "bestaand element")
        elif waarde == "deelproces" and d_u["paginatype"] != "bedrijfsproces":
            reden = f"deelproces van '{doel}', dat geen bedrijfsproces is"
        elif waarde == "variant" and d_u["archimate_type"] != u.get("archimate_type") and u.get("archimate_type"):
            reden = f"variant van '{doel}', dat een ander type heeft ({d_u['archimate_type']})"
        else:
            if waarde == "variant":  # het type volgt uit het begrip waarvan het afhangt
                u["archimate_type"] = d_u["archimate_type"]
            continue
        u["voorleggen"] = True
        if reden not in u["redenen"]:
            u["redenen"].append(reden)

    # Een onderdeel dat kernobject is van een bedrijfsproces, is een subobject.
    subobjecten: set[str] = set()
    for bid, n in sorted(niveau.items()):
        ko = beoordelingen[bid].get("kernobject")
        u = uitkomsten.get(ko) if ko else None
        d = beoordelingen.get(ko) if ko else None
        if n != "bedrijfsproces" or not u or u["soort"] != "onderdeel" or ko in subobjecten or ko in afgewezen:
            continue
        if antwoord(d.get("kenmerken") or {}, "afhankelijkheid")["waarde"] != "onderdeel" or d.get("vak") != "bedrijf/passief":
            continue
        als = _als_element(d)
        if als and als.soort == "element" and als.paginatype == "bedrijfsobject":
            als.objectniveau = "subobject"
            als.regel = EERSTE_INDELINGSREGEL + 7
            uitkomsten[ko] = asdict(als)
            subobjecten.add(ko)
    objecten = {b for b, u in uitkomsten.items() if u and u["soort"] == "element" and u["paginatype"] == "bedrijfsobject"}

    def ketens(bid: str, ko: str) -> set[str]:
        """De bedrijfsinteracties met kernobject `ko` die dit proces bedient."""
        return {r["naar"] for r in beoordelingen[bid].get("relaties") or []
                if r["soort"] == "bediening" and r["naar"] in interacties
                and beoordelingen[r["naar"]].get("kernobject") == ko}

    per_kernobject: dict[str, list[str]] = {}
    ouders: dict[str, list[str]] = {}
    for bid, n in sorted(niveau.items()):
        if n != "levensloopproces":
            continue
        for r in beoordelingen[bid].get("relaties") or []:
            if r["soort"] != "aggregatie" or r["naar"] not in niveau:
                continue
            if niveau[r["naar"]] == "levensloopproces":
                fouten.append(f"{bid}: levensloopproces aggregeert levensloopproces '{r['naar']}'; de procesindeling "
                              "naar kernobject is strikt hiërarchisch (een keten is een bedrijfsinteractie)")
            else:
                ouders.setdefault(r["naar"], []).append(bid)
    for bid, boven in sorted(ouders.items()):
        if len(boven) > 1:
            fouten.append(f"{bid}: hangt onder meer levensloopprocessen ({', '.join(boven)}); een bedrijfsproces hangt "
                          "onder één levensloopproces")
    # Triggering (klant tot klant): een bedrijfsproces dat een ander bedrijfsproces onder
    # hetzelfde levensloopproces triggert, wijst op een deelproces (voorleggen); een gebeurtenis start altijd een
    # bedrijfsproces, nooit een deelproces (fout).
    for bid, d in sorted(beoordelingen.items()):
        u = uitkomsten.get(bid)
        if not u or u["soort"] != "element" or bid in afgewezen:
            continue
        for r in d.get("relaties") or []:
            if r["soort"] != "triggering":
                continue
            doel = uitkomsten.get(r["naar"])
            if (niveau.get(bid) == "bedrijfsproces" and niveau.get(r["naar"]) == "bedrijfsproces"
                    and set(ouders.get(bid, [])) & set(ouders.get(r["naar"], []))):
                reden = (f"getriggerd door bedrijfsproces '{bid}' onder hetzelfde levensloopproces: deelproces daarvan "
                         "(klant tot klant)?")
                if reden not in doel["redenen"]:
                    doel["voorleggen"] = True
                    doel["redenen"].append(reden)
            elif (u["paginatype"] == "gebeurtenis" and doel and doel["soort"] == "onderdeel"
                  and doel.get("archimate_type") == "business-process"):
                fouten.append(f"{bid}: gebeurtenis triggert deelproces '{r['naar']}'; een gebeurtenis start een "
                              "bedrijfsproces (klant tot klant)")
    for bid, u in sorted(uitkomsten.items()):
        if not u or u["soort"] != "element" or u["paginatype"] not in ("bedrijfsproces", "bedrijfsinteractie") \
                or bid in afgewezen:
            continue
        ko = beoordelingen[bid].get("kernobject")
        if not ko:
            continue
        if ko not in objecten:
            fouten.append(f"{bid}: kernobject '{ko}' is geen bedrijfsobject of afspraak met een pagina")
            continue
        if u["paginatype"] == "bedrijfsinteractie" or u["procesniveau"] == "levensloopproces":
            for veld in ("taakveld", "beleidsdomein"):
                eigen, van_object = beoordelingen[bid].get(veld), beoordelingen[ko].get(veld)
                if van_object and eigen != van_object:
                    fouten.append(f"{bid}: {veld} '{eigen or '—'}' wijkt af van dat van het kernobject '{ko}' "
                                  f"('{van_object}'); het volgt uit het kernobject")
        if u["procesniveau"] == "levensloopproces":
            per_kernobject.setdefault(ko, []).append(bid)
            kernobject_van.setdefault(ko, bid)
    for ko, processen in sorted(per_kernobject.items()):
        if len(processen) > 1 and not set.intersection(*(ketens(p, ko) for p in processen)):
            for bid in processen[1:]:
                fouten.append(f"{bid}: kernobject '{ko}' heeft al het levensloopproces '{processen[0]}' (per "
                              "kernobject één levensloopproces, of één per partij als ze samen een bedrijfsinteractie "
                              "met dat kernobject bedienen)")
    for bid in sorted(objecten):
        u = uitkomsten[bid]
        if u["objectniveau"] or u["generiek"]:
            continue
        if bid in kernobject_van:
            u["objectniveau"] = "kernobject"
            u["regel"] = EERSTE_INDELINGSREGEL + 6
        else:
            u["regel"] = EERSTE_INDELINGSREGEL + 8
            u["voorleggen"] = True
            u["redenen"].append("geen proces bepaalt de levensloop van dit object (kernobject), en het is geen deel "
                                "van een object of generiek")
    return fouten



REDEN_GEEN_GGM = "data-object zonder sterke GGM-match"
ZEKERHEID = ("kennis", "logica", "indruk")   # van een besluit; zonder veld: logica


def voor_te_leggen(uitkomst: Uitkomst | dict, data_objecten: list[dict] = ()) -> list[str]:
    """De redenen waarom de redacteur over dit begrip moet beslissen (leeg: de AI mag het zelf afhandelen).
    `data_objecten`: de afgeleide data-objecten van het element (tools/beslissen.py), elk met de sterkte van zijn
    GGM-match."""
    u = uitkomst if isinstance(uitkomst, dict) else asdict(uitkomst)
    redenen = list(u["redenen"]) or (["voorleggen"] if u["voorleggen"] else [])
    if u["soort"] == "element" and any(d["ggm_sterkte"] not in ("exact", "sterk") for d in data_objecten):
        redenen.append(REDEN_GEEN_GGM)
    return redenen


def open_redenen(redenen: list[str], status: str | None, besluiten: list[dict] | None) -> list[str]:
    """Wat nog voorgelegd moet worden: bij een element tot het akkoord (`review`), bij een begrip zonder pagina tot een
    besluit `afwijzen`. Een besluit dekt geen reden; het akkoord of de afwijzing sluit ze af."""
    if status in ("goedgekeurd", "afgewezen") or (status is None and is_afgewezen({"besluiten": besluiten})):
        return []
    return list(redenen)


def voorgestelde_status(uitkomst: Uitkomst | dict, ggm_match: str | None = None,
                        besluiten: list[dict] | None = None) -> str | None:
    """`afgewezen` als het laatste besluit van de redacteur `afwijzen` is, anders `review`: het akkoord maakt het
    element `goedgekeurd`. De redenen om voor te leggen (`voor_te_leggen`) houden de status niet tegen; ze staan bij
    het element tot het akkoord.

    Geen pagina (synoniem, bron, buiten scope, eigenschap, onderdeel, verwijzing, specialisatie, geen element,
    conflict, herkend, geen pagina) → None.
    """
    u = uitkomst if isinstance(uitkomst, dict) else asdict(uitkomst)
    if u["soort"] != "element":
        return None
    if is_afgewezen({"besluiten": besluiten}):
        return "afgewezen"
    return "review"



# --- Generatie: documentatie (wikipagina) en het beoordeling-schema ---

def _cel(tekst: str) -> str:
    return tekst.replace("|", "\\|")


# De bronduiding (laag 3) van de bronnen van de aanpak, waar de herkomst van een kenmerk naar linkt (A5): de naam in de
# herkomst, en bij NORA het woord erachter. ArchiMate en UPL hebben (nog) geen bronduiding: die blijven tekst.
HERKOMST_BRON = (("GEMMA Online, Proceshiërarchie", None, "2026-vng-gemma-proceshierarchie"),
                 ("GEMMA Online, Impact ketensamenwerking", None, "2026-vng-gemma-impact-ketensamenwerking"),
                 ("GEMMA", None, "2026-vng-over-gemma"),
                 ("NORA", "Kanalen", "2026-noraonline-kanalen"),
                 ("NORA", "Dienstverlening", "2026-noraonline-dienstverlening"))
BRONDUIDING_MAP = "modellen/gemma/bronduidingen/overig"


def herkomst_tekst(herkomst: str, van: str = "kennismodel") -> str:
    """De herkomst van een kenmerk, met de naam van elke bron als link naar haar bronduiding en de vindplaats erachter.
    `van` is de map van de pagina, relatief aan de wiki."""
    uit = []
    for deel in herkomst.split("; "):
        naam, _, rest = deel.partition(" (")
        for n, woord, bron in HERKOMST_BRON:
            pad = WIKI_ROOT / BRONDUIDING_MAP / f"{bron}.md"
            if naam == n and (woord is None or rest.startswith(woord)) and pad.exists():
                deel = f"[{naam}]({'../' * (van.count('/') + 1)}{BRONDUIDING_MAP}/{bron}.md)" + (f" ({rest}" if rest else "")
                break
        uit.append(deel)
    return "; ".join(uit)


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


PAD_UITLEG = ("Beantwoord de vragen op het pad, in vier fasen (`tools/bepaal_type.py vragen <id>`). Afbakenen: alleen een "
              "afwijking in de scope (stap 1) en de *afhankelijkheid* (stap 2), met een stop als het begrip afvalt. "
              "Typeren: de keuzevelden (vak, hoofdkenmerk, soort gedrag; zie de matrix), de kenmerken van het "
              "hoofdkenmerk en de keuzekenmerken *procesniveau* en *interactievorm*. Onderbouwen: de toetskenmerken van "
              "het type. Indelen: een script, met *generiek* als afwijking. Een kenmerk buiten het pad laat je weg: het "
              "script leidt het standaardantwoord af (*standaard ja* staat erbij, anders nee). Een relatiekenmerk (†) "
              "met ja noemt zijn tegenpartij in `naar`: het id van het element (het script vult het als de relatie "
              "bestaat, en dan steunt het kenmerk op haar bron); bestaat het element (nog) niet, dan naam en type, met "
              "een onderbouwing en bron. Bij \"Noem …\" hoort bij ja een concreet begrip, artikel of relatie uit de "
              "bronnen; zonder zo'n verwijzing is het antwoord nee.")


def doc_matrix(per_vak: bool = True) -> list[str]:
    """De ArchiMate-matrix met de vakken, en per vak wat Typeren vraagt (kennismodel/kenmerken-en-beslistabel.md); zonder
    `per_vak` alleen de matrix (kennismodel/README.md)."""
    def cel(laag: str, aspect: str, extern: bool | None) -> str:
        return ", ".join(v.typen for v in VAKKEN if (v.laag, v.aspect, v.extern) == (laag, aspect, extern)) or "—"

    kolommen = [("actief", False), ("actief", True), ("gedrag", False), ("gedrag", True), ("passief", None),
                ("samengesteld", None)]
    regels = ["### De ArchiMate-matrix", "",
              "Typeren kiest eerst het vak: de laag, het aspect en intern of extern, zoals in ArchiMate. Het vak bepaalt "
              "welke hoofdkenmerken en soorten gedrag er zijn, en welke vragen volgen. Motivatie kent geen aspecten.", "",
              "| Laag | Actief intern | Actief extern | Gedrag intern | Gedrag extern | Passief | Samengesteld |",
              "|---|---|---|---|---|---|---|",
              "| bedrijf | " + " | ".join(cel("bedrijf", a, e) for a, e in kolommen) + " |",
              "| applicatie | zonder element | zonder element | zonder element | zonder element | Data-object (afgeleid uit de GGM-match) | "
              "— |",
              "| technologie | zonder element: komt misschien nog | | | | | |",
              "| strategie | Resource: zonder element | | Capability; Waardestroom en Handelwijze: zonder element | | | |",
              "| motivatie | Beleidskader (element); Kwaliteitsdoel (matchdoel); de andere typen buiten dit model | | | | | |",
              "| overig | | | | | | Locatie (geen pagina), Groepering (indeling) |", ""]
    if not per_vak:
        return regels
    regels += ["| Vak (`vak`) | Typen | Hoofdkenmerk (`hoofdkenmerk`) | Soort gedrag (`soort_gedrag`) | Typeren daarna |",
               "|---|---|---|---|---|"]
    for v in VAKKEN:
        hoofd = ", ".join(f"*{NAAM[h]}*" for h in v.hoofdkenmerken)
        hoofd += " (kiezen)" if len(v.hoofdkenmerken) > 1 else " (volgt uit het vak)"
        soort = (", ".join(f"*{NAAM[x]}*" for x in v.soorten) + (" (kiezen)" if len(v.soorten) > 1 else
                                                                  " (volgt uit het vak)")) if v.soorten else "—"
        groep = sorted({x for aarden, nodig, afw in TYPEGROEP for x in (*nodig, *afw)
                        if set(v.hoofdkenmerken) & aarden})
        regels.append(f"| `{v.sleutel}` | {v.typen} | {hoofd} | {soort} | {_namen(groep) if groep else '—'} |")
    nr = next(i for i, r in enumerate(REGELS, start=1) if r.stap.startswith("3"))
    regels += ["", f"Past het hoofdkenmerk of de soort gedrag niet bij het vak, dan is er een conflict (regel {nr}).", ""]
    return regels


def doc_keuzekenmerken() -> list[str]:
    """De keuzekenmerken met hun waarden en het criterium per waarde (kennismodel/kenmerken-en-beslistabel.md)."""
    regels = ["### Keuzekenmerken", "",
              "Een keuzekenmerk heeft een waardenlijst: precies één waarde, met één onderbouwing en bron (in `kenmerken`; "
              "het vak, het hoofdkenmerk en de soort gedrag zijn keuzevelden bovenaan). De waarde *zelfstandig* is het "
              "standaardantwoord.", ""]
    for k in KEUZEKENMERKEN:
        regels += [f"**{k.naam}** (stap {k.stap}). {_cel(k.vraag)} Herkomst: {_cel(herkomst_tekst(k.herkomst))}.", "",
                   "| Waarde | Criterium |", "|---|---|", *[f"| `{w}` | {_cel(c)} |" for w, c in k.waarden], ""]
    return regels


def doc_vragentabel() -> list[str]:
    """De vragenlijst met voorbeelden en herkomst, per groep (kennismodel/kenmerken-en-beslistabel.md)."""
    regels = ["### Kenmerken", "", PAD_UITLEG, ""]
    nr = 0
    for groep in GROEPEN:
        regels += [f"**{groep}.** {GROEP_ALS[groep]}", "", "| Nr | Kenmerk | Vraag | Ja | Nee | Herkomst |",
                   "|---|---|---|---|---|---|"]
        for km_ in (k for k in KENMERKEN if k.groep == groep):
            nr += 1
            naam = f"*{km_.naam}*" + (" †" if km_.sleutel in RELATIONEEL else "") + (
                " (standaard ja)" if STANDAARD.get(km_.sleutel) == "ja" else "")
            regels.append(f"| {nr} | {naam} | {_cel(km_.vraag)} | {_cel(km_.ja)} | {_cel(km_.nee)} | "
                          f"{_cel(herkomst_tekst(km_.herkomst))} |")
        regels.append("")
    return regels


def doc_toetskenmerken() -> list[str]:
    """De toetskenmerken per type (stap 5): een relatiekenmerk (†) altijd ja of nee met tegenpartij, de andere standaard ja."""
    regels = ["### Toetskenmerken per type", "",
              "Alle toetskenmerken van het type moeten ja zijn; een nee wordt voorgelegd. Een relatiekenmerk (†) is een "
              "kernrelatie: altijd ja of nee, met de tegenpartij. De andere zijn standaard ja; de beoordeling schrijft "
              "alleen een nee, de elementpagina toont ze allemaal.", "",
              "| Type | Toetskenmerken |", "|---|---|"]
    for t in TYPEN:
        if t.toets:
            regels.append(f"| {t.naam} | " + ", ".join(
                f"*{NAAM[s]}*" + (" †" if s in RELATIONEEL else "") + (" (expliciet)" if s in t.expliciet else "")
                for s in t.toets) + " |")
    return regels + [""]


def doc_stappen() -> list[str]:
    regels = ["### Stappentabel", "",
              "Vier fasen, zeven stappen. Afbakenen (stap 0 tot en met 2) en het type in Typeren (stap 3) van boven naar "
              "beneden: de eerste passende regel beslist en levert het einde of een voorlopig type op. Stap 4 (grondslag) "
              "doet het script, stap 5 toetst de toetskenmerken, stap 6 deelt in.", "",
              "| Nr | Stap | Als | Dan |", "|---|---|---|---|"]
    regels += [f"| {i} | {r.stap} | {_cel(r.als)} | {_cel(r.dan)} |" for i, r in enumerate(REGELS, start=1)]
    regels += [f"| {EERSTE_NIVEAUREGEL + i} | {s} | {_cel(a)} | {_cel(d)} |" for i, (s, a, d) in enumerate(NIVEAU_REGELS)]
    regels += [f"| — | {s} | {_cel(a)} | {_cel(d)} |" for s, a, d in NAREGELS[:1]]
    regels += [f"| {EERSTE_TOETSREGEL + i} | {s} | {_cel(a)} | {_cel(d)} |" for i, (s, a, d) in enumerate(TOETS_REGELS)]
    regels += [f"| {EERSTE_INDELINGSREGEL + i} | {s} | {_cel(a)} | {_cel(d)} |" for i, (s, a, d) in enumerate(INDELING)]
    regels += [f"| — | {s} | {_cel(a)} | {_cel(d)} |" for s, a, d in NAREGELS[1:]]
    regels.append("")
    return regels


def schema() -> dict:
    antwoord = {
        "type": "object",
        "required": ["waarde"],
        "properties": {
            "waarde": {"enum": ["ja", "nee"]},
            "onderbouwing": {"type": "string", "minLength": 1,
                             "description": "Verplicht, behalve bij een relatiekenmerk met ja waarvan `naar` "
                                            "alleen element-id's noemt (script)"},
            "bronnen": {"type": "array", "items": {"type": "string"}},
            "naar": {"type": "array", "minItems": 1, "items": {"oneOf": [
                {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$",
                 "description": "Het id van het element; bestaat de relatie, dan steunt het kenmerk op haar bron"},
                {"type": "object", "required": ["naam", "type"], "additionalProperties": False,
                 "properties": {"naam": {"type": "string", "minLength": 1},
                                "type": {"enum": [*PAGINATYPEN, "procescluster"]}},
                 "description": "Een tegenpartij die (nog) geen element is: naam en paginatype"}]},
                     "description": "Alleen bij een relatiekenmerk (" + ", ".join(RELATIONEEL) + ") met ja: de "
                                    "tegenpartij van de relatie (O3)"},
            "gemma_relatie": {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": "^id-"},
                              "description": "Alleen bij " + ", ".join(GEMMA_KENMERKEN) + ": de GEMMA-relaties "
                                             "waarop de plek in een GEMMA-indeling steunt, in plaats van een bron "
                                             "(regel Elke claim een bron); het script toetst ze aan het model"},
        },
        "additionalProperties": False,
    }

    def keuze(k: Keuzekenmerk) -> dict:
        return {"type": "object", "required": ["waarde"], "additionalProperties": False,
                "properties": {"waarde": {"enum": [w for w, _ in k.waarden]},
                               "onderbouwing": {"type": "string", "minLength": 1},
                               "bronnen": {"type": "array", "items": {"type": "string"}}},
                "description": f"Keuzekenmerk (stap {k.stap}): precies één waarde, met onderbouwing en bron"}

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
        "description": "Beoordeling van één begrip (onderwerpen/<onderwerp>/beoordelingen/<id>.yaml): het oordeel van de AI. "
                       "`status` vullen de scripts (tools/beslissen.py, llmwiki promote) en `beslist` staat in beslist.yaml; nooit zelf "
                       "invullen. Gegenereerd door tools/bepaal_type.py schema.",
        "type": "object",
        "required": ["begrip", "onderwerpen", "kenmerken"],
        "properties": {
            "begrip": {**tekst, "description": "De naam: de gangbare term uit beleid en praktijk"},
            "onderwerpen": {"type": "array", "minItems": 1, "items": id_,
                            "description": "Het eerste is het thuisonderwerp (regel Thuishoren); de andere gebruiken het "
                                           "element met relaties en per_onderwerp"},
            "kenmerken": {
                "type": "object",
                "properties": {**{s: {"$ref": "#/$defs/antwoord"} for s in SLEUTELS if s not in KEUZE},
                               **{k.sleutel: keuze(k) for k in KEUZEKENMERKEN}},
                "additionalProperties": False,
                "description": "De kenmerken op het pad (tools/bepaal_type.py vragen): de keuzekenmerken en de "
                               "relatiekenmerken; een kenmerk in Afbakenen en Indelen alleen bij een afwijking, een "
                               "toetskenmerk dat geen relatie is alleen bij een nee. Buiten het pad leidt het script het "
                               "standaardantwoord af",
            },
            "vak": {"enum": [v.sleutel for v in VAKKEN], "description": KEUZEVELDEN["vak"]},
            "hoofdkenmerk": {"enum": HOOFDKENMERK, "description": KEUZEVELDEN["hoofdkenmerk"]},
            "soort_gedrag": {"enum": SOORT_GEDRAG, "description": KEUZEVELDEN["soort_gedrag"]},
            **{s: {"type": "string", "description": d} for s, d in EXTRA_VELDEN.items()},
            **{s: {"enum": list(w), "description": "Indelingsveld: de plaats in de indelingen (stap 6)"}
               for s, w in WAARDEN.items()},
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
            "object_van": {**obj(["id", "wijziging", "datum"], id=id_, wijziging={"enum": ["hernoemd", "samengevoegd", "gesplitst"]},
                                 datum={"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"}),
                           "description": "Het Archi-object dat dit element voortzet na hernoemen, samenvoegen of splitsen "
                                          "(regel Objectbehoud): het begrip-id van het oude begrip. Hernoemd: altijd; "
                                          "samengevoegd of gesplitst: de redacteur kiest of en welk object blijft"},
            "taakveld": tekst,
            "beleidsdomein": tekst,
            "ggm": obj(["sterkte", "onderbouwing"], guid={"type": "string", "pattern": "^EAID_"}, sterkte=sterkte,
                       onderbouwing=tekst,
                       duplicaten={"type": "array", "items": obj(["guid", "toelichting"],
                                                                 guid={"type": "string", "pattern": "^EAID_"},
                                                                 toelichting=tekst)}),
            "gemma": obj(["sterkte", "onderbouwing"], id=tekst, sterkte=sterkte, onderbouwing=tekst),
            "data_objecten": {"type": "array", "minItems": 1, "items": obj(
                ["naam", "ggm"], naam={**tekst, "pattern": "-data$"},
                ggm=obj(["guid", "sterkte", "onderbouwing"], guid={"type": "string", "pattern": "^EAID_"},
                        sterkte={"enum": ["exact", "sterk", "partieel"]}, onderbouwing=tekst)),
                "description": "Alleen een extra data-object, voor een andere GGM-entiteit dan de match van het "
                               "element (`ggm`): naam (op -data) en de GGM-match. Het data-object <naam>-data uit "
                               "`ggm` maakt het script zelf (tools/beslissen.py)"},
            "gemma_generiek": {**obj(["id", "onderbouwing"], id=tekst, onderbouwing=tekst),
                               "description": "Specialisatie van een generiek GEMMA-element (bedrijfsproces, "
                                              "gebeurtenis, dienst of rol), met het id van dat element; bij een "
                                              "cluster naar soort werk bepaalt dit het procesniveau"},
            "gemma_functie": {**obj(["id"], id=tekst, gemma_relatie={"type": "string", "pattern": "^id-"},
                                    bronnen={**bron_ids, "minItems": 1}, vindplaats=tekst),
                              "description": "Bij een bedrijfsfunctie of dienst: de plek in de GEMMA-functiehiërarchie "
                                             "(Functie-indeling naar domein), als het id van de bovenliggende GEMMA-functie, "
                                             "die zelf geen element is. De plek steunt op de GEMMA-relatie van die functie "
                                             "naar de GEMMA-match van dit element (`gemma_relatie`), of anders op "
                                             "`bronnen` met `vindplaats` (regel Elke claim een bron); het script toetst "
                                             "ze aan het model"},
            "kwaliteitsdoelen": {"type": "array", "items": obj(
                ["id", "sterkte", "onderbouwing", "bronnen"], id=tekst, sterkte={"enum": list(km.STERKTEN)},
                onderbouwing=tekst, bronnen={**bron_ids, "minItems": 1}, vindplaats=tekst),
                "description": "Bij een beleidskader: de GEMMA-kwaliteitsdoelen waaraan het grondslag geeft (relatie "
                               "invloed, 'geeft grondslag aan'), met het GEMMA-id, de sterkte ("
                               + ", ".join(f"{s} {u}" for s, u in km.STERKTEN.items()) + "), een onderbouwing en de "
                               "bronnen"},
            "naamkeuze": alineas,
            "homoniemen": {"type": "array", "items": obj(["begrip", "betekenis", "waar", "naamkeuze"], begrip=tekst,
                                                         betekenis=tekst, waar=tekst, naamkeuze=tekst, element=id_)},
            "generalisatie": alineas,
            "specialisaties": {"type": "array", "items": obj(["naam", "omschrijving"], naam=tekst, omschrijving=tekst,
                                                             element=id_, ggm_guid=tekst, ggm_attribuut=tekst)},
            "deelprocessen": {"type": "array", "items": obj(["naam", "omschrijving", "bronnen"], naam=tekst,
                                                            omschrijving=tekst, bronnen=bron_ids, vindplaats=tekst,
                                                            begrip=id_),
                              "description": "Bij een bedrijfsproces: de deelprocessen in volgorde, elk met één of "
                                             "twee zinnen voor procesontwerpers (wat er gebeurt, wie, welke termijn); "
                                             "`begrip` is de beoordeling van een deelproces zonder pagina"},
            "ggm_componenten": {"type": "array", "items": obj(["naam", "guid", "toelichting"], naam=tekst,
                                                              guid={"type": "string", "pattern": "^EAID_"},
                                                              toelichting=tekst)},
            "tegenhanger": obj(["element", "toelichting"], element=id_, toelichting=tekst),
            "relaties": {"type": "array", "items": obj(
                ["soort", "naar", "ggm_match"],
                soort={"type": "string", "pattern": r"^(associatie|associatie \(gericht\)|aggregatie|compositie|"
                                                    r"specialisatie|toewijzing|toegang \([a-zë-]+\)|triggering|"
                                                    r"stroom|realisatie|bediening)$"},
                naar=id_, naam=tekst, kardinaliteit=tekst,
                ggm_match={"enum": ["exact", "geen"],
                           "description": "exact: de relatie is een GGM-relatie tussen de gematchte entiteiten "
                                          "(`ggm_relatie`); geen: geen GGM-relatie, ook niet bij een afgeleide keten"},
                via={**id_, "description": "Een begrip met uitkomst specialisatie van het doel (een specialisatie "
                                           "zonder pagina)"},
                ggm_relatie={"type": "array", "items": {"type": "string", "pattern": "^EAID_"}},
                gemma_relatie={"type": "string", "pattern": "^id-",
                               "description": "Een relatie binnen een GEMMA-indeling tussen twee gematchte elementen: "
                                              "het id van de GEMMA-relatie, in plaats van bronnen (regel Elke claim "
                                              "een bron); het script toetst haar aan het model"},
                bronnen=bron_ids, vindplaats=tekst)},
            "bronnen": {**bron_ids, "description": "Bronnen naast die in kenmerken en relaties, bijv. de algemene "
                                                   "bron van de beschrijving"},
            "vragen": {"type": "array", "items": tekst, "description": "Open vragen aan de redacteur"},
            "besluiten": {"type": "array", "items": {**obj(
                ["datum", "besluit", "gevolg"], datum={"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"},
                besluit=tekst, gevolg={"enum": ["afwijzen", "verwerkt"]},
                zekerheid={"enum": list(ZEKERHEID),
                           "description": "kennis: domeinkennis van de redacteur of een bron, geldt als regel; logica: "
                                          "afgeleid, opnieuw voorleggen als nieuwe informatie de redenering raakt; "
                                          "indruk: voorlopig, in fase 3 opnieuw voorleggen. Zonder veld: logica"},
                stand={**tekst, "description": "Bij een besluit dat nog open staat: hoe het nu staat"})}},
            "status": {"enum": ["review", "goedgekeurd", "afgewezen"],
                       "description": "Door tools/beslissen.py en llmwiki promote; niet zelf invullen"},
            "beslist": {"type": "object", "description": "Door tools/beslissen.py; niet zelf invullen"},
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_eval = sub.add_parser("evalueer", help="Pas de beslistabel toe op een assessment of beoordeling")
    p_eval.add_argument("bestand")
    p_eval.add_argument("--schrijf", action="store_true", help="Zet de uitkomst terug in het bestand (veld 'uitkomst')")
    p_status = sub.add_parser("status", help="Voorgestelde status voor een uitkomst")
    p_status.add_argument("--uitkomst", required=True)
    p_status.add_argument("--ggm-match")
    p_schema = sub.add_parser("schema", help="Beoordeling-schema")
    p_schema.add_argument("--schrijf", action="store_true", help=f"Schrijf naar {SCHEMA_PATH.relative_to(WIKI_ROOT)}")
    p_vragen = sub.add_parser("vragen", help="De vragen voor de volgende fase van een beoordeling")
    p_vragen.add_argument("id", nargs="?", help="De beoordeling; zonder id of bij een nieuw begrip: fase A")
    p_vragen.add_argument("--type", dest="paginatype", help="Fase B van dit paginatype (of procescluster)")
    p_vragen.add_argument("--wiki", type=Path, default=WIKI_ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    if args.cmd == "vragen":
        data = None
        if args.id:
            import gam_gemeen
            from llmwiki import beoordeling as beoordelingen
            alle = beoordelingen.alle(args.wiki, gam_gemeen.wiki_yaml(args.wiki))
            data = alle[args.id][1] if args.id in alle else None
            if data is None:
                print(f"Geen beoordeling '{args.id}': een nieuw begrip.")
        try:
            print("\n".join(vragen(data, args.paginatype)))
        except ValueError as exc:
            print(f"fout: {exc}")
            return 1
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
        print(voorgestelde_status(uitkomst, args.ggm_match))
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
