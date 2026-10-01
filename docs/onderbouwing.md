# Onderbouwing: portable monorepo voor meerdere LLM-wiki's

Peildatum onderzoek: 26 september 2026, bijgewerkt 27 september 2026 met vier use-cases (onboarding, kladblok versus archief, gate-smaken, opsplitsing documentatie). Harness-gedrag verandert snel; sectie 8 bevat een verificatieprocedure.

Dit is het naslagdocument: onderzoek, alternatieven, keuzes en bronnen. Voor dagelijks gebruik zijn er twee kortere documenten:

| Document | Voor wie | Inhoud |
|---|---|---|
| `ARCHITECTURE.md` (Architectuur-Kompas) | Iedereen in het team | Wat een LLM-wiki is, principes, plattegrond, spelregels |
| `docs/kluswijzer.md` | Wie de repository inricht | Vier klussen met begin, taak en eindresultaat |
| `docs/onderbouwing.md` (dit document) | Wie een keuze wil begrijpen of herzien | Waarom het zo is ingericht, met bronnen |

Bij tegenstrijdigheid geldt dit document; het Kompas en de Kluswijzer worden erop bijgewerkt.

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
| Skill-brug | Kopieën vanuit één canonieke bron | Geen symlinks of junctions. Lokale kopieën worden alleen via het script gegenereerd en op bronhash gecontroleerd |
| PUBLISH | Altijd menselijke gate, zonder terminalcodes; per wiki kiesbaar tussen vrijgave via document (smaak A) of via bevestigingswoord in de chat (smaak B); geldt ook voor architectuurmodel-export | Akkoord van de redacteur plus een goedkeuringsklik in het harness (5.13) |
| Tussenresultaten | Kladblok persistent op schijf, niet in Git, na afronding automatisch opgeruimd | Run-directory per wiki, gitignored, met bewaartermijn (5.11) |
| Blijvende vastlegging | Bronverslag en logboek in Git, niet op MediaWiki | Bronverslag in centrale bronindex (5.19); logboek in `log.md` (alle soorten); bij curatie zijn de pagina's zelf ook archief |
| Onboarding | Nieuwe collega werkt binnen enkele minuten, zonder handmatige inrichting | Controle en herstel via `llmwiki workspace-check`, aangestuurd vanuit de root-AGENTS.md (5.17) |
| Hergebruik core | Mogelijk later buiten deze repository | Core moet als pakket extraheerbaar zijn zonder herstructurering |
| Content-opslag | Wikitext per pagina (sync); Markdown met frontmatter (curatie, knowledge-base) | Conflictbasis `revisies.json` (sync) of frontmatter-status (curatie); één formaat per wiki (5.18) |
| Wiki-typen | Naast MediaWiki-sync ook lokale Obsidian-curatie (optioneel met export naar ArchiMate/UML/XMI) en ongestructureerde kennisopbouw | Drie soorten (`sync`/`curation`/`knowledge-base`) in een keten; MediaWiki wordt een optioneel exportdoel; vault = repository-root; pagina's zijn het archief bij curatie; `voortgang.md` gegenereerd bij curatie (5.18) |
| Bronnen | Centraal en gedeeld; alle bronnen als origineel plus Markdown-conversie in Git; per wiki ingedeeld naar onderwerp | Drie lagen `sources/raw`, `sources/index`, `wikis/<key>/bronnen/<onderwerp>/`; scoping via tags; taken starten vanuit een onderwerppagina (5.19) |
| Oplevering | Markdown in de repository: Kompas, Kluswijzer en dit naslagdocument | Drie documenten, zie begin van dit document |

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
| Claude Code | [Verified] `.claude/skills/` | [Verified] Werkmap en alle ouders tot repository-root; geneste `.claude/skills/` onder de werkmap laden bij eerste bestandstoegang | [Verified] Root en genest blijven beide beschikbaar; geneste variant krijgt gekwalificeerde naam zoals `/apps/web:deploy`. [Verified] Leest niets onder `.agents/`. De brug kopieert daarom canonieke skills naar deze locatie |
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
| **LLM-wiki** | Een zelfstandige eenheid bestaande uit: content, wiki-Rules, wiki-Skills (waaronder Workflows), een wiki-manifest en, waar nodig, wiki-schemas en -scripts. Is van soort `sync` (werkkopie van één MediaWiki-site, zonder domein-lens of curatiestatus), `curation` (domein-lens op de centrale bronnen, met pagina's en optionele curatiestatus, optioneel een exportdoel) of `knowledge-base` (ongestructureerde kennisopbouw, geen curatiestatus, geen run/gate); zie 5.18. | Repository (K) |
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
| **Kladblok** | De run-directory met State en artefacten van lopende en recent afgeronde runs. Onzichtbaar voor het team, niet in Git, na afloop opgeruimd. | Repository (K) |
| **Record** | Blijvend verslag van een besluit in Git. Sync: een regel in `log.md` per publicatie, plus de commit. Curatie/knowledge-base: de pagina's zelf plus `log.md`. Nooit door het Model geschreven, altijd afgeleid door de CLI. | Repository (K) |
| **Publicatievoorstel** | Leesbaar Markdown-document per run met samenvatting, wijzigingen en akkoordvelden; basis voor de menselijke gate. | Repository (K) |
| **Harness** | Runtime die Model, Tools, Context, permissies, discovery, MCP-verbindingen, subagents en gebruikersinterface levert. Voorbeelden: Claude Code, OpenCode, VS Code/Copilot, Cursor, Codex. | Leverancier (H) |
| **Model** | Het LLM. Levert: interpretatie van de Vraag, redeneren, plannen, keuze welke Skill of Tool nodig is, tekstproductie. Levert niet: bestandstoegang, geheugen tussen Sessies, afdwinging van regels. | Leverancier |
| **Sessie** | Interactie in één harness waarin de gebruiker Vragen stelt en één of meer Agents worden ingezet. Een Run kan meerdere Sessies overspannen. | Harness |
| **Vraag / Antwoord** | Opdracht van de gebruiker, bijvoorbeeld "werk deze pagina bij met wiki-edit" / reactie van het systeem, bijvoorbeeld een samenvatting van de run en het publicatievoorstel. | — |
| **Resultaat** | Bijgewerkte content en records in Git en, na de gate, gepubliceerde pagina's op de MediaWiki-site of een geëxporteerd architectuurmodel. | — |

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
| Begrijpelijkheid mens | Hoog per wiki | Hoog | Middel | Hoog, mits Kompas en README |
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
                            | STATE (kladblok)         |   | EXTERN                   |
                            | .work/runs/<id>/         |   | MediaWiki-site           |
                            | (gevalideerd, schemas)   |   | architectuurmodel-doel   |
                            +------------+-------------+   | (alleen via gate)        |
                                         |                 +--------------------------+
                                         v
                            +--------------------------+
                            | RESULTAAT                |
                            | content/ (of pagina's)   |
                            | en log.md in Git; na de  |
                            | gate: publicatie/export  |
                            +--------------------------+
```

### 5.2 Concepten en verantwoordelijkheden

| Concept | Verantwoordelijk voor | Niet verantwoordelijk voor | Vorm |
|---|---|---|---|
| Repository-Rules | Structuur, veiligheidsregels, artefactconventies, werkplekcontrole, verwijzing naar het Kompas | Domeinkennis, procedures | `AGENTS.md` in root, max. circa 100 regels |
| Wiki-Rules | Domein, taal, stijl, naamgeving, wiki-specifieke verboden | Generieke regels herhalen | `wikis/<key>/AGENTS.md` |
| Capability-Skill | Eén taak goed uitvoeren; eigen scripts en references | Volgorde van stappen, publiceren | `.agents/skills/<naam>/SKILL.md` |
| Workflow-Skill | Volgorde, gates, artefact-overdracht, Rol-toewijzing | Inhoudelijke uitvoering van een stap | `.agents/skills/<naam>/SKILL.md` met `metadata.kind: workflow` |
| llmwiki-CLI | Deterministische operaties: pull, push, run-State, schemavalidatie, bestandsnaam-mapping, bindingen genereren | Inhoudelijke beoordeling | Python-pakket `tools/llmwiki/` |
| Schemas | Contract tussen stappen en tussen Agents | Inhoudelijke kwaliteit | JSON Schema 2020-12 |
| Wiki-manifest | Eén bron voor site-URL, namespaces, MCP-server, publicatie-instellingen, uitbreidingspunten | Instructies voor het Model | `wikis/<key>/wiki.yaml` |
| Harness-bindingen | Discovery-brug, MCP-clientconfig, instellingen, optionele Agentprofielen | Domeinlogica | Gegenereerd door `llmwiki harness sync` |
| Run-directory (kladblok) | State en artefacten van één Run | Eindresultaat | `wikis/<key>/.work/runs/<run-id>/`, gitignored |
| Archief (`log.md`) | Blijvende verantwoording: wie publiceerde/promoveerde wat, wanneer, met welk akkoord | Werk-in-uitvoering | `wikis/<key>/log.md`, in Git, alleen aanvullen |
| Publicatievoorstel | Menselijke beoordeling en akkoord (smaak A) | Afdwinging | `wikis/<key>/voorstellen/<run-id>.md`, gitignored |
| `llmwiki workspace-check` | Werkplek controleren en herstellen, kladblok opruimen | Inhoudelijk werk | CLI-commando |

### 5.3 Repositorystructuur

```text
llm-wikis/                                  Git-root
├── AGENTS.md                               repository-Rules (S)
├── ARCHITECTURE.md                         Architectuur-Kompas
├── README.md                               installatie en gebruik voor mensen
├── docs/
│   ├── kluswijzer.md                       inrichtingsstappen
│   └── onderbouwing.md                     dit document
├── pyproject.toml                          Python-pakket llmwiki + CLI (K)
├── uv.lock
├── .gitattributes                          regeleinden en binaire bestanden
├── .obsidian/app.json                      Obsidian-vault = repository-root (5.18)
├── sources/                                centrale bronnen: raw/ en index/ (5.19)
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
├── tools/
│   └── llmwiki/                            deterministische core (K)
│       ├── __init__.py
│       ├── cli.py                          llmwiki pull|run|validate|publish|promote|harness|workspace-check
│       ├── sync.py                         pywikibot pull/push
│       ├── titles.py                       paginatitel <-> bestandsnaam
│       ├── runs.py                         run-State, opruimen kladblok, phases_for per wiki-soort
│       ├── gate.py                         publicatievoorstel, akkoordcontrole, publish/promote
│       ├── logbook.py                      log.md/voortgang.md
│       ├── workspace_check.py               werkplekcontrole en herstel
│       ├── harness.py                      bindingen genereren/controleren
│       └── schemas/                        generieke schemas (S)
│           ├── source.schema.json
│           ├── source-index.schema.json
│           ├── assessment.schema.json
│           ├── changeset.schema.json
│           ├── validation-report.schema.json
│           ├── publish-plan.schema.json
│           ├── approval.schema.json
│           └── run-state.schema.json
├── tests/
├── wikis/
│   ├── _template/                          sjabloon voor een nieuwe sync-wiki
│   ├── _template-md/                       sjabloon voor een nieuwe curatie-wiki
│   └── gemma/                              type sync: één LLM-wiki
│       ├── AGENTS.md                       wiki-Rules (S)
│       ├── wiki.yaml                       wiki-manifest (K)
│       ├── content/                        wikitext (Resultaat, in Git)
│       │   ├── main/
│       │   │   └── Gemeentelijk_gegevenslandschap.wiki
│       │   └── template/
│       ├── revisies.json                   conflictbasis: pad -> {titel, revid}
│       ├── log.md                          blijvend verslag (in Git, niet op MediaWiki)
│       ├── .agents/skills/                 wiki-Skills, canoniek (C), leeg tenzij nodig
│       ├── .work/                          run-State, gitignored
│       │   └── runs/<run-id>/
│       ├── mediawiki-mcp.config.json       gegenereerd, gecommit (5.10)
│       ├── .mcp.json                       gegenereerd (H: Claude Code)
│       ├── opencode.json                   gegenereerd (H: OpenCode; MCP-blok + permission.bash)
│       ├── .vscode/mcp.json                gegenereerd (H: VS Code)
│       ├── .vscode/settings.json           gegenereerd (H: VS Code)
│       ├── .cursor/mcp.json                gegenereerd (H: Cursor)
│       ├── .claude/settings.json           gegenereerde permissies (H: Claude Code)
│       └── .claude/skills/                 gegenereerde brug, gitignored (H: Claude Code)
├── .claude/
│   ├── settings.json                       permissies repository-breed (H)
│   └── skills/                             gegenereerde brug, gitignored (H)
├── opencode.json                           (H) root-sessies
└── .vscode/settings.json                   (H)
```

Codex leest `.agents/skills/` en `AGENTS.md` native, zonder gegenereerd bestand (5.14); Cursor idem, met een optionele extra brug pas als verificatie een probleem laat zien (5.14). Een `curation`-wiki zonder MediaWiki-exportdoel genereert geen van de MCP-bestanden.

Toelichting op keuzes:

- `wikis/<key>/` in plaats van `wiki-<key>/` op root-niveau: alle wiki's zijn met één glob (`wikis/*/`) te vinden door scripts, lint en OpenCode-`instructions`; de root blijft overzichtelijk. De werkmap wordt `cd wikis/gemma-online`.
- Generieke Skills staan in de root-`.agents/skills/`, niet in `core/.agents/skills/`: [Verified] Codex, OpenCode en Cursor vinden skills alleen in `.agents/skills/` van de werkmap of een bovenliggende map; een map `core/` ligt niet op het pad van `wikis/gemma-online` naar de root.
- Het Python-pakket staat in `tools/llmwiki/`: installeerbaar met `uv sync`, CLI `llmwiki` werkt vanuit elke map. De map heet `tools/` omdat de inhoud Tools zijn in de zin van de terminologie; de gebruikelijke Python-naam `src/` zegt een niet-programmeur niets. Het pakket zelf blijft `llmwiki` en staat in een eigen submap: [Inferred] een pakket met de naam `tools` botst met andere pakketten die zo heten en maakt de latere extractie als zelfstandig pakket lastiger. [Inferred] `pyproject.toml` kan de pakketmap expliciet aanwijzen (bij hatchling `[tool.hatch.build.targets.wheel] packages = ["tools/llmwiki"]`); de bescherming van de src-layout (tests draaien tegen het geïnstalleerde pakket, niet tegen losse bestanden in de werkmap) blijft daarmee behouden. [Inferred] `uv run` vindt vanuit `wikis/gemma-online` de `pyproject.toml` in de root door omhoog te zoeken.
- Schemas zitten in het pakket: Skills verwijzen naar `llmwiki schema show <naam>` of `llmwiki validate`, niet naar een relatief pad buiten de skill-directory. [Verified] De specificatie beveelt verwijzingen relatief aan de skill-root aan; een pad naar `../../tools/...` zou de skill aan deze repository binden.
- Er is geen aparte map voor "knowledge" bij een sync-wiki. Kennis die het product is, staat in `content/`. Ongestructureerde kennisopbouw die een sync-wiki informeert, hoort in een eigen `knowledge-base`-wiki (5.18), niet in een submap van de sync-wiki.
- Er is geen map `agents/` met Agentprofielen. Zie 5.9.
- `voorstellen/` staat buiten `.work/` en is geen verborgen map. [Inferred] Editors zoals Obsidian tonen mappen die met een punt beginnen standaard niet; een publicatievoorstel in `.work/` zou voor de redacteur onvindbaar zijn.

### 5.4 Afhankelijkheidsrichting

```text
 wiki-Workflow (bijv. gemma-begrippen-update, curatie)
        │ gebruikt
        ├──────────────► generieke Workflow (wiki-update, curatie | wiki-edit, sync)
        │                        │ gebruikt
        │                        ├──► generieke Skills (wiki-ingest ... wiki-publish)
        │                        │            │ roepen aan
        │                        │            └──► llmwiki-CLI  ──► pywikibot ──► MediaWiki
        │                        └──► Rollen (logisch)
        ├──────────────► wiki-Skills (bijv. gemma-bo, gemma-archimate)
        │                        └──► wiki-scripts, wiki-schemas
        └──► logische MediaWiki-operaties ──► MCP-server "mediawiki" (via harness)

 Rules:   wiki-AGENTS.md ──verwijst naar──► repository-AGENTS.md
 Harness-bindingen ──gegenereerd uit──► wiki.yaml + .agents/skills (nooit andersom)
```

Regels voor afhankelijkheden:

1. De generieke laag verwijst nooit naar een wiki-key, wiki-pad, wiki-Skill of domeinterm. Controle: `llmwiki lint` zoekt in `.agents/skills/` en `tools/llmwiki/` naar `wikis/`, bekende wiki-keys en naar skillnamen met een wiki-prefix, en faalt bij een treffer.
2. Een wiki verwijst naar generieke Skills alleen bij naam, nooit via een pad in de root-map.
3. Wiki's verwijzen niet naar elkaar. Gedeeld gedrag verhuist naar de generieke laag; gedeelde bronnen staan in `sources/`, en de uitkomst van de ene wiki wordt voor de volgende een bron (5.18).
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
| Publicatiegate | Akkoord in publicatievoorstel (smaak A) of bevestigingswoord in chat (smaak B); keuze in `wiki.yaml`; `llmwiki` controleert het akkoord in smaak A | Permissieregel 'ask' op `publish apply` en `export apply`: goedkeuringsklik van de mens | K + H |
| MediaWiki-toegang | Logische operaties in skills; `wiki.yaml` beschrijft de server | `.mcp.json`, `opencode.json`, `.codex/config.toml`, `.vscode/mcp.json`, `.cursor/mcp.json` | S + H |
| Credentials | Namen van omgevingsvariabelen in `wiki.yaml` | Waarden in gebruikersomgeving of gitignored `.env` | H |
| Rollen | Beschreven in Workflow-Skill | Agentprofielen (optioneel) | K + H |
| Modelkeuze | Niet vastgelegd | Harness-instelling of Agentprofiel | H |
| State | `.work/runs/` | — | K |
| Schemas | JSON Schema in pakket en wiki | — | S |

### 5.6 Discovery van Rules

Inhoud:

- Root-`AGENTS.md`: werkplekcontrole bij de eerste Vraag van een Sessie (5.17), repository-opbouw (verwijzing naar het Kompas), de Workflow-conventie (artefacten, run-directory, records), veiligheid (nooit publiceren of exporteren zonder gate, nooit credentials in bestanden), hoe `llmwiki` wordt aangeroepen, dat generieke Skills geen wiki-kennis mogen bevatten. Geen domeinkennis.
- Wiki-`AGENTS.md`: begint met een expliciete verwijzing, daarna domein, taal, stijl, doelgroep, naamgevingsconventies, verboden constructies, welke Workflow-Skill de standaard is.

```markdown
# GEMMA-wiki

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de Context staan: lees dat bestand voordat je iets wijzigt.

## Domein
...
## Standaard Workflow
Gebruik skill `wiki-edit` voor het bijwerken van pagina's (deze wiki is `sync`).
```

Waarom deze vorm:

- [Verified] Alle vijf harnesses lezen AGENTS.md; het is de enige instructielocatie die overal werkt.
- [Verified] Claude Code en Codex voegen root- en wiki-AGENTS.md samen bij starten in de wiki-map; Cursor combineert geneste bestanden; VS Code doet dat met `chat.useCustomizationsInParentRepositories`. [Speculative] OpenCode laadt mogelijk alleen de dichtstbijzijnde. De expliciete verwijzing in de eerste regel maakt het resultaat onafhankelijk van die verschillen: in het slechtste geval leest het Model de root-Rules via een Tool-aanroep. Voor OpenCode wordt de verwijzing daarnaast deterministisch gemaakt via `instructions` in de gegenereerde `wikis/<key>/opencode.json` (5.16).
- Aparte wiki-rulebestanden (zoals `.claude/rules/` of `.cursor/rules/*.mdc`) worden niet gebruikt: [Verified] ze zijn harness-specifiek, en de extra functie (padgebonden activering) wordt al gedekt door wiki-Skills met progressieve disclosure.
- Er komt geen `CLAUDE.md`. [Verified] Zodra een CLAUDE.md of CLAUDE.local.md in de werkmap of daarboven staat, leest Claude Code AGENTS.md standaard niet meer. Een lokale CLAUDE.local.md van één gebruiker zou dus de wiki-Rules uitschakelen. `llmwiki harness check` meldt het bestaan van zulke bestanden. Terugval voor Claude Code-versies ouder dan v2.1.277: een CLAUDE.md naast elke AGENTS.md met alleen `@AGENTS.md`; [Verified] Claude Code leest het geïmporteerde bestand dan niet dubbel.
- Todo's en nieuwe regels staan in de repository, op de plek waar ze gelden (wiki, Skill of root), en niet in het persoonlijke geheugen van een harness. [Verified] Dat geheugen (bij Claude Code in de home-directory) is per gebruiker en per machine; op een andere werkplek, in een ander harness of voor een collega bestaat het niet. Alleen persoonlijke voorkeuren van de gebruiker horen daar.
- Omvang: Rules blijven klein. [Verified] Codex kapt samengevoegde AGENTS.md-inhoud standaard af bij 32 KiB; Claude Code adviseert minder dan 200 regels per bestand.

Rangorde bij tegenstrijdigheid, vastgelegd in de root-AGENTS.md: repository-veiligheidsregels > wiki-Rules > Skill-instructies > Vraag van de gebruiker voor zover die de gate raakt. [Inferred] Geen harness dwingt deze rangorde technisch af; daarom wordt de regel die er echt toe doet (niet publiceren zonder mens) ook buiten het Model afgedwongen: controles in de CLI en een goedkeuringsklik in het harness (5.13).

### 5.7 Discovery van Skills

**Canonieke locatie.** `.agents/skills/` in de root (generiek) en in `wikis/<key>/` (wiki-specifiek).

[Verified] Codex, OpenCode, VS Code en Cursor lezen deze locatie. [Verified] Claude Code niet.

**Brug voor Claude Code.** `llmwiki harness sync` maakt voor elke skill in een canonieke `.agents/skills/` een beheerde kopie in de naastgelegen `.claude/skills/`. Elke kopie bevat een `.bridge-source.json` met de canonieke bron en bronhash. `llmwiki harness check` meldt ontbrekende, onbeheerde en verouderde kopieën. De brugmappen staan in `.gitignore` en worden uitsluitend vanuit de canonieke bron opnieuw opgebouwd.

Waarom niet andersom (canoniek in `.claude/skills/`, brug voor Codex): beide richtingen vereisen één brug. `.agents/skills/` is leverancier-neutraal, wordt door agentskills.io aanbevolen en door vier van de vijf harnesses gelezen. Kopiëren vanuit die ene bron voorkomt platformafhankelijke symlink- en junctionsemantiek.

Waarom geen Claude Code-plugin als brug: [Verified] een skills-directory-plugin laadt alleen vanuit de primaire werkmap en niet vanuit bovenliggende mappen; skills krijgen dan een plugin-prefix (`/plugin:skill`), zodat de naam in Claude Code afwijkt van de naam in de andere harnesses. Dat breekt pariteit.

Neveneffect: OpenCode, VS Code en Cursor lezen ook `.claude/skills/` en zien elke skill dan twee keer met identieke inhoud. [Verified] OpenCode verlangt unieke namen. Maatregelen:
- OpenCode: `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` in de omgeving van de gebruiker. [Verified] Deze variabele schakelt alleen het lezen van `.claude/skills` uit.
- VS Code en Cursor: [Speculative] gedrag bij identieke duplicaten niet gedocumenteerd; [Verified] de agentskills.io-gids adviseert clients om bij botsingen deterministisch één variant te kiezen. Verificatie in sectie 8. Als duplicaten problemen geven: de brug alleen aanmaken met `llmwiki harness sync --only claude` op machines waar Claude Code wordt gebruikt, en in VS Code `chat.agentSkillsLocations` beperken.

**Discovery per werkmap.**

| Werkmap | Claude Code | Codex | OpenCode | VS Code | Cursor |
|---|---|---|---|---|---|
| `wikis/gemma-online` | [Verified] root- en wiki-brug via ouderdirectories | [Verified] root- en wiki-`.agents/skills` | [Verified] beide, omhoog tot Git-root | [Verified] beide met `chat.useCustomizationsInParentRepositories: true` in de gegenereerde `wikis/gemma-online/.vscode/settings.json` | [Speculative] alleen wiki-skills; zie 5.14 |
| repository-root | [Verified] generieke skills direct; wiki-skills pas na lezen van een bestand in die wiki, met gekwalificeerde naam bij botsing | [Verified] alleen generieke | [Verified] alleen generieke | [Speculative] alleen generieke | [Verified] generieke overal; wiki-skills beperkt tot bestanden in die wiki |

[Inferred] Vanuit de root lekken wiki-Skills dus niet naar andere wiki's: de meeste harnesses laden ze niet, en Cursor en Claude Code beperken ze tot de betreffende directory.

**Naamgeving, precedence en conflicten.**

- Generieke Skills: prefix `wiki-` (`wiki-ingest`, `wiki-assess`, `wiki-write`, `wiki-validate`, `wiki-publish`, `wiki-update`).
- Wiki-Skills: prefix met de wiki-key (`gemma-bo`, `gemma-archimate`, `gemma-begrippen-update`).
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
Na VALIDATE: draai `llmwiki run status`; die noemt de laatste fase voor deze curatie-wiki (`promote`, of `promote` + `export` als `exports:` is ingevuld, zie 5.18) en het bijbehorende plan-commando. Hieronder staat `promote`; `export` werkt hetzelfde. De CLI meldt welke smaak deze wiki gebruikt.
- Smaak A (document): meld het pad van het promotievoorstel en stop. Ga pas verder als de gebruiker vraagt de promotie uit te voeren; `llmwiki promote apply` controleert zelf het akkoord.
- Smaak B (chat): toon de samenvatting uit het voorstel en vraag de gebruiker letterlijk AKKOORD te typen. Instemming in andere woorden ("prima", "ziet er goed uit") is geen akkoord: vraag opnieuw om het woord.
Wijzig nooit zelf de akkoordvelden in een voorstel. Het harness vraagt de gebruiker bij `promote apply` altijd nog om goedkeuring; omzeil dat niet.
`promote apply` schrijft na een geslaagde toepassing een regel in `log.md` (een sync-wiki gebruikt in plaats hiervan `wiki-edit`; `publish apply` schrijft daar hetzelfde soort regel).
```

**Wiki-Workflow `gemma-begrippen-update`** (een curatie-wiki met een ArchiMate-exportdoel, niet de GEMMA-website zelf — die is `sync` en gebruikt `wiki-edit`) is dun en verwijst:

```markdown
---
name: gemma-begrippen-update
description: Werk de GEMMA-begrippenwiki bij op basis van nieuw bronmateriaal, inclusief bedrijfsobject- en ArchiMate-controles. Gebruik voor elke inhoudelijke wijziging van GEMMA-begrippen.
metadata:
  kind: workflow
  scope: wiki
  requires-skills: "wiki-update gemma-bo gemma-archimate"
  requires-tools: "llmwiki"
---

# Workflow gemma-begrippen-update

Volg skill `wiki-update` volledig, met deze uitbreidingen:

| Fase | Aanvulling |
|---|---|
| ASSESS | Laad `gemma-bo`; classificeer elk voorgesteld begrip als bedrijfsobject of niet, volgens `schemas/bedrijfsobject.schema.json`. |
| WRITE | Laad `gemma-archimate` voor pagina's in namespace ArchiMate. |
| VALIDATE | Draai daarnaast `uv run python tools/check_archimate.py --run <run-id>`. |
| Na PROMOTE | Als `exports.archimate` is ingevuld: stel voor een architectuurmodel-export te maken met `llmwiki export plan --target archimate`. Dezelfde gate geldt. |
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
| Claude Code | [Verified] `/gemma-begrippen-update <bron>` |
| Codex | [Verified] `$gemma-begrippen-update` in de prompt of via `/skills` |
| VS Code/Copilot | [Verified] `/gemma-begrippen-update` |
| Cursor | [Verified] `/gemma-begrippen-update` |
| OpenCode | [Verified] het Model laadt skills via de `skill`-Tool; [Inferred] de Vraag "gebruik skill gemma-begrippen-update voor bron X" is voldoende. Optioneel een gegenereerd command-bestand als snelkoppeling (H). |

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

**Correctie (deze versie).** Eerdere versies gingen uit van platte env-vars (`MW_API_URL`/`MW_USERNAME`) rechtstreeks in het MCP-clientblok. Het gekozen pakket, **`@professional-wiki/mediawiki-mcp-server`** (npm; actief onderhouden, bevestigd hetzelfde pakket als een al bestaand, werkend MediaWiki-beheerproject dat als kennisbron is gebruikt bij deze correctie), werkt zo niet: het leest een eigen `config.json` (pad via de env-var `CONFIG`) met een `wikis`-object (`server`, `articlepath`, `scriptpath`, `username`/`password` of `token`, `readOnly`). De rest van deze sectie is bijgewerkt.

**Keuzes.**

1. **MCP per wiki, niet repository-breed.** Een `sync`-wiki, of een `curation`-wiki met MediaWiki als exportdoel, heeft precies één doel-site; `knowledge-base`-wiki's hebben geen MediaWiki-server (5.18). Een per-wiki serverinstantie met die site als vaste standaard voorkomt dat een Agent in de GEMMA-sessie per ongeluk een andere wiki raadpleegt of wijzigt. De serverconfiguratie staat daarom in de wiki-map.
2. **Vaste servernaam `mediawiki` in elke wiki en elk harness.** Skills verwijzen naar "MCP-server `mediawiki`, tool `<naam zoals de server die publiceert>`". [Verified] Claude Code maakt daar `mcp__mediawiki__<tool>` van; [Inferred] andere harnesses gebruiken een eigen prefix. De door de server gepubliceerde naam is gelijk in elk harness; alleen het prefix verschilt. Een Skill noemt daarom nooit de geprefixte naam.
3. **MCP wijst altijd naar het hoofddoel, nooit naar een testomgeving.** Een testomgeving (bijvoorbeeld een OTAP-staging) kan achter een extra HTTP Basic Auth-laag zitten die los staat van MediaWiki's eigen login — bij een pakket dat zulke userinfo-in-URL niet ondersteunt (zoals dit pakket, vermoedelijk vanwege de gebruikte HTTP-client) is een testomgeving dan simpelweg niet bereikbaar via MCP. Omdat MCP toch alleen-lezen is, is dit geen verlies: lezen tegen het hoofddoel is voor die rol voldoende. Live schrijven naar een testdoel loopt via pywikibot (`llmwiki pull/publish --doel <naam>`), dat wél een aparte Basic-Auth-laag kan doorgeven (pywikibots `authenticate`-dictionary, buiten deze repository ingesteld).
4. **Rolverdeling MCP versus pywikibot.** MCP voor interactief lezen, zoeken en verkennen tijdens het bewerken. Pywikibot via `llmwiki pull`/`publish` voor het daadwerkelijk ophalen en publiceren. MCP-schrijfoperaties worden niet gebruikt: publiceren loopt uitsluitend via de gate. `readOnly: true` in de gegenereerde `config.json` zet dit ook aan de kant van de MCP-server af; harness-permissies blokkeren daarnaast de schrijf-Tools waar de client dat toelaat.
5. **Terugval zonder MCP.** Elke Skill die MCP gebruikt, noemt een terugval via `llmwiki pull --titel <titel>` (leest via pywikibot). [Inferred] Daarmee blijft de Workflow uitvoerbaar in een harness of omgeving waar de MCP-server ontbreekt of niet is goedgekeurd.

**Gegenereerde `config.json` (per wiki, gecommit).**

```json
{
  "readOnly": true,
  "wikis": {
    "gemma-online": {
      "sitename": "gemma-online",
      "server": "https://redactie.gemmaonline.nl",
      "articlepath": "/wiki",
      "scriptpath": "",
      "readOnly": true
    }
  }
}
```

Geen geheimen in dit bestand: alleen niet-gevoelige serverinformatie uit `wiki.yaml`'s `site`-blok. Authenticatie (Bot Password, eventuele Basic Auth voor een testdoel) blijft volledig in pywikibots eigen, buiten deze repository gehouden configuratie (zie hieronder) — de MCP-server zelf draait `readOnly` en heeft dus geen schrijfcredentials nodig.

**Harness-clientbestand (voorbeeld: Claude Code, `.mcp.json`).**

```json
{
  "mcpServers": {
    "mediawiki": {
      "command": "npx",
      "args": ["-y", "@professional-wiki/mediawiki-mcp-server@latest"],
      "env": { "CONFIG": "mediawiki-mcp.config.json" }
    }
  }
}
```

Het `CONFIG`-pad is **relatief aan de wiki-map**, zodat het bestand machine-onafhankelijk en gecommit kan zijn (in tegenstelling tot een eerder overwogen ontwerp met een absoluut, per-gebruiker pad). Of dat relatieve pad in elke harness correct oplost — de child-process-cwd bij het starten van een stdio-server verschilt mogelijk per harness — is nieuw verificatiepunt **V10** (sectie 8), naast het bestaande V6 voor env-var-syntax per harness. `llmwiki harness sync` genereert hetzelfde soort blok voor OpenCode (`opencode.json`), Codex (`.codex/config.toml`), VS Code (`.vscode/mcp.json`) en Cursor (`.cursor/mcp.json`), telkens wijzend op dezelfde `config.json`.

**Pywikibot: inloggegevens komen uit omgevingsvariabelen, de servers uit een family-bestand in de wiki-map.** Zie 5.10a; dat vervangt de eerdere keuze om credentials en family volledig in pywikibots eigen globale configuratie (`~/.pywikibot/user-config.py` met een `password_file`) te laten.

[Verified] Claude Code vraagt goedkeuring voor project-servers uit `.mcp.json`; [Verified] een gekloonde repository kan die goedkeuring niet zelf geven. Dit is een gewenste eigenschap en geen probleem voor de architectuur.

#### 5.10a Inloggegevens voor GEMMA Online (2026-09-29)

**Aanleiding.** De eerdere keuze vroeg van elke redacteur een eigen pywikibot-configuratie buiten de repository: een family-bestand, een `user-config.py`, een `password_file` en een `authenticate`-regel voor de extra toegangslaag van staging. Niemand had dat ingericht, de README beschreef het niet (workspace-check verwees er wel naar), en het wachtwoordbestand staat als platte tekst op schijf, op Windows vaak in een met OneDrive gesynchroniseerde map. Tegelijk zegt de repository-regel: credentials alleen in omgevingsvariabelen, genoemd bij naam in `wiki.yaml`. Het ontwerp volgde die regel niet.

**Wat er nodig is.** Twee omgevingen, elk met een eigen login: redactie (`redactie.gemmaonline.nl`, code `en`) en staging (`gemma2-redactie.staging.wikixl.nl`, code `staging`). Staging heeft daarnaast een HTTP Basic Auth-laag vóór de wiki.

**Afweging opslag.**

| Optie | Voor | Tegen |
|---|---|---|
| Omgevingsvariabelen van de gebruiker (gekozen) | Volgt de repository-regel; werkt op Windows, macOS en Linux op dezelfde manier; geen extra pakket; op de desktop al in gebruik; op Windows zonder beheerrechten persistent in te stellen | Leesbaar voor elk programma dat onder je eigen account draait (op Windows onversleuteld in het register onder `HKCU\Environment`, op Linux in je shellprofiel) |
| pywikibot `password_file` (eerdere keuze) | Standaard pywikibot | Wachtwoord als platte tekst in een bestand; lekt makkelijk via OneDrive, back-ups of een verkeerde `git add`; per machine handwerk |
| Windows Credentiallijst of macOS-sleutelhanger via `keyring` | Versleuteld opgeslagen | Extra pakket; per besturingssysteem anders (op Linux een Secret Service nodig); moeilijker uit te leggen en te controleren |

Het risico van omgevingsvariabelen beperken we met **BotPasswords** in plaats van het echte wachtwoord: per omgeving een apart botwachtwoord (Speciaal:BotWachtwoorden), met alleen de rechten die publiceren nodig heeft (basisrechten en pagina's bewerken), en per stuk in te trekken zonder je account te raken.

**Uitwerking.**

1. **Namen in `wiki.yaml`, waarden in de omgeving.** Per doel de namen van de variabelen, bijvoorbeeld:
   ```yaml
   site:
     family: gemmaonline
     code: en
     inlog: {gebruiker: GEMMA_REDACTIE_USER, wachtwoord: GEMMA_REDACTIE_BOTPASSWORD}
   test_targets:
     staging:
       family: gemmaonline
       code: staging
       inlog: {gebruiker: GEMMA_STAGING_USER, wachtwoord: GEMMA_STAGING_BOTPASSWORD}
       http_toegang: {gebruiker: GEMMA_STAGING_HTTP_USER, wachtwoord: GEMMA_STAGING_HTTP_PASSWORD}
   ```
   De namen zijn vrij te kiezen; wie op een andere machine al variabelen heeft, kan die namen hier zetten. De gebruikersnaam van een botwachtwoord heeft de vorm `Hoofdaccount@botnaam`; pywikibot herkent de `@` en logt dan in met `action=login` in plaats van `clientlogin`.
2. **Family-bestand in de repository** (`wikis/gemma-online/families/gemmaonline_family.py`, en een kopie in `wikis/_template`): alleen de twee servers en hun paden, geen geheimen. Naam en vorm (`<naam>_family.py`, klasse `Family`) schrijft pywikibot voor; pywikibot kan een family ook zonder bestand uit alleen een serveradres opbouwen (`AutoFamily`), maar het bestand is de gangbare, best gedocumenteerde weg. `llmwiki` meldt elke map `wikis/*/families/` zelf aan bij pywikibot. Daarmee vervalt de oorspronkelijke reden om de family buiten de repository te houden (dynamische Site-constructie niet te verifiëren): de family staat vast in een bestand, alleen niet meer per machine.
3. **Geen eigen configuratie en geen wachtwoordbestand.** `llmwiki` zet pywikibots werkmap op `.work/pywikibot/` (al genegeerd door git; daar komen alleen de sessiecookie, de cache en de throttle-administratie). Daar staat een leeg `user-config.py`, omdat pywikibot `PYWIKIBOT_DIR` alleen gebruikt als dat bestand er is; anders belanden die werkbestanden in de map waar het commando draait. `.gitignore` sluit ze daarnaast als vangnet uit (`*.lwp`, `apicache/`, `throttle.ctrl`). `llmwiki` leest de variabelen uit `wiki.yaml`, geeft gebruiker en botwachtwoord rechtstreeks aan pywikibots login en zet de Basic Auth voor staging in pywikibots `authenticate`. Heeft iemand al een eigen pywikibot-configuratie (`PYWIKIBOT_DIR` gezet), dan gebruikt `llmwiki` die ongewijzigd.
4. **workspace-check** meldt per doel welke variabele ontbreekt, als opmerking en niet als blokkade: zonder inlog werken curatiewiki's en de MCP-server gewoon door; alleen `pull`/`publish` naar dat doel faalt, met een melding die de ontbrekende namen noemt. Een ontbrekend family-bestand is wel een blokkade (fout in de repository). Het setup-script toont dezelfde lijst, met de stappen om een variabele te zetten.
5. **README**, sectie *Inloggegevens GEMMA Online*: botwachtwoorden aanmaken en de variabelen zetten, per besturingssysteem. Op Windows: *Start* → typ "omgevingsvariabelen" → *Omgevingsvariabelen voor uw account bewerken* (geen beheerrechten nodig) → *Gebruikersvariabelen* → *Nieuw...*, of met het script `scripts/inlog-instellen.ps1` (vraagt per variabele de waarde; wachtwoorden onzichtbaar en buiten de PowerShell-geschiedenis); daarna VS Code en de terminal opnieuw starten. Op macOS/Linux: `export` in het shellprofiel.

**Wat verandert ten opzichte van de eerdere keuze.** "`llmwiki` schrijft of leest die configuratie nooit" vervalt: `llmwiki` leest de namen uit `wiki.yaml` en de waarden uit de omgeving, en geeft ze in het geheugen door aan pywikibot (`tools/llmwiki/sync.py`, tests in `tests/test_sync_inlog.py`). Er komt niets geheims in de repository of in een bestand dat `llmwiki` schrijft; alleen pywikibots sessiecookie staat in `.work/pywikibot/`.

**Verificatie.** Verificatiepunt V11 in sectie 8. Op 2026-09-29 getest: `pull` met een botwachtwoord uit de omgevingsvariabelen werkt tegen redactie en staging (inclusief de extra HTTP-toegangslaag en het scriptpad `""` op staging), ook herhaald: een tweede aanroep hergebruikt de sessiecookie, want MediaWiki weigert een nieuwe login binnen een bestaande botwachtwoord-sessie. De `WARNING: readapidenied` vooraf komt van pywikibots controle vóór het inloggen (anoniem lezen is niet toegestaan) en is onschuldig. Publiceren is nog niet getest.

**Pull van een testdoel.** `llmwiki pull --doel <testdoel>` schrijft naar `.work/sync/<doel>/`, niet naar de werkkopie `content/`: staging is een periodiek ververste, oudere kopie en overschreef bij de eerste test de actuele productietekst in `content/`. De revisies blijven per doel gesleuteld op het `content/`-pad (`.work/sync/<doel>.json`), zodat `publish --doel` ze voor de conflictcontrole vindt.

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

**Run-directory.** Voorbeeld voor een curatie-wiki (vier fasen vóór de gate):

```text
wikis/opzet2/.work/runs/2026-09-26T1412-a3f9/
├── state.json                  run-state.schema.json
├── input/                      verwijzingen naar of kopieën van brondocumenten
├── source.json                 source.schema.json          (INGEST)
├── assessment.json             assessment.schema.json      (ASSESS)
├── changeset.json              changeset.schema.json       (WRITE)
├── changeset/                  voorgestelde Markdown-pagina's, gestaged
├── validation-report.json      validation-report.schema.json (VALIDATE)
├── promote-plan.json           publish-plan.schema.json    (PROMOTE plan)
└── log.jsonl                   gebeurtenissen per fase (welk harness, welk Model, tijd)
```

Een sync-wiki heeft maar één fase vóór de gate (`phases_for` geeft `[validate]`): alleen `validation-report.json` en, na `publish plan`, `publish-plan.json` — geen `source.json`/`assessment.json`/`changeset.json`/`changeset/`, want er is geen INGEST/ASSESS/WRITE. `content/` wordt bij een sync-wiki rechtstreeks in de werkboom bewerkt, niet gestaged in het kladblok.

`state.json` bevat: workflow-naam, huidige fase, status per fase (`pending|done|failed`), paden en hashes van artefacten, basis-revisies van de betrokken pagina's. `llmwiki run complete <fase>` is de enige manier om een fase af te ronden en valideert het artefact eerst.

**Kladblok versus archief.** Twee soorten opslag met een verschillend doel. Er is geen apart `records/`-archief meer (eerdere versies hadden dat voor type A; zie de correctie in 5.18) — het blijvende verslag is `log.md`, voor elke wiki-soort op dezelfde manier geschreven door de CLI:

| | Kladblok | Archief |
|---|---|---|
| Doel | Hervatten na onderbreking zonder stappen opnieuw te doen | Verantwoording: wie publiceerde/promoveerde wat, wanneer, met welk akkoord |
| Plaats | `wikis/<key>/.work/runs/<run-id>/` | `wikis/<key>/log.md`; bij curatie ook de pagina's zelf |
| Git | Nee | Ja |
| MediaWiki | Nee | Nee |
| Inhoud | Alle artefacten, ruwe tussenresultaten | Één regel per publicatie/promotie (datum, actie, titel/pagina-id, akkoord, hash) |
| Wie schrijft | Model (artefacten) en CLI (State) | Alleen de CLI (`publish apply`/`promote apply`), nooit het Model |
| Levensduur | Onafgeronde runs blijven staan tot hervat of afgebroken; afgeronde runs worden na `work.retention_days` (standaard 30) verwijderd | Blijvend, alleen aanvullen |

`llmwiki run close <run-id> --besluit "<tekst>"` schrijft voor een run die bewust zonder publicatie wordt afgesloten (bijvoorbeeld: bron beoordeeld, geen wijziging nodig) optioneel een regel in `log.md` als er een besluit te noteren is. `llmwiki run abandon <run-id>` schrijft niets en verwijdert het kladblok van die run. Een onderbroken of geannuleerde run laat dus niets achter in de wiki — ook niet in `log.md`.

**Git.** `.work/` en `voorstellen/` staan in `.gitignore`. Bij een sync-wiki bewerkt de Agent `content/` rechtstreeks in de werkboom; de mens beoordeelt via het publicatievoorstel (met een echte git-diff erin) of met `git diff`. Bij een curatie-wiki staat het concept eerst gestaged in het kladblok (`changeset/`) en wordt het pas bij een geslaagde `promote apply` in de werkboom gezet. Commit gebeurt na publicatie/promotie, met content en `log.md` samen en de run-id in het commit-bericht. Na `publish apply` bevat `revisies.json` de nieuwe revisie-id's (5.12, 5.13) — geen aparte `.meta.json` meer.

**Opruimen.** `llmwiki workspace-check` roept `llmwiki run prune` aan; dat verwijdert afgeronde runs ouder dan de bewaartermijn en de bijbehorende voorstellen. Onafgeronde runs worden nooit automatisch verwijderd; `workspace-check` meldt ze wel, zodat de Agent kan voorstellen ze te hervatten.

### 5.12 Schemas

**Rol.** Schemas zijn het contract tussen fasen en tussen Agents, onafhankelijk van harness en Model. Ze maken de overdracht deterministisch controleerbaar; het Model hoeft niet te worden vertrouwd op de vorm van zijn uitvoer. [Inferred] Dit is de belangrijkste maatregel voor model-portability: een zwakker Model faalt zichtbaar op de fase-grens in plaats van ongemerkt verderop.

**Generiek (in `tools/llmwiki/schemas/`).**

| Schema | Beschrijft | Noodzaak |
|---|---|---|
| `source` | Bron: id, type, locatie, hash, samenvatting, relevante fragmenten | Nodig: invoer voor ASSESS |
| `assessment` | Per voorgestelde wijziging: doelpagina, soort (nieuw, wijzigen, geen actie), motivering, bronverwijzing | Nodig: overdracht naar WRITE |
| `changeset` | Per pagina: titel, bestand, basis-revisie, soort wijziging | Nodig: overdracht naar VALIDATE en PUBLISH |
| `validation-report` | Per controle: resultaat, ernst, pagina | Nodig: gate-invoer |
| `publish-plan` | Exacte lijst van edits (of exportinhoud) met basis-revisie en hash van de nieuwe tekst | Nodig: gate |
| `approval` | Frontmatter van het publicatievoorstel: akkoord, naam, plan-hash | Nodig: smaak A wordt door code gecontroleerd |
| `run-state` | Zie 5.11 | Nodig: hervatten |

**`revisies.json` (geen JSON Schema, één bestand per sync-wiki, geen sidecar per pagina).** Pad → `{titel, revid}`, gecommit. Vervangt een eerder overwogen `page-meta`-sidecar per pagina (titel, pageid, revid, tijdstempel, namespace, contentmodel, categorieën, sha1): die velden hadden geen consument buiten de conflictcontrole zelf, wat tegen de regel "geen schema zonder validerende code" ingaat (zie hieronder). Nodig voor: conflictdetectie bij `publish apply` (5.13). Een testdoel (bijvoorbeeld een OTAP-staging) krijgt een eigen, gitignored bestand (`.work/sync/<doel>.json`): die revisies zijn operationele state, geen gedeelde waarheid, omdat een testomgeving periodiek vanuit het hoofddoel ververst kan worden.

**Wiki-specifiek (in `wikis/<key>/schemas/`).** Alleen als er een domeinobject is dat deterministisch moet worden gecontroleerd, bijvoorbeeld `bedrijfsobject.schema.json` voor GEMMA. Een wiki-schema breidt een generiek schema uit via het veld `extensions` dat elk generiek schema als vrij object toestaat, niet door het generieke schema te kopiëren.

**Wanneer geen schema.** Voor vrije tekst (paginatekst zelf), voor tussenstappen binnen één fase, en voor iets dat maar door één script wordt gelezen en geschreven zonder Model ertussen. Een schema dat niet door code wordt gevalideerd, wordt niet toegevoegd.

**Standaard.** JSON Schema draft 2020-12 (S). Validatie met de Python-bibliotheek `jsonschema` via `llmwiki validate <artefact>`.

### 5.13 Scripts en deterministische logica

**Regel.** Alles wat zonder Model kan, gebeurt zonder Model.

| Plaats | Wat | Voorbeelden |
|---|---|---|
| `tools/llmwiki/` (repository-breed) | Logica die elke wiki nodig heeft | pull, publish, bestandsnaam-mapping (`titles.py`), run-State, schemavalidatie, publish/promote plan/apply, `log.md`/`voortgang.md`, lint, harness sync/check, workspace-check |
| `wikis/<key>/tools/` | Logica die meerdere Skills van één wiki gebruiken (zelfde naam als de root-map `tools/`: Python die de werkstroom aanroept; de root-map `scripts/` is alleen voor setup) | `check_archimate.py` |
| `<skill>/scripts/` | Logica die alleen die Skill gebruikt | parser voor een bronformaat |
| Workflow-Skill | Geen scripts; alleen aanroepvolgorde | — |

**Aanroep.** Generieke logica altijd via de CLI: `uv run python -m llmwiki <commando>`. Wiki- en Skill-scripts via `uv run python <pad>`, met paden relatief aan de wiki-map (waar de Workflow start) respectievelijk aan de skill-directory. [Verified] De specificatie beveelt paden relatief aan de skill-root aan.

**Taal en platform.** Uitsluitend Python (geen Bash of PowerShell) voor alles wat de Workflow aanroept, met `pathlib`, UTF-8 expliciet bij lezen en schrijven, en geen afhankelijkheid van een specifieke shell. [Verified] Claude Code draait op Windows zonder Git Bash commando's via PowerShell; [Inferred] een Python-CLI werkt identiek onder Bash, PowerShell en cmd.

**Publicatiegate.**

Eisen: de Agent publiceert of exporteert nooit zelfstandig; de redacteur hoeft geen terminalcodes of wachtwoorden in te voeren en blijft in de eigen editor of chat; per wiki is te kiezen tussen twee smaken; de gate geldt voor publicatie naar MediaWiki en voor architectuurmodel-export.

Probleem met de smaken op zichzelf: in smaak A heeft de Agent schrijfrechten op het voorstel en kan hij `akkoord_voor_publicatie: ja` zelf invullen; in smaak B beoordeelt het Model zelf of het woord AKKOORD is getypt. [Inferred] Beide smaken rusten daarom op Model-gedrag en zijn op zichzelf geen technische afdwinging. De afdwinging komt van een handeling die alleen de mens kan doen: de goedkeuringsklik die het harness toont voordat een commando met permissie 'ask' wordt uitgevoerd.

Werking:

1. **Plan.** `llmwiki publish plan --run <id>` controleert dat VALIDATE geslaagd is, haalt per pagina de actuele revisie op en vergelijkt die met de basis-revisie uit `revisies.json`. Bij afwijking: stop met conflictmelding. Schrijft `publish-plan.json` en het publicatievoorstel `wikis/<key>/voorstellen/<run-id>.md`, en berekent een plan-hash.
2. **Publicatievoorstel.** Leesbaar Markdown-document met bovenaan:
   ```yaml
   ---
   run: 2026-09-26T1412-a3f9
   plan_hash: 3f9a1c07
   akkoord_voor_publicatie: nee
   beoordeeld_door: ""
   ---
   ```
   daaronder het plan: per pagina één tabelrij (element als link naar de voorgestelde tekst, met actie en type eronder, status, samenvatting in één regel, besluit, opmerking), gegroepeerd naar wat er gebeurt, en de open vragen uit de pagina's. De volledige diffs staan in `voorstellen/<run-id>-details.md`. Zie 5.13b.
3. **Akkoord (smaak volgens `publish.approval` in `wiki.yaml`).**
   - Smaak A, `document`: de redacteur zet in het voorstel `akkoord_voor_publicatie: ja` en vult een naam in, en vraagt de Agent daarna de publicatie uit te voeren.
   - Smaak B, `chat`: de Agent toont de samenvatting in de chat en vraagt om het letterlijke woord AKKOORD. Andere instemming leidt tot een herhaalde vraag, niet tot uitvoering.
4. **Uitvoeren.** De Agent roept `llmwiki publish apply --run <id>` aan. De CLI controleert:
   - smaak A: `akkoord_voor_publicatie: ja`, `beoordeeld_door` niet leeg, en `plan_hash` in het voorstel gelijk aan de actuele plan-hash (een akkoord op een verouderd voorstel geldt niet);
   - beide: de besluiten in het plan (5.13b);
   - smaak B: niets aanvullends; zie laag 2;
   - beide: opnieuw de basis-revisies.
5. **Laag 2: harness-goedkeuring.** De gegenereerde harness-configuratie zet `llmwiki publish apply` en `llmwiki export apply` op 'ask' (5.15, 5.16). Het harness toont de mens het exacte commando en wacht op een klik. Dit is de enige laag die de Agent niet zelf kan vervullen.
6. **Laag 3: MCP alleen-lezen** en een deny-regel op directe pywikibot-aanroepen, zodat de Agent de CLI niet kan omzeilen.
7. **Vastlegging.** Na publicatie schrijft de CLI een regel in `log.md` (5.11), inclusief naam en smaak van het akkoord.

Architectuurmodel-export gebruikt hetzelfde mechanisme, voor een `curation`-wiki met een ingevuld `exports:`-blok: `llmwiki export plan --target <naam>` en `llmwiki export apply --target <naam> --run <id>`. De generieke CLI regelt voorstel en akkoord; de exporteur zelf is een wiki-script dat in `wiki.yaml` onder `exports` wordt genoemd (bijvoorbeeld `tools/export_archimate.py`). Zo blijft de generieke laag vrij van ArchiMate-kennis. (Nog niet gebouwd: er is nog geen concrete `exports:`-behoefte geweest, zie 5.18.)

Grenzen:
- [Inferred] Als een gebruiker in het harness automatische goedkeuring aanzet (auto-approve, "yolo", `bypassPermissions` of vergelijkbaar), vervalt laag 2 en rust de gate voor smaak B volledig op Model-gedrag. [Speculative] Per harness verschilt of een 'ask'-regel in zo'n modus nog een vraag oplevert; zie V5 in sectie 8. Het Kompas noemt daarom als spelregel: automatische goedkeuring staat uit in sessies waarin wordt gepubliceerd. `llmwiki workspace-check` controleert voor zover mogelijk of de gegenereerde permissieregels aanwezig zijn.
- [Verified] Claude Code kent daarnaast een MCP-annotatie `anthropic/requiresUserInteraction` die bij elke aanroep een goedkeuringsvraag afdwingt, ook in `acceptEdits`, `auto` en `bypassPermissions`. Als de ervaring leert dat laag 2 in Claude Code onvoldoende is, kan `publish apply` ook als Tool van een kleine lokale MCP-server worden aangeboden. Dat is Claude Code-specifiek en daarom geen onderdeel van de basisarchitectuur.
- Smaak A is sterker dan smaak B: het akkoord is gebonden aan een plan-hash, heeft een naam en staat in een document dat de redacteur zelf bewerkt. Smaak B is sneller, maar het akkoord bestaat alleen in de gespreksgeschiedenis; het logboek vermeldt daarom "akkoord via chat, goedkeuring via harness".

**Bestandsnamen voor paginatitels (repository-portability).** MediaWiki-titels bevatten tekens die op Windows niet zijn toegestaan (`: / \ * ? " < > |`), kunnen alleen in hoofdlettergebruik verschillen, en kunnen gereserveerde Windows-namen opleveren (`CON`, `NUL`). [Verified] Windows en macOS gebruiken standaard hoofdletterongevoelige bestandssystemen. `llmwiki.titles` bepaalt daarom:

- namespace-map met vaste Engelstalige canonieke naam in kleine letters (`main`, `template`, `category`);
- bestandsnaam: titel met spaties behouden (niet vervangen door `_`), `:` als `§`, overige verboden tekens percent-gecodeerd, Unicode genormaliseerd naar NFC; `.wiki`-extensie alleen voor het wikitext-contentmodel, css/js-pagina's behouden hun eigen extensie;
- `/` in de titel wordt een geneste map; een pagina die zelf ook subpagina's heeft, krijgt haar inhoud in `_index` binnen die map;
- als twee titels na hoofdletterongevoelige vergelijking gelijk zijn, of de naam gereserveerd of langer dan 120 tekens is: suffix `~<8 tekens hash van exacte titel>`;
- de exacte titel staat altijd in `revisies.json` (een override-blokje voor een pad met hash-suffix); de bestandsnaam is nooit de bron van waarheid.

#### 5.13a Python-omgeving op beheerde werkplekken (2026-09-29)

**Aanroep altijd via `python -m`.** De CLI draait als `uv run python -m llmwiki …` (`tools/llmwiki/__main__.py`) en de tests als `uv run python -m pytest`. De programma's die `uv` in `.venv/Scripts` aanmaakt (`llmwiki.exe`, `pytest.exe`) zijn lokaal gemaakt en niet ondertekend. Op beheerde Windows-laptops blokkeert Microsoft Defender zulke bestanden (Attack Surface Reduction-regel voor onbekende uitvoerbare bestanden), terwijl de ondertekende `python.exe` wel mag draaien. Eén vaste aanroep voor iedereen is eenvoudiger dan detecteren wie geblokkeerd wordt: skills, permissies (`.claude/settings.json`, gegenereerd door `harness.py`), pre-commit-hooks en CI gebruiken alle deze vorm. Het script `llmwiki` in `pyproject.toml` blijft bestaan, maar de documentatie noemt het niet.

**Alle afhankelijkheden standaard.** `mediawiki` (pywikibot) en `pdf` (pymupdf4llm) zijn dependency-groups met `[tool.uv] default-groups`, geen optionele extra's meer: een gewone `uv sync` installeerde extra's niet en haalde ze zelfs weg als ze eerder waren geïnstalleerd. Prijs: een grotere eerste installatie (pdf trekt `numpy` en `onnxruntime` mee).

**Geen C-compiler nodig.** pywikibot hangt af van `mwparserfromhell`, dat niet voor elke Python-versie een kant-en-klaar pakket heeft (bijvoorbeeld nog niet voor Python 3.14 op Windows); bouwen vraagt dan de Microsoft C++ Build Tools. `[tool.uv.extra-build-variables]` zet `WITH_EXTENSION=0` voor dit pakket, waarmee het zijn variant in puur Python bouwt. Is er wel een kant-en-klaar pakket, dan gebruikt uv dat en doet de instelling niets.

**Afgewezen: de Python-versie vastzetten** (bijvoorbeeld 3.13, waarvoor wel kant-en-klare pakketten bestaan). uv zou dan een eigen Python downloaden; die is niet ondertekend en loopt op beheerde laptops tegen hetzelfde Defender-beleid aan. Bovendien veroudert een vaste versie.

#### 5.13b Het voorstel als plan met een besluit per pagina (2026-09-30)

**Aanleiding.** Het voorstel was één lange diff (bij de herbeoordeling van lijkbezorging 43 pagina's, 285 kB). De redacteur kon het niet lezen en kon alleen het geheel goed- of afkeuren.

**Keuze.** Het voorstel is een plan: per pagina één tabelrij met een samenvatting in één regel (de definitie, of welke secties wijzigen) en de kolommen Besluit en Opmerking, gegroepeerd naar wat er gebeurt, met daaronder de open vragen uit de pagina's (*Ter discussie*). De volledige diffs staan in een apart detailbestand. De redacteur wijzigt besluiten en opmerkingen in de eigen editor:

- `goedkeuren` (alleen bij status `review`) of `schrijven` / `publiceren`: standaard;
- `overslaan`: niet schrijven; `apply` weigert als een pagina die wel wordt geschreven ernaar linkt;
- `aanpassen`: terug naar de Agent met de opmerking; `apply` weigert tot er een nieuw plan is. Het nieuwe plan neemt de besluiten over voor pagina's waarvan de inhoud niet veranderde.

**Waarom zo.** Een gewoon Markdown-bestand plus de CLI werkt in elk harness en elke editor; de planmodus van één harness (bijvoorbeeld Claude Code) zou alleen daar werken en laat zich niet aan de plan-hash binden. De plan-hash dekt alleen de inhoud, niet de besluiten: de redacteur mag het plan bewerken zonder het te breken, en `apply` voert uit wat er op het moment van het akkoord staat. De akkoordvelden, de goedkeuringsklik (laag 2) en de deny-regel op `voorstellen/` blijven ongewijzigd; de Agent schrijft ook de besluitkolommen nooit.

**Afgewezen.** Een apart besluitbestand naast het voorstel (twee bestanden om bij te werken) en besluiten in de frontmatter (onleesbaar bij tientallen pagina's).

Voor curatie-wiki's is dit voorstel vervangen door 5.13c; voor sync-wiki's met `approval: document` geldt het nog.

#### 5.13c Zacht oordeel, harde vorm (2026-10-01)

**Aanleiding.** Ook met het plan uit 5.13b bleef beoordelen zwaar. De concepten stonden in het kladblok (`.work/`, niet in Git), dus de redacteur kon de wijzigingen niet in de eigen editor of in Source Control zien. Akkoord kostte zeven handelingen op drie plekken: het voorstel lezen, de besluitkolom invullen, de links naar `.work/` en het detailbestand openen, de akkoordvelden zetten, de AI vragen, klikken en committen. De elementpagina's waren grotendeels data die de AI met de hand opmaakte, deels dubbel (kenmerken in de frontmatter én als tabel), met veel vormregels en controles. En omdat het akkoord bij de paginahash hoorde, maakte elke vormwijziging goedgekeurde pagina's weer `review`.

**Keuze.** De AI levert alleen het oordeel per begrip, in een beoordeling (YAML) in de werkboom. Scripts van de wiki leiden daaruit af wat vast kan (type uit de beslistabel, status, letterlijke modelgegevens, paginapad; harde controles en zachte signalen) en maken alle leesbare pagina's en overzichten, deterministisch. De redacteur beoordeelt die pagina's (preview en Source Control) en een overzicht van wat wacht op akkoord, en geeft akkoord met het woord AKKOORD in de chat; `llmwiki promote apply` zet daarna de status en schrijft `log.md`, na de klik in het harness. Het akkoord hoort bij de inhoudshash van de beoordeling, niet van de pagina.

- Geen run en geen kladblok voor curatie: de werkboom is de toestand, zichtbaar in Git. Hervatten is `git status`; afbreken is de wijzigingen terugdraaien.
- Wat het render-script garandeert (links naar de domein-lens, relaties in beide richtingen, geen verwijzingen in de frontmatter, de vorm), is geen regel meer voor de AI. De regels van een wiki gaan over het oordeel en hebben een naam in plaats van een code.
- Voorleggen gaat in de chat, één vraag tegelijk, met context, argumenten en advies; het antwoord wordt een besluit in de beoordeling dat de redenen noemt die het dekt. Zo heeft een besluit van de redacteur een vaste route naar `review`.
- De pre-commit-controles: `render-check` (elke pagina gelijk aan de render van de beoordelingen) en `goedgekeurd-guard` (elke `goedgekeurd` met een regel in `log.md` met de inhoudshash).

**Gevolg voor 5.11.** Artefacten per fase en overdracht naar subagents via artefacten gelden alleen nog voor sync-wiki's. Een subagent krijgt bij curatie paden in de werkboom mee. Een afgebroken taak laat bij curatie wel iets achter in de werkboom; terugdraaien in Git ruimt het op.

**Waarom zo.** De redacteur ziet wat er verandert op de plek waar hij ook ander werk bekijkt, en hoeft het alleen te lezen, niet te bewerken. Wat een programma kan (principe 6), doet een programma: de AI schrijft geen opmaak, links of statussen meer, en kan daar dus ook geen fouten in maken. Een andere opmaak vraagt geen nieuw akkoord, omdat het akkoord over de inhoud gaat. Het werkt in elk harness: YAML, Markdown, Git en de CLI.

**Afgewezen.** Concepten in de werkboom laten schrijven door de AI met het oude voorstel erbij (de diffs bleven ruis van handmatige opmaak); pagina's pas na het akkoord renderen (de redacteur zou YAML moeten lezen in plaats van pagina's); oude pagina's omzetten naar beoordelingen (de criteria waren zo veranderd dat bijna alles opnieuw moest; de oude pagina's staan onder tag `voor-herbeoordeling`).

### 5.14 Een wiki als zelfstandig subproject openen

**Gevolgen van de keuze van werkmap.**

| Aspect | Werkmap = repository-root | Werkmap = `wikis/gemma-online` |
|---|---|---|
| Git | Normaal | [Verified] Normaal; alle harnesses vinden de Git-root door omhoog te zoeken |
| AGENTS.md | Alleen root direct; wiki-Rules pas bij werken in de wiki (Claude Code, Cursor) of niet (Codex) | Root en wiki samengevoegd (Claude Code, Codex); expliciete verwijzing als vangnet |
| Skills | Generiek; wiki-Skills beperkt of niet zichtbaar | Generiek en wiki-specifiek |
| Workflow | Moet de wiki als argument krijgen | Wiki volgt uit werkmap (`wiki.yaml`) |
| Scripts | Paden moeten wiki-map bevatten | CLI vindt `wiki.yaml` in werkmap of daarboven |
| MCP | Alleen repository-brede servers | [Verified] Claude Code leest `.mcp.json` uit de projectroot; [Inferred] dat is de werkmap, dus de wiki-server is beschikbaar |
| Geschikt voor | Onderhoud aan core, werk over meerdere wiki's | Inhoudelijk werk aan één wiki |

**Per harness bij openen van `wikis/gemma-online`.**

| Harness | Rules | Skills | MCP | Extra nodig |
|---|---|---|---|---|
| Claude Code | [Verified] root + wiki | [Verified] via brug in beide niveaus | [Inferred] `wikis/gemma-online/.mcp.json` | Brug via `llmwiki harness sync`; v2.1.277+ of CLAUDE.md-terugval |
| Codex | [Verified] root + wiki | [Verified] root + wiki | [Inferred] `wikis/gemma-online/.codex/config.toml`, alleen in vertrouwd project | Project vertrouwen |
| OpenCode | [Speculative] dichtstbijzijnde; `instructions` voegt root toe | [Verified] root + wiki | [Inferred] `wikis/gemma-online/opencode.json` | `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` bij aanwezigheid brug |
| VS Code | [Verified] root + wiki met instelling | [Verified] root + wiki met instelling | [Inferred] `wikis/gemma-online/.vscode/mcp.json` | Gegenereerde `.vscode/settings.json` met `chat.useCustomizationsInParentRepositories: true`, `chat.useAgentsMdFile: true` |
| Cursor | [Speculative] alleen wiki; verwijzing in wiki-AGENTS.md als vangnet | [Speculative] alleen wiki | [Inferred] `wikis/gemma-online/.cursor/mcp.json` | Zie hieronder |

**Cursor.** [Verified] Cursor vindt geneste `.agents/skills/` en geneste AGENTS.md wanneer de repository-root is geopend, en beperkt ze tot de betreffende directory. Aanbeveling voor Cursor: open de repository-root en werk in bestanden onder `wikis/gemma-online/`. Als Cursor alleen de wiki-map moet openen en verificatie (sectie 8) bevestigt dat bovenliggende skills dan ontbreken, genereert `llmwiki harness sync --cursor-wiki-root` een brug `wikis/<key>/.cursor/skills/` met ingangen naar de generieke skills. [Verified] `.cursor/skills/` is een Cursor-eigen locatie en wordt door de andere harnesses niet gelezen, dus deze brug veroorzaakt geen duplicaten elders. Dit is de enige plek waar volledige pariteit een tweede brug kan vereisen.

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

`wikis/gemma-online/.mcp.json`:

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

`wikis/gemma-online/.claude/settings.json` (en dezelfde `ask`- en `deny`-regels in de root):

```json
{
  "permissions": {
    "allow": [
      "Bash(uv run python -m llmwiki workspace-check*)",
      "Bash(uv run python -m llmwiki run *)",
      "Bash(uv run python -m llmwiki validate *)",
      "Bash(uv run python -m llmwiki publish plan *)",
      "Bash(uv run python -m llmwiki export plan *)",
      "Bash(uv run python -m llmwiki pull *)",
      "Bash(uv run python tools/check_*)"
    ],
    "ask": [
      "Bash(uv run python -m llmwiki publish apply*)",
      "Bash(uv run python -m llmwiki export apply*)",
      "Bash(llmwiki publish apply*)",
      "Bash(llmwiki export apply*)"
    ],
    "deny": [
      "Bash(*pywikibot*)",
      "Bash(uv run python tools/export_*)",
      "Edit(voorstellen/**)",
      "Write(voorstellen/**)"
    ]
  }
}
```

[Verified] Claude Code-permissieregels worden door de client afgedwongen, ongeacht wat het Model besluit; [Verified] CLAUDE.md-instructies niet; [Verified] 'ask'- en 'deny'-regels gaan voor `allowed-tools` in Skills. [Inferred] Patronen op shell-commando's zijn omzeilbaar via alternatieve schrijfwijzen (bijvoorbeeld het pakket direct via `python -m` aanroepen); de deny op directe pywikibot-aanroepen en het ontbreken van MCP-schrijfrechten beperken dat. De deny op het bewerken van `voorstellen/` maakt het voor de Agent in Claude Code moeilijker om in smaak A zelf akkoord te geven; [Inferred] schrijven via een shell-commando blijft mogelijk, dus dit is een extra drempel en geen garantie. Namen van eventuele MCP-schrijf-Tools komen als `mcp__mediawiki__<tool>` in `deny`.

[Inferred] Een project-`settings.json` geldt voor de Sessie in de map waarin Claude Code start; daarom staat hij zowel in de root als in elke wiki-map, beide gegenereerd uit één bron.

Optioneel, later: `.claude/agents/<rol>.md` voor Agentprofielen (5.9).

### 5.16 Dezelfde architectuur in OpenCode en andere harnesses

Portable delen (Rules, Skills, Workflows, schemas, CLI, run-State, gate) zijn identiek. Per harness verschilt alleen:

**OpenCode.** `wikis/gemma-online/opencode.json` (gegenereerd):

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
      "*llmwiki publish apply*": "ask",
      "*llmwiki export apply*": "ask",
      "*pywikibot*": "deny"
    }
  }
}
```

[Verified] `instructions` bestaat in `opencode.json`; [Verified] OpenCode kent de permissiewaarden `allow`, `deny` en `ask` met wildcards (gedocumenteerd voor `permission.skill`). [Inferred] Dezelfde vorm voor `permission.bash` en de vorm van het `mcp`-blok; verificatie in sectie 8. Gebruikersomgeving: `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` zolang de Claude Code-brug aanwezig is.

**Codex.** `wikis/gemma-online/.codex/config.toml` (gegenereerd):

```toml
[mcp_servers.mediawiki]
command = "npx"
args = ["-y", "<mediawiki-mcp-server-pakket>"]
env_vars = ["MW_GEMMA_USER", "MW_GEMMA_PASSWORD"]
env = { MW_API_URL = "https://www.gemmaonline.nl/w/api.php" }
```

In `wiki-publish/agents/openai.yaml`: `policy.allow_implicit_invocation: false`. [Verified] Codex leest skills uit `.agents/skills/` en AGENTS.md zonder verdere configuratie. [Inferred] Veldnamen `env_vars` en `env`; verificatie in sectie 8. Laag 2 van de gate rust in Codex op de goedkeuringsmodus: [Inferred] in een modus die commando's buiten de sandbox of met netwerktoegang laat goedkeuren, vraagt `publish apply` (dat netwerk nodig heeft) om goedkeuring. Verificatie in sectie 8.

**VS Code/Copilot.** `wikis/gemma-online/.vscode/settings.json`:

```json
{
  "chat.useAgentsMdFile": true,
  "chat.useCustomizationsInParentRepositories": true
}
```

en `wikis/gemma-online/.vscode/mcp.json` met een `servers`-blok voor `mediawiki`. [Verified] VS Code leest `.agents/skills/` en ondersteunt `disable-model-invocation`. [Inferred] Laag 2 van de gate: VS Code vraagt goedkeuring voor terminalcommando's tenzij ze op een auto-approve-lijst staan; de generator zet `publish apply` en `export apply` nooit op die lijst.

**Cursor.** `wikis/gemma-online/.cursor/mcp.json` met `mcpServers.mediawiki`; verder 5.14. [Verified] Cursor leest `.agents/skills/` en AGENTS.md en ondersteunt `disable-model-invocation`. [Inferred] Laag 2 van de gate: Cursor vraagt goedkeuring voor terminalcommando's buiten de toegestane lijst; dezelfde regel als bij VS Code.

**Generator.** `llmwiki harness sync` schrijft al deze bestanden uit `wiki.yaml` en de skill-directories; `llmwiki harness check` faalt als een gegenereerd bestand afwijkt van wat de generator zou schrijven, als er een CLAUDE.md op een wiki-pad staat, of als een brug verouderd is. `check` draait in een pre-commit-hook en in CI. Gegenereerde bestanden beginnen, waar het formaat commentaar toestaat, met de regel dat ze gegenereerd zijn en uit welke bron.

Rechtvaardiging van deze adapterlaag tegenover het principe "geen abstractie om de abstractie": zonder generator zouden per wiki vijf MCP-configuraties met dezelfde informatie in vijf syntaxen met de hand worden onderhouden, en zou de Claude Code-brug handmatig moeten worden aangelegd op elk platform. De generator voegt geen nieuw concept toe; hij vertaalt één portable bron naar bestaande harness-formaten, en elk gegenereerd bestand blijft met de hand leesbaar en schrijfbaar.

### 5.17 Onboarding: werkplek controleren en herstellen

**Doel.** Een nieuwe collega kloont de repository, opent een wiki-map in een harness, stelt een Vraag en kan binnen enkele minuten werken, zonder handmatig bestanden te verplaatsen, paden in te stellen of rechten te regelen.

**Wat er na klonen ontbreekt.**

| Onderdeel | Waarom het ontbreekt | Gevolg zonder herstel |
|---|---|---|
| Claude Code-brug `.claude/skills/` | Gitignored (5.7) | Claude Code ziet geen Skills |
| Python-omgeving | `uv sync` nog niet gedraaid | `llmwiki` werkt niet |
| Credentials | Omgevingsvariabelen staan niet in Git | MCP-server en publicatie werken niet |
| Goedkeuring projectservers en vertrouwen van de map | Moet per gebruiker in het harness | [Verified] Claude Code start projectservers uit `.mcp.json` pas na goedkeuring; [Inferred] Codex laadt projectconfiguratie alleen in een vertrouwd project |

De gegenereerde harness-configuratie (MCP, instellingen, permissies) staat wel in Git en is dus direct aanwezig.

**Kip-en-ei.** De controle kan geen Skill zijn: zonder brug ziet Claude Code geen Skills. [Verified] Alle vijf harnesses lezen AGENTS.md zonder voorbereiding. De controle-instructie staat daarom bovenaan de root-AGENTS.md:

```markdown
## Werkplek eerst
Bij de eerste Vraag in een Sessie, vóór inhoudelijk werk:
1. Draai `uv run python -m llmwiki workspace-check`.
   Werkt `uv` niet: leg de gebruiker in gewone taal uit hoe `uv` wordt geïnstalleerd
   (zie README, sectie Installatie) en stop.
