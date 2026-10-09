# Architectuur van de wiki gemma-archimate-model

Dit document is leidend: het zegt waarom het model is zoals het is en hoe de wiki werkt. Wat het model is (elementtypen, relaties, indelingen) en de regels voor het modelleren staan in het [kennismodel](kennismodel/README.md), met de [modelleerregels](kennismodel/modelleerregels.md). De werkwijze van de AI staat in [AGENTS.md](AGENTS.md), de stappen en sjablonen in de skills. De wiki is van het type `curation`; de algemene opzet staat in de `ARCHITECTURE.md` van de repository.

## 1 Doel

Deze wiki bouwt een onderbouwd, herleidbaar GEMMA-architectuurmodel van de bedrijfslaag, voor het GEMMA-team van VNG: bedrijfsobjecten, afspraken, producten, diensten, processen, functies, gebeurtenissen, actoren, rollen, samenwerkingen, kanalen en bedrijfsinteracties, met de beleidskaders uit de motivatielaag. Het resultaat is de export naar Archi, die in het GEMMA-model wordt geïmporteerd. Het model voedt een landelijke standaard; kwaliteit en herleidbaarheid gaan daarom voor snelheid.

## 2 Plaats in de keten

```text
bronnen                                     matchdoelen
wetten, informatiemodellen (UPL, RSGB),     GGM · GEMMA-model · UPL · Over GEMMA (kennismodel)
richtlijnen, beleid, praktijk               indelingslijsten (Iv3, GGM-beleidsdomeinen, GEMMA-domeinen,
        │                                   procesarchitectuur)
        ▼                                           │
   deze wiki  ◄─────────────── matchen ─────────────┘
        │
        ├──►  export naar Archi (.archimate, met de id's van GEMMA)  ──►  GEMMA-model
        └──►  terugmeldingen  ──►  GGM-beheer · werkgroep procesarchitectuur · GEMMA-team
```

- **Bronnen** zeggen welke begrippen er zijn en wat ze betekenen: landelijke regelgeving, informatiemodellen zoals de UPL, richtlijnen, gemeentelijke regelgeving (de VNG-modellen), beleid en praktijk. Hun voorrang staat in de regel Bronvoorrang.
- **Matchdoelen** zijn modellen waartegen de wiki een element toetst en koppelt: het GGM, het GEMMA-model, Over GEMMA (het GEMMA-kennismodel) en de indelingslijsten. Een matchdoel is geen bron: een claim steunt op een bron, niet op wat we ertegen matchen. De UPL is bron én matchdoel: zij noemt het aanbod van gemeenten, en een UPL-product valt nooit weg.
- **Terugmeldingen** gaan naar de beheerder van het matchdoel: een bevinding over het GGM naar GGM-beheer, over de UPL of het kennismodel procesarchitectuur naar de werkgroep procesarchitectuur, over het GEMMA-model zelf naar het GEMMA-team.

## 3 Uitgangspunten en voorrang

### 3.1 Herleidbaar model

Elk element, elk kenmerk en elke relatie is herleidbaar tot een bron, met de vindplaats, en elk besluit van de redacteur over het model staat bij het begrip of het onderwerp waarover het gaat. Herleidbaarheid geldt voor het model, niet voor de regels, de skills en de documentatie: die zijn consistent en overzichtelijk, en hun geschiedenis staat in Git. Een regel draagt dus geen datum en geen besluit mee, en een besluittekst noemt een regel of sectie bij naam, nooit een bestandspad; zo raakt een herstructurering van de wiki het model niet.

### 3.2 Zacht oordeel, harde vorm

| Wie | Wat | Waar |
|---|---|---|
| AI | het **oordeel** per begrip: kenmerken met onderbouwing en bron, naam, definitie, beschrijving, matches op betekenis, relaties, open vragen | `beoordelingen/begrippen/<id>.yaml` |
| redacteur | **besluiten** over wat is voorgelegd; vastgelegd door de AI | `besluiten:` in de beoordeling of het onderwerp |
| script | **beslissen**: type uit de beslistabel, status, letterlijke modelvelden, paginapad; harde controles en signalen | `status:` en `beslist:` in de beoordeling ([tools/beslissen.py](tools/beslissen.py)) |
| script | **renderen**: alle leesbare pagina's en overzichten | [tools/render.py](tools/render.py) |
| redacteur | **akkoord**, met het woord AKKOORD in de chat | `llmwiki promote`, `log.md` |

