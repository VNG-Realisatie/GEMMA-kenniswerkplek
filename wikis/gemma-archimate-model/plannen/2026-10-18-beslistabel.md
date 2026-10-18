# Plan: de beslistabel herzien

Basis: main op 5800edb7. De besluiten van de redacteur per wijziging staan in hoofdstuk 7.

## 1 Doel

Bij het vastleggen van de potentiële relaties in lijkbezorging bleken 61 van de 109 open kenmerken te horen bij begrippen die geen pagina krijgen: ze beantwoorden alle kenmerken van hun type en vallen pas daarna af. Beoordelen is nog te zwaar. Het doel van dit plan:

- zo weinig mogelijk stappen, in een volgorde zonder overbodig werk;
- zoveel mogelijk zekerheid, met weinig twijfelgevallen om voor te leggen;
- een beslistabel die beter te begrijpen is: een logische opbouw, benoemde fasen en duidelijke termen;
- met behoud van een goed model en van de herleidbaarheid.

## 2 De beslistabel straks, in één oogopslag

Vier fasen, zeven stappen. Elke fase beantwoordt één vraag. Wat geen eigen element wordt, valt af in de eerste fase, vóór er werk aan de kenmerken van het type wordt gedaan.

| Fase | Vraag van de fase | Stap | Wat er gevraagd wordt | Uitkomst |
|---|---|---|---|---|
| **Afbakenen** | Wordt dit begrip een eigen element? | 0 Welk begrip | Bestaat het al? Is het een synoniem of homoniem? | bestaand: alleen het onderwerp erbij; synoniem: stop |
| | | 1 Scope | Alleen een afwijking: niet herkenbaar, niet gemeentelijk, buiten dit model, hoort bij een ander onderwerp | stop |
| | | 2 Afhankelijk | Keuzekenmerk *afhankelijkheid*: zelfstandig, of eigenschap, onderdeel, deelproces, variant of invoer van een ander, met het begrip waarvan het afhangt | geen pagina: stop |
| **Typeren** | Welk type en niveau, en is er een grondslag? | 3 Type en niveau | Keuzekenmerken: vak, hoofdkenmerk, soort gedrag, procesniveau met kernobject, interactievorm; bij een partij ook eigen rechtspersoon en soort partij | voorlopig element met type en niveau |
| | | 4 Grondslag | Het script kijkt of er een landelijke bron is | geen grondslag: stop, behalve een UPL-dienst |
| — | | — | De tabel voor de redacteur | besluiten |
| **Onderbouwen** | Voldoet het element aan zijn type? | 5 Toetskenmerken | De toetskenmerken van het type: de relatiekenmerken met hun tegenpartij, de andere standaard ja | element; een nee wordt voorgelegd |
| **Indelen** | Waar hoort het in de indelingen? | 6 Indeling | Script: objectniveau, toets van het procesniveau, generiek | indeling |

De werkstroom heeft drie Sessies: Sessie 1 doet Afbakenen en Typeren en eindigt met de tabel voor de redacteur, Sessie 2 doet Onderbouwen, en Sessie 3 doet Indelen (script), voorleggen en akkoord.

**Kort in de beoordeling, volledig op de pagina.** In de beoordeling (yaml) staat alleen wat de AI kiest of afwijkt: de keuzekenmerken, de relatiekenmerken met tegenpartij en de afwijkingen. Het script zet op de elementpagina alle kenmerken die tot het element leiden, ook de standaard ja, met hun bron. Het script is goedkoop; de pagina blijft volledig en leesbaar voor de redacteur.

### Alleen echte twijfel voorleggen

Een twijfelgeval is een keuze tussen verdedigbare alternatieven die niet volgt uit de beslistabel, een regel, een bron of een eerder besluit. Alleen dat wordt voorgelegd. Wat eenduidig volgt (een stop in Afbakenen zonder twijfel, een thuisonderwerp of grondslag die eenduidig uit de inhoud volgt, een toets die het script doet), staat in de samenvatting ter bevestiging. Een twijfelgeval wordt voorgelegd zoals aan een architect of engineer, niet aan een jurist:

| De redacteur kent (niet uitleggen) | Meegeven bij elk twijfelgeval | Niet meegeven |
|---|---|---|
| ArchiMate en de elementtypen; GEMMA (kennismodel, procesniveaus, functies); de opbouw van het GGM; de beslistabel en de regels van deze wiki; de gemeentelijke praktijk in grote lijnen | het begrip in één zin in gewone taal: wie doet wat, met welk object, met welk resultaat; wat de bron zegt, samengevat, met de bron als link en het artikel als vindplaats; wat er in GEMMA en het GGM staat; de opties met per optie het gevolg voor het model (welk element, welke relaties, welke pagina, wat de export in GEMMA verandert); een concreet voorbeeld uit het model; een advies met de reden; een eerder besluit met zijn zekerheid | juridische uitleg of afwegingen; lange citaten (alleen een citaat dat de doorslag geeft); uitleg van ArchiMate, GEMMA of de beslistabel; de volledige kenmerkenlijst |

Dit komt in `references/besluiten.md` van skill gemma-archimate-model-beoordelen, dat het nu al in het kort zegt.

### De toetskenmerken per type (stap 5)

Met † een relatiekenmerk: altijd ja of nee, met de tegenpartij. De andere zijn standaard ja: in de beoordeling staat alleen een nee, met onderbouwing en bron, en die wordt voorgelegd. Op de elementpagina zet het script alle toetskenmerken, ook de standaard ja.

| Type | Toetskenmerken |
|---|---|
| Bedrijfsproces, Bedrijfsinteractie | *toegewezen partij* †, *aanleiding* †, *benoembaar resultaat* |
| Procescluster | *omvat processen* † |
| Bedrijfsfunctie | *bedient gedrag* †, *toegewezen partij* †, *gebruikt objecten* †, *in functie-indeling* †, *stabiel over tijd* |
| Gebeurtenis | *leidt tot gedrag* †, *komt herhaald voor* |
| Dienst | *gerealiseerd door* †, *afnemer*, *benoembaar resultaat* |
| Product | *omvat diensten en afspraken* †, *zelfstandig aanbod*, *afnemer*, *benoembaar resultaat* |
| Bedrijfsobject, Afspraak | *wordt bewerkt* †, *onderscheidbare exemplaren*, *levenscyclus* |
| Actor | *vervult een rol* † |
| Rol, Bedrijfssamenwerking | *voert gedrag uit* † |
| Kanaal | *ontsluit een dienst* † |
| Beleidskader | *is grondslag voor* †, *in werking* |
| Capability | *gerealiseerd door* † (minstens twee functies), en expliciet *beoordeelbaar*, *onderscheidend*, *stabiel over tijd* (het type is nog in opbouw) |

## 3 Termen

Nu worden voor hetzelfde verschillende woorden gebruikt (poort, drempel, eis, kernrelatie, keuzeveld, fase A en B). Voorstel:

| Term | Betekenis | Vervangt |
|---|---|---|
| **kenmerk** | een vraag over een begrip, met een antwoord en een onderbouwing | — |
| **ja/nee-kenmerk** | een kenmerk met het antwoord ja of nee | — |
| **keuzekenmerk** | een kenmerk met een waardenlijst: precies één waarde, met het criterium per waarde en één onderbouwing met bron (bijvoorbeeld *vak*: `bedrijf/passief`) | keuzeveld |
| **relatiekenmerk** | een ja/nee-kenmerk dat een relatie beweert en zijn tegenpartij noemt: een element, of de naam en het type van een element dat er nog niet is | relationeel kenmerk |
| **standaardantwoord** en **afwijking** | het antwoord dat geldt als er niets staat; alleen een afwijking wordt geschreven, met onderbouwing en bron | "alleen een afwijking" bij de poort |
| **toetskenmerk** | een kenmerk dat ja moet zijn voor het type; een relatiekenmerk onder de toetskenmerken heet **kernrelatie** | kernrelatie, eis en drempel |
| **fase** | een van de vier delen van de beslistabel: Afbakenen, Typeren, Onderbouwen, Indelen | fase A en B; "poort" |
| **stap** | één beslissing in een fase, genummerd 0 tot en met 6 | de stappen 0 tot en met 7 |
| **Sessie** | een werksessie van de update-skill (1, 2, 3) | "Fase 1, 2, 3" in de update-skill |

