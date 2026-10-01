# Architectuur-Kompas

Dit is de korte uitleg van hoe deze repository werkt. Voor wie een nieuwe wiki inricht: `docs/kluswijzer.md`. Voor de redenen achter elke keuze, met bronnen: `docs/onderbouwing.md`.

## 1. Wat is een LLM-wiki?

Een LLM-wiki is een verzameling kennispagina's die we samen met een AI-assistent bijhouden. Bij elke wiki horen pagina's, een eigen kijk op de gedeelde bronnen, huisregels (Rules), vaardigheden (Skills), werkstromen (Workflows) en gereedschap (Tools). Wat voor elke wiki geldt, staat één keer in de gedeelde laag; wat voor één wiki geldt, in de map van die wiki.

### Soorten wiki's

Drie soorten, benoemd naar hun doel:

| Soort (`wiki.yaml` `type:`) | Doel | Waar staat de waarheid | Laatste stap |
|---|---|---|---|
| `sync` | Een MediaWiki-site beheren, bijvoorbeeld GEMMA Online | Op de site | Publiceren na akkoord (git-diff-review) |
| `curation` | Gestructureerde kennis opbouwen, optioneel tot een export (ArchiMate, UML/XMI, CSV, MediaWiki) | In de repository: het oordeel van de AI in beoordelingen, pagina's gegenereerd door scripts | Goedkeuren met AKKOORD in de chat (`kandidaat` → `review` → `goedgekeurd`), en met een ingevuld `exports:`-blok: daarna exporteren per doel |
| `knowledge-base` | Ongestructureerde kennis opbouwen: notities, adviezen, ontwerpen, architectuurdocumenten — eigen eindresultaten | In de repository | Geen — review via een gewone `git diff`/commit |

De soorten vormen samen een keten. Wat de ene wiki oplevert, wordt een bron voor de volgende:

```text
Beleidskader (curation) → Begrippen & ArchiMate (curation + exports) → Informatiemodellen (curation + exports) → GEMMA Online (sync)
```

### Gereedschap bij een sync-wiki

Een sync-wiki gebruikt twee soorten toegang tot de externe site, elk voor een ander moment:

| Gereedschap | Wanneer | Wat |
|---|---|---|
| MCP (`mediawiki`) | Tijdens het bewerken: verkennen, opzoeken, een pagina lezen | Alleen-lezen, interactief vanuit de AI-omgeving, wijst altijd naar het hoofddoel (nooit een testomgeving) |
| `llmwiki pull` / `llmwiki publish` (pywikibot) | Vóór het bewerken (ophalen naar `content/`) en ná akkoord (schrijven) | Enige weg naar schrijven; nooit via MCP, altijd na de publicatiegate |

Achtergrond en het volledige ontwerp: `docs/onderbouwing.md` 5.10.

### Bronnen: drie lagen

Alle bronnen staan één keer centraal in de repository en worden door alle wiki's gedeeld.

| Laag | Plaats | Wat | Voor wie |
|---|---|---|---|
| 1. Origineel | `sources/raw/` | Het document (pdf, docx) en een Markdown-versie met dezelfde naam. Wordt nooit gewijzigd | Alle wiki's |
| 2. Technische index | `sources/index/<bron>.md` | Gegevens, korte samenvatting, trefwoorden, begrippen en een inhoudsopgave met regelnummers. Alleen voor de AI, om context te sparen (skill `wiki-intake`) | Alle wiki's |
| 3. Domein-lens | `wikis/<wiki>/<map>/<onderwerp>/<bron>.md` (de map staat in `wiki.yaml`, bijv. `bronnen/` of `bronanalyses/`) | Wat deze bron betekent voor dit domein, met uittreksels, en onder de titel links naar laag 1 | Eén wiki |

**Herleidbaarheid loopt via links, van pagina naar brontekst:** pagina → domein-lens → laag 1. Elke verwijzing naar een bron op een pagina is een link naar de domein-lens van die bron, ook in tabellen; de domein-lens linkt naar de tekst, het origineel en de online bron. De technische index zit niet in deze keten: een pagina linkt nooit naar laag 2.

Zo voorkomen we dat een wiki verzuipt in alle bronnen:
- **Filter per wiki.** In `wiki.yaml` staat welke thema's (tags) een wiki gebruikt. Andere bronnen ziet de AI voor die wiki niet.
- **Werk vanuit een onderwerp.** Elke taak begint bij een onderwerppagina (`onderwerpen/<thema>.md`). Die pagina noemt de bronnen die ertoe doen; alleen die leest de AI.
- **Eerst de index, dan de passage.** De AI leest eerst de technische index en daarna alleen de passages uit laag 1 die ertoe doen, op regelnummer.