De AI oordeelt; het script beslist en rendert; de redacteur geeft akkoord. De AI schrijft dus geen pagina's, geen links en geen statussen. Wat een script garandeert of tegenhoudt, hoeft geen regel te zijn: de regels gaan over het oordeel.

### 3.3 Eén model

Een begrip komt één keer voor in het hele model, ook als meer onderwerpen het gebruiken; een gelijke naam met een andere betekenis is een homoniem. Andere onderwerpen gebruiken het element met een relatie en maken geen kopie. Waar een element thuishoort, volgt een voorrangsregel (regel Thuishoren): een bedrijfsobject hoort bij het eigen onderwerp waar het ontstaat en beheerd wordt, dan bij een thematisch gedeeld onderwerp, dan bij Kern; proces, dienst, product en gebeurtenis horen bij het onderwerp van hun kernobject; actor, rol, functie, beleidskader en kanaal hebben geen eigen thuis en gaan naar een gedeeld onderwerp of Kern zodra meer onderwerpen ze gebruiken. De inhoud beslist, niet het aantal relaties en niet de volgorde waarin onderwerpen zijn beoordeeld. Een begrip mag verhuizen; het object in Archi blijft.

| Laag | Onderwerpen | Voorbeelden |
|---|---|---|
| Eigen onderwerp | Burgerzaken, Lijkbezorging, Participatie, … | Graf, Reisdocument, Stoffelijk overschot |
| Thematisch gedeeld | Besluitvorming · Bestuur en organisatie · Heffingen en betalingen · Adressen en gebieden; groeit met het beoordelen | Besluit, Beschikking, Vergunning · Gemeente, College van B&W, Burgemeester · Heffing |
| Kern | Kern | wat echt overal is, bij voorkeur met een match in GGM 99-kern (Persoon, Adres, Zaak, Document); ook de bronnen over het kennismodel (Over GEMMA, Proceshiërarchie, Impact van ketensamenwerking) |

### 3.4 Voor alle gemeenten

Het GEMMA-model geldt voor alle gemeenten; elementen die van gemeente tot gemeente verschillen, horen er niet in. Daarom heeft elk element een landelijke wettelijke grondslag: een bron van brontype `europese-regelgeving` of `rijksregelgeving`, met het artikel (regel Wettelijke grondslag). Gemeentelijke regelgeving telt alleen als VNG-model, de gemeenschappelijke vorm; de verordening van één gemeente is een voorbeeld en een bron voor taal, niet voor het model, en een afwijking ervan is een afwijking in de praktijk. Richtlijnen, beleid en praktijk dienen voor taal, voorbeelden, werkwijze en het vinden van lacunes, niet als onderbouwing.

Eén uitzondering: een product of dienst uit de UPL blijft, ook zonder landelijke grondslag. Dan noemt het de grondslag in een VNG-model als die er is, en anders volgt een terugmelding aan de werkgroep procesarchitectuur. Zo'n product wordt niet uitgewerkt in processen, objecten of rollen, want die zouden per gemeente verschillen. Een bedrijfsfunctie volgt de grondslag van wat zij omvat. Een relatie heeft geen eigen grondslag nodig: dat is te gedetailleerd, en een bron volstaat, zoals bij elke claim.

### 3.5 GEMMA volgen, of afwijken en terugmelden

De wiki volgt de namen, definities, indelingen en modelleerafspraken van GEMMA. Waar de wiki afwijkt (een eigen indeling, een relatie die niet in Over GEMMA staat, een UPL-product onder een ander taakveld), meldt zij dat terug, met wat er nu staat, de bevinding en een voorstel. Het wiki-model wordt in GEMMA geïmporteerd en werkt gekoppelde GEMMA-elementen bij; een terugmelding zegt daarom wat de import verandert en wat het GEMMA-team moet controleren of beslissen. De import verwijdert niets: wat de wiki laat vervallen, blijft in GEMMA tot het GEMMA-team besluit.

### 3.6 Consistentie boven behoud

