## Context

Ik ontwerp een **portable monorepo voor meerdere LLM-wiki's**.

Het doel is één Git-repository waarin meerdere zelfstandige LLM-wiki's kunnen worden beheerd, terwijl generieke agentic functionaliteit maar één keer wordt gedefinieerd en door alle wiki's kan worden hergebruikt.

De repository moet bruikbaar zijn vanuit meerdere agentic harnesses, waaronder:

* Claude Code
* OpenCode
* VS Code/Copilot
* Cursor
* Codex
* eventueel andere harnesses die de relevante open standaarden ondersteunen

Ik wil zoveel mogelijk gebruikmaken van bestaande standaarden, met name:

* `AGENTS.md`
* Agent Skills / `.agents/skills/`
* MCP

Ik wil **geen eigen adapterarchitectuur introduceren als bestaande standaarden hetzelfde probleem oplossen**.

## Beoogde structuur

Mijn huidige gedachte is ongeveer:

```text
llm-wikis/
├── AGENTS.md
├── .agents/
│   └── skills/
│       ├── ingest/
│       ├── assess/
│       ├── write/
│       └── validate/
├── schemas/
├── scripts/
├── mcp/
│
├── wiki-gemma/
│   ├── AGENTS.md
│   ├── .agents/
│   │   └── skills/
│   │       ├── gemma-bo/
│   │       └── gemma-archimate/
│   ├── workflows/
│   │   ├── update-wiki/
│   │   └── derive-bo/
│   ├── schemas/
│   ├── scripts/
│   ├── sources/
│   └── wiki/
│
├── wiki-foo/
│   ├── AGENTS.md
│   ├── .agents/
│   │   └── skills/
│   ├── workflows/
│   ├── schemas/
│   ├── scripts/
│   ├── sources/
│   └── wiki/
│
└── ...
```

De bedoeling is dat bijvoorbeeld:

```text
wiki-gemma/workflows/update-wiki/
```

zowel generieke als GEMMA-specifieke capabilities kan gebruiken:

```text
workflow
   │
   ├── generic skill: ingest
   ├── generic skill: assess
   ├── GEMMA skill: gemma-bo
   ├── generic skill: write
   └── generic skill: validate
```

Een andere wiki kan dezelfde generieke skills gebruiken maar eigen skills en workflows toevoegen.

## Centrale architectuurvraag

Ontwerp een architectuur voor deze **portable agent-harness monorepo met meerdere LLM-wiki's**.

De kernvraag is:

> Hoe scheid ik de generieke agentic infrastructuur, de wiki-specifieke kennis en workflows, en de harness-specifieke runtime/configuratie zodanig dat dezelfde Git-repository met meerdere LLM-wiki's portable blijft tussen verschillende agentic harnesses?

## 1. Definieer de lagen

Maak een duidelijk architectuurmodel met minimaal deze lagen:

```text
repository / platform
        ↓
LLM-wiki instance
        ↓
workflow
        ↓
skills / agents / tools
        ↓
harness runtime
        ↓
LLM
```

Bepaal of dit model correct is en pas het aan als een betere decompositie bestaat.

Maak expliciet onderscheid tussen:

* repository;
* platform;
* LLM-wiki;
* workflow;
* skill;
* agent;
* tool;
* MCP;
* context;
* state;
* rules/instructions;
* schema;
* script;
* harness;
* model.

Geef per onderdeel aan:

* wat het conceptueel is;
* wie het beheert;
* waar het leeft;
* of het portable is;
* of het runtime-state bevat.

## 2. Generieke versus wiki-specifieke functionaliteit

Bepaal wat in de repository-root hoort en wat in een wiki-directory hoort.

Onderzoek bijvoorbeeld:

```text
root/
├── AGENTS.md
├── .agents/skills/
├── schemas/
├── scripts/
└── mcp/

wiki-gemma/
├── AGENTS.md
├── .agents/skills/
├── workflows/
├── schemas/
├── scripts/
├── sources/
└── wiki/
```

Beantwoord voor elk onderdeel:

* Waarom hoort het op rootniveau?
* Waarom hoort het bij een wiki?
* Kan het beide niveaus hebben?
* Hoe werkt overriding of uitbreiding?
* Hoe voorkom je duplicatie?

Maak hiervan een tabel.

## 3. Rules en `AGENTS.md`

Onderzoek de huidige ondersteuning van `AGENTS.md` bij:

* Claude Code;
* OpenCode;
* VS Code/Copilot;
* Cursor;
* Codex.

Bepaal:

