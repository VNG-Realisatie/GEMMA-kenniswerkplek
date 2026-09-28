## Conclusie

* [Verified] **Agent Skills + `SKILL.md`** is momenteel belangrijkste portable standaard voor herbruikbare agent-capabilities. OpenAI, VS Code/Copilot en OpenCode ondersteunen dit formaat; Cursor ondersteunt Agent Skills eveneens. ([Visual Studio Code][1])
* [Verified] **`AGENTS.md`** is brede conventie voor projectinstructies, maar geen formele standaard. OpenCode, Codex, Cursor en VS Code ondersteunen het; Claude Code gebruikt primair `CLAUDE.md`. ([Visual Studio Code][2])
* [Verified] **MCP** is formele protocolstandaard voor aansluiting van AI-applicaties op tools, resources en prompts. MCP standaardiseert daarmee toolintegratie, niet workflows, skills of agents. ([Model Context Protocol][3])
* [Inferred] De beste architectuur is daarom **portable core + wiki's + dunne harness-adapters**, waarbij `SKILL.md` het primaire portable capability-formaat is en `AGENTS.md` de gemeenschappelijke projectinstructielaag.
* [Inferred] Workflows, domeinagents en state moeten **niet worden gemodelleerd als eigenschappen van een specifieke harness**. Ze vormen applicatielogica bovenop skills en tools.
* [Inferred] De repository moet **niet proberen één universele discovery-mechaniek te maken**. Laat iedere harness zijn eigen discovery uitvoeren en gebruik kleine adapters waar discovery niet overeenkomt.

## 1. Architectuurconcepten

### LLM-wiki

* [Inferred] Een **LLM-wiki** is een domeinspecifieke kennis- en uitvoeringsomgeving bestaande uit:

  * kennis/content;
  * bronnen;
  * domeinregels;
  * skills;
  * workflows;
  * schemas;
  * deterministische scripts;
  * externe tools.
* [Inferred] Een LLM-wiki is dus meer dan MediaWiki-content. MediaWiki is één extern kennissysteem binnen de wiki-omgeving.

### Generieke core

* [Inferred] De **core** bevat capabilities die meerdere wiki's kunnen gebruiken zonder kennis van één specifiek domein.
* [Inferred] Voorbeelden:

  * ingest;
  * source assessment;
  * documentanalyse;
  * wiki-update;
  * validatie;
  * Git-operaties;
  * bronverwijzingen;
  * generieke schemas;
  * generieke scripts.
* [Inferred] Core mag niet afhankelijk zijn van `gemma`, `wiki-a`, of andere domeinbegrippen.

### Wiki

* [Inferred] Een wiki bevat domeinspecifieke kennis en capabilities.
* [Inferred] Voorbeeld:

  * `gemma-bo`;
  * `gemma-archimate`;
  * GEMMA-bronnen;
  * GEMMA-validatieregels;
  * GEMMA-schemas.

### Skill

* [Verified] Een Agent Skill is een directory met `SKILL.md` en optioneel scripts, references, assets en andere resources. Skill beschrijft wanneer en hoe capability wordt uitgevoerd. ([OpenAI Developers][4])
* [Inferred] Skill = **herbruikbare capability**.
* [Inferred] Skill beschrijft niet primair *wanneer een volledige bedrijfsworkflow start*, maar *hoe een bepaalde capability wordt uitgevoerd*.
* [Inferred] `ingest`, `assess`, `write` en `validate` zijn dus goede skills.

### Workflow

* [Inferred] Workflow = **geordende uitvoering van capabilities met doel, invoer, tussenresultaten en eindresultaat**.
* [Inferred] Voorbeeld:

  * `update-wiki`
  * `ingest`
  * `assess`
  * `write`
  * `validate`
  * `publish`
* [Inferred] Workflow is geen Agent Skills-standaardconcept. Je moet dit als eigen architectuurconcept definiëren.
* [Inferred] Workflow kan skills aanroepen, scripts uitvoeren, state produceren en agents inzetten.

### Agent