Andere namen voor keuzekenmerk zijn ook mogelijk: *kenmerk met waardenlijst* (letterlijk, maar lang) of *meerkeuzekenmerk*. Ik raad *keuzekenmerk* aan: kort, en het past naast ja/nee-kenmerk.

De keuzekenmerken straks:

| Keuzekenmerk | Waarden | Stap | Nieuw? |
|---|---|---|---|
| *afhankelijkheid* | zelfstandig (standaard), eigenschap, onderdeel (zonder eigen bedrijfsproces), deelproces (geen klant tot klant), variant (geen eigen gegevens, regels of werkwijze), invoer van een ander; met het begrip waarvan het afhangt | 2 | nieuw (V1) |
| *vak* | de vakken van de ArchiMate-matrix, zoals `bedrijf/gedrag-intern`, `bedrijf/passief` | 3 | bestaat |
| *hoofdkenmerk* | bij `bedrijf/actief-intern`: handelende partij, hoedanigheid, samenwerkingsverband; bij `bedrijf/passief`: object, afspraak, representatie | 3 | bestaat; de waarden bij passief zijn nieuw (V7) |
| *soort gedrag* | bij `bedrijf/gedrag-intern`: per keer doorlopen, gegroepeerd gedrag, toestandsverandering, gezamenlijk gedrag; bij `bedrijf/gedrag-extern` volgt aangeboden gedrag uit het vak | 3 | bestaat |
| *procesniveau* | levensloopproces, bedrijfsproces, cluster naar soort werk; met het kernobject | 3 | nieuw (V2) |
| *interactievorm* | estafette (elke partij verantwoordelijk voor haar eigen deel), orkestratie (één partij verantwoordelijk voor het geheel) | 3 | nieuw (V8) |
| *eigen rechtspersoon*, *soort partij*, *landelijk* | ja of nee, bij een partij of regeling | 3 | *soort partij* komt uit stap 5 (V9) |

## 4 Wat verandert, en waarom

Gemeten op 484 beoordelingen (2026-10-18). Een beoordeling is samen 137.000 woorden: kenmerken 34%, beschrijving 20%, relaties 13%, de rest elk 4% of minder.

