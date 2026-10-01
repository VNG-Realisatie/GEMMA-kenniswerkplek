# Kluswijzer: de repository inrichten

Vier klussen, in deze volgorde. Elke klus heeft een beginsituatie, een taak en een eindresultaat dat je kunt controleren. Een klus is af als alle punten onder "Eindresultaat" kloppen.

Achtergrond per onderdeel: `docs/onderbouwing.md` (sectienummers tussen haakjes). Overzicht voor het team: `ARCHITECTURE.md`.

| Klus | Naam | Levert op |
|---|---|---|
| 1 | Fundament | Mappen, huisregels, leeg gereedschapspakket |
| 2 | Werkplek | Startcontrole en koppelingen met de vijf AI-omgevingen |
| 3 | Gereedschapskist | Gedeelde vaardigheden, gedeelde werkstroom en het gereedschap dat ze gebruiken, inclusief de publicatiegate |
| 4 | Eerste bewoner | De GEMMA-wiki, getest in alle vijf AI-omgevingen |

---

## Klus 1: Fundament

**Begin.** Een lege Git-repository. Op de machine van de inrichter staan Git en `uv`.

**Taak.**

1. Maak de basismappen: `.agents/skills/`, `tools/llmwiki/`, `tests/`, `docs/`, `sources/raw/`, `sources/index/`, `wikis/_template/`. Zet `.obsidian/app.json` in de root: relatieve Markdown-links, geen `[[wikilinks]]`, `tools/` en `tests/` uitgesloten (5.18). De rest van `.obsidian/` in `.gitignore`.
2. Leg vast hoe bestanden zich op elk besturingssysteem gedragen (6.1):
   - `.gitattributes` met `* text=auto eol=lf` en binaire bestandstypen als `binary`;
   - `.editorconfig` met UTF-8 en LF;
   - `.gitignore` met `.work/`, `voorstellen/`, `.claude/skills/`, `wikis/*/.claude/skills/`, `.env`.
3. Maak `pyproject.toml` met pakket `llmwiki`, commando `llmwiki` en `uv.lock`. De eerste versie kent alleen `llmwiki --version`.
4. Schrijf de root-`AGENTS.md` (maximaal circa 100 regels) met deze onderdelen, in deze volgorde (5.6, 5.17):
   - **Werkplek eerst**: bij de eerste Vraag `uv run python -m llmwiki workspace-check`, en wat te doen bij elke status;
   - **Veiligheid**: nooit publiceren of exporteren zonder akkoord; akkoordvelden nooit zelf invullen; nooit credentials in bestanden;
   - **Rangorde**: repository-veiligheidsregels > wiki-Rules > Skill-instructies;
   - **Werkwijze**: werkstromen via Skills, tussenresultaten via `llmwiki run`, geen State alleen in het gesprek;
   - **Grenzen**: gedeelde Skills bevatten geen kennis van één wiki;
   - verwijzing naar `ARCHITECTURE.md`.
5. Zet `ARCHITECTURE.md`, `docs/kluswijzer.md` en `docs/onderbouwing.md` in de repository.
6. Schrijf `README.md` met installatie per besturingssysteem: Git, `uv`, Node (voor de MCP-server), `git config core.longpaths true` op Windows.

**Eindresultaat.**

- [ ] Een verse kloon op Windows en op Linux of macOS geeft dezelfde bestanden, zonder gewijzigde regeleinden (`git status` is schoon).
- [ ] `uv run python -m llmwiki --version` werkt vanuit de hoofdmap en vanuit `wikis/_template`.
- [ ] De repository bevat geen `CLAUDE.md` en geen symlinks.
- [ ] Een collega zonder programmeerkennis kan na het lezen van `ARCHITECTURE.md` uitleggen waar content, bronnen en verslagen staan.

---

## Klus 2: Werkplek

**Begin.** Klus 1 is af. Er is een test-MediaWiki (of een testnamespace) met een testaccount.

**Taak.**

1. Maak het sjabloon `wikis/_template/` (type `sync`, een kale werkkopie — zie 5.18) met `AGENTS.md` (eerste regel verwijst naar `../../AGENTS.md`), `wiki.yaml` naar de test-MediaWiki met `publish.approval: document`, `site.family`/`site.code` (een geregistreerde pywikibot-family), en lege mappen `content/`, `voorstellen/`, `.agents/skills/`, plus een leeg `revisies.json` (`{}`) en `log.md`. Geen `onderwerpen/`/`bronnen/`/`records/` — dat hoort bij een curatie-wiki (Klus 3), niet bij een sync-wiki.
2. Bouw `llmwiki harness sync` en `llmwiki harness check` (5.7, 5.16):
   - brug `.claude/skills/` voor elke `.agents/skills/`: eerst symlink, dan junction op Windows, dan kopie met bronvermelding;
   - MCP-configuratie per wiki uit `wiki.yaml`: `.mcp.json`, `opencode.json`, `.codex/config.toml`, `.vscode/mcp.json`, `.cursor/mcp.json`;
   - `.vscode/settings.json` met `chat.useAgentsMdFile` en `chat.useCustomizationsInParentRepositories`;
   - `instructions: ["../../AGENTS.md"]` in de OpenCode-configuratie van elke wiki;
   - permissies (5.15, 5.16): `workspace-check`, `run`, `validate`, `plan` vooraf toegestaan; `publish apply` en `export apply` op 'ask'; directe pywikibot-aanroepen en exportscripts geweigerd;
   - `check` faalt bij afwijkende gegenereerde bestanden, verouderde kopieën of een `CLAUDE.md`/`CLAUDE.local.md` op een wiki-pad.
