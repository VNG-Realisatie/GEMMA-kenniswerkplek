# Architectuur van de wiki gemma-archimate-model

Deze wiki bouwt het GEMMA-architectuurmodel voor de bedrijfslaag onderbouwd opnieuw op: bedrijfsobjecten, contracten, producten, diensten, processen, functies, gebeurtenissen, actoren en rollen. Elk element is herleidbaar tot bronnen, gematcht op het GGM en op het huidige GEMMA-model, en pas na akkoord van een redacteur vastgesteld. Het is een wiki van het type `curation` (zie de `ARCHITECTURE.md` van de repository voor de algemene opzet). De regels staan in [AGENTS.md](AGENTS.md); dit document legt uit hoe alles samenhangt.

## 1. Plaats in de keten

```text
wetten, informatiemodellen, beleid (sources/)  ─┐
GGM-XMI (sources/, via tools/ggm.py)           ─┼─►  deze wiki  ─►  (later) export naar het GEMMA-model / GEMMA Online
GEMMA-model AMEFF (sources/, tools/gemma.py)    ┘
```

Het GGM is zowel bron (kandidaat-begrippen, definities, relaties) als toets. Het GEMMA-model is alleen matchdoel: het laat zien hoe een element nu in GEMMA staat. Terugschrijven naar GEMMA is nog niet gebouwd (advies: een deel-`.archimate` met behoud van id's, zie skill `gemma-archimate-model-gemma-release`).

## 2. Plattegrond

```text
wikis/gemma-archimate-model/
├── AGENTS.md · ARCHITECTURE.md · wiki.yaml
├── begrippen/<onderwerp>.md                 begrippenlijst per onderwerp — ingang van een run
├── bronanalyses/<onderwerp>/<bron-id>.md    wat een bron betekent voor de architectuur
├── bedrijfsarchitectuur/
│   ├── bedrijfsobjecten/<taakveld>/<beleidsdomein>/   business-object en contract
│   ├── producten/ · diensten/ · bedrijfsprocessen/ · bedrijfsfuncties/   (<taakveld>/<beleidsdomein>/)
│   └── gebeurtenissen/ · actoren/ · rollen/ · bedrijfssamenwerkingen/ · kanalen/   plat
├── motivatie/beleidskaders/                beleidskaders (Driver): rijks- of EU-regelgeving en VNG-modelverordeningen
├── (later) applicatiearchitectuur/          o.a. data-objecten
├── analyses/ggm-terugmeldingen.md           doorlopende lijst met terugmeldingen aan het GGM
├── analyses/beslistabel.md                  kenmerken en beslistabel, gegenereerd uit tools/bepaal_type.py
├── ggm/ · gemma/                            gegenereerd door de tools; nooit met de hand bewerken
├── schemas/                                 één JSON-schema per paginatype
├── tools/                                   Python-gereedschap van deze wiki (met tests in tools/tests/)
└── .agents/skills/                          vaardigheden van deze wiki
```

Mapnamen van taakveld en beleidsdomein: kleine letters met koppeltekens (`8 Volkshuisvesting` → `8-volkshuisvesting`).

## 3. Paginatypen en velden

| Paginatype | Map | Schema | Gecureerd |
|---|---|---|---|
| `onderwerp` | `begrippen/` | [schemas/onderwerp.schema.json](schemas/onderwerp.schema.json) | nee |
| `bronanalyse` | `bronanalyses/<onderwerp>/` | [schemas/bronanalyse.schema.json](schemas/bronanalyse.schema.json) | nee |
| `analyse` | `analyses/` | [schemas/analyse.schema.json](schemas/analyse.schema.json) | nee |
| `bedrijfsobject`, `product`, `dienst`, `bedrijfsproces`, `bedrijfsfunctie`, `gebeurtenis`, `actor`, `rol`, `bedrijfssamenwerking`, `kanaal` | `bedrijfsarchitectuur/…` | `schemas/<type>.schema.json`, gedeelde velden in [schemas/element-basis.schema.json](schemas/element-basis.schema.json) | ja |
| `beleidskader` | `motivatie/beleidskaders/` | [schemas/beleidskader.schema.json](schemas/beleidskader.schema.json), gedeelde velden in element-basis | ja |

Veldprefixen op een elementpagina ([EL12]):

| Prefix | Betekenis | Wie vult |
|---|---|---|
| geen | Eigen veld van de wiki, algemeen ArchiMate (`naam`, `definitie`, `definitie_formeel`, `toelichting`, `synoniemen`, `grondslag`, `match`, `data_object`, `kenmerken` …) | model |
| `ggm_` | Letterlijk uit het GGM | alleen `tools/ggm.py` |
| `gemma_` | Letterlijk uit het GEMMA-model, na een match | alleen `tools/gemma.py` |

In de frontmatter staan geen verwijzingen naar andere pagina's ([EL17]). Alle verwijzingen tussen pagina's zijn relatieve Markdown-links in de body; Obsidian toont zo de omgekeerde kant als backlink. De vaste tabellen (relaties, specialisaties, begrippen, terugmeldingen) leest de tool uit de body.

## 4. Herleidbaarheid

```text
sources/raw (origineel) → sources/index (intake) → bronanalyses/<onderwerp>/<bron-id>.md
    → begrippen/<onderwerp>.md (begrippentabel met uitkomst per begrip) → elementpagina (bronnen:, ## Bronnen)
    bronanalyse ## Relaties (werkwoord + vindplaats) → relatierij op de elementpagina (kolom Bron)
```

`tools/check_elementen.py` eist dat elke bron van een element een bronanalyse heeft (behalve de modelbronnen GGM en GEMMA), dat elke bronanalyse in de bronnenlijst van haar onderwerp staat, en dat elk element in een begrippenlijst voorkomt.

## 5. Werkstroom

Skill [gemma-archimate-model-update](.agents/skills/gemma-archimate-model-update/SKILL.md) volgt de gedeelde `wiki-update` en voegt per fase toe:

| Fase | Skill | Gereedschap | Resultaat |
|---|---|---|---|
| INGEST | [gemma-archimate-model-ingest](.agents/skills/gemma-archimate-model-ingest/SKILL.md) | `llmwiki source add` (ook `--url`, pdf, `--brontype`) | bronanalyse (begrippen en relaties), bron in de begrippenlijst |
| ASSESS | [gemma-archimate-model-assess](.agents/skills/gemma-archimate-model-assess/SKILL.md) + [criteria](.agents/skills/gemma-archimate-model-criteria/SKILL.md) | `tools/bepaal_type.py`, `tools/relaties.py uit-bronnen`, `tools/ggm.py`, `tools/gemma.py` | beoordeling per begrip, relaties uit de bronnen |
| WRITE | [gemma-archimate-model-write](.agents/skills/gemma-archimate-model-write/SKILL.md) | `tools/ggm.py`, `tools/gemma.py`, `tools/relaties.py`, `tools/terugmelding.py` | gestagede pagina's |
| VALIDATE | `wiki-validate` | `llmwiki validate --run`, `tools/check_elementen.py` | validatierapport |
| GATE + PROMOTE | `wiki-publish` | `llmwiki promote plan/apply` | goedgekeurde pagina's, `log.md` |

Nieuwe modelversies: [gemma-archimate-model-ggm-release](.agents/skills/gemma-archimate-model-ggm-release/SKILL.md) en [gemma-archimate-model-gemma-release](.agents/skills/gemma-archimate-model-gemma-release/SKILL.md).

## 6. Criteria: is een begrip een element, en welk?

Eén plek: skill [gemma-archimate-model-criteria](.agents/skills/gemma-archimate-model-criteria/SKILL.md), met de code in [tools/bepaal_type.py](tools/bepaal_type.py).

- **Kenmerken** zijn neutrale eigenschappen van een begrip (bijv. *onderscheidbare exemplaren*). Het model beantwoordt ze allemaal, één keer, met onderbouwing en bron-id's.
- **Criteria** zijn de regels van de beslistabel: welke combinatie van kenmerken tot welk type leidt. De tool past ze toe; het type is dus een uitkomst, geen keuze vooraf.
- De beslistabel heeft zeven stappen: welk begrip (synoniem of homoniem), scope (*herkenbaar*, *gemeentelijk*, *buiten dit model*), afhankelijkheid (eigenschap, onderdeel, ander onderwerp), consistentie (kenmerken passen bij de aard), type (de aard bepaalt het voorlopige type), een **drempel** per type (een kernrelatie die ja moet zijn, en van de overige drempelcriteria hoogstens één nee) en de **zelfstandige specialisatie**. Criteria van 2026-10-01; de onderbouwing staat in `analyses/kenmerken.md`, `analyses/gemma-kennismodel.md`, `analyses/gegevensrollen.md` en `analyses/synoniemen-en-homoniemen.md`.
- De documentatie (vragenlijst, naslag, per type, matrix en in de skill ook de stappentabel) in de skill en in [analyses/beslistabel.md](analyses/beslistabel.md), en het schema [schemas/beoordeling.schema.json](schemas/beoordeling.schema.json), worden uit de code gegenereerd; een test bewaakt dat ze gelijk blijven.
- Elementpagina's met de kenmerken van 2026-09-30 blijven geldig tot de herbeoordeling; de controle meldt ze als "herbeoordeling nodig".
- Interaction wordt herkend, maar heeft geen paginatype: zo'n begrip wordt voorgelegd. Representation en Location zijn een vaste uitkomst zonder pagina. Van de motivatielaag zit alleen het beleidskader in dit model; de rest van de motivatie- en strategielaag valt erbuiten.

## 7. Bronvoorrang en definities

- Brontype per bron (in de intake): `wet`, `informatiemodel`, `beleid`, `overig`, `model`. De leesvolgorde staat in `wiki.yaml` (`bronvoorrang`); `llmwiki run start --onderwerp` houdt haar aan. `model` (het GEMMA-model) is een matchdoel en valt buiten de volgorde.
- Wet en informatiemodel bepalen welke begrippen er zijn en wat ze formeel betekenen; beleid levert de gangbare taal. Voorrang bepaalt niet of iets een element is ([SRC10]).
- Uitzondering: de naam en de herkenbare `definitie` komen uit de gangbare taal van beleids- en praktijkbronnen; de wetsterm wordt een synoniem met context "wet" (bijv. *Urn*, met *asbus* als wetsterm). Zie [references/naamgeving.md](.agents/skills/gemma-archimate-model-write/references/naamgeving.md).
- De definitie van een actor of rol beschrijft de partij of de verantwoordelijkheid zelf, los van het onderwerp; wat de partij in het onderwerp doet, staat in `## Relaties`.
- `definitie` is de herkenbare definitie (altijd, ≤160 tekens, gaat naar GEMMA). `definitie_formeel` staat er alleen bij een wezenlijk verschil: als onder beide definities niet precies dezelfde exemplaren vallen. Een formele definitie uit het GGM staat al in `ggm_definitie` en wordt niet gekopieerd. Zie [references/definitie.md](.agents/skills/gemma-archimate-model-write/references/definitie.md).

## 8. Relaties

Elementen en relaties worden samen gevonden, in dezelfde fasen en uit dezelfde bronnen. Een relatie wordt pas een ArchiMate-relatie als van beide kanten vaststaat wat voor element het is; de relatie volgt dus de beoordeling van de begrippen.

| Fase | Elementen | Relaties |
|---|---|---|
| INGEST | De bronanalyse noemt de kernbegrippen (`## Kernbegrippen`) | De bronanalyse noemt de relaties tussen die begrippen zoals de bron ze formuleert: van, werkwoord, naar, vindplaats (`## Relaties`) |
| ASSESS | Kenmerken → beslistabel → type per begrip | De relaties uit de bronanalyses gaan mee in de voorstellen (`relaties`). `tools/relaties.py uit-bronnen` lost beide kanten op via de uitkomst van de beslistabel: element → relatie; eigenschap of specialisatie zonder pagina → opgetild naar het genoemde begrip; geen element → relatie vervalt (met reden). Het werkwoord en de typen van beide kanten bepalen de ArchiMate-relatie |
| WRITE | Elementpagina's, GGM-match | `tools/relaties.py voorstel <id> --bronnen <assessment.json>` voegt de relaties uit de bronnen samen met de kandidaten uit het GGM en geeft de rijen voor `## Relaties` |
| VALIDATE | Schema's, kenmerken ↔ type | Relatietabel, ArchiMate-toets, GGM-relatie past bij de uiteinden, elke bron-id heeft een bronanalyse |

**Opslag.** Een relatie staat één keer, als rij in `## Relaties` op de pagina van het bronelement, met een relatieve link naar het doel; Obsidian toont de andere kant als backlink. Kolommen: `Relatie`, `Naar`, `Naam`, `Kardinaliteit`, `Grondslag`, `GGM-relatie`, `Bron` (bron-id's met vindplaats).

**Grondslag.** `ggm-exact` (één GGM-relatie tussen de gematchte entiteiten), `ggm-afgeleid` (opgetild of via een keten) of `bron` (alleen uit de bronnen; bron-id verplicht). Een relatie uit een bron tussen dezelfde elementen als een GGM-relatie bevestigt die: de bron-id komt erbij en de grondslag blijft `ggm-*`; noemt de bron een ander relatietype, dan staat dat in de toelichting. Bij tegenspraak wint de hoger gerangschikte bron (wet boven GGM); beleid levert de herkenbare naam.

**Uit de bronnen naar ArchiMate** (`van_bron` in [tools/relaties.py](tools/relaties.py)): de typen van beide elementen bepalen de soort relatie (partij → gedrag: toewijzing; tussen partijen alleen actor → rol bij "vervult" of "treedt op als", anders een gerichte associatie; gedrag ↔ object: toegang, met lezen of schrijven uit het werkwoord; gebeurtenis ↔ gedrag: triggering; gedrag → dienst: realisatie; dienst → partij of gedrag: bediening), het werkwoord bepaalt richting, deel-geheel ("bestaat uit", "maakt deel uit van") en specialisatie ("is een"). Wat niet in de ArchiMate-tabel past, wordt een gerichte associatie. Een begrip dat verhuist (uitkomst element, doel de begrippenlijst) krijgt in die run geen pagina; relaties ernaartoe vervallen met die reden. De uitkomst is een voorstel; het model controleert richting en betekenis.

**Uit het GGM** ([tools/relaties.py](tools/relaties.py) `voorstel`): specialisaties zonder pagina en GGM-componenten worden opgetild; ketens via niet-opgenomen entiteiten krijgen het zwakste type (compositie > aggregatie > associatie) en een samengestelde kardinaliteit; relaties naar enumeraties vervallen. Mapping: Generalization → specialisatie; Aggregation (composite/shared) → compositie/aggregatie, alleen bij een deel-geheel-naam, anders een gerichte associatie met terugmeldkandidaat; Association en Usage → associatie.

**Terugmelden** alleen bij `ggm-exact` (fout type, richting, kardinaliteit, naam, dubbel); nieuwe relaties uit de bronnen en afgeleide relaties niet. De groepering op beleidsdomein (in GEMMA een aggregatie vanuit een Grouping) wordt afgeleid uit `taakveld`/`beleidsdomein` en niet als relatie vastgelegd. Elke rij wordt getoetst aan een deelverzameling van de ArchiMate-relatietabel. Werkwijze in detail: [references/relaties.md](.agents/skills/gemma-archimate-model-write/references/relaties.md).

**Aandachtspunt:** in het GGM-export zijn de richting van deel-geheel en de multipliciteiten niet altijd eenduidig. De tool volgt de EA-conventie (het uiteinde met het ruitje is het geheel); de namen ("bevat", "leidt tot") bevestigen dat meestal, maar de multipliciteiten lijken vaak omgedraaid. Controleer ze bij gebruik.

## 9. GGM en GEMMA als bron

| | GGM | GEMMA-model |
|---|---|---|
| Bronbestand | XMI 2.1 (Enterprise Architect) | ArchiMate Open Exchange (AMEFF); een Archi-bronbestand `.archimate` kan ook |
| Herkomst | GitHub `Gemeente-Delft/Gemeentelijk-Gegevensmodel`, `wiki.yaml` → `ggm.herkomst` (repository, ref, pad) | GitHub `VNG-Realisatie/GEMMA-Archi-repository`, `export/GEMMA release.xml`, `wiki.yaml` → `gemma.herkomst` |
| Tool | [tools/ggm.py](tools/ggm.py) | [tools/gemma.py](tools/gemma.py) |
| Gegenereerd | `ggm/ggm_parsed.json`, `ggm/<taakveld>/<beleidsdomein>.md` | `gemma/gemma_parsed.json`, `gemma/overzicht.md` |
| Veldblok | `ggm.py velden <guid>` → `ggm_*` | `gemma.py velden <id>` → `gemma_*` |
| Match | `zoek`, `naamgenoten`, `generalisaties`, `attribuut`, `relaties` | `koppel <ggm-guid>`, `zoek`, `groepering` |
| Nieuwe versie | `release --id <bron-id> [--ref <branch/tag>]` + `verrijk --run` | `release --id <bron-id> [--ref <branch/tag>]` + `verrijk --run` |

Gegenereerde bestanden hebben een hash-kop; `tools/check_elementen.py` meldt een handmatige wijziging ([SRC5]).

## 10. Status, gate en autonomie

- De AI zet een element op `review` alleen als de beslistabel geen conflict en geen "voorleggen" geeft. Daarnaast moet een element met `data_object: ja` een GGM-match exact of sterk hebben, en een `governance-object` wordt altijd voorgelegd. Anders krijgt het element status `kandidaat`, met een sectie `## Ter discussie` ([EL18]).
- `llmwiki promote apply` keurt na akkoord (smaak A: document) alleen `review`-pagina's goed; een `kandidaat` wordt geschreven zoals hij is, zonder logregel.
- Een goedgekeurde pagina die opnieuw wordt gestaged (bijv. door een modelrelease), gaat terug naar `review`.

## 11. Controles

[tools/check_elementen.py](tools/check_elementen.py) is het uitbreidingspunt van VALIDATE. Het geeft een **fout** bij:

| Groep | Controles |
|---|---|
| Plaats en schema | map, uniek id, kenmerken ↔ type, `data_object` |
| Status | status ↔ autonomie, `## Ter discussie` |
| Definities | regels voor de formele definitie |
| Modelvelden | `ggm_*`/`gemma_*` gelijk aan het model |
| Links en bronnen | verwijzingen in de frontmatter, herleidbaarheid |
| Relaties | relatietabel en ArchiMate-toets, GGM-relatie past bij de uiteinden, bron-id heeft een bronanalyse |
| Hiërarchie en tegenhangers | specialisaties met en zonder pagina, wederzijdse tegenhanger |
| Pagina's en bestanden | technische verwijzingen, begrippenlijst en bronanalyse, gegenereerde bestanden |

Een **waarschuwing** geeft het bij registr*-taal, absolute taal, meer dan één zin in de definitie, een ontbrekende tegenhanger, niet-wederzijdse homoniemen en een afwijkende GEMMA-groepering. Waarschuwingen beoordeelt het model inhoudelijk.

## 12. Regels

De regels staan met een id in [AGENTS.md](AGENTS.md):
- **PR**: werkwijze;
- **IH**: inhoud en herleidbaarheid;
- **SRC**: bronnen en modellen;
- **EL**: elementen (de vroegere groep BO, nu algemeen ArchiMate);
- **WC**: scope en formulering.

Regels die een tool afdwingt, staan in AGENTS.md als korte regel. De uitvoering staat in de tool of de skill.

## 13. Nog niet gebouwd

- Dekkingsanalyse van het GGM (entiteitendekking) en de export naar CSV of `.archimate`.
- Inhoudelijke audits (definities, duplicaten, werkvoorraad).
- Het hernoemen van elementen met automatisch bijwerken van alle links.
- Paginatypen voor Collaboration, Interface, Interaction, Location en Representation, en `applicatiearchitectuur/`.
- Het tonen van de formele definitie op GEMMA Online.
