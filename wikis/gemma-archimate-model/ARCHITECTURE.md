# Architectuur van de wiki gemma-archimate-model

Deze wiki bouwt het GEMMA-architectuurmodel voor de bedrijfslaag onderbouwd opnieuw op: bedrijfsobjecten,
contracten, producten, diensten, processen, functies, gebeurtenissen, actoren en rollen. Elk element is
herleidbaar tot bronnen, gematcht op het GGM en op het huidige GEMMA-model, en pas na akkoord van een redacteur
vastgesteld. Het is een wiki van het type `curation` (zie de `ARCHITECTURE.md` van de repository voor de
algemene opzet). De regels staan in [AGENTS.md](AGENTS.md); dit document legt uit hoe alles samenhangt.

## 1. Plaats in de keten

```text
wetten, informatiemodellen, beleid (sources/)  ─┐
GGM-XMI (sources/, via tools/ggm.py)           ─┼─►  deze wiki  ─►  (later) export naar het GEMMA-model / GEMMA Online
GEMMA-model .archimate (sources/, tools/gemma.py)┘
```

Het GGM is zowel bron (kandidaat-begrippen, definities, relaties) als toets. Het GEMMA-model is alleen
matchdoel: het laat zien hoe een element nu in GEMMA staat. Terugschrijven naar GEMMA is nog niet gebouwd
(advies: een deel-`.archimate` met behoud van id's, zie skill `gemma-archimate-model-gemma-release`).

## 2. Plattegrond

```text
wikis/gemma-archimate-model/
├── AGENTS.md · ARCHITECTURE.md · wiki.yaml
├── begrippen/<onderwerp>.md                 begrippenlijst per onderwerp — ingang van een run
├── bronanalyses/<onderwerp>/<bron-id>.md    wat een bron betekent voor de architectuur
├── bedrijfsarchitectuur/
│   ├── bedrijfsobjecten/<taakveld>/<beleidsdomein>/   business-object en contract
│   ├── producten/ · bedrijfsdiensten/ · bedrijfsprocessen/ · bedrijfsfuncties/   (<taakveld>/<beleidsdomein>/)
│   └── bedrijfsgebeurtenissen/ · actoren/ · rollen/   plat
├── (later) applicatiearchitectuur/          o.a. data-objecten
├── analyses/ggm-terugmeldingen.md           doorlopende lijst met terugmeldingen aan het GGM
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
| `bedrijfsobject`, `product`, `bedrijfsdienst`, `bedrijfsproces`, `bedrijfsfunctie`, `bedrijfsgebeurtenis`, `actor`, `rol` | `bedrijfsarchitectuur/…` | `schemas/<type>.schema.json`, gedeelde velden in [schemas/element-basis.schema.json](schemas/element-basis.schema.json) | ja |

Veldprefixen op een elementpagina ([EL12]):

| Prefix | Betekenis | Wie vult |
|---|---|---|
| geen | Eigen veld van de wiki, algemeen ArchiMate (`naam`, `definitie`, `definitie_formeel`, `toelichting`, `synoniemen`, `grondslag`, `match`, `data_object`, `kenmerken` …) | model |
| `ggm_` | Letterlijk uit het GGM | alleen `tools/ggm.py` |
| `gemma_` | Letterlijk uit het GEMMA-model, na een match | alleen `tools/gemma.py` |

In de frontmatter staan geen verwijzingen naar andere pagina's ([EL17]). Alle verwijzingen tussen pagina's
zijn relatieve Markdown-links in de body; Obsidian toont zo de omgekeerde kant als backlink. De vaste tabellen
(relaties, specialisaties, begrippen, terugmeldingen) leest de tool uit de body.

## 4. Herleidbaarheid

```text
sources/raw (origineel) → sources/index (intake) → bronanalyses/<onderwerp>/<bron-id>.md
    → begrippen/<onderwerp>.md (begrippentabel met uitkomst per begrip) → elementpagina (bronnen:, ## Bronnen)
```

`tools/check_elementen.py` eist dat elke bron van een element een bronanalyse heeft (behalve de modelbronnen
GGM en GEMMA), dat elke bronanalyse in de bronnenlijst van haar onderwerp staat, en dat elk element in een
begrippenlijst voorkomt.

## 5. Werkstroom

Skill [gemma-archimate-model-update](.agents/skills/gemma-archimate-model-update/SKILL.md) volgt de gedeelde
`wiki-update` en voegt per fase toe:

| Fase | Skill | Gereedschap | Resultaat |
|---|---|---|---|
| INGEST | [gemma-archimate-model-ingest](.agents/skills/gemma-archimate-model-ingest/SKILL.md) | `llmwiki source add` (ook `--url`, pdf, `--brontype`) | bronanalyse, bron in de begrippenlijst |
| ASSESS | [gemma-archimate-model-assess](.agents/skills/gemma-archimate-model-assess/SKILL.md) + [criteria](.agents/skills/gemma-archimate-model-criteria/SKILL.md) | `tools/bepaal_type.py`, `tools/ggm.py`, `tools/gemma.py` | beoordeling per begrip |
| WRITE | [gemma-archimate-model-write](.agents/skills/gemma-archimate-model-write/SKILL.md) | `tools/ggm.py`, `tools/gemma.py`, `tools/relaties.py`, `tools/terugmelding.py` | gestagede pagina's |
| VALIDATE | `wiki-validate` | `llmwiki validate --run`, `tools/check_elementen.py` | validatierapport |
| GATE + PROMOTE | `wiki-publish` | `llmwiki promote plan/apply` | goedgekeurde pagina's, `log.md` |

Nieuwe modelversies: [gemma-archimate-model-ggm-release](.agents/skills/gemma-archimate-model-ggm-release/SKILL.md)
en [gemma-archimate-model-gemma-release](.agents/skills/gemma-archimate-model-gemma-release/SKILL.md).

## 6. Criteria: is een begrip een element, en welk?

Eén plek: skill [gemma-archimate-model-criteria](.agents/skills/gemma-archimate-model-criteria/SKILL.md), met de
code in [tools/bepaal_type.py](tools/bepaal_type.py).

- **Kenmerken** zijn neutrale eigenschappen van een begrip (bijv. *onderscheidbare exemplaren*). Het model
  beantwoordt ze allemaal, één keer, met onderbouwing en bron-id's.
- **Criteria** zijn de regels van de beslistabel: welke combinatie van kenmerken tot welk type leidt. De tool
  past ze toe; het type is dus een uitkomst, geen keuze vooraf.
- De tabellen in de skill en het schema [schemas/beoordeling.schema.json](schemas/beoordeling.schema.json) worden
  uit de code gegenereerd; een test bewaakt dat ze gelijk blijven.
- Collaboration, Interface, Interaction, Location en Representation worden herkend, maar hebben nog geen
  paginatype: zo'n begrip wordt voorgelegd. De motivatie- en strategielaag valt buiten dit model.

## 7. Bronvoorrang en definities

- Brontype per bron (in de intake): `wet`, `informatiemodel`, `beleid`, `overig`, `model`. De leesvolgorde staat in
  `wiki.yaml` (`bronvoorrang`); `llmwiki run start --onderwerp` houdt haar aan. `model` (het GEMMA-model) is een
  matchdoel en valt buiten de volgorde.
- Wet en informatiemodel bepalen welke begrippen er zijn en wat ze formeel betekenen; beleid levert de gangbare
  taal. Voorrang bepaalt niet of iets een element is ([SRC10]).
- `definitie` is de herkenbare definitie (altijd, ≤160 tekens, gaat naar GEMMA). `definitie_formeel` staat er
  alleen bij een wezenlijk verschil: als onder beide definities niet precies dezelfde exemplaren vallen. Een
  formele definitie uit het GGM staat al in `ggm_definitie` en wordt niet gekopieerd. Zie
  [references/definitie.md](.agents/skills/gemma-archimate-model-write/references/definitie.md).

## 8. Relaties

Een relatie staat één keer, als rij in `## Relaties` op de pagina van het bronelement, met een link naar het doel.
[tools/relaties.py](tools/relaties.py) leidt kandidaten af uit het GGM:
- grondslag `ggm-exact`, `ggm-afgeleid` of `bron`;
- specialisaties zonder pagina en GGM-componenten worden opgetild;
- ketens via niet-opgenomen entiteiten krijgen het zwakste type;
- relaties naar enumeraties vervallen.

Mapping van GGM-typen: Generalization → specialisatie; Aggregation (composite/shared) → compositie/aggregatie,
alleen bij een deel-geheel-naam, anders een gerichte associatie met terugmeldkandidaat; Association/Usage → associatie.
Terugmelden alleen bij exacte matches. De groepering op beleidsdomein (in GEMMA een aggregatie vanuit een Grouping)
wordt afgeleid uit `taakveld`/`beleidsdomein` en niet als relatie vastgelegd. Elke rij wordt getoetst aan een
deelverzameling van de ArchiMate-relatietabel. Zie
[references/relaties.md](.agents/skills/gemma-archimate-model-write/references/relaties.md).

**Aandachtspunt:** in het GGM-export zijn de richting van deel-geheel en de multipliciteiten niet altijd
eenduidig. De tool volgt de EA-conventie (het uiteinde met het ruitje is het geheel); de namen ("bevat",
"leidt tot") bevestigen dat meestal, maar de multipliciteiten lijken vaak omgedraaid. Controleer ze bij gebruik.

## 9. GGM en GEMMA als bron

| | GGM | GEMMA-model |
|---|---|---|
| Bronbestand | XMI 2.1 (Enterprise Architect) | Archi-bronbestand `.archimate` |
| Herkomst | GitHub `Gemeente-Delft/Gemeentelijk-Gegevensmodel`, `wiki.yaml` → `ggm.herkomst` (repository, ref, pad) | aangeleverd bestand |
| Tool | [tools/ggm.py](tools/ggm.py) | [tools/gemma.py](tools/gemma.py) |
| Gegenereerd | `ggm/ggm_parsed.json`, `ggm/<taakveld>/<beleidsdomein>.md` | `gemma/gemma_parsed.json`, `gemma/overzicht.md` |
| Veldblok | `ggm.py velden <guid>` → `ggm_*` | `gemma.py velden <id>` → `gemma_*` |
| Match | `zoek`, `naamgenoten`, `generalisaties`, `attribuut`, `relaties` | `koppel <ggm-guid>`, `zoek`, `groepering` |
| Nieuwe versie | `release --id <bron-id> [--ref <branch/tag>]` + `verrijk --run` | `release <bestand> --id <bron-id>` + `verrijk --run` |

Gegenereerde bestanden hebben een hash-kop; `tools/check_elementen.py` meldt een handmatige wijziging ([SRC5]).

## 10. Status, gate en autonomie

- De AI zet een element op `review` alleen als de beslistabel geen conflict en geen "voorleggen" geeft. Daarnaast
  moet een element met `data_object: ja` een GGM-match exact of sterk hebben, en een `governance-object` wordt
  altijd voorgelegd. Anders krijgt het element status `kandidaat`, met een sectie `## Ter discussie` ([EL18]).
- `llmwiki promote apply` keurt na akkoord (smaak A: document) alleen `review`-pagina's goed; een `kandidaat` wordt
  geschreven zoals hij is, zonder logregel.
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
| Relaties | relatietabel en ArchiMate-toets, GGM-relatie past bij de uiteinden |
| Hiërarchie en tegenhangers | specialisaties met en zonder pagina, wederzijdse tegenhanger |
| Pagina's en bestanden | technische verwijzingen, begrippenlijst en bronanalyse, gegenereerde bestanden |

Een **waarschuwing** geeft het bij registr*-taal, absolute taal, meer dan één zin in de definitie, een ontbrekende
tegenhanger, niet-wederzijdse homoniemen en een afwijkende GEMMA-groepering. Waarschuwingen beoordeelt het model
inhoudelijk.

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