## 2. Principes

1. **De mens beslist.** De AI bereidt voor. Publiceren of exporteren gebeurt alleen na een bewuste handeling van een redacteur.
2. **Herleidbaar van bron tot begrip.** Voor elke wijziging is terug te vinden welke bron is gelezen, welk voorstel is gedaan en wie het heeft goedgekeurd.
3. **Eén keer vastleggen.** Gedeelde werkwijzen staan op één plek. Een wiki vult ze aan, maar kopieert ze niet.
4. **Werkt in elke AI-omgeving.** Dezelfde wiki werkt in Claude Code, OpenCode, VS Code/Copilot, Cursor en Codex, op Windows, Linux en macOS. Daarvoor gebruiken we open standaarden (AGENTS.md, Agent Skills, MCP).
5. **Kladblok is geen archief.** Tussenstappen van de AI blijven onzichtbaar en worden opgeruimd. Alleen afgeronde, betekenisvolle verslagen komen in de officiële historie.
6. **Wat vast kan, staat in code.** Ophalen, controleren, vergelijken en publiceren doet een programma, niet de AI.
7. **Niets toevoegen zonder reden.** Een extra bestand, laag of instelling komt er alleen als het een concreet probleem oplost.

## 3. Plattegrond

De hele repository is één Obsidian-vault, zodat links naar de gedeelde bronnen overal werken.

```text
llm-wikis/                    open deze map in Obsidian
├── AGENTS.md                 huisregels voor de hele repository
├── ARCHITECTURE.md           dit kompas
├── docs/                     kluswijzer en onderbouwing
├── sources/
│   ├── raw/                  originelen + Markdown-versie   (nooit wijzigen)
│   └── index/                één intakepagina per bron
├── .agents/skills/           gedeelde vaardigheden en de gedeelde werkstroom
├── tools/llmwiki/              gereedschap
└── wikis/
    ├── gemma/                type sync: GEMMA Online, kale werkkopie
    │   ├── AGENTS.md · wiki.yaml
    │   ├── content/          de MediaWiki-pagina's, directe werkkopie
    │   ├── revisies.json     conflictbasis: titel → laatst bekende revisie
    │   ├── log.md            logboek: wie publiceerde wat, wanneer (alleen aanvullen)
    │   └── voorstellen/      publicatievoorstellen ter beoordeling
    ├── gemma-kennis/         type knowledge-base: notities/adviezen/ontwerpen
    │   ├── AGENTS.md · wiki.yaml
    │   └── <onderwerp>/<document>.md
    ├── opzet2/               type curation (met of zonder exports:)
    │   ├── AGENTS.md · wiki.yaml
    │   ├── onderwerpen/      ingang voor elke taak
    │   ├── bronnen/<onderwerp>/
    │   ├── kandidaten/       voorgestelde begrippen met status
    │   ├── export/           goedgekeurde exports (alleen met exports:-blok)
    │   ├── log.md            logboek: wie keurde wat goed   (alleen aanvullen)
    │   ├── voortgang.md      overzicht van open werk        (automatisch)
    │   └── voorstellen/
    └── gemma-archimate-model/  type curation met beoordelingen en gegenereerde pagina's (eigen ARCHITECTURE.md)
```

De mapnamen van een curatie-wiki (`onderwerpen/`, `bronnen/`, `kandidaten/`) zijn standaardwaarden; een wiki kan eigen namen kiezen in `wiki.yaml` (`page_types.<type>.dir`).

Links tussen pagina's zijn gewone relatieve Markdown-links; ze werken in Obsidian en in VS Code. Mappen die met een punt beginnen (`.agents`, `.work`, `.claude` enzovoort) zijn voor de AI-omgevingen; `.work/` is het kladblok van de AI en staat niet in Git.

## 4. Hoe een update verloopt

### Voorbeeld: een pagina bijwerken op GEMMA Online (sync)

De redacteur vraagt: *"Werk de pagina Zaakgericht werken bij met deze wijziging, met wiki-sync-edit."*

| Stap | Wat gebeurt er | Wie |
|---|---|---|
| PULL | Pagina ophalen naar `content/` (of al lokaal aanwezig) | Gereedschap, via pywikibot |
| BEWERK | `content/`-bestand direct aanpassen | AI |
| VALIDATE | Controle op vorm, links | Gereedschap en AI |
| PLAN | Voorstel met git-diff, gebaseerd op de actuele revisie op de site | Gereedschap |
| Akkoord | Beoordelen van het publicatievoorstel en akkoord geven | Redacteur |
| PUBLISH | Publiceren naar de wiki en een regel in `log.md` | Gereedschap, na goedkeuring |