Een betere modellering gaat voor het vermijden van herbeoordeling. Wordt het resultaat beter van een andere regel, naam of indeling, dan worden de geraakte beoordelingen opnieuw beoordeeld en voorgelegd, per geval. Waar het kan, is een wijziging mechanisch: een relatietype toevoegen aan of weghalen uit het kennismodel is opnieuw filteren, geen herbeoordeling (§4.2).

### 3.7 Voorrang

Bij het modelleren geldt een vaste voorrang; de regels staan in de [modelleerregels](kennismodel/modelleerregels.md).

- **Bronnen:** europese-regelgeving › rijksregelgeving › informatiemodel › richtlijn › gemeentelijke-regelgeving › beleid › overig. Voorrang bepaalt wat formeel geldt en welke begrippen er zijn, nooit óf iets een element is. De naam komt uit de gangbare taal; de wetsterm wordt een synoniem.
- **Een element modelleren:** welk begrip (synoniem of homoniem) › grondslag › kenmerken en type › kernrelaties › indeling › overige relaties › matches.
- **Matchen:** op betekenis, niet op naam; een zwakke of partiële GEMMA-match wordt voorgelegd, omdat de export dan een GEMMA-element overschrijft.
- **Relaties:** grondslag › kernrelatie › indelingsrelaties › overige relaties uit de bronanalyse › GGM-match van de relatie › GEMMA.
- **Thuishoren:** eigen onderwerp › thematisch gedeeld › Kern (§3.3).

## 4 Het kennismodel

Het [kennismodel](kennismodel/README.md) beschrijft wat het model is: per architectuurlaag de elementtypen, per type de modelleerafspraken (definitie, herkenning, kernrelatie, drempel, niveaus, eigenschappen, indelingen, naamvorm, afstemming, toegestane en weggefilterde relaties), de relatietypen met de vaste namen, de indelingen, en per laag de elementtypen die niet tot een element leiden. Het is metadata: het telt niets. Het wordt gegenereerd uit één bron, [tools/kennismodel.py](tools/kennismodel.py); alleen de modelleerregels zijn met de hand geschreven. De scripts lezen het kennismodel in plaats van eigen tabellen te houden, zodat de documentatie, de beslistabel, de controles en de export niet uit de pas kunnen lopen. Dit hoofdstuk zegt waarom het zo is.

### 4.1 Elementtypen en kenmerken

- **Kenmerken eerst, type als uitkomst.** De AI beantwoordt neutrale vragen over het begrip (heeft het onderscheidbare exemplaren, is het gedrag, wordt het per keer doorlopen), elk met onderbouwing en bron. De beslistabel leidt daaruit het type af. Zo is het type toetsbaar en herhaalbaar, en wordt het geen keuze vooraf op gevoel. Registratie, eigendom of een systeem zijn geen argument: wat de gemeente vastlegt, zegt niets over wat een begrip is (regel Beslistabel beslist).
- **Per type een kernrelatie en een drempel.** Elk type heeft één kenmerk dat het type bepaalt, één kernrelatie die ja moet zijn (een proces heeft een toegewezen partij, een dienst wordt gerealiseerd door gedrag, een gebeurtenis start gedrag), en een drempel van overige kenmerken waarvan hoogstens één nee mag zijn. Daarmee krijgen alle typen een vergelijkbare, typische toets, en tellen overlappende kenmerken niet dubbel.
- **Namen uit het GEMMA-kennismodel.** De typen heten zoals in Over GEMMA (dienst, gebeurtenis, afspraak), met de GEMMA-definities waar die passen. De bedrijfsinteractie is een uitbreiding: GEMMA kent haar als element (*Ketensamenwerking*), niet in het kennismodel.
- **Een regeling.** Een concreet benoemde regeling als geheel die een taak, bevoegdheid of plicht van de gemeente regelt, wordt een beleidskader (motivatielaag); de soort regeling is het bedrijfsobject Regeling, dat de gemeente vaststelt en bekendmaakt; een los artikel valt buiten het model. Een landelijke richtlijn als geheel kan ook een beleidskader zijn, maar is geen wettelijke grondslag.
- **Wat geen element wordt.** Een representatie (bedrijfslaag) en een locatie (in ArchiMate een *Other*-element) zijn een vaste uitkomst zonder pagina; van de motivatielaag zit alleen het beleidskader in het model; een data-object is een annotatie bij een bedrijfsobject. Het kennismodel noemt per laag de typen die niet tot een element leiden, met de reden.
- **Groepering.** Een groepering (ook een *Other*-element) is geen begrip uit een bron, maar de knoop van een indeling: taakveld, beleidsdomein, domein, de groep van de Grondslagindeling. Zij krijgt geen pagina en geen beoordeling; het script maakt haar bij de export uit de indelingsvelden. Zonder groeperingen hebben de indelingen geen relaties in GEMMA; daarom staan de groepering en haar aggregaties in het kennismodel.