* [Verified] Harnesses zoals OpenCode en VS Code ondersteunen expliciete custom agents/subagents met eigen instructies, tools, permissions en eventueel modelkeuze. ([OpenCode][5])
* [Inferred] Een agent is **uitvoeringsrol met eigen instructies, bevoegdheden en eventueel model**.
* [Inferred] Maak onderscheid tussen:

  * **logical agent role** — portable;
  * **agent runtime configuration** — harness-specifiek.
* [Inferred] Bijvoorbeeld:

  * `researcher`;
  * `assessor`;
  * `writer`;
  * `validator`.

### Tool

* [Verified] MCP definieert tools als uitvoerbare functies waarmee een model acties kan uitvoeren of informatie kan ophalen. ([Model Context Protocol][3])
* [Inferred] Tool = **operationele capability buiten het model**.
* [Inferred] Voorbeelden:

  * filesystem;
  * Git;
  * MediaWiki;
  * search;
  * Python;
  * API.

### MCP

* [Verified] MCP standaardiseert communicatie tussen AI-applicatie en servers die tools, resources en prompts aanbieden. ([Model Context Protocol][3])
* [Inferred] MCP is daarom **tool/resource-integratielaag**, niet workflowlaag.
* [Inferred] Workflow moet zeggen:

  * "publiceer pagina naar MediaWiki".
* [Inferred] Harness-configuratie bepaalt:

  * welke MCP-server;
  * welk endpoint;
  * credentials;
  * permissions;
  * concrete toolnamen.
* [Inferred] Portable workflow mag dus bij voorkeur niet afhankelijk zijn van `mediawiki_update_page` als concrete MCP-toolnaam.

### Context

* [Inferred] Context = informatie die tijdelijk beschikbaar is binnen modeluitvoering.
* [Inferred] Context bevat bijvoorbeeld:

  * relevante wiki-pagina;
  * bronfragmenten;
  * skill-instructies;
  * assessment;
  * gebruikersopdracht.
* [Inferred] Context is primair runtime-state van model/harness en hoort niet automatisch in Git.

### State

* [Inferred] State = **persistent resultaat dat nodig is om workflowuitvoering te hervatten, controleren of reproduceren**.
* [Inferred] Voorbeelden:

  * ingest-resultaat;
  * assessment;
  * wijzigingsvoorstel;
  * validatieresultaat;
  * workflowstatus.
* [Inferred] State hoort alleen in Git als versiebeheer van die state daadwerkelijk waarde heeft.

### Harness

* [Inferred] Harness = runtime die model, context, tools, permissions, skills, agents, instructies en workflow-uitvoering bij elkaar brengt.
* [Verified] Claude Code, OpenCode, VS Code/Copilot en Cursor hebben ieder eigen discovery- en configuratiemechanismen. ([Claude Platform Docs][6])
* [Inferred] Harness bepaalt daarom:

  * model;
  * contextopbouw;
  * toolbeschikbaarheid;
  * permissions;
  * MCP-configuratie;
  * agent runtime;
  * discovery;
  * sessie/state-management.

## 2. Standaarden versus conventies

### Formele/open standaarden

* [Verified] **MCP** is formele open protocolstandaard voor model-contextintegratie. ([Model Context Protocol][3])
* [Verified] **Agent Skills** is een open standaard voor portable skills met `SKILL.md`. ([Visual Studio Code][1])

### Brede conventies

* [Verified] **`AGENTS.md`** wordt door meerdere agent-harnesses ondersteund, maar discovery en nesting verschillen. ([Visual Studio Code][2])
* [Inferred] `AGENTS.md` is daarom geschikt als **shared baseline**, niet als volledige portable instructie-engine.

### Harness-specifiek

* [Verified] Claude Code gebruikt `CLAUDE.md` als projectgeheugen/instructielaag en ondersteunt imports en geneste bestanden. ([Claude Platform Docs][6])
* [Verified] OpenCode V2 gebruikt `AGENTS.md` en heeft eigen `.opencode/skills`, `.opencode/agents` en configuratie. ([OpenCode][7])
* [Verified] VS Code ondersteunt meerdere formats afhankelijk van geselecteerde harness, waaronder `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` en `.claude/rules`. ([Visual Studio Code][2])
* [Verified] Cursor heeft `.cursor/rules` en ondersteunt `AGENTS.md`, inclusief nested `AGENTS.md`. ([Cursor][8])

