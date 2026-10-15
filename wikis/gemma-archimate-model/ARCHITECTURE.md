# Architectuur van de wiki gemma-archimate-model

Dit document is leidend: het zegt waarom het model is zoals het is en hoe de wiki werkt. Wat het model is (elementtypen, relaties, indelingen) en de regels voor het modelleren staan in het [kennismodel](kennismodel/README.md), met de [modelleerregels](kennismodel/modelleerregels.md). De werkwijze van de AI staat in [AGENTS.md](AGENTS.md), de stappen en sjablonen in de skills. De wiki is van het type `curation`; de algemene opzet staat in de `ARCHITECTURE.md` van de repository.

## 1 Doel

Deze wiki bouwt een onderbouwd, herleidbaar GEMMA-architectuurmodel van de bedrijfslaag, voor het GEMMA-team van VNG: bedrijfsobjecten, afspraken, producten, diensten, processen, functies, gebeurtenissen, actoren, rollen, samenwerkingen, kanalen en bedrijfsinteracties, met de beleidskaders uit de motivatielaag. Het resultaat is de export naar Archi, die in het GEMMA-model wordt geïmporteerd. Het model voedt een landelijke standaard; kwaliteit en herleidbaarheid gaan daarom voor snelheid.

## 2 Plaats in de keten

```text
bronnen voor de inhoud                      matchdoelen
wetten, informatiemodellen (UPL, RSGB),     GEMMA-model · GEMMA Online · GGM · UPL
richtlijnen, gemeentelijke regelgeving      overgenomen indelingen (GEMMA, Iv3, GGM, UPL)
(ook VNG-modelverordeningen), beleid, praktijk
        │                                           │
        │   bronnen voor de methode                 │
        │   Over GEMMA · Proceshiërarchie ·         │
        │   Impact van ketensamenwerking            │
        ▼          │                                │
   deze wiki  ◄────┘◄────────────── matchen ────────┘
        │
        ├──►  export naar Archi (.archimate, met de id's van GEMMA)  ──►  tussenmodel  ──►  GEMMA-model
        └──►  terugmeldingen  ──►  GGM-beheer · werkgroep procesarchitectuur · GEMMA-team
```

Een bron heeft voor de wiki één van drie rollen; haar vorm (document of model) bepaalt alleen waar ze in `sources/` staat (ARCHITECTURE.md van de repository, *Bronnen: drie lagen*).

- **Bronnen voor de inhoud** zeggen welke begrippen er zijn en wat ze betekenen: landelijke regelgeving, informatiemodellen zoals de UPL, richtlijnen, gemeentelijke regelgeving, beleid en praktijk. Het model ontstaat uit deze bronnen. Hun voorrang staat in de regel Bronvoorrang.
- **Bronnen voor de methode** zeggen hoe je modelleert: Over GEMMA (de metadata van GEMMA: elementtypen, relaties en werkwijze) en de pagina's over de procesarchitectuur (Proceshiërarchie, Impact van ketensamenwerking). Ze onderbouwen het kennismodel en een keuze voor een type of niveau, nooit de inhoud. De export markeert per elementtype en relatietype of het *in Over GEMMA* staat: dat vergelijkt het kennismodel van de wiki met dat van GEMMA, en een verschil is kandidaat voor een terugmelding.
- **Matchdoelen** zijn bestaande modellen waartegen de wiki haar inhoud toetst en koppelt. Het GEMMA-model en GEMMA Online zijn allebei inhoud van GEMMA, gestructureerd en ongestructureerd, en ze vullen elkaar aan; verder het GGM en de overgenomen indelingen. Een matchdoel is geen bron: wie GEMMA met GEMMA onderbouwt, redeneert in een cirkel. Een VNG-modelverordening (Model-APV, Model beheersverordening) is geen matchdoel: zij is een voorbeeldverordening die de VNG voor alle gemeenten opstelt en die een gemeente overneemt en aanpast, gemeentelijke regelgeving in de gemeenschappelijke vorm. Zij is een bron voor wat gemeenten regelen, maar nooit grondslag, want zij heeft geen rechtskracht tot een gemeente haar vaststelt (regel Bronvoorrang). De UPL is bron én matchdoel: zij noemt het aanbod van gemeenten, en een UPL-item valt nooit weg. Later vergelijkt de wiki haar inhoud ook met een momentopname van GEMMA Online, om conflicten te vinden; een conflict wordt een GEMMA-terugmelding.
- **Terugmeldingen** gaan naar de beheerder van het matchdoel: een bevinding over het GGM naar GGM-beheer, over de UPL of het kennismodel procesarchitectuur naar de werkgroep procesarchitectuur, over het GEMMA-model zelf naar het GEMMA-team.

## 3 Uitgangspunten en voorrang

### 3.1 Herleidbaar model