2. Meldt workspace-check `herstelbaar`: vraag de gebruiker of je de werkplek mag inrichten,
   draai dan `uv run python -m llmwiki workspace-check --fix` en geef de meldingen in gewone taal door.
3. Meldt workspace-check `actie gebruiker`: leg per punt uit wat de gebruiker moet doen
   en begin niet aan inhoudelijk werk tot workspace-check `ok` meldt.
4. Meldt workspace-check dat Skills pas na herladen beschikbaar zijn: zeg dat tegen de gebruiker.
```

**`llmwiki workspace-check`.**

| Controle | `--fix` doet | Anders: melding aan gebruiker |
|---|---|---|
| Python-omgeving aanwezig en actueel | `uv sync` | — |
| Brug aanwezig en actueel | `harness sync` (beheerde kopie met bronhash) | — |
| Geen CLAUDE.md of CLAUDE.local.md op een wiki-pad | — | Uitleg dat dit bestand de wiki-Rules uitschakelt, met voorstel het te hernoemen |
| Credentials voor een sync-wiki (alleen namen, nooit waarden) | — | Opmerking, niet blokkerend: welke variabele ontbreekt, dat die alleen nodig is voor werk met die wiki, en hoe je die instelt |
| Commando voor de MCP-server beschikbaar (bijv. `npx`) | — | Opmerking, niet blokkerend: welk programma ontbreekt; alleen nodig voor werk met een sync-wiki |
| Gegenereerde permissieregels voor de gate aanwezig | `harness sync` | — |
| Onafgeronde runs | — | Lijst, zodat de Agent kan voorstellen te hervatten |
| Afgeronde runs ouder dan bewaartermijn | `run prune` | — |

Uitvoer: een korte tekst in gewone taal en, met `--json`, een machineleesbare status (`ok`, `herstelbaar`, `actie gebruiker`) voor de Agent. `workspace-check` zonder `--fix` wijzigt niets en is in de permissies vooraf toegestaan, zodat de eerste controle geen goedkeuringsvraag oplevert.

**Platformonafhankelijke brug.** De brug gebruikt op ieder besturingssysteem beheerde kopieën (5.7), zodat symlinkrechten en Windows Developer Mode geen rol spelen. Na wijziging van een canonieke skill meldt `workspace-check` de verouderde kopie en kan `--fix` haar opnieuw opbouwen.

**Herladen na eerste inrichting.** [Verified] Claude Code ziet een skills-map die bij de start van de Sessie nog niet bestond pas na `/reload-skills`; [Verified] Codex adviseert een herstart als een nieuwe Skill niet verschijnt. `workspace-check` meldt daarom na het aanmaken van de brug per harness wat de gebruiker moet doen. De Agent zegt dat de Skills beschikbaar zijn, niet dat ze geladen zijn: of een Skill in de Context wordt geladen, beslist het harness.

**Wat niet te automatiseren is.** Goedkeuren van projectservers, vertrouwen van de map en invullen van credentials blijven menselijke handelingen. Dat is bedoeld: een gekloonde repository hoort zichzelf geen toegang te geven. `workspace-check` zorgt dat de gebruiker precies weet welke handeling nodig is.

**Tijdsduur.** [Speculative] "Binnen enkele minuten" hangt af van de downloadtijd bij de eerste `uv sync` en van de start van de MCP-server; dit wordt gemeten in de pariteitstest (sectie 8).

### 5.18 Soorten wiki's: sync, curatie en knowledge-base

**Correctie (deze versie).** Eerdere versies van dit document kenden drie typen A/B/C, waarbij "type A" (sync) óók de domein-lens (`onderwerpen/`, `bronnen/<onderwerp>/`) en het `records/`-archief van curatie kreeg, en "hybride" een eigen vierde letter-variant was. Onderzoek tijdens de bouw van Klus 2/3, tegen een al bestaande, in productie zijnde buursetup (een reëel MediaWiki-beheerproject met een aparte kennisbank ernaast, bewust van elkaar gescheiden), liet zien dat dit twee aparte problemen samenvoegde die niets met elkaar te maken hebben: (1) een site beheren (direct bewerken, git-diff-review, publiceren) en (2) kennis opbouwen (met of zonder formele curatiestatus). Vandaar de herziening hieronder. Wiki-soorten heten voortaan bij naam (`sync`/`curation`/`knowledge-base`), nooit als letter — dat botste leesbaar met "Model A–D" (4) en "smaak A/B" (5.13).

Een LLM-wiki heeft niet altijd een MediaWiki-site als bron van waarheid. De architectuur kent drie soorten. Ze delen Rules, Skills, run-State, gate en de centrale bronnen (5.19); ze verschillen in doel, contentformaat en de laatste fase.

| | `sync` | `curation` | `knowledge-base` |
|---|---|---|---|
| Doel | Een MediaWiki-site beheren | Gestructureerde kennis opbouwen, optioneel tot een export | Ongestructureerde kennis opbouwen: notities, adviezen, ontwerpen, architectuurdocumenten |
| Voorbeeld | GEMMA Online (MediaWiki) | Beleidskader-analyse; begrippen voor ArchiMate/UML | Een projectkennisbank die redactie op een sync-wiki voedt |
| Bron van waarheid | Externe site | Repository (Markdown in Git) | Repository |
| Pagina's | `content/` in wikitext, exacte werkkopie | `onderwerpen/`, `bronnen/`, `kandidaten/` in Markdown | `<onderwerp>/<document>.md`, vrije indeling |
| Curatiestatus | Nee | Optioneel: `kandidaat` → `review` → `goedgekeurd` | Nee |
| Laatste fase | PUBLISH na akkoord (git-diff-review) | PROMOTE; met een ingevuld `exports:`-blok: daarna EXPORT per doel | Geen — review is een gewone `git diff`/commit |
| MediaWiki/MCP nodig | Ja | Alleen als MediaWiki een exportdoel is | Nee |
| Archief | `log.md` (5.11) | De pagina's zelf plus `log.md` | De documenten zelf |

Wat voorheen "hybride" (type C) heette, is geen aparte soort: het is gewoon een `curation`-wiki met een ingevuld `exports:`-blok. Zonder dat blok stopt de workflow na PROMOTE.

**Keten in het gemeentelijke landschap.** Curatie-wiki's volgen elkaar op; de uitkomst van de ene is bron voor de volgende, en komt uiteindelijk als redactionele wijziging bij een sync-wiki terecht:

```text
Beleidskader (curation) → Begrippen & ArchiMate (curation + exports) → Informatiemodellen (curation + exports) → GEMMA Online (sync)
```

Overdracht loopt via de centrale bronnen, niet via verwijzingen tussen wiki's: een goedgekeurde export (of een `knowledge-base`-document) wordt met `llmwiki source add --from-export <wiki>/<pad>` een nieuwe bron in `sources/` met eigen tags, en de volgende wiki neemt die op via zijn bronfilter (5.19). Regel 3 uit 5.4 blijft zo gelden: wiki's verwijzen niet naar elkaars interne pagina's — ook niet een sync-wiki naar een `knowledge-base`-wiki.

Keuzes:
- **Eén contentformaat per wiki.** Wikitext alleen in `content/` van een sync-wiki. Markdown in de curatiemappen en in `knowledge-base`. Omzetting naar wikitext of XMI gebeurt alleen bij publiceren/export.
- **Bij curatie en knowledge-base zijn de pagina's het archief.** Geen aparte records voor bronnen en kandidaten — dubbele vastlegging. Het logboek is `log.md`. Een sync-wiki gebruikt óók `log.md` (één regel per publicatie, met titel en revisie) — geen apart `records/`-archief meer; de conflictbasis is `revisies.json`, geen `.meta.json`-sidecar per pagina (5.12, 5.13).
- **`knowledge-base` gebruikt geen run/gate.** Er is niets om te publiceren; `llmwiki run start` weigert expliciet voor dit type (in plaats van stil iets verkeerds te doen). Review is een gewone `git diff`/commit.
- **De Obsidian-vault is de repository-root.** Alleen dan werken relatieve links van een wiki naar `sources/` in Obsidian; [Inferred] Obsidian opent geen links naar bestanden buiten de vault. `.obsidian/app.json` in de root zet Markdown-links op relatief pad en sluit `tools/` en `tests/` uit via de uitsluitfilters. [Inferred] Mappen die met een punt beginnen (`.work`, `.agents`, `.claude`) toont Obsidian standaard niet.
- **Bronnen per onderwerp (curatie).** Een curatie-wiki deelt zijn bronanalyses in naar onderwerp: `bronnen/<onderwerp>/<bron-id>.md`, waarbij `<onderwerp>` gelijk is aan de id van `onderwerpen/<onderwerp>.md`. Een bron die bij meer onderwerpen hoort, staat bij het hoofdonderwerp; andere onderwerppagina's linken ernaar. De mapnamen zijn standaardwaarden: een wiki kiest eigen namen via `page_types.<type>.dir` in `wiki.yaml` (bijv. `begrippen/` en `bronanalyses/` in `gemma-archimate-model`). `llmwiki run start --onderwerp` zoekt de onderwerppagina in de map van paginatype `onderwerp`.
- **Paginatype-schema.** Staat bij een paginatype in `wiki.yaml` een `schema`, dan valideert `llmwiki validate --schema page` de frontmatter daartegen. Relatieve `$ref`s worden opgelost vanuit de map van het schema, zodat een wiki gedeelde definities in één bestand kan zetten. Gestagede pagina's worden met `--run <run-id>` beoordeeld op hun doelpad uit `changeset.json` (id, relatieve links; de andere pagina's uit dezelfde changeset gelden als bestaand).
- **Promotie per status.** `promote apply` keurt alleen pagina's goed die de Agent op `review` zette. Een `kandidaat` (nog voor te leggen) wordt ongewijzigd geschreven, zonder logregel; een gestagede `goedgekeurd` weigert het plan.

#### Repositorystructuur

```text
llm-wikis/                          Git-root = Obsidian-vault
├── AGENTS.md                       repository-Rules
├── .obsidian/app.json              linkinstellingen en uitsluitingen (rest gitignored)
├── sources/                        centrale bronnen, gedeeld door alle wiki's (5.19)
│   ├── raw/                        laag 1: originelen + conversie, onveranderlijk
│   │   ├── 2026-vng-omgevingsplan.pdf
│   │   └── 2026-vng-omgevingsplan.md
│   └── index/                      laag 2: gedeelde intake
│       └── 2026-vng-omgevingsplan.md
├── .agents/skills/                 generieke Skills (o.a. wiki-intake)
├── tools/llmwiki/                    deterministische core
└── wikis/
    ├── gemma/                      type sync: kale werkkopie
    │   ├── AGENTS.md · wiki.yaml
    │   ├── content/                MediaWiki-pagina's (.wiki, evt. .css/.js)
    │   ├── revisies.json           conflictbasis: pad → {titel, revid}, gecommit
    │   ├── log.md                  logboek, alleen aanvullen, door de CLI
    │   └── voorstellen/ · .agents/skills/ · .work/
    ├── gemma-kennis/                type knowledge-base
    │   ├── AGENTS.md · wiki.yaml
    │   └── <onderwerp>/<document>.md
    └── opzet2/                     type curation (met of zonder exports:)
        ├── AGENTS.md · wiki.yaml
        ├── log.md                  logboek, alleen aanvullen, door de CLI
        ├── voortgang.md            gegenereerd overzicht
        ├── onderwerpen/            ingang voor elke taak: <thema>.md
        ├── bronnen/<onderwerp>/    laag 3: domein-lens per bron
        ├── kandidaten/             met curatiestatus
        ├── export/                 alleen met exports:-blok, alleen via de gate
        ├── schemas/ · mappings/    paginamodellen; vertaling naar exportdoelen
        └── voorstellen/ · .agents/skills/ · .work/