### 4.2 Relaties

- **Gevonden tegenover gefilterd.** Een beoordeling legt elke relatie vast die de bron noemt, mits zij geldig is in ArchiMate. De export neemt alleen de relaties mee die in het kennismodel staan; de rest staat op de pagina van het element en in het exportrapport. Zo gaat niets verloren wat de bron zegt, en is het kennismodel aanpassen opnieuw filteren in plaats van herbeoordelen.
- **Weggefilterd of niet in Over GEMMA.** Weggefilterd is een relatie die niet in het kennismodel van de wiki staat; de export laat haar weg, met de reden. Niet in Over GEMMA is een relatie die wel in het kennismodel van de wiki staat maar niet in het GEMMA-kennismodel: een uitbreiding, die gemarkeerd meegaat en kandidaat is voor een terugmelding.
- **Een actor via een rol.** Een actor vervult een rol en hangt alleen via die rol aan gedrag en objecten, zoals in GEMMA. Een rol mag ook aan een bedrijfsproces worden toegewezen, niet alleen aan een functie: GEMMA doet dat zelf op het niveau van het deelproces. Een functie bedient een proces in plaats van het te aggregeren.
- **Toegang met vaste namen.** Wat een rol met een object ís, is een verantwoordelijkheid: houder, bronhouder, beheerder, verstrekker, afnemer, toezichthouder, betrokkene, of partij bij een afspraak. Wat gedrag met een object dóét, is een handeling: registreren, bijwerken, beëindigen, raadplegen, verstrekken, en voor de archieffase bewaren, overbrengen en vernietigen. Beide reeksen komen uit de wetten van de basisregistraties, de AVG en de Archiefwet, en het ArchiMate-toegangstype volgt eruit. *Houder* in plaats van eigenaar, omdat de wetten van houden spreken en eigendom van gegevens geen juridisch begrip is; *afnemer* in plaats van raadpleger, omdat het de wettelijke term is en de plicht tot gebruik en terugmelden meedraagt; verwerkingsverantwoordelijke en zorgdrager zijn een toevoeging bij houder, geen eigen verantwoordelijkheid. De twee reeksen toetsen elkaar: een bronhouder hoort toegewezen te zijn aan gedrag dat registreert of bijwerkt, en een object met een levenscyclus hoort gedrag te hebben dat het registreert én beëindigt.
- **Grondslag als relatie.** Een beleidskader *is grondslag voor* wat het regelt, bij voorkeur een product; een VNG-model *werkt uit voor* wat de wet regelt en is alleen grondslag voor een UPL-product zonder landelijke grondslag; een richtlijn *geeft richtlijn voor*.
- **Kwaliteitsdoelen.** Een beleidskader *geeft grondslag aan* een kwaliteitsdoel van GEMMA (een invloed, met een sterkte), zoals Over GEMMA het voorschrijft: de regeling is de bindende basis voor het doel en bepaalt welke eisen en normen het moet vervullen. Het kwaliteitsdoel is een matchdoel: de wiki maakt er geen nieuw, maar kiest het uit GEMMA en onderbouwt de sterkte met de bepalingen van de regeling.
- **GGM-match van een relatie** alleen bij bedrijfsobjecten, data-objecten en beleidsdomeinen. Een relatie die het script uit een keten in het GGM afleidt (A–X–B wordt A–B), is een voorstel en geen match.

### 4.3 Processen en ketens