### Eigen architectuurkeuzes

* [Inferred] `workflow` is eigen architectuurconcept.
* [Inferred] `logical agent role` is eigen architectuurconcept.
* [Inferred] `wiki` als zelfstandige applicatie-eenheid is eigen architectuurconcept.
* [Inferred] `core` als gedeelde capabilitylaag is eigen architectuurconcept.
* [Inferred] Data-contracten tussen workflowstappen zijn eigen architectuurkeuze.

## 3. Alternatieve architecturen

### Model A — iedere wiki volledig zelfstandig

* [Inferred] Elke wiki bevat eigen rules, skills, workflows en scripts.
* [Inferred] Voordeel:

  * maximale eenvoud per wiki.
* [Inferred] Nadeel:

  * duplicatie;
  * afwijkende implementaties;
  * moeilijk centraal verbeteren;
  * grotere kans op divergentie.
* [Inferred] Geschikt wanneer wiki's inhoudelijk vrijwel onafhankelijk zijn.

### Model B — centrale core + wiki's

* [Inferred] Core bevat generieke skills en scripts.
* [Inferred] Iedere wiki bevat eigen domeinspecifieke skills en workflows.
* [Inferred] Voordeel:

  * hergebruik;
  * duidelijke scheiding;
  * eenvoudige Git-versiebeheersing.
* [Inferred] Nadeel:

  * dependency discovery moet goed worden ontworpen.
* [Inferred] Dit model past goed bij meerdere inhoudelijk verschillende wiki's met gedeelde agentic capabilities.

### Model C — core als package

* [Inferred] Core wordt technisch als afzonderlijk package/versioned component behandeld.
* [Inferred] Voordeel:

  * expliciete dependency/versioning.
* [Inferred] Nadeel:

  * extra package-managementlaag;
  * minder transparant voor mensen;
  * skills zijn niet vanzelf package-onafhankelijk.
* [Inferred] Dit is vooral zinvol wanneer core door meerdere repositories wordt gebruikt.

### Model D — capability registry

* [Inferred] Een centrale registry beschrijft skills, workflows en afhankelijkheden.
* [Inferred] Voordeel:

  * expliciete discovery.
* [Inferred] Nadeel:

  * extra metadata en tooling;
  * registry kan snel dupliceren wat `SKILL.md` al beschrijft.
* [Inferred] Voor één monorepo is zo'n registry waarschijnlijk onnodige abstractie.

## 4. Aanbevolen architectuur

### Kernmodel

* [Inferred] Gebruik **Model B**, maar met één belangrijke verfijning:

  * portable core;
  * portable wiki;
  * portable workflows;
  * Agent Skills als capabilityformaat;
  * harness-adapters;
  * MCP als externe toolinterface.
* [Inferred] Conceptueel:

  * `Harness`

    * runt `Agent`
    * gebruikt `Workflow`
    * laadt `Rules`
    * ontdekt `Skills`
    * gebruikt `Tools`
  * `Workflow`

    * componeert `Skills`
    * gebruikt `Scripts`
    * leest/schrijft `State`
    * gebruikt `Schemas`
  * `Skill`

    * gebruikt `Scripts`
    * gebruikt `References`
    * gebruikt `Tools`
  * `Tool`

    * filesystem / Git / MCP / API
  * `Wiki`

    * content / sources / domain skills / domain workflows / domain rules
  * `Core`

    * generic skills / generic workflows / generic scripts / generic schemas

### Afhankelijkheidsrichting

* [Inferred] Gebruik deze richting:

  * `Harness → Workflow`
  * `Harness → Agent`
  * `Harness → Skills`
  * `Workflow → Skills`
  * `Workflow → Scripts`
  * `Workflow → Schemas`
  * `Skill → Scripts`
  * `Skill → Tools`
  * `Wiki → Core`
  * `Wiki → Wiki-specific Skills`
  * `Wiki → Wiki-specific Workflows`