| # | Wijziging | Stap | Waarom (gemeten) |
|---|---|---|---|
| V1 | **Eén keuzekenmerk *afhankelijkheid*** vervangt *slechts eigenschap*, *eigen identiteit*, *zelfstandige specialisatie*, *invoer van een ander*, de stop bij *deel van object* en de deelproces-tak van *bijdrage aan groter proces*. Het type van een variant of deelproces volgt uit het begrip waarvan het afhangt; het script toetst dat dat begrip bestaat en bij een variant hetzelfde type heeft. | 2 | Nu vallen 78 begrippen pas na alle kenmerken van het type af (specialisatie 52, invoer van een ander 14, deelproces 9, deel van object 3), samen ongeveer 7.700 woorden; hetzelfde idee wordt op drie plaatsen getoetst |
| V2 | **Keuzekenmerk *procesniveau*** met kernobject vervangt *omvat levensloop*, *bijdrage aan groter proces*, *klant tot klant* en *groepeert processen*. Het script toetst de samenhang: een levensloopproces omvat de processen van zijn kernobject, een bedrijfsproces hoort bij één levensloopproces. | 3 | De tabel voor de redacteur vraagt het niveau al; daarna wordt het opnieuw afgeleid (4.575 woorden). Ongeveer 15 van de 69 inhoudelijke besluiten gaan erover |
| V3 | **Grondslag door het script**: zonder landelijke bron (`europese-regelgeving`, `rijksregelgeving`) stopt het begrip; een UPL-dienst gaat naar de hoek zonder grondslag; een functie en een capability volgen wat ze omvatten. | 4 | Vijf begrippen zijn na een volledige beoordeling afgewezen om de regel Wettelijke grondslag |
| V4 | **Toetskenmerken** in plaats van kernrelatie, eis en drempel: alle moeten ja zijn; relatiekenmerken expliciet met tegenpartij, de andere standaard ja; een nee wordt voorgelegd (nu mag één drempelkenmerk nee zijn). | 5 | De drempelkenmerken gaven bij elementen 2 keer nee in 533 antwoorden (*benoembaar resultaat* 189 van 189 ja, *afnemer* 93 van 93); ongeveer 10.000 woorden |
| V5 | **Zes annotaties bij het proces vervallen**: *eigen besluit*, *eigen normering*, *komt herhaald voor*, *leidt tot gebeurtenis*, *levert aanbod*, *gebruikt objecten* (ook bij de interactie). De relaties die de bron noemt, blijven in de beoordeling. | 5 | Ze beslissen niets; ARCHITECTURE.md, sectie 4.3, zegt zelf dat eigen besluit en normering niets zeggen over begin en eind van een proces; ongeveer 9.000 woorden |
| V6 | **Tegenhanger als het bestaande veld `tegenhanger`**; de drie kenmerken bij actor en rol vervallen. | 5 | Bij 39 rollen en actoren nooit een tegenhanger; ongeveer 1.400 woorden |
| V7 | **Hoofdkenmerk bij een ding**: object, afspraak of representatie. | 3 | *afspraak* en *waarneembare vorm* zijn bijna altijd nee met onderbouwing (2 en 10 keer ja); ongeveer 2.000 woorden |
| V8 | **Keuzekenmerk *interactievorm*** in plaats van altijd voorleggen; voorleggen alleen bij twijfel. Het kanaal blijft altijd voorgelegd, bewust, voor de centrale set. | 3 | De redacteur besliste al twee keer met dit onderscheid (Bezorgen stoffelijk overschot, Beheren Nederlanderschap); een besluit dat breder geldt, wordt een regel (ARCHITECTURE.md, sectie 3.1) |
| V9 | ***Los van verantwoordelijkheid*** wordt een afwijking (het volgt uit het hoofdkenmerk; het conflict blijft); ***soort partij*** gaat naar stap 3. | 3 | 4 van de 11 begrippen die nu na de drempel afvallen, vallen af op *soort partij* |
| V10 | **Gereedschap: het script vult de tegenpartij** van een relatiekenmerk met het id als de relatie bestaat; de AI noemt alleen een tegenpartij die nog geen element is. | 5 | De todo "Potentiële relaties vastleggen" is nu handwerk (225 open kenmerken) |

**Effect.** De grootste winst zit in de vragen die de AI niet meer hoeft te beoordelen. Elke vraag kost denkwerk: de passage zoeken, lezen en afwegen, en dan schrijven. Dat zijn de meeste tokens, meer dan de tekst die overblijft. Schatting op de 484 beoordelingen (de omzetting meet het):

| | Nu | Straks |
|---|---|---|
| Vragen die de AI beantwoordt (keuzekenmerken en kenmerken) | ongeveer 3.500 | ongeveer 1.250 (−65%) |
| Een bedrijfsproces | ongeveer 15 vragen | 5: vak, soort gedrag, procesniveau, *toegewezen partij*, *aanleiding* |
| Een begrip zonder pagina | tot 12 vragen, met de kenmerken van het type | 1 of 2, in Afbakenen |
| Begrippen in Sessie 2 (de beoordelingsagenten) | alle begrippen voorbij de poort | alleen elementen: ongeveer 100 begrippen minder |
| Woorden in de kenmerken | 44.300 | 15.000 à 20.000 |

Minder woorden geeft daarnaast een kleinere context bij het lezen van precedenten, het werkpakket en de vragen van het script. Van de 109 open kenmerken in lijkbezorging blijven er ongeveer 30, en de id's vult het script.

## 5 Uitgangspunten en regels

