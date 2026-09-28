# Architectuur: portable monorepo voor meerdere LLM-wiki's

Peildatum onderzoek: 26 september 2026. Harness-gedrag verandert snel; sectie 8 bevat een verificatieprocedure.

## 0. Leeswijzer

### 0.1 Labels voor feitelijke claims

| Label | Betekenis |
|---|---|
| [Verified] | Staat in actuele officiële documentatie of is een breed geaccepteerd feit. Bron in sectie 10. |
| [Inferred] | Logische afleiding uit gedocumenteerde feiten, niet letterlijk gedocumenteerd. |
| [Speculative] | Niet gedocumenteerd of onduidelijk gedocumenteerd. Moet worden geverifieerd (sectie 8). |

Uitspraken zonder label zijn architectuurkeuzes, geen feitelijke claims.

### 0.2 Classificatie van voorzieningen

| Code | Categorie | Voorbeeld |
|---|---|---|
| (S) | Formele/open standaard | Agent Skills-specificatie, MCP, AGENTS.md, JSON Schema |
| (C) | Conventie ondersteund door meerdere tools | `.agents/skills/` |
| (H) | Harness-specifieke voorziening | `.claude/`, `opencode.json`, `.codex/`, `.vscode/`, `.cursor/` |
| (K) | Eigen architectuurkeuze | Workflow als skill, run-directory, publish-gate |

### 0.3 Terminologie

Dit document gebruikt uitsluitend de volgende termen in de opgegeven betekenis: Vraag, Antwoord, Sessie, Model, Rules, Context, State, Skill, Workflow, Agent, Rol, Agentprofiel, Tool, MCP, Resultaat. Aanvullend gedefinieerd in sectie 3: LLM-wiki, generieke laag, wiki-laag, harness, artefact, run.

---

## 1. Uitkomsten van het interview

| Onderwerp | Antwoord | Consequentie voor de architectuur |
|---|---|---|
| Werkmap | Generiek werk vanuit de repository-root, specifiek werk vanuit een wiki-map; wiki-map komt vaker voor | Beide werkmappen moeten volwaardig werken; de wiki-map is het primaire ontwerppunt |
| Harness-pariteit | Volledige pariteit | Elke Workflow moet in Claude Code, OpenCode, VS Code/Copilot, Cursor en Codex op dezelfde manier starten en dezelfde Resultaten opleveren. Waar een harness een voorziening mist, is een minimale brug nodig |
| Symlinks | Onbekend of beschikbaar | Geen symlinks in Git. Lokale koppelingen alleen via script met terugval op kopiëren |
| PUBLISH | Altijd menselijke gate | De gate moet deterministisch zijn en mag niet afhangen van Model-gedrag of harness-permissies alleen |
| Tussenresultaten | Persistent op schijf, niet in Git; alleen eindresultaat in Git | Run-directory per wiki, gitignored |
| Hergebruik core | Mogelijk later buiten deze repository | Core moet als pakket extraheerbaar zijn zonder herstructurering |
| Content-opslag | Wikitext plus metadata per pagina | Sidecar-bestand per pagina met revisie-informatie |
| Oplevering | Markdown in de repository | Dit bestand |

---

## 2. Onderzoek: standaarden en harness-ondersteuning

### 2.1 Wat is gestandaardiseerd en wat niet

| Onderwerp | Status | Bevinding |
|---|---|---|
| AGENTS.md | (S) | [Verified] Op 9 december 2025 heeft de Linux Foundation de Agentic AI Foundation (AAIF) opgericht met MCP, goose en AGENTS.md als eerste projecten. [Inferred] AGENTS.md standaardiseert het bestandsformaat (vrije Markdown) en de naam, niet een normatief algoritme voor overerving tussen geneste bestanden. Elke harness implementeert nesting anders (tabel 2.2). |
| CLAUDE.md | (H) | [Verified] Claude Code-specifiek. Claude Code leest AGENTS.md sinds v2.1.277 zelfstandig, maar standaard alleen als er geen CLAUDE.md of CLAUDE.local.md in de werkmap of daarboven staat. |
| Agent Skills (`SKILL.md`) | (S) | [Verified] Open specificatie op agentskills.io. Definieert de inhoud van een skill-directory: verplicht `name` (max. 64 tekens, kleine letters, cijfers, koppeltekens, gelijk aan directorynaam) en `description` (max. 1024 tekens); optioneel `license`, `compatibility`, `metadata` (string-naar-string) en `allowed-tools` (experimenteel). Optionele submappen `scripts/`, `references/`, `assets/`. [Verified] De specificatie legt niet vast waar skills staan. |
| `.agents/skills/` | (C) | [Verified] De implementatiegids van agentskills.io noemt `.agents/skills/` een breed geadopteerde conventie voor uitwisseling tussen clients en noemt het scannen van bovenliggende directories tot de Git-root als optie voor monorepos. |
| MCP | (S) | [Verified] Onder AAIF-beheer. [Verified] Claude Code ondersteunt protocolrevisie 2026-07-28. MCP standaardiseert server, tools, resources en prompts; niet het configuratiebestand van de client. |
| MCP-clientconfiguratie | (H) | [Verified] Elk harness heeft een eigen bestand en formaat: `.mcp.json` (Claude Code), `opencode.json` (OpenCode), `.codex/config.toml` (Codex). [Inferred] VS Code gebruikt `.vscode/mcp.json` en Cursor `.cursor/mcp.json`. |
| Agent-/subagentdefinities | (H) | [Verified] Geen gemeenschappelijk formaat. Claude Code: Markdown met frontmatter; Codex: TOML-bestanden in `.codex/agents/` met verplicht `name`, `description`, `developer_instructions`. [Inferred] OpenCode, VS Code en Cursor gebruiken elk een eigen Markdown-variant. |
| Workflow | geen | [Inferred] Er bestaat geen open standaard voor een agentic workflow als afzonderlijk bestandsformaat. Codex en Claude Code noemen skills zelf het middel om herbruikbare werkwijzen vast te leggen. |
| Data-contracten | (S) | [Verified] JSON Schema is een open standaard, los van agentic tooling. |
| Tool-naamgeving | (H) | [Verified] Claude Code prefixeert MCP-tools als `mcp__<server>__<tool>`. [Inferred] Andere harnesses gebruiken andere prefixen; de naam die de MCP-server zelf publiceert is de enige portable naam. |

### 2.2 Ondersteuning per harness

Rules (instructiebestanden):

| Harness | Leest AGENTS.md | Bovenliggende bestanden bij starten in submap | Geneste bestanden onder werkmap |
|---|---|---|---|
| Claude Code | [Verified] Ja, v2.1.277+, alleen zonder CLAUDE.md op het pad | [Verified] Ja, alle AGENTS.md van werkmap tot root, samengevoegd | [Verified] Ja, zodra het Model een bestand in die submap leest |
| Codex | [Verified] Ja | [Verified] Ja, van projectroot (meestal Git-root) naar werkmap, één bestand per directory, samengevoegd, max. 32 KiB standaard | [Verified] Nee, zoeken stopt bij de werkmap |
| OpenCode | [Verified] Ja; CLAUDE.md alleen als terugval | [Speculative] Documentatie zegt dat OpenCode omhoog zoekt en dat "de eerste match per categorie wint"; onduidelijk of daarmee ook de root-AGENTS.md wordt geladen als de wiki-map een eigen AGENTS.md heeft | [Speculative] Niet gedocumenteerd. [Verified] Aanvullende bestanden kunnen expliciet via `instructions` in `opencode.json` (ook met globs) |
| VS Code/Copilot | [Verified] Ja | [Verified] Alleen met instelling `chat.useCustomizationsInParentRepositories`; dan worden alle customization-typen tussen werkmap en Git-root verzameld | [Verified] Met `chat.useNestedAgentsMdFiles` (standaard uit) worden geneste AGENTS.md als paden aangeboden; het Model kiest |
| Cursor | [Verified] Ja, root en submappen; geneste bestanden worden gecombineerd met bovenliggende, specifiekste wint | [Speculative] Niet gedocumenteerd voor het openen van een submap | [Verified] Ja |

Skills:

| Harness | Project-locaties | Bovenliggende directories | Naamconflicten |
|---|---|---|---|
| Claude Code | [Verified] `.claude/skills/` | [Verified] Werkmap en alle ouders tot repository-root; geneste `.claude/skills/` onder de werkmap laden bij eerste bestandstoegang | [Verified] Root en genest blijven beide beschikbaar; geneste variant krijgt gekwalificeerde naam zoals `/apps/web:deploy`. [Verified] Leest niets onder `.agents/`. [Verified] Een skill-map mag een symlink zijn; hetzelfde doel wordt één keer geladen |
| Codex | [Verified] `.agents/skills/` | [Verified] Werkmap tot repository-root | [Verified] Niet samengevoegd; beide verschijnen in selectors |
| OpenCode | [Verified] `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` | [Verified] Omhoog tot de Git-worktree | [Verified] Namen moeten uniek zijn over alle locaties |
| VS Code/Copilot | [Verified] `.github/skills/`, `.claude/skills/`, `.agents/skills/`, plus `chat.agentSkillsLocations` | [Verified] Via `chat.useCustomizationsInParentRepositories` | [Speculative] Niet gedocumenteerd |
| Cursor | [Verified] `.agents/skills/`, `.cursor/skills/`, plus `.claude/skills/` en `.codex/skills/` voor compatibiliteit | [Verified] Geneste `.agents/skills/` overal in de repository worden gevonden en automatisch beperkt tot bestanden in die directory. [Speculative] Openen van alleen een submap niet gedocumenteerd | [Speculative] Niet gedocumenteerd |

Frontmatter buiten de specificatie:

| Veld | Claude Code | VS Code | Cursor | OpenCode | Codex |
|---|---|---|---|---|---|
| `disable-model-invocation` | [Verified] ja | [Verified] ja | [Verified] ja | [Verified] genegeerd (alleen 5 velden herkend) | [Verified] via `agents/openai.yaml` `policy.allow_implicit_invocation: false` |
| `paths` | [Verified] ja | [Speculative] | [Verified] ja | genegeerd | [Speculative] |
| `context: fork`, `agent`, `model` | [Verified] ja | [Speculative] | [Speculative] | genegeerd | [Speculative] |

### 2.3 Kernbevindingen