- **De GEMMA-ladder.** De procesniveaus volgen de proceshiërarchie van GEMMA: levensloopproces, bedrijfsproces, deelproces, processtap, handeling. Een specialisatie van een generiek GEMMA-proces is geen niveau.
- **Eén levensloopproces per kernobject.** Het levensloopproces omvat het gedrag over de levensloop van één exemplaar van een kernobject, van begin tot eind (*Beheren grafrechten*: van uitgifte tot verval), met GEMMA type *Bedrijfsproces (cluster)*. Zonder die groepering wordt elk van de honderden UPL-producten een los proces en wordt het model plat; met haar groeit het model met het aantal kernobjecten, niet met het aantal producten. Boven het levensloopproces staan geen procesniveaus maar de groeperingen taakveld en beleidsdomein, die uit het kernobject volgen.
- **Klant tot klant.** Een bedrijfsproces begint bij een aanleiding van buiten (verzoek, melding, gebeurtenis, termijn) en loopt door tot het resultaat voor de klant, onder verantwoordelijkheid van één organisatie. Wat voor hetzelfde geval op een ander proces volgt en pas samen daarmee de dienst levert, is een deelproces. Of een stap belangrijk is (eigen besluit, eigen normering), zegt niets over waar het klant-tot-klantproces begint en eindigt.
- **Deelproces zonder pagina.** Een deelproces krijgt geen pagina; het bedrijfsproces beschrijft zijn deelprocessen in volgorde, op de pagina en als eigenschap in Archi. Zo blijft het model op het abstractieniveau van GEMMA en heeft de procesontwerper toch het overzicht.
- **Een gebeurtenis start een bedrijfsproces.** Een gebeurtenis is een aanleiding van buiten of een rechtsgevolg van een proces, en start altijd een bedrijfsproces, nooit een deelproces. Een tussentoestand binnen één proces is geen element.
- **Geen ketenproces.** Waar de processen van meer partijen samenkomen, is dat bij een estafette een bedrijfsinteractie (ketensamenwerking), bediend door de bedrijfsprocessen van de partijen; het ketenproces erboven is impliciet en staat alleen in de beschrijving. Bij orkestratie voert de gemeente onder aansturing van een ander een deel uit, en specialiseert dat deel *Leveren dienst aan derden*. Een kernobject mag in een ketensamenwerking één levensloopproces per partij hebben.

### 4.4 Indelingen

- **GEMMA volgen.** De indelingen van GEMMA blijven en worden gevolgd: de Beleidsdomeinindeling (taakveld en beleidsdomein), de Functie-indeling naar domein en de Procesindeling naar soort werk (het processenlandschap). Een nieuwe indeling komt er alleen waar GEMMA er geen heeft: de Procesindeling naar kernobject (levensloopprocessen en ketensamenwerkingen), Ketensamenwerking als map, en de Grondslagindeling (beleidskaders naar het brontype van hun regeling).
- **Doelgroep als groepering.** GEMMA modelleert een doelgroep (gemeente, inwoners en ondernemers, ketenpartners) als rol die applicatieservices ordent. Een doelgroep is een ordening en geen hoedanigheid; in de wiki is zij daarom een groepering, die de actoren, rollen, samenwerkingen en kanalen van die doelgroep aggregeert. De afwijking is teruggemeld.
- **Alles ingedeeld.** Elk element staat in minstens één indeling, ook in Archi; er zijn geen wezen. Een functie zonder GEMMA-match breidt de functieketen van GEMMA uit, onder een bestaande GEMMA-functie.
- **Specialisatie of aggregatie.** Specialisatie koppelt aan een indeling van GEMMA (wat voor soort is het?), aggregatie aan een eigen indeling (waar hoort het bij?).
- **Hergebruik boven nieuwe indelingen.** Gebruikt een ander type hetzelfde criterium, dan valt het in de bestaande indeling: producten en diensten in de Beleidsdomeinindeling en de Functie-indeling, kanalen in de Doelgroepindeling. Een product hangt direct aan de domeingroepering, omdat een functie in ArchiMate geen product mag aggregeren.
- **Strikt hiërarchisch** waar het kan: een bedrijfsproces hangt onder één levensloopproces, een levensloopproces aggregeert geen levensloopproces, en het beleidsdomein van een levensloopproces is dat van zijn kernobject.
- Afwijken van de UPL-indeling of het GEMMA-domein mag, mits teruggemeld (regel Afwijken mits teruggemeld).

### 4.5 Synoniemen en homoniemen