```

`wiki.yaml` voor `sync` (kern; zie 5.10 voor de MCP-onderdelen):

```yaml
key: gemma-online
type: sync
site:
  family: gemmaonline                # pywikibot-family: families/gemmaonline_family.py (5.10a)
  code: en                           # hoofddoel = bron van waarheid
  server: redactie.gemmaonline.nl    # domein voor MCP-config
  articlepath: /wiki
  scriptpath: ""
test_targets:
  staging: { family: gemmaonline, code: staging }
content:
  layout: namespace                  # namespace (default) | category (per wiki, indien nodig)
  namespaces: [0]
publish:
  approval: document                 # smaak A of B, zie 5.13
mcp:
  target: site                       # altijd het hoofddoel, nooit een testdoel
work:
  retention_days: 30
```

`wiki.yaml` voor `curation` (kern, ongewijzigd):

```yaml
key: opzet2
type: curation                       # sync | curation | knowledge-base
sources:
  tags: [omgevingswet, dso]          # scoping: alleen bronnen met een van deze tags
  exclude_tags: [concept]
page_types:
  onderwerp: { dir: onderwerpen, schema: schemas/onderwerp.schema.json }
  bron:      { dir: bronnen,     schema: schemas/bron.schema.json, group_by: onderwerp }
  kandidaat: { dir: kandidaten,  schema: schemas/kandidaat.schema.json, curated: true }