Elk element, elk kenmerk en elke relatie is herleidbaar tot een bron, met de vindplaats, of, voor de plek in een overgenomen indeling, tot de relatie uit het model die het script toetst (§4.4), en elk inhoudelijk besluit van de redacteur over een begrip of onderwerp staat bij dat begrip of onderwerp. Een besluit dat breder geldt (in meer onderwerpen, of als patroon) wordt één keer bewaard: als regel in het kennismodel, met de onderbouwing in dit document. Herleidbaarheid geldt voor het model, niet voor de regels, de skills en de documentatie: die zijn consistent en overzichtelijk, en hun geschiedenis staat in Git. Een regel draagt dus geen datum en geen besluit mee, en een besluittekst noemt een regel of sectie bij naam, nooit een bestandspad; zo raakt een herstructurering van de wiki het model niet.

### 3.2 Zacht oordeel, harde vorm

| Wie | Wat | Waar |
|---|---|---|
| AI | het **oordeel** per begrip: kenmerken met onderbouwing en bron, naam, definitie, beschrijving, matches op betekenis, relaties, open vragen | `onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml` |
| redacteur | **besluiten** over wat is voorgelegd; vastgelegd door de AI | `besluiten:` in de beoordeling of het onderwerp |
| script | **beslissen**: type uit de beslistabel, status, letterlijke modelvelden, paginapad; harde controles en signalen | `status:` en `beslist:` in de beoordeling ([tools/beslissen.py](tools/beslissen.py)) |
| script | **renderen**: alle leesbare pagina's en overzichten | [tools/render.py](tools/render.py) |
| redacteur | **akkoord**, met het woord AKKOORD in de chat | `llmwiki promote`, `log.md` |

De AI oordeelt; het script beslist en rendert; de redacteur geeft akkoord. De AI schrijft dus geen pagina's, geen links en geen statussen. Wat een script garandeert of tegenhoudt, hoeft geen regel te zijn: de regels gaan over het oordeel.

### 3.3 Eén model

Een begrip komt één keer voor in het hele model, ook als meer onderwerpen het gebruiken; een gelijke naam met een andere betekenis is een homoniem. Andere onderwerpen gebruiken het element met een relatie en maken geen kopie. Waar een element thuishoort, volgt een voorrangsregel (regel Thuishoren): een bedrijfsobject hoort bij het eigen onderwerp waar het ontstaat en beheerd wordt, dan bij een thematisch gedeeld onderwerp, dan bij Kern; proces, dienst, product en gebeurtenis horen bij het onderwerp van hun kernobject; actor, rol, functie, beleidskader en kanaal hebben geen eigen thuis en gaan naar een gedeeld onderwerp of Kern zodra meer onderwerpen ze gebruiken. De inhoud beslist, niet het aantal relaties en niet de volgorde waarin onderwerpen zijn beoordeeld. Een begrip mag verhuizen; het object in Archi blijft.

De thuisonderwerpen samen zijn een indeling die uit de bronnen ontstaat (§4.4). Elk onderwerp heeft een niveau (`niveau`), met deze criteria:

| Niveau | Criterium | Onderwerpen | Voorbeelden |
|---|---|---|---|
| `eigen` | één samenhangende taak van de gemeente uit landelijke regelgeving, met eigen kernobjecten die de gemeente over hun hele levensloop beheert; het onderwerp heet naar die taak | Burgerzaken, Lijkbezorging, Participatie, … | Graf, Reisdocument, Stoffelijk overschot |
| `thematisch` | begrippen die meer eigen onderwerpen op dezelfde manier gebruiken, uit een eigen algemene regeling | Besluitvorming (Awb) · Bestuur en organisatie (Gemeentewet) · Heffingen en betalingen; groeit met het beoordelen | Besluit, Beschikking, Vergunning · Gemeente, College van B&W, Burgemeester · Heffing |
| `kern` | wat overal voorkomt en te breed is voor een thema | Kern | Persoon, Adres, Zaak, Document |

Een indeling uit een model, zoals de GEMMA-functiehiërarchie of een beleidsdomein, is geen onderwerp: zij staat ernaast als overgenomen indeling.

### 3.4 Voor alle gemeenten

Het GEMMA-model geldt voor alle gemeenten; elementen die van gemeente tot gemeente verschillen, horen er niet in. Daarom heeft elk element een landelijke wettelijke grondslag: een bron van brontype `europese-regelgeving` of `rijksregelgeving`, met het artikel (regel Wettelijke grondslag). Gemeentelijke regelgeving is geen grondslag, ook een VNG-modelverordening niet: een VNG-modelverordening werkt de wet uit in de vorm die gemeenten gemeenschappelijk hebben (§2); de verordening van één gemeente is een voorbeeld en een bron voor taal, niet voor het model, en een afwijking ervan is een afwijking in de praktijk. Richtlijnen, beleid en praktijk dienen voor taal, voorbeelden, werkwijze en het vinden van lacunes, niet als onderbouwing.

