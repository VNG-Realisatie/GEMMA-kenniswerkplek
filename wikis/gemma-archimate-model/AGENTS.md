# gemma-archimate-model-wiki (curation)

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de Context staan: lees dat bestand voordat je iets wijzigt. Dit bestand zegt wat geldt; hoe de wiki werkt (mappen, beoordelingen, scripts, render) staat in `ARCHITECTURE.md`, waarom het model is zoals het is in `docs/`, en hoe je het doet in de skills. Waar je wat vindt: de kaart onderaan.

## Domein

- Het GEMMA-architectuurmodel, bedrijfslaag: bedrijfsobjecten, contracten, producten, diensten, processen, functies, gebeurtenissen, actoren, rollen, samenwerkingen en kanalen, plus beleidskaders (motivatielaag). Elk element wordt onderbouwd afgeleid uit bronnen en gematcht op het GGM en het GEMMA-model.
- Doelgroep: het GEMMA-team van VNG. Het resultaat voedt een landelijke standaard; kwaliteit en herleidbaarheid gaan voor snelheid.
- Taal: Nederlands; gevestigde ArchiMate-termen mogen Engels blijven.

## Standaard Workflow

Gebruik skill `gemma-archimate-model-update` voor elke inhoudelijke wijziging. De AI geeft het oordeel per begrip in een beoordeling (`beoordelingen/begrippen/<id>.yaml`); scripts leiden type en status af en maken alle pagina's (`tools/afleiden.py`, `tools/render.py`). Pagina's en overzichten worden nooit met de hand bewerkt. De redacteur beoordeelt de pagina's en geeft akkoord met het woord AKKOORD in de chat. Eerdere besluiten van de redacteur staan in `besluiten/per-begrip.md` (per begrip) en `besluiten/werkwijze.md` (over de werkwijze, met waar ze nu staan).

## Regels

Verwijs naar een regel met haar naam, bijvoorbeeld "regel Navragen". Achter een regel staat of een script haar controleert: *(schema)* en *(script)* houden een fout tegen, *(signaal)* geeft een waarschuwing die de AI inhoudelijk beoordeelt. Zonder markering is het een regel voor het oordeel van de AI.

Wat het render-script garandeert, is geen regel: bronverwijzingen als link naar de bronanalyse, relaties in beide richtingen, geen verwijzingen in de frontmatter, geen links naar tools of regels, de vorm van de pagina. De status zetten de scripts en het akkoord; de AI zet nooit een status.

Een regel is kort: de kern. Staat er meer bij een regel, dan noemt zij waar de uitwerking staat (hoe, in een skill) en de onderbouwing (waarom, in `docs/`).

### Werkwijze

- **Navragen** — Bij twijfel over een begrip, bron, naam of match: vraag het de redacteur, één vraag tegelijk, met context, argumenten en advies. Nooit gokken. Wat al in `besluiten/per-begrip.md` staat, vraag je niet opnieuw.
- **Eén naamgeving** — Noem brontypen, groepen en mappen precies zoals in de regel Bronvoorrang (`rijksregelgeving`, groep *Rijksregelgeving*; samen met `europese-regelgeving` heten ze landelijke regelgeving), in beoordelingen, analyses, terugmeldingen en de chat (besluit redacteur 2026-10-08).
- **Bestaand bijwerken** — Bestaat een beoordeling al, werk haar dan bij. Neem niet aan wat erin hoort.
- **Per geval** — Een besluit (hernoemen, samenvoegen, afwijzen, herformuleren) nooit in bulk doorvoeren op grond van één eerder akkoord; leg elk geval apart voor.
- **Letterlijk verplaatsen** — Bij verplaatsen of splitsen de bestaande tekst ongewijzigd overnemen, tenzij de redacteur iets anders vraagt.
- **Objectbehoud** — Hernoemen, samenvoegen of splitsen van een element leidt niet vanzelf tot een nieuw object in Archi: de redacteur gebruikt de objecten in views, en de export werkt views niet bij. Leg in `beoordelingen/objecten.yaml` vast welk bestaand object het element voortzet. Bij hernoemen altijd; bij samenvoegen vraag je de redacteur of en welk object blijft; bij splitsen of er een object blijft en welk deel het krijgt. *(script: het register klopt; de export weigert een typewijziging van een voortgezet object)*

### Oordeel