curation:
  states: [kandidaat, review, goedgekeurd, afgewezen]
  gated: [goedgekeurd]
  approval: document                 # smaak A of B, zie 5.13
  min_reviewers: 1
exports:                             # leeg zonder exportdoel
  archimate: { format: archimate-oef, mapping: mappings/archimate.yaml, out: export/model.xml }
  xmi:       { format: xmi, script: tools/export_xmi.py, out: export/informatiemodel.xmi }
  csv:       { format: csv, page_type: kandidaat, out: export/kandidaten.csv }
```

`wiki.yaml` voor `knowledge-base` (kern):

```yaml
key: gemma-kennis
type: knowledge-base
sources:
  tags: [gemma]
```

Frontmatter-conventie voor alle Markdown-paginatypen (generiek; paginatypen voegen velden toe):

```yaml
---
id: kandidaat-zaakdossier            # stabiel, gelijk aan bestandsnaam zonder .md
type: kandidaat
status: review                       # alleen bij curated paginatypen
onderwerp: zaakgericht-werken        # id van de onderwerppagina
bronnen: [2026-vng-omgevingsplan]    # bron-id's uit sources/index: herleidbaarheid
bijgewerkt: 2026-09-27
---
```

#### Workflows

Twee generieke Workflow-Skills: `wiki-edit` voor `sync`, `wiki-update` voor `curation`. `knowledge-base` gebruikt losse capability-Skills (`wiki-kennis-ingest`) zonder Workflow-gate.

```text
sync:         PULL → BEWERK → VALIDATE → GATE → PUBLISH
curation:     INGEST → ASSESS → WRITE → VALIDATE → GATE → PROMOTE
                                                          → EXPORT (per doel, alleen met exports:)
