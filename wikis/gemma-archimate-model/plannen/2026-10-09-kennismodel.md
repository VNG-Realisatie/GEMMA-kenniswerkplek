# Plan: het kennismodel van gemma-archimate-model

## 1. Doel

Eén overzichtelijke plek die beschrijft hoe het model eruitziet (het kennismodel), één document dat uitlegt waarom (ARCHITECTURE.md), en een model dat herleidbaar is tot bronnen en besluiten. Regels, skills en documentatie hoeven niet herleidbaar te zijn; consistentie en overzicht gaan voor het vermijden van nieuwe beoordelingen.

## 2. Hoe het gaat werken

### 2.1 Vier plekken, elk één taak

| Plek | Taak | Herleidbaar? |
|---|---|---|
| **ARCHITECTURE.md** | Leidend: doel, uitgangspunten, voorrang en het waarom, hoog over; hoe de wiki werkt. Verwijst naar het kennismodel | nee (Git is de geschiedenis) |
| **kennismodel/** | Wat het model is: alle concepttypen en de regels die de modellering raken. Metadata, geen aantallen | nee |
| **AGENTS.md** | De werkwijze van de AI (Navragen, Per geval, Elke claim een bron, …) en de kaart *Waar vind je wat* | nee |
| **skills** | Hoe je het doet: stappen en sjablonen; ze verwijzen naar het kennismodel en herhalen het niet | nee |
| **beoordelingen/** | Het model zelf: per begrip het oordeel, de gevonden relaties en de besluiten van de redacteur; per onderwerp de besluiten over het onderwerp als geheel | **ja** |

Geen datums of "besluit redacteur" in regels en skills. `docs/`, `besluiten/` en `beoordelingen/besluiten-eerder.yaml` vervallen.

### 2.2 Het kennismodel

Gegenereerd uit één bron, `tools/kennismodel.py`, behalve `modelleerregels.md`. Ingedeeld zoals ArchiMate en GEMMA, per architectuurlaag.

```
kennismodel/
├── README.md                      overzicht: elementtypen per laag, relatiematrix (toegestaan), indelingen
├── modelleerregels.md             regels voor alle elementen, met de voorrangsregels (met de hand)
├── indelingen.md                  per indeling: wat, waarnaar, niveaus, groepering (GEMMA of wiki), regels
├── kenmerken-en-beslistabel.md    één vragenlijst (vraag, voorbeeld ja/nee, herkomst) + de stappentabel
├── bedrijfsarchitectuur/
│   ├── <type>-modelleerafspraken.md   bedrijfsobject, afspraak, product, dienst, bedrijfsproces, bedrijfsfunctie,
│   │                                  gebeurtenis, actor, rol, bedrijfssamenwerking, kanaal, bedrijfsinteractie
│   └── weggefilterd.md                elementtypen van de laag die niet tot een element leiden (representatie, locatie)
├── motivatie/                     beleidskader-modelleerafspraken.md · weggefilterd.md (doel, principe, eis, waarde, …)
└── applicatiearchitectuur/        data-object-modelleerafspraken.md (nu een annotatie) · weggefilterd.md
```

Kaarten en indelingen samen zijn alle concepttypen:
- elementtypen;
- relatietypen, met de kernrelatie;
- eigenschappen per type;
- niveaus en profielen (levensloopproces, kernobject, GEMMA-profiel);
- vaste relatienamen (handelingen, verantwoordelijkheden, grondslag);
- koppelingen naar buiten het model (GGM-entiteit, GEMMA-element, generiek GEMMA-element, data-object);
- de indelingen;
- per laag de elementtypen die niet tot een element leiden.

**Modelleerafspraken van één elementtype** (voorbeeld):

```
# Bedrijfsproces (Business Process) — modelleerafspraken
Definitie      Reeks opeenvolgend uit te voeren activiteiten … (GEMMA)
In Over GEMMA  ja (Bedrijfsproces)
Herken je aan  gedrag · per keer doorlopen          → kenmerken-en-beslistabel
Kernrelatie    Rol ─toewijzing→ Bedrijfsproces  (kenmerk toegewezen partij)
Drempel        aanleiding · benoembaar resultaat
Niveaus        levensloopproces (omvat levensloop; GEMMA-profiel Bedrijfsproces (cluster))
               › bedrijfsproces (klant tot klant) › deelproces (geen pagina; veld deelprocessen)
               cluster naar soort werk (groepeert processen)
Eigenschappen  kernobject · afnemer · gemma_generiek · deelprocessen · gemma (match)
Indelingen     Procesindeling naar kernobject · naar soort werk · Beleidsdomeinindeling (via kernobject)
Naamvorm       infinitief met object in GEMMA-volgorde: Behandelen aanvraag
Afstemming     GEMMA: match of specialisatie van een generiek GEMMA-bedrijfsproces; GGM: geen
Voorbeeld      wel: Verlenen grafrecht · niet: Uitreiken reisdocument (deelproces)

## Relaties (in het kennismodel van de wiki; gaan mee in de export)
| Richting | Relatie              | Ander type     | Namen                                                    | Kern | In Over GEMMA |
| in       | toewijzing           | Rol            | —                                                        | ja   | ja |
| uit      | toegang              | Bedrijfsobject | registreren, bijwerken, beëindigen, … (8 handelingen)    |      | ja |
| uit      | realisatie           | Dienst         | —                                                        |      | ja |
| in       | associatie (gericht) | Beleidskader   | is grondslag voor, werkt uit voor, geeft richtlijn voor  |      | ja |
| uit      | stroom               | Bedrijfsproces | levert aan                                               |      | nee → terugmelding kennismodel |

## Weggefilterd (niet in het kennismodel van de wiki; de export laat ze weg)
| Relatie                                     | Reden                                  |
| Actor ─toewijzing→ Bedrijfsproces           | een actor hangt via een rol aan gedrag |
| Bedrijfsfunctie ─aggregatie→ Bedrijfsproces | een functie bedient een proces         |
```

**Weggefilterd of niet in Over GEMMA** zijn twee verschillende dingen:
- **Weggefilterd:** niet in het kennismodel van de wiki. De export laat het weg; de reden staat erbij.
- **Niet in Over GEMMA:** wel in het kennismodel van de wiki, maar niet in het GEMMA-kennismodel. Het gaat mee in de export, gemarkeerd, en is een kandidaat voor een terugmelding over het kennismodel.

### 2.3 Modelleerregels en voorrang (`kennismodel/modelleerregels.md`; hoog over in ARCHITECTURE.md)

**Welke regel waar.** De namen blijven gelijk, want `tools/signalen.py` noemt ze.

| Regel | Plek |
|---|---|
| Navragen, Eén naamgeving, Bestaand bijwerken, Per geval, Letterlijk verplaatsen, Elke claim een bron, Zonder bron, Geen absolute taal, Drie registers, GEMMA-terugmeldingen formuleren | AGENTS.md (werkwijze) |
| Beslistabel beslist, Match op betekenis, Zwakke match voorleggen, Eén element in het hele model, Thuishoren, Relaties tussen onderwerpen, Gemeentelijk perspectief, Tegenspraak, Wettelijke grondslag, Bronvoorrang, Begrijpelijk, Los van het onderwerp, Afwijken mits teruggemeld, Objectbehoud | `kennismodel/modelleerregels.md` |
| Naamvorm, drempel, niveaus, toegestane en weggefilterde relaties | de modelleerafspraken van het type |
| Alles ingedeeld, beleidsdomein via kernobject, functieketen, één levensloopproces per kernobject | `kennismodel/indelingen.md` |

**Bronnen.** Wat formeel geldt: europese-regelgeving › rijksregelgeving › informatiemodel (zoals de UPL, RSGB, RGBZ) › richtlijn › gemeentelijke-regelgeving › beleid › overig. De naam komt uit de gangbare taal; voorrang bepaalt nooit of iets een element is. Het GGM en het GEMMA-model zijn geen bron maar matchdoel; de UPL is bron én matchdoel.

**Een element modelleren, in deze volgorde:**
1. Welk begrip? Synoniem of homoniem (stap 0).
2. Grondslag: de juiste landelijke wettelijke bron, met het artikel.
3. Kenmerken → type, via de beslistabel. De uitkomst is bindend.
4. Kernrelaties, uit dezelfde wettekst.
5. Indeling en indelingsrelaties.
6. Overige relaties, uit de bronanalyse.
7. Matches.

**Matchen**, door de AI (kandidaten met `tools/ggm.py` en `tools/gemma.py`; het script haalt daarna alleen de letterlijke velden op):

| Match | Typen | Wat het doet | Zonder match |
|---|---|---|---|
| UPL (ook bron) | product, dienst | een UPL-item valt nooit weg; de naam letterlijk uit de UPL | procesarchitectuur-terugmelding |
| GGM | bedrijfsobject, data-object; beleidsdomein | matchdoel en toets: entiteit, definitie, relaties; per beleidsdomein de dekking | GGM-terugmelding (hiaat) |
| GEMMA-model | alle elementtypen | het id gaat mee in de export en overschrijft naam en definitie; zwak of partieel voorleggen | nieuw element via de export; GEMMA-terugmelding als een GEMMA-element vervalt |
| Generiek GEMMA-element | gebeurtenis, rol, dienst, bedrijfsproces | specialisatie (`gemma_generiek`) | voorstel aan GEMMA |
| GEMMA-kennismodel (Over GEMMA) | elementtypen en relatietypen | namen en definities van de typen | in de export gemarkeerd als niet in Over GEMMA |
| Indelingslijsten | typen met een indeling | Iv3-taakveld, GGM-beleidsdomein, GEMMA-domein, GEMMA-procesarchitectuur (soort werk) | nieuwe groepering in de export; terugmelding |

**Relaties.** Ter uitleg als aparte stappen; bij het beoordelen gebeuren ze vaak tegelijk, uit dezelfde wettekst:
1. grondslag (*is grondslag voor* vanuit een beleidskader);
2. kernrelatie van het type;
3. indelingsrelaties (levensloopproces → aggregatie → bedrijfsproces, functieketen, kernobject);
4. overige relaties uit de bronanalyse (per partij wat zij houdt, beheert, uitvoert of vervult; toegang met een handeling of verantwoordelijkheid);
5. GGM-match van de relatie, alleen bij bedrijfsobjecten, data-objecten en beleidsdomeinen (`ggm_match: exact | geen`);
6. GEMMA (geen match: de relatie gaat als nieuw mee in de export).

De beoordeling legt alle gevonden relaties vast; alleen de geldigheid in ArchiMate is een harde eis. De export neemt alleen relaties mee die in het kennismodel staan. Een relatietype later toevoegen of weghalen is opnieuw filteren, geen herbeoordeling. Welke gevonden relaties wegvallen, staat in het exportrapport en op de pagina van het element.

**Thuishoren** (te toetsen tijdens het beoordelen):
- **Een bedrijfsobject:** eigen onderwerp (waar het ontstaat en beheerd wordt) › thematisch gedeeld onderwerp (ook beheerd vanuit een ander onderwerp) › Kern (te breed voor een thema).
- **Proces, dienst, product, gebeurtenis:** het onderwerp van het kernobject.
- **Actor, rol, functie, beleidskader, kanaal:** geen eigen thuis; een gedeeld onderwerp of Kern zodra meer onderwerpen ze gebruiken.

Andere onderwerpen gebruiken het element met een relatie en maken geen kopie; een begrip mag verhuizen.

### 2.4 Onderwerpen

| Laag | Onderwerpen | Voorbeelden |
|---|---|---|
| Eigen onderwerp | Burgerzaken, Lijkbezorging, Participatie, … | Graf, Reisdocument, Stoffelijk overschot |
| Thematisch gedeeld | Besluitvorming · Bestuur en organisatie · Heffingen en betalingen · Adressen en gebieden (groeit met het beoordelen) | Besluit, Beschikking, Vergunning, Regeling · Gemeente, Gemeenteraad, College van B&W, Burgemeester, Beslisser, Rijk · Heffing, Heffingsverordening |
| Kern | Kern | wat echt overal is, bij voorkeur met een match in GGM 99-kern (Persoon, Adres, Zaak, Document). Ook de bronanalyses voor het kennismodel (Over GEMMA, Proceshiërarchie, Impact van ketensamenwerking) |

Algemeen vervalt; de 15 elementen ervan worden per geval verdeeld.

### 2.5 Export naar Archi

- **Het kennismodel van de wiki gaat mee:** een concept per elementtype, een relatie per toegestaan relatietype, en de indelingen als groeperingsconcept. Ze krijgen het id uit Over GEMMA waar dat bestaat.
- **Eigenschappen:** `wiki-gemma-model kernrelatie` (ja/nee) en `in Over GEMMA` (ja/nee); geen aantallen.
- **Het GEMMA-kennismodel uit Over GEMMA** blijft een eigen groep, ter vergelijking.
- **De relaties van de elementen** worden gefilterd op het kennismodel. Het rapport noemt de weggelaten relaties, en wat niet in Over GEMMA staat als kandidaat voor een terugmelding.

### 2.6 Besluiten over het model

- Een besluit over een begrip staat in de `besluiten:` van zijn beoordeling, een besluit over een onderwerp als geheel in de `besluiten:` van het onderwerp. Een begrip zonder beoordeling krijgt zijn besluit voorlopig bij het onderwerp. Er is geen register en geen apart overzicht; de begrippenlijst van een onderwerp toont de besluiten over het onderwerp.
- Wat al besloten is, vraag je niet opnieuw (regel Navragen).
- Een besluittekst noemt een regel of ARCHITECTURE-sectie bij naam, nooit een bestandspad.
- Een besluit over de werkwijze verwerk je in de regel of skill, zonder register.

### 2.7 Naamgeving

| Nu | Wordt | Toelichting |
|---|---|---|
| Regelgevingindeling | **Grondslagindeling** | Overal: code, export (alleen de naam; de sleutel van `vast_id` blijft, dus de id's blijven gelijk), `wiki.yaml` (submap `regelgeving` → `grondslag`), tekst |
| element-veld `grondslag` + `grondslag_toelichting` | **vervalt**; wat het toevoegde komt in `ggm:` | De toelichting bij `procesobject` en `ggm-afgeleid` gaat naar `ggm.onderbouwing`; `regelgeving` en `bron` vallen weg; de reden "grondslag regelgeving: altijd voorleggen" vervalt |
| relatie-veld `grondslag` (`ggm-exact`, `ggm-afgeleid`, `bron`) | **`ggm_match: exact \| geen`** | Een relatie die `tools/relaties.py` uit een GGM-keten afleidt (A–X–B → A–B) is geen match: `geen`, met de keten in `ggm_relatie` en de GGM als bron |
| stap *afleiden*, `tools/afleiden.py`, `curation.afleiden`, blok `afgeleid:` | **beslissen en renderen**, `tools/beslissen.py`, `curation.beslissen`, blok `beslist:` | Ook in de gedeelde llmwiki-code (`SCRIPTVELDEN`, `akkoord.draai_script`) en de sjabloonwiki's; het blok is een scriptveld, dus geen nieuw akkoord |
| "grondslag" | alleen de **wettelijke grondslag** | de regel Wettelijke grondslag, de relatie *is grondslag voor*, de Grondslagindeling |
| pagina per elementtype | `<elementtype>-modelleerafspraken.md` | in de taal van *Over GEMMA: kennismodel en modelleerafspraken* |

### 2.8 ARCHITECTURE.md (leidend, hoog over)

| Hoofdstuk | Essentie |
|---|---|
| **1 Doel** | Een onderbouwd, herleidbaar GEMMA-architectuurmodel van de bedrijfslaag, voor het GEMMA-team. Het resultaat is de Archi-export die in GEMMA wordt geïmporteerd. Kwaliteit en herleidbaarheid gaan voor snelheid. |
| **2 Plaats in de keten** | Bronnen (wetten, informatiemodellen zoals de UPL, richtlijnen, beleid) → de wiki → de export → GEMMA. Matchdoelen: het GGM, het GEMMA-model, de UPL, Over GEMMA en de indelingslijsten. Terugmeldingen gaan naar de werkgroep procesarchitectuur, GGM-beheer en het GEMMA-team. |
| **3 Uitgangspunten en voorrang** | 3.1 **Herleidbaar model** (het model wel; regels, skills en documentatie niet). 3.2 **Zacht oordeel, harde vorm**: de AI oordeelt (kenmerken, tekst, matches, relaties); het script beslist en rendert; de redacteur geeft akkoord; wat een script garandeert, is geen regel. 3.3 **Eén model**: een begrip komt één keer voor; thuishoren als voorrangsregel; een begrip mag verhuizen. 3.4 **Voor alle gemeenten**: een landelijke grondslag; een VNG-model voor gemeentelijke regelgeving; alleen een UPL-product blijft zonder. 3.5 **GEMMA volgen**, of afwijken en terugmelden. 3.6 **Consistentie boven behoud**: wordt het resultaat beter, dan opnieuw beoordelen. 3.7 **Voorrang** hoog over (bronnen, modelleren, matchen, relaties, thuishoren) → `kennismodel/modelleerregels.md`. |
| **4 Het kennismodel** | Wat de concepttypen zijn (zie 2.2), en het waarom per onderwerp. 4.1 Elementtypen en kenmerken (kenmerken eerst, type als uitkomst, kernrelatie en drempel, namen uit het GEMMA-kennismodel). 4.2 Relaties (gevonden tegenover gefilterd; een actor via een rol; toegang met vaste handelingen en verantwoordelijkheden, uit de wetten van de basisregistraties, de AVG en de Archiefwet). 4.3 Processen en ketens (GEMMA-ladder; levensloopproces per kernobject, anders worden 500 producten 500 processen; klant tot klant; deelproces zonder pagina; estafette is een bedrijfsinteractie, bij orkestratie *Leveren dienst aan derden*; geen ketenproces). 4.4 Indelingen (GEMMA volgen; alles ingedeeld; Beleidsdomeinindeling, Functie-indeling naar domein, Procesindeling naar kernobject en naar soort werk, Ketensamenwerking, Doelgroepindeling, Grondslagindeling). 4.5 Synoniemen en homoniemen (stap 0). |
| **5 Werkstroom en status** | Onderwerp → bronnen → beoordelen → beslissen en renderen (script) → voorleggen → akkoord → export → commit; de statussen, en wanneer een akkoord opnieuw nodig is. |
| **6 Hoe de wiki werkt** | Plattegrond; beoordelingen en registers; beslissen, renderen en controles; GGM en GEMMA als matchdoel lezen; export (id's, mappen, objectbehoud, volledige sync, kennismodel, filter, rapport). |
| **7 Nog niet gebouwd** | Applicatielaag, views in de export, dekkingsanalyse van het GGM. |

Wat nu in `docs/` staat, gaat op in hoofdstuk 3 en 4 (de kern van de afweging, zonder datums) en in `kennismodel/`. Tellingen, ijkingen en vergelijkingen met eerdere standen vervallen; die staan in Git.

## 3. Verschil met nu, en waarom het beter is

| Nu | Straks | Waarom beter |
|---|---|---|
| Kenmerken en beslistabel in vier tot zes vormen, ruim 900 regels; het beeld van één type verspreid over zes plekken | Eén pagina modelleerafspraken per type; één vragenlijst en één stappentabel | Je ziet een type op één scherm; geen dubbele tekst die uit de pas loopt |
| Regels in AGENTS.md mengen werkwijze en modellering; uitwerking in references en docs | Werkwijze in AGENTS.md, modelleerregels in het kennismodel, het waarom in ARCHITECTURE.md | Elke soort regel op één plek; ARCHITECTURE.md is het ene document om te begrijpen |
| Regels en skills dragen datums en besluiten mee (20 plekken); besluitentabellen met Stand in docs | Geen datums in regels en skills; geen werkwijze-register; Git is de geschiedenis | Regels lezen als regels; herleidbaarheid alleen waar ze telt: het model |
| Besluiten per begrip deels in beoordelingen, deels in een register (39 rijen), plus een gegenereerd overzicht | Elk besluit bij zijn begrip of onderwerp | Eén plek per besluit; niets dubbel |
| Een pad in een besluittekst maakt het akkoord afhankelijk van de bestandsstructuur (ARCHITECTURE.md §6: `inhoud_hash` in `tools/llmwiki/beoordeling.py` neemt alle velden mee behalve de scriptvelden) | Besluitteksten noemen een regel of sectie bij naam | Herstructureren raakt het model niet meer |
| `tools/afleiden.py` weigert een gevonden relatie die niet in de GEMMA-afspraken past | De beoordeling legt elke gevonden, in ArchiMate geldige relatie vast; de export filtert op het kennismodel | Niets wat de bron zegt gaat verloren; het kennismodel aanpassen is opnieuw filteren |
| Het kennismodel in de export is alleen Over GEMMA, plus wat de wiki extra gebruikt | Het volledige kennismodel van de wiki, met kernrelaties en de markering *in Over GEMMA* | GEMMA ziet de modelleerafspraken van de wiki, en wat ervan afwijkt |
| "Grondslag" betekent drie dingen: het element-veld (273× ingevuld: 241 `bron`, 18 `regelgeving`, 10 `ggm-entiteit`, 4 `procesobject`), het relatie-veld (795 `bron`, 1 `ggm-exact`) en de wettelijke grondslag | Alleen de wettelijke grondslag; GGM-match in `ggm:` en `ggm_match` | Eén woord, één betekenis; het element-veld was een GGM-match, gemengd met wat het type of de bronnen al zeggen |
| Het GGM staat als bron in de bronvoorrang en in de regels (AGENTS.md, skill ingest, ARCHITECTURE.md §1 en §10, beoordelen §2 en §6). In de praktijk: 1 beoordeling met het GGM als bron, 27 met het GEMMA-model | GGM en GEMMA-model alleen matchdoel; de UPL bron én matchdoel | Bron en toets niet meer door elkaar; een claim steunt op een bron, niet op wat we ertegen matchen |
| *Afleiden* zegt niet wat het script doet | *Beslissen en renderen* | De naam zegt wat er gebeurt |
| Thuishoren: elk element een thuisonderwerp; Algemeen als restbak | Voorrangsregel: eigen onderwerp › thematisch gedeeld › Kern; alleen objecten hebben echt een thuis | Herkenbare onderwerpen; aansluiting op GGM 99-kern |
| Weggefilterd en "niet in Over GEMMA" niet te onderscheiden | Twee aparte markeringen | Je ziet wat de wiki weglaat en wat GEMMA (nog) niet kent |

Gevolgen voor de beoordelingen: geen bestaande relatie hoeft te veranderen. De 44 combinaties van brontype, relatie en doeltype in de beoordelingen zijn alle geldig in ArchiMate. Kandidaten die buiten een strikt kennismodel kunnen vallen (per soort voor te leggen):
- beleidskader → associatie → rol, gebeurtenis, bedrijfsobject of beleidskader;
- gebeurtenis → associatie → bedrijfsobject;
- rol → associatie → rol;
- actor → associatie → actor;
- bedrijfsobject → associatie → dienst.

De veldnamen, de eerdere besluiten, de paden, de onderwerpen en de signalen veranderen wel beoordelingen; dat gebeurt in fase 5, met één AKKOORD.

## 4. Uitvoering

### Fase 0 — Plannen in de repository (denkniveau laag; eerst, in deze sessie)
Plannen staan nu in `~/.claude/plans/`, buiten de repository: niet in Git, niet op een andere werkplek. Ze gaan naar de plek waar ze gelden, met een duidelijke titel en de datum vooraan. De inhoud blijft ongewijzigd; alleen harde regelovergangen worden hersteld (`llmwiki ontvouw --schrijf`, want `llmwiki lint` controleert dat).

| Nu (`~/.claude/plans/`) | Wordt |
|---|---|
| `ik-begin-het-overzicht-pure-wreath.md` (dit plan) | `wikis/gemma-archimate-model/plannen/2026-10-09-kennismodel.md` |
| `wordt-functie-lijkbezorging-dan-reactive-blossom.md` | `wikis/gemma-archimate-model/plannen/2026-10-04-indelingen-kenmerken-en-herbeoordeling-lijkbezorging.md` |
| `analyseer-de-bestaande-home-mark-documen-silly-bentley.md` | `wikis/gemma-archimate-model/plannen/2026-09-29-bedrijfsarchitectuur-wiki-overnemen.md` |
| `lees-de-3-documenten-shimmying-kay.md` | `docs/plannen/2026-09-28-klus-2-pywikibot-en-drie-wiki-soorten.md` (repository) |

Daarna:
- de originelen in `~/.claude/plans/` weghalen;
- de kaart *Waar vind je wat* in AGENTS.md en ARCHITECTURE.md §6 krijgen de map `plannen/`;
- `lint` draaien en committen op main.

Een plan dat klaar is, blijft als geschiedenis in `plannen/`; wat geldt, staat in ARCHITECTURE.md en `kennismodel/`. Het plan van de herstructurering van 2026-10-08 bestaat niet meer apart (dit bestand is overschreven); de uitvoering staat in de commits 6a2a34e tot en met ec09e20.

### Fase 1 — Het kennismodel als één bron (denkniveau hoog voor de inhoud, middel voor de bouw)
1. Nieuw `tools/kennismodel.py`, gebouwd op wat er al is:
   - **elementtypen per laag** uit `bepaal_type.TYPEN`, aangevuld met het relatietype en de richting van de kernrelatie, de naamvorm, de eigenschappen (`VERPLICHT`, `EXTRA_VELDEN`, `WAARDEN`), de niveaus en profielen, *in Over GEMMA*, en de afstemming met GGM en GEMMA;
   - **relaties per type**: toegestaan (bron, relatie, doel, namen, kern, toegangstype, in Over GEMMA) en weggefilterd (met de reden). Startpunt zijn de 44 combinaties, `relaties.TOEGESTAAN`, de GEMMA-uitzonderingen in `relaties.toegestaan()` (die worden weggefilterd, met reden), en `HANDELINGEN` en `VERANTWOORDELIJKHEDEN`;
   - **indelingen** uit `bepaal_type.INDELING_PER_TYPE` en `tools/archimate_export.py`, met de Grondslagindeling;
   - **elementtypen zonder element per laag**: representatie en locatie; doel, principe, eis, beperking, waarde, uitkomst en vermogen; groepering als thema.

   `bepaal_type.py`, `relaties.py` en `archimate_export.py` lezen hieruit in plaats van eigen tabellen te houden.
2. De twijfelgevallen in de relatielijst leg ik de redacteur per soort voor, één voor één.
3. Genereren naar `kennismodel/` (zie 2.2), met paginatype `kennismodel` en een schema. Een check in de pre-commit bewaakt dat de pagina's gelijk zijn aan de bron.
4. `modelleerregels.md` met de hand schrijven: de regels uit 2.3, letterlijk uit AGENTS.md en de references (`onderwerpen.md`, `grondslag.md`), zonder datums, plus de voorrangsregels.
5. De criteria-skill wordt alleen werkwijze, met de gegenereerde vragenlijst en verwijzingen naar de modelleerafspraken; `docs/beslistabel.md` vervalt.
6. Regelgevingindeling → Grondslagindeling.
7. Tests: elk type heeft modelleerafspraken; elke kernrelatie staat in de relaties van haar type; elke laag heeft `weggefilterd.md`; de pagina's zijn gelijk aan de bron.

### Fase 2 — Gevonden relaties en filter (denkniveau middel)
1. `tools/afleiden.py`: alleen de ArchiMate-geldigheid blijft een fout.
2. `tools/signalen.py`:
   - een signaal bij een relatie buiten het kennismodel;
   - een signaal bij een kenmerk dat een kernrelatie is, met de waarde ja maar zonder relatie van dat type.
3. `tools/render.py`: een relatie buiten het kennismodel staat op de pagina met *niet in het kennismodel, gaat niet mee in de export*.
4. `references/relaties.md`: de volgorde uit 2.3; leg de gevonden relaties vast; de relatietabel verwijst naar de modelleerafspraken.

### Fase 3 — Kennismodel in de export (denkniveau middel)
1. `tools/archimate_export.py`:
   - de groep *Kennismodel-wiki* wordt het volledige kennismodel (zie 2.5), met hergebruik van `CONCEPT_VOORKEUR` en `laad_kennismodel`;
   - de relaties van de elementen worden gefilterd;
   - het rapport noemt wat wegvalt en wat niet in Over GEMMA staat.
2. Skill archimate-export en de tests bijwerken.

### Fase 4 — Naamgeving, ARCHITECTURE.md, opruimen (denkniveau hoog voor de tekst, middel voor het hernoemen)
1. Hernoemen *afleiden* → *beslissen en renderen* (zie 2.7), in:
   - het wiki-script en zijn imports en tests;
   - `wiki.yaml` en de sjabloonwiki's;
   - `tools/llmwiki/akkoord.py` en `tools/llmwiki/beoordeling.py`;
   - het blok `afgeleid:` → `beslist:` in alle beoordelingen;
   - `render.py`, `signalen.py`, `archimate_export.py`, de skills en `docs/onderbouwing.md` van de repository.
2. ARCHITECTURE.md opnieuw schrijven (zie 2.8).
3. `git rm -r docs besluiten`. De lijst per begrip vervalt in `tools/render.py`; de begrippenlijst krijgt een sectie *Besluiten* uit het onderwerp; paginatype `doc` vervalt.
4. AGENTS.md alleen werkwijze en kaart. Geen datums of "besluit redacteur" in AGENTS.md, skills en references.
5. De bronanalyses in `bronanalyses/algemeen/` en `todo.md` verwijzen naar ARCHITECTURE-secties of `kennismodel/`.
6. Het GGM alleen als matchdoel, op deze plekken:
   - AGENTS.md en skill ingest: de bronvoorrang zonder GGM;
   - de intake van het GGM: brontype `model`;
   - ARCHITECTURE.md;
   - skill beoordelen §2: per beleidsdomein de dekking toetsen in plaats van GGM-entiteiten als begrippen te verzamelen;
   - skill beoordelen §6 en `tools/relaties.py voorstel`: GGM-relaties alleen om een gevonden relatie te matchen.
7. `references/besluiten.md` en de regel Navragen volgens 2.6.

### Fase 5 — Beoordelingen en onderwerpen, met AKKOORD (denkniveau hoog; akkoord laag)
1. De 39 rijen uit `besluiten-eerder.yaml` letterlijk naar:
   - de beoordeling van het begrip of de begrippen;
   - het onderwerp, bij een besluit over het onderwerp als geheel (Afbakening Burgerzaken, Onderwerp Algemeen, Indelingsvelden, UPL-producten van lijkbezorging, Afronding Burgerzaken);
   - het onderwerp, bij een begrip zonder beoordeling (Uitdaagrecht, Uniforme openbare voorbereidingsprocedure, Bestuursorgaan, Participatiebeleid).

   Daarna vervalt het register; het script controleert de `besluiten:` van een onderwerp.
2. Element-`grondslag` vervalt, en de toelichting gaat naar `ggm.onderbouwing`. Relatie-`grondslag` wordt `ggm_match` (`bron` → `geen`, `ggm-exact` → `exact`). Bij te werken:
   - het schema en `bepaal_type.py` (`GRONDSLAGEN`, `voor_te_leggen`, `voorgestelde_status`);
   - `render.py` en `archimate_export.py`;
   - `references/grondslag.md`, dat opgaat in `ggm-match.md` en de modelleerregel Wettelijke grondslag.
3. Besluitteksten met een pad noemen de regel of sectie bij naam.
4. De signalen uit fase 2 per soort beoordelen; voorleggen waar een betere modellering mogelijk is.
5. Onderwerpen Kern en de thematische gedeelde onderwerpen aanmaken. De 15 elementen van Algemeen per geval verdelen (voorleggen), en de drie bronanalyses naar Kern. Algemeen vervalt; de regel Thuishoren en `tools/signalen.py` volgen de voorrangsregel.
6. De beoordeling met het GGM als bron en de 27 met het GEMMA-model als bron nakijken.
7. Beslissen en renderen, `llmwiki promote plan`, de redacteur geeft AKKOORD, `promote apply`, export, commit.

## 5. Kritieke bestanden

- **Nieuw:** `tools/kennismodel.py`, `kennismodel/**`, `schemas/kennismodel.schema.json`, `tools/tests/test_gam_kennismodel.py`, `beoordelingen/onderwerpen/{kern,besluitvorming,…}.yaml`
- **Hernoemd:** `tools/afleiden.py` → `tools/beslissen.py`
- **Bijwerken:** `tools/{bepaal_type,relaties,signalen,render,archimate_export}.py`, `wiki.yaml`, `schemas/beoordeling.schema.json`, `sources/index/2026-vng-ggm-2-5-1.md`; gedeeld: `tools/llmwiki/{akkoord,beoordeling}.py`, `wikis/_template*/wiki.yaml`
- **Tekst:** `ARCHITECTURE.md`, `AGENTS.md`, de skills (criteria, beoordelen met references, update, ingest, archimate-export), `todo.md`, `bronanalyses/algemeen/overig/*.md`
- **Weg:** `docs/`, `besluiten/`, `beoordelingen/besluiten-eerder.yaml`, `references/grondslag.md`, `beoordelingen/onderwerpen/algemeen.yaml`

## 6. Verificatie

- `uv run pytest` (repository en wiki) groen, met de nieuwe tests voor het kennismodel.
- `kennismodel/` gelijk aan de bron (check in de pre-commit); elk elementtype heeft modelleerafspraken; geen aantallen.
- Beslissen en renderen zonder fouten; `render.py --check`, `llmwiki lint`, `goedgekeurd-guard` en `log-alleen-aanvullen` ok.
- Export:
  - in Archi het kennismodel van de wiki met alle elementtypen, de toegestane relaties, de eigenschappen kernrelatie en *in Over GEMMA*, en de Grondslagindeling;
  - de groeperingen houden hun id's;
  - het rapport noemt wat wegvalt;
  - `--check` ok.
- Na fase 5 geeft `grep -rn "docs/\|besluit redacteur\|besluiten redacteur\|Regelgevingindeling\|afgeleid:\|grondslag: \(bron\|ggm\|regelgeving\|procesobject\)" AGENTS.md ARCHITECTURE.md kennismodel .agents beoordelingen tools` geen treffers, en heeft elke inhoudelijk gewijzigde beoordeling een AKKOORD.

## 7. Volgende stap

Fase 0 voer ik nog in deze sessie uit. Begin daarna in een nieuwe sessie (deze is vol). Fase 1 en 4 vragen denkniveau hoog, fase 2 en 3 middel, het AKKOORD in fase 5 laag. Startprompt:

```
Werk in wikis/gemma-archimate-model, op main na de commit van fase 0. Voer het plan in wikis/gemma-archimate-model/plannen/2026-10-09-kennismodel.md uit vanaf fase 1 ("het kennismodel van gemma-archimate-model"), fase voor fase, met een commit per fase. Uitgangspunten van de redacteur: herleidbaarheid geldt voor het model, niet voor regels, skills en documentatie; consistentie en overzicht gaan voor het vermijden van herbeoordeling; ARCHITECTURE.md is leidend en vervangt docs/; regels die de modellering raken staan in kennismodel/, AGENTS.md alleen de werkwijze; het kennismodel is metadata (geen aantallen); GGM en GEMMA-model zijn matchdoel, de UPL is bron én matchdoel; beoordelingen leggen de gevonden relaties vast, de export filtert op het kennismodel. Twijfelgevallen één voor één voorleggen, in eenvoudige taal met per optie wat er gebeurt.
```