ARCHITECTURE.md zegt waarom het model en de wiki zijn zoals ze zijn. Het wordt gebruikt bij het maken van het kennismodel, de beslistabel, de scripts en de skills, niet bij het beoordelen. Een aanpassing werkt dus door via de beslistabel (`tools/bepaal_type.py`, waaruit `kennismodel/kenmerken-en-beslistabel.md` wordt gegenereerd) en de skills. De plannen zijn geschiedenis: wat erin besloten is, staat in ARCHITECTURE.md en in het kennismodel.

| Uitgangspunt (sectie) | Nu | Voorstel |
|---|---|---|
| Herleidbaar model (3.1) | elk kenmerk op het pad een eigen onderbouwing en bron | **A1**: elk antwoord dat tot het element leidt, heeft een bron (hieronder) |
| Herleidbaar model (3.1) | herleidbaarheid geldt niet voor de regels | **A5**: een regel noemt zijn herkomst als link naar de bronduiding van de bron van de aanpak, zonder geschiedenis (hieronder) |
| Voorrang bij het modelleren (3.7) | welk begrip › grondslag › kenmerken en type | **A2**: welk begrip › afbakening › type › grondslag › onderbouwing. De grondslag hangt af van het type (een functie volgt wat zij omvat, een UPL-dienst mag zonder) en kan dus niet eerder |
| Kenmerken eerst, type als uitkomst (4.1) | neutrale vragen, het type volgt eruit; voor vak, hoofdkenmerk en soort gedrag al vervangen door keuzekenmerken | **A3**: keuzes eerst, kenmerken als toets. De AI kiest in Typeren met keuzekenmerken; het script toetst de samenhang en leidt het type af; in Onderbouwen alleen de toetskenmerken |
| Twee fasen, de nee als dubbelcheck (4.1) | fase A en B; elke nee op het pad met onderbouwing | **A4**: vier benoemde fasen. De dubbelcheck zijn de keuzes en de kernrelaties met bron, niet de nee's |
| Alleen wat afwijkt (4.1) | alleen bij de poort | uitbreiden: ook afhankelijkheid, de toetskenmerken die geen relatie zijn, *los van verantwoordelijkheid* (in A1 en V4) |
| Kenmerk en relatie samen (4.1) | het relatiekenmerk blijft de bewering en noemt zijn tegenpartij | houden; V10 maakt het onderhoud mechanisch |
| Per type een kernrelatie en een drempel (4.1) | kernrelatie ja, hoogstens één drempelkenmerk nee | vervangen door de toetskenmerken (V4) |
| Zacht oordeel, harde vorm (3.2) | de AI oordeelt, het script beslist en rendert | **A8**: aanvullen met "kort in de beoordeling, volledig op de pagina": de AI schrijft alleen keuzes, relatiekenmerken en afwijkingen; het script toont op de pagina alles wat tot het element leidt |
| Processen en ketens (4.3) | GEMMA-ladder, deelproces zonder pagina, estafette of orkestratie | houden; V2 en V8 maken er keuzekenmerken van |
| Wanneer opnieuw akkoord (5) | de akkoord-hash telt de kenmerken | houden: na de omzetting één nieuw AKKOORD, zoals bij de vorige omzetting van de kenmerken; de publicatiegate blijft onaangetast |

### A1: een hoofdbron per element

De beoordeling heeft een lijst *bronnen*, met de hoofdbron eerst. Elk kenmerk steunt op die lijst, tenzij het zelf een andere bron noemt. De vindplaats (het artikel) staat in de onderbouwing van een keuzekenmerk, een relatiekenmerk en een afwijking; een standaardantwoord (zoals *afnemer* ja) heeft geen eigen onderbouwing en steunt op de bronnen van de beoordeling.

Is één bron genoeg? Bij 176 van de 274 elementen met bronnen bij de kenmerken dekt één bron alle kenmerken; de andere gebruiken er 2 à 3. Een lijst van 1 à 3 bronnen per element volstaat dus meestal, en een kenmerk noemt dan zelden nog een eigen bron. Nu heeft 98 van de 296 elementen geen lijst *bronnen*: de omzetting vult die uit de bronnen van de kenmerken.