Synoniemen en homoniemen zijn geen kenmerken van een begrip maar verhoudingen tussen een woord en een begrip. Ze komen daarom vóór de kenmerken, in stap 0 van de beslistabel: eerst vaststellen welk begrip bedoeld is. Een synoniem wordt geen element; het woord komt bij het element, met de context (wet, beleid, GGM, GEMMA). Een homoniem is breed: dezelfde naam voor een ander begrip, in elke bron en voor elk type; het begrip gaat door naar de kenmerken, de naamkeuze wordt voorgelegd en beide elementen verwijzen naar elkaar. Een actor of rol en een bedrijfsobject met dezelfde naam zijn een tegenhanger, geen homoniem. Een duplicaat (hetzelfde begrip twee keer in het GGM) is geen verhouding tussen begrippen en blijft bij de GGM-match.

## 5 Werkstroom en status

Skill [gemma-archimate-model-update](.agents/skills/gemma-archimate-model-update/SKILL.md) volgt de gedeelde `wiki-curatie-update`. Er is geen run: de werkboom is de toestand, en Git laat elke wijziging zien.

```text
 STAP                           WIE        RESULTAAT                                        STATUS
 1 Onderwerp                    AI+redact. beoordelingen/onderwerpen/<onderwerp>.yaml         —
 2 Bronnen en bronanalyse       AI         sources/, bronanalyses/                            —
 3 Beoordelen                   AI         beoordelingen/begrippen/<id>.yaml                  —
 4 Beslissen en renderen        script     status, beslist, alle pagina's                     kandidaat of review
 5 Voorleggen (één voor één)    AI→redact. besluiten: in de beoordeling → terug naar 4        kandidaat → review of afgewezen
 6 Bekijken                     redacteur  llmwiki promote plan; ter-beoordeling.md, pagina's, Source Control
 7 AKKOORD in de chat           redacteur
 8 Vastleggen                   script     llmwiki promote apply; log.md                      review → goedgekeurd
 9 Exporteren                   script     tools/archimate_export.py; export/                 —
10 Commit                       redact./AI pre-commit-controles
```

| Status | Wie | Wanneer |
|---|---|---|
| `kandidaat` | `tools/beslissen.py` | er staat een reden open die geen besluit van de redacteur dekt (de beslistabel zegt voorleggen, zoals bij een nieuwe bedrijfsinteractie of een kanaal, of een geautomatiseerd verwerkt object heeft geen sterke GGM-match) |
| `review` | `tools/beslissen.py` | niets meer voor te leggen; wacht op akkoord |
| `goedgekeurd` | `llmwiki promote apply`, na AKKOORD | met een regel in `log.md` met de hash van de inhoud van de beoordeling |
| `afgewezen` | `tools/beslissen.py`, na het besluit afwijzen | geen pagina; blijft in de begrippenlijst |

**Wanneer opnieuw akkoord.** De hash dekt de hele beoordeling behalve de scriptvelden `status` en `beslist`. Een inhoudelijke wijziging maakt een goedgekeurde beoordeling weer `review`; een andere opmaak, een nieuw script, een nieuwe modelrelease of een ander filter in het kennismodel niet. De pre-commit-controle `goedgekeurd-guard` weigert `goedgekeurd` zonder overeenkomende regel in `log.md`, en `log-alleen-aanvullen` weigert een gewijzigde of verwijderde regel.

**Besluiten.** Een besluit over een begrip staat in de `besluiten:` van zijn beoordeling, een besluit over een onderwerp als geheel in de `besluiten:` van het onderwerp; de begrippenlijst van een onderwerp toont ze. Er is geen apart register. Wat al besloten is, vraagt de AI niet opnieuw (regel Navragen). Een besluit over de werkwijze wordt verwerkt in de regel of de skill waar het hoort.

## 6 Hoe de wiki werkt

### 6.1 Plattegrond