Eén uitzondering, de hoek *zonder grondslag*: een dienst uit de UPL blijft, ook zonder landelijke grondslag, want een UPL-item valt nooit weg. Zij is dan geen wettelijke taak. De wiki werkt haar uit voor zover mogelijk (een element met pagina, zonder processen, objecten, gebeurtenissen of rollen, want die zouden per gemeente verschillen), meldt haar terug aan de werkgroep procesarchitectuur en exporteert haar niet: wat geen wettelijke taak is, hoort niet in een model voor alle gemeenten (§6.3, §6.5). Een bedrijfsfunctie volgt de grondslag van wat zij omvat of bedient. Een relatie heeft geen eigen grondslag nodig: dat is te gedetailleerd, en een bron volstaat, zoals bij elke claim.

### 3.5 GEMMA volgen, of afwijken en terugmelden

De wiki volgt de namen, definities, indelingen en modelleerafspraken van GEMMA. Waar de wiki afwijkt (een eigen indeling, een relatie die niet in Over GEMMA staat, een UPL-dienst onder een ander taakveld), meldt zij dat terug, met wat er nu staat, de bevinding en een voorstel. Het wiki-model wordt in GEMMA geïmporteerd en werkt gekoppelde GEMMA-elementen bij; een terugmelding zegt daarom wat de import verandert en wat het GEMMA-team moet controleren of beslissen. De import verwijdert niets: wat de wiki laat vervallen, blijft in GEMMA tot het GEMMA-team besluit.

### 3.6 Consistentie boven behoud

Een betere modellering gaat voor het vermijden van herbeoordeling. Wordt het resultaat beter van een andere regel, naam of indeling, dan worden de geraakte beoordelingen opnieuw beoordeeld en voorgelegd, per geval. Waar het kan, is een wijziging mechanisch: een relatietype toevoegen aan of weghalen uit het kennismodel is opnieuw filteren, geen herbeoordeling (§4.2).

### 3.7 Voorrang

Bij het modelleren geldt een vaste voorrang; de regels staan in de [modelleerregels](kennismodel/modelleerregels.md).

- **Bronnen:** europese-regelgeving › rijksregelgeving › informatiemodel › richtlijn › gemeentelijke-regelgeving › beleid › overig. Voorrang bepaalt wat formeel geldt en welke begrippen er zijn, nooit óf iets een element is. De naam komt uit de gangbare taal; de wetsterm wordt een synoniem.
- **Een element modelleren:** welk begrip (synoniem of homoniem) › grondslag › kenmerken en type › kernrelaties › indeling › overige relaties › matches.
- **Matchen:** op betekenis, niet op naam; een zwakke of partiële GEMMA-match wordt voorgelegd, omdat de export dan een GEMMA-element overschrijft.
- **Relaties:** grondslag › kernrelatie › indelingsrelaties › overige relaties uit de bronduiding › GGM-match van de relatie › GEMMA.
- **Thuishoren:** eigen onderwerp › thematisch gedeeld › Kern (§3.3); een overgenomen indeling staat ernaast.

## 4 Het kennismodel

Het [kennismodel](kennismodel/README.md) beschrijft wat het model is: per architectuurlaag de elementtypen, per type de modelleerafspraken, de relatietypen met de vaste namen, de [indelingen](kennismodel/indelingen.md), en per laag de elementtypen die niet tot een element leiden. Het wordt gegenereerd uit één bron, [tools/kennismodel.py](tools/kennismodel.py); alleen de modelleerregels zijn met de hand geschreven. De scripts lezen het kennismodel in plaats van eigen tabellen te houden, zodat de documentatie, de beslistabel, de controles en de export niet uit de pas kunnen lopen. Wat er geldt, staat in het kennismodel; dit hoofdstuk zegt alleen waarom.

### 4.1 Elementtypen en kenmerken

- **Kenmerken eerst, type als uitkomst.** De AI beantwoordt neutrale vragen over het begrip, elk met onderbouwing en bron, en de beslistabel leidt daaruit het type af. Zo is het type toetsbaar en herhaalbaar, en geen keuze vooraf op gevoel. Wat de gemeente vastlegt, zegt niets over wat een begrip is (regel Beslistabel beslist).
- **Twee fasen.** Fase A (poort, aard en de groep van die aard) bepaalt het pad door de beslistabel; fase B vraagt alleen de kenmerken van dat type, en buiten het pad leidt het script nee af. Zo schrijft de AI alleen wat de uitkomst bepaalt, de redacteur ziet de keuze met de meeste gevolgen vroeg, en de nee op het pad blijft als dubbelcheck.
- **Per type een kernrelatie en een drempel.** Eén kenmerk bepaalt het type, één kernrelatie moet ja zijn, en van de overige kenmerken mag hoogstens één nee zijn. Zo krijgen alle typen een vergelijkbare toets, en tellen overlappende kenmerken niet dubbel.
- **Namen uit het GEMMA-kennismodel.** De typen heten zoals in Over GEMMA, met de GEMMA-definities waar die passen. De bedrijfsinteractie is een uitbreiding: GEMMA kent haar als element (*Ketensamenwerking*), niet in het kennismodel.
- **Een UPL-item is een dienst.** De UPL noemt per naam één aanbod van de overheid aan een afnemer. Een product is een gebundeld aanbod van diensten met afspraken (Over GEMMA) en komt dus nooit uit één UPL-item; de UPL zelf maakt geen onderscheid tussen product en dienst.
- **Een regeling.** Een concreet benoemde regeling als geheel wordt een beleidskader, de soort regeling het bedrijfsobject Regeling, en een los artikel valt buiten het model. Een landelijke richtlijn wordt nooit een beleidskader: zij geeft de gemeente geen taak, bevoegdheid of plicht, maar beschrijft hoe zij die uitvoert (§3.4).
- **Wat geen element wordt.** Het kennismodel noemt per laag de typen die niet tot een element leiden, met de reden. Een groepering is geen begrip uit een bron maar de knoop van een indeling, zonder pagina en zonder beoordeling. Zij staat toch in het kennismodel, omdat de indelingen zonder groeperingen geen relaties in GEMMA hebben.