* [Inferred] Vermijd:

  * `Core → Wiki`
  * `Core → Harness`
  * `Workflow → concrete harness tool`
  * `Skill → concrete model`
  * `Wiki → andere Wiki`

## 5. Concrete repositorystructuur

* [Inferred] De architectuur leidt tot:

```text
repo/
├── AGENTS.md
├── core/
│   ├── skills/
│   │   ├── ingest/
│   │   │   └── SKILL.md
│   │   ├── assess/
│   │   │   └── SKILL.md
│   │   ├── write/
│   │   │   └── SKILL.md
│   │   └── validate/
│   │       └── SKILL.md
│   ├── workflows/
│   ├── scripts/
│   └── schemas/
├── wikis/
│   ├── gemma/
│   │   ├── AGENTS.md
│   │   ├── content/
│   │   ├── sources/
│   │   ├── skills/
│   │   │   ├── gemma-bo/
│   │   │   │   └── SKILL.md
│   │   │   └── gemma-archimate/
│   │   │       └── SKILL.md
│   │   ├── workflows/
│   │   │   └── update-wiki.md
│   │   ├── scripts/
│   │   └── schemas/
│   └── wiki-b/
│       ├── AGENTS.md
│       ├── content/
│       ├── sources/
│       ├── skills/
│       ├── workflows/
│       ├── scripts/
│       └── schemas/
├── adapters/
│   ├── claude/
│   ├── opencode/
│   ├── copilot/
│   ├── cursor/
│   └── codex/
└── .gitignore
```

* [Inferred] `core/skills` en `wikis/*/skills` volgen Agent Skills-conventie.
* [Inferred] De overige directories zijn eigen architectuurconventies.
* [Inferred] De exacte directorynamen zijn geen standaard en kunnen worden aangepast.

## 6. Rules

### Baseline

* [Verified] `AGENTS.md` is hiervoor bruikbaar omdat meerdere relevante harnesses het ondersteunen. ([Visual Studio Code][2])
* [Inferred] Gebruik daarom:

  * repository-root `AGENTS.md` voor minimale universele projectregels;
  * wiki-level `AGENTS.md` voor domeincontext;
  * aanvullende bestanden voor uitgebreide regels.
* [Inferred] Houd `AGENTS.md` klein. Het wordt breed geladen en verhoogt anders onnodig contextgebruik.
* [Verified] OpenAI adviseert expliciet om `AGENTS.md` niet te vullen met instructies die voor iedere taak onnodig context kosten. ([OpenAI Developers][9])

### Inheritance

* [Verified] Nested `AGENTS.md` werkt verschillend per harness. OpenCode combineert gevonden bestanden; Codex injecteert root-to-leaf; Cursor ondersteunt parent/child-combinatie; VS Code noemt nested support experimenteel voor zijn Local agent. ([OpenCode][7])
* [Inferred] Gebruik nested `AGENTS.md` daarom alleen voor **basiscontext**, niet voor complexe inheritance-logica.
* [Inferred] Maak wiki-specifieke regels expliciet en laat workflows/skills ze gericht laden.

## 7. Skills

### Discovery

* [Verified] `.agents/skills/<name>/SKILL.md` wordt door meerdere systemen ondersteund; OpenCode ondersteunt daarnaast `.opencode/skills` en `.claude/skills`. ([OpenCode][10])
* [Inferred] Gebruik `.agents/skills` als primaire portable locatie.
* [Inferred] Plaats generieke skills daar:

```text
.agents/
└── skills/
    ├── ingest/
    │   └── SKILL.md
    ├── assess/
    │   └── SKILL.md
    └── validate/
        └── SKILL.md
```

* [Inferred] Gebruik per wiki:

```text
wikis/gemma/.agents/skills/
```

* [Inferred] Dit maakt discovery mogelijk via directoryhiërarchie, zonder eigen skill-registry.

### Probleem

