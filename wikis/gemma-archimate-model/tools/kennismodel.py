"""Het kennismodel van deze wiki: alle concepttypen en de afspraken die de modellering raken, als metadata.

Eén bron voor:
- ELEMENTTYPEN, per architectuurlaag: de GEMMA-naam, het ArchiMate-type, de definitie met herkomst, of het type in Over
  GEMMA staat, de niveaus, de eigenschappen, de naamvorm, de afstemming met GGM, GEMMA en UPL, de afspraken en
  voorbeelden;
- RELATIES: de toegestane relaties tussen de typen (bron, relatie, doel, vaste namen, kernrelatie, in Over GEMMA), en
  WEGGEFILTERD: relaties die in ArchiMate geldig zijn maar niet in het kennismodel van de wiki staan, met de reden;
- de vaste relatienamen: HANDELINGEN en VERANTWOORDELIJKHEDEN (toegang) en GRONDSLAGNAMEN (beleidskader);
- INDELINGEN, met per indeling wat ze indeelt, waarnaar, de niveaus, de groepering en de afspraken;
- ZONDER_ELEMENT: per laag de elementtypen die niet tot een element leiden, met de reden.

Het kennismodel is metadata: het telt niets. Wat een begrip is, beslist de beslistabel (tools/bepaal_type.py); welke
relaties in ArchiMate geldig zijn, toetst tools/relaties.py. tools/bepaal_type.py, tools/relaties.py en
tools/archimate_export.py lezen hun typen, eigenschappen, namen en indelingen hieruit.

De pagina's in kennismodel/ worden hieruit gegenereerd (`paginas()`), behalve modelleerregels.md, die met de hand
geschreven is. tools/render.py schrijft ze mee; de pre-commit (`tools/render.py --check`) bewaakt dat ze gelijk zijn
aan deze bron.

Gebruik (vanuit de wikimap):
    uv run python tools/kennismodel.py            # de pagina's naar het scherm (paden)
    uv run python tools/render.py                 # alles schrijven, ook kennismodel/
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path

MAP = "kennismodel"
HANDMATIG = ("modelleerregels.md",)  # met de hand geschreven; render beheert ze niet

LAGEN = {"bedrijfsarchitectuur": "Bedrijfsarchitectuur", "motivatie": "Motivatie",
         "applicatiearchitectuur": "Applicatiearchitectuur", "overig": "Overig"}

# --- Eigenschappen ---

AFNEMERS = ("extern", "intern")
DOMEINEN = ("Bestuur", "Fysieke leefomgeving", "Niet domeingebonden", "Openbare orde en veiligheid", "Ondersteuning",
            "Publieksdiensten", "Sociaal domein")  # GEMMA domeinen
DOELGROEPEN = ("gemeente", "inwoners en ondernemers", "ketenpartners")
DOELGROEP_OMSCHRIJVING = {  # de documentatie van de groepering van een doelgroep in de export
    "gemeente": "De gemeente zelf: haar bestuursorganen, ambtelijke rollen en kanalen.",
    "inwoners en ondernemers": "Inwoners, ondernemers en organisaties die als klant of belanghebbende met de gemeente "
                               "te maken hebben.",
    "ketenpartners": "Organisaties waarmee de gemeente structureel samenwerkt of die zij opdracht geeft.",
}
REGELGEVERS = ("EU", "rijk", "landelijke organisatie", "VNG-model")
WAARDEN = {"afnemer": AFNEMERS, "domein": DOMEINEN, "doelgroep": DOELGROEPEN, "regelgever": REGELGEVERS}

EIGENSCHAPPEN = {  # veld in de beoordeling → wat het vastlegt
    "kernobject": "het bedrijfsobject waarvan het proces de levensloop omvat (levensloopproces), waarin het een "
                  "mutatie doet (bedrijfsproces), of dat door de keten gaat (bedrijfsinteractie)",
    "afnemer": "voor wie het is: extern of intern (de bovenste laag van het processenlandschap, de rol Klant en de "
               "externe en interne UPL-lijst)",
    "domein": "het GEMMA-domein, de plaats in de Functie-indeling naar domein",
    "doelgroep": "gemeente, inwoners en ondernemers of ketenpartners: de plaats in de Doelgroepindeling",
    "regelgever": "EU, rijk, landelijke organisatie of VNG-model: bepaalt de groep in de Grondslagindeling",
    "kwaliteitsdoelen": "de GEMMA-kwaliteitsdoelen waaraan het beleidskader grondslag geeft, met de sterkte van die "
                        "invloed, een onderbouwing en de bronnen",
    "taakveld": "het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling",
    "beleidsdomein": "het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling",
    "gemma_generiek": "het generieke GEMMA-element waarvan dit een specialisatie is (exacte match)",
    "deelprocessen": "de deelprocessen in volgorde, elk met één of twee zinnen en een bron (geen eigen pagina)",
    "gemma": "de match met het GEMMA-model: het id gaat mee in de export",
    "ggm": "de match met het GGM: entiteit, sterkte en onderbouwing",
    "data_object": "annotatie: het begrip wordt als gegevensstructuur geautomatiseerd verwerkt",
}

# --- Vaste relatienamen ---

# Handeling van gedrag op een object → ArchiMate-toegangstype
HANDELINGEN = {"registreren": "schrijven", "bijwerken": "lezen-schrijven", "beëindigen": "schrijven",
               "raadplegen": "lezen", "verstrekken": "lezen", "bewaren": "lezen-schrijven", "overbrengen": "lezen",
               "vernietigen": "schrijven"}
# Verantwoordelijkheid van een rol (of bedrijfssamenwerking) voor een object → ArchiMate-toegangstype
VERANTWOORDELIJKHEDEN = {"houder": "lezen-schrijven", "bronhouder": "schrijven", "beheerder": "lezen-schrijven",
                         "verstrekker": "lezen", "afnemer": "lezen", "toezichthouder": "lezen", "betrokkene": "lezen",
                         "partij": "lezen-schrijven"}
# Naam van de relatie van een beleidskader naar wat erop steunt, naar de groep in de Grondslagindeling
GRONDSLAGNAMEN = {"is grondslag voor": "Europese regelgeving, Rijksregelgeving; Gemeentelijke regelgeving alleen naar "
                                       "een UPL-product of -dienst zonder landelijke grondslag",
                  "werkt uit voor": "Gemeentelijke regelgeving: werkt de wet uit",
                  "geeft richtlijn voor": "Richtlijn: geen wettelijke grondslag"}

# --- Relatietypen ---

RELATIETYPEN = {  # Nederlandse naam → ArchiMate-relatie
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
    "invloed": "influence",
}
# De sterkte van een invloed (ArchiMate: het attribuut strength van de influence-relatie).
STERKTEN = {"++": "bindend: de regeling stelt eisen of normen voor het doel",
            "+": "draagt bij: de regeling bevordert het doel",
            "-": "beperkt: de regeling staat het doel deels in de weg",
            "--": "staat haaks: de regeling gaat tegen het doel in"}
RELATIETYPE_UITLEG = {
    "associatie": "een betekenisvolle verbinding; gericht als de naam een leesrichting heeft",
    "aggregatie": "het geheel omvat het deel; het deel bestaat ook los",
    "compositie": "het deel bestaat alleen in het geheel",
    "specialisatie": "is een: het doel is het bredere begrip van hetzelfde type",
    "toewijzing": "wie het gedrag uitvoert, of welke actor een rol vervult",
    "toegang": "gedrag of een rol gebruikt een object, met een vaste handeling of verantwoordelijkheid",
    "triggering": "het een start het ander, in de tijd",
    "stroom": "gedrag geeft iets door aan ander gedrag",
    "realisatie": "gedrag realiseert een dienst; een data-object realiseert een bedrijfsobject",
    "bediening": "het een ondersteunt of bedient het ander",
    "invloed": "een motivatie-element beïnvloedt een ander, met een sterkte",
}

# --- Elementtypen ---


@dataclass(frozen=True)
class Elementtype:
    sleutel: str  # bestandsnaam van de modelleerafspraken
    naam: str  # GEMMA-naam
    engels: str  # ArchiMate-naam
    archimate_type: str
    laag: str
    paginatype: str | None  # paginatype in wiki.yaml; None: een annotatie, geen pagina
    definitie: str
    herkomst: str  # GEMMA, NORA of ArchiMate
    over_gemma: bool  # het type staat in Over GEMMA (kennismodel en modelleerafspraken)
    duiding: str
    naamvorm: str
    afstemming: tuple  # (doel, afspraak)
    wel: str
    niet: str
    niveaus: tuple = ()
    eigenschappen: tuple = ()
    verplicht: tuple = ()  # eigenschappen die ingevuld moeten zijn
    afspraken: tuple = ()
    zonder_pagina: str = "annotatie"  # bij paginatype None: wat het type dan is


GEMMA_MATCH = ("GEMMA-model", "match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en "
                              "definitie van het GEMMA-element; een zwakke of partiële match voorleggen")
GGM_GEEN = ("GGM", "geen match: het GGM modelleert gegevens")

ELEMENTTYPEN: list[Elementtype] = [
    Elementtype(
        "bedrijfsobject", "Bedrijfsobject", "Business Object", "business-object", "bedrijfsarchitectuur",
        "bedrijfsobject", "Een concept dat binnen een bepaald domein wordt gebruikt en betekenis heeft.", "GEMMA", True,
        "Een ding waar de gemeente mee werkt: het wordt geregistreerd, bijgewerkt of geraadpleegd door gemeentelijk "
        "gedrag. De soort regeling (Regeling) is ook een bedrijfsobject.",
        "de gangbare term uit beleid en praktijk, zonder lidwoord; de wetsterm wordt een synoniem met context \"wet\"",
        (("GGM", "matchdoel en toets: entiteit, definitie en relaties; zonder match een GGM-terugmelding (hiaat)"),
         GEMMA_MATCH),
        "Graf; Aanvraag; Vergunning", "aanvraag ontvangen (gebeurtenis); register van begraven lijken (representatie)",
        niveaus=("kernobject: het object waarvan één levensloopproces de hele levensloop omvat",
                 "subobject: een deel van een kernobject, met een eigen bedrijfsproces",
                 "generiek object: dezelfde betekenis in veel onderwerpen; domeinspecialisaties krijgen geen pagina en "
                 "staan in relaties met `via`",
                 "onderdeel zonder eigen proces, en invoer die een andere partij maakt: geen pagina"),
        eigenschappen=("taakveld", "beleidsdomein", "ggm", "gemma", "data_object"),
        afspraken=("Registratie, eigendom, systeembeheer, regie of een extern systeem zijn geen argument voor een "
                   "bedrijfsobject; alleen *geautomatiseerd verwerkt* telt, als annotatie.",
                   "Een concreet benoemde regeling als geheel is een beleidskader; de soort (\"verordening\") is het "
                   "bedrijfsobject Regeling.",
                   "Een kernobject heeft één thuis: het onderwerp waar het ontstaat en beheerd wordt.")),
    Elementtype(
        "afspraak", "Afspraak", "Contract", "contract", "bedrijfsarchitectuur", "bedrijfsobject",
        "Overeenkomst tussen meerdere partijen betreffende een bepaald onderwerp.", "GEMMA", True,
        "Een afspraak tussen partijen (overeenkomst, convenant). Een besluit of verordening is géén afspraak. Een "
        "afspraak is een bijzonder bedrijfsobject en heeft dezelfde pagina en indeling.",
        "de gangbare term uit beleid en praktijk, zoals bij een bedrijfsobject",
        (("GGM", "als bij een bedrijfsobject"), GEMMA_MATCH),
        "Uitvoeringsovereenkomst; Grafrecht", "subsidiebeschikking (eenzijdig besluit); verordening",
        niveaus=("als bij een bedrijfsobject: kernobject, subobject of generiek",),
        eigenschappen=("taakveld", "beleidsdomein", "ggm", "gemma", "data_object")),
    Elementtype(
        "product", "Product", "Product", "product", "bedrijfsarchitectuur", "product",
        "Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan "
        "een afnemer en met waarde voor die afnemer.", "GEMMA", True,
        "Wat de gemeente als geheel aanbiedt, zoals in de productencatalogus: diensten met afspraken, geen losse "
        "objecten. Een verleend exemplaar is een bedrijfsobject, geen product.",
        "de UPL-naam letterlijk (Grafuitgifte), met een synoniem waar dat betekenis toevoegt",
        (("UPL", "bron én matchdoel: een UPL-item valt nooit weg en houdt zijn naam; zonder match een "
                 "procesarchitectuur-terugmelding"), GGM_GEEN, GEMMA_MATCH),
        "bewonersparkeervergunning zoals de productencatalogus haar aanbiedt",
        "bezoekersparkeervergunning als tarief van de parkeervergunning (geen zelfstandig aanbod)",
        eigenschappen=("afnemer", "domein", "taakveld", "beleidsdomein", "gemma"), verplicht=("domein", "afnemer"),
        afspraken=("Een product of dienst uit de UPL blijft ook zonder landelijke wettelijke grondslag; dan wordt het "
                   "niet uitgewerkt in processen, objecten, gebeurtenissen of rollen.",
                   "Een beleidskader hangt bij voorkeur aan een product; aan een proces of dienst alleen zolang er geen "
                   "product is.")),
    Elementtype(
        "dienst", "Dienst", "Business Service", "business-service", "bedrijfsarchitectuur", "dienst",
        "Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van "
        "haar omgeving (de dienstafnemer(s)).", "NORA", True,
        "Wat een afnemer van de gemeente kan krijgen, los van hoe het wordt uitgevoerd; gerealiseerd door een proces of "
        "functie.",
        "vanuit de afnemer, wat die kan doen of krijgen (Melding openbare ruimte doen); staat het in de UPL, dan de "
        "UPL-naam letterlijk (Verlof tot begraven)",
        (("UPL", "bron én matchdoel, als bij een product"), GGM_GEEN, GEMMA_MATCH,
         ("generiek GEMMA-element", "bij *generiek*: specialisatie van een generieke GEMMA-dienst (`gemma_generiek`, "
                                    "exacte match); ontbreekt die, dan een voorstel aan GEMMA")),
        "Onderhoud van graven; Melding openbare ruimte doen", "melding afhandelen (proces)",
        eigenschappen=("afnemer", "domein", "taakveld", "beleidsdomein", "gemma", "gemma_generiek"),
        verplicht=("domein", "afnemer"),
        afspraken=("Een dienst wordt gerealiseerd door een bedrijfsproces of bedrijfsfunctie; de verantwoordelijke rol "
                   "hangt aan dat proces of die functie, niet aan de dienst.",
                   "Een product of dienst valt nooit weg: wie het levert, is een bedrijfsproces.")),
    Elementtype(
        "bedrijfsproces", "Bedrijfsproces", "Business Process", "business-process", "bedrijfsarchitectuur",
        "bedrijfsproces", "Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, "
                          "zoals de levering van een Product of Dienst.", "GEMMA", True,
        "Wordt per keer doorlopen en levert een resultaat op. Ook het levensloopproces en het cluster naar soort werk "
        "zijn in ArchiMate een bedrijfsproces.",
        "infinitief met het object in GEMMA-volgorde, werkwoord eerst, zonder lidwoord (Behandelen aanvraag); bestaat "
        "er een GEMMA-proces met dezelfde betekenis, dan de GEMMA-naam; het zelfstandig naamwoord uit de bron wordt "
        "een synoniem met context \"beleid\"",
        (GGM_GEEN, GEMMA_MATCH,
         ("generiek GEMMA-element", "een bedrijfsproces specialiseert vaak een generiek GEMMA-bedrijfsproces "
                                    "(`gemma_generiek`, exacte match); een cluster naar soort werk altijd")),
        "Beheren grafrechten (levensloopproces); Verlenen grafrecht (bedrijfsproces); Behandelen vergunningaanvragen "
        "lijkbezorging (cluster naar soort werk)",
        "Uitreiken reisdocument (deelproces: volgt op de verstrekking, voor hetzelfde geval); Vergunningverlening "
        "(functie)",
        niveaus=("levensloopproces: het gedrag over de hele levensloop van één exemplaar van een kernobject, van begin "
                 "tot eind (*omvat levensloop*); in GEMMA een cluster van bedrijfsprocessen over één thema, GEMMA type "
                 "*Bedrijfsproces (cluster)*",
                 "bedrijfsproces: klant tot klant, onder verantwoordelijkheid van één organisatie; één mutatie in de "
                 "levensloop van een kernobject, en het levert een product, dienst of besluit (*bijdrage aan groter "
                 "proces* met *klant tot klant*)",
                 "deelproces: binnen één bedrijfsfunctie, levert een deeldienst; geen pagina, de tekst staat in "
                 "`deelprocessen` van het bedrijfsproces",
                 "processtap en handeling: geen pagina",
                 "cluster naar soort werk: de bedrijfsprocessen van één soort werk, als specialisatie van een "
                 "generiek GEMMA-bedrijfsproces (*groepeert processen*)"),
        eigenschappen=("kernobject", "afnemer", "gemma_generiek", "deelprocessen", "taakveld", "beleidsdomein",
                       "gemma"),
        verplicht=("afnemer",),
        afspraken=("Per kernobject één levensloopproces, met het taakveld en beleidsdomein van het kernobject. Alleen "
                   "binnen een ketensamenwerking mag een kernobject er meer hebben, één per partij, die samen de "
                   "bedrijfsinteractie met dat kernobject bedienen.",
                   "Een bedrijfsproces begint bij een aanleiding van buiten het proces (een verzoek of melding van een "
                   "klant, een gebeurtenis of een termijn) en loopt door tot het resultaat voor die klant, zonder de "
                   "voortzetting te zijn van een ander proces voor hetzelfde geval. *Eigen besluit* en *eigen "
                   "normering* bepalen het procesniveau niet; *levert aanbod* zonder *klant tot klant* wordt "
                   "voorgelegd.",
                   "Een bedrijfsproces hangt onder één levensloopproces. Triggert een bedrijfsproces een ander "
                   "bedrijfsproces onder hetzelfde levensloopproces voor hetzelfde geval, dan wordt dat voorgelegd "
                   "(mogelijk een deelproces).",
                   "Een groepering van processen is alleen een cluster naar soort werk, met `gemma_generiek`, en alleen "
                   "bij minstens twee bedrijfsprocessen; anders specialiseert het bedrijfsproces zelf. De taak is geen "
                   "procesniveau: boven het levensloopproces staan beleidsdomein en taakveld uit de "
                   "Beleidsdomeinindeling.",
                   "Een ketenproces is geen procesniveau en geen element: waar de bedrijfsprocessen van meer partijen "
                   "samenkomen, is dat een bedrijfsinteractie.",
                   "Een rol mag aan een bedrijfsproces worden toegewezen, niet alleen aan een bedrijfsfunctie.")),
    Elementtype(
        "bedrijfsfunctie", "Bedrijfsfunctie", "Business Function", "business-function", "bedrijfsarchitectuur",
        "bedrijfsfunctie", "Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of "
                           "competenties nodig zijn.", "GEMMA", True,
        "Doorlopende groepering van gedrag; bedient processen. Niet \"wat de gemeente kan\": dat is een vermogen.",
        "een zelfstandig naamwoord voor een doorlopend gebied van gedrag, vaak op -ing, -beheer of -verlening "
        "(Vergunningverlening); een functie en een proces hebben nooit dezelfde naam",
        (GGM_GEEN, ("GEMMA-model", "bij voorkeur een exacte match met een GEMMA-functie; een functie zonder match breidt "
                                   "de GEMMA-functieketen uit")),
        "Exploiteren van begraafplaatsen; Burgerlijke stand diensten", "Lijkbezorging als functie; aanslag opleggen",
        eigenschappen=("domein", "gemma"), verplicht=("domein",),
        afspraken=("Een bedrijfsfunctie heeft geen eigen wettelijke bron nodig: zij volgt de grondslag van de diensten "
                   "en processen die zij omvat, en vervalt alleen als zij niets meer omvat.",
                   "Bedienende GEMMA-functies worden een element met een exacte match; een proces mag door meer "
                   "functies worden bediend.")),
    Elementtype(
        "gebeurtenis", "Gebeurtenis", "Business Event", "business-event", "bedrijfsarchitectuur", "gebeurtenis",
        "Iets dat binnen of buiten een organisatie is gebeurd en binnen die organisatie of daarbuiten gevolgen heeft.",
        "GEMMA", True, "Ogenblikkelijk voorval dat gedrag start of afsluit (verhuizing, aanvraag ontvangen).",
        "een voltooide toestandsverandering (Overlijden; Verval van het grafrecht)",
        (GGM_GEEN, GEMMA_MATCH,
         ("generiek GEMMA-element", "bij *generiek*: specialisatie van een generieke GEMMA-gebeurtenis "
                                    "(`gemma_generiek`, exacte match)")),
        "Overlijden; Verval van het grafrecht; Aanvraag ontvangen", "verhuizing doorgeven (proces)",
        eigenschappen=("gemma", "gemma_generiek"),
        afspraken=("Een gebeurtenis van buiten (de klant, een derde, het recht of een termijn) start een bedrijfsproces, "
                   "nooit een deelproces.",
                   "Een gebeurtenis die het resultaat is van een bedrijfsproces (een rechtsgevolg) kan elders een "
                   "bedrijfsproces starten; een tussentoestand binnen één bedrijfsproces is geen element.",
                   "Een gebeurtenis hangt onder het levensloopproces van het object waarvan de toestand verandert.")),
    Elementtype(
        "actor", "Actor", "Business Actor", "business-actor", "bedrijfsarchitectuur", "actor",
        "Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren.", "GEMMA", True,
        "Persoon, organisatie of eenheid, ook extern of generiek (inwoner), en een samenwerkingsverband met eigen "
        "rechtspersoon (GGD). Hangt alleen via een rol aan gedrag en objecten.",
        "de soort partij in de gangbare term (College van B&W; Kerkgenootschap)",
        (GGM_GEEN, GEMMA_MATCH),
        "College van B&W; Kerkgenootschap; GGD; Rijk",
        "gemeente Utrecht (één exemplaar); een afzonderlijk ministerie of rijksdienst (staat in de beschrijving van "
        "Rijk)",
        eigenschappen=("doelgroep", "gemma"), verplicht=("doelgroep",),
        afspraken=("Een actor is een soort partij: elke gemeente heeft ermee te maken in dezelfde rol. Dat sluit uit "
                   "wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat: Rijk, "
                   "Provincie en Waterschap zijn een soort partij.",
                   "Tussen actoren alleen structurele relaties (deel van, lid van, voorzitter van); een handeling loopt "
                   "via rollen en processen of een gebeurtenis.",
                   "Een externe partij wordt alleen een actor bij een structurele relatie met de gemeente "
                   "(opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht).")),
    Elementtype(
        "rol", "Rol", "Business Role", "business-role", "bedrijfsarchitectuur", "rol",
        "Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden.",
        "ArchiMate", True, "Verantwoordelijkheid of hoedanigheid (aanvrager, belastingplichtige, heffingsambtenaar).",
        "de hoedanigheid in de gangbare term (Houder van de begraafplaats; Rechthebbende op het graf)",
        (GGM_GEEN, GEMMA_MATCH,
         ("generiek GEMMA-element", "bij *generiek*: specialisatie van een generieke GEMMA-rol (`gemma_generiek`, "
                                    "exacte match), zoals Klant")),
        "Houder van de begraafplaats; Rechthebbende op het graf; Aanvrager", "gemeenteraad (actor)",
        eigenschappen=("doelgroep", "gemma", "gemma_generiek"), verplicht=("doelgroep",),
        afspraken=("Wat een rol met een object is, is toegang met een vaste verantwoordelijkheid; een handeling "
                   "(aanvragen, afgeven) is een toewijzing van de rol aan het proces dat het object gebruikt of maakt.",
                   "Een doelgroep (minima, jongeren) is geen rol maar een indeling van een actor.")),
    Elementtype(
        "bedrijfssamenwerking", "Bedrijfssamenwerking", "Business Collaboration", "business-collaboration",
        "bedrijfsarchitectuur", "bedrijfssamenwerking",
        "Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een "
        "specifiek collectief gedrag in een bepaalde context.", "ArchiMate", True,
        "Samenwerkingsverband zonder eigen rechtspersoon (Zorg- en Veiligheidshuis); met eigen rechtspersoon is het "
        "een actor.",
        "de gangbare naam van het verband",
        (GGM_GEEN, GEMMA_MATCH),
        "Zorg- en Veiligheidshuis", "GGD (eigen rechtspersoon: actor)",
        eigenschappen=("doelgroep", "gemma"), verplicht=("doelgroep",)),
    Elementtype(
        "kanaal", "Kanaal", "Business Interface", "business-interface", "bedrijfsarchitectuur", "kanaal",
        "Communicatiekanaal dat bij de dienstverlening wordt gebruikt. Elk kanaal kent verschillende vormen waarin "
        "informatie kan worden gedeeld.", "NORA", True, "Loket, website, telefoon.",
        "de gangbare naam van het kanaal",
        (GGM_GEEN, GEMMA_MATCH),
        "publieksbalie; gemeentelijke website", "klantcontact (gedrag)",
        eigenschappen=("doelgroep", "gemma"), verplicht=("doelgroep",),
        afspraken=("Kanalen vormen één centrale set: een onderwerp koppelt een dienst aan een bestaand kanaal; een "
                   "nieuw kanaal alleen na besluit van de redacteur.",)),
    Elementtype(
        "bedrijfsinteractie", "Bedrijfsinteractie", "Business Interaction", "business-interaction",
        "bedrijfsarchitectuur", "bedrijfsinteractie",
        "A unit of collective business behavior performed by two or more business actors, roles or collaborations.",
        "ArchiMate", False,
        "Gezamenlijk gedrag, zoals een ketensamenwerking waarin de bedrijfsprocessen van de partijen samenkomen (in het "
        "GEMMA-model het element Ketensamenwerking), of een keukentafelgesprek.",
        "als bij een bedrijfsproces: infinitief met het object (Bezorgen stoffelijk overschot)",
        (GGM_GEEN, GEMMA_MATCH),
        "Bezorgen stoffelijk overschot (ketensamenwerking van gemeente, arts en uitvaartondernemer)",
        "Treffen maatregel bij besmet lijk (de GGD adviseert alleen)",
        eigenschappen=("kernobject", "taakveld", "beleidsdomein", "gemma"),
        afspraken=("Een ketensamenwerking is een bedrijfsinteractie met een kernobject: het object dat door de keten "
                   "gaat. De bedrijfsprocessen van de partijen bedienen haar; een bedrijfssamenwerking of de rollen van "
                   "de partijen voeren haar uit. Het ketenproces erboven is impliciet en staat alleen in de beschrijving.",
                   "Elke nieuwe bedrijfsinteractie wordt voorgelegd: estafette (elke partij verantwoordelijk voor haar "
                   "deel: een bedrijfsinteractie) of orkestratie (één partij verantwoordelijk: geen interactie; voert "
                   "de gemeente het deel uit, dan specialiseert dat bedrijfsproces het GEMMA-proces *Leveren dienst aan "
                   "derden*).")),
    Elementtype(
        "beleidskader", "Beleidskader", "Driver", "driver", "motivatie", "beleidskader",
        "Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het "
        "kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden.", "NORA",
        True,
        "Een concreet benoemde regeling of richtlijn als geheel die voor alle gemeenten geldt: Europese regelgeving, "
        "rijksregelgeving, een landelijke richtlijn of een VNG-model van gemeentelijke regelgeving.",
        "de officiële citeertitel (Wet op de lijkbezorging); de afkorting wordt een synoniem",
        (GGM_GEEN, ("GEMMA-model", "match op betekenis; de motivatielaag van het GEMMA-model bevat nog vooral "
                                   "kernwaarden")),
        "Wet op de lijkbezorging; Archiefwet; AVG; Circulaire adresonderzoek BRP; Model-beheersverordening "
        "begraafplaatsen",
        "beheersverordening van één gemeente (blijft bron); artikel 16 (losse norm, buiten het model); 'verordening' "
        "als soort (bedrijfsobject Regeling)",
        eigenschappen=("regelgever", "taakveld", "beleidsdomein", "gemma", "kwaliteitsdoelen"), verplicht=("regelgever",),
        afspraken=("Een regeling of beleid van één gemeente blijft bron en wordt geen element; het VNG-model staat in "
                   "het model als gemeenschappelijke vorm.",
                   "Een beleidskader in de groep Richtlijn is geen wettelijke grondslag: zijn relatie heet *geeft "
                   "richtlijn voor*. Een beleidskader in Gemeentelijke regelgeving is alleen grondslag voor een "
                   "UPL-product of -dienst zonder landelijke grondslag, en werkt voor de rest de wet uit (*werkt uit "
                   "voor*).",
                   "De relaties naar een ander beleidskader (*werkt uit*, *verwijst naar*) en naar een rol, gebeurtenis "
                   "of bedrijfsobject zijn een uitbreiding op het GEMMA-kennismodel, dat een beleidskader alleen aan "
                   "een product en een kwaliteitsdoel koppelt.")),
    Elementtype(
        "kwaliteitsdoel", "Kwaliteitsdoel", "Goal", "goal", "motivatie", None,
        "Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de "
        "burgers en bedrijven.", "NORA", True,
        "Geen begrip uit een bron: de kwaliteitsdoelen staan vast in GEMMA (uit NORA en GEMMA). De wiki legt alleen vast "
        "welke beleidskaders er grondslag aan geven, en hoe sterk. Een doel van één beleidsveld (armoedebestrijding) is "
        "geen kwaliteitsdoel en geen element.",
        "de naam uit GEMMA, letterlijk (Privacy, Rechtmatig)",
        (("GEMMA-model", "een kwaliteitsdoel van GEMMA (GEMMA type Kwaliteitsdoel), op id; de wiki maakt er geen nieuw"),),
        "Privacy (de AVG geeft er grondslag aan)", "armoedebestrijding (een beleidsdoel)",
        afspraken=("Een kwaliteitsdoel krijgt geen pagina en geen beoordeling; het beleidskader noemt het in "
                   "`kwaliteitsdoelen`, met het GEMMA-id, de sterkte, een onderbouwing en de bronnen.",
                   "Sterkte: " + "; ".join(f"`{s}` {u}" for s, u in STERKTEN.items()) + "."),
        zonder_pagina="matchdoel (GEMMA)"),
    Elementtype(
        "data-object", "Data-object", "Data Object", "data-object", "applicatiearchitectuur", None,
        "Samenhangende set gegevens die geautomatiseerd kan worden verwerkt.", "GEMMA", True,
        "Nu een annotatie (`data_object: ja`) bij een begrip dat *geautomatiseerd verwerkt* wordt; voorbereiding op de "
        "applicatielaag. In GEMMA realiseert een data-object een bedrijfsobject.",
        "als het bedrijfsobject dat het realiseert",
        (("GGM", "matchdoel: een gegevensobject zonder sterke GGM-match wordt voorgelegd"),),
        "zaak in het zaaksysteem", "keukentafelgesprek",
        eigenschappen=("data_object", "ggm"),
        afspraken=("Gegevensvastlegging bepaalt nooit of iets een element is; *geautomatiseerd verwerkt* is alleen een "
                   "annotatie.",)),
    Elementtype(
        "groepering", "Groepering", "Grouping", "grouping", "overig", None,
        "Een groepering aggregeert of omvat concepten die bij elkaar horen op grond van een gemeenschappelijk kenmerk.",
        "ArchiMate", True,
        "Geen begrip uit een bron, maar een knoop van een indeling: taakveld, beleidsdomein, domein, groep van de "
        "Grondslagindeling. Zonder groepering heeft een indeling geen relaties in de export. Een groepering komt uit "
        "GEMMA, of de wiki maakt haar nieuw: een beleidsdomein dat GEMMA niet kent, een groep van de Grondslagindeling.",
        "de naam uit de indelingslijst (Iv3-taakveld, GGM-beleidsdomein, GEMMA-domein) of het brontype (Rijksregelgeving)",
        (("GEMMA-model", "de groepering van GEMMA met dezelfde naam en hetzelfde GEMMA type; anders een nieuwe groepering "
                         "in de map van de wiki, met een terugmelding"),
         ("GGM", "het beleidsdomein: per beleidsdomein de dekking")),
        "Burgerzaken (beleidsdomein)", "lijkbezorging als thema (een onderwerp, geen groepering)",
        afspraken=("Een groepering krijgt geen pagina en geen beoordeling; het script maakt haar bij de export uit de "
                   "indelingsvelden van de elementen. De beschrijving van een beleidsdomein staat in het register van "
                   "beleidsdomeinen.",
                   "Een begrip dat alleen een thema is, wordt geen groepering en geen element."),
        zonder_pagina="indeling"),
]
ELEMENTTYPE = {e.sleutel: e for e in ELEMENTTYPEN}
VAN_ARCHIMATE = {e.archimate_type: e for e in ELEMENTTYPEN}
PAGINATYPEN = sorted({e.paginatype for e in ELEMENTTYPEN if e.paginatype})
VERPLICHT = {e.paginatype: e.verplicht for e in ELEMENTTYPEN if e.verplicht and e.paginatype != "bedrijfsproces"}


def typevelden(sleutel: str) -> tuple[str | None, str, str]:
    """(paginatype, ArchiMate-type, GEMMA-naam) van een elementtype of een elementtype zonder element."""
    if sleutel in ELEMENTTYPE:
        e = ELEMENTTYPE[sleutel]
        return e.paginatype, e.archimate_type, e.naam
    z = ZONDER[sleutel]
    return None, z.archimate_type, z.naam


def sleutel_van(archimate_type: str) -> str | None:
    e = VAN_ARCHIMATE.get(archimate_type)
    return e.sleutel if e else None


# --- Elementtypen die niet tot een element leiden ---


@dataclass(frozen=True)
class ZonderElement:
    sleutel: str
    naam: str
    engels: str
    archimate_type: str
    laag: str
    reden: str
    over_gemma: str = ""  # de naam in Over GEMMA, als die afwijkt of bestaat


ZONDER_ELEMENT: list[ZonderElement] = [
    ZonderElement("representatie", "Representatie", "Representation", "representation", "bedrijfsarchitectuur",
                  "De waarneembare vorm (document, formulier, register, bericht) van de informatie van een object: "
                  "vermelden bij dat object, geen pagina."),
    ZonderElement("locatie", "Locatie", "Location", "location", "overig",
                  "Een fysieke plaats als zodanig: geen pagina. Een gebiedsindeling als gegeven is een bedrijfsobject."),
    ZonderElement("uitkomst", "Uitkomst", "Outcome", "outcome", "motivatie", "Buiten dit model."),
    ZonderElement("principe", "Principe", "Principle", "principle", "motivatie", "Buiten dit model.",
                  "Architectuurprincipe"),
    ZonderElement("eis", "Eis", "Requirement", "requirement", "motivatie",
                  "Buiten dit model: een losse norm uit één artikel ('binnen acht weken beslissen') is een eis of "
                  "beperking; de regeling als geheel is een beleidskader of blijft bron.", "Requirement, Implicatie"),
    ZonderElement("beperking", "Beperking", "Constraint", "constraint", "motivatie", "Buiten dit model, als een eis.",
                  "Standaard"),
    ZonderElement("waarde", "Waarde", "Value", "value", "motivatie", "Buiten dit model."),
    ZonderElement("kernwaarde", "Kernwaarde", "Driver", "driver", "motivatie",
                  "Buiten dit model: een fundamentele overtuiging waaraan overheidsdienstverlening moet voldoen. Ook een "
                  "Driver; alleen het beleidskader is een element.", "Kernwaarde"),
    ZonderElement("vermogen", "Vermogen", "Capability", "capability", "motivatie",
                  "Buiten dit model (strategielaag): \"wat de gemeente kan\" is geen bedrijfsfunctie.", "Capability"),
    ZonderElement("applicatiecomponent", "Applicatiecomponent", "Application Component", "application-component",
                  "applicatiearchitectuur", "De applicatielaag is nog niet gebouwd.", "Applicatiecomponent"),
    ZonderElement("applicatieservice", "Applicatieservice", "Application Service", "application-service",
                  "applicatiearchitectuur", "De applicatielaag is nog niet gebouwd.", "Applicatieservice"),
    ZonderElement("applicatiefunctie", "Applicatiefunctie", "Application Function", "application-function",
                  "applicatiearchitectuur", "De applicatielaag is nog niet gebouwd.", "Applicatiefunctie"),
    ZonderElement("applicatie-interface", "Applicatie-interface", "Application Interface", "application-interface",
                  "applicatiearchitectuur", "De applicatielaag is nog niet gebouwd.", "Applicatie-interface"),
    ZonderElement("applicatieproces", "Applicatieproces", "Application Process", "application-process",
                  "applicatiearchitectuur", "De applicatielaag is nog niet gebouwd.", "Applicatieproces"),
    ZonderElement("applicatie-event", "Applicatie-event", "Application Event", "application-event",
                  "applicatiearchitectuur", "De applicatielaag is nog niet gebouwd.", "Applicatie-event"),
]
ZONDER = {z.sleutel: z for z in ZONDER_ELEMENT}

# --- Relaties ---

GEDRAG = ("bedrijfsproces", "bedrijfsfunctie", "gebeurtenis", "dienst", "bedrijfsinteractie")
OBJECT = ("bedrijfsobject", "afspraak")
PARTIJ = ("actor", "rol", "bedrijfssamenwerking", "kanaal")


@dataclass(frozen=True)
class Relatie:
    bron: str
    soort: str  # Nederlandse relatienaam; associatie (gericht) voor een gerichte associatie
    doel: str
    over_gemma: bool  # staat in Over GEMMA (associatie in beide richtingen)
    namen: tuple = ()  # vaste namen; leeg: een vrije naam uit de bron
    kern: tuple = ()  # de kenmerken waarvoor dit de kernrelatie is
    toelichting: str = ""


H, V = tuple(HANDELINGEN), tuple(VERANTWOORDELIJKHEDEN)
UITBREIDING = "uitbreiding op het GEMMA-kennismodel"
RELATIES: list[Relatie] = [
    # Partijen
    Relatie("actor", "toewijzing", "rol", True, ("vervult",), ("vervult_een_rol",)),
    Relatie("actor", "aggregatie", "actor", False, ("omvat",), (), "structureel: deel van, lid van"),
    Relatie("actor", "associatie (gericht)", "actor", False, ("is voorzitter van",), (),
            "alleen een structurele relatie"),
    Relatie("bedrijfssamenwerking", "aggregatie", "rol", True),
    Relatie("bedrijfssamenwerking", "aggregatie", "actor", True),
    Relatie("bedrijfssamenwerking", "toewijzing", "bedrijfsproces", True, (), ("voert_gedrag_uit",)),
    Relatie("bedrijfssamenwerking", "toewijzing", "bedrijfsfunctie", False, (), ("voert_gedrag_uit",)),
    Relatie("bedrijfssamenwerking", "toewijzing", "bedrijfsinteractie", False, (), ("voert_gedrag_uit",)),
    Relatie("bedrijfssamenwerking", "toegang", "bedrijfsobject", False, V, (), "een verantwoordelijkheid, als bij een rol"),
    Relatie("rol", "toewijzing", "bedrijfsproces", True, (), ("voert_gedrag_uit", "toegewezen_partij")),
    Relatie("rol", "toewijzing", "bedrijfsfunctie", True, (), ("voert_gedrag_uit",)),
    Relatie("rol", "toewijzing", "bedrijfsinteractie", False, (), ("voert_gedrag_uit", "toegewezen_partij")),
    Relatie("rol", "toegang", "bedrijfsobject", True, V, (), "een verantwoordelijkheid; *partij* alleen naar een afspraak"),
    Relatie("rol", "toegang", "afspraak", False, V, ()),
    Relatie("rol", "aggregatie", "rol", True),
    Relatie("rol", "specialisatie", "rol", True, ("is een",)),
    Relatie("kanaal", "toewijzing", "dienst", True, (), ("ontsluit_een_dienst",)),
    Relatie("kanaal", "bediening", "rol", True),
    # Gedrag
    Relatie("bedrijfsproces", "toegang", "bedrijfsobject", True, H, ("wordt_bewerkt",)),
    Relatie("bedrijfsproces", "toegang", "afspraak", False, H, ("wordt_bewerkt",)),
    Relatie("bedrijfsfunctie", "toegang", "bedrijfsobject", True, H, ("wordt_bewerkt",)),
    Relatie("bedrijfsinteractie", "toegang", "bedrijfsobject", False, H, ("wordt_bewerkt",)),
    Relatie("bedrijfsproces", "realisatie", "dienst", True, ("realiseert",), ("gerealiseerd_door",)),
    Relatie("bedrijfsfunctie", "realisatie", "dienst", True, ("realiseert",), ("gerealiseerd_door",)),
    Relatie("bedrijfsfunctie", "bediening", "bedrijfsproces", True, ("bedient",), ("bedient_gedrag",)),
    Relatie("bedrijfsproces", "bediening", "bedrijfsfunctie", True, ("bedient",)),
    Relatie("bedrijfsproces", "bediening", "bedrijfsinteractie", False, (), (),
            "de bedrijfsprocessen van de partijen bedienen de ketensamenwerking"),
    Relatie("bedrijfsfunctie", "aggregatie", "bedrijfsfunctie", True, ("omvat",), (), "de GEMMA-functieketen"),
    Relatie("bedrijfsfunctie", "aggregatie", "dienst", False, ("omvat",), (), "Functie-indeling naar domein"),
    Relatie("bedrijfsproces", "aggregatie", "bedrijfsproces", True, ("omvat",), ("omvat_processen",),
            "levensloopproces of cluster naar soort werk → bedrijfsproces"),
    Relatie("bedrijfsproces", "aggregatie", "gebeurtenis", False, ("omvat",), (),
            "levensloopproces → gebeurtenis van zijn kernobject"),
    Relatie("bedrijfsproces", "specialisatie", "bedrijfsproces", True, ("is een",)),
    Relatie("bedrijfsproces", "triggering", "bedrijfsproces", True, ("leidt tot",)),
    Relatie("bedrijfsproces", "triggering", "gebeurtenis", True, ("leidt tot",)),
    Relatie("bedrijfsproces", "stroom", "bedrijfsproces", False, (), (), "geeft iets door aan een ander proces"),
    Relatie("gebeurtenis", "triggering", "bedrijfsproces", True, ("leidt tot",), ("leidt_tot_gedrag",)),
    Relatie("gebeurtenis", "triggering", "bedrijfsinteractie", False, ("start",), ("leidt_tot_gedrag",)),
    Relatie("gebeurtenis", "triggering", "gebeurtenis", False, (), (), "een rechtsgevolg dat een ander teweegbrengt"),
    Relatie("gebeurtenis", "specialisatie", "gebeurtenis", False, ("is een",), (), "naar een generieke gebeurtenis"),
    Relatie("dienst", "bediening", "bedrijfsproces", True, ("bedient",)),
    Relatie("dienst", "bediening", "rol", True, ("bedient",), (), "de rol van de afnemer"),
    Relatie("dienst", "aggregatie", "dienst", True, ("omvat",)),
    Relatie("dienst", "specialisatie", "dienst", False, ("is een",), (), "naar een generieke dienst"),
    # Aanbod
    Relatie("product", "aggregatie", "dienst", True, ("omvat",), ("omvat_diensten_en_afspraken",)),
    Relatie("product", "aggregatie", "afspraak", True, ("omvat",), ("omvat_diensten_en_afspraken",)),
    Relatie("product", "bediening", "rol", True, ("bedient",), (), "de rol van de afnemer, een specialisatie van Klant"),
    # Objecten
    Relatie("bedrijfsobject", "associatie (gericht)", "bedrijfsobject", True),
    Relatie("bedrijfsobject", "aggregatie", "bedrijfsobject", True, ("bevat",)),
    Relatie("bedrijfsobject", "compositie", "bedrijfsobject", True, ("bevat",)),
    Relatie("bedrijfsobject", "specialisatie", "bedrijfsobject", True, ("is een",)),
    Relatie("afspraak", "associatie (gericht)", "bedrijfsobject", False),
    # Motivatie
    *[Relatie("beleidskader", "associatie (gericht)", doel, doel == "product", tuple(GRONDSLAGNAMEN),
              ("is_grondslag_voor",), "de grondslag; bij voorkeur naar een product")
      for doel in ("product", "dienst", "bedrijfsproces")],
    Relatie("beleidskader", "associatie (gericht)", "beleidskader", False, ("werkt uit", "verwijst naar"), (),
            "een AMvB of VNG-model werkt een wet uit"),
    *[Relatie("beleidskader", "associatie (gericht)", doel, False,
              ("is grondslag voor", "is model voor") if doel == "bedrijfsobject" else ("is grondslag voor",), (),
              f"de regeling die {naam} regelt" + ("; *is model voor*: een VNG-model voor de soort regeling "
                                                     "(Regeling)" if doel == "bedrijfsobject" else ""))
      for doel, naam in (("rol", "de rol"), ("gebeurtenis", "de gebeurtenis"), ("bedrijfsobject", "het object"))],
    Relatie("beleidskader", "invloed", "kwaliteitsdoel", True, ("geeft grondslag aan",), (),
            "met een sterkte; het kwaliteitsdoel is een element van GEMMA (veld `kwaliteitsdoelen`)"),
    # Applicatie
    Relatie("data-object", "realisatie", "bedrijfsobject", True, (), (), "nu een annotatie"),
    # Indelingen: de groeperingen van de Beleidsdomeinindeling, de Functie-indeling naar domein en de Grondslagindeling
    Relatie("groepering", "aggregatie", "groepering", True, (), (), "taakveld → beleidsdomein; domein → beleidsdomein"),
    *[Relatie("groepering", "aggregatie", doel, doel in ("bedrijfsobject", "bedrijfsfunctie", "rol"), (), (), toelichting)
      for doel, toelichting in (
        ("bedrijfsobject", "Beleidsdomeinindeling"),
        ("afspraak", "Beleidsdomeinindeling"),
        ("product", "Beleidsdomeinindeling; Functie-indeling naar domein"),
        ("dienst", "Beleidsdomeinindeling"),
        ("bedrijfsproces", "Beleidsdomeinindeling: alleen een levensloopproces"),
        ("bedrijfsinteractie", "Beleidsdomeinindeling"),
        ("bedrijfsfunctie", "Functie-indeling naar domein: alleen een functie op domeinniveau"),
        ("beleidskader", "Beleidsdomeinindeling; Grondslagindeling"),
        ("actor", "Doelgroepindeling"),
        ("rol", "Doelgroepindeling"),
        ("bedrijfssamenwerking", "Doelgroepindeling"),
        ("kanaal", "Doelgroepindeling"))],
]


@dataclass(frozen=True)
class Weggefilterd:
    bron: tuple
    soort: tuple  # Nederlandse relatienamen; "*" = elke relatie die niet is toegestaan
    doel: tuple
    reden: str


ALLE = ("*",)
WEGGEFILTERD: list[Weggefilterd] = [
    Weggefilterd(("actor",), ("toewijzing", "toegang", "associatie"), GEDRAG + OBJECT,
                 "een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol"),
    Weggefilterd(("actor",), ("toewijzing",), ("actor", "bedrijfssamenwerking", "kanaal"),
                 "tussen partijen is alleen *actor vervult rol* een toewijzing"),
    Weggefilterd(("rol", "bedrijfssamenwerking"), ("toewijzing",), PARTIJ,
                 "tussen partijen is alleen *actor vervult rol* een toewijzing"),
    Weggefilterd(("rol", "bedrijfssamenwerking"), ("toewijzing",), ("dienst",),
                 "een dienst krijgt geen rol toegewezen: de rol hangt aan het proces of de functie die de dienst "
                 "realiseert"),
    Weggefilterd(("rol",), ("associatie",), OBJECT,
                 "wat een rol met een object is, is toegang met een verantwoordelijkheid; een handeling is een "
                 "toewijzing van de rol aan het proces"),
    Weggefilterd(("rol",), ("associatie",), ("rol",),
                 "een handeling tussen rollen loopt via een proces (toewijzing), een stroom of een gebeurtenis, zoals "
                 "tussen actoren"),
    Weggefilterd(("kanaal",), ALLE, ALLE, "een kanaal is toegewezen aan een dienst en bedient een rol"),
    Weggefilterd(("bedrijfsfunctie",), ("aggregatie", "compositie"), ("bedrijfsproces",),
                 "een functie bedient een proces; processen groeperen in een cluster naar soort werk"),
    Weggefilterd(("dienst",), ("toegang",), OBJECT,
                 "een dienst heeft geen toegang tot een object; het proces dat haar realiseert wel"),
    Weggefilterd(("gebeurtenis",), ("associatie",), OBJECT,
                 "het object volgt uit het levensloopproces waaronder de gebeurtenis hangt"),
    Weggefilterd(OBJECT, ("associatie",), ("dienst",),
                 "een object hangt via het proces dat de dienst realiseert (toegang) aan een dienst"),
]


def kale_soort(soort: str) -> str:
    """`toegang (registreren)` → toegang; `associatie (gericht)` → associatie."""
    return soort.split(" (")[0]


def toegestaan(bron: str, soort: str, doel: str) -> Relatie | None:
    """De relatie in het kennismodel tussen twee elementtypen (sleutels), of None."""
    s = kale_soort(soort)
    return next((r for r in RELATIES if (r.bron, kale_soort(r.soort), r.doel) == (bron, s, doel)), None)


def weggefilterd(bron: str, soort: str, doel: str) -> Weggefilterd | None:
    """De reden waarom een relatie niet in het kennismodel staat, als die er is; None bij een toegestane relatie."""
    if toegestaan(bron, soort, doel):
        return None
    s = kale_soort(soort)
    return next((w for w in WEGGEFILTERD if bron in w.bron and (w.soort == ALLE or s in w.soort)
                 and (w.doel == ALLE or doel in w.doel)), None)


def toegangstype(naam: str | None) -> str | None:
    """ArchiMate-toegangstype (lezen, schrijven, lezen-schrijven) bij een handeling of verantwoordelijkheid."""
    return HANDELINGEN.get(naam) or VERANTWOORDELIJKHEDEN.get(naam)


def kernrelaties(kenmerk: str) -> list[Relatie]:
    return [r for r in RELATIES if kenmerk in r.kern]


# --- Indelingen ---


@dataclass(frozen=True)
class Indeling:
    naam: str
    wat: str
    waarnaar: str
    typen: dict  # elementtype-sleutel → voorwaarde (None: altijd)
    niveaus: str
    groepering: str  # GEMMA | GEMMA, uitgebreid | wiki
    in_archi: str
    velden: tuple
    afspraken: tuple = ()


INDELINGEN: list[Indeling] = [
    Indeling("Beleidsdomeinindeling", "objecten, aanbod, beleidskaders, en de bovenste knoop van de processen",
             "het taakveld (Iv3) en het beleidsdomein",
             {"bedrijfsobject": None, "afspraak": None, "product": None, "dienst": None, "beleidskader": None,
              "bedrijfsproces": "alleen een levensloopproces, onder het beleidsdomein van zijn kernobject",
              "bedrijfsinteractie": "onder het beleidsdomein van haar kernobject"},
             "taakveld › beleidsdomein › element", "GEMMA",
             "aggregatie vanuit de groepering van het beleidsdomein; een beleidsdomein dat GEMMA niet kent wordt een "
             "nieuwe groepering onder het taakveld, in de map van de wiki", ("taakveld", "beleidsdomein"),
             ("Een bedrijfsobject heeft één beleidsdomein; het beleidsdomein van een levensloopproces en een "
              "bedrijfsinteractie volgt uit hun kernobject.",
              "Een beleidsdomein dat GEMMA niet kent, wordt een gemeentelijk beleidsdomein met een terugmelding; zijn "
              "beschrijving staat in het register van beleidsdomeinen.",
              "Het domein van een product of dienst past bij de GEMMA-domeinen van zijn beleidsdomein.")),
    Indeling("Functie-indeling naar domein", "functies, producten en diensten", "het GEMMA-domein",
             {"bedrijfsfunctie": None, "product": None, "dienst": None},
             "domein › functie (de keten tot het domeinniveau) › dienst; domein › product", "GEMMA",
             "aggregatie vanuit de domeingroepering (een functie op domeinniveau, een product) of vanuit de "
             "bovenliggende functie (een functie, een dienst)", ("domein",),
             ("De Functie-indeling is een relatie, geen eigenschap: de bovenliggende functie wordt een element en "
              "aggregeert de functie eronder, volgens de GEMMA-functieketen, tot en met de functie op domeinniveau "
              "(GEMMA type *Bedrijfsfunctie domein*); alleen die hangt via `domein` aan de domeingroepering.",
              "Een dienst hangt onder één functie in hetzelfde domein.",
              "Een product hangt via `domein` direct aan de domeingroepering: ArchiMate laat een functie geen product "
              "aggregeren. De diensten die het omvat, hangen onder hun functie.",
              "Een functie bedient een proces; ze aggregeert geen proces.")),
    Indeling("Procesindeling naar kernobject", "processen, gebeurtenissen en ketensamenwerkingen", "het kernobject",
             {"bedrijfsproces": "levensloopproces en bedrijfsproces", "gebeurtenis": None, "bedrijfsinteractie": None},
             "levensloopproces (per kernobject) › bedrijfsproces; een gebeurtenis onder het levensloopproces van het "
             "object waarvan de toestand verandert; een bedrijfsinteractie bij haar kernobject", "wiki",
             "aggregatie; in de map Procesindeling naar kernobject, een bedrijfsinteractie in de map Ketensamenwerking",
             ("kernobject",),
             ("Strikt hiërarchisch: per kernobject één levensloopproces, of één per partij als ze samen een "
              "bedrijfsinteractie met dat kernobject bedienen; een levensloopproces aggregeert geen levensloopproces; "
              "een bedrijfsproces hangt onder hoogstens één levensloopproces.",
              "Het taakveld en beleidsdomein van een levensloopproces en een bedrijfsinteractie zijn die van hun "
              "kernobject.")),
    Indeling("Procesindeling naar soort werk", "bedrijfsprocessen; via generieke GEMMA-elementen ook gebeurtenissen, "
                                               "diensten en rollen", "de soort werk (het processenlandschap van GEMMA)",
             {"bedrijfsproces": "cluster naar soort werk en bedrijfsproces", "gebeurtenis": "bij *generiek*",
              "dienst": "bij *generiek*", "rol": "bij *generiek*"},
             "generiek GEMMA-element › cluster naar soort werk › bedrijfsproces", "GEMMA, uitgebreid",
             "specialisatie naar het generieke GEMMA-element (exacte match); aggregatie van cluster naar bedrijfsproces",
             ("gemma_generiek",),
             ("Specialisatie en bediening naar GEMMA lopen alleen via een exacte match.",
              "Een cluster naar soort werk breidt het processenlandschap uit zonder GEMMA-elementen te wijzigen.")),
    Indeling("Doelgroepindeling", "partijen en kanalen", "de doelgroep",
             {"actor": None, "rol": None, "bedrijfssamenwerking": None, "kanaal": None},
             "doelgroep (gemeente, inwoners en ondernemers, ketenpartners) › element", "wiki",
             "aggregatie vanuit de groepering van de doelgroep, in de map Doelgroepindeling", ("doelgroep",),
             ("Een doelgroep is een ordening, geen hoedanigheid: in de wiki een groepering. GEMMA modelleert de "
              "doelgroep als rol (GEMMA type *Groep*) die applicatieservices ordent; die afwijking is teruggemeld.",)),
    Indeling("Grondslagindeling", "beleidskaders", "het brontype van de regeling, afgeleid uit de regelgever",
             {"beleidskader": None},
             "groep (Europese regelgeving, Rijksregelgeving, Richtlijn, Gemeentelijke regelgeving) › beleidskader",
             "wiki", "aggregatie vanuit de groep; groep en map heten als het brontype, in de map Grondslagindeling",
             ("regelgever",),
             ("Alleen gevulde groepen bestaan.",
              "De naam van de relatie van een beleidskader volgt de groep: *is grondslag voor*, *werkt uit voor* of "
              "*geeft richtlijn voor*.")),
]
INDELING = {i.naam: i for i in INDELINGEN}
ALGEMENE_INDELINGSAFSPRAKEN = (
    "Alles ingedeeld: elk element staat in minstens één indeling, ook in de export.",
    "GEMMA volgen: de GEMMA-indelingen blijven ongewijzigd; een nieuwe indeling komt er alleen waar GEMMA er geen heeft, "
    "en een tweede elementtype met hetzelfde criterium valt in de bestaande indeling.",
    "Specialisatie koppelt aan een GEMMA-indeling (wat voor soort is het?), aggregatie aan een eigen indeling (waar "
    "hoort het bij?).",
    "Bij voorkeur hiërarchisch; meer ouders geeft een signaal, behalve de twee ouders van een bedrijfsproces "
    "(levensloopproces en cluster naar soort werk).",
)

# Grondslagindeling: een beleidskader valt onder het brontype van zijn regeling (regel Bronvoorrang), afgeleid uit de
# regelgever. Groep en map heten als het brontype; de omschrijving is die van de regel Bronvoorrang.
REGELGEVER_BRONTYPE = {"EU": "europese-regelgeving", "rijk": "rijksregelgeving", "landelijke organisatie": "richtlijn",
                       "VNG-model": "gemeentelijke-regelgeving"}
BRONTYPE_OMSCHRIJVING = {
    "europese-regelgeving": "Regelgeving van de Europese Unie die voor alle gemeenten geldt, zoals verordeningen die "
                            "rechtstreeks werken (AVG, AI-verordening).",
    "rijksregelgeving": "Regelgeving van het Rijk die voor alle gemeenten gelijk is: wetten, algemene maatregelen van "
                        "bestuur en ministeriële regelingen, en door Nederland goedgekeurde verdragen.",
    "richtlijn": "Landelijke uitvoeringsvoorschriften, handleidingen, circulaires en handreikingen van het Rijk, "
                 "uitvoeringsorganisaties en koepels (HUP van RvIG, NVVB, VNG, Divosa).",
    "gemeentelijke-regelgeving": "Verordeningen, nadere regels, beleidsregels en regelingen van gemeenschappelijke "
                                 "regelingen, die elke gemeente zelf vaststelt, en de VNG-modellen daarvan. Omdat de "
                                 "inhoud per gemeente verschilt, staat in het model het VNG-model als gemeenschappelijke "
                                 "vorm; de regeling van één gemeente is een voorbeeld en geen element.",
}


def brontype_naam(brontype: str) -> str:
    """De naam van een brontype als groep of map: `europese-regelgeving` → Europese regelgeving."""
    return brontype.replace("-", " ").capitalize()


def grondslaggroep(data: dict) -> str | None:
    """De groep van een beleidskader in de Grondslagindeling (ook zijn submap): de naam van zijn brontype."""
    brontype = REGELGEVER_BRONTYPE.get(data.get("regelgever"))
    return brontype_naam(brontype) if brontype else None


def indelingen_van(sleutel: str) -> list[tuple[Indeling, str | None]]:
    return [(i, i.typen[sleutel]) for i in INDELINGEN if sleutel in i.typen]


def paginatypen_in(indeling: str) -> tuple[str, ...]:
    """De paginatypen die altijd (zonder voorwaarde) in een indeling vallen."""
    return tuple(dict.fromkeys(ELEMENTTYPE[s].paginatype for s, voorwaarde in INDELING[indeling].typen.items()
                               if voorwaarde is None))


def indeling_tekst(paginatype: str) -> str:
    """De indelingen van een paginatype, in één zin."""
    delen = []
    for e in ELEMENTTYPEN:
        if e.paginatype != paginatype:
            continue
        for i, voorwaarde in indelingen_van(e.sleutel):
            tekst = i.naam + (f" ({voorwaarde})" if voorwaarde else "")
            if tekst not in delen:
                delen.append(tekst)
    return "; ".join(delen)


# --- Pagina's ---

GEGENEREERD = "<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->"
ARCHI_SPECIALISATIE = "In de export: specialisatie naar het GEMMA-element."


def _cel(tekst) -> str:
    return " ".join(("" if tekst is None else str(tekst)).split()).replace("|", "\\|")


def _tabel(kolommen: list[str], rijen: list[list]) -> list[str]:
    return ["| " + " | ".join(kolommen) + " |", "|" + "---|" * len(kolommen),
            *["| " + " | ".join(_cel(c) for c in rij) + " |" for rij in rijen], ""]


def _pagina(pid: str, titel: str, regels: list[str]) -> str:
    body = "\n".join(regels).strip("\n")
    while "\n\n\n" in body:
        body = body.replace("\n\n\n", "\n\n")
    return f"---\nid: {pid}\ntype: kennismodel\ntitel: {titel}\n---\n\n# {titel}\n\n{GEGENEREERD}\n\n{body}\n"


def _naam(sleutel: str) -> str:
    return (ELEMENTTYPE.get(sleutel) or ZONDER[sleutel]).naam


def _pad(e: Elementtype) -> str:
    return f"{e.laag}/{e.sleutel}-modelleerafspraken.md"


def _link(sleutel: str, van: str = "") -> str:
    """Link naar de modelleerafspraken van een elementtype, vanaf de map `van` binnen kennismodel/."""
    e = ELEMENTTYPE[sleutel]
    pad = _pad(e) if not van else (f"{e.sleutel}-modelleerafspraken.md" if van == e.laag else f"../{_pad(e)}")
    return f"[{e.naam}]({pad})"


def _namen(r: Relatie) -> str:
    if r.namen == H:
        return "een handeling: " + ", ".join(f"{n} ({HANDELINGEN[n]})" for n in H)
    if r.namen == V:
        return "een verantwoordelijkheid: " + ", ".join(f"{n} ({VERANTWOORDELIJKHEDEN[n]})" for n in V)
    if r.bron == "groepering":
        return "geen: het script maakt de relatie uit de indelingsvelden"
    return ", ".join(r.namen) if r.namen else "vrij, uit de bron"


def _kenmerknaam(sleutel: str) -> str:
    import bepaal_type

    return bepaal_type.NAAM[sleutel]


def _typedefs(e: Elementtype) -> list:
    import bepaal_type

    return [t for t in bepaal_type.TYPEN if t.archimate_type == e.archimate_type and t.paginatype == e.paginatype]


def _herken(e: Elementtype) -> list[str]:
    import bepaal_type

    regels = []
    for t in _typedefs(e):
        kop = "" if len(_typedefs(e)) == 1 else f"{t.naam}: "
        moet = [f"*{_kenmerknaam(t.kern)}* (kernrelatie)"] + [f"*{_kenmerknaam(s)}*" for s in t.eis]
        tekst = f"{kop}{t.bepaald_door}. Moet ja: {', '.join(moet)}"
        if t.drempel:
            tekst += f"; hoogstens {bepaal_type.DREMPEL_ONTBREKEND} nee: " + ", ".join(
                f"*{_kenmerknaam(s)}*" for s in t.drempel)
        regels.append(tekst + ".")
    return regels


def modelleerafspraken(e: Elementtype) -> str:
    van = e.laag
    kaart = [["Definitie", f"{e.definitie} ({e.herkomst})"],
             ["In Over GEMMA", f"ja ({e.naam})" if e.over_gemma else f"nee: {UITBREIDING}"],
             ["Duiding", e.duiding]]
    herken = _herken(e)
    if herken:
        kaart.append(["Herken je aan", " ".join(herken) + " Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md)."])
    kern = [r for r in RELATIES if r.kern and (r.doel == e.sleutel or r.bron == e.sleutel)
            and any(k in {t.kern for t in _typedefs(e)} for k in r.kern)]
    if kern:
        kaart.append(["Kernrelatie", "; ".join(f"{_naam(r.bron)} ─{r.soort}→ {_naam(r.doel)}" for r in kern)])
    if e.niveaus:
        kaart.append(["Niveaus", " · ".join(e.niveaus)])
    if e.eigenschappen:
        kaart.append(["Eigenschappen", " · ".join(
            f"`{v}`{' (verplicht)' if v in e.verplicht else ''}: {EIGENSCHAPPEN[v]}"
            + (f" ({', '.join(WAARDEN[v])})" if v in WAARDEN else "") for v in e.eigenschappen)])
    ind = indelingen_van(e.sleutel)
    if ind:
        kaart.append(["Indelingen", "; ".join(f"[{i.naam}](../indelingen.md)" + (f" ({w})" if w else "")
                                                for i, w in ind)])
    kaart += [["Naamvorm", e.naamvorm],
              ["Afstemming", " · ".join(f"{doel}: {tekst}" for doel, tekst in e.afstemming)],
              ["Voorbeeld", f"wel: {e.wel} · niet: {e.niet}"]]
    regels = [f"*{e.engels}* in ArchiMate · laag {LAGEN[e.laag]}"
              + (f" · paginatype `{e.paginatype}`" if e.paginatype else f" · geen pagina ({e.zonder_pagina})"), "",
              *_tabel(["Afspraak", "Inhoud"], kaart)]
    if e.afspraken:
        regels += ["## Afspraken", "", *[f"- {a}" for a in e.afspraken], ""]
    rijen = []
    for r in RELATIES:
        for richting, ander in (("uit", r.doel), ("in", r.bron)):
            if (r.bron if richting == "uit" else r.doel) != e.sleutel or (richting == "in" and r.bron == r.doel):
                continue
            rijen.append([richting, r.soort, _link(ander, van) if ander in ELEMENTTYPE else _naam(ander), _namen(r),
                          ", ".join(f"*{_kenmerknaam(k)}*" for k in r.kern) if r.kern else "",
                          "ja" if r.over_gemma else f"nee: {UITBREIDING}", r.toelichting])
    if rijen:
        regels += ["## Relaties", "",
                   "In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een "
                   "uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een "
                   "terugmelding over het kennismodel.", "",
                   *_tabel(["Richting", "Relatie", "Ander type", "Namen", "Kern", "In Over GEMMA", "Toelichting"], rijen)]
    weg = [w for w in WEGGEFILTERD if e.sleutel in w.bron or e.sleutel in w.doel]
    if weg:
        regels += ["## Weggefilterd", "",
                   "Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar "
                   "weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.", "",
                   *_tabel(["Relatie", "Reden"], [[_weg_tekst(w, e.sleutel), w.reden] for w in weg])]
    return _pagina(f"{e.sleutel}-modelleerafspraken", f"{e.naam} — modelleerafspraken", regels)


def _weg_tekst(w: Weggefilterd, sleutel: str) -> str:
    """De weggefilterde relatie, vanuit het type van de pagina: aan de andere kant alleen dat type."""
    def kant(t, alleen_dit):
        return _naam(sleutel) if alleen_dit else ("elk type" if t == ALLE else ", ".join(_naam(s) for s in t))

    soort = "andere relatie" if w.soort == ALLE else " of ".join(w.soort)
    bron_hier = sleutel in w.bron
    return f"{kant(w.bron, bron_hier and len(w.bron) > 1)} ─{soort}→ {kant(w.doel, not bron_hier)}"


def weggefilterd_pagina(laag: str) -> str:
    rijen = [[f"{z.naam} ({z.engels})", z.over_gemma or "—", z.reden] for z in ZONDER_ELEMENT if z.laag == laag]
    regels = [f"Elementtypen van de laag {LAGEN[laag]} die niet tot een element van dit model leiden. Een begrip "
              "van zo'n type krijgt de uitkomst uit de beslistabel (geen pagina, of buiten dit model).", "",
              *_tabel(["Elementtype", "In Over GEMMA", "Reden"], rijen)]
    return _pagina(f"{laag}-weggefilterd", f"{LAGEN[laag]} — weggefilterd", regels)


def readme() -> str:
    regels = ["Wat het model is: de elementtypen per architectuurlaag, de relaties ertussen en de indelingen. Het "
              "kennismodel is metadata; het telt niets. Waarom het model zo is, staat in [ARCHITECTURE.md]"
              "(../ARCHITECTURE.md); de regels voor het modelleren, met de voorrang, in "
              "[modelleerregels](modelleerregels.md); de vragen die een begrip een type geven in "
              "[kenmerken en beslistabel](kenmerken-en-beslistabel.md).", "",
              "Twee markeringen zijn verschillend:", "",
              "- **Weggefilterd**: niet in het kennismodel van de wiki. Een beoordeling legt elke gevonden relatie "
              "vast; de export laat een weggefilterde relatie weg, met de reden.",
              "- **Niet in Over GEMMA**: wel in het kennismodel van de wiki, maar niet in het GEMMA-kennismodel (Over "
              f"GEMMA): een {UITBREIDING}. Het gaat mee in de export, gemarkeerd, en is een kandidaat voor een "
              "terugmelding over het kennismodel.", ""]
    for laag, laagnaam in LAGEN.items():
        rijen = [[_link(e.sleutel), e.engels, f"`{e.paginatype}`" if e.paginatype else e.zonder_pagina,
                  "ja" if e.over_gemma else "nee"] for e in ELEMENTTYPEN if e.laag == laag]
        regels += [f"## {laagnaam}", "",
                   *(_tabel(["Elementtype", "ArchiMate", "Paginatype", "In Over GEMMA"], rijen) if rijen else []),
                   f"Elementtypen zonder element: [weggefilterd]({laag}/weggefilterd.md) ("
                   + ", ".join(z.naam.lower() for z in ZONDER_ELEMENT if z.laag == laag) + ").", ""]
    regels += ["## Relatietypen", "",
               *_tabel(["Relatie", "ArchiMate", "Betekenis"],
                       [[n, RELATIETYPEN[n], RELATIETYPE_UITLEG[n]] for n in RELATIETYPEN]),
               "De vaste namen: een **handeling** van gedrag op een object ("
               + ", ".join(f"{n}: {t}" for n, t in HANDELINGEN.items()) + "), een **verantwoordelijkheid** van een rol "
               "voor een object (" + ", ".join(f"{n}: {t}" for n, t in VERANTWOORDELIJKHEDEN.items())
               + "), en de **grondslag** van een beleidskader ("
               + "; ".join(f"*{n}*: {t}" for n, t in GRONDSLAGNAMEN.items()) + ").", ""]
    typen = [e.sleutel for e in ELEMENTTYPEN if e.paginatype]
    kort = {e.sleutel: e.naam for e in ELEMENTTYPEN}
    cellen = {}
    for r in RELATIES:
        if r.bron in typen and r.doel in typen:
            cellen.setdefault((r.bron, r.doel), []).append(kale_soort(r.soort) + ("" if r.over_gemma else "*"))
    regels += ["## Relatiematrix", "",
               "Per brontype (rij) en doeltype (kolom) de toegestane relaties; \\* is een uitbreiding op het "
               "GEMMA-kennismodel. Een leeg vak: weggefilterd.", "",
               *_tabel(["Van \\ naar", *[kort[t] for t in typen]],
                       [[kort[b], *[", ".join(cellen.get((b, d), [])) for d in typen]] for b in typen])]
    regels += ["## Indelingen", "", *_tabel(["Indeling", "Deelt in", "Naar", "Groepering"],
                                            [[f"[{i.naam}](indelingen.md)", i.wat, i.waarnaar, i.groepering]
                                             for i in INDELINGEN])]
    return _pagina("kennismodel", "Kennismodel", regels)


def indelingen_pagina() -> str:
    regels = ["Waar staat elk element in het model? Een **indeling** ordent naar één criterium, met benoemde niveaus. "
              "Een view toont één indeling voor één of meer elementtypen.", "",
              "## Voor alle indelingen", "", *[f"- {a}" for a in ALGEMENE_INDELINGSAFSPRAKEN], ""]
    for i in INDELINGEN:
        typen = "; ".join(_link(s) + (f" ({w})" if w else "") for s, w in i.typen.items())
        rijen = [["Deelt in", typen], ["Naar", i.waarnaar], ["Niveaus", i.niveaus], ["Groepering", i.groepering],
                 ["In Archi", i.in_archi], ["Eigenschappen", ", ".join(f"`{v}`" for v in i.velden)]]
        regels += [f"## {i.naam}", "", *_tabel(["", ""], rijen)]
        if i.naam == "Grondslagindeling":
            regels += _tabel(["Regelgever", "Groep", "Omschrijving"],
                             [[r, brontype_naam(b), BRONTYPE_OMSCHRIJVING[b]] for r, b in REGELGEVER_BRONTYPE.items()])
        regels += [*[f"- {a}" for a in i.afspraken], ""]
    return _pagina("indelingen", "Indelingen", regels)


def kenmerken_pagina() -> str:
    import bepaal_type

    regels = ["Elk begrip uit een bron krijgt één keer dezelfde vragen: de kenmerken. De beslistabel past daar vaste "
              "regels op toe; de uitkomst is het type, of de reden waarom het begrip geen eigen pagina krijgt. Er wordt "
              "nooit eerst een type gekozen. Per elementtype staat in zijn modelleerafspraken welke kenmerken het type "
              "bepalen, welke de kernrelatie is en welke drempel geldt.", "",
              *bepaal_type.doc_stap0(), *bepaal_type.doc_vragentabel(), *bepaal_type.doc_stappen()]
    regels = [r[1:] if r.startswith("### ") else r for r in regels]
    return _pagina("kenmerken-en-beslistabel", "Kenmerken en beslistabel", regels)


def paginas() -> dict[str, str]:
    """Pad (relatief aan de wiki) → inhoud van elke gegenereerde pagina in kennismodel/."""
    uit = {f"{MAP}/README.md": readme(), f"{MAP}/indelingen.md": indelingen_pagina(),
           f"{MAP}/kenmerken-en-beslistabel.md": kenmerken_pagina()}
    for e in ELEMENTTYPEN:
        uit[f"{MAP}/{_pad(e)}"] = modelleerafspraken(e)
    for laag in LAGEN:
        uit[f"{MAP}/{laag}/weggefilterd.md"] = weggefilterd_pagina(laag)
    return uit


def main(argv: list[str] | None = None) -> int:
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args(argv)
    for pad in paginas():
        print(pad)
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.exit(main())