- **Beslistabel beslist** — Of een begrip een element is en van welk type, volgt alleen uit de kenmerken en de beslistabel (skill `gemma-archimate-model-criteria`). Registratie, eigendom, systeembeheer, regie of een extern systeem zijn geen argument. *(script; signaal bij registr*-taal)*
- **Match op betekenis** — Match met GGM en GEMMA op betekenis, niet op naam: herken homoniemen en synoniemen en volg relaties en generalisaties. Lees de modellen alleen via `tools/ggm.py` en `tools/gemma.py`, nooit direct en nooit via kopieën of CSV-exports. *(script: de gekozen match moet bestaan; signaal bij een afwijkende modelnaam)*
- **Zwakke match voorleggen** — Een GEMMA-match met sterkte `zwak` of `partieel` leg je altijd voor aan de redacteur, met wat er in GEMMA verandert: de export naar Archi (skill `gemma-archimate-model-archimate-export`) neemt het GEMMA-id over en overschrijft naam en definitie van dat GEMMA-element. Matchen is de verantwoordelijkheid van de wiki en de redacteur; de export en Archi vertrouwen de match. Past het GEMMA-element niet echt, kies dan `sterkte: geen` en noem het in de onderbouwing.
- **Eén element in het hele model** — Eén betekenis is één element in het hele model, ook als meer onderwerpen het gebruiken; een gelijke naam met een andere betekenis is een homoniem (regel Match op betekenis). Zoek vóór je een begrip beoordeelt in alle beoordelingen, van alle onderwerpen, op naam en synoniemen, en werk een bestaande beoordeling bij. Uitwerking: skill gemma-archimate-model-beoordelen, `references/onderwerpen.md`. *(signaal)*
- **Thuishoren** — Elk element heeft één thuisonderwerp, het eerste in `onderwerpen`. Een generiek element en een orgaan of de organisatie van de gemeente horen in Algemeen; anders beslist de inhoud: het onderwerp van de taak waarin het element ontstaat of verandert, niet het aantal relaties en niet de volgorde van inlezen. Uitwerking: skill gemma-archimate-model-beoordelen, `references/onderwerpen.md`. *(signaal)*
- **Relaties tussen onderwerpen** — Een relatie tussen elementen van verschillende onderwerpen is een gewone relatie, vastgelegd in de beoordeling van het bronelement; elk element heeft minstens één relatie met een ander element. Uitwerking: skill gemma-archimate-model-beoordelen, `references/onderwerpen.md`. *(signaal: element zonder relatie)*
- **Gemeentelijk perspectief** — Beschrijf wat de gemeente ziet, doet en beslist. Een externe partij wordt alleen een element bij een structurele relatie met de gemeente (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht); een partij die alleen als context in de bron staat, noem je in de beschrijving. Precedent: GGD wel.

### Bronnen

- **Elke claim een bron** — Elk kenmerk `ja`, elke relatie en elke bewering steunt op een bron; citaten letterlijk, met vindplaats. *(script: elk kenmerk `ja` en elk element heeft een bron; elke bron bestaat en heeft een bronanalyse)*
- **Zonder bron** — Een claim zonder bron wordt een open vraag ("verificatie nodig").
- **Tegenspraak** — Spreken bronnen elkaar tegen, leg dan beide vast en markeer de tegenspraak. Wat formeel geldt volgt de regel Bronvoorrang (landelijke regelgeving gaat voor, `overig` komt laatst); de afwijkende bron blijft vermeld als afwijking in de praktijk (besluit redacteur 2026-10-06).
- **Wettelijke grondslag** — Het model geldt voor alle gemeenten; daarom heeft elk element een landelijke wettelijke bron, dat is een bron van brontype `europese-regelgeving` of `rijksregelgeving` (regel Bronvoorrang), genoemd met het artikel. Uitzonderingen: een product of dienst uit de UPL blijft ook zonder (dan wordt het niet uitgewerkt), een bedrijfsfunctie volgt de grondslag van wat zij omvat, en een relatie heeft genoeg aan een bron. Uitwerking: skill gemma-archimate-model-beoordelen, `references/grondslag.md`; onderbouwing: `docs/wettelijke-grondslag.md`. *(script; signaal: een element zonder landelijke wettelijke bron)*
- **Bronvoorrang** — Voor welke begrippen er zijn en wat ze formeel betekenen, gaat een bron met een hoger brontype voor. Het brontype staat per bron in de intake (`sources/index/`); de volgorde staat in `wiki.yaml` `bronvoorrang` en is, van hoog naar laag:
  1. `europese-regelgeving`: regelgeving van de Europese Unie die voor alle gemeenten geldt, zoals verordeningen die rechtstreeks werken (AVG, AI-verordening).
  2. `rijksregelgeving`: regelgeving van het Rijk die voor alle gemeenten gelijk is: wetten, algemene maatregelen van bestuur en ministeriële regelingen, en door Nederland goedgekeurde verdragen.
  3. `informatiemodel`: GGM, RSGB, RGBZ, catalogi van basisregistraties, en architectuurmodellen zoals de UPL-lijsten.
  4. `richtlijn`: landelijke uitvoeringsvoorschriften, handleidingen, circulaires en handreikingen van het Rijk, uitvoeringsorganisaties en koepels (HUP van RvIG, NVVB, VNG, Divosa).
  5. `gemeentelijke-regelgeving`: verordeningen, nadere regels, beleidsregels en regelingen van gemeenschappelijke regelingen, die elke gemeente zelf vaststelt, en de VNG-modellen daarvan. Omdat de inhoud per gemeente verschilt, staat in het model het VNG-model als gemeenschappelijke vorm; de regeling van één gemeente is een voorbeeld en geen element.
  6. `beleid`: intern gericht beleid van een gemeente (beleidsnota's, visies, programma's).
  7. `overig`: praktijk, zoals productpagina's, websites en presentaties.

  Voorrang bepaalt nooit of iets een element is. De naam en de herkenbare definitie komen uit de gangbare taal van bronnen van `richtlijn`, `beleid` en `overig`; de wetsterm wordt een synoniem met context "wet". Precedent: Urn, niet Asbus. `europese-regelgeving` en `rijksregelgeving` heten samen landelijke regelgeving. Brontype `model` (het GEMMA-model) is een matchdoel en valt buiten de volgorde (besluiten redacteur 2026-10-08). *(signaal)*