### A5: bronnen van de aanpak

Het kennismodel noemt per kenmerk een herkomst als tekst, zoals "GEMMA (definitie Bedrijfsproces)" of "GEMMA Online, Proceshiërarchie (PH 81)". Voor Over GEMMA, de GEMMA Proceshiërarchie en GEMMA Impact ketensamenwerking bestaan al bronduidingen (`modellen/gemma/bronduidingen/overig/`), maar het kennismodel en ARCHITECTURE.md linken er niet naar. Voor ArchiMate (12 keer als herkomst) en NORA (3 keer) is er geen bronduiding. Voorstel: ArchiMate en NORA opnemen als bron met een bronduiding, de herkomst in het kennismodel als link naar de bronduiding met vindplaats, en ARCHITECTURE.md, sectie 3.1, aanvullen: een regel noemt zijn herkomst. De bronnen zijn stabiel; daarna kost het weinig onderhoud.

### A6: de criteria voor het niveau van een onderwerp

De update-skill verwijst bij stap 1 naar ARCHITECTURE.md, sectie 3.3, voor de criteria van het niveau van een onderwerp (eigen, thematisch, kern). Volgens de regels van de wiki staat wat geldt in het kennismodel en de modelleerregels, en waarom in ARCHITECTURE.md; een skill verwijst ernaar en herhaalt het niet. De regel Thuishoren noemt de criteria al kort, en de update-skill leest de modelleerregels al in Sessie 1. Voorstel: de criteria volledig in de regel Thuishoren, ARCHITECTURE.md houdt het waarom, en de update-skill verwijst naar de regel. Zo is er geen dubbele tekst en leest het beoordelen ARCHITECTURE.md niet.

### A7: de termen

De termen uit hoofdstuk 3 in het kennismodel, de modelleerregels, de skills, ARCHITECTURE.md en de scripts.

## 6 Risico's

- **V1**: een variant wordt afgebakend zonder de kenmerken van het type. De vraag blijft gelijk ("eigen gegevens, regels of werkwijze"), de tabel na Typeren toont elke variant, en regel Objectbehoud vangt een latere wijziging op.
- **A1, A4, V4**: minder dwang om te toetsen. De keuzes en de kernrelaties blijven expliciet, met bron; de standaard ja gaf bij elementen 2 keer nee in 533 antwoorden, en de poort werkt al zo.
- **V4**: twee elementen die nu één drempelkenmerk nee hebben, worden voorgelegd.
- **V5**: wie een proces inricht, ziet *eigen besluit* en *eigen normering* niet meer als kenmerk; ze kunnen in de beschrijving staan.
- **Omzetting**: alle goedgekeurde beoordelingen gaan naar review, met één nieuw AKKOORD; elke uitkomst die verandert, wordt per geval voorgelegd.
- **Buiten dit plan**: na de kenmerken zijn de beschrijving (20%) en de relaties (13%) het grootst. Een vervolgplan kan ze lichter maken.

## 7 Besluiten van de redacteur

Elk apart voorgelegd (regel Per geval), en op 2026-10-18 door de redacteur genomen:

- V1 *afhankelijkheid* als keuzekenmerk in stap 2, met de zes waarden: ja.
- V2 *procesniveau* als keuzekenmerk in Typeren, zonder *klant tot klant* als extra toets: ja.
- V3 grondslag door het script: ja.
- V4 toetskenmerken, alle ja, een nee wordt voorgelegd (geen telling meer): ja.
- V5 de zes annotaties bij het proces vervallen, zonder vrij veld: ja.
- V6 tot en met V10: ja.
- A1 tot en met A8: ja.
- Alleen echte twijfel voorleggen, met de tabel uit hoofdstuk 2, in `references/besluiten.md`: ja.

## 8 Uitvoering, na de besluiten