knowledge-base: (geen run/gate) ingest → classificeren → document bijwerken
```

| Fase | `sync` | `curation` |
|---|---|---|
| PULL / INGEST | `llmwiki pull` haalt de pagina op naar `content/` (optioneel — kan al lokaal staan) | Laag 1 en 2 als de bron nieuw is (5.19); laag 3 in `bronnen/<onderwerp>/` |
| BEWERK / ASSESS | Agent past `content/` direct aan | Welke onderwerpen en kandidaten worden geraakt |
| — / WRITE | (geen aparte fase) | Markdown-pagina's; nieuwe kandidaten met `status: kandidaat`. De Agent mag `kandidaat` → `review` zetten |
| VALIDATE | Wikitext-controles | Frontmatter tegen schema, links, curatieregels, wiki-scripts |
| GATE | Publicatievoorstel met een git-diff (5.13) | Promotievoorstel; met `exports:` ook het exportvoorstel |
| Laatste fase | `publish apply` (pywikibot, na conflictcontrole tegen de live revisie) | `promote apply`, met `exports:` daarna `export apply` per doel |

De gate is dezelfde als in 5.13, met één extra controle bij sync: `publish apply` haalt vlak vóór schrijven de live revisie op en vergelijkt die met de basis in `revisies.json` — een tussentijdse externe wijziging wordt geweigerd, niet overschreven.

Wat anders is bij curatie:
- [Inferred] De Agent kan `status: goedgekeurd` zelf in een lokaal bestand schrijven. Daarom weigeren `llmwiki validate` en de pre-commit-hook elke pagina met een gated status zonder promotieregel in `log.md` met overeenkomende inhoudshash.
- Bij `min_reviewers` > 1 bevat `beoordeeld_door` een lijst; `promote apply` controleert het aantal.
- Wijzigt een goedgekeurde pagina inhoudelijk, dan zet VALIDATE hem terug naar `review`.

Een wiki-Workflow (bijv. `opzet2-update`) blijft dun, zoals in 5.8, en verwijst naar `wiki-update` (curatie) of `wiki-edit` (sync).

#### Tooling

MediaWiki is één van de doelen, geen vaste afhankelijkheid.

| Onderdeel | Plaats | Afhankelijkheden |
|---|---|---|
| Kern: run-State, gate, voorstellen, `log.md`, `voortgang.md`, workspace-check, harness sync, lint | `llmwiki` | Geen MediaWiki |
| Bronbeheer: `source add|list|show`, conversie naar Markdown, onveranderlijkheid van `raw/` | `llmwiki` (5.19) | Converter, keuze in Klus 3 |
| Markdown-validatie: frontmatter per paginatype, relatieve links, geen `[[wikilinks]]`, `id` = bestandsnaam, bron-id's bestaan in `sources/index/` en vallen binnen de scope, statusovergangen | `llmwiki validate` | Geen MediaWiki |
| MediaWiki: `pull`, `publish`, titelmapping (`titles.py`), conflictcontrole | groep `mediawiki` (standaard geïnstalleerd met `uv sync`) | pywikibot, met een family-bestand in de wiki-map en inloggegevens uit omgevingsvariabelen (5.10a) |
| ArchiMate Open Exchange-writer | `llmwiki` (generiek) | [Verified] Open standaard van The Open Group; nog te bouwen bij een concreet `exports:`-gebruik |
| UML/XMI-export (RSGB, MIM) | Wiki-script via `exports.xmi` | [Inferred] XMI-varianten verschillen per modelleertool; daarom eerst per wiki, generiek pas bij een tweede gebruiker |
| CSV-writer | `llmwiki` (generiek) | Geen; nog te bouwen bij een concreet `exports:`-gebruik |
| Vertaling paginatype → ArchiMate-element of UML-klasse | Wiki: `mappings/`, eventueel wiki-script | Domeinkennis blijft in de wiki |

Logboekdiscipline:
- `log.md` wordt alleen aangevuld, altijd door de CLI, één kop per gebeurtenis, bijvoorbeeld `## [2026-09-27] promote | kandidaat-zaakdossier | M. Jansen | a3f9` (curatie) of `## [2026-09-27] publish | Contact | M. Jansen | a3f9` (sync). Lint en pre-commit weigeren wijzigen of verwijderen van bestaande regels.
- `voortgang.md` wordt bij `run complete`, `promote apply` en `workspace-check` opnieuw gegenereerd (curatie): open runs, aantallen per status, wat wacht op review, laatste export per doel. Een sync-wiki heeft geen `voortgang.md` — `log.md` en `git log` volstaan voor een kale werkkopie.

