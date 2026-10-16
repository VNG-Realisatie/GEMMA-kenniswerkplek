---
id: modelleerregels
type: kennismodel
titel: Modelleerregels
---

# Modelleerregels

De regels die voor alle elementen gelden, met de voorrang. Wat per elementtype geldt (kernrelatie, niveaus, naamvorm, relaties), staat in zijn modelleerafspraken; het overzicht in het [kennismodel](README.md), de vragen in [kenmerken en beslistabel](kenmerken-en-beslistabel.md). De werkwijze van de AI staat in [AGENTS.md](../AGENTS.md), het waarom in [ARCHITECTURE.md](../ARCHITECTURE.md). Deze pagina is met de hand geschreven.

Verwijs naar een regel met haar naam ("regel Thuishoren"). *(schema)* en *(script)* houden een fout tegen, *(signaal)* geeft een waarschuwing die de AI inhoudelijk beoordeelt; zonder markering is het een regel voor het oordeel van de AI.

## Voorrang

### Bronvoorrang

Voor welke begrippen er zijn en wat ze formeel betekenen, gaat het hogere brontype voor (per bron in `sources/index/`; de volgorde in `wiki.yaml` `bronvoorrang`):

1. `europese-regelgeving`: regelgeving van de EU die voor alle gemeenten geldt, zoals verordeningen die rechtstreeks werken (AVG, AI-verordening).
2. `rijksregelgeving`: wetten, algemene maatregelen van bestuur, ministeriële regelingen en door Nederland goedgekeurde verdragen.
3. `informatiemodel`: RSGB, RGBZ, catalogi van basisregistraties, en architectuurmodellen zoals de UPL-lijsten.
4. `richtlijn`: landelijke uitvoeringsvoorschriften, handleidingen, circulaires en handreikingen (HUP van RvIG, NVVB, VNG, Divosa). Een bron, nooit een element, ook niet als geheel (regel Wettelijke grondslag).
5. `gemeentelijke-regelgeving`: verordeningen, nadere regels, beleidsregels en regelingen van gemeenschappelijke regelingen, en de VNG-modelverordeningen. De regeling van één gemeente is een voorbeeld, geen element. Een VNG-modelverordening is de gemeenschappelijke vorm van een gemeentelijke regeling, zonder eigen rechtskracht: een bron, nooit grondslag (regel Wettelijke grondslag).
6. `beleid`: intern gericht beleid van een gemeente (beleidsnota's, visies, programma's).
7. `overig`: praktijk, zoals productpagina's, websites en presentaties.

- Voorrang bepaalt nooit of iets een element is.
- Naam en herkenbare definitie komen uit de gangbare taal van `richtlijn`, `beleid` en `overig`; de wetsterm wordt een synoniem met context "wet". Precedent: Urn, niet Asbus.
- `europese-regelgeving` en `rijksregelgeving` heten samen landelijke regelgeving.
- Een matchdoel (brontype `model`: het GGM, het GEMMA-model en GEMMA Online, ook de redactionele tekst) is geen bron en valt buiten de volgorde: het dient voor matchen en, zoals gemeentelijke beleidsstukken, voor termen en taal, niet voor een claim. *(signaal; ook bij een bron van brontype `model` in een kenmerk of relatie)*
- Wat een functie is, steunt op de wet die de groep taken aan de gemeente toewijst, niet op GEMMA. De UPL is bron én matchdoel.
- Een bron voor de methode (Over GEMMA, Proceshiërarchie, Impact van ketensamenwerking; brontype `overig`) onderbouwt het kennismodel en een keuze voor type of niveau, niet de inhoud (ARCHITECTURE.md, sectie 2).
- De plek in een overgenomen indeling steunt op de relatie uit het model (regel Elke claim een bron).

### Een element modelleren, in deze volgorde

1. Welk begrip? Synoniem of homoniem (stap 0 van de beslistabel).
2. Grondslag: de juiste landelijke wettelijke bron, met het artikel (regel Wettelijke grondslag).
3. Kenmerken → type, via de beslistabel. De uitkomst is bindend (regel Beslistabel beslist).
4. Kernrelaties, uit dezelfde wettekst.
5. Indeling en indelingsrelaties ([indelingen](indelingen.md)).
6. Overige relaties, uit de bronduiding.
7. Matches.

### Matchen

De AI matcht op betekenis (regel Match op betekenis), met de kandidaten uit `tools/ggm.py` en `tools/gemma.py`; het script haalt de letterlijke velden op.