Een tussentijdse wijziging van diezelfde pagina op de site (door iemand anders) wordt bij PUBLISH herkend en geweigerd — niet stilzwijgend overschreven.

### Voorbeeld: een onderwerp bijwerken in een curatie-wiki

De redacteur vraagt: *"Verwerk deze nota voor onderwerp lijkbezorging."* De wiki-workflow volgt `wiki-curatie-update`. Uitgangspunt: **zacht oordeel, harde vorm**. De AI geeft het oordeel per begrip; scripts van de wiki leiden af wat vast kan en maken alle pagina's; de redacteur beoordeelt de pagina's.

| Stap | Wat gebeurt er | Wie |
|---|---|---|
| Bronnen | Origineel en Markdown-versie in `sources/raw/`, intake in `sources/index/`, domein-lens (bronanalyse) in de wiki | Gereedschap en AI |
| Beoordelen | Per begrip een beoordeling (YAML): kenmerken met bron, naam, definitie, beschrijving, match op betekenis, relaties | AI |
| Afleiden en renderen | Type en status uit de beslistabel, letterlijke modelgegevens, harde controles; daarna alle pagina's en een overzicht van wat wacht op akkoord | Scripts van de wiki |
| Voorleggen | Wat de scripts als open markeren, één vraag tegelijk in de chat; het antwoord wordt een besluit in de beoordeling | AI en redacteur |
| Bekijken | `llmwiki promote plan`: samenvatting in de chat; de redacteur leest de pagina's en de wijzigingen in Source Control | Redacteur |
| Akkoord | Het woord AKKOORD in de chat, daarna één klik op "toestaan" | Redacteur |
| Vastleggen | `llmwiki promote apply`: status `goedgekeurd`, een regel per element in `log.md`, pagina's opnieuw gerenderd | Gereedschap, na goedkeuring |

Er is geen run en geen kladblok: alles staat in de werkboom en is te zien in Git. Het akkoord hoort bij de inhoud van de beoordeling; een andere opmaak of een bijgewerkt model vraagt geen nieuw akkoord, een inhoudelijke wijziging wel. Een pagina met `goedgekeurd` zonder overeenkomende regel in `log.md`, of een pagina die afwijkt van wat de scripts maken, wordt bij opslaan in Git geweigerd. De publicatie of goedkeuring staat na afloop in `log.md` — dat is het blijvende verslag.

## 5. Spelregels

### Wie doet wat

| Rol | Doet | Doet nooit |
|---|---|---|
| Redacteur | Stelt de Vraag, beoordeelt voorstellen, geeft akkoord | — |
| AI-assistent | Leest, analyseert, schrijft voorstellen, controleert | Zelf publiceren of exporteren, akkoordvelden invullen |
| Gereedschap | Haalt pagina's op, controleert, publiceert, legt vast | Inhoudelijk oordelen |
| AI-omgeving | Vraagt de redacteur om een klik voordat er gepubliceerd wordt | — |

### Akkoord geven

Per wiki staat in `wiki.yaml` welke vorm geldt.

- **In de chat** (`approval: chat`). De AI toont een samenvatting en vraagt om het woord **AKKOORD**. "Prima" of "ziet er goed uit" is geen akkoord. Een curatie-wiki met beoordelingen gebruikt altijd deze vorm: de redacteur beoordeelt de gerenderde pagina's en de wijzigingen in Git, niet een voorstelbestand. Ook geschikt voor dagelijks redactiewerk in een sync-wiki.
- **Via een document** (`approval: document`), alleen bij publiceren naar een externe site. De AI zet een publicatievoorstel klaar in `voorstellen/`: per pagina een samenvatting en een besluit (publiceren, overslaan, aanpassen), en de volledige diffs in een apart detailbestand. De redacteur zet `akkoord_voor_publicatie` op `ja`, vult een naam in en vraagt de AI het plan uit te voeren.

In beide vormen vraagt de AI-omgeving daarna nog om één klik op "toestaan". Die klik kan de AI niet zelf geven; dat is de echte beveiliging.

**Daarom: zet automatische goedkeuring in de AI-omgeving uit wanneer je publiceert of goedkeurt.** Met automatische goedkeuring vervalt die klik.

### Werkplek eerst

Bij de eerste vraag in een nieuwe sessie controleert de AI of de werkplek in orde is en richt die zo nodig in, na toestemming. Pas daarna begint het inhoudelijke werk. Soms is een handeling van jezelf nodig, zoals het goedkeuren van de koppeling met de wiki of het invullen van je inloggegevens. De AI legt dan uit wat je moet doen. Op Windows zijn geen beheerdersrechten nodig.

### Huisregels