### Tekst

- **Begrijpelijk** — Herkenbaar voor domeinexperts; geen jargon tenzij nodig. De definitie is één zin. *(signaal)*
- **Los van het onderwerp** — Definitie en beschrijving gelden in elk onderwerp; toets: past de tekst ongewijzigd in elk ander onderwerp? Wat een element in één onderwerp doet, staat onder `per_onderwerp`. *(signaal)*
- **Naamvorm** — Een proces is een infinitief met object in GEMMA-volgorde ("Behandelen aanvraag"), een functie een zelfstandig naamwoord voor het gebied van gedrag ("Vergunningverlening"), een gebeurtenis een voltooide verandering ("Overlijden"), een dienst geformuleerd vanuit de afnemer ("Melding openbare ruimte doen"). Het zelfstandig naamwoord uit de bron wordt een synoniem met context "beleid". Een product of dienst uit de UPL krijgt de UPL-naam letterlijk ("Verlof tot begraven"), met een synoniem waar dat betekenis toevoegt (besluit redacteur 2026-10-05). *(signaal)*
- **Geen absolute taal** — Geen "structureel buiten scope", "per definitie" of "het GGM modelleert nooit X" zonder concrete, domeinspecifieke reden; schrijf dan "in het GGM niet compleet gedekt". Een bewering met een concrete reden (ontbrekend beleidsdomein, wetsartikel, attribuutvergelijking) blijft staan. Beoordeel elk geval apart. *(signaal)*

### Terugmeldingen

- **Drie registers** — Een bevinding over het GGM, over de GEMMA-procesarchitectuur (UPL-lijsten, kennismodel) of over het GEMMA-model zelf gaat als terugmelding naar het register van die ontvanger: wat er nu staat, **Bevinding:** en **Voorstel:**, geschreven voor een lezer buiten de wiki. Uitwerking: skill gemma-archimate-model-beoordelen, `references/terugmeldingen.md`. *(script: een open melding zonder Bevinding of Voorstel)*
- **GEMMA-terugmeldingen formuleren** — Het wiki-model wordt in het GEMMA-model geïmporteerd: een wiki-element dat aan een GEMMA-element is gekoppeld, werkt dat element bij (naam, definitie, relaties, indeling). Formuleer een melding daarom als wat de import in GEMMA verandert en wat het GEMMA-team moet controleren of beslissen, niet als een verzoek om iets over te nemen. De import verwijdert niets: wat de wiki laat vervallen, blijft in GEMMA tot het GEMMA-team besluit.
- **Afwijken mits teruggemeld** — Het model mag afwijken van de UPL-indeling (taakveld, GEMMA-domein) en van het kennismodel procesarchitectuur, mits de afwijking is teruggemeld in de procesarchitectuur-terugmeldingen; de terugmelding dekt dan het signaal (besluit redacteur 2026-10-05). *(signaal)*

## Waar vind je wat

### Per soort