| Match | Typen | Wat het doet | Zonder match |
|---|---|---|---|
| UPL (ook bron) | dienst | elk UPL-item wordt een dienst en valt nooit weg; de naam letterlijk uit de UPL | procesarchitectuur-terugmelding |
| GGM | bedrijfsobject, en voor het data-object ook rol, actor en gebeurtenis; beleidsdomein | matchdoel en toets: entiteit, definitie, relaties; per beleidsdomein de dekking | GGM-terugmelding (hiaat) |
| GEMMA-model | alle elementtypen | het id gaat mee in de export en overschrijft naam en definitie; zwak of partieel voorleggen | nieuw element via de export; GEMMA-terugmelding als een GEMMA-element vervalt |
| Generiek GEMMA-element | gebeurtenis, rol, dienst, bedrijfsproces | specialisatie (`gemma_generiek`) | voorstel aan GEMMA |
| GEMMA-kennismodel (Over GEMMA) | elementtypen en relatietypen | namen en definities van de typen | in de export gemarkeerd als niet in Over GEMMA |
| Indelingslijsten | typen met een indeling | Iv3-taakveld, GGM-beleidsdomein, GEMMA-domein, GEMMA-procesarchitectuur (soort werk) | nieuwe groepering in de export; terugmelding |

### Relaties

Bij het beoordelen vaak tegelijk, uit dezelfde wettekst:

1. grondslag (*is grondslag voor* vanuit een beleidskader);
2. kernrelatie van het type;
3. indelingsrelaties (levensloopproces → aggregatie → bedrijfsproces, functieketen, kernobject);
4. overige relaties uit de bronduiding (per partij wat zij houdt, beheert, uitvoert of vervult; toegang met een handeling of verantwoordelijkheid);
5. de GGM-match van de relatie, alleen bij bedrijfsobjecten, data-objecten en beleidsdomeinen;
6. GEMMA (geen match: de relatie gaat als nieuw mee in de export).

Welke relaties tussen twee typen toegestaan of weggefilterd zijn, met de reden, staat in de modelleerafspraken van het type.

## Oordeel

- **Beslistabel beslist**
  - Of een begrip een element is en van welk type, volgt alleen uit de kenmerken en de beslistabel (skill `gemma-archimate-model-criteria`). De uitkomst typeert een begrip uit een bron ("wat is het?"). *(script)*
  - Registratie, eigendom, systeembeheer, regie of een extern systeem zijn geen argument, ook niet impliciet of als synoniem ("wat de gemeente registreert", "registratieobject", "eigendom ligt bij X", "regie, niet registratie"). Bij een bedrijfsobject mag de tekst de registratie noemen; de gegevens staan in het data-object, dat het script afleidt uit de GGM-match. *(signaal bij registr*-taal, niet bij een bedrijfsobject)*
  - Een GGM-entiteit heeft een eigen classificatie, is geen begrip en wordt pas via een bron beoordeeld.
  - Een kenmerk *ja* dat een kernrelatie is, heeft die relatie bij het element of bij wat eronder ligt: een bedrijfsproces onder het levensloopproces, een proces of functie onder of bediend door de functie, een specialisatie met pagina, een gebeurtenis die het element triggert; niet bij een dienst zonder grondslag (regel Wettelijke grondslag). *(signaal)*
- **Match op betekenis** — Op betekenis, niet op naam: herken homoniemen en synoniemen, volg relaties en generalisaties. Lees de modellen alleen via `tools/ggm.py` en `tools/gemma.py`, nooit direct of via kopieën. *(script: de gekozen match bestaat; signaal bij een afwijkende modelnaam)*
- **Zwakke match voorleggen** — Een GEMMA-match `zwak` of `partieel` leg je voor, met wat er in GEMMA verandert: de export (skill `gemma-archimate-model-archimate-export`) neemt het GEMMA-id over en overschrijft naam en definitie. De export vertrouwt de match. Past het GEMMA-element niet echt, kies dan `sterkte: geen` en noem het in de onderbouwing.
- **Eén element in het hele model** — Eén betekenis is één element, ook als meer onderwerpen het gebruiken.
  - Zoek vóór het beoordelen in alle beoordelingen op naam en synoniemen. Bestaat het al, werk die beoordeling bij: je onderwerp in `onderwerpen`, wat alleen daar geldt onder `per_onderwerp`.
  - Zelfde begrip, andere naam: `synoniem_van`; zelfde naam, andere betekenis: `homoniemen` (regel Match op betekenis). *(signaal: dezelfde naam of hetzelfde synoniem in twee beoordelingen zonder `synoniem_van` of `homoniemen`; dezelfde GEMMA- of GGM-match, exact of sterk, bij twee elementen)*