- Regels voor de hele repository staan in `AGENTS.md` in de hoofdmap. Regels voor één wiki staan in `AGENTS.md` in de wikimap en verwijzen naar de hoofdregels.
- Een gedeelde vaardigheid bevat nooit kennis van één specifieke wiki.
- Vaardigheden van een wiki beginnen met de naam van die wiki (`gemma-…`). Gedeelde vaardigheden beginnen met `wiki-`.
- Plaats geen `CLAUDE.md` in de repository: daarmee negeert Claude Code de huisregels.
- Bestanden in `sources/raw/` worden nooit gewijzigd. Een nieuwe versie van een document is een nieuwe bron.
- Een wiki verwijst niet naar pagina's van een andere wiki. Wat de volgende wiki in de keten nodig heeft, wordt na goedkeuring als bron toegevoegd aan `sources/`.
- Een wiki mag een eigen `ARCHITECTURE.md` hebben voor haar eigen opzet (mappen, paginatypen, vaardigheden, gereedschap). De wiki-`AGENTS.md` blijft kort en verwijst ernaar.

### Soorten vaardigheden en gereedschap

Elke vaardigheid (Skill) is een map met een `SKILL.md`. In de kop staat in `metadata` wat voor vaardigheid het is:

| Veld | Waarden | Betekenis |
|---|---|---|
| `kind` | `workflow` | Legt de volgorde van stappen vast: fasen, wie wat doet, waar de mens akkoord geeft. Voert zelf geen stap uit. |
| | `capability` | Voert één stap uit (bijvoorbeeld een bron verwerken, een pagina schrijven). |
| `scope` | `core` | Gedeeld door alle wiki's, naam begint met `wiki-`, bevat geen kennis van één wiki. Staat in `.agents/skills/`. |
| | `wiki` | Hoort bij één wiki, naam begint met de wiki-naam (bijv. `gemma-archimate-model-…`). Staat in `wikis/<wiki>/.agents/skills/`. |
| `requires-skills`, `requires-tools` | namen | Van welke vaardigheden en welk gereedschap deze vaardigheid afhangt; `llmwiki lint` controleert dit. |
| `reads`, `writes` | artefacten | Wat de stap leest en oplevert (bijv. `assessment`, `changeset`). |

Een wiki-workflow is dun: hij volgt een gedeelde workflow (`wiki-curatie-update`, `wiki-sync-edit`) en voegt per stap op een **uitbreidingspunt** eigen vaardigheden, scripts of controles toe. Naslag die een vaardigheid nodig heeft, staat in haar map onder `references/`.

Gereedschap (code) staat op drie plekken:

| Plek | Voor |
|---|---|
| `tools/llmwiki/` | Wat elke wiki nodig heeft; aanroepen via `uv run python -m llmwiki …` |
| `wikis/<wiki>/tools/` | Wat meerdere vaardigheden van één wiki gebruiken; aanroepen via `uv run python tools/…` vanuit de wikimap |
| `<skill>/scripts/` | Wat alleen die ene vaardigheid gebruikt (naam volgens de Agent Skills-standaard) |

De map `scripts/` in de hoofdmap is alleen voor het eenmalig inrichten van de werkplek.

## 6. Begrippen

| Begrip | Betekenis hier |
|---|---|
| Vraag / Antwoord | Wat je de AI vraagt / wat de AI teruggeeft |
| Sessie | Eén gesprek in een AI-omgeving |
| Model | Het taalmodel dat de tekst verwerkt en maakt |
| Rules | Huisregels in `AGENTS.md` |
| Skill | Uitgeschreven werkwijze voor één taak (`capability`) of voor een volgorde van stappen (`workflow`) |
| Workflow | Volgorde van stappen, zelf ook vastgelegd als Skill (`metadata.kind: workflow`) |
| Uitbreidingspunt | Plek in een gedeelde workflow waar een wiki eigen vaardigheden of controles toevoegt |
| Agent / Rol | De AI die een taak uitvoert / de verantwoordelijkheid die hij daarbij heeft (lezer, beoordelaar, schrijver, controleur) |
| Tool | Programma of functie buiten het model |
| MCP | Standaardkoppeling tussen de AI-omgeving en de MediaWiki-site |
| Context | Wat de AI op dit moment "ziet" |
| State | Waar een taak staat: bij een curatie-wiki in de werkboom (beoordelingen), bij een sync-wiki in het kladblok |
| Resultaat | Bijgewerkte pagina's, verslagen en na akkoord de publicatie |

## 7. Verder lezen

- Een nieuwe wiki of repository inrichten: `docs/kluswijzer.md`
- Waarom het zo is ingericht, per AI-omgeving: `docs/onderbouwing.md`