| Soort | Waar | Paginatype | Wie schrijft | Met de hand? |
|---|---|---|---|---|
| Regels: wat geldt | dit bestand | — | de AI, na een besluit van de redacteur | ja |
| Werkstroom: de stappen | skill `gemma-archimate-model-update` | — | — | ja |
| Criteria: is het een element, en welk type | skill `gemma-archimate-model-criteria`; [naslag/beslistabel.md](naslag/beslistabel.md) | lijst | de tabellen: `tools/bepaal_type.py` | alleen de tekst buiten de gegenereerde blokken |
| Werkinstructie per veld van een beoordeling | skill gemma-archimate-model-beoordelen en zijn `references/` | — | — | ja |
| Sjablonen | beoordeling: skill gemma-archimate-model-beoordelen §4; bronanalyse: skill gemma-archimate-model-ingest §4; terugmelding: `references/terugmeldingen.md`; besluit en voorleggen: `references/besluiten.md`; vorm: `schemas/` | — | — | ja |
| Oordeel per begrip | `beoordelingen/begrippen/<id>.yaml` | — | de AI; `status` en `afgeleid` de scripts | ja, behalve `status` en `afgeleid` |
| Registers | `beoordelingen/terugmeldingen/`, `objecten.yaml`, `beleidsdomeinen.yaml`, `besluiten-eerder.yaml`, `onderwerpen/` | — | de AI | ja |
| Wat een bron betekent | `bronanalyses/<onderwerp>/<brontype>/<bron-id>.md` | bronanalyse | de AI | ja |
| Waarom: onderbouwing | [docs/](docs/README.md) | doc | de AI | ja |
| Besluiten over de werkwijze (geschiedenis) | [besluiten/werkwijze.md](besluiten/werkwijze.md) en de besluitentabellen in `docs/` | doc | de AI | ja |
| Besluiten per begrip | [besluiten/per-begrip.md](besluiten/per-begrip.md) | lijst | `tools/render.py` | nee |
| Elementpagina's en overzichten | `bedrijfsarchitectuur/`, `motivatie/`, `begrippen/`, `overzichten/` | per elementtype | `tools/render.py` | nee |
| Terugmeldlijsten, ter beoordeling, voortgang | `terugmeldingen/`, [ter-beoordeling.md](ter-beoordeling.md), [voortgang.md](voortgang.md) | lijst | `tools/render.py` | nee |
| Open punten | [todo.md](todo.md) | — | de AI | ja |
| Akkoorden | [log.md](log.md) | — | `llmwiki promote apply` | nee |
| Controles | `tools/afleiden.py` (fout), `tools/signalen.py` (signaal) | — | — | — |

### Per regel

| Regel | Hoe (skill) | Waarom (docs, besluiten) | Controle |
|---|---|---|---|
| Navragen, Per geval | `references/besluiten.md` | `besluiten/werkwijze.md` | — |
| Eén naamgeving, Bronvoorrang | — | `docs/wettelijke-grondslag.md` | signaal |
| Bestaand bijwerken, Letterlijk verplaatsen | — | — | — |
| Objectbehoud | skill gemma-archimate-model-archimate-export | `besluiten/werkwijze.md`, thema 6 | script |
| Beslistabel beslist | skill gemma-archimate-model-criteria | `docs/kenmerken.md`, `docs/gemma-kennismodel.md`, `docs/proceshierarchie.md`, `docs/indelingen.md` | script, signaal |
| Match op betekenis, Zwakke match voorleggen | `references/ggm-match.md`, `references/gemma-match.md` | `docs/synoniemen-en-homoniemen.md` | script, signaal |
| Eén element in het hele model, Thuishoren, Relaties tussen onderwerpen | `references/onderwerpen.md`, `references/relaties.md` | `besluiten/werkwijze.md`, thema 3 | signaal |
| Gemeentelijk perspectief | `references/relaties.md` | `docs/gegevensrollen.md` | — |
| Elke claim een bron, Zonder bron, Tegenspraak | skill gemma-archimate-model-ingest | — | script |
| Wettelijke grondslag | `references/grondslag.md` | `docs/wettelijke-grondslag.md` | script, signaal |
| Begrijpelijk, Los van het onderwerp, Naamvorm, Geen absolute taal | `references/definitie.md`, `references/naamgeving.md` | — | signaal |
| Drie registers, GEMMA-terugmeldingen formuleren, Afwijken mits teruggemeld | `references/terugmeldingen.md` | `docs/wettelijke-grondslag.md` (besluit 4 en 15) | script, signaal |

De `references/` in deze tabel zijn die van skill gemma-archimate-model-beoordelen.