* hoe root-level `AGENTS.md` wordt ontdekt;
* hoe nested `AGENTS.md` wordt behandeld;
* of rules worden geërfd;
* wat er gebeurt als een subdirectory een eigen `AGENTS.md` heeft;
* of de huidige implementaties voldoende gelijk zijn om hierop een portable architectuur te baseren.

Belangrijk:

Ik wil voorkomen dat wiki-specifieke rules alleen werken in één harness.

Onderzoek daarom ook of het verstandiger is om wiki-specifieke domeinregels in bijvoorbeeld:

```text
wiki-gemma/rules/
```

te plaatsen en `wiki-gemma/AGENTS.md` alleen als entrypoint te gebruiken.

Vergelijk beide modellen.

## 4. Agent Skills

Onderzoek de huidige Agent Skills-standaard.

Bepaal:

* of `.agents/skills/` daadwerkelijk een portable standaard is;
* hoe skill discovery in een monorepo werkt;
* of skills uit bovenliggende directories beschikbaar zijn;
* hoe lokale wiki-skills zich verhouden tot root-skills;
* of een skill dezelfde naam mag hebben op beide niveaus;
* hoe conflicts/precedence worden opgelost;
* welke onderdelen van een skill portable zijn.

Vergelijk bijvoorbeeld:

```text
root/.agents/skills/ingest/
wiki-gemma/.agents/skills/gemma-bo/
```

met:

```text
wiki-gemma/.agents/skills/ingest/
```

Bepaal of de eerste vorm de voorkeur verdient en waarom.

## 5. Workflows

Mijn workflow is bijvoorbeeld:

```text
wiki-gemma/workflows/update-wiki/
```

Onderzoek of een workflow:

* een zelfstandig concept moet zijn;
* beter als Agent Skill kan worden geïmplementeerd;
* een combinatie van skills moet zijn;
* door een agent moet worden uitgevoerd;
* harness-specifiek moet worden aangeroepen.

Maak onderscheid tussen:

```text
workflow = procesdefinitie
skill    = uitvoeringskennis/capability
agent    = doelgerichte uitvoeringslogica
```

Beoordeel of deze definities technisch houdbaar zijn.

Bepaal ook waar een workflow mag verwijzen naar:

* skills;
* scripts;
* schemas;
* tools;
* MCP;
* andere workflows;
* agents.

## 6. Agents en subagents

Onderzoek hoe agents en subagents zich verhouden tot de portable kern.

Beantwoord:

* Is er een portable standaard voor agentdefinities?
* Of zijn agentdefinities momenteel grotendeels harness-specifiek?
* Wanneer heeft een workflow een aparte agent nodig?
* Wanneer is een gewone skill voldoende?
* Wanneer is een subagent nuttig?
* Waar hoort een agentdefinitie thuis als hij wiki-specifiek is?
* Waar hoort hij thuis als hij generiek is?
* Waar horen agent-specifieke permissions en modelkeuzes?

Maak expliciet onderscheid tussen:

```text
agent concept
```

en:

```text
harness agent configuration
```

## 7. MCP en tools

De wiki's kunnen externe systemen gebruiken via MCP, bijvoorbeeld een MediaWiki MCP-server.

Onderzoek hoe dit architectonisch moet worden gescheiden.

Maak onderscheid tussen:

### Portable

De workflow kan conceptueel zeggen:

```text
lees de betreffende MediaWiki-pagina
```

of:

```text
publiceer de gevalideerde wijziging naar MediaWiki
```

### Harness/runtime

De concrete configuratie:

```text
MCP server
server URL
credentials
tool names
permissions
```

Bepaal waar deze verschillende onderdelen moeten leven.

Onderzoek ook of MCP-configuratie:

* repositorybreed;
* wiki-specifiek;
* of deels beide

moet zijn.

## 8. Scripts

Bepaal wanneer een script:

```text
root/scripts/
```

moet staan en wanneer:

```text
wiki-gemma/scripts/
```

of:

```text
.agents/skills/foo/scripts/
```

de juiste plaats is.

Gebruik als criterium bijvoorbeeld:

```text
generiek repositoryprobleem
→ root

wiki-specifieke logica
→ wiki

ondersteunende implementatie van één skill
→ skill
```

Beoordeel of dit een goed principe is.

## 9. Schemas en data-contracten

Ik wil een `schemas/`-laag gebruiken als dat daadwerkelijk waarde toevoegt.

Onderzoek:

```text
root/schemas/
wiki-gemma/schemas/
```

Bepaal:

* wanneer een schema generiek is;
* wanneer het wiki-specifiek is;
* wanneer een schema over-engineering is;
* of workflowstappen beter expliciete bestanden/data-contracten kunnen gebruiken;
* hoe schemas bijdragen aan overdracht tussen agents.

Voorbeelden:

```text
source
assessment
wiki-page
update-result
gemma-bo
```

## 10. Context en state

Onderzoek hoe context en state door deze architectuur lopen.

Bijvoorbeeld:

```text
INGEST
  ↓
ASSESS
  ↓
WRITE
  ↓
VALIDATE
```

Vergelijk:

### Context doorgeven

```text
INGEST
  ↓
grote context
  ↓
ASSESS
  ↓
grote context
  ↓
WRITE
```

met:

### Persistente tussenresultaten

```text
INGEST → ingest-result
              ↓
           ASSESS → assessment
                         ↓
                      WRITE
                         ↓
                     VALIDATE
```

Analyseer:

* context-window gebruik;
* tokenkosten;
* latency;
* reproduceerbaarheid;
* foutisolatie;
* parallelisering;
* agentwisseling;
* state management;
* Git-versiebeheer;
* mogelijkheid om een workflow later te hervatten.

Geef een architectuuradvies voor een LLM-wiki.

## 11. Monorepo en werkdirectory

Een belangrijk doel is dat ik bijvoorbeeld:

```bash
cd wiki-gemma
```

kan doen en vervolgens de GEMMA-wiki als zelfstandige LLM-projectcontext kan gebruiken.

Tegelijk moet de harness generieke resources kunnen vinden in:

```text
../.agents/
../schemas/
../scripts/
```

Onderzoek hoe goed dit momenteel werkt bij de relevante harnesses.

Bepaal of:

```text
repository root = workspace
```

of:

```text
wiki directory = workspace
```

de betere aanpak is.

Bespreek de consequenties voor:

* Git;
* skill discovery;
* `AGENTS.md`;
* workflows;
* MCP;
* scripts;
* relatieve paden;
* context;
* Claude Code;
* OpenCode;
* VS Code/Copilot;
* Cursor;
* Codex.

## 12. Harness portability

Maak expliciet onderscheid tussen drie soorten portability:

### A. Repository portability

De Git-repository kan op Windows/Linux/macOS worden gebruikt.

### B. Harness portability

Dezelfde wiki kan met Claude Code, OpenCode, Copilot, Cursor en Codex worden gebruikt.

### C. Model portability

Dezelfde workflow kan met verschillende LLM's worden uitgevoerd.

Bepaal welke onderdelen deze drie vormen van portability beïnvloeden.

## 13. Harness-specifieke laag

Ontwerp vervolgens de minimale harness-specifieke laag.

Bijvoorbeeld:

```text
.claude/
.opencode/
.cursor/
.github/
```

Bepaal wat hier werkelijk thuishoort.

Denk aan:

* permissions;
* hooks;
* MCP-configuratie;
* commands;
* agent-configuratie;
* modelkeuze;
* runtime-instellingen.

De architectuur moet voorkomen dat domeinlogica hier terechtkomt.

## 14. Concrete architectuur

Geef uiteindelijk een aanbevolen repositorystructuur.

Bijvoorbeeld:

```text
llm-wikis/
├── AGENTS.md
├── .agents/
│   └── skills/
│       ├── ingest/
│       ├── assess/
│       ├── write/
│       └── validate/
├── schemas/
├── scripts/
├── mcp/
│
├── wiki-gemma/
│   ├── AGENTS.md
│   ├── rules/
│   ├── .agents/
│   │   └── skills/
│   │       ├── gemma-bo/
│   │       └── gemma-archimate/
│   ├── workflows/
│   │   ├── update-wiki/
│   │   └── derive-bo/
│   ├── schemas/
│   ├── scripts/
│   ├── sources/
│   └── wiki/
│
└── wiki-foo/
    ├── AGENTS.md
    ├── rules/
    ├── .agents/
    ├── workflows/
    ├── schemas/
    ├── scripts/
    ├── sources/
    └── wiki/
```

Pas deze structuur aan als onderzoek daar aanleiding toe geeft.

## 15. Voorbeeldworkflow

Werk minimaal één concrete workflow uit:

```text
wiki-gemma/workflows/update-wiki/
```

Laat zien hoe deze workflow:

1. generieke rules gebruikt;
2. GEMMA-specifieke rules gebruikt;
3. generieke skills gebruikt;
4. GEMMA-specifieke skills gebruikt;
5. scripts gebruikt;
6. schemas gebruikt;
7. MediaWiki via MCP gebruikt;
8. eventueel agents/subagents gebruikt;
9. tussenresultaten opslaat;
10. uiteindelijk de wiki bijwerkt.

Laat expliciet zien welke onderdelen portable zijn en welke door het harness worden geleverd.

## 16. Vergelijking van mogelijke architecturen

Vergelijk minimaal deze drie modellen:

### Model A — alles per wiki

```text
wiki-a/
  rules/
  skills/
  workflows/
  scripts/

wiki-b/
  rules/
  skills/
  workflows/
  scripts/
```

### Model B — centrale generieke laag + wiki's

```text
root/
  rules/
  skills/
  scripts/

wiki-a/
  rules/
  skills/
  workflows/

wiki-b/
  rules/
  skills/
  workflows/
```

### Model C — packages/modules

```text
core/
wiki-a/
wiki-b/
harness/
```

Beoordeel de verschillen op:

* portability;
* eenvoud;
* hergebruik;
* skill discovery;
* onderhoud;
* versiebeheer;
* harness-compatibiliteit;
* begrijpelijkheid voor mensen;
* begrijpelijkheid voor agents;
* risico op verborgen afhankelijkheden.

Geef geen subjectieve ranking, maar beschrijf de concrete voor- en nadelen en onder welke omstandigheden ieder model passend is.

## 17. Belangrijke ontwerpprincipes

Hanteer minimaal deze principes:

1. **Portable first**
   Domeinlogica en generieke agentic kennis mogen niet afhankelijk zijn van één harness.

2. **Gebruik bestaande standaarden**
   Gebruik `AGENTS.md`, Agent Skills en MCP waar deze passend zijn.

3. **Geen adapterlaag zonder noodzaak**
   Maak geen eigen adapterarchitectuur als harnesses dezelfde standaard rechtstreeks ondersteunen.

4. **Geen duplicatie**
   Een generieke skill wordt niet per wiki gekopieerd.

5. **Wiki-specifiek waar nodig**
   Domeinkennis en domeinworkflows horen bij de betreffende wiki.

6. **Harness als runtime**
   Het harness levert de uitvoeringsomgeving, modelaanroep, permissions, MCP-configuratie en eventueel subagents.

7. **Duidelijke afhankelijkheidsrichting**

```text
wiki
  ↓
generic core
  ↓
harness
  ↓
model
```

Een generieke component mag niet afhankelijk worden van een specifieke wiki.

8. **Expliciete afhankelijkheden**
   Een workflow moet duidelijk maken welke skills, scripts, schemas en tools hij nodig heeft.

9. **Persistente state alleen waar nuttig**
   Maak geen bestanden voor tussenresultaten zonder concreet voordeel.

10. **Menselijk onderhoudbaar**
    De repository moet ook zonder een LLM begrijpelijk en onderhoudbaar zijn.

## 18. Onderzoeksmethode

Gebruik actuele officiële documentatie voor:

* Claude Code;
* OpenCode;
* VS Code/Copilot;
* Cursor;
* Codex;
* Agent Skills;
* MCP.

Maak duidelijk onderscheid tussen:

* formele/open standaarden;
* conventies die door meerdere tools worden ondersteund;
* harness-specifieke functionaliteit;
* mijn eigen architectuurkeuzes.

Gebruik geen verouderde aannames over `CLAUDE.md`, `AGENTS.md`, skills of MCP.

## Gewenst eindresultaat

Lever uiteindelijk:

1. een conceptueel architectuurmodel;
2. een concrete monorepo-directorystructuur;
3. een verantwoordelijkheidsmatrix voor alle onderdelen;
4. een dependencymodel tussen root, wiki en harness;
5. een analyse van `AGENTS.md` en nested instructions;
6. een analyse van portable Agent Skills;
7. een analyse van workflows versus skills versus agents;
8. een analyse van MCP en tools;
9. een analyse van context en state;
10. een analyse van workspace/monorepo discovery;
11. een vergelijking van alternatieve architecturen;
12. een concreet voorbeeld voor `wiki-gemma`;
13. een concreet voorbeeld van uitvoering vanuit Claude Code;
14. een concreet voorbeeld van uitvoering vanuit OpenCode;
15. een migratiepad vanaf een bestaande Claude Code LLM-wiki.

De uiteindelijke architectuur moet zo veel mogelijk gebaseerd zijn op bestaande standaarden en zo weinig mogelijk op zelfbedachte conventies.