Gevolgen:
- `llmwiki workspace-check` controleert bij curatie en knowledge-base geen MediaWiki-credentials of pywikibot-family, wel de Obsidian-instellingen in de root.
- `llmwiki harness sync` genereert MCP-configuratie alleen voor wiki's met een MediaWiki-doel (sync, of curatie met MediaWiki als exportdoel).
- Generieke Skills `wiki-write` en `wiki-validate` hebben per contentformaat een reference (`references/markdown.md`, `references/wikitext.md`).

### 5.19 Gedeelde bronnen en contextbescherming

**Drie lagen.**

| Laag | Plaats | Inhoud | Wie schrijft | Gedeeld |
|---|---|---|---|---|
| 1. Ruwe originelen | `sources/raw/<bron-id>.<ext>` en `sources/raw/<bron-id>.md` | Origineel (pdf, docx) en de Markdown-conversie met dezelfde naam | `llmwiki source add` (script) | Ja |
| 2. Technische index | `sources/index/<bron-id>.md` | Gegevens, samenvatting, trefwoorden, begrippen en inhoudsopgave met regelnummers; om context te sparen, geen schakel in de herleidbaarheid | `llmwiki source add` (gegevens, inhoudsopgave) en generieke Skill `wiki-intake` (tekst), één keer per bron | Ja |
| 3. Domein-lens | `wikis/<key>/<map uit wiki.yaml>/<onderwerp>/<bron-id>.md` (bijv. `bronnen/` of `bronanalyses/`) | Wiki-specifieke analyse en uittreksels met vindplaats, en onder de titel links naar laag 1 | Wiki-Skill tijdens INGEST | Nee |