```text
wikis/gemma-archimate-model/
├── ARCHITECTURE.md                   dit document: waarom en hoe (leidend)
├── AGENTS.md                         de werkwijze van de AI, met de kaart "Waar vind je wat"
├── wiki.yaml · todo.md · log.md      instellingen · open punten · akkoorden (alleen aan te vullen)
├── kennismodel/                      wat het model is (gegenereerd), met modelleerregels.md (met de hand)
├── plannen/<datum>-<titel>.md        plannen voor grotere wijzigingen; een plan dat klaar is, blijft als geschiedenis
├── beoordelingen/                    wat de AI schrijft (YAML)
│   ├── begrippen/<id>.yaml           het oordeel per begrip; status en beslist zet het script
│   ├── onderwerpen/<onderwerp>.yaml  naam, omschrijving, bronnen en besluiten van een onderwerp
│   ├── terugmeldingen/               registers per ontvanger: ggm.yaml, procesarchitectuur.yaml, gemma.yaml
│   ├── objecten.yaml                 welk Archi-object een hernoemd, samengevoegd of gesplitst element voortzet
│   └── beleidsdomeinen.yaml          de beschrijving van een beleidsdomein
├── bronanalyses/<onderwerp>/<brontype>/<bron-id>.md   wat een bron betekent voor de architectuur (AI)
├── bedrijfsarchitectuur/ · motivatie/ · begrippen/ · overzichten/   gegenereerd door tools/render.py
├── terugmeldingen/ · ter-beoordeling.md · voortgang.md              gegenereerd door tools/render.py
├── ggm/ · gemma/                     gegenereerd door tools/ggm.py en tools/gemma.py
├── export/                           het Archi-bestand en het exportrapport
├── schemas/                          beoordeling (gegenereerd), bronanalyse, kennismodel, lijst
├── tools/                            het gereedschap van deze wiki, met tests in tools/tests/
└── .agents/skills/                   hoe je het doet
```

### 6.2 Beoordelingen en registers

Een beoordeling is het oordeel van de AI over één begrip: kenmerken, naam, definitie, beschrijving, tekst per onderwerp, synoniemen en homoniemen, de matches met GGM en GEMMA, relaties, indelingsvelden, open vragen en besluiten. Het schema wordt gegenereerd uit de beslistabel ([tools/bepaal_type.py](tools/bepaal_type.py)). Een relatie staat één keer, in de beoordeling van het bronelement; de render zet de inkomende kant op de pagina van het doel. Naast de beoordelingen houdt de AI registers bij: de onderwerpen, de terugmeldingen per ontvanger (met wat er nu staat, **Bevinding:** en **Voorstel:**), de objecten die in Archi worden voortgezet, en de beschrijving van de beleidsdomeinen.

### 6.3 Beslissen, renderen en controles

[tools/beslissen.py](tools/beslissen.py) leest de beoordelingen, past de beslistabel toe, zet de status, haalt de letterlijke velden van de gekozen GGM- en GEMMA-match op, bepaalt het paginapad en roept daarna de render aan. Het houdt een fout tegen (er wordt dan niets geschreven): het schema, onvolledige kenmerken, een claim zonder bron, een bron zonder bronanalyse, een match die niet bestaat, een relatie die in ArchiMate niet geldig is of naar iets dat geen element is, een fout in de indeling of de hiërarchie, een ongeldige terugmelding, een handmatig gewijzigd modelbestand. [tools/signalen.py](tools/signalen.py) geeft signalen, met de naam van de regel: absolute taal, registratietaal, de naamvorm, een afwijkende modelnaam zonder synoniem, een kenmerk dat een kernrelatie is zonder die relatie, een relatie buiten het kennismodel, een element zonder relatie of zonder landelijke grondslag. Een signaal beoordeelt de AI inhoudelijk: oplossen of toelichten.

[tools/render.py](tools/render.py) maakt alle leesbare bestanden: de elementpagina's (de map volgt uit het type, de submappen uit de indelingsvelden), de begrippenlijst per onderwerp met de besluiten over het onderwerp, de overzichten per indeling, de terugmeldlijsten, `ter-beoordeling.md`, `voortgang.md` en het kennismodel. Het oordeelt niet en schrijft nooit in `beoordelingen/`; twee keer renderen geeft hetzelfde resultaat. Het garandeert de vorm: elke bronverwijzing is een link naar de bronanalyse, relaties staan in beide richtingen, verwijzingen staan als link in de tekst en niet in de frontmatter, er staan geen links naar tools of regels, en een relatie buiten het kennismodel staat erbij met de melding dat zij niet meegaat in de export. `render.py --check` in de pre-commit bewaakt dat de pagina's gelijk zijn aan de beoordelingen en het kennismodel aan zijn bron.

### 6.4 GGM en GEMMA als matchdoel lezen