1. Dit plan met de besluiten vastleggen (gedaan, 2026-10-18).
2. `tools/bepaal_type.py`: `REGELS`, `TYPEN` (toetskenmerken in plaats van kern, eis en drempel), `POORT_STOP`, `TYPEGROEP`, `STAP_7`, `pad`, `fase_a`, `fase_b_type`, `_stap_5_en_6`, `_stap_7`, `vragen`, `KEUZEVELDEN`, `STANDAARD`, de termen; `schemas/beoordeling.schema.json` (*afhankelijkheid*, *procesniveau*, *interactievorm*); `tools/beoordeling.py normaliseer` vult de tegenpartij uit de relaties (met `relaties_bij`); `tools/render.py` toont alle kenmerken die tot het element leiden, ook de standaard ja; tests in `tools/tests/`; `tools/kennismodel.py` genereert de beslistabel met de herkomst als link (woordbudget kennismodel 17.100) (middel).
3. Bronnen ArchiMate en NORA opnemen met skill wiki-ingest en een bronduiding (middel).
4. ARCHITECTURE.md 3.1, 3.2, 3.3, 3.7, 4.1; de regel Thuishoren; skills gemma-archimate-model-criteria, -beoordelen (met `references/besluiten.md`: alleen echte twijfel, en hoe) en -update, binnen hun woordbudget (middel).
5. Omzettingsscript voor de 484 beoordelingen: vervallen kenmerken eruit, de keuzekenmerken uit de huidige uitkomst, de lijst *bronnen* gevuld (middel).
6. Beslissen, verschillen per geval voorleggen, AKKOORD, `tools/afronden.py`, commit `rules:` (hoog, daarna laag).
7. Verder met lijkbezorging, deel 2 van de todo (middel).

## 9 Verificatie

- `uv run pytest wikis/gemma-archimate-model/tools/tests -q`.
- Vóór en na de omzetting de `beslist.yaml` van alle onderwerpen vergelijken: soort, type, procesniveau en objectniveau per begrip gelijk; elk verschil apart voorleggen.
- `uv run python tools/beslissen.py` zonder fouten; `uv run python tools/archimate_export.py --check`; `uv run python -m llmwiki lint` (woordbudgetten); de render-check via `tools/afronden.py`.
- De woorden in de kenmerken vóór en na tellen.

## Bijlage: elk kenmerk, nu en straks

| Kenmerken (nu) | Straks | Wijziging |
|---|---|---|
| *herkenbaar*, *gemeentelijk*, *buiten dit model*, *betekenis in onderwerp* | stap 1, afwijking | — |
| *slechts eigenschap*, *eigen identiteit*, *zelfstandige specialisatie*, *invoer van een ander*, *deel van object* | stap 2, waarden van *afhankelijkheid*; het subobject (2 gevallen) herkent het script in stap 6 | V1 |
| *bijdrage aan groter proces*, *klant tot klant*, *omvat levensloop*, *groepeert processen* | stap 2 (deelproces) en stap 3 (*procesniveau*) | V1, V2 |
| de hoofdkenmerken, de soorten gedrag | stap 3, keuzekenmerk | — |
| *afspraak*, *waarneembare vorm* | stap 3, waarden van *hoofdkenmerk* bij een ding | V7 |
| *los van verantwoordelijkheid* | stap 3, afwijking | V9 |
| *eigen rechtspersoon*, *landelijk*, *soort partij* | stap 3 | V9 |
| *benoembaar resultaat*, *afnemer*, *stabiel over tijd*, *in werking*, *komt herhaald voor* (gebeurtenis), *onderscheidbare exemplaren*, *levenscyclus* (bedrijfsobject), *zelfstandig aanbod* | stap 5, toetskenmerk, standaard ja | V4 |
| de relatiekenmerken in de tabel van stap 5 | stap 5, toetskenmerk, expliciet met tegenpartij | V4, V10 |
| *eigen besluit*, *eigen normering*, *komt herhaald voor*, *leidt tot gebeurtenis*, *levert aanbod*, *gebruikt objecten* (proces en interactie) | vervallen; de relaties blijven | V5 |
| *onderscheidbare exemplaren*, *levenscyclus*, *wordt bewerkt* (actor en rol) | vervallen; het veld `tegenhanger` | V6 |
| *generiek* | stap 6, afwijking | — |