### 4.2 Relaties

- **Gevonden tegenover gefilterd.** Een beoordeling legt elke relatie vast die de bron noemt en die geldig is in ArchiMate; de export neemt alleen de relaties mee die in het kennismodel staan. Zo gaat niets verloren wat de bron zegt, en is het kennismodel aanpassen opnieuw filteren in plaats van herbeoordelen. Een relatie die in het kennismodel van de wiki staat maar niet in Over GEMMA, is een uitbreiding: zij gaat gemarkeerd mee en is kandidaat voor een terugmelding.
- **Een actor via een rol**, zoals in GEMMA. Een rol mag ook aan een bedrijfsproces worden toegewezen, niet alleen aan een functie, omdat GEMMA dat zelf doet op het niveau van het deelproces.
- **Toegang met vaste namen.** Wat een rol met een object ís (een verantwoordelijkheid) en wat gedrag met een object dóét (een handeling), komt uit de wetten van de basisregistraties, de AVG en de Archiefwet, en het ArchiMate-toegangstype volgt eruit. *Houder* in plaats van eigenaar, omdat de wetten van houden spreken en eigendom van gegevens geen juridisch begrip is; *afnemer* in plaats van raadpleger, omdat het de wettelijke term is en de plicht tot gebruik en terugmelden meedraagt. De twee reeksen toetsen elkaar: een bronhouder hoort toegewezen te zijn aan gedrag dat registreert of bijwerkt.
- **Grondslag als relatie.** Een beleidskader *is grondslag voor* wat het regelt, bij voorkeur een dienst of product. Een VNG-modelverordening *werkt uit voor* en is nooit grondslag: zij heeft geen eigen rechtskracht tot een gemeente haar vaststelt.
- **Kwaliteitsdoelen.** Een beleidskader *geeft grondslag aan* een kwaliteitsdoel van GEMMA, zoals Over GEMMA het voorschrijft: de regeling is de bindende basis voor het doel en bepaalt welke eisen en normen het moet vervullen. Het kwaliteitsdoel is een matchdoel; de wiki maakt er geen nieuw.
- **GGM-match van een relatie** alleen bij bedrijfsobjecten, data-objecten en beleidsdomeinen. Een relatie die het script uit een keten in het GGM afleidt, is een voorstel en geen match.

### 4.3 Processen en ketens

- **De GEMMA-ladder.** De procesniveaus volgen de proceshiërarchie van GEMMA. Een specialisatie van een generiek GEMMA-proces is geen niveau.
- **Eén levensloopproces per kernobject** (*Beheren grafrechten*: van uitgifte tot verval). Zonder die groepering wordt elk van de honderden UPL-producten een los proces en wordt het model plat; met haar groeit het model met het aantal kernobjecten, niet met het aantal producten.
- **Klant tot klant.** Een bedrijfsproces loopt van een aanleiding van buiten tot het resultaat voor de klant, onder verantwoordelijkheid van één organisatie. Wat voor hetzelfde geval op een ander proces volgt en pas samen daarmee de dienst levert, is een deelproces. Of een stap belangrijk is (eigen besluit, eigen normering), zegt niets over waar het proces begint en eindigt.
- **Deelproces zonder pagina.** Het bedrijfsproces beschrijft zijn deelprocessen in volgorde. Zo blijft het model op het abstractieniveau van GEMMA, en heeft de procesontwerper toch het overzicht.
- **Een gebeurtenis start een bedrijfsproces**, nooit een deelproces. Een tussentoestand binnen één proces is geen element.
- **Geen ketenproces.** Waar de processen van meer partijen samenkomen, is dat bij een estafette een bedrijfsinteractie (ketensamenwerking), bediend door de bedrijfsprocessen van de partijen; het ketenproces erboven blijft impliciet. Bij orkestratie specialiseert het deel van de gemeente *Leveren dienst aan derden*.

### 4.4 Indelingen

Welke indelingen er zijn, met hun niveaus en hun plaats in Archi, staat in [indelingen](kennismodel/indelingen.md). Waarom ze zo zijn:

- **Drie soorten.** Een indeling die ontstaat uit de bronnen (de thuisonderwerpen van §3.3, de Procesindeling naar kernobject, de Grondslagindeling) ordent de inhoud zoals de bronnen haar aanreiken. Een indeling overgenomen uit een model (GEMMA, Iv3, GGM, UPL, later NORA) geeft herkenbaarheid en koppelt aan wat al bestaat. De ArchiMate-indeling (laag › elementtype) ordent de wiki zelf. Indelingen zijn niet leidend: wat uit de bronnen komt, kan een indeling later doen veranderen.
- **Overnemen is letterlijk.** Een overgenomen indeling komt as-is uit het model, ook de tussenliggende knopen, zonder beoordeling en zonder bron. Een bladfunctie van GEMMA wordt pas een element als een onderwerp haar betekenis geeft; een functie zonder GEMMA-match breidt de functieketen van GEMMA uit, onder een bestaande GEMMA-functie.
- **De plek bij het kind.** Een functie of dienst noemt haar plek onder een GEMMA-functie zonder beoordeling (`gemma_functie`). Zo staat de plek één keer, bij het element, en heeft de knoop geen beoordeling nodig; het script toetst haar aan het model.
- **Plek tegenover inhoud.** Een bewering over de plek van een element in een overgenomen indeling gaat over het matchdoel zelf en steunt op de relatie uit het model (`gemma_relatie`). Wat het element is, steunt op een bron voor de inhoud; een pagina van GEMMA Online is daarvoor geen bron (§2).
- **Doelgroep als groepering.** GEMMA modelleert een doelgroep als rol. Een doelgroep is een ordening en geen hoedanigheid; in de wiki is zij daarom een groepering. De afwijking is teruggemeld.
- **Alles ingedeeld, met dekking.** Elk element staat in minstens één indeling, ook in Archi. De indelingspagina's tonen de hele indeling met de wiki-elementen eronder, zodat te zien is welke gaten de bronnen nog niet hebben gevonden.
- **Specialisatie of aggregatie.** Specialisatie koppelt aan een indeling van GEMMA (wat voor soort is het?), aggregatie aan een eigen indeling (waar hoort het bij?). Hergebruik gaat boven een nieuwe indeling, en de indelingen zijn strikt hiërarchisch waar het kan.
- Afwijken van de UPL-indeling of het GEMMA-domein mag, mits teruggemeld (regel Afwijken mits teruggemeld).

### 4.5 Synoniemen en homoniemen

Synoniemen en homoniemen zijn geen kenmerken van een begrip, maar verhoudingen tussen een woord en een begrip. Daarom komen ze vóór de kenmerken, in stap 0 van de beslistabel: eerst vaststellen welk begrip bedoeld is. Een homoniem is breed (dezelfde naam voor een ander begrip, in elke bron en voor elk type), omdat elke elementnaam op zichzelf ondubbelzinnig moet zijn. Een tegenhanger (een actor of rol en een bedrijfsobject met dezelfde naam) en een GGM-duplicaat zijn geen homoniem.

## 5 Werkstroom en status

Skill [gemma-archimate-model-update](.agents/skills/gemma-archimate-model-update/SKILL.md) volgt de gedeelde `wiki-curatie-update`. Er is geen run: de werkboom is de toestand, en Git laat elke wijziging zien.

```text
 STAP                           WIE        RESULTAAT                                                      STATUS
 1 Onderwerp                    AI+redact. onderwerpen/<onderwerp>/afbakening.yaml                        —
 2 Bronnen en bronduiding       AI         sources/, onderwerpen/<onderwerp>/bronduidingen/                —
 3 Beoordelen                   AI         onderwerpen/<thuisonderwerp>/beoordelingen/<id>.yaml            —
 4 Beslissen en renderen        script     status, beslist, alle pagina's                                 review
 5 Voorleggen (één tabel)       AI→redact. besluiten: in de beoordeling → terug naar 4                    review of afgewezen
 6 Bekijken                     redacteur  llmwiki promote plan; ter-beoordeling.md, pagina's, Source Control
 7 AKKOORD in de chat           redacteur
 8 Vastleggen                   script     llmwiki promote apply; log.md                                  review → goedgekeurd
 9 Exporteren                   script     tools/archimate_export.py; export/                             —
10 Commit                       redact./AI pre-commit-controles
```

| Status | Wie | Wanneer |
|---|---|---|
| `review` | `tools/beslissen.py` | wacht op akkoord; zegt de beslistabel voorleggen (zoals bij een nieuwe bedrijfsinteractie of een kanaal, of een geautomatiseerd verwerkt object zonder sterke GGM-match), dan staat de reden in `beslist.open` en op de pagina tot het akkoord |
| `goedgekeurd` | `llmwiki promote apply`, na AKKOORD | met een regel in `log.md` met de hash van de inhoud van de beoordeling |
| `afgewezen` | `tools/beslissen.py`, na het besluit afwijzen | geen pagina; blijft in de begrippenlijst |

