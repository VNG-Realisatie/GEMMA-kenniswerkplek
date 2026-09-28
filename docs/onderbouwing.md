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
| Symlinks | Onbekend of beschikbaar | Geen symlinks in Git. Lokale koppelingen alleen via script met terugval op kopiëren |
| PUBLISH | Altijd menselijke gate, zonder terminalcodes; per wiki kiesbaar tussen vrijgave via document (smaak A) of via bevestigingswoord in de chat (smaak B); geldt ook voor architectuurmodel-export | Akkoord van de redacteur plus een goedkeuringsklik in het harness (5.13) |
| Tussenresultaten | Kladblok persistent op schijf, niet in Git, na afronding automatisch opgeruimd | Run-directory per wiki, gitignored, met bewaartermijn (5.11) |
| Blijvende vastlegging | Bronverslag, kandidaat-begrippen en logboek in Git, niet op MediaWiki | Bronverslag in centrale bronindex (5.19); kandidaten en logboek in `records/` (type A) of in de pagina's plus `log.md` (type B/C) |
| Onboarding | Nieuwe collega werkt binnen enkele minuten, zonder handmatige inrichting | Controle en herstel via `llmwiki workspace-check`, aangestuurd vanuit de root-AGENTS.md (5.17) |
| Hergebruik core | Mogelijk later buiten deze repository | Core moet als pakket extraheerbaar zijn zonder herstructurering |
| Content-opslag | Wikitext plus metadata per pagina (type A); Markdown met frontmatter (type B/C) | Sidecar-bestand per pagina (A) of frontmatter (B/C); één formaat per wiki (5.18) |
| Wiki-typen | Naast MediaWiki-sync ook lokale Obsidian-curatie en hybride export (ArchiMate, UML/XMI) | Drie typen in een keten; MediaWiki wordt een optioneel doel; vault = repository-root; pagina's zijn het archief bij B/C; `voortgang.md` gegenereerd (5.18) |
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
| **LLM-wiki** | Een zelfstandige eenheid bestaande uit: content (wikitext of Markdown), een domein-lens op de centrale bronnen, wiki-Rules, wiki-Skills (waaronder Workflows), wiki-schemas, wiki-scripts en een wiki-manifest. Is van type A (sync met één MediaWiki-site), B (lokale curatie in Markdown) of C (curatie plus export naar externe doelen); zie 5.18. | Repository (K) |
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
| **Record** | Blijvend, leesbaar verslag van een afgeronde run in Git (type A): kandidaat-begrippen en logboek; de bron staat in de centrale bronindex. Afgeleid uit artefacten, niet door het Model geschreven. | Repository (K) |
| **Publicatievoorstel** | Leesbaar Markdown-document per run met samenvatting, wijzigingen en akkoordvelden; basis voor de menselijke gate. | Repository (K) |
| **Harness** | Runtime die Model, Tools, Context, permissies, discovery, MCP-verbindingen, subagents en gebruikersinterface levert. Voorbeelden: Claude Code, OpenCode, VS Code/Copilot, Cursor, Codex. | Leverancier (H) |
| **Model** | Het LLM. Levert: interpretatie van de Vraag, redeneren, plannen, keuze welke Skill of Tool nodig is, tekstproductie. Levert niet: bestandstoegang, geheugen tussen Sessies, afdwinging van regels. | Leverancier |
| **Sessie** | Interactie in één harness waarin de gebruiker Vragen stelt en één of meer Agents worden ingezet. Een Run kan meerdere Sessies overspannen. | Harness |
| **Vraag / Antwoord** | Opdracht van de gebruiker, bijvoorbeeld "voer gemma-update-wiki uit voor bron X" / reactie van het systeem, bijvoorbeeld een samenvatting van de run en het publicatievoorstel. | — |
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
                            | content/ en records/     |
                            | in Git; na de gate:      |
                            | pagina's of export       |
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
| Records | Blijvende verantwoording: welke bron, welke kandidaat-begrippen, welke besluiten | Werk-in-uitvoering | `wikis/<key>/records/`, in Git |
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
│       ├── cli.py                          llmwiki pull|run|validate|publish|export|harness|workspace-check
│       ├── sync.py                         pywikibot pull/push
│       ├── titles.py                       paginatitel <-> bestandsnaam
│       ├── runs.py                         run-State, opruimen kladblok
│       ├── records.py                      records afleiden uit artefacten
│       ├── gate.py                         publicatievoorstel, akkoordcontrole, publish/export
│       ├── workspace_check.py               werkplekcontrole en herstel
│       ├── harness.py                      bindingen genereren/controleren
│       └── schemas/                        generieke schemas (S)
│           ├── source.schema.json
│           ├── assessment.schema.json
│           ├── changeset.schema.json
│           ├── validation-report.schema.json
│           ├── publish-plan.schema.json
│           ├── approval.schema.json
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
│       ├── bronnen/<onderwerp>/            domein-lens op centrale bronnen (5.19)
│       ├── records/                        blijvende verslagen (in Git, niet op MediaWiki)
│       │   ├── kandidaten/<run-id>.md
│       │   └── logboek/<run-id>.md
│       ├── voorstellen/                    publicatievoorstellen, gitignored
│       ├── schemas/                        wiki-specifieke schemas, alleen indien nodig
│       │   └── bedrijfsobject.schema.json
│       ├── scripts/                        wiki-specifieke deterministische logica
│       │   ├── check_archimate.py
│       │   └── export_archimate.py         exporteur voor architectuurmodel
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
- Het Python-pakket staat in `tools/llmwiki/`: installeerbaar met `uv sync`, CLI `llmwiki` werkt vanuit elke map. De map heet `tools/` omdat de inhoud Tools zijn in de zin van de terminologie; de gebruikelijke Python-naam `src/` zegt een niet-programmeur niets. Het pakket zelf blijft `llmwiki` en staat in een eigen submap: [Inferred] een pakket met de naam `tools` botst met andere pakketten die zo heten en maakt de latere extractie als zelfstandig pakket lastiger. [Inferred] `pyproject.toml` kan de pakketmap expliciet aanwijzen (bij hatchling `[tool.hatch.build.targets.wheel] packages = ["tools/llmwiki"]`); de bescherming van de src-layout (tests draaien tegen het geïnstalleerde pakket, niet tegen losse bestanden in de werkmap) blijft daarmee behouden. [Inferred] `uv run` vindt vanuit `wikis/gemma` de `pyproject.toml` in de root door omhoog te zoeken.
- Schemas zitten in het pakket: Skills verwijzen naar `llmwiki schema show <naam>` of `llmwiki validate`, niet naar een relatief pad buiten de skill-directory. [Verified] De specificatie beveelt verwijzingen relatief aan de skill-root aan; een pad naar `../../tools/...` zou de skill aan deze repository binden.
- Er is geen aparte map voor "knowledge". Kennis die het product is, staat in `content/`. Kennis die een Skill nodig heeft om zijn taak te doen (bijvoorbeeld het GEMMA-metamodel), staat in `references/` van die Skill en wordt progressief geladen.
- Er is geen map `agents/` met Agentprofielen. Zie 5.9.
- `records/` en `voorstellen/` staan buiten `.work/` en zijn geen verborgen mappen. [Inferred] Editors zoals Obsidian tonen mappen die met een punt beginnen standaard niet; een publicatievoorstel in `.work/` zou voor de redacteur onvindbaar zijn.

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
Gebruik skill `gemma-update-wiki` voor het bijwerken van pagina's.
```

Waarom deze vorm:

- [Verified] Alle vijf harnesses lezen AGENTS.md; het is de enige instructielocatie die overal werkt.
- [Verified] Claude Code en Codex voegen root- en wiki-AGENTS.md samen bij starten in de wiki-map; Cursor combineert geneste bestanden; VS Code doet dat met `chat.useCustomizationsInParentRepositories`. [Speculative] OpenCode laadt mogelijk alleen de dichtstbijzijnde. De expliciete verwijzing in de eerste regel maakt het resultaat onafhankelijk van die verschillen: in het slechtste geval leest het Model de root-Rules via een Tool-aanroep. Voor OpenCode wordt de verwijzing daarnaast deterministisch gemaakt via `instructions` in de gegenereerde `wikis/<key>/opencode.json` (5.16).
- Aparte wiki-rulebestanden (zoals `.claude/rules/` of `.cursor/rules/*.mdc`) worden niet gebruikt: [Verified] ze zijn harness-specifiek, en de extra functie (padgebonden activering) wordt al gedekt door wiki-Skills met progressieve disclosure.
- Er komt geen `CLAUDE.md`. [Verified] Zodra een CLAUDE.md of CLAUDE.local.md in de werkmap of daarboven staat, leest Claude Code AGENTS.md standaard niet meer. Een lokale CLAUDE.local.md van één gebruiker zou dus de wiki-Rules uitschakelen. `llmwiki harness check` meldt het bestaan van zulke bestanden. Terugval voor Claude Code-versies ouder dan v2.1.277: een CLAUDE.md naast elke AGENTS.md met alleen `@AGENTS.md`; [Verified] Claude Code leest het geïmporteerde bestand dan niet dubbel.
- Omvang: Rules blijven klein. [Verified] Codex kapt samengevoegde AGENTS.md-inhoud standaard af bij 32 KiB; Claude Code adviseert minder dan 200 regels per bestand.

Rangorde bij tegenstrijdigheid, vastgelegd in de root-AGENTS.md: repository-veiligheidsregels > wiki-Rules > Skill-instructies > Vraag van de gebruiker voor zover die de gate raakt. [Inferred] Geen harness dwingt deze rangorde technisch af; daarom wordt de regel die er echt toe doet (niet publiceren zonder mens) ook buiten het Model afgedwongen: controles in de CLI en een goedkeuringsklik in het harness (5.13).

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
Na VALIDATE: draai `llmwiki run status`; die noemt de laatste fase voor deze wiki (publish, promote of promote + export, zie 5.18) en het bijbehorende plan-commando. Hieronder staat publish; promote en export werken hetzelfde. De CLI meldt welke smaak deze wiki gebruikt.
- Smaak A (document): meld het pad van het publicatievoorstel en stop. Ga pas verder als de gebruiker vraagt de publicatie uit te voeren; `llmwiki publish apply` controleert zelf het akkoord.
- Smaak B (chat): toon de samenvatting uit het voorstel en vraag de gebruiker letterlijk AKKOORD te typen. Instemming in andere woorden ("prima", "ziet er goed uit") is geen akkoord: vraag opnieuw om het woord.
Wijzig nooit zelf de akkoordvelden in een publicatievoorstel. Het harness vraagt de gebruiker bij `publish apply` altijd nog om goedkeuring; omzeil dat niet.
`publish apply` legt na publicatie zelf kandidaten en logboek vast in `records/` (type A); `promote apply` schrijft `log.md` (type B/C).
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
| Na PUBLISH | Als de wijziging ArchiMate-elementen raakt: stel voor een architectuurmodel-export te maken met `llmwiki export plan --target archimate`. Dezelfde gate geldt. |
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

1. **MCP per wiki, niet repository-breed.** Een wiki van type A, of van type C met MediaWiki als doel, heeft precies één doel-site; wiki's van type B hebben geen MediaWiki-server (5.18). Een per-wiki serverinstantie met die site als vaste standaard voorkomt dat een Agent in de GEMMA-sessie per ongeluk een andere wiki raadpleegt of wijzigt. De serverconfiguratie staat daarom in de wiki-map. Repository-brede MCP-servers (bijvoorbeeld documentatie) mogen in de root-configuratie.
2. **Vaste servernaam `mediawiki` in elke wiki en elk harness.** Skills verwijzen naar "MCP-server `mediawiki`, tool `<naam zoals de server die publiceert>`". [Verified] Claude Code maakt daar `mcp__mediawiki__<tool>` van; [Inferred] andere harnesses gebruiken een eigen prefix. De door de server gepubliceerde naam is gelijk in elk harness; alleen het prefix verschilt. Een Skill noemt daarom nooit de geprefixte naam.
3. **Rolverdeling MCP versus scripts.** MCP voor interactief lezen, zoeken en verkennen tijdens ASSESS en WRITE. Pywikibot via `llmwiki pull/push` voor bulk-synchronisatie en voor publiceren. MCP-schrijfoperaties worden niet gebruikt: publiceren loopt uitsluitend via de gate. Waar de MCP-server dat toestaat, draait hij alleen-lezen; anders blokkeren harness-permissies de schrijf-Tools.
4. **Terugval zonder MCP.** Elke Skill die MCP gebruikt, noemt een terugval via `llmwiki page get <titel>` (leest via pywikibot of lokale content). [Inferred] Daarmee blijft de Workflow uitvoerbaar in een harness of omgeving waar de MCP-server ontbreekt of niet is goedgekeurd.
5. **Meerdere MCP-servers.** Toegestaan per wiki (bijvoorbeeld een ArchiMate-repository voor GEMMA). Elke server staat in `wiki.yaml` en krijgt een vaste naam; `metadata.requires-tools` noemt `mcp:<naam>`.

**`wiki.yaml` (voorbeeld: MCP, gate, export en kladblok).**

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
  approval: document            # document (smaak A) | chat (smaak B)
  edit_summary_prefix: "[llm-wiki]"
exports:
  archimate:
    script: scripts/export_archimate.py
    target: "env:GEMMA_ARCHIMATE_TARGET"
    approval: document          # exports volgen dezelfde gate, met eigen smaak
work:
  retention_days: 30            # afgeronde runs in het kladblok
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
├── publish-plan.diff           technische diff
└── log.jsonl                   gebeurtenissen per fase (welk harness, welk Model, tijd)
```

`state.json` bevat: workflow-naam, huidige fase, status per fase (`pending|done|failed`), paden en hashes van artefacten, basis-revisies van de betrokken pagina's. `llmwiki run complete <fase>` is de enige manier om een fase af te ronden en valideert het artefact eerst.

**Kladblok versus archief.** Twee soorten opslag met een verschillend doel:

| | Kladblok | Archief (records) |
|---|---|---|
| Doel | Hervatten na onderbreking zonder stappen opnieuw te doen | Verantwoording: welke bron, welke voorstellen, welke besluiten |
| Plaats | `wikis/<key>/.work/runs/<run-id>/` | `wikis/<key>/records/` |
| Git | Nee | Ja |
| MediaWiki | Nee | Nee |
| Inhoud | Alle artefacten, ruwe tussenresultaten | Twee leesbare Markdown-verslagen per afgeronde run; de bron staat in de centrale bronindex (5.19) |
| Wie schrijft | Model (artefacten) en CLI (State) | Alleen de CLI, afgeleid uit gevalideerde artefacten |
| Levensduur | Onafgeronde runs blijven staan tot hervat of afgebroken; afgeronde runs worden na `work.retention_days` (standaard 30) verwijderd | Blijvend |

Records per afgeronde run:

| Bestand | Afgeleid uit | Inhoud |
|---|---|---|
| `records/kandidaten/<run-id>.md` | `assessment.json`, `changeset.json` | Voorgestelde begrippen en wijzigingen, met motivering en bronverwijzing; wat is overgenomen en wat niet |
| `records/logboek/<run-id>.md` | `state.json`, `log.jsonl`, akkoord | Wie wanneer wat besloot: fasen, akkoord (naam, smaak), publicatie of export, revisie-id's |

Wanneer records ontstaan:
- `llmwiki publish apply` en `llmwiki export apply` schrijven ze na een geslaagde publicatie of export.
- `llmwiki run close <run-id> --besluit "<tekst>"` schrijft ze voor een run die bewust zonder publicatie wordt afgesloten (bijvoorbeeld: bron beoordeeld, geen wijziging nodig).
- `llmwiki run abandon <run-id>` schrijft niets en verwijdert het kladblok van die run. Een onderbroken of geannuleerde run laat dus niets achter in de wiki.

Records hebben YAML-frontmatter (run-id, datum, bron-id's, akkoord), zodat ze in Obsidian of een andere Markdown-editor doorzoekbaar zijn. Door records af te leiden in plaats van ze door het Model te laten schrijven, is de keten bron → kandidaat → pagina herleidbaar en reproduceerbaar.

Afweging: records voegen per run twee bestanden toe aan Git; het bronverslag is vervangen door `sources/index/` en de domein-lens (5.19). Records gelden voor type A; bij type B en C zijn de pagina's zelf het archief (5.18). Dit wijzigt de eerdere interviewkeuze "alleen eindresultaat in Git" op verzoek van de gebruiker. Ruwe artefacten blijven buiten Git; alleen de verantwoording komt erin.

**Git.** `.work/` en `voorstellen/` staan in `.gitignore`. WRITE schrijft naar `content/` in de werkboom; de mens beoordeelt via het publicatievoorstel of met `git diff`. Commit gebeurt na publicatie, met content en records samen en de run-id in het commit-bericht. Na PUBLISH haalt `llmwiki pull` de nieuwe revisie-id's op en werkt de `.meta.json`-bestanden bij.

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
| `page-meta` | Sidecar per pagina: titel, pageid, revid, tijdstempel, namespace, contentmodel, categorieën, sha1 | Nodig: conflictdetectie bij push |
| `run-state` | Zie 5.11 | Nodig: hervatten |

**Wiki-specifiek (in `wikis/<key>/schemas/`).** Alleen als er een domeinobject is dat deterministisch moet worden gecontroleerd, bijvoorbeeld `bedrijfsobject.schema.json` voor GEMMA. Een wiki-schema breidt een generiek schema uit via het veld `extensions` dat elk generiek schema als vrij object toestaat, niet door het generieke schema te kopiëren.

**Wanneer geen schema.** Voor vrije tekst (paginatekst zelf), voor tussenstappen binnen één fase, en voor iets dat maar door één script wordt gelezen en geschreven zonder Model ertussen. Een schema dat niet door code wordt gevalideerd, wordt niet toegevoegd.

**Standaard.** JSON Schema draft 2020-12 (S). Validatie met de Python-bibliotheek `jsonschema` via `llmwiki validate <artefact>`.

### 5.13 Scripts en deterministische logica

**Regel.** Alles wat zonder Model kan, gebeurt zonder Model.

| Plaats | Wat | Voorbeelden |
|---|---|---|
| `tools/llmwiki/` (repository-breed) | Logica die elke wiki nodig heeft | pull, push, bestandsnaam-mapping, run-State, records, schemavalidatie, publish/export plan/apply, lint, harness sync/check, workspace-check |
| `wikis/<key>/scripts/` | Logica die meerdere Skills van één wiki gebruiken | `check_archimate.py` |
| `<skill>/scripts/` | Logica die alleen die Skill gebruikt | parser voor een bronformaat |
| Workflow-Skill | Geen scripts; alleen aanroepvolgorde | — |

**Aanroep.** Generieke logica altijd via de CLI: `uv run llmwiki <commando>`. Wiki- en Skill-scripts via `uv run python <pad>`, met paden relatief aan de wiki-map (waar de Workflow start) respectievelijk aan de skill-directory. [Verified] De specificatie beveelt paden relatief aan de skill-root aan.

**Taal en platform.** Uitsluitend Python (geen Bash of PowerShell) voor alles wat de Workflow aanroept, met `pathlib`, UTF-8 expliciet bij lezen en schrijven, en geen afhankelijkheid van een specifieke shell. [Verified] Claude Code draait op Windows zonder Git Bash commando's via PowerShell; [Inferred] een Python-CLI werkt identiek onder Bash, PowerShell en cmd.

**Publicatiegate.**

Eisen: de Agent publiceert of exporteert nooit zelfstandig; de redacteur hoeft geen terminalcodes of wachtwoorden in te voeren en blijft in de eigen editor of chat; per wiki is te kiezen tussen twee smaken; de gate geldt voor publicatie naar MediaWiki en voor architectuurmodel-export.

Probleem met de smaken op zichzelf: in smaak A heeft de Agent schrijfrechten op het voorstel en kan hij `akkoord_voor_publicatie: ja` zelf invullen; in smaak B beoordeelt het Model zelf of het woord AKKOORD is getypt. [Inferred] Beide smaken rusten daarom op Model-gedrag en zijn op zichzelf geen technische afdwinging. De afdwinging komt van een handeling die alleen de mens kan doen: de goedkeuringsklik die het harness toont voordat een commando met permissie 'ask' wordt uitgevoerd.

Werking:

1. **Plan.** `llmwiki publish plan --run <id>` controleert dat VALIDATE geslaagd is, haalt per pagina de actuele revisie op en vergelijkt die met de basis-revisie uit `.meta.json`. Bij afwijking: stop met conflictmelding. Schrijft `publish-plan.json` en het publicatievoorstel `wikis/<key>/voorstellen/<run-id>.md`, en berekent een plan-hash.
2. **Publicatievoorstel.** Leesbaar Markdown-document met bovenaan:
   ```yaml
   ---
   run: 2026-09-26T1412-a3f9
   plan_hash: 3f9a1c07
   akkoord_voor_publicatie: nee
   beoordeeld_door: ""
   ---
   ```
   daaronder een samenvatting in gewone taal (welke pagina's, wat verandert, waarom, uit welke bron) en per pagina de wijziging als leesbare diff.
3. **Akkoord (smaak volgens `publish.approval` in `wiki.yaml`).**
   - Smaak A, `document`: de redacteur zet in het voorstel `akkoord_voor_publicatie: ja` en vult een naam in, en vraagt de Agent daarna de publicatie uit te voeren.
   - Smaak B, `chat`: de Agent toont de samenvatting in de chat en vraagt om het letterlijke woord AKKOORD. Andere instemming leidt tot een herhaalde vraag, niet tot uitvoering.
4. **Uitvoeren.** De Agent roept `llmwiki publish apply --run <id>` aan. De CLI controleert:
   - smaak A: `akkoord_voor_publicatie: ja`, `beoordeeld_door` niet leeg, en `plan_hash` in het voorstel gelijk aan de actuele plan-hash (een akkoord op een verouderd voorstel geldt niet);
   - smaak B: niets aanvullends; zie laag 2;
   - beide: opnieuw de basis-revisies.
5. **Laag 2: harness-goedkeuring.** De gegenereerde harness-configuratie zet `llmwiki publish apply` en `llmwiki export apply` op 'ask' (5.15, 5.16). Het harness toont de mens het exacte commando en wacht op een klik. Dit is de enige laag die de Agent niet zelf kan vervullen.
6. **Laag 3: MCP alleen-lezen** en een deny-regel op directe pywikibot-aanroepen, zodat de Agent de CLI niet kan omzeilen.
7. **Vastlegging.** Na publicatie schrijft de CLI de records (5.11), inclusief naam en smaak van het akkoord.

Architectuurmodel-export gebruikt hetzelfde mechanisme: `llmwiki export plan --target <naam>` en `llmwiki export apply --target <naam> --run <id>`. De generieke CLI regelt voorstel, akkoord en records; de exporteur zelf is een wiki-script dat in `wiki.yaml` onder `exports` wordt genoemd (voor GEMMA `scripts/export_archimate.py`). Zo blijft de generieke laag vrij van ArchiMate-kennis.

Grenzen:
- [Inferred] Als een gebruiker in het harness automatische goedkeuring aanzet (auto-approve, "yolo", `bypassPermissions` of vergelijkbaar), vervalt laag 2 en rust de gate voor smaak B volledig op Model-gedrag. [Speculative] Per harness verschilt of een 'ask'-regel in zo'n modus nog een vraag oplevert; zie V5 in sectie 8. Het Kompas noemt daarom als spelregel: automatische goedkeuring staat uit in sessies waarin wordt gepubliceerd. `llmwiki workspace-check` controleert voor zover mogelijk of de gegenereerde permissieregels aanwezig zijn.
- [Verified] Claude Code kent daarnaast een MCP-annotatie `anthropic/requiresUserInteraction` die bij elke aanroep een goedkeuringsvraag afdwingt, ook in `acceptEdits`, `auto` en `bypassPermissions`. Als de ervaring leert dat laag 2 in Claude Code onvoldoende is, kan `publish apply` ook als Tool van een kleine lokale MCP-server worden aangeboden. Dat is Claude Code-specifiek en daarom geen onderdeel van de basisarchitectuur.
- Smaak A is sterker dan smaak B: het akkoord is gebonden aan een plan-hash, heeft een naam en staat in een document dat de redacteur zelf bewerkt. Smaak B is sneller, maar het akkoord bestaat alleen in de gespreksgeschiedenis; het logboek vermeldt daarom "akkoord via chat, goedkeuring via harness".

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

`wikis/gemma/.claude/settings.json` (en dezelfde `ask`- en `deny`-regels in de root):

```json
{
  "permissions": {
    "allow": [
      "Bash(uv run llmwiki workspace-check*)",
      "Bash(uv run llmwiki run *)",
      "Bash(uv run llmwiki validate *)",
      "Bash(uv run llmwiki publish plan *)",
      "Bash(uv run llmwiki export plan *)",
      "Bash(uv run llmwiki pull *)",
      "Bash(uv run python scripts/check_*)"
    ],
    "ask": [
      "Bash(uv run llmwiki publish apply*)",
      "Bash(uv run llmwiki export apply*)",
      "Bash(llmwiki publish apply*)",
      "Bash(llmwiki export apply*)"
    ],
    "deny": [
      "Bash(*pywikibot*)",
      "Bash(uv run python scripts/export_*)",
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
      "*llmwiki publish apply*": "ask",
      "*llmwiki export apply*": "ask",
      "*pywikibot*": "deny"
    }
  }
}
```

[Verified] `instructions` bestaat in `opencode.json`; [Verified] OpenCode kent de permissiewaarden `allow`, `deny` en `ask` met wildcards (gedocumenteerd voor `permission.skill`). [Inferred] Dezelfde vorm voor `permission.bash` en de vorm van het `mcp`-blok; verificatie in sectie 8. Gebruikersomgeving: `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` zolang de Claude Code-brug aanwezig is.

**Codex.** `wikis/gemma/.codex/config.toml` (gegenereerd):

```toml
[mcp_servers.mediawiki]
command = "npx"
args = ["-y", "<mediawiki-mcp-server-pakket>"]
env_vars = ["MW_GEMMA_USER", "MW_GEMMA_PASSWORD"]
env = { MW_API_URL = "https://www.gemmaonline.nl/w/api.php" }
```

In `wiki-publish/agents/openai.yaml`: `policy.allow_implicit_invocation: false`. [Verified] Codex leest skills uit `.agents/skills/` en AGENTS.md zonder verdere configuratie. [Inferred] Veldnamen `env_vars` en `env`; verificatie in sectie 8. Laag 2 van de gate rust in Codex op de goedkeuringsmodus: [Inferred] in een modus die commando's buiten de sandbox of met netwerktoegang laat goedkeuren, vraagt `publish apply` (dat netwerk nodig heeft) om goedkeuring. Verificatie in sectie 8.

**VS Code/Copilot.** `wikis/gemma/.vscode/settings.json`:

```json
{
  "chat.useAgentsMdFile": true,
  "chat.useCustomizationsInParentRepositories": true
}
```

en `wikis/gemma/.vscode/mcp.json` met een `servers`-blok voor `mediawiki`. [Verified] VS Code leest `.agents/skills/` en ondersteunt `disable-model-invocation`. [Inferred] Laag 2 van de gate: VS Code vraagt goedkeuring voor terminalcommando's tenzij ze op een auto-approve-lijst staan; de generator zet `publish apply` en `export apply` nooit op die lijst.

**Cursor.** `wikis/gemma/.cursor/mcp.json` met `mcpServers.mediawiki`; verder 5.14. [Verified] Cursor leest `.agents/skills/` en AGENTS.md en ondersteunt `disable-model-invocation`. [Inferred] Laag 2 van de gate: Cursor vraagt goedkeuring voor terminalcommando's buiten de toegestane lijst; dezelfde regel als bij VS Code.

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
1. Draai `uv run llmwiki workspace-check`.
   Werkt `uv` niet: leg de gebruiker in gewone taal uit hoe `uv` wordt geïnstalleerd
   (zie README, sectie Installatie) en stop.
2. Meldt workspace-check `herstelbaar`: vraag de gebruiker of je de werkplek mag inrichten,
   draai dan `uv run llmwiki workspace-check --fix` en geef de meldingen in gewone taal door.
3. Meldt workspace-check `actie gebruiker`: leg per punt uit wat de gebruiker moet doen
   en begin niet aan inhoudelijk werk tot workspace-check `ok` meldt.
4. Meldt workspace-check dat Skills pas na herladen beschikbaar zijn: zeg dat tegen de gebruiker.
```

**`llmwiki workspace-check`.**

| Controle | `--fix` doet | Anders: melding aan gebruiker |
|---|---|---|
| Python-omgeving aanwezig en actueel | `uv sync` | — |
| Brug aanwezig en actueel | `harness sync` (symlink, junction of kopie) | — |
| Geen CLAUDE.md of CLAUDE.local.md op een wiki-pad | — | Uitleg dat dit bestand de wiki-Rules uitschakelt, met voorstel het te hernoemen |
| Credentials voor deze wiki (alleen namen, nooit waarden) | — | Welke variabele ontbreekt en hoe je die instelt op dit besturingssysteem |
| Commando voor de MCP-server beschikbaar (bijv. `npx`) | — | Welk programma ontbreekt |
| Gegenereerde permissieregels voor de gate aanwezig | `harness sync` | — |
| Onafgeronde runs | — | Lijst, zodat de Agent kan voorstellen te hervatten |
| Afgeronde runs ouder dan bewaartermijn | `run prune` | — |

Uitvoer: een korte tekst in gewone taal en, met `--json`, een machineleesbare status (`ok`, `herstelbaar`, `actie gebruiker`) voor de Agent. `workspace-check` zonder `--fix` wijzigt niets en is in de permissies vooraf toegestaan, zodat de eerste controle geen goedkeuringsvraag oplevert.

**Windows zonder rechten.** De brug valt terug op een junction of kopie (5.7), dus ontbrekende symlink-rechten blokkeren nooit. `workspace-check` meldt Developer Mode alleen als optionele verbetering (kopieën moeten na wijziging van Skills opnieuw worden bijgewerkt), met één link die de juiste instellingenpagina opent: `ms-settings:developers`. [Inferred] Deze URI opent op Windows 10 en 11 de pagina met ontwikkelaarsinstellingen.

**Herladen na eerste inrichting.** [Verified] Claude Code ziet een skills-map die bij de start van de Sessie nog niet bestond pas na `/reload-skills`; [Verified] Codex adviseert een herstart als een nieuwe Skill niet verschijnt. `workspace-check` meldt daarom na het aanmaken van de brug per harness wat de gebruiker moet doen. De Agent zegt dat de Skills beschikbaar zijn, niet dat ze geladen zijn: of een Skill in de Context wordt geladen, beslist het harness.

**Wat niet te automatiseren is.** Goedkeuren van projectservers, vertrouwen van de map en invullen van credentials blijven menselijke handelingen. Dat is bedoeld: een gekloonde repository hoort zichzelf geen toegang te geven. `workspace-check` zorgt dat de gebruiker precies weet welke handeling nodig is.

**Tijdsduur.** [Speculative] "Binnen enkele minuten" hangt af van de downloadtijd bij de eerste `uv sync` en van de start van de MCP-server; dit wordt gemeten in de pariteitstest (sectie 8).

### 5.18 Soorten wiki's: sync, curatie en hybride

Een LLM-wiki heeft niet altijd een MediaWiki-site als bron van waarheid. De architectuur kent drie typen. Ze delen Rules, Skills, de generieke Workflow, run-State, gate en de centrale bronnen (5.19); ze verschillen in contentformaat, bron van waarheid en de laatste fase.

| | Type A: sync | Type B: curatie | Type C: hybride |
|---|---|---|---|
| Voorbeeld | GEMMA Online (MediaWiki) | Beleidskader-analyse, curatieomgeving zoals OpzetII | Begrippen en ArchiMate; informatiemodellen (RSGB, MIM) |
| Bron van waarheid | Externe site | Repository (Markdown in Git) | Repository; doelen krijgen afgeleide kopieën |
| Pagina's | `content/` in wikitext | `onderwerpen/`, `bronnen/`, `kandidaten/` in Markdown | Als B, plus `export/` |
| Curatiestatus | Nee | `kandidaat` → `review` → `goedgekeurd` | Als B |
| Laatste fase | PUBLISH na akkoord | PROMOTE: status naar `goedgekeurd` | PROMOTE, daarna EXPORT per doel |
| Exportdoelen | — | — | ArchiMate Open Exchange, UML/XMI, MediaWiki, CSV |
| MediaWiki/MCP nodig | Ja | Nee | Alleen als MediaWiki een doel is |
| Archief | `records/kandidaten/`, `records/logboek/` (5.11) | De pagina's zelf plus `log.md` | Als B |

**Keten in het gemeentelijke landschap.** De typen volgen elkaar op; de uitkomst van de ene wiki is bron voor de volgende:

```text
Beleidskader (B) → Begrippen & ArchiMate (C) → Informatiemodellen (C) → GEMMA Online (A)
```

Overdracht loopt via de centrale bronnen, niet via verwijzingen tussen wiki's: een goedgekeurde export wordt met `llmwiki source add --from-export <wiki>/<doel>` een nieuwe bron in `sources/` met eigen tags, en de volgende wiki neemt die op via zijn bronfilter (5.19). Regel 3 uit 5.4 blijft zo gelden: wiki's verwijzen niet naar elkaars interne pagina's.

Keuzes:
- **Eén contentformaat per wiki.** Wikitext alleen in `content/` van type A. Markdown in de curatiemappen van B en C. Omzetting naar wikitext of XMI gebeurt alleen bij export.
- **Bij type B en C zijn de pagina's het archief.** Aparte records voor bronnen en kandidaten zouden dubbele vastlegging zijn; het logboek is `log.md`. Type A houdt `records/kandidaten/` en `records/logboek/`; het bronverslag vervalt daar ook, omdat de centrale bronindex (5.19) die rol overneemt.
- **De Obsidian-vault is de repository-root.** Alleen dan werken relatieve links van een wiki naar `sources/` in Obsidian; [Inferred] Obsidian opent geen links naar bestanden buiten de vault. `.obsidian/app.json` in de root zet Markdown-links op relatief pad en sluit `tools/` en `tests/` uit via de uitsluitfilters. [Inferred] Mappen die met een punt beginnen (`.work`, `.agents`, `.claude`) toont Obsidian standaard niet.
- **Bronnen per onderwerp.** Een wiki deelt zijn bronanalyses in naar onderwerp: `bronnen/<onderwerp>/<bron-id>.md`, waarbij `<onderwerp>` gelijk is aan de id van `onderwerpen/<onderwerp>.md`. Een bron die bij meer onderwerpen hoort, staat bij het hoofdonderwerp; andere onderwerppagina's linken ernaar.

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
    ├── gemma/                      type A
    │   ├── AGENTS.md · wiki.yaml
    │   ├── content/                MediaWiki-pagina's (.wiki + .meta.json)
    │   ├── onderwerpen/            optioneel: werkpagina's per thema, niet gepubliceerd
    │   ├── bronnen/<onderwerp>/    laag 3: domein-lens
    │   ├── records/                kandidaten en logboek per run
    │   └── voorstellen/ · .agents/skills/ · .work/
    └── opzet2/                     type B of C
        ├── AGENTS.md · wiki.yaml
        ├── log.md                  logboek, alleen aanvullen, door de CLI
        ├── voortgang.md            gegenereerd overzicht
        ├── onderwerpen/            ingang voor elke taak: <thema>.md
        ├── bronnen/<onderwerp>/    laag 3: domein-lens per bron
        ├── kandidaten/             met curatiestatus
        ├── export/                 alleen type C, alleen via de gate
        ├── schemas/ · mappings/    paginamodellen; vertaling naar exportdoelen
        └── voorstellen/ · .agents/skills/ · .work/
```

`wiki.yaml` voor type B/C (kern):

```yaml
key: opzet2
type: curation                       # sync | curation | hybrid
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
targets:                             # leeg bij type B
  archimate: { format: archimate-oef, mapping: mappings/archimate.yaml, out: export/model.xml }
  xmi:       { format: xmi, script: scripts/export_xmi.py, out: export/informatiemodel.xmi }
  csv:       { format: csv, page_type: kandidaat, out: export/kandidaten.csv }
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

De generieke Workflow `wiki-update` blijft één Skill. De Vraag noemt een onderwerppagina (5.19); de laatste fase volgt uit `wiki.yaml` via `llmwiki run status`.

```text
INGEST → ASSESS → WRITE → VALIDATE → GATE → PUBLISH            (type A)
                                           → PROMOTE            (type B)
                                           → PROMOTE → EXPORT   (type C)
```

| Fase | Type A | Type B/C |
|---|---|---|
| INGEST | Laag 1 en 2 als de bron nieuw is (5.19); laag 3 in `bronnen/<onderwerp>/` | Idem |
| ASSESS | Welke pagina's veranderen | Welke onderwerpen en kandidaten worden geraakt |
| WRITE | Wikitext in `changeset/` | Markdown-pagina's; nieuwe kandidaten met `status: kandidaat`. De Agent mag `kandidaat` → `review` zetten |
| VALIDATE | Wikitext-controles, wiki-scripts | Frontmatter tegen schema, links, curatieregels, wiki-scripts |
| GATE | Publicatievoorstel (5.13) | Promotievoorstel; bij C ook het exportvoorstel |
| Laatste fase | `publish apply` | `promote apply`, bij C daarna `export apply` per doel |

De gate is dezelfde als in 5.13. Wat anders is bij B en C:
- [Inferred] De Agent kan `status: goedgekeurd` zelf in een lokaal bestand schrijven. Daarom weigeren `llmwiki validate` en de pre-commit-hook elke pagina met een gated status zonder promotieregel in `log.md` met overeenkomende inhoudshash.
- Bij `min_reviewers` > 1 bevat `beoordeeld_door` een lijst; `promote apply` controleert het aantal.
- Wijzigt een goedgekeurde pagina inhoudelijk, dan zet VALIDATE hem terug naar `review`.

Een wiki-Workflow (bijv. `opzet2-update`) blijft dun, zoals in 5.8.

#### Tooling

MediaWiki is één van de doelen, geen vaste afhankelijkheid.

| Onderdeel | Plaats | Afhankelijkheden |
|---|---|---|
| Kern: run-State, gate, voorstellen, `log.md`, `voortgang.md`, workspace-check, harness sync, lint | `llmwiki` | Geen MediaWiki |
| Bronbeheer: `source add|list|show`, conversie naar Markdown, onveranderlijkheid van `raw/` | `llmwiki` (5.19) | Converter, keuze in Klus 3 |
| Markdown-validatie: frontmatter per paginatype, relatieve links, geen `[[wikilinks]]`, `id` = bestandsnaam, bron-id's bestaan in `sources/index/` en vallen binnen de scope, statusovergangen | `llmwiki validate` | Geen MediaWiki |
| MediaWiki: pull, publish, conflictcontrole, Markdown→wikitext | extra `mediawiki` (`uv sync --extra mediawiki`) | pywikibot; [Inferred] pandoc of Python-converter |
| ArchiMate Open Exchange-writer | `llmwiki` (generiek) | [Verified] Open standaard van The Open Group |
| UML/XMI-export (RSGB, MIM) | Wiki-script via `targets.xmi` | [Inferred] XMI-varianten verschillen per modelleertool; daarom eerst per wiki, generiek pas bij een tweede gebruiker |
| CSV-writer | `llmwiki` (generiek) | Geen |
| Vertaling paginatype → ArchiMate-element of UML-klasse | Wiki: `mappings/`, eventueel wiki-script | Domeinkennis blijft in de wiki |

Logboekdiscipline:
- `log.md` wordt alleen aangevuld, altijd door de CLI, één kop per gebeurtenis, bijvoorbeeld `## [2026-09-27] promote | kandidaat-zaakdossier | M. Jansen | a3f9`. Lint en pre-commit weigeren wijzigen of verwijderen van bestaande regels.
- `voortgang.md` wordt bij `run complete`, `promote apply` en `workspace-check` opnieuw gegenereerd: open runs, aantallen per status, wat wacht op review, laatste export per doel.

Gevolgen:
- `llmwiki workspace-check` controleert bij type B geen MediaWiki-credentials, wel de Obsidian-instellingen in de root.
- `llmwiki harness sync` genereert MCP-configuratie alleen voor wiki's met een MediaWiki-doel.
- Generieke Skills `wiki-write` en `wiki-validate` hebben per contentformaat een reference (`references/markdown.md`, `references/wikitext.md`).

### 5.19 Gedeelde bronnen en contextbescherming

**Drie lagen.**

| Laag | Plaats | Inhoud | Wie schrijft | Gedeeld |
|---|---|---|---|---|
| 1. Ruwe originelen | `sources/raw/<bron-id>.<ext>` en `sources/raw/<bron-id>.md` | Origineel (pdf, docx) en de Markdown-conversie met dezelfde naam | `llmwiki source add` (script) | Ja |
| 2. Gedeelde intake | `sources/index/<bron-id>.md` | Metadata, managementsamenvatting, inhoudsopgave, thematags | Generieke Skill `wiki-intake`, één keer per bron | Ja |
| 3. Domein-lens | `wikis/<key>/bronnen/<onderwerp>/<bron-id>.md` | Wiki-specifieke analyse en uittreksels met paragraafverwijzing naar laag 1 | Wiki-Skill tijdens INGEST | Nee |

Regels:
- **Bron-id** `<jaar>-<uitgever>-<korte-titel>`, kleine letters en koppeltekens; gelijk in alle drie lagen. Dat maakt de keten bron → lens → kandidaat herleidbaar via bestandsnaam en frontmatter.
- **Laag 1 is onveranderlijk.** Alles staat gewoon in Git, dus ook de pdf's. De pre-commit-hook staat in `sources/raw/` alleen toevoegen toe. Een nieuwe versie van een document krijgt een nieuw bron-id. [Inferred] De repository groeit met elke pdf; bij grote aantallen is Git LFS later zonder structuurwijziging in te voeren.
- **Conversie is deterministisch.** `llmwiki source add <bestand>` kopieert het origineel, zet het om naar Markdown, berekent een hash en weigert als het bron-id al bestaat. `wiki-intake` controleert daarna de conversie steekproefsgewijs (koppen, tabellen) en meldt problemen in plaats van de conversie te herschrijven.
- **Laag 2 is generiek.** `wiki-intake` bevat geen wiki-kennis (regel 1 uit 5.4). Het schema `source-index.schema.json` in de core legt de frontmatter vast: id, titel, uitgever, datum, versie, pad en hash van laag 1, tags, samenvatting.
- **Hergebruik.** Bestaat `sources/index/<bron-id>.md` al, dan slaat INGEST laag 1 en 2 over en maakt alleen de domein-lens.

**Contextbescherming.** Doel: een wiki verzuipt niet in alle bronnen van de repository, en een Sessie laadt alleen wat de taak nodig heeft.

| Maatregel | Werking | Afdwinging |
|---|---|---|
| Scoping via tags | `sources.tags` en `sources.exclude_tags` in `wiki.yaml` bepalen welke bronnen een wiki ziet | `llmwiki source list` toont alleen bronnen in scope; `validate` meldt verwijzingen naar bronnen buiten scope |
| Taakgericht werken | Elke run start vanuit een onderwerppagina: `/opzet2-update onderwerpen/zaakgericht-werken.md`. De `bronnen:`-lijst in die pagina bepaalt welke bronnen worden gelezen | `llmwiki run start --onderwerp` legt de bronlijst vast in de State; INGEST en ASSESS krijgen alleen die bron-id's |
| Leesvolgorde | Eerst laag 2 (kort), dan laag 3; laag 1 alleen voor specifieke passages | Instructie in `wiki-update` en de wiki-Rules |
| Kleine intake | Managementsamenvatting in laag 2 met een vaste maximale omvang | Schema en lint |

[Inferred] De Obsidian-vault op root-niveau toont alle bronnen aan de mens; de scoping geldt voor de Agent en de CLI, niet voor wat een redacteur kan openen.

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
| K15 | Kladblok (gitignored, met bewaartermijn) gescheiden van records (kandidaten, logboek) in Git; records door de CLI afgeleid, niet door het Model geschreven | K |
| K16 | Werkplekcontrole via `llmwiki workspace-check`, aangestuurd vanuit de root-AGENTS.md; Windows-rechten nooit blokkerend | K |
| K17 | Architectuurmodel-export valt onder dezelfde gate; exporteur is een wiki-script, gate en records zijn generiek | K |
| K18 | Documentatie in drie lagen: Kompas, Kluswijzer, onderbouwing | K |
| K19 | Drie wiki-typen (sync, curatie, hybride) met één contentformaat per wiki; laatste fase PUBLISH, PROMOTE of PROMOTE + EXPORT, bepaald door `wiki.yaml` | K |
| K20 | Curatiestatus in frontmatter; gated statussen alleen geldig met promotieregel in `log.md`, gecontroleerd door validate en pre-commit | K |
| K21 | MediaWiki als optionele extra van `llmwiki`; ArchiMate Open Exchange en CSV als generieke writers, vertaling van paginatypen per wiki | S + K |
| K22 | Centrale bronnen in drie lagen (raw, index, domein-lens) met één bron-id; raw onveranderlijk, alles in Git | K |
| K23 | Contextbescherming: scoping via tags in `wiki.yaml`, runs starten vanuit een onderwerppagina | K |
| K24 | Obsidian-vault is de repository-root; overdracht tussen wiki's in de keten via `sources/` | K |

---

## 8. Open punten en verificatieprocedure

Punten gemarkeerd als [Speculative] die de architectuur raken:

| Nr | Vraag | Test | Gevolg bij negatief resultaat |
|---|---|---|---|
| V1 | Laadt OpenCode bij starten in `wikis/gemma` ook de root-AGENTS.md? | Vraag in een nieuwe Sessie: "welke instructiebestanden zijn geladen?" | Geen: `instructions` in `opencode.json` dekt dit al |
| V2 | Vindt Cursor bij openen van alleen `wikis/gemma` root-skills en root-AGENTS.md? | Open map, controleer Customize > Skills | Activeer `--cursor-wiki-root`-brug |
| V3 | Behandelt Claude Code een Windows-junction als symlinked skill-map? | `llmwiki harness sync` op Windows zonder Developer Mode, daarna `/skills` | Val terug op kopie |
| V4 | Hoe gaan VS Code en Cursor om met identieke skills in `.agents/skills/` en `.claude/skills/`? | Beide aanwezig, controleer skill-lijst | Brug alleen op Claude Code-machines of VS Code `chat.agentSkillsLocations` beperken |
| V5 | Vraagt elk harness bij een 'ask'-regel op `publish apply` altijd om goedkeuring, ook in modi met automatische goedkeuring? | Laat de Agent `publish apply` aanroepen in een testwiki, eerst in de standaardmodus, daarna in de auto-approve-modus van dat harness | Spelregel "automatische goedkeuring uit bij publiceren" is dan de enige bescherming voor smaak B; overweeg voor dat harness alleen smaak A, en voor Claude Code de MCP-variant met `anthropic/requiresUserInteraction` |
| V6 | Exacte veldnamen MCP-config OpenCode, Codex, VS Code, Cursor | Generator-uitvoer laden, server moet verbinden | Generator aanpassen |
| V7 | Leest Codex `.codex/config.toml` in de werkmap als die onder de Git-root ligt? | Start Codex in `wikis/gemma`, vraag MCP-status | Config in root plaatsen met server per wiki onder eigen naam |
| V8 | Volgt elk harness de instructie "Werkplek eerst" uit de root-AGENTS.md bij de eerste Vraag? | Nieuwe kloon, eerste Vraag is inhoudelijk | Instructie scherper en hoger in AGENTS.md; in Claude Code eventueel een SessionStart-hook die `workspace-check` draait (H) |
| V9 | Duur van de eerste inrichting op een schone machine | Tijd meten van klonen tot eerste `workspace-check ok`, per besturingssysteem | Afhankelijkheden beperken of vooraf te installeren programma's in README noemen |

Pariteitstest per harness (handmatig, per release van een harness of van de core):

1. `llmwiki harness check` slaagt.
2. Start in `wikis/_template` (testwiki tegen een test-MediaWiki). Vraag: "Welke Rules en Skills heb je geladen?" Controleer: root- en wiki-Rules, generieke en wiki-Skills, elke naam één keer.
3. Voer `/<key>-update-wiki` (of `$...`) uit met een vaste testbron.
4. Controleer dat alle artefacten tegen hun schema valideren en dat de Agent stopt bij de gate.
5. Smaak A: controleer dat `publish apply` weigert zolang het voorstel op `nee` staat of een verouderde plan-hash heeft. Smaak B: controleer dat "prima" geen publicatie start. Beide: controleer dat het harness om goedkeuring vraagt.
6. Controleer dat na publicatie twee records (type A) of een regel in `log.md` (type B/C) bestaan en dat een afgebroken run niets achterlaat buiten `.work/`.

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