Regels:
- **Bron-id** `<jaar>-<uitgever>-<korte-titel>`, kleine letters en koppeltekens; gelijk in alle drie lagen.
- **Herleidbaarheid loopt via links, van pagina naar brontekst.** Elke verwijzing naar een bron op een pagina is een relatieve link naar de domein-lens van die bron; de domein-lens heeft direct onder de titel een regel met links naar laag 1 (tekst, origineel, online), gemaakt met `llmwiki source bronregel --schrijf`. De keten is dus pagina → domein-lens → laag 1. Laag 2 zit niet in die keten: een bron-id in de frontmatter is voor het gereedschap, een link is voor de lezer.
- **Laag 1 is onveranderlijk.** Alles staat gewoon in Git, dus ook de pdf's. De pre-commit-hook staat in `sources/raw/` alleen toevoegen toe. Een nieuwe versie van een document krijgt een nieuw bron-id. [Inferred] De repository groeit met elke pdf; bij grote aantallen is Git LFS later zonder structuurwijziging in te voeren.
- **Conversie is deterministisch.** `llmwiki source add <bestand>` kopieert het origineel, zet het om naar Markdown, berekent een hash en weigert als het bron-id al bestaat. Het zet ook de inhoudsopgave in de index. `wiki-intake` controleert daarna de conversie steekproefsgewijs (koppen, tabellen) en meldt problemen in plaats van de conversie te herschrijven.
- **Laag 2 is generiek.** `wiki-intake` bevat geen wiki-kennis (regel 1 uit 5.4). Het schema `source-index.schema.json` in de core legt de frontmatter vast: id, titel, uitgever, datum, versie, pad en hash van laag 1, tags. Wat in de tekst van de index staat en waarom: zie *Laag 2 als technische index* hieronder.
- **Hergebruik.** Bestaat `sources/index/<bron-id>.md` al, dan slaat INGEST laag 1 en 2 over en maakt alleen de domein-lens.

- **Ophalen via URL.** `llmwiki source add --url <url>` haalt een bron op en zet HTML deterministisch om naar Markdown: tekst blijft letterlijk, alleen opmaakruis (scripts, navigatie, voettekst, knoppenteksten) verdwijnt. Bekende weergave-URL's worden eerst omgezet naar de download-URL (bijv. iBabs, `*.bestuurlijkeinformatie.nl`). Pdf's worden omgezet met pymupdf4llm (groep `pdf`, standaard geïnstalleerd met `uv sync`). De intake legt `url`, `url_pagina` en `opgehaald` vast.
- **Brontype en bronvoorrang.** De intake kent een optioneel `brontype` (`wet`, `informatiemodel`, `beleid`, `overig`, `model`). Een wiki kan in `wiki.yaml` `bronvoorrang` een leesvolgorde op brontype vastleggen; `run start --onderwerp` zet de bronlijst in die volgorde. Wat de rangorde inhoudelijk betekent (bijv. voor definities), is een wiki-regel.

**Waarom één intakebestand per bron.** Laag 2 is `sources/index/<bron-id>.md`, niet één catalogus.
- *Herleidbaar via de bestandsnaam.* Het bron-id is in alle drie lagen de bestandsnaam; bestaan en uniciteit zijn een bestandscontrole (`source add` weigert een bestaand id, `validate` zoekt het bestand op).
- *Contextbescherming.* Een run leest alleen de intakes van de bronnen uit de onderwerppagina; een catalogus met samenvattingen zou steeds helemaal geladen worden.
- *Een intake is een pagina.* Metadata én tekst (samenvatting, inhoudsopgave), met hetzelfde frontmatter-, schema- en lintgereedschap als elke andere pagina.
- *Backlinks.* Pagina's linken naar de domein-lens, en de domein-lens naar laag 1; Obsidian toont per domein-lens welke pagina's haar gebruiken. De index heeft geen backlinks nodig.
- *Git.* Gelijktijdige toevoegingen raken verschillende bestanden (geen merge-conflicten); `git log` per bron toont de historie van de intake.
- *Niet in laag 1.* `sources/raw/` is onveranderlijk en letterlijk; een samenvatting of correctie achteraf kan daar niet staan.

Afgewezen: één catalogusbestand (geen ruimte voor tekst, conflicten, alles laden), de intake in de frontmatter van `raw/<bron-id>.md` (laag 1 is onveranderlijk) en een intake per wiki (dubbel werk, in strijd met principe 3). Nadeel: geen overzicht in één oogopslag; dat levert `llmwiki source list` of een gegenereerd overzicht, dat nooit zelf de bron van waarheid is.