| | GGM | GEMMA-model |
|---|---|---|
| Bronbestand | XMI (Enterprise Architect), brontype `model` | Archi-bestand `.archimate` (met map-id's en profielen, nodig voor de export), brontype `model` |
| Tool | [tools/ggm.py](tools/ggm.py) | [tools/gemma.py](tools/gemma.py) |
| Zoeken (AI) | `kandidaten`, `entiteit`, `naamgenoten`, `generalisaties`, `attribuut`, `relaties` | `kandidaten`, `element`, `koppel`, `zoek`, `groepering` |
| Letterlijke velden (script) | `velden` → `beslist.ggm` | `velden` → `beslist.gemma` |
| Nieuwe versie | skill gemma-archimate-model-ggm-release | skill gemma-archimate-model-gemma-release |

De AI kiest de match op betekenis; het script haalt bij elke run de letterlijke velden op, zodat een nieuwe release vanzelf meegaat. De modellen worden alleen via deze tools gelezen, nooit direct of via een kopie. Het GGM is matchdoel voor bedrijfsobjecten, data-objecten en beleidsdomeinen: per beleidsdomein wordt de dekking getoetst, en een hiaat wordt een GGM-terugmelding; een GGM-entiteit is zelf geen begrip en wordt pas via een bron beoordeeld. Het GEMMA-model is matchdoel voor alle typen: zijn id gaat mee in de export.

### 6.5 Export naar Archi

[tools/archimate_export.py](tools/archimate_export.py) schrijft de goedgekeurde elementen en relaties als `export/gemma-archimate-model.archimate`, om in Archi te bekijken en in het GEMMA-model te importeren (Archi voegt samen op id). Werkwijze: skill [gemma-archimate-model-archimate-export](.agents/skills/gemma-archimate-model-archimate-export/SKILL.md).

- **Id's en mappen.** Een element met een GEMMA-match krijgt het GEMMA-id en staat in dezelfde mappen als in GEMMA; een nieuw element krijgt een vast id, afgeleid van het begrip-id, in de map `wiki-gemma-model`. Een relatie krijgt het id van de GEMMA-relatie van hetzelfde type tussen dezelfde elementen, anders een vast id. Naam en definitie komen uit de wiki, ook over een GEMMA-element heen; de oude gaan mee als eigenschap. De export vertrouwt de match; daarom wordt een zwakke match voorgelegd.
- **Indelingen.** Elk element komt in zijn indelingen, met een aggregatie vanuit de groepering van GEMMA of een nieuwe groepering van de wiki, en een specialisatie naar een generiek GEMMA-element. De groeperingen houden hun id's.
- **Objectbehoud.** Een hernoemd, samengevoegd of gesplitst element zet het Archi-object voort dat `beoordelingen/objecten.yaml` noemt, zodat views in Archi blijven werken; de export weigert een typewijziging van een voortgezet object.
- **Volledige sync.** Elk object draagt een exportdatum. Na de import verwijdert een jArchi-script wat de wiki zelf maakte en ouder is; bij een GEMMA-object haalt het alleen de wiki-eigenschappen weg.
- **Kennismodel.** De groep *Kennismodel-wiki* bevat het volledige kennismodel van de wiki: een concept per elementtype, een relatie per toegestaan relatietype en de indelingen als groepering, met het id uit Over GEMMA waar dat bestaat, en de eigenschappen kernrelatie en *in Over GEMMA*. Het GEMMA-kennismodel uit Over GEMMA blijft een eigen groep, ter vergelijking.
- **Filter en rapport.** De relaties van de elementen worden gefilterd op het kennismodel. Het rapport noemt de weggelaten relaties, wat niet in Over GEMMA staat als kandidaat voor een terugmelding, de specialisaties en de nieuwe groeperingen.
- **Gate.** Alleen `goedgekeurd`, met een regel in `log.md`; `--concept` is alleen om te bekijken. De export weigert bij een fout of een verouderde beslissing of render. Na elk AKKOORD volgt een nieuwe export, die meegaat in de commit; importeren in GEMMA doet de redacteur.

## 7 Nog niet gebouwd

- De applicatielaag: nu alleen het data-object, als annotatie bij een bedrijfsobject.
- Views in de export naar Archi; de wiki maakt wel overzichten per indeling.
- Een dekkingsanalyse van het GGM per beleidsdomein.