- **Thuishoren** — Elk element heeft één thuisonderwerp, het eerste in `onderwerpen`: dat beoordeelt het, ook *betekenis in onderwerp*; de andere gebruiken het met relaties en `per_onderwerp`. De inhoud beslist:
  - een bedrijfsobject: het eigen onderwerp waar het ontstaat en beheerd wordt; anders een thematisch gedeeld onderwerp (Besluitvorming, Bestuur en organisatie, Heffingen en betalingen …), ook voor een generiek element; anders Kern;
  - een proces, dienst of product: het onderwerp van zijn kernobject; een gebeurtenis: dat van het object waarvan de toestand verandert;
  - een actor, rol, functie, beleidskader of kanaal: het onderwerp dat het gebruikt, en een thematisch gedeeld onderwerp of Kern zodra meer onderwerpen het gebruiken; de organen en de organisatie van de gemeente: Bestuur en organisatie.
  - Het `niveau` van een onderwerp: `eigen` (één taak uit landelijke regelgeving, met eigen kernobjecten), `thematisch` (begrippen die meer eigen onderwerpen op dezelfde manier gebruiken, uit een eigen algemene regeling) of `kern` (te breed voor een thema); criteria in ARCHITECTURE.md, sectie 3.3.
  - Een indeling uit een model (de GEMMA-functiehiërarchie, een beleidsdomein) is geen onderwerp: een knoop daarvan krijgt geen beoordeling (ARCHITECTURE.md, sectie 4.4).
  - Het aantal relaties is een aanwijzing; de volgorde van inlezen is geen argument.
  - Volgt het thuis eenduidig uit de inhoud, dan verplaatst de AI zonder voorleggen en noemt het ter bevestiging; bij twijfel voorleggen. Verplaatsen gaat per geval (regel Per geval), via de volgorde van `onderwerpen`; het Archi-object blijft.
  - Hoort een begrip bij een onderwerp dat nog niet bestaat: uitkomst verwijzing.
  - De omschrijving van een onderwerp noemt zijn kernobjecten en wat erbuiten valt, met het thuis daarvan.
  - *(signaal: kernobject met een ander thuisonderwerp; verwijzing naar een onderwerp dat nu bestaat; element met meer relaties naar één ander onderwerp dan naar het eigen, generieke elementen en elementen van een gedeeld onderwerp of Kern uitgezonderd)*
- **Relaties tussen onderwerpen** — Een gewone relatie, in de beoordeling van het bronelement, waar de bronnen haar noemen (`tools/relaties.py voorstel` kijkt over alle onderwerpen); verwijs, herhaal niet. Is het bronelement van een ander onderwerp en goedgekeurd, dan gaat het opnieuw ter beoordeling. Elk element heeft minstens één relatie, behalve een dienst zonder grondslag; de samenhang staat in `voortgang.md`. *(signaal: element zonder relatie)*
- **Gemeentelijk perspectief** — Beschrijf wat de gemeente ziet, doet en beslist.
  - Een dienst of proces met een eigen handeling van de gemeente hoort erbij, ook als een ander (rechtbank, minister) beslist.
  - Een externe partij (UWV, IND, COA, GGD …) wordt alleen een element bij een structurele relatie: opdrachtgever, mede-eigenaar (gemeenschappelijke regeling), prestatieafspraken of een wettelijke overlegplicht. Alleen context of afbakening, of alleen per geval op verzoek (gedeputeerde staten als beroepsinstantie): *gemeentelijk* nee, in de beschrijving. Precedenten: GGD wel (mede-eigenaar en opdrachtgever); Officier van justitie en Arts als behandelende arts (meld- en overlegplicht met de gemeentelijke lijkschouwer).
  - De interne processen en rollen van een ketenpartner blijven buiten scope.
  - Een begrip "geen element" blijft in de begrippenlijst, met de uitkomst en de reden.

## Bronnen