**Wanneer opnieuw akkoord.** De hash dekt de hele beoordeling behalve de scriptvelden `status` en `beslist` en de `besluiten`: het akkoord keurt het model goed, niet het verslag van de besluiten. Een inhoudelijke wijziging maakt een goedgekeurde beoordeling weer `review`; een andere opmaak, een nieuw script, een nieuwe modelrelease, een ander filter in het kennismodel of een gewijzigd besluit niet. De pre-commit-controle `goedgekeurd-guard` weigert `goedgekeurd` zonder overeenkomende regel in `log.md`, en `log-alleen-aanvullen` weigert een gewijzigde of verwijderde regel.

**Besluiten.** Een besluit legt inhoud vast: een keuze, een afwijking, een afbakening of een afwijzing, niet het ja op opnemen (dat is het akkoord). Een besluit over een begrip staat in de `besluiten:` van zijn beoordeling, een besluit over een onderwerp als geheel in de `besluiten:` van het onderwerp; de begrippenlijst van een onderwerp toont ze. Er is geen apart register, en een herzien besluit verdwijnt (Git bewaart het). Wat al besloten is, vraagt de AI niet opnieuw (regel Navragen). Een besluit over de werkwijze wordt verwerkt in de regel of de skill waar het hoort.

## 6 Hoe de wiki werkt

### 6.1 Plattegrond

```text
wikis/gemma-archimate-model/
├── ARCHITECTURE.md                   dit document: waarom en hoe (leidend)
├── AGENTS.md                         de werkwijze van de AI, met de kaart "Waar vind je wat"
├── wiki.yaml · todo.md · todo-later.md · log.md      instellingen · open punten (actief, later) · akkoorden (alleen aan te vullen)
├── kennismodel/                      wat het model is (gegenereerd), met modelleerregels.md (met de hand)
├── plannen/<datum>-<titel>.md        plannen voor grotere wijzigingen; een plan dat klaar is, blijft als geschiedenis
├── onderwerpen/<onderwerp>/          de ontstane indeling: per onderwerp alles bij elkaar
│   ├── afbakening.yaml               naam, niveau, status, omschrijving, bronnen en besluiten van het onderwerp (AI)
│   ├── beoordelingen/<id>.yaml       het oordeel per begrip met dit thuisonderwerp (AI); status en beslist zet het script
│   ├── bronduidingen/<brontype>/<bron-id>.md   wat een bron betekent voor de architectuur (AI)
│   ├── begrippen.md                  de begrippenlijst (gegenereerd door tools/render.py)
│   └── overzicht.md                  de views op de indelingen (gegenereerd door tools/render.py)
├── modellen/<model>/                 per model: bronduidingen, overgenomen indelingen en terugmeldingen
│   ├── gemma/                        bronduidingen/ (GEMMA-model; Over GEMMA, Proceshiërarchie, Impact) · indelingen/beleidsdomeinen.yaml · terugmeldingen/{gemma-team,procesarchitectuur}.yaml (AI) en .md (gegenereerd)
│   ├── ggm/                          bronduidingen/ (GGM, GGM-website) · terugmeldingen.yaml (AI) en terugmeldingen.md (gegenereerd)
│   └── upl/                          bronduidingen/ (UPL van Logius, de aangevulde lijsten extern en intern van GEMMA)
├── elementpaginas/                   gegenereerd door tools/render.py, volgens de ArchiMate-indeling (bedrijfsarchitectuur/, motivatie/); overig/indelingen/ (de indelingspagina's) en overig/zonder-grondslag.md
├── ter-beoordeling.md · voortgang.md gegenereerd door tools/render.py
├── export/                           het Archi-bestand en het exportrapport
├── schemas/                          beoordeling (gegenereerd), bronduiding, kennismodel, lijst
├── tools/                            het gereedschap van deze wiki, met tests in tools/tests/
└── .agents/skills/                   hoe je het doet
```

### 6.2 Beoordelingen en registers

Een beoordeling is het oordeel van de AI over één begrip: kenmerken, naam, definitie, beschrijving, tekst per onderwerp, synoniemen en homoniemen, de matches met GGM en GEMMA, de plek in de functiehiërarchie (`gemma_functie`), relaties, indelingsvelden, open vragen en besluiten. Het schema wordt gegenereerd uit de beslistabel ([tools/bepaal_type.py](tools/bepaal_type.py)). Een relatie staat één keer, in de beoordeling van het bronelement; de render zet de inkomende kant op de pagina van het doel. De beoordeling staat in de map van haar thuisonderwerp (het eerste in `onderwerpen`; `tools/beslissen.py` controleert dat); een begrip dat verhuist, verhuist dus mee, en het pad van zijn elementpagina verandert niet, want elementpagina's volgen de ArchiMate-indeling. Naast de beoordelingen houdt de AI registers bij: de afbakening van elk onderwerp, de terugmeldingen per ontvanger (bij het model van de ontvanger) (met wat er nu staat, **Bevinding:** en **Voorstel:**), en de beschrijving van de beleidsdomeinen.