* [Verified] Niet iedere harness ontdekt `.agents/skills` exact hetzelfde; OpenCode doet dat wel, VS Code ondersteunt `.agents/skills`, terwijl Claude Code eigen skill discovery heeft. ([OpenCode][10])
* [Inferred] De adapters mogen daarom alleen discovery/configuratie vertalen.
* [Inferred] Ze mogen niet de skill zelf dupliceren.

## 8. Workflows

### Workflow als portable artefact

* [Inferred] Bewaar workflowdefinitie onafhankelijk van harness:

```text
wikis/gemma/workflows/update-wiki.md
```

* [Inferred] Workflow beschrijft:

  * doel;
  * inputs;
  * stappen;
  * benodigde skills;
  * schemas;
  * state;
  * validatie;
  * eventuele menselijke goedkeuring.
* [Inferred] Workflow beschrijft niet:

  * Claude command;
  * OpenCode command;
  * modelnaam;
  * MCP endpoint;
  * permission syntax.

### Harness entrypoint

* [Inferred] Maak per harness alleen dunne entrypoints:

  * Claude command/skill;
  * OpenCode command;
  * Codex skill/agent;
  * VS Code prompt/agent;
  * Cursor command/skill.
* [Inferred] Elk entrypoint verwijst naar dezelfde portable workflow.

## 9. Agents

### Logical agent

* [Inferred] Definieer portable rollen alleen wanneer rol echt waarde toevoegt:

  * `researcher`;
  * `assessor`;
  * `writer`;
  * `validator`.
* [Inferred] Leg rol vast als tekstuele instructie of skill-gerelateerde resource.

### Runtime agent

* [Verified] Harnesses koppelen daar eigen model-, permission- en toolconfiguratie aan. OpenCode-agentdefinities bevatten bijvoorbeeld model en permissions. ([OpenCode][5])
* [Inferred] Runtimeconfiguratie hoort dus in `adapters/`, niet in de wiki-workflow.

## 10. MCP

### Architectuur

* [Verified] MCP-server exposeert tools/resources/prompts; client/harness bepaalt hoe deze beschikbaar komen voor modeluitvoering. ([Model Context Protocol][3])
* [Inferred] Maak MCP-configuratie harness-specifiek:

```text
adapters/
├── claude/
│   └── mcp/
├── opencode/
│   └── mcp/
├── copilot/
│   └── mcp/
└── codex/
    └── mcp/
```

* [Inferred] Gebruik dezelfde semantische capability:

  * `mediawiki.read`
  * `mediawiki.write`
* [Inferred] Laat concrete MCP-toolnaam en servernaam bij adapterlaag.
* [Inferred] Workflow zegt dus niet:

  * `call mcp__mediawiki__update_page`
* [Inferred] Workflow zegt:

  * `publish wiki page`.

### MediaWiki

* [Inferred] MediaWiki MCP kan rechtstreeks door skills worden gebruikt wanneer harness discovery en toolnamen bekend zijn.
* [Inferred] Voor maximale portability moet skill instructie de **doelactie** beschrijven en alleen concrete toolnamen noemen in harness-specifieke instructie.

## 11. Context en state

### Context

* [Inferred] Gebruik context voor tijdelijke informatie die binnen één stap nodig is.
* [Inferred] Geef niet automatisch volledige output van `INGEST` door aan `ASSESS` en vervolgens `WRITE`.

### Persistent tussenresultaat

* [Inferred] Gebruik persistent artefact wanneer resultaat:

  * groot is;
  * later opnieuw nodig is;
  * controleerbaar moet zijn;
  * door andere agent gebruikt wordt;
  * workflow hervatbaar moet maken.
* [Inferred] Geschikte keten:

```text
INGEST
  ↓
source-result.json
  ↓
ASSESS
  ↓
assessment.json
  ↓
WRITE
  ↓
proposal/
  ↓
VALIDATE
  ↓
validation.json
  ↓
PUBLISH
```

* [Inferred] Dit verlaagt contextgebruik, maakt foutisolatie mogelijk en maakt workflowhervatting eenvoudiger.
* [Inferred] Git is geschikt voor state wanneer menselijke review en reproduceerbaarheid belangrijk zijn; tijdelijke runtime-state hoort buiten Git.