- **Tegenspraak** — Leg beide bronnen vast en markeer de tegenspraak. Formeel geldt de regel Bronvoorrang; de afwijkende bron blijft vermeld als afwijking in de praktijk.
- **Wettelijke grondslag** — Het model geldt voor alle gemeenten: elk element heeft een landelijke wettelijke bron (`europese-regelgeving` of `rijksregelgeving`), met het artikel. *(script; signaal: een element zonder landelijke wettelijke bron)*
  - Een relatie heeft geen eigen landelijke grondslag nodig: een bron volstaat (regel Elke claim een bron).
  - `richtlijn`, `beleid` en `overig` dienen voor taal, voorbeelden, werkwijze en lacunes, niet als onderbouwing; een grondslag uit de UPL geldt pas na controle in de wettekst.
  - De hoek *zonder grondslag*, de enige uitzondering: een UPL-dienst blijft, ook zonder landelijke wettelijke grondslag. Zij is geen wettelijke taak: een pagina zonder processen, objecten, gebeurtenissen of rollen; *gerealiseerd door* steunt op de bron. Zij wordt teruggemeld aan de procesarchitectuur (ook als de UPL een grondslag noemt die geen taak geeft) en niet geëxporteerd. Het script herkent haar (de UPL als bron, geen landelijke regelgeving, geen *is grondslag voor* van een beleidskader van de EU of het Rijk) en zet haar op `elementpaginas/overig/zonder-grondslag.md` (ARCHITECTURE.md, secties 3.4 en 6.3). *(script: een bedrijfsproces dat zo'n dienst realiseert; signaal: een ontbrekende procesarchitectuur-terugmelding)*
  - Een element zonder landelijke wettelijke bron blijft niet, ook geen product of dienst buiten de UPL.
  - Staat de grondslag eenduidig in de nagelezen wettekst, dan voegt de AI bron en *is grondslag voor* toe zonder voorleggen en noemt het ter bevestiging; bij twijfel voorleggen.
  - Een bedrijfsfunctie volgt de grondslag van wat zij omvat of bedient. Een bladfunctie van GEMMA die een proces van een onderwerp bedient, met een bron, wordt een element; wat zij is, steunt op de wet (regel Bronvoorrang). Een functie erboven is een knoop zonder beoordeling, met `gemma_functie` (ARCHITECTURE.md, sectie 4.4). Een functie die geen proces bedient, is geen element.
  - De grondslag is de relatie *is grondslag voor* van een beleidskader van de EU of het Rijk. Een VNG-modelverordening is nooit grondslag: zij *werkt uit voor*, ook bij een UPL-dienst zonder landelijke grondslag. Een landelijke richtlijn wordt nooit een beleidskader. De groep volgt de Grondslagindeling ([indelingen](indelingen.md)). *(script: is grondslag voor vanuit een VNG-modelverordening; schema: geen regelgever voor een richtlijn)*

## Tekst

- **Begrijpelijk** — Herkenbaar voor domeinexperts; geen jargon tenzij nodig. De definitie is één zin. *(signaal)*
- **Los van het onderwerp** — Definitie en beschrijving gelden in elk onderwerp; toets: past de tekst ongewijzigd in elk ander onderwerp? Wat een element in één onderwerp doet, staat onder `per_onderwerp`. *(signaal)*
- **Naamvorm** — De naamvorm van het type staat in zijn modelleerafspraken: een proces "Behandelen aanvraag", een functie "Vergunningverlening", een gebeurtenis "Overlijden", een dienst vanuit de afnemer "Melding openbare ruimte doen". Het zelfstandig naamwoord uit de bron wordt een synoniem met context "beleid". Een product of dienst uit de UPL houdt de UPL-naam letterlijk ("Verlof tot begraven"), met een synoniem waar dat betekenis toevoegt. *(signaal)*

## Terugmelden en export

- **Afwijken mits teruggemeld** — Het model mag afwijken van de UPL-indeling (taakveld, GEMMA-domein) en van het kennismodel procesarchitectuur, mits teruggemeld in de procesarchitectuur-terugmeldingen; de terugmelding dekt dan het signaal. *(signaal)*
- **Objectbehoud** — Hernoemen, samenvoegen of splitsen maakt niet vanzelf een nieuw object in Archi: de redacteur gebruikt de objecten in views, en de export werkt views niet bij. `object_van` in de beoordeling noemt het object dat het element voortzet (het begrip-id van het oude begrip, met `wijziging` en `datum`): bij hernoemen altijd; bij samenvoegen en splitsen beslist de redacteur of en welk object blijft. *(script: het veld klopt; de export weigert een typewijziging van een voortgezet object)*