### 6.3 Beslissen, renderen en controles

[tools/beslissen.py](tools/beslissen.py) leest de beoordelingen, past de beslistabel toe, zet de status, haalt de letterlijke velden van de gekozen GGM- en GEMMA-match (ook die van de bovenliggende functie, `gemma_functie`) op, bepaalt het paginapad, herkent de diensten zonder grondslag (`beslist.zonder_grondslag`: de UPL als bron, geen bron van landelijke regelgeving en geen *is grondslag voor* van een beleidskader van de EU of het Rijk) en roept daarna de render aan. Het houdt een fout tegen (er wordt dan niets geschreven): het schema, onvolledige kenmerken, een claim zonder bron, een bron zonder bronduiding, een match die niet bestaat, een relatie die in ArchiMate niet geldig is of naar iets dat geen element is, een fout in de indeling of de hiërarchie, een ongeldige terugmelding, een besluit van een onderwerp over een begrip dat een beoordeling heeft, een besluittekst met een bestandspad, een handmatig gewijzigd modelbestand. [tools/signalen.py](tools/signalen.py) geeft signalen, met de naam van de regel: absolute taal, registratietaal, de naamvorm, een afwijkende modelnaam zonder synoniem, een kenmerk dat een kernrelatie is zonder die relatie, een relatie buiten het kennismodel, een element zonder relatie of zonder landelijke grondslag, een dienst zonder grondslag zonder procesarchitectuur-terugmelding. Een dienst zonder grondslag krijgt geen signaal voor een ontbrekende kernrelatie, realisatie of relatie: zij wordt niet uitgewerkt. Een signaal beoordeelt de AI inhoudelijk: oplossen of toelichten.