- **B1.** [Verified] Er is geen project-skilllocatie die alle vijf harnesses lezen. `.agents/skills/` mist Claude Code; `.claude/skills/` mist Codex. [Inferred] Volledige pariteit vereist daarom één canonieke locatie plus een brug voor precies één harness.
- **B2.** [Verified] Alle vijf harnesses lezen AGENTS.md. [Verified] Overerving tussen geneste bestanden verschilt per harness. Een architectuur die op één interpretatie van overerving rust, is niet portable.
- **B3.** [Verified] OpenCode eist unieke skillnamen over alle locaties. [Inferred] Skillnamen vormen daarom in de praktijk één globale naamruimte per sessie; naamgeving moet botsingen voorkomen, niet oplossen.
- **B4.** [Verified] Agentprofielen, MCP-clientconfiguratie, permissies en hooks hebben geen gemeenschappelijk formaat. Deze horen bij de harness als runtime.
- **B5.** [Verified] Claude Code en Codex beschrijven skills als het middel voor herbruikbare werkwijzen en ondersteunen dat een skill delegatie aan subagents voorschrijft. [Inferred] Een Workflow kan portable worden gemodelleerd als skill.
- **B6.** [Verified] VS Code vindt bovenliggende customizations alleen met een instelling. [Speculative] Cursor mogelijk helemaal niet bij het openen van een submap.

---

## 3. Architectuurconcepten

### 3.1 Definities