## 12. Schemas

### Gebruik

* [Inferred] Gebruik schema's alleen wanneer data tussen stappen of agents een expliciet contract nodig heeft.
* [Inferred] Goede kandidaten:

  * `source`;
  * `assessment`;
  * `page-update`;
  * `validation-result`.
* [Inferred] Gebruik JSON Schema als generiek contractformaat wanneer toolingvalidatie nodig is.

### Generiek versus wiki

* [Inferred] Generieke schemas:

  * workflow metadata;
  * source;
  * assessment;
  * validation;
  * update-result.
* [Inferred] Wiki-specific:

  * GEMMA-object;
  * ArchiMate-element;
  * domeinspecifieke assessment.

## 13. Scripts

### Plaatsing

* [Inferred] Plaats script daar waar eigenaarschap ligt:

  * `core/scripts/` → generiek;
  * `wikis/gemma/scripts/` → GEMMA-specifiek;
  * `skill/scripts/` → uitsluitend skill-specifiek.
* [Inferred] Script hoort niet in `workflow/` tenzij workflow zelf deterministische uitvoeringscode bevat.
* [Verified] Agent Skills ondersteunen scripts als onderdeel van skill resources. ([OpenAI Developers][4])
* [Inferred] Python is geschikte portable taal voor repositoryoperaties; gebruik `/` in configuratie en Python `pathlib` voor OS-onafhankelijke paden.

## 14. Monorepo workspace

### Repository root

* [Inferred] Repository root als workspace geeft beste discovery van core en gedeelde configuratie.
* [Inferred] Dit is vooral geschikt voor beheer van meerdere wiki's.

### Wiki als workspace

* [Inferred] `cd wikis/gemma` moet ook bruikbaar zijn.
* [Verified] OpenCode zoekt vanaf huidige directory omhoog richting Git-worktree en ontdekt daar `AGENTS.md` en skills. ([OpenCode][7])
* [Verified] Claude Code zoekt eveneens omhoog naar instructiebestanden en ontdekt geneste instructies bij het lezen van subtrees. ([Claude Platform Docs][6])
* [Inferred] Maak daarom wiki-directory een **logische workspace**, maar houd Git-root de technische repository-root.
* [Inferred] Harness-adapters moeten voorkomen dat een wiki alleen werkt wanneer repository-root geopend is.

### VS Code

* [Verified] VS Code heeft expliciete ondersteuning voor parent-repository customizations via `chat.useCustomizationsInParentRepositories`, maar die instelling is niet standaard geactiveerd. ([Visual Studio Code][11])
* [Inferred] Voor VS Code is daarom adapterconfiguratie belangrijker wanneer `wikis/gemma` rechtstreeks als workspace wordt geopend.

## 15. Portable/harness-specifieke verdeling

### Portable

* [Inferred] Portable maken:

  * wiki content;
  * sources;
  * `SKILL.md`;
  * workflowdefinities;
  * scripts;
  * schemas;
  * domeinregels;
  * logical agent roles;
  * state/data-contracten.

### Harness-specifiek

* [Inferred] Harness-specifiek houden:

  * modelselectie;
  * permissions;
  * MCP registration;
  * hooks;
  * command syntax;
  * agent runtime configuration;
  * session settings;
  * discovery workarounds.
* [Inferred] Deze scheiding is kern van harness portability.

## 16. OS-portability

### Repository

* [Inferred] Git repository zelf is OS-portable wanneer bestanden geen OS-specifieke absolute paden of shellcommando's vereisen.
* [Inferred] Gebruik:

  * UTF-8;
  * LF;
  * `/` als repositorypadnotatie;
  * Python voor complexe scripts;
  * relatieve paden;
  * geen `/home/...`;
  * geen `C:\...`.
* [Inferred] Leg newlinebeleid vast met `.gitattributes`.

### Runtime

* [Verified] Claude Code ondersteunt macOS, Linux en Windows via WSL/Git Bash; daarmee bestaat ook voor harness-runtime een OS-afhankelijkheid die buiten de repository ligt. ([Claude Platform Docs][12])
* [Inferred] Repository-portability betekent daarom niet dat iedere harness-runtime identiek werkt op ieder OS.