[tools/render.py](tools/render.py) maakt alle leesbare bestanden: de elementpagina's (de map volgt uit het type, de submappen uit de indelingsvelden), de begrippenlijst per onderwerp met de besluiten over het onderwerp, de overzichten per indeling, de indelingspagina's met dekking (via [tools/indelingspaginas.py](tools/indelingspaginas.py)), de terugmeldlijsten, de lijst van diensten zonder grondslag met hun terugmelding (`elementpaginas/overig/zonder-grondslag.md`; zo'n dienst krijgt ook een melding op haar pagina), `ter-beoordeling.md`, `voortgang.md` en het kennismodel. Het oordeelt niet en schrijft nooit in een beoordeling; twee keer renderen geeft hetzelfde resultaat. Het garandeert de vorm: elke bronverwijzing is een link naar de bronduiding, relaties staan in beide richtingen, verwijzingen staan als link in de tekst en niet in de frontmatter, er staan geen links naar tools of regels, en een relatie buiten het kennismodel staat erbij met de melding dat zij niet meegaat in de export. `render.py --check` in de pre-commit bewaakt dat de pagina's gelijk zijn aan de beoordelingen en het kennismodel aan zijn bron.

### 6.4 GGM en GEMMA als matchdoel lezen

| | GGM | GEMMA-model |
|---|---|---|
| Bronbestand | XMI (Enterprise Architect) in `sources/modellen/`, brontype `model` | Archi-bestand `.archimate` (met map-id's en profielen, nodig voor de export) in `sources/modellen/`, brontype `model` |
| Omzetting | JSON naast het bestand, door llmwiki (`sources/modellen/<bron-id>.json`) | idem |
| Tool | [tools/ggm.py](tools/ggm.py) | [tools/gemma.py](tools/gemma.py) |
| Zoeken (AI) | `kandidaten`, `entiteit`, `naamgenoten`, `generalisaties`, `attribuut`, `relaties` | `kandidaten`, `element`, `koppel`, `zoek`, `groepering`, `functie`, `functies` |
| Letterlijke velden (script) | `velden` → `beslist.ggm` | `velden` → `beslist.gemma` |
| Nieuwe versie | skill gemma-archimate-model-ggm-release | skill gemma-archimate-model-gemma-release |

De AI kiest de match op betekenis; het script haalt bij elke run de letterlijke velden op, zodat een nieuwe release vanzelf meegaat. De tools lezen de JSON-omzetting in `sources/modellen/` van de bron die `wiki.yaml` (`ggm.bron`, `gemma.bron`) noemt; het model zelf lees je alleen via deze tools, nooit direct of via een kopie in de wiki. Het GGM is matchdoel voor bedrijfsobjecten, data-objecten en beleidsdomeinen: per beleidsdomein wordt de dekking getoetst, en een hiaat wordt een GGM-terugmelding; een GGM-entiteit is zelf geen begrip en wordt pas via een bron beoordeeld. Het GEMMA-model is matchdoel voor alle typen: zijn id gaat mee in de export. Wat een model voor de wiki betekent (zijn rol, de delen en eigenschappen die de wiki gebruikt), staat in zijn bronduiding in `modellen/<model>/bronduidingen/`; die verhuist bij een nieuwe release mee naar het nieuwe bron-id.

### 6.5 Export naar Archi

[tools/archimate_export.py](tools/archimate_export.py) schrijft de goedgekeurde elementen en relaties als `export/gemma-archimate-model.archimate`, om in Archi te bekijken en in het GEMMA-model te importeren (Archi voegt samen op id). Werkwijze: skill [gemma-archimate-model-archimate-export](.agents/skills/gemma-archimate-model-archimate-export/SKILL.md).

- **Id's en mappen.** Een element met een GEMMA-match krijgt het GEMMA-id en staat in dezelfde mappen als in GEMMA; een nieuw element krijgt een vast id, afgeleid van het begrip-id, in de map `wiki-gemma-model`. Een relatie krijgt het id van de GEMMA-relatie van hetzelfde type tussen dezelfde elementen, anders een vast id. Tussen twee elementen staat één toegangsrelatie: de beoordeling legt elke handeling uit de bron vast, de render en de export voegen ze met dezelfde functie samen (`kennismodel.toegang_per_paar`), met de vereniging van de toegangstypen, zodat de pagina en het model in Archi gelijk zijn, er geen dubbele relaties zijn en elke handeling herleidbaar blijft (op de pagina in de relatie, in Archi in de eigenschap `toegang`). Het toegangstype volgt uit de handeling, niet uit wie het object beheert: ook een ander proces dan dat van het kernobject maakt of wijzigt het object, en een regel naar eigenaarschap zou objecten splitsen. Naam en definitie komen uit de wiki, ook over een GEMMA-element heen; de oude gaan mee als eigenschap. De export vertrouwt de match; daarom wordt een zwakke match voorgelegd.
- **Indelingen.** Elk element komt in zijn indelingen, met een aggregatie vanuit de groepering van GEMMA of een nieuwe groepering van de wiki, en een specialisatie naar een generiek GEMMA-element. De groeperingen houden hun id's. Van een overgenomen indeling gaat elke gebruikte tak mee tot en met de wortel (bij de functiehiërarchie tot en met het domein), letterlijk, met de id's van de knopen en relaties uit het model; een knoop wordt niet overschreven als wiki-element. `gemma_functie` wordt de aggregatie vanaf de bovenliggende GEMMA-functie. Zo kan de redacteur het resultaat in een tussenmodel controleren en er views maken voordat het in GEMMA gaat. Met `--volledig` gaat de hele indeling mee, om de gaten te zien. De onderwerpen gaan pas mee na de consolidatie van de indelingen: GEMMA kent er geen tegenhanger van.
- **Objectbehoud.** Een hernoemd, samengevoegd of gesplitst element zet het Archi-object voort dat het veld `object_van` van zijn beoordeling noemt (een feit over het element, dus bij het begrip en niet in een register), zodat views in Archi blijven werken; de export weigert een typewijziging van een voortgezet object.
- **Volledige sync.** Elk object draagt een exportdatum. Na de import verwijdert een jArchi-script wat de wiki zelf maakte en ouder is; bij een GEMMA-object haalt het alleen de wiki-eigenschappen weg.
- **Kennismodel.** De groep *Kennismodel-wiki* bevat het volledige kennismodel van de wiki: een concept per elementtype, een relatie per toegestaan relatietype (bij toegang één per paar elementtypen: het toegangstype hoort bij de relatie in het inhoudelijk model) en de indelingen als groepering, met het id uit Over GEMMA waar dat bestaat, en de eigenschappen kernrelatie en *in Over GEMMA*. Het GEMMA-kennismodel uit Over GEMMA blijft een eigen groep, ter vergelijking.
- **Zonder grondslag.** Een UPL-dienst zonder landelijke grondslag gaat niet mee (`beslist.zonder_grondslag`): zij is geen wettelijke taak (§3.4).
- **Filter en rapport.** De relaties van de elementen worden gefilterd op het kennismodel. Het rapport noemt de weggelaten relaties, de samengevoegde toegangsrelaties, wat niet in Over GEMMA staat als kandidaat voor een terugmelding, de specialisaties, de nieuwe groeperingen, de dekking van de functiehiërarchie en de diensten zonder grondslag.
- **Gate.** Alleen `goedgekeurd`, met een regel in `log.md`; `--concept` is alleen om te bekijken. De export weigert bij een fout of een verouderde beslissing of render. De export draait alleen op verzoek van de redacteur (per afronding volstaat `--check`) en gaat dan mee in de commit; importeren in GEMMA doet de redacteur.

## 7 Nog niet gebouwd

- De applicatielaag: nu alleen het data-object, als annotatie bij een bedrijfsobject.
- De overgenomen indelingen as-is (§4.4): de functiehiërarchie uit het model, de plek van een wiki-element erin (`gemma_functie`), de pagina per indeling met dekking, en de export tot en met de wortel met `--volledig`. Nu hebben de functies boven het niveau van een onderwerp nog een beoordeling.
- De vergelijking met een momentopname van GEMMA Online (§2).
- Views in de export naar Archi; de wiki maakt wel overzichten per indeling.
- Een dekkingsanalyse van het GGM per beleidsdomein.