| Concept | Definitie in deze architectuur | Wie levert het |
|---|---|---|
| **LLM-wiki** | Een zelfstandige eenheid bestaande uit: content (lokale kopie van MediaWiki-pagina's), bronmateriaal, wiki-Rules, wiki-Skills (waaronder Workflows), wiki-schemas, wiki-scripts en een wiki-manifest. Heeft precies één doel-MediaWiki-site. | Repository (K) |
| **Generieke laag (core)** | Alles wat voor elke LLM-wiki geldt: repository-Rules, generieke Skills, de generieke Workflow, generieke schemas en het deterministische Python-pakket (pull, push, validatie, run-State). Kent geen enkele specifieke wiki. | Repository (K) |
| **Wiki-laag** | Domeinspecifieke Rules, Skills, schemas, scripts, content en bronnen van één LLM-wiki. Mag de generieke laag gebruiken, nooit andersom. | Repository (K) |
| **Rules** | Principes, beperkingen en instructies die tijdens uitvoering altijd gelden. Vorm: AGENTS.md. Klein houden; procedures horen in Skills. | Repository (S) |
| **Skill** | Herbruikbare kennis en werkwijze voor één taak, als Agent Skills-directory. Wordt progressief geladen: eerst naam en beschrijving, daarna de instructies, daarna resources. | Repository (S) |
| **Workflow** | Een Skill van het soort `workflow`: beschrijft welke stappen in welke volgorde worden uitgevoerd, welke Skills en Tools per stap worden ingezet, welke artefacten elke stap leest en schrijft, en waar een menselijke gate staat. Geen eigen bestandsformaat. | Repository (K op basis van S) |
| **Agent** | Doelgerichte uitvoeringslogica: het harness laat een Model in een lus Tools aanroepen tot een doel is bereikt. De hoofd-Agent voert de Workflow uit; subagents voeren afgebakende stappen uit in een eigen Context. | Harness + Model |
| **Rol** | Logische verantwoordelijkheid binnen een Workflow, bijvoorbeeld `ingester`, `assessor`, `writer`, `validator`. Portable; beschreven in de Workflow-Skill. | Repository (K) |
| **Agentprofiel** | Harness-specifieke configuratie waarmee een harness een Rol uitvoert: Model, toegestane Tools, permissies, instructies, vooraf geladen Skills. Niet portable. | Harness (H) |
| **Tool** | Concrete functie buiten het Model: bestand lezen, shell-commando, MCP-tool, script. | Harness en MCP-servers |
| **MCP** | Protocol waarmee het harness gestandaardiseerd toegang krijgt tot externe Tools en bronnen, hier de MediaWiki-site. | (S) |
| **Context** | Alle informatie die een Model in één aanroep ziet: systeeminstructies van het harness, Rules, Skill-catalogus, geladen Skills, gespreksgeschiedenis, Tool-resultaten. Vluchtig en per Agent. | Harness |
| **State** | Actuele toestand van de uitvoering: huidige fase, invoer- en uitvoerartefacten, beslissingen, fouten. In deze architectuur persistent op schijf in een run-directory, nooit alleen in Context. | Repository (K) |
| **Artefact** | Een persistent tussenresultaat van een Workflow-stap, gevalideerd tegen een schema. | Repository (K) |
| **Run** | Eén uitvoering van een Workflow, met eigen id en eigen directory. | Repository (K) |
| **Harness** | Runtime die Model, Tools, Context, permissies, discovery, MCP-verbindingen, subagents en gebruikersinterface levert. Voorbeelden: Claude Code, OpenCode, VS Code/Copilot, Cursor, Codex. | Leverancier (H) |
| **Model** | Het LLM. Levert: interpretatie van de Vraag, redeneren, plannen, keuze welke Skill of Tool nodig is, tekstproductie. Levert niet: bestandstoegang, geheugen tussen Sessies, afdwinging van regels. | Leverancier |
| **Sessie** | Interactie in één harness waarin de gebruiker Vragen stelt en één of meer Agents worden ingezet. Een Run kan meerdere Sessies overspannen. | Harness |
| **Vraag / Antwoord** | Opdracht van de gebruiker, bijvoorbeeld "voer gemma-update-wiki uit voor bron X" / reactie van het systeem, bijvoorbeeld een samenvatting van de run en de publish-diff. | — |
| **Resultaat** | Bijgewerkte content in Git en, na de gate, gepubliceerde pagina's op de MediaWiki-site. | — |

### 3.2 Verdeling harness versus Model versus repository

| Verantwoordelijkheid | Repository (portable) | Harness (runtime) | Model |
|---|---|---|---|
| Wat moet er gebeuren | Workflow-Skill | — | — |
| Hoe een taak wordt uitgevoerd | Skill-instructies en scripts | — | Interpretatie en uitvoering |
| Welke Skills bestaan | Directories met `SKILL.md` | Discovery en catalogus in Context | Keuze welke te laden |
| Regels die altijd gelden | AGENTS.md | Laden in Context | Naleven (niet gegarandeerd) |
| Regels die afgedwongen moeten worden | Scripts met harde controles | Permissies, hooks, sandbox | — |
| Toegang tot MediaWiki | Logische operaties in Skills; pull/push-scripts | MCP-serverconfiguratie, credentials, toolnamen | Aanroepen van Tools |
| State | Run-directory met artefacten | — | Lezen en schrijven via Tools |
| Context-beheer | Artefacten klein en gestructureerd houden | Compactie, subagent-isolatie | — |
| Modelkeuze | Niet vastgelegd | Configuratie en Agentprofielen | — |

---

## 4. Alternatieve architecturen

### Model A — volledig onafhankelijk

Elke wiki bevat alle eigen Rules, Skills, Workflows, schemas en scripts. Geen gedeelde laag.

- Voordelen: maximale isolatie; een wiki-map kan als los project worden geopend en werkt in elke harness zonder bovenliggende discovery; eenvoudig te begrijpen per wiki.
- Nadelen: generieke Skills en scripts N keer gedupliceerd; verbeteringen moeten handmatig worden doorgevoerd; drift tussen wiki's is onvermijdelijk. Botst met het principe "geen duplicatie".
- Passend als: er één of twee wiki's zijn, de wiki's inhoudelijk weinig gemeen hebben, of een wiki door een ander team wordt beheerd.

### Model B — generieke core in de repository-root plus wiki's

Generieke Rules en Skills op root-niveau; elke wiki voegt eigen Rules en Skills toe in de eigen map. Discovery via de standaardmechanismen van de harnesses (bovenliggende directories).

- Voordelen: geen duplicatie; sluit direct aan op `.agents/skills/` en AGENTS.md; weinig bestanden.
- Nadelen: afhankelijk van bovenliggende discovery, die per harness verschilt (B2, B6); scripts met relatieve paden breken als vanuit een andere map wordt gestart; core is niet zonder herstructurering naar een andere repository te verplaatsen.
- Passend als: alle gebruikers vanuit de repository-root werken en de core nooit buiten deze repository wordt gebruikt.

### Model C — core als pakket of module

De generieke laag wordt een zelfstandig versioneerbaar pakket (bijvoorbeeld Python-pakket plus skill-pakket of harness-plugin) dat elke wiki als afhankelijkheid installeert.

- Voordelen: expliciete versies en afhankelijkheden; herbruikbaar buiten de repository; scripts werken vanuit elke map.
- Nadelen: [Verified] er bestaat geen harness-onafhankelijk distributieformaat voor skills; Claude Code, Codex en Cursor hebben elk een eigen plugin-formaat. [Inferred] Een skill-pakket vereist daarom een installatie- of kopieerstap per harness en per wiki, dus een adapterlaag. Versie-afstemming binnen één repository voegt ceremonie toe zonder direct probleem op te lossen.
- Passend als: de core daadwerkelijk door andere repositories of teams wordt gebruikt.

### Model D — gelaagde monorepo: standaarden voor Context, pakket voor deterministische logica, gegenereerde harness-bindingen

Combinatie van B en C, gesplitst naar soort functionaliteit:

- LLM-gerichte functionaliteit (Rules, Skills, Workflows) volgt Model B: canoniek in `.agents/skills/` en AGENTS.md op root- en wiki-niveau, discovery via standaardmechanismen.
- Deterministische functionaliteit (pull, push, validatie, run-State, schemas) volgt Model C: één Python-pakket in de repository met een CLI die vanuit elke map werkt.
- Harness-specifieke bindingen (Claude Code-skillbrug, MCP-configuratie per harness, instellingen) worden door één script gegenereerd uit één bron per wiki. Wiki-AGENTS.md verwijst expliciet naar de root-AGENTS.md, zodat overerving niet van één harness-interpretatie afhangt.

- Voordelen: geen duplicatie van domeinlogica; werkt vanuit root en wiki-map; scripts padonafhankelijk; core later als pakket te extraheren zonder Skills te herschrijven; harness-verschillen zijn beperkt tot gegenereerde, controleerbare bestanden.
- Nadelen: één extra script (bindingen genereren en controleren); gebruikers moeten dat script na klonen en na wijziging van skills draaien; gegenereerde bestanden zijn extra bestanden in de repository.
- Passend als: meerdere wiki's, meerdere harnesses met pariteitseis, vaker werken vanuit een wiki-map, en mogelijk later hergebruik van de core. Dat is de situatie uit het interview.

### Vergelijking

| Criterium | A | B | C | D |
|---|---|---|---|---|
| Harness-portability | Hoog per wiki | Middel: afhankelijk van bovenliggende discovery | Laag tot middel: plugin-formaten verschillen | Hoog: één brug, expliciete verwijzingen |
| Eenvoud | Hoog per wiki, laag voor het geheel | Hoog | Laag | Middel |
| Hergebruik | Geen | Binnen repository | Binnen en buiten repository | Binnen repository; buiten na extractie van pakket |
| Onderhoudbaarheid | Laag bij meer dan 2 wiki's | Middel | Middel: versiebeheer | Hoog |
| Skill-discovery | Triviaal | Harness-afhankelijk | Per harness installatie | Standaard plus één gegenereerde brug |
| Workflow-compositie | Binnen wiki | Generiek plus specifiek via namen | Via pakketversies | Generiek plus specifiek via namen en gedeclareerde afhankelijkheden |
| Versiebeheer | Per wiki-map | Eén Git-historie | Pakketversies plus Git | Eén Git-historie; pakketversie optioneel |
| Afhankelijkheden | Impliciet | Impliciet | Expliciet | Expliciet via `metadata` en lint |
| Begrijpelijkheid mens | Hoog per wiki | Hoog | Middel | Hoog, mits README en dit document |
| Begrijpelijkheid Agent | Hoog | Middel: afhankelijk van geladen Rules | Middel | Hoog: expliciete verwijzingen en schemas |

---

## 5. Aanbevolen architectuur: Model D

### 5.1 Conceptueel model

```text
                 Gebruiker  --Vraag-->  Sessie  <--Antwoord--
                                          |
+-----------------------------------------v------------------------------------------+
| HARNESS (runtime, niet portable)                                                    |
|  Model-keuze | Context-beheer | discovery | permissies | hooks | subagents | MCP-client|
+------------+--------------------------+------------------------+-------------------+
             | laadt                    | laadt                  | verbindt
             v                          v                        v
+------------------------+  +--------------------------+  +---------------------------+
| RULES                  |  | SKILLS                   |  | TOOLS                     |
| AGENTS.md (repo)       |  | generiek  .agents/skills |  | shell, bestanden          |
| AGENTS.md (wiki)       |  | wiki      .agents/skills |  | llmwiki-CLI (determinist.)|
+------------------------+  |  - capability-skills     |  | MCP: mediawiki-server     |
                            |  - workflow-skills       |  +-------------+-------------+
                            +------------+-------------+                |
                                         | lezen/schrijven              |
                                         v                              v
                            +--------------------------+   +--------------------------+
                            | STATE                    |   | EXTERN                   |
                            | runs/<id>/  artefacten   |   | MediaWiki-site           |
                            | (gevalideerd, schemas)   |   | (alleen via gate)        |
                            +------------+-------------+   +--------------------------+
                                         |
                                         v
                            +--------------------------+
                            | RESULTAAT                |
                            | content/ in Git          |
                            | gepubliceerde pagina's   |
                            +--------------------------+
```

### 5.2 Concepten en verantwoordelijkheden

| Concept | Verantwoordelijk voor | Niet verantwoordelijk voor | Vorm |
|---|---|---|---|
| Repository-Rules | Structuur, veiligheidsregels, artefactconventies, verwijzing naar deze architectuur | Domeinkennis, procedures | `AGENTS.md` in root, max. circa 100 regels |
| Wiki-Rules | Domein, taal, stijl, naamgeving, wiki-specifieke verboden | Generieke regels herhalen | `wikis/<key>/AGENTS.md` |
| Capability-Skill | Eén taak goed uitvoeren; eigen scripts en references | Volgorde van stappen, publiceren | `.agents/skills/<naam>/SKILL.md` |
| Workflow-Skill | Volgorde, gates, artefact-overdracht, Rol-toewijzing | Inhoudelijke uitvoering van een stap | `.agents/skills/<naam>/SKILL.md` met `metadata.kind: workflow` |
| llmwiki-CLI | Deterministische operaties: pull, push, run-State, schemavalidatie, bestandsnaam-mapping, bindingen genereren | Inhoudelijke beoordeling | Python-pakket `src/llmwiki/` |
| Schemas | Contract tussen stappen en tussen Agents | Inhoudelijke kwaliteit | JSON Schema 2020-12 |
| Wiki-manifest | Eén bron voor site-URL, namespaces, MCP-server, publicatie-instellingen, uitbreidingspunten | Instructies voor het Model | `wikis/<key>/wiki.yaml` |
| Harness-bindingen | Discovery-brug, MCP-clientconfig, instellingen, optionele Agentprofielen | Domeinlogica | Gegenereerd door `llmwiki harness sync` |
| Run-directory | State en artefacten van één Run | Eindresultaat | `wikis/<key>/.work/runs/<run-id>/`, gitignored |

### 5.3 Repositorystructuur

```text
llm-wikis/                                  Git-root
├── AGENTS.md                               repository-Rules (S)
├── ARCHITECTURE.md                         dit document
├── README.md                               installatie en gebruik voor mensen
├── pyproject.toml                          Python-pakket llmwiki + CLI (K)
├── uv.lock
├── .gitattributes                          regeleinden en binaire bestanden
├── .gitignore
├── .editorconfig
├── .agents/
│   └── skills/                             generieke Skills, canoniek (C)
│       ├── wiki-ingest/
│       │   └── SKILL.md
│       ├── wiki-assess/
│       │   ├── SKILL.md
│       │   └── references/criteria.md
│       ├── wiki-write/
│       │   ├── SKILL.md
│       │   └── references/wikitext-style.md
│       ├── wiki-validate/
│       │   └── SKILL.md
│       ├── wiki-publish/
│       │   └── SKILL.md
│       └── wiki-update/                    generieke Workflow-Skill
│           └── SKILL.md
├── src/
│   └── llmwiki/                            deterministische core (K)
│       ├── __init__.py
│       ├── cli.py                          llmwiki pull|push|run|validate|harness
│       ├── sync.py                         pywikibot pull/push
│       ├── titles.py                       paginatitel <-> bestandsnaam
│       ├── runs.py                         run-State
│       ├── harness.py                      bindingen genereren/controleren
│       └── schemas/                        generieke schemas (S)
│           ├── source.schema.json
│           ├── assessment.schema.json
│           ├── changeset.schema.json
│           ├── validation-report.schema.json
│           ├── publish-plan.schema.json
│           ├── page-meta.schema.json
│           └── run-state.schema.json
├── tests/
├── wikis/
│   ├── _template/                          sjabloon voor een nieuwe wiki
│   └── gemma/                              één LLM-wiki
│       ├── AGENTS.md                       wiki-Rules (S)
│       ├── README.md
│       ├── wiki.yaml                       wiki-manifest (K)
│       ├── content/                        wikitext + metadata (Resultaat, in Git)
│       │   ├── main/
│       │   │   ├── Gemeentelijk_gegevenslandschap.wiki
│       │   │   └── Gemeentelijk_gegevenslandschap.meta.json
│       │   └── template/
│       ├── sources/                        bronmateriaal (in Git, grote binaire bestanden via LFS)
│       ├── schemas/                        wiki-specifieke schemas, alleen indien nodig
│       │   └── bedrijfsobject.schema.json
│       ├── scripts/                        wiki-specifieke deterministische logica
│       │   └── check_archimate.py
│       ├── .agents/
│       │   └── skills/                     wiki-Skills, canoniek (C)
│       │       ├── gemma-bo/
│       │       ├── gemma-archimate/
│       │       └── gemma-update-wiki/      wiki-Workflow-Skill
│       ├── .work/                          run-State, gitignored
│       │   └── runs/<run-id>/
│       ├── .mcp.json                       gegenereerd (H: Claude Code)
│       ├── opencode.json                   gegenereerd (H: OpenCode)
│       ├── .codex/config.toml              gegenereerd (H: Codex)
│       ├── .vscode/mcp.json                gegenereerd (H: VS Code)
│       ├── .vscode/settings.json           gegenereerd (H: VS Code)
│       ├── .cursor/mcp.json                gegenereerd (H: Cursor)
│       └── .claude/skills/                 gegenereerde brug, gitignored (H: Claude Code)
├── .claude/
│   ├── settings.json                       permissies repository-breed (H)
│   └── skills/                             gegenereerde brug, gitignored (H)
├── opencode.json                           (H) root-sessies
├── .codex/config.toml                      (H) root-sessies
├── .vscode/settings.json                   (H)
└── .cursor/                                (H) alleen indien nodig
```

Toelichting op keuzes:

- `wikis/<key>/` in plaats van `wiki-<key>/` op root-niveau: alle wiki's zijn met één glob (`wikis/*/`) te vinden door scripts, lint en OpenCode-`instructions`; de root blijft overzichtelijk. De werkmap wordt `cd wikis/gemma`.
- Generieke Skills staan in de root-`.agents/skills/`, niet in `core/.agents/skills/`: [Verified] Codex, OpenCode en Cursor vinden skills alleen in `.agents/skills/` van de werkmap of een bovenliggende map; een map `core/` ligt niet op het pad van `wikis/gemma` naar de root.
- Het Python-pakket staat in `src/llmwiki/`: installeerbaar met `uv sync`, CLI `llmwiki` werkt vanuit elke map. [Inferred] `uv run` vindt vanuit `wikis/gemma` de `pyproject.toml` in de root door omhoog te zoeken.
- Schemas zitten in het pakket: Skills verwijzen naar `llmwiki schema show <naam>` of `llmwiki validate`, niet naar een relatief pad buiten de skill-directory. [Verified] De specificatie beveelt verwijzingen relatief aan de skill-root aan; een pad naar `../../src/...` zou de skill aan deze repository binden.
- Er is geen aparte map voor "knowledge". Kennis die het product is, staat in `content/`. Kennis die een Skill nodig heeft om zijn taak te doen (bijvoorbeeld het GEMMA-metamodel), staat in `references/` van die Skill en wordt progressief geladen.
- Er is geen map `agents/` met Agentprofielen. Zie 5.9.

### 5.4 Afhankelijkheidsrichting

```text
 wiki-Workflow (gemma-update-wiki)
        │ gebruikt
        ├──────────────► generieke Workflow (wiki-update)
        │                        │ gebruikt
        │                        ├──► generieke Skills (wiki-ingest ... wiki-publish)
        │                        │            │ roepen aan
        │                        │            └──► llmwiki-CLI  ──► pywikibot ──► MediaWiki
        │                        └──► Rollen (logisch)
        ├──────────────► wiki-Skills (gemma-bo, gemma-archimate)
        │                        └──► wiki-scripts, wiki-schemas
        └──► logische MediaWiki-operaties ──► MCP-server "mediawiki" (via harness)

 Rules:   wiki-AGENTS.md ──verwijst naar──► repository-AGENTS.md
 Harness-bindingen ──gegenereerd uit──► wiki.yaml + .agents/skills (nooit andersom)
```

Regels voor afhankelijkheden:

1. De generieke laag verwijst nooit naar een wiki-key, wiki-pad, wiki-Skill of domeinterm. Controle: `llmwiki lint` zoekt in `.agents/skills/` en `src/llmwiki/` naar `wikis/`, bekende wiki-keys en naar skillnamen met een wiki-prefix, en faalt bij een treffer.
2. Een wiki verwijst naar generieke Skills alleen bij naam, nooit via een pad in de root-map.
3. Wiki's verwijzen niet naar elkaar. Gedeeld gedrag verhuist naar de generieke laag.
4. Skills en Workflows noemen geen harness-specifieke Tool-namen, bestandslocaties of commando's (5.10).
5. Harness-bindingen zijn afgeleid. Geen enkele portable file leest een harness-bestand.
6. Afhankelijkheden worden gedeclareerd in de `metadata` van `SKILL.md` (standaardveld, string-naar-string):

```yaml
metadata:
  kind: workflow                   # capability | workflow
  scope: wiki                      # core | wiki
  requires-skills: "wiki-update gemma-bo gemma-archimate"
  requires-tools: "llmwiki mcp:mediawiki"
  reads: "source"
  writes: "assessment changeset"
```

[Verified] `metadata` is onderdeel van de specificatie en wordt door OpenCode, Cursor en Claude Code geaccepteerd. `llmwiki lint` controleert dat elke naam in `requires-skills` bestaat en binnen de toegestane richting valt.

### 5.5 Portable versus harness-specifiek

| Onderdeel | Portable (repository) | Harness-specifiek | Classificatie |
|---|---|---|---|
| Rules | `AGENTS.md` root en wiki | Geen `CLAUDE.md` (zie 5.6) | S |
| Skills en Workflows | `.agents/skills/*/SKILL.md` met alleen specificatievelden plus `metadata` | Claude Code-brug `.claude/skills/`; optioneel `agents/openai.yaml` binnen een skill voor Codex-invocatiebeleid | C + H |
| Invocatiebeleid PUBLISH | Tekst in skill: "alleen op expliciete opdracht" | `disable-model-invocation: true` (Claude Code, VS Code, Cursor); `policy.allow_implicit_invocation: false` (Codex) | H |
| Publicatiegate | `llmwiki publish apply` vereist interactieve bevestiging | Permissieregels die `publish apply` voor de Agent blokkeren | K + H |
| MediaWiki-toegang | Logische operaties in skills; `wiki.yaml` beschrijft de server | `.mcp.json`, `opencode.json`, `.codex/config.toml`, `.vscode/mcp.json`, `.cursor/mcp.json` | S + H |
| Credentials | Namen van omgevingsvariabelen in `wiki.yaml` | Waarden in gebruikersomgeving of gitignored `.env` | H |
| Rollen | Beschreven in Workflow-Skill | Agentprofielen (optioneel) | K + H |
| Modelkeuze | Niet vastgelegd | Harness-instelling of Agentprofiel | H |
| State | `.work/runs/` | — | K |
| Schemas | JSON Schema in pakket en wiki | — | S |

### 5.6 Discovery van Rules

Inhoud:

- Root-`AGENTS.md`: repository-opbouw (verwijzing naar dit document), de Workflow-conventie (artefacten, run-directory), veiligheid (nooit publiceren zonder gate, nooit credentials in bestanden), hoe `llmwiki` wordt aangeroepen, dat generieke Skills geen wiki-kennis mogen bevatten. Geen domeinkennis.
- Wiki-`AGENTS.md`: begint met een expliciete verwijzing, daarna domein, taal, stijl, doelgroep, naamgevingsconventies, verboden constructies, welke Workflow-Skill de standaard is.

```markdown
# GEMMA-wiki

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de Context staan: lees dat bestand voordat je iets wijzigt.

## Domein
...
## Standaard Workflow
Gebruik skill `gemma-update-wiki` voor het bijwerken van pagina's.
```

Waarom deze vorm:

- [Verified] Alle vijf harnesses lezen AGENTS.md; het is de enige instructielocatie die overal werkt.
- [Verified] Claude Code en Codex voegen root- en wiki-AGENTS.md samen bij starten in de wiki-map; Cursor combineert geneste bestanden; VS Code doet dat met `chat.useCustomizationsInParentRepositories`. [Speculative] OpenCode laadt mogelijk alleen de dichtstbijzijnde. De expliciete verwijzing in de eerste regel maakt het resultaat onafhankelijk van die verschillen: in het slechtste geval leest het Model de root-Rules via een Tool-aanroep. Voor OpenCode wordt de verwijzing daarnaast deterministisch gemaakt via `instructions` in de gegenereerde `wikis/<key>/opencode.json` (5.16).
- Aparte wiki-rulebestanden (zoals `.claude/rules/` of `.cursor/rules/*.mdc`) worden niet gebruikt: [Verified] ze zijn harness-specifiek, en de extra functie (padgebonden activering) wordt al gedekt door wiki-Skills met progressieve disclosure.
- Er komt geen `CLAUDE.md`. [Verified] Zodra een CLAUDE.md of CLAUDE.local.md in de werkmap of daarboven staat, leest Claude Code AGENTS.md standaard niet meer. Een lokale CLAUDE.local.md van één gebruiker zou dus de wiki-Rules uitschakelen. `llmwiki harness check` meldt het bestaan van zulke bestanden. Terugval voor Claude Code-versies ouder dan v2.1.277: een CLAUDE.md naast elke AGENTS.md met alleen `@AGENTS.md`; [Verified] Claude Code leest het geïmporteerde bestand dan niet dubbel.
- Omvang: Rules blijven klein. [Verified] Codex kapt samengevoegde AGENTS.md-inhoud standaard af bij 32 KiB; Claude Code adviseert minder dan 200 regels per bestand.

Rangorde bij tegenstrijdigheid, vastgelegd in de root-AGENTS.md: repository-veiligheidsregels > wiki-Rules > Skill-instructies > Vraag van de gebruiker voor zover die de gate raakt. [Inferred] Geen harness dwingt deze rangorde technisch af; daarom zijn de regels die er echt toe doen (publiceren) ook in code afgedwongen (5.13).

### 5.7 Discovery van Skills

**Canonieke locatie.** `.agents/skills/` in de root (generiek) en in `wikis/<key>/` (wiki-specifiek).

[Verified] Codex, OpenCode, VS Code en Cursor lezen deze locatie. [Verified] Claude Code niet.

**Brug voor Claude Code.** `llmwiki harness sync` maakt voor elke skill in een canonieke `.agents/skills/` een ingang in de naastgelegen `.claude/skills/`, in deze volgorde van voorkeur:

1. Symlink naar de skill-directory (Linux, macOS, Windows met Developer Mode).
2. Directory junction op Windows zonder Developer Mode. [Inferred] Junctions vereisen geen extra rechten; [Speculative] of Claude Code een junction als symlink behandelt, moet worden geverifieerd.
3. Kopie, met een `.bridge-source`-bestand dat de bron en een hash vastlegt. `llmwiki harness check` meldt verouderde kopieën.

De brugmappen staan in `.gitignore`. Er staan dus nooit symlinks in Git, wat [Verified] het Windows-probleem met `core.symlinks` vermijdt.

Waarom niet andersom (canoniek in `.claude/skills/`, brug voor Codex): beide richtingen vereisen één brug. `.agents/skills/` is leverancier-neutraal, wordt door agentskills.io aanbevolen en door vier van de vijf harnesses gelezen. [Verified] Claude Code documenteert expliciet ondersteuning voor symlinked skill-mappen en laadt één doel maar één keer.

Waarom geen Claude Code-plugin als brug: [Verified] een skills-directory-plugin laadt alleen vanuit de primaire werkmap en niet vanuit bovenliggende mappen; skills krijgen dan een plugin-prefix (`/plugin:skill`), zodat de naam in Claude Code afwijkt van de naam in de andere harnesses. Dat breekt pariteit.

Neveneffect: OpenCode, VS Code en Cursor lezen ook `.claude/skills/` en zien elke skill dan twee keer met identieke inhoud. [Verified] OpenCode verlangt unieke namen. Maatregelen:
- OpenCode: `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` in de omgeving van de gebruiker. [Verified] Deze variabele schakelt alleen het lezen van `.claude/skills` uit.
- VS Code en Cursor: [Speculative] gedrag bij identieke duplicaten niet gedocumenteerd; [Verified] de agentskills.io-gids adviseert clients om bij botsingen deterministisch één variant te kiezen. Verificatie in sectie 8. Als duplicaten problemen geven: de brug alleen aanmaken met `llmwiki harness sync --only claude` op machines waar Claude Code wordt gebruikt, en in VS Code `chat.agentSkillsLocations` beperken.

**Discovery per werkmap.**

| Werkmap | Claude Code | Codex | OpenCode | VS Code | Cursor |
|---|---|---|---|---|---|
| `wikis/gemma` | [Verified] root- en wiki-brug via ouderdirectories | [Verified] root- en wiki-`.agents/skills` | [Verified] beide, omhoog tot Git-root | [Verified] beide met `chat.useCustomizationsInParentRepositories: true` in de gegenereerde `wikis/gemma/.vscode/settings.json` | [Speculative] alleen wiki-skills; zie 5.14 |
| repository-root | [Verified] generieke skills direct; wiki-skills pas na lezen van een bestand in die wiki, met gekwalificeerde naam bij botsing | [Verified] alleen generieke | [Verified] alleen generieke | [Speculative] alleen generieke | [Verified] generieke overal; wiki-skills beperkt tot bestanden in die wiki |

[Inferred] Vanuit de root lekken wiki-Skills dus niet naar andere wiki's: de meeste harnesses laden ze niet, en Cursor en Claude Code beperken ze tot de betreffende directory.

**Naamgeving, precedence en conflicten.**

- Generieke Skills: prefix `wiki-` (`wiki-ingest`, `wiki-assess`, `wiki-write`, `wiki-validate`, `wiki-publish`, `wiki-update`).
- Wiki-Skills: prefix met de wiki-key (`gemma-bo`, `gemma-archimate`, `gemma-update-wiki`).
- Overschrijven van een generieke Skill door een wiki-Skill met dezelfde naam is verboden. [Verified] Precedence verschilt per harness (Claude Code kwalificeert, Codex toont beide, OpenCode eist uniciteit); naamgelijkheid geeft dus per harness ander gedrag. Een wiki die een generieke stap anders wil, maakt een eigen Skill met eigen naam en verwijst daarnaar vanuit de wiki-Workflow.
- `llmwiki lint` controleert: uniciteit over root en alle wiki's, prefixregels, `name` gelijk aan directorynaam, alleen toegestane frontmattervelden, `SKILL.md` korter dan 500 regels. [Verified] De specificatie levert daarnaast `skills-ref validate`.

**Frontmatter.** Portable Skills gebruiken alleen `name`, `description`, `license`, `compatibility`, `metadata`. Uitzonderingen alleen voor side-effect-Skills (`wiki-publish`): `disable-model-invocation: true` plus `agents/openai.yaml` met `allow_implicit_invocation: false`. [Verified] OpenCode negeert onbekende velden; [Verified] Claude Code accepteert specificatievelden zonder aanpassing. Deze twee uitzonderingen zijn harness-annotaties die andere harnesses negeren; de werkelijke bescherming zit in de gate (5.13).

**Skill of Workflow-stap?** Iets wordt een eigen Skill als aan minstens één voorwaarde is voldaan:
- het is herbruikbaar in meer dan één Workflow of meer dan één wiki;
- het vereist eigen references of scripts die niet altijd in Context horen;
- het moet los kunnen worden aangeroepen of getest.

Anders blijft het een stap in de Workflow-Skill. Voorbeeld: "commit-bericht opstellen na validatie" is een zin in `wiki-update`, geen Skill.

### 5.8 Workflows: generiek en specifiek combineren

**Een Workflow is een Skill** met `metadata.kind: workflow`. Dit is een eigen keuze (K) op basis van een standaard (S): er is geen Workflow-standaard (2.1). [Verified] Claude Code, Codex, VS Code en Cursor laden Skills zowel expliciet (slash-commando, `$naam` in Codex) als op basis van de beschrijving; [Verified] OpenCode laadt ze via de `skill`-Tool op basis van naam en beschrijving. Een Workflow-Skill bevat geen uitvoeringskennis van de stappen zelf; die zit in de capability-Skills.

**Generieke Workflow `wiki-update`** definieert:

```text
INGEST → ASSESS → WRITE → VALIDATE → [GATE] → PUBLISH
```

per fase: Rol, te laden Skill, invoerartefact, uitvoerartefact, schema, stopcriterium, en een **uitbreidingspunt** dat de wiki mag vullen.

Voorbeeld (verkort):

```markdown
---
name: wiki-update
description: Werk pagina's van een LLM-wiki bij op basis van nieuw bronmateriaal via INGEST, ASSESS, WRITE, VALIDATE en een menselijke gate voor PUBLISH. Gebruik wanneer de gebruiker vraagt een wiki bij te werken of een bron te verwerken.
metadata:
  kind: workflow
  scope: core
  requires-skills: "wiki-ingest wiki-assess wiki-write wiki-validate wiki-publish"
  requires-tools: "llmwiki"
---

# Workflow wiki-update

Werkmap: de wiki-directory (bevat `wiki.yaml`). Bepaal die eerst.

## Run starten of hervatten
1. `llmwiki run start --workflow <naam-van-aanroepende-workflow>` of `llmwiki run resume <run-id>`.
2. `llmwiki run status` geeft de eerstvolgende fase. Voer alleen die fase uit.

## Fasen
| Fase | Rol | Skill | Leest | Schrijft |
|---|---|---|---|---|
| INGEST | ingester | wiki-ingest | bron(nen) | sources.json |
| ASSESS | assessor | wiki-assess | sources.json, content/ | assessment.json |
| WRITE | writer | wiki-write | assessment.json | changeset/ + changeset.json |
| VALIDATE | validator | wiki-validate | changeset.json | validation-report.json |
| PUBLISH | (mens) | wiki-publish | validation-report.json | publish-plan.json |

Na elke fase: `llmwiki run complete <fase>`; dit valideert het artefact tegen het schema en weigert bij fouten.

## Uitbreidingspunten
Een wiki-Workflow mag per fase aanvullende Skills en controles opgeven. Voer die uit binnen dezelfde fase, na de generieke Skill.

## Delegatie
Als het harness subagents ondersteunt: voer INGEST, ASSESS en VALIDATE elk uit in een aparte subagent met als opdracht "laad skill <X>, lees <artefact>, schrijf <artefact>". Geef geen gespreksgeschiedenis mee; alleen run-id en artefactpaden.

## Gate
Publiceer nooit zelf. Na VALIDATE: draai `llmwiki publish plan`, toon de samenvatting, en geef de gebruiker het commando `llmwiki publish apply <run-id>` om zelf uit te voeren.
```

**Wiki-Workflow `gemma-update-wiki`** is dun en verwijst:

```markdown
---
name: gemma-update-wiki
description: Werk de GEMMA-wiki bij op basis van nieuw bronmateriaal, inclusief bedrijfsobject- en ArchiMate-controles. Gebruik voor elke inhoudelijke wijziging van GEMMA-pagina's.
metadata:
  kind: workflow
  scope: wiki
  requires-skills: "wiki-update gemma-bo gemma-archimate"
  requires-tools: "llmwiki mcp:mediawiki"
---

# Workflow gemma-update-wiki

Volg skill `wiki-update` volledig, met deze uitbreidingen:

| Fase | Aanvulling |
|---|---|
| ASSESS | Laad `gemma-bo`; classificeer elk voorgesteld begrip als bedrijfsobject of niet, volgens `schemas/bedrijfsobject.schema.json`. |
| WRITE | Laad `gemma-archimate` voor pagina's in namespace ArchiMate. |
| VALIDATE | Draai daarnaast `uv run python scripts/check_archimate.py --run <run-id>`. |
```

Deze vorm beantwoordt de compositievraag:
- Generiek gedrag staat één keer in `wiki-update`; de wiki-Workflow herhaalt geen stappen.
- Specifiek gedrag staat in wiki-Skills, aangeroepen op benoemde uitbreidingspunten.
- Afhankelijkheden zijn expliciet in `metadata.requires-skills` en door lint controleerbaar.
- De generieke Workflow kent geen wiki; hij kent alleen het begrip "uitbreidingspunt".

Alternatief overwogen: uitbreidingen declareren in `wiki.yaml` (`extensions.assess: [gemma-bo]`) en de generieke Workflow die lijst laten lezen. Afgewezen voor de eerste versie: de wiki-Workflow-Skill is voor mens en Model direct leesbaar, vergt geen extra configuratietaal en is zelf een aanroepbaar ingangspunt. Overstap naar declaratieve uitbreidingen is pas zinvol als er veel wiki's met identieke uitbreidingspatronen zijn.

**Starten van een Workflow per harness.**

| Harness | Expliciet starten |
|---|---|
| Claude Code | [Verified] `/gemma-update-wiki <bron>` |
| Codex | [Verified] `$gemma-update-wiki` in de prompt of via `/skills` |
| VS Code/Copilot | [Verified] `/gemma-update-wiki` |
| Cursor | [Verified] `/gemma-update-wiki` |
| OpenCode | [Verified] het Model laadt skills via de `skill`-Tool; [Inferred] de Vraag "gebruik skill gemma-update-wiki voor bron X" is voldoende. Optioneel een gegenereerd command-bestand als snelkoppeling (H). |

[Inferred] Een harness-specifiek ingangspunt is dus nergens noodzakelijk; de Skill-naam is het portable ingangspunt.

### 5.9 Agents en subagents

**Onderscheid.** Rol (portable, in de Workflow-Skill) versus Agentprofiel (harness-configuratie). De Rol beschrijft opdracht, invoer, uitvoer en grenzen. Het Agentprofiel bepaalt Model, Tools en permissies.

**Wanneer wat.**

| Situatie | Oplossing |
|---|---|
| Taak past in één Context en heeft geen afwijkende rechten nodig | Skill in de hoofd-Agent |
| Stap produceert veel tussenruis (grote bronnen, veel pagina's lezen) | Subagent met de Skill als opdracht, alleen artefact terug |
| Stappen zijn onafhankelijk (meerdere bronnen ingesten, meerdere pagina's valideren) | Parallelle subagents, elk met eigen artefact |
| Stap moet met andere rechten draaien (alleen-lezen assessor) of een ander Model | Agentprofiel in het harness |
| Onafhankelijke beoordeling gewenst (validator die niet door de writer is beïnvloed) | Subagent zonder gespreksgeschiedenis |

[Verified] Codex waarschuwt dat parallelle schrijvende Agents conflicten veroorzaken en noemt subagents vooral nuttig voor leesintensief werk. Daarom: WRITE draait in één Agent; INGEST, ASSESS-onderzoek en VALIDATE mogen parallel.

**Wat portable is aan een Agent.** Rolnaam, opdracht, invoer- en uitvoerartefact, toegestane logische operaties ("alleen lezen", "geen MediaWiki-schrijfoperaties"). **Wat niet portable is.** Modelnaam, reasoning-niveau, Tool-lijst in harness-syntax, sandbox-modus, permissies, bestandsformaat van het profiel.

**Eerste versie zonder eigen Agentprofielen.** [Verified] Claude Code (`general-purpose`) en Codex (`default`, `worker`, `explorer`) kunnen een ingebouwde subagent starten met een taakomschrijving, en Codex volgt delegatie-instructies uit AGENTS.md of Skills. [Inferred] OpenCode, VS Code en Cursor kunnen dat via hun ingebouwde subagent-Tool. De Workflow-Skill formuleert delegatie in gewone taal. Er is dus geen profielbestand nodig om de Workflow te laten werken.

**Wanneer Agentprofielen toevoegen.** Pas als een concreet probleem optreedt, bijvoorbeeld kosten (goedkoper Model voor INGEST) of veiligheid (assessor zonder schrijfrechten). Dan:
- de Rol staat al in de Workflow-Skill;
- per harness een profielbestand, gegenereerd door `llmwiki harness sync` uit een klein bestand `wikis/<key>/agents.yaml` (of root) met per Rol: beschrijving, verwijzing naar de Skill, `readonly: true|false`, en per harness een optionele modelnaam;
- locaties: [Verified] `.claude/agents/` (Claude Code), `.codex/agents/*.toml` (Codex); [Inferred] `.opencode/agents/` (OpenCode), `.github/agents/*.agent.md` (VS Code), `.cursor/agents/` (Cursor).

Dit is de enige plek waar de architectuur een generator voor Agentprofielen voorziet, en alleen als er meer dan één harness een profiel nodig heeft.

### 5.10 MCP-integratie

**Scheiding.**

| Laag | Bevat | Voorbeeld |
|---|---|---|
| Workflow/Skill (portable) | Wat er met MediaWiki moet gebeuren, als logische operatie | "Lees de actuele versie van de pagina", "zoek pagina's in categorie X" |
| Wiki-manifest (portable) | Welke server een wiki gebruikt, welke site, welke omgevingsvariabelen | `mcp.servers.mediawiki` in `wiki.yaml` |
| Harness-config (gegenereerd) | Clientconfiguratie in harness-formaat | `.mcp.json`, `opencode.json`, `.codex/config.toml`, `.vscode/mcp.json`, `.cursor/mcp.json` |
| Gebruikersomgeving (geheim) | Credentials | `MW_GEMMA_USER`, `MW_GEMMA_PASSWORD` |

**Keuzes.**

1. **MCP per wiki, niet repository-breed.** Elke wiki heeft precies één doel-site. Een per-wiki serverinstantie met die site als vaste standaard voorkomt dat een Agent in de GEMMA-sessie per ongeluk een andere wiki raadpleegt of wijzigt. De serverconfiguratie staat daarom in de wiki-map. Repository-brede MCP-servers (bijvoorbeeld documentatie) mogen in de root-configuratie.
2. **Vaste servernaam `mediawiki` in elke wiki en elk harness.** Skills verwijzen naar "MCP-server `mediawiki`, tool `<naam zoals de server die publiceert>`". [Verified] Claude Code maakt daar `mcp__mediawiki__<tool>` van; [Inferred] andere harnesses gebruiken een eigen prefix. De door de server gepubliceerde naam is gelijk in elk harness; alleen het prefix verschilt. Een Skill noemt daarom nooit de geprefixte naam.
3. **Rolverdeling MCP versus scripts.** MCP voor interactief lezen, zoeken en verkennen tijdens ASSESS en WRITE. Pywikibot via `llmwiki pull/push` voor bulk-synchronisatie en voor publiceren. MCP-schrijfoperaties worden niet gebruikt: publiceren loopt uitsluitend via de gate. Waar de MCP-server dat toestaat, draait hij alleen-lezen; anders blokkeren harness-permissies de schrijf-Tools.
4. **Terugval zonder MCP.** Elke Skill die MCP gebruikt, noemt een terugval via `llmwiki page get <titel>` (leest via pywikibot of lokale content). [Inferred] Daarmee blijft de Workflow uitvoerbaar in een harness of omgeving waar de MCP-server ontbreekt of niet is goedgekeurd.
5. **Meerdere MCP-servers.** Toegestaan per wiki (bijvoorbeeld een ArchiMate-repository voor GEMMA). Elke server staat in `wiki.yaml` en krijgt een vaste naam; `metadata.requires-tools` noemt `mcp:<naam>`.

**`wiki.yaml` (voorbeeld, MCP-deel).**

```yaml
key: gemma
site:
  api: https://www.gemmaonline.nl/w/api.php
  family: gemma
  lang: nl
namespaces: [0, 10, 14]
mcp:
  servers:
    mediawiki:
      command: npx
      args: ["-y", "<mediawiki-mcp-server-pakket>"]
      env:
        MW_API_URL: "${site.api}"
        MW_USERNAME: "env:MW_GEMMA_USER"
        MW_PASSWORD: "env:MW_GEMMA_PASSWORD"
      readonly: true
publish:
  require_tty_confirmation: true
  edit_summary_prefix: "[llm-wiki]"
```

`llmwiki harness sync` vertaalt dit naar de vijf clientformaten, inclusief de per harness verschillende syntax voor omgevingsvariabelen ([Verified] Claude Code `${VAR}` en `${VAR:-default}`; [Inferred] OpenCode `{env:VAR}`, VS Code `${env:VAR}`, Cursor `${env:VAR}`, Codex `env_vars`). [Speculative] Op Windows vereisen sommige clients voor een stdio-server die via `npx` start een `cmd /c`-omweg; de generator neemt dat op basis van het platform mee zodra verificatiepunt V6 dat per harness heeft vastgesteld.

[Verified] Claude Code vraagt goedkeuring voor project-servers uit `.mcp.json`; [Verified] een gekloonde repository kan die goedkeuring niet zelf geven. Dit is een gewenste eigenschap en geen probleem voor de architectuur.

### 5.11 Context en State

**Vergelijking.**

| Criterium | Context doorgeven (één lange Sessie) | Persistente artefacten per fase |
|---|---|---|
| Context-window | Groeit met elke fase; bronnen en paginatekst stapelen op | Elke fase start klein: Rules, één Skill, één artefact |
| Tokengebruik en kosten | Elke beurt betaalt opnieuw voor de volledige geschiedenis | Alleen relevante invoer; hogere vaste kosten per subagent |
| Latency | Geen opstartkosten per fase | Opstartkosten per subagent; parallelisatie compenseert |
| Reproduceerbaarheid | Laag: afhankelijk van gespreksverloop en compactie | Hoog: fase opnieuw uitvoerbaar op hetzelfde artefact |
| Foutisolatie | Fout in ASSESS vervuilt WRITE onzichtbaar | Schemavalidatie stopt de Workflow op de fase-grens |
| Parallelisatie | Niet mogelijk | Per bron of pagina |
| Agentwisseling | Niet mogelijk zonder verlies | Elke fase in elk harness en met elk Model |
| Hervatten | Verloren na afsluiten of compactie | `llmwiki run resume` |
| Git | Niets controleerbaar | Artefacten inspecteerbaar; eindresultaat in Git |

[Verified] Codex beschrijft "context pollution" en "context rot" als reden om ruis naar subagents te verplaatsen; [Verified] Claude Code bewaart geladen Skills na compactie slechts binnen een budget, zodat Skill-instructies uit een lange Sessie kunnen wegvallen. [Inferred] Beide bevestigen dat lange Context-ketens onbetrouwbaar zijn voor meerfasige Workflows.

**Regel.** State en overdracht tussen fasen gaan altijd via artefacten. Context wordt alleen binnen een fase gebruikt. Uitzondering: kleine, interactieve correcties met de gebruiker binnen één fase.

**Run-directory.**

```text
wikis/gemma/.work/runs/2026-09-26T1412-a3f9/
├── state.json                  run-state.schema.json
├── input/                      verwijzingen naar of kopieën van brondocumenten
├── sources.json                source.schema.json          (INGEST)
├── assessment.json             assessment.schema.json      (ASSESS)
├── changeset.json              changeset.schema.json       (WRITE)
├── changeset/                  voorgestelde wikitext per pagina
├── validation-report.json      validation-report.schema.json (VALIDATE)
├── publish-plan.json           publish-plan.schema.json    (PUBLISH plan)
├── publish-plan.diff           leesbare diff voor de mens
└── log.jsonl                   gebeurtenissen per fase (welk harness, welk Model, tijd)
```

`state.json` bevat: workflow-naam, huidige fase, status per fase (`pending|done|failed`), paden en hashes van artefacten, basis-revisies van de betrokken pagina's. `llmwiki run complete <fase>` is de enige manier om een fase af te ronden en valideert het artefact eerst.

**Git.** `.work/` staat in `.gitignore` (interviewkeuze). WRITE schrijft uiteindelijk naar `content/` in de werkboom; de mens beoordeelt met `git diff`; commit gebeurt na VALIDATE en vóór of direct na PUBLISH, met run-id in het commit-bericht. Na PUBLISH haalt `llmwiki pull` de nieuwe revisie-id's op en werkt de `.meta.json`-bestanden bij.

### 5.12 Schemas

**Rol.** Schemas zijn het contract tussen fasen en tussen Agents, onafhankelijk van harness en Model. Ze maken de overdracht deterministisch controleerbaar; het Model hoeft niet te worden vertrouwd op de vorm van zijn uitvoer. [Inferred] Dit is de belangrijkste maatregel voor model-portability: een zwakker Model faalt zichtbaar op de fase-grens in plaats van ongemerkt verderop.

**Generiek (in `src/llmwiki/schemas/`).**

| Schema | Beschrijft | Noodzaak |
|---|---|---|
| `source` | Bron: id, type, locatie, hash, samenvatting, relevante fragmenten | Nodig: invoer voor ASSESS |
| `assessment` | Per voorgestelde wijziging: doelpagina, soort (nieuw, wijzigen, geen actie), motivering, bronverwijzing | Nodig: overdracht naar WRITE |
| `changeset` | Per pagina: titel, bestand, basis-revisie, soort wijziging | Nodig: overdracht naar VALIDATE en PUBLISH |
| `validation-report` | Per controle: resultaat, ernst, pagina | Nodig: gate-invoer |
| `publish-plan` | Exacte lijst van edits met basis-revisie en hash van de nieuwe tekst | Nodig: gate |
| `page-meta` | Sidecar per pagina: titel, pageid, revid, tijdstempel, namespace, contentmodel, categorieën, sha1 | Nodig: conflictdetectie bij push |
| `run-state` | Zie 5.11 | Nodig: hervatten |

**Wiki-specifiek (in `wikis/<key>/schemas/`).** Alleen als er een domeinobject is dat deterministisch moet worden gecontroleerd, bijvoorbeeld `bedrijfsobject.schema.json` voor GEMMA. Een wiki-schema breidt een generiek schema uit via het veld `extensions` dat elk generiek schema als vrij object toestaat, niet door het generieke schema te kopiëren.

**Wanneer geen schema.** Voor vrije tekst (paginatekst zelf), voor tussenstappen binnen één fase, en voor iets dat maar door één script wordt gelezen en geschreven zonder Model ertussen. Een schema dat niet door code wordt gevalideerd, wordt niet toegevoegd.

**Standaard.** JSON Schema draft 2020-12 (S). Validatie met de Python-bibliotheek `jsonschema` via `llmwiki validate <artefact>`.

### 5.13 Scripts en deterministische logica

**Regel.** Alles wat zonder Model kan, gebeurt zonder Model.

| Plaats | Wat | Voorbeelden |
|---|---|---|
| `src/llmwiki/` (repository-breed) | Logica die elke wiki nodig heeft | pull, push, bestandsnaam-mapping, run-State, schemavalidatie, publish plan/apply, lint, harness sync/check |
| `wikis/<key>/scripts/` | Logica die meerdere Skills van één wiki gebruiken | `check_archimate.py` |
| `<skill>/scripts/` | Logica die alleen die Skill gebruikt | parser voor een bronformaat |
| Workflow-Skill | Geen scripts; alleen aanroepvolgorde | — |

**Aanroep.** Generieke logica altijd via de CLI: `uv run llmwiki <commando>`. Wiki- en Skill-scripts via `uv run python <pad>`, met paden relatief aan de wiki-map (waar de Workflow start) respectievelijk aan de skill-directory. [Verified] De specificatie beveelt paden relatief aan de skill-root aan.

**Taal en platform.** Uitsluitend Python (geen Bash of PowerShell) voor alles wat de Workflow aanroept, met `pathlib`, UTF-8 expliciet bij lezen en schrijven, en geen afhankelijkheid van een specifieke shell. [Verified] Claude Code draait op Windows zonder Git Bash commando's via PowerShell; [Inferred] een Python-CLI werkt identiek onder Bash, PowerShell en cmd.

**Publicatiegate (harde eis uit het interview).**

1. `llmwiki publish plan --run <id>`: controleert dat VALIDATE geslaagd is, haalt per pagina de actuele revisie op en vergelijkt met de basis-revisie uit `.meta.json`. Bij afwijking: stop met conflictmelding. Schrijft `publish-plan.json` en `publish-plan.diff` en toont een plan-hash.
2. `llmwiki publish apply --run <id>`: weigert als stdin geen interactieve terminal is; vraagt de mens de eerste 8 tekens van de plan-hash over te typen; controleert opnieuw de basis-revisies; publiceert via pywikibot; schrijft resultaat naar `log.jsonl`.
3. Tweede laag: harness-permissies blokkeren `llmwiki publish apply` voor de Agent (5.15, 5.16).
4. Derde laag: MCP-server alleen-lezen.

[Inferred] Shell-Tools van Agents draaien zonder interactieve terminal, zodat stap 2 ook zonder harness-permissies niet door een Agent kan worden voltooid. [Speculative] Dit moet per harness worden geverifieerd, omdat sommige harnesses een pseudo-terminal kunnen aanbieden; daarom blijft laag 3 nodig.

**Bestandsnamen voor paginatitels (repository-portability).** MediaWiki-titels bevatten tekens die op Windows niet zijn toegestaan (`: / \ * ? " < > |`), kunnen alleen in hoofdlettergebruik verschillen, en kunnen gereserveerde Windows-namen opleveren (`CON`, `NUL`). [Verified] Windows en macOS gebruiken standaard hoofdletterongevoelige bestandssystemen. `llmwiki.titles` bepaalt daarom:

- namespace-map met vaste Engelstalige canonieke naam in kleine letters (`main`, `template`, `category`);
- bestandsnaam: titel met spaties als `_`, verboden tekens percent-gecodeerd, Unicode genormaliseerd naar NFC;
- als twee titels na hoofdletterongevoelige vergelijking gelijk zijn, of de naam gereserveerd of langer dan 120 tekens is: suffix `~<8 tekens hash van exacte titel>`;
- de exacte titel staat altijd in `.meta.json`; de bestandsnaam is nooit de bron van waarheid.

### 5.14 Een wiki als zelfstandig subproject openen

**Gevolgen van de keuze van werkmap.**

| Aspect | Werkmap = repository-root | Werkmap = `wikis/gemma` |
|---|---|---|
| Git | Normaal | [Verified] Normaal; alle harnesses vinden de Git-root door omhoog te zoeken |
| AGENTS.md | Alleen root direct; wiki-Rules pas bij werken in de wiki (Claude Code, Cursor) of niet (Codex) | Root en wiki samengevoegd (Claude Code, Codex); expliciete verwijzing als vangnet |
| Skills | Generiek; wiki-Skills beperkt of niet zichtbaar | Generiek en wiki-specifiek |
| Workflow | Moet de wiki als argument krijgen | Wiki volgt uit werkmap (`wiki.yaml`) |
| Scripts | Paden moeten wiki-map bevatten | CLI vindt `wiki.yaml` in werkmap of daarboven |
| MCP | Alleen repository-brede servers | [Verified] Claude Code leest `.mcp.json` uit de projectroot; [Inferred] dat is de werkmap, dus de wiki-server is beschikbaar |
| Geschikt voor | Onderhoud aan core, werk over meerdere wiki's | Inhoudelijk werk aan één wiki |

**Per harness bij openen van `wikis/gemma`.**

| Harness | Rules | Skills | MCP | Extra nodig |
|---|---|---|---|---|
| Claude Code | [Verified] root + wiki | [Verified] via brug in beide niveaus | [Inferred] `wikis/gemma/.mcp.json` | Brug via `llmwiki harness sync`; v2.1.277+ of CLAUDE.md-terugval |
| Codex | [Verified] root + wiki | [Verified] root + wiki | [Inferred] `wikis/gemma/.codex/config.toml`, alleen in vertrouwd project | Project vertrouwen |
| OpenCode | [Speculative] dichtstbijzijnde; `instructions` voegt root toe | [Verified] root + wiki | [Inferred] `wikis/gemma/opencode.json` | `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` bij aanwezigheid brug |
| VS Code | [Verified] root + wiki met instelling | [Verified] root + wiki met instelling | [Inferred] `wikis/gemma/.vscode/mcp.json` | Gegenereerde `.vscode/settings.json` met `chat.useCustomizationsInParentRepositories: true`, `chat.useAgentsMdFile: true` |
| Cursor | [Speculative] alleen wiki; verwijzing in wiki-AGENTS.md als vangnet | [Speculative] alleen wiki | [Inferred] `wikis/gemma/.cursor/mcp.json` | Zie hieronder |

**Cursor.** [Verified] Cursor vindt geneste `.agents/skills/` en geneste AGENTS.md wanneer de repository-root is geopend, en beperkt ze tot de betreffende directory. Aanbeveling voor Cursor: open de repository-root en werk in bestanden onder `wikis/gemma/`. Als Cursor alleen de wiki-map moet openen en verificatie (sectie 8) bevestigt dat bovenliggende skills dan ontbreken, genereert `llmwiki harness sync --cursor-wiki-root` een brug `wikis/<key>/.cursor/skills/` met ingangen naar de generieke skills. [Verified] `.cursor/skills/` is een Cursor-eigen locatie en wordt door de andere harnesses niet gelezen, dus deze brug veroorzaakt geen duplicaten elders. Dit is de enige plek waar volledige pariteit een tweede brug kan vereisen.

### 5.15 Minimale harness-configuratie voor Claude Code

Bestanden:

| Bestand | Inhoud | In Git |
|---|---|---|
| `AGENTS.md`, `wikis/<key>/AGENTS.md` | Rules (portable) | Ja |
| `.claude/skills/`, `wikis/<key>/.claude/skills/` | Brug naar `.agents/skills/` | Nee |
| `wikis/<key>/.mcp.json` | Gegenereerd uit `wiki.yaml` | Ja |
| `.claude/settings.json` | Permissies | Ja |
| `wikis/<key>/.claude/settings.json` | Permissies voor sessies in de wiki-map | Ja |
| Geen `CLAUDE.md` | — | — |

`wikis/gemma/.mcp.json`:

```json
{
  "mcpServers": {
    "mediawiki": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "<mediawiki-mcp-server-pakket>"],
      "env": {
        "MW_API_URL": "https://www.gemmaonline.nl/w/api.php",
        "MW_USERNAME": "${MW_GEMMA_USER}",
        "MW_PASSWORD": "${MW_GEMMA_PASSWORD}"
      }
    }
  }
}
```

`wikis/gemma/.claude/settings.json` (en dezelfde `deny`-regels in de root):

```json
{
  "permissions": {
    "allow": [
      "Bash(uv run llmwiki run *)",
      "Bash(uv run llmwiki validate *)",
      "Bash(uv run llmwiki publish plan *)",
      "Bash(uv run llmwiki pull *)",
      "Bash(uv run python scripts/*)"
    ],
    "deny": [
      "Bash(uv run llmwiki publish apply*)",
      "Bash(llmwiki publish apply*)",
      "Bash(*pywikibot*)"
    ]
  }
}
```

[Verified] Claude Code-permissieregels worden door de client afgedwongen, ongeacht wat het Model besluit; [Verified] CLAUDE.md-instructies niet. [Inferred] Deny-patronen op shell-commando's zijn omzeilbaar via alternatieve schrijfwijzen; daarom is de TTY-controle in de CLI de primaire gate en deze regel een tweede laag. Namen van eventuele MCP-schrijf-Tools komen als `mcp__mediawiki__<tool>` in `deny`.

[Inferred] Een project-`settings.json` geldt voor de Sessie in de map waarin Claude Code start; daarom staat hij zowel in de root als in elke wiki-map, beide gegenereerd uit één bron.

Optioneel, later: `.claude/agents/<rol>.md` voor Agentprofielen (5.9).

### 5.16 Dezelfde architectuur in OpenCode en andere harnesses

Portable delen (Rules, Skills, Workflows, schemas, CLI, run-State, gate) zijn identiek. Per harness verschilt alleen:

**OpenCode.** `wikis/gemma/opencode.json` (gegenereerd):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["../../AGENTS.md"],
  "mcp": {
    "mediawiki": {
      "type": "local",
      "command": ["npx", "-y", "<mediawiki-mcp-server-pakket>"],
      "environment": {
        "MW_API_URL": "https://www.gemmaonline.nl/w/api.php",
        "MW_USERNAME": "{env:MW_GEMMA_USER}",
        "MW_PASSWORD": "{env:MW_GEMMA_PASSWORD}"
      },
      "enabled": true
    }
  },
  "permission": {
    "bash": {
      "*llmwiki publish apply*": "deny"
    }
  }
}
```

[Verified] `instructions` en `permission.skill` bestaan in `opencode.json`. [Inferred] De vorm van het `mcp`-blok en `permission.bash`; verificatie in sectie 8. Gebruikersomgeving: `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` zolang de Claude Code-brug aanwezig is.

**Codex.** `wikis/gemma/.codex/config.toml` (gegenereerd):

```toml
[mcp_servers.mediawiki]
command = "npx"
args = ["-y", "<mediawiki-mcp-server-pakket>"]
env_vars = ["MW_GEMMA_USER", "MW_GEMMA_PASSWORD"]
env = { MW_API_URL = "https://www.gemmaonline.nl/w/api.php" }
```

In `wiki-publish/agents/openai.yaml`: `policy.allow_implicit_invocation: false`. [Verified] Codex leest skills uit `.agents/skills/` en AGENTS.md zonder verdere configuratie. [Inferred] Veldnamen `env_vars` en `env`; verificatie in sectie 8. De gate rust op de TTY-controle en de Codex-sandbox/goedkeuringsmodus.

**VS Code/Copilot.** `wikis/gemma/.vscode/settings.json`:

```json
{
  "chat.useAgentsMdFile": true,
  "chat.useCustomizationsInParentRepositories": true
}
```

en `wikis/gemma/.vscode/mcp.json` met een `servers`-blok voor `mediawiki`. [Verified] VS Code leest `.agents/skills/` en ondersteunt `disable-model-invocation`.

**Cursor.** `wikis/gemma/.cursor/mcp.json` met `mcpServers.mediawiki`; verder 5.14. [Verified] Cursor leest `.agents/skills/` en AGENTS.md en ondersteunt `disable-model-invocation`.

**Generator.** `llmwiki harness sync` schrijft al deze bestanden uit `wiki.yaml` en de skill-directories; `llmwiki harness check` faalt als een gegenereerd bestand afwijkt van wat de generator zou schrijven, als er een CLAUDE.md op een wiki-pad staat, of als een brug verouderd is. `check` draait in een pre-commit-hook en in CI. Gegenereerde bestanden beginnen, waar het formaat commentaar toestaat, met de regel dat ze gegenereerd zijn en uit welke bron.

Rechtvaardiging van deze adapterlaag tegenover het principe "geen abstractie om de abstractie": zonder generator zouden per wiki vijf MCP-configuraties met dezelfde informatie in vijf syntaxen met de hand worden onderhouden, en zou de Claude Code-brug handmatig moeten worden aangelegd op elk platform. De generator voegt geen nieuw concept toe; hij vertaalt één portable bron naar bestaande harness-formaten, en elk gegenereerd bestand blijft met de hand leesbaar en schrijfbaar.

---

## 6. Portability-analyse

### 6.1 Repository-portability (Linux, Windows, macOS)

| Risico | Maatregel |
|---|---|
| Symlinks in Git | Geen; brug lokaal via symlink, junction of kopie |
| Regeleinden | `.gitattributes`: `* text=auto eol=lf`; binaire bronnen expliciet `binary` |
| Hoofdletterongevoelige bestandssystemen, verboden tekens, gereserveerde namen | Titelmapping met hash-suffix (5.13) |
| Padlengte Windows | Korte mapnamen; `git config core.longpaths true` in README |
| Unicode-normalisatie macOS | NFC bij schrijven van bestandsnamen |
| Shell-verschillen | Alleen Python-CLI; geen shell-scripts in Workflows |
| Python-omgeving | `uv` met lockfile; zelfde versies op elk OS |
| Credentials | Omgevingsvariabelen; geen paden naar gebruikersmappen in Git |
| Grote bronbestanden | Git LFS voor binaire bronnen boven een drempel |

[Inferred] Met deze maatregelen ziet de repository er na `git clone`, `uv sync` en `llmwiki harness sync` op elk OS hetzelfde uit; alleen de gitignored brug verschilt in techniek (symlink, junction of kopie), niet in inhoud.

### 6.2 Harness-portability

Ondersteund door: AGENTS.md (alle vijf), Agent Skills-formaat (alle vijf), `.agents/skills/` (vier van vijf), MCP (alle vijf), Workflow als Skill (alle vijf), artefacten in bestanden (alle vijf), CLI via shell-Tool (alle vijf).

Beperkt door: skill-locatie Claude Code (brug), bovenliggende discovery VS Code (instelling) en Cursor (onbekend), MCP-clientformaten (generator), Agentprofielen (bewust uitgesteld), invocatiebeleid en permissies (harness-annotaties, gate in code).

Definitie van pariteit in deze architectuur: dezelfde Vraag in elk harness laadt dezelfde Rules en Skills, doorloopt dezelfde fasen, produceert artefacten die tegen dezelfde schemas valideren, en stopt bij dezelfde gate. Pariteit in gebruikerservaring (menu's, modelkeuze, snelheid) valt erbuiten.

### 6.3 Model-portability

| Maatregel | Effect |
|---|---|
| Skills in gewone taal, zonder modelspecifieke trefwoorden | Geen afhankelijkheid van één Model |
| Schemavalidatie op elke fase-grens | Fouten van een zwakker Model worden direct zichtbaar |
| Deterministische stappen in code | Minder oppervlak waarop Modellen verschillen |
| Kleine fasen met kleine Context | Werkt ook met Modellen met een kleiner context-window |
| Modelkeuze alleen in harness-config | Wisselen zonder repository-wijziging |
| Evaluaties per Skill | [Verified] agentskills.io beschrijft een eval-aanpak; vergelijk Modellen op dezelfde testgevallen |

[Inferred] De grootste resterende modelafhankelijkheid is de kwaliteit van ASSESS en WRITE; die is niet te standaardiseren, alleen te meten.

---

## 7. Samenvatting van keuzes

| Nr | Keuze | Classificatie |
|---|---|---|
| K1 | Eén Git-repository; wiki's in `wikis/<key>/` | K |
| K2 | Rules alleen in AGENTS.md (root en wiki); wiki-AGENTS.md verwijst expliciet naar root; geen CLAUDE.md | S + K |
| K3 | Skills canoniek in `.agents/skills/` op root- en wiki-niveau | C |
| K4 | Gegenereerde, gitignored brug `.claude/skills/` voor Claude Code | H + K |
| K5 | Skillnamen met prefix (`wiki-`, `<key>-`); overschrijven verboden; uniciteit gecontroleerd | K |
| K6 | Workflow is een Skill met `metadata.kind: workflow`; wiki-Workflow is dun en verwijst naar generieke Workflow plus wiki-Skills op uitbreidingspunten | K op S |
| K7 | Afhankelijkheden in `metadata`; lint bewaakt richting | K op S |
| K8 | Rollen in de Workflow; Agentprofielen pas bij concreet probleem, dan gegenereerd | K + H |
| K9 | MCP per wiki, vaste servernaam, logische operaties in Skills, geen MCP-schrijfoperaties | S + K |
| K10 | State via persistente, schemagevalideerde artefacten in gitignored run-directory | K |
| K11 | JSON Schema voor alle overdrachten; wiki-schemas alleen voor deterministisch te controleren domeinobjecten | S |
| K12 | Deterministische core als Python-pakket met CLI; later extraheerbaar | K |
| K13 | Publicatiegate in code (TTY-bevestiging plus revisiecontrole), aangevuld met harness-permissies | K + H |
| K14 | Eén generator voor alle harness-bindingen, met `check` in pre-commit en CI | K |

---

## 8. Open punten en verificatieprocedure

Punten gemarkeerd als [Speculative] die de architectuur raken:

| Nr | Vraag | Test | Gevolg bij negatief resultaat |
|---|---|---|---|
| V1 | Laadt OpenCode bij starten in `wikis/gemma` ook de root-AGENTS.md? | Vraag in een nieuwe Sessie: "welke instructiebestanden zijn geladen?" | Geen: `instructions` in `opencode.json` dekt dit al |
| V2 | Vindt Cursor bij openen van alleen `wikis/gemma` root-skills en root-AGENTS.md? | Open map, controleer Customize > Skills | Activeer `--cursor-wiki-root`-brug |
| V3 | Behandelt Claude Code een Windows-junction als symlinked skill-map? | `llmwiki harness sync` op Windows zonder Developer Mode, daarna `/skills` | Val terug op kopie |
| V4 | Hoe gaan VS Code en Cursor om met identieke skills in `.agents/skills/` en `.claude/skills/`? | Beide aanwezig, controleer skill-lijst | Brug alleen op Claude Code-machines of VS Code `chat.agentSkillsLocations` beperken |
| V5 | Kan een Agent in een van de harnesses een interactieve TTY krijgen? | Laat de Agent `llmwiki publish apply` proberen in een test-wiki | Laag 2 en 3 van de gate zijn verplicht, niet optioneel |
| V6 | Exacte veldnamen MCP-config OpenCode, Codex, VS Code, Cursor | Generator-uitvoer laden, server moet verbinden | Generator aanpassen |
| V7 | Leest Codex `.codex/config.toml` in de werkmap als die onder de Git-root ligt? | Start Codex in `wikis/gemma`, vraag MCP-status | Config in root plaatsen met server per wiki onder eigen naam |

Pariteitstest per harness (handmatig, per release van een harness of van de core):

1. `llmwiki harness check` slaagt.
2. Start in `wikis/_template` (testwiki tegen een test-MediaWiki). Vraag: "Welke Rules en Skills heb je geladen?" Controleer: root- en wiki-Rules, generieke en wiki-Skills, elke naam één keer.
3. Voer `/<key>-update-wiki` (of `$...`) uit met een vaste testbron.
4. Controleer dat alle artefacten tegen hun schema valideren en dat de Agent stopt bij de gate.
5. Controleer dat een poging van de Agent om `publish apply` uit te voeren faalt.

---

## 9. Invoeringsvolgorde

1. `src/llmwiki`: titelmapping, pull met `.meta.json`, run-State, schemas, validatie, publish plan/apply met gate.
2. Root-AGENTS.md en generieke Skills `wiki-ingest` tot en met `wiki-update`.
3. `wikis/_template` en `wikis/gemma` met AGENTS.md, `wiki.yaml`, content via `llmwiki pull`.
4. `llmwiki harness sync/check` voor Claude Code-brug en MCP-configuratie van de vijf harnesses.
5. Pariteitstest (sectie 8) in alle vijf harnesses; verificatiepunten V1 tot en met V7 afsluiten.
6. GEMMA-Skills `gemma-bo`, `gemma-archimate` en Workflow `gemma-update-wiki`.
7. Agentprofielen alleen als stap 5 of 6 een concreet kosten- of veiligheidsprobleem toont.
8. Extractie van `llmwiki` en de generieke Skills naar een eigen repository alleen als een andere repository ze nodig heeft; de structuur hoeft daarvoor niet te veranderen.

---

## 10. Bronnen

- Agent Skills-specificatie: https://agentskills.io/specification
- Agent Skills, implementatiegids voor clients (discovery, `.agents/skills/`, conflicten, trust): https://agentskills.io/client-implementation/adding-skills-support.md
- Claude Code, geheugen, CLAUDE.md en AGENTS.md: https://code.claude.com/docs/en/memory
- Claude Code, skills: https://code.claude.com/docs/en/skills
- Claude Code, MCP: https://code.claude.com/docs/en/mcp
- Claude Code, plugins laden: https://code.claude.com/docs/en/plugins/loading
- OpenCode, rules: https://opencode.ai/docs/rules/
- OpenCode, agent skills: https://opencode.ai/docs/skills/
- Codex, agent skills: https://developers.openai.com/codex/skills
- Codex, AGENTS.md: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Codex, subagents en custom agents: https://learn.chatgpt.com/docs/agent-configuration/subagents.md
- VS Code, agent skills: https://code.visualstudio.com/docs/copilot/customization/agent-skills
- VS Code, custom instructions en geneste AGENTS.md: https://code.visualstudio.com/docs/agent-customization/custom-instructions
- VS Code, customizations in monorepo: https://code.visualstudio.com/docs/agent-customization/overview
- Cursor, skills: https://cursor.com/docs/skills
- Cursor, rules en AGENTS.md: https://cursor.com/docs/rules
- Linux Foundation, oprichting Agentic AI Foundation: https://www.prnewswire.com/news-releases/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agentsmd-302636897.html