3. Bouw `llmwiki workspace-check` met en zonder `--fix` (5.17): Python-omgeving, brug, CLAUDE.md-controle, credentials (alleen namen), MCP-servercommando, permissieregels, onafgeronde runs, opruimen. Uitvoer in gewone taal plus `--json` met status `ok`, `herstelbaar` of `actie gebruiker`. Meldingen voor Windows noemen Developer Mode alleen als optie, met de link `ms-settings:developers`.
4. Zet `llmwiki harness check` in een pre-commit-hook en in CI.

**Eindresultaat.**

- [ ] Op een schone machine: kloon, open `wikis/_template` in elk van de vijf AI-omgevingen, stel een inhoudelijke Vraag. De AI draait eerst `workspace-check`, vraagt toestemming, richt in en meldt wat de gebruiker zelf moet doen (koppeling goedkeuren, credentials instellen, eventueel herladen).
- [ ] Op Windows zonder Developer Mode en zonder beheerdersrechten lukt de inrichting (junction of kopie).
- [ ] Na inrichting noemt de AI in elke omgeving op de vraag "welke huisregels en vaardigheden heb je?" de root- en wiki-regels, zonder dubbele vaardigheden.
- [ ] De MCP-server `mediawiki` verbindt met de test-MediaWiki in elke omgeving.
- [ ] De tijd van klonen tot `workspace-check: ok` is per besturingssysteem gemeten en genoteerd (V9).

---

## Klus 3: Gereedschapskist

**Begin.** Klus 2 is af. `wikis/_template` werkt in alle vijf omgevingen.

**Taak.**

1. Bouw het gereedschap in `tools/llmwiki/`:
   - `pull` met titelmapping (`titles.py`) en een gecommit `revisies.json` (titel → laatst bekende revisie) per wiki (5.13);
   - `run start|status|complete|resume|close|abandon|prune` met State in `.work/runs/<run-id>/` (5.11); `phases_for(wiki_yaml)` bepaalt de fasen per wiki-soort (sync: alleen `validate`; curation: de vier fasen; knowledge-base: geen — geen run/gate);
   - schemas en `validate` voor source, assessment, changeset, validation-report, publish-plan, approval, run-state (5.12);
   - `publish plan|apply` (sync, via pywikibot) en `promote plan|apply` (curation): publicatievoorstel, akkoordcontrole (smaak A: `ja`, naam, actuele plan-hash), conflictcontrole (5.13); geen aparte records meer — beide schrijven een regel in `log.md`;
   - bronbeheer (5.19): `source add` (origineel en Markdown-conversie met dezelfde naam in `sources/raw/`, hash, weigert bestaand bron-id), `source list` met scoping via tags, `source add --from-export`; schema `source-index`; pre-commit staat in `sources/raw/` alleen toevoegen toe;
   - `run start --onderwerp` legt de bronlijst van de onderwerppagina vast; INGEST en ASSESS krijgen alleen die bronnen;
   - `lint` voor skillnamen, voorvoegsels, frontmatter, `requires-skills` en verboden verwijzingen van gedeelde naar wiki-specifieke onderdelen (5.4, 5.7);
   - zonder MediaWiki-afhankelijkheid (5.18): Markdown-validatie (frontmatter per paginatype, relatieve links, statusovergangen), `promote plan|apply`, `log.md` en `voortgang.md`; writers voor ArchiMate Open Exchange en CSV pas bij een concrete `exports:`-behoefte (Klus 4); pywikibot alleen via de extra `mediawiki`. Test met een tweede sjabloon `wikis/_template-md` (type `curation`) naast het bestaande `wikis/_template` (type `sync`).