## 17. Concrete dependencystructuur

* [Inferred] Conceptueel:

```text
                    HARNESS
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       AGENTS       AGENTS        MCP
          │
          ↓
       WORKFLOW
          │
      ┌───┼────┐
      ↓   ↓    ↓
   SKILLS SCRIPTS SCHEMAS
      │
      ↓
    TOOLS
      │
      ├── filesystem
      ├── Git
      └── MCP
             │
             ↓
         MediaWiki
```

* [Inferred] Wiki-specifieke uitbreiding zit naast core:

```text
CORE
├── generic skills
├── generic scripts
└── generic schemas
        ↑
        │
WIKI
├── domain skills
├── domain workflows
├── domain rules
├── domain schemas
└── domain scripts
```

## 18. Discoverystrategie

### Repositoryregels

* [Inferred] Root `AGENTS.md` bevat alleen regels die voor iedere wiki gelden.

### Wikiregels

* [Inferred] Wiki `AGENTS.md` bevat alleen regels die voor die wiki gelden.

### Skills

* [Verified] Gebruik `SKILL.md` met `name` en `description`; skills worden on-demand ontdekt/geladen door ondersteunde harnesses. ([OpenCode][10])
* [Inferred] Discovery moet daarom primair gebaseerd zijn op **directory discovery + skill metadata**, niet op eigen registry.

### Workflow

* [Inferred] Workflow discovery kan via:

  * expliciete bestandslocatie;
  * skill die workflow beschrijft;
  * harness command dat workflowbestand opent.
* [Inferred] Maak workflownamen uniek binnen wiki, niet globaal.

## 19. Minimale Claude Code-adapter

* [Verified] Claude Code gebruikt `CLAUDE.md` als projectinstructie en ondersteunt imports. ([Claude Platform Docs][6])
* [Inferred] Minimale adapter:

```text
adapters/claude/
├── CLAUDE.md
├── skills/
└── agents/
```

* [Inferred] `CLAUDE.md` moet zo klein mogelijk zijn:

  * uitleg repository;
  * verwijzing naar portable `AGENTS.md`;
  * verwijzing naar workflowgebruik;
  * eventueel Claude-specifieke beperkingen.
* [Inferred] Dupliceer geen domeinregels in `CLAUDE.md`.

## 20. OpenCode-adapter

* [Verified] OpenCode ondersteunt direct `AGENTS.md`, `.agents/skills`, `.opencode/skills`, `.opencode/agents` en `opencode.json`. ([OpenCode][7])
* [Inferred] OpenCode heeft daardoor relatief weinig adaptercode nodig.
* [Inferred] Gebruik portable `AGENTS.md` + `.agents/skills` en alleen `.opencode/` voor echte OpenCode-specificatie.

## 21. Codex, Copilot en Cursor

* [Verified] Codex gebruikt `AGENTS.md` als projectinstructielaag en ondersteunt nested instruction discovery. ([OpenAI Developers][13])
* [Verified] VS Code ondersteunt `AGENTS.md` en `.agents/skills`, maar precieze discovery hangt af van geselecteerde agent harness. ([Visual Studio Code][2])
* [Verified] Cursor ondersteunt `AGENTS.md`, nested discovery en eigen `.cursor/rules`. ([Cursor][8])
* [Inferred] Daardoor kan dezelfde repository grotendeels zonder duplicatie met alle drie werken.

## 22. Belangrijkste ontwerpkeuze

* [Inferred] **Gebruik Agent Skills als portable capabilitystandaard.**
* [Inferred] **Gebruik `AGENTS.md` als gemeenschappelijke projectinstructieconventie.**
* [Inferred] **Gebruik MCP als portable protocol voor externe tools.**
* [Inferred] **Maak workflows eigen portable architectuurconcept.**
* [Inferred] **Maak agents composities van workflow + role + runtimeconfiguratie.**
* [Inferred] **Maak harness-adapters dun.**
* [Inferred] **Gebruik geen centrale registry zolang directory discovery en skill metadata voldoende zijn.**