**Laag 2 als technische index (analyse, 2026-09-30).** Laag 2 is een hulpmiddel voor de Agent om context te sparen, geen document voor de lezer en geen schakel in de herleidbaarheid (die loopt van pagina via domein-lens naar laag 1, zie hierboven). Tot deze datum bevatte geen enkele index tekst: `source add` schreef "Nog geen samenvatting." en de bedoelde Skill `wiki-intake` bestond niet.

*Omvang van laag 1.* 271 bronnen, samen 2,6 miljoen woorden. De mediaan is 1.700 woorden, 10% is langer dan 20.000 woorden, de grootste 266.000. De Wet op de lijkbezorging telt 8.400 woorden. Eén lange bron helemaal lezen kost meer context dan de rest van een run; kiezen wát je leest is dus de winst.

*Vragen die de index moet beantwoorden zonder laag 1 te openen:*

| Vraag van de Agent | Sectie in de index | Wie maakt het |
|---|---|---|
| Hoort deze bron bij mijn vraag of onderwerp? | Frontmatter (brontype, tags, `beschrijving`), `## Samenvatting` (reikwijdte, ook wat níet in de bron staat) | Gereedschap en Model |
| Onder welk woord vind ik haar? | `## Trefwoorden`, met synoniemen en spreektaal die niet in de titel staan | Model |
| Waar in de tekst staat begrip X? | `## Begrippen`, per begrip het regelnummer in laag 1 | Model, regelnummers opgezocht |
| Welk deel moet ik lezen, en wat kost dat? | `## Inhoud`, per kop het regelnummer en het aantal woorden tot de volgende kop | Gereedschap (`llmwiki source inhoud`) |
| Welke andere bronnen hangen ermee samen? | `## Verwijst naar` | Model |
| Is dit de actuele versie? | Frontmatter (`datum`, `versie`, `opgehaald`), status in de samenvatting | Gereedschap en Model |

*Keuzes.*
- **Regelnummers, geen paginanummers of paragraaftitels.** Een Agent leest een bestand op regelnummer (offset); laag 1 is onveranderlijk, dus een regelnummer blijft geldig. Paragraaftitels zijn niet altijd uniek en pdf-conversies hebben geen paginanummers.
- **Woorden als maat voor de kosten.** Het aantal woorden per sectie laat vóór het lezen zien of een hoofdstuk in zijn geheel past.
- **Het gereedschap maakt wat vastligt, het Model wat begrip vraagt.** Inhoudsopgave, omvang en gegevens zijn deterministisch en staan er direct na `source add`; samenvatting, trefwoorden en begrippen vragen lezen en komen van `wiki-intake`.
- **Klein houden.** Tekstsecties samen hooguit 400 woorden en de inhoudsopgave hooguit ongeveer 60 rijen: dan leest een Agent de index van tien bronnen voor minder dan de tekst van één middelgrote bron. Bij een bron onder 2.000 woorden volstaan samenvatting en trefwoorden; de tekst zelf lezen is dan goedkoop.
- **Zoeken met gewone middelen.** Trefwoorden en begrippen staan als platte tekst, zodat zoeken over `sources/index/` (grep, de zoekfunctie van de harness of Obsidian) direct de juiste bron en het regelnummer geeft. Een eigen zoekopdracht in `llmwiki` volgt pas als dat aantoonbaar tekortschiet (principe 7).

*Niet in de index:* interpretatie voor één wiki (dat is de domein-lens), citaten waarop een pagina steunt (pagina's citeren laag 1 via de domein-lens), en links vanuit pagina's (een pagina linkt nooit naar de index).

**Contextbescherming.** Doel: een wiki verzuipt niet in alle bronnen van de repository, en een Sessie laadt alleen wat de taak nodig heeft.

| Maatregel | Werking | Afdwinging |
|---|---|---|
| Scoping via tags | `sources.tags` en `sources.exclude_tags` in `wiki.yaml` bepalen welke bronnen een wiki ziet | `llmwiki source list` toont alleen bronnen in scope; `validate` meldt verwijzingen naar bronnen buiten scope |
| Taakgericht werken | Elke run start vanuit een onderwerppagina: `/opzet2-update onderwerpen/zaakgericht-werken.md`. De `bronnen:`-lijst in die pagina bepaalt welke bronnen worden gelezen | `llmwiki run start --onderwerp` legt de bronlijst vast in de State; INGEST en ASSESS krijgen alleen die bron-id's |
| Leesvolgorde | Eerst laag 2 (kort), dan laag 3; uit laag 1 alleen de passages die index of domein-lens aanwijzen, op regelnummer | Instructie in `wiki-assess` en de wiki-Rules |
| Kleine index | Tekstsecties in laag 2 samen hooguit 400 woorden, inhoudsopgave hooguit ongeveer 60 rijen | Instructie in `wiki-intake` |

[Inferred] De Obsidian-vault op root-niveau toont alle bronnen aan de mens; de scoping geldt voor de Agent en de CLI, niet voor wat een redacteur kan openen.

---

## 6. Portability-analyse

### 6.1 Repository-portability (Linux, Windows, macOS)

| Risico | Maatregel |
|---|---|
| Symlinks in Git | Geen; de lokale brug bestaat uit beheerde kopieën |
| Regeleinden | `.gitattributes`: `* text=auto eol=lf`; binaire bronnen expliciet `binary` |
| Hoofdletterongevoelige bestandssystemen, verboden tekens, gereserveerde namen | Titelmapping met hash-suffix (5.13) |
| Padlengte Windows | Korte mapnamen; `git config core.longpaths true` in README |
| Unicode-normalisatie macOS | NFC bij schrijven van bestandsnamen |
| Shell-verschillen | Alleen Python-CLI; geen shell-scripts in Workflows |
| Python-omgeving | `uv` met lockfile; zelfde versies op elk OS |
| Credentials | Omgevingsvariabelen; geen paden naar gebruikersmappen in Git |
| Grote bronbestanden | Git LFS voor binaire bronnen boven een drempel |

[Inferred] Met deze maatregelen ziet de repository er na `git clone`, `uv sync` en `llmwiki harness sync` op elk OS hetzelfde uit; de gitignored brug gebruikt overal dezelfde kopietechniek en inhoud.

### 6.2 Harness-portability

Ondersteund door: AGENTS.md (alle vijf), Agent Skills-formaat (alle vijf), `.agents/skills/` (vier van vijf), MCP (alle vijf), Workflow als Skill (alle vijf), artefacten in bestanden (alle vijf), CLI via shell-Tool (alle vijf).

Beperkt door: skill-locatie Claude Code (brug), bovenliggende discovery VS Code (instelling) en Cursor (onbekend), MCP-clientformaten (generator), Agentprofielen (bewust uitgesteld), invocatiebeleid en permissies (harness-annotaties; de gate rust op een 'ask'-regel per harness, zie V5).

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
| K13 | Publicatiegate: akkoord via publicatievoorstel (smaak A) of bevestigingswoord (smaak B), per wiki kiesbaar; afgedwongen door een harness-goedkeuringsklik ('ask') op `publish apply` en `export apply`; revisie- en plan-hashcontrole in code | K + H |
| K14 | Eén generator voor alle harness-bindingen, met `check` in pre-commit en CI | K |
| K15 | Kladblok (gitignored, met bewaartermijn) gescheiden van het archief (`log.md`, bij curatie ook de pagina's) in Git; `log.md` door de CLI afgeleid, niet door het Model geschreven; geen apart `records/`-archief | K |
| K16 | Werkplekcontrole via `llmwiki workspace-check`, aangestuurd vanuit de root-AGENTS.md; Windows-rechten nooit blokkerend | K |
| K17 | Architectuurmodel-export valt onder dezelfde gate; exporteur is een wiki-script, gate is generiek | K |
| K18 | Documentatie in drie lagen: Kompas, Kluswijzer, onderbouwing | K |
| K19 | Drie wiki-soorten (`sync`, `curation`, `knowledge-base`), benoemd naar doel niet naar letter, met één contentformaat per wiki; wat voorheen "hybride" heette is `curation` met een ingevuld `exports:`-blok, geen aparte soort; laatste fase PUBLISH (sync), PROMOTE of PROMOTE + EXPORT (curation), of geen gate (knowledge-base), bepaald door `wiki.yaml` | K |
| K20 | Curatiestatus in frontmatter; gated statussen alleen geldig met promotieregel in `log.md`, gecontroleerd door validate en pre-commit | K |
| K21 | MediaWiki als optionele extra van `llmwiki`; ArchiMate Open Exchange en CSV als generieke writers (nog te bouwen bij een concrete `exports:`-behoefte), vertaling van paginatypen per wiki | S + K |
| K22 | Centrale bronnen in drie lagen (raw, index, domein-lens) met één bron-id; raw onveranderlijk, alles in Git | K |
| K23 | Contextbescherming: scoping via tags in `wiki.yaml`, runs starten vanuit een onderwerppagina | K |
| K24 | Obsidian-vault is de repository-root; overdracht tussen wiki's in de keten via `sources/` | K |
| K25 | `knowledge-base` is een eigen wiki-soort voor ongestructureerde kennisopbouw (notities, adviezen, ontwerpen, architectuurdocumenten), zonder run/gate; niet hetzelfde als `curation` (gestructureerd, richting een export) en niet een submap van een sync-wiki | K |
| K26 | Sync-wiki: kale werkkopie zonder domein-lens of `records/`; conflictbasis `revisies.json` (gecommit, pad → titel/revid), geen `.meta.json`-sidecar per pagina; MediaWiki-toegang via MCP (alleen-lezen, altijd hoofddoel) voor verkennen en pywikibot (via `llmwiki pull`/`publish`) voor lezen/schrijven, met een family-bestand in de wiki-map en inloggegevens uit omgevingsvariabelen (5.10a) | K |

---

## 8. Open punten en verificatieprocedure

Punten gemarkeerd als [Speculative] die de architectuur raken:

| Nr | Vraag | Test | Gevolg bij negatief resultaat |
|---|---|---|---|
| V1 | Laadt OpenCode bij starten in `wikis/gemma-online` ook de root-AGENTS.md? | Vraag in een nieuwe Sessie: "welke instructiebestanden zijn geladen?" | Geen: `instructions` in `opencode.json` dekt dit al |
| V2 | Vindt Cursor bij openen van alleen `wikis/gemma-online` root-skills en root-AGENTS.md? | Open map, controleer Customize > Skills | Activeer `--cursor-wiki-root`-brug |
| V4 | Hoe gaan VS Code en Cursor om met identieke skills in `.agents/skills/` en `.claude/skills/`? | Beide aanwezig, controleer skill-lijst | Brug alleen op Claude Code-machines of VS Code `chat.agentSkillsLocations` beperken |
| V5 | Vraagt elk harness bij een 'ask'-regel op `publish apply` altijd om goedkeuring, ook in modi met automatische goedkeuring? | Laat de Agent `publish apply` aanroepen in een testwiki, eerst in de standaardmodus, daarna in de auto-approve-modus van dat harness | Spelregel "automatische goedkeuring uit bij publiceren" is dan de enige bescherming voor smaak B; overweeg voor dat harness alleen smaak A, en voor Claude Code de MCP-variant met `anthropic/requiresUserInteraction` |
| V6 | Exacte veldnamen MCP-config OpenCode, VS Code, Cursor | Generator-uitvoer laden, server moet verbinden | Generator aanpassen |
| V7 | Leest Codex `.agents/skills/` en `AGENTS.md` native in `wikis/gemma-online` zonder gegenereerd bestand, zoals 5.14 aanneemt? | Start Codex in `wikis/gemma-online`, vraag welke Rules/Skills geladen zijn | Alsnog een gegenereerd Codex-bestand toevoegen aan `harness.py` |
| V8 | Volgt elk harness de instructie "Werkplek eerst" uit de root-AGENTS.md bij de eerste Vraag? | Nieuwe kloon, eerste Vraag is inhoudelijk | Instructie scherper en hoger in AGENTS.md; in Claude Code eventueel een SessionStart-hook die `workspace-check` draait (H) |
| V9 | Duur van de eerste inrichting op een schone machine | Tijd meten van klonen tot eerste `workspace-check ok`, per besturingssysteem | Afhankelijkheden beperken of vooraf te installeren programma's in README noemen |
| V10 | Resolvet het relatieve `CONFIG`-pad naar `mediawiki-mcp.config.json` (5.10) correct in elke harness (child-process-cwd bij een stdio-server verschilt mogelijk per harness)? | MCP-server registreren, `whoami`/lees-tool aanroepen in elke harness vanuit `wikis/gemma-online` | Generator laat per harness een absoluut, lokaal-berekend pad schrijven (dan niet meer gecommit voor die ene harness-file) |
| V11 | Werkt inloggen met botwachtwoorden uit omgevingsvariabelen (5.10a) tegen redactie en staging, inclusief de extra HTTP-toegangslaag van staging en het aangenomen scriptpad `""` op staging? | Variabelen zetten, `uv run python -m llmwiki pull --wiki wikis/gemma-online --titel "Wat is GEMMA" --doel staging`, daarna zonder `--doel`; één testpublicatie alleen op staging | Scriptpad of protocol in `gemmaonline_family.py` aanpassen; bij een login-API die `action=login` weigert: gewoon account via `clientlogin` of OAuth (pywikibots `authenticate` met vier sleutels) |

Pariteitstest per harness (handmatig, per release van een harness of van de core):

1. `llmwiki harness check` slaagt.
2. Start in `wikis/_template` (testwiki tegen een test-MediaWiki). Vraag: "Welke Rules en Skills heb je geladen?" Controleer: root- en wiki-Rules, generieke en wiki-Skills, elke naam één keer.
3. Voer skill `wiki-edit` (sync) of `<key>-update` (curatie) uit met een vaste testbron.
4. Controleer dat alle artefacten tegen hun schema valideren en dat de Agent stopt bij de gate.
5. Smaak A: controleer dat `publish apply`/`promote apply` weigert zolang het voorstel op `nee` staat of een verouderde plan-hash heeft. Smaak B: controleer dat "prima" geen publicatie start. Beide: controleer dat het harness om goedkeuring vraagt.
6. Controleer dat na publicatie een regel in `log.md` bestaat en dat een afgebroken run niets achterlaat buiten `.work/`.

---

## 9. Invoeringsvolgorde

De uitvoerbare volgorde staat in `docs/kluswijzer.md` (vier klussen: Fundament, Werkplek, Gereedschapskist, Eerste bewoner). Daarna, alleen bij aanleiding:

- Agentprofielen alleen als de pariteitstest of het gebruik een concreet kosten- of veiligheidsprobleem toont (5.9).
- Extractie van `llmwiki` en de generieke Skills naar een eigen repository alleen als een andere repository ze nodig heeft; de structuur hoeft daarvoor niet te veranderen.

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