2. Schrijf de gedeelde vaardigheden in `.agents/skills/`: `wiki-intake` (laag 2, controle van de conversie), `wiki-ingest` (laag 3, domein-lens), `wiki-publish` (sync), `wiki-kennis-ingest` (knowledge-base) (5.7). Alleen standaardvelden plus `metadata`; `wiki-publish` krijgt `disable-model-invocation: true` en `agents/openai.yaml` met `allow_implicit_invocation: false`.
3. Schrijf de gedeelde werkstromen `wiki-curatie-update` (curation: beoordelingen, scripts voor afleiden en renderen, akkoord in de chat; 5.13c) en `wiki-sync-edit` (sync) met stappen, rollen, uitbreidingspunten en de gate (5.8).
4. Schrijf tests voor het gereedschap, met ten minste deze gevallen voor de gate:
   - voorstel op `nee` → weigeren;
   - `ja` zonder naam → weigeren;
   - `ja` met een verouderde plan-hash → weigeren;
   - pagina op de site gewijzigd sinds ophalen → weigeren met conflictmelding;
   - afgebroken run → geen bestanden buiten `.work/`.

**Eindresultaat.**

- [ ] In `wikis/_template` doorloopt een testpagina de volledige `wiki-sync-edit`-workflow (pull → bewerken → validate → plan → akkoord → publish) tegen de test-MediaWiki, in minstens één AI-omgeving, met smaak A en met smaak B.
- [ ] Twee testbronnen (pdf en docx) staan als origineel en Markdown in `sources/raw/` en met intake in `sources/index/`; een tweede wiki hergebruikt de intake zonder die opnieuw te maken; een wijziging in `sources/raw/` wordt door de pre-commit-hook geweigerd.
- [ ] Een run gestart vanuit een onderwerppagina leest alleen de bronnen van die pagina; een bron buiten de tags van de wiki wordt door `validate` gemeld.
- [ ] Na publicatie staat een regel in `log.md` en is de testpagina bijgewerkt op de test-MediaWiki.
- [ ] In `wikis/_template-md` werkt een volledige run zonder MediaWiki-extra geïnstalleerd; een kandidaat die de Agent zelf op `goedgekeurd` zet, wordt door de pre-commit-hook geweigerd; `promote apply` schrijft `log.md` en werkt `voortgang.md` bij.
- [ ] Een onderbroken run is in een nieuwe sessie te hervatten vanaf de laatste afgeronde fase, zonder eerdere fasen opnieuw uit te voeren.
- [ ] "Prima" in smaak B leidt niet tot publicatie. In smaak A leidt een voorstel op `nee` niet tot publicatie.
- [ ] De AI-omgeving vraagt om een klik vóór `publish apply`.
- [ ] `llmwiki lint` en alle tests slagen.

---

## Klus 4: Eerste bewoner

**Begin.** Klus 3 is af. Toegang tot de GEMMA-site (of een testkopie) en tot het doel voor de architectuurmodel-export.

**Taak.**

1. Kopieer `wikis/_template` naar `wikis/gemma-online` (type `sync`, kale werkkopie). Vul `AGENTS.md` (domein, taal, stijl, doelgroep, naamgeving) en `wiki.yaml` (site, namespaces, gekozen smaak, bewaartermijn).
2. Haal de content op met `llmwiki pull` en commit die.
3. Optioneel, alleen voor zover een concreet probleem daarom vraagt: een losstaande curatie-wiki (bv. `wikis/gemma-begrippen`, type `curation` met een ingevuld `exports:`-blok voor ArchiMate) voor gestructureerde begrippenopbouw — géén onderdeel van `wikis/gemma-online` zelf (5.18: een sync-wiki heeft geen domein-lens). Voeg pas dan GEMMA-specifieke vaardigheden (`gemma-bo`, `gemma-archimate`), een schema en exportscripts toe, in die curatie-wiki.
4. Schrijf zo nodig een dunne wiki-Workflow bovenop `wiki-sync-edit` (sync) die GEMMA-specifieke controles toevoegt op het uitbreidingspunt VALIDATE (5.8).
5. Draai `llmwiki harness sync` en voer de pariteitstest uit in alle vijf omgevingen (sectie 8). Sluit de verificatiepunten V1 tot en met V10 af en werk `docs/onderbouwing.md` bij met de uitkomsten.

**Eindresultaat.**

- [ ] `cd wikis/gemma-online` en een Vraag als *"Werk deze pagina bij met wiki-sync-edit"* werkt in alle vijf omgevingen op dezelfde manier: dezelfde stappen, geldige tussenresultaten, stop bij het akkoord.
- [ ] Eén echte wijziging is gepubliceerd op de GEMMA-site, met een regel in `log.md` en een commit met de run-id.
- [ ] Als een curatie-wiki met exportdoel is toegevoegd: één architectuurmodel-export is via dezelfde gate uitgevoerd.
- [ ] Vanuit de hoofdmap zijn wiki-specifieke vaardigheden niet zichtbaar voor andere wiki's (`llmwiki lint` en een controle per omgeving).
- [ ] In Obsidian, geopend op de repository-root, werken links van `wikis/gemma-begrippen/bronnen/` (indien aanwezig) naar `sources/index/` en `sources/raw/`.
- [ ] De uitkomsten van V1 tot en met V10 staan in `docs/onderbouwing.md`, met eventuele aanpassingen aan de brug, de configuratie of de gate.