## 23. Eindbeeld

* [Inferred] De architectuur wordt daarmee:

```text
                    ┌───────────────────────┐
                    │       HARNESS         │
                    │ Claude/OpenCode/etc.  │
                    └───────────┬────────────┘
                                │
                    ┌───────────▼────────────┐
                    │   HARNESS ADAPTER      │
                    │ discovery/config/tools │
                    └───────────┬────────────┘
                                │
               ┌────────────────▼────────────────┐
               │       PORTABLE LLM-WIKI         │
               │                                 │
               │ AGENTS.md                       │
               │ workflows/                      │
               │ skills/                         │
               │ schemas/                        │
               │ scripts/                        │
               │ sources/                        │
               │ content/                        │
               └────────────────┬────────────────┘
                                │
                    ┌───────────▼────────────┐
                    │     SHARED CORE        │
                    │ generic skills/scripts │
                    │ schemas/workflows      │
                    └───────────┬────────────┘
                                │
               ┌────────────────▼────────────────┐
               │            TOOLS                │
               │ filesystem · Git · MCP · APIs │
               └────────────────┬────────────────┘
                                │
                         ┌──────▼──────┐
                         │  MediaWiki  │
                         └─────────────┘
```

* [Inferred] Dit geeft drie onafhankelijke portability-assen:

  * **repository portability** → Git + OS-onafhankelijke bestanden/scripts;
  * **harness portability** → portable skills/workflows + dunne adapters;
  * **model portability** → geen modelafhankelijke workflowlogica.
* [Inferred] Belangrijkste beperking blijft **harness discovery**. Daarvoor bestaat momenteel geen universele standaard die rules, workflows, agents en MCP-configuratie volledig uniform maakt. De architectuur moet dit niet weg-abstraheren, maar klein en expliciet isoleren. ([Visual Studio Code][2])
* [Inferred] Daarmee is **core + wiki's + portable skills/workflows + dunne harness-adapters** de meest directe architectuur die de gevraagde doelen bereikt zonder eigen frameworklaag te introduceren.

[1]: https://code.visualstudio.com/docs/agent-customization/agent-skills?utm_source=chatgpt.com "Use Agent Skills in VS Code"
[2]: https://code.visualstudio.com/docs/agent-customization/custom-instructions?utm_source=chatgpt.com "Use custom instructions in VS Code"
[3]: https://ts.sdk.modelcontextprotocol.io/?utm_source=chatgpt.com "MCP TypeScript SDK | MCP TypeScript SDK (v1)"
[4]: https://developers.openai.com/api/docs/guides/tools-skills?utm_source=chatgpt.com "Skills | OpenAI API"
[5]: https://opencode.ai/v2/docs/agents?utm_source=chatgpt.com "Agents | OpenCode"
[6]: https://docs.anthropic.com/zh-CN/docs/claude-code/memory?utm_source=chatgpt.com "管理 Claude 的内存 - Anthropic"
[7]: https://opencode.ai/v2/docs/instructions?utm_source=chatgpt.com "Instructions | OpenCode"
[8]: https://cursor.com/docs/rules?trk=article-ssr-frontend-pulse_little-text-block&utm_source=chatgpt.com "Rules | Cursor Docs"
[9]: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra?utm_source=chatgpt.com "Rethinking skills and prompts for GPT-6 Astra | OpenAI Developers"
[10]: https://opencode.ai/docs/skills?utm_source=chatgpt.com "Agent Skills | OpenCode"
[11]: https://code.visualstudio.com/docs/agents/reference/ai-settings?utm_source=chatgpt.com "AI settings reference"
[12]: https://docs.anthropic.com/en/docs/claude-code/getting-started?utm_source=chatgpt.com "Set up Claude Code - Anthropic"
[13]: https://developers.openai.com/api/docs/guides/latest-model?gallery=open&galleryItem=trivia-quiz-game&model=gpt-5.3-codex&translationFallback=de-DE&utm_source=chatgpt.com "Model guidance | OpenAI API"
