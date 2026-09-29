| Eigenaar                    | Ingevuld door |
| --------------------------- | ------------- |
| Kennis Centrum Architectuur | Mark Backer   |

# GEMMA kenniswerkplek: monorepo voor LLM-wiki's

Zie [ARCHITECTURE.md](ARCHITECTURE.md) voor het architectuur-kompas, [docs/kluswijzer.md](docs/kluswijzer.md) voor de inrichtingsstappen en [docs/onderbouwing.md](docs/onderbouwing.md) voor de volledige onderbouwing.

## Status van deze inrichting

Uitgevoerd: **Klus 1 (Fundament)**, **Klus 3 (Gereedschapskist)** volledig — inclusief het MediaWiki-deel — en **Klus 2 (Werkplek)** grotendeels. Concreet werkt nu:

- Drie wiki-soorten (`sync`, `curation`, `knowledge-base`; zie `ARCHITECTURE.md` §1 en `docs/onderbouwing.md` 5.18) met de bijbehorende `llmwiki`-CLI: run-State, de publicatiegate (`promote plan|apply` voor curatie, `publish plan|apply` voor sync, beide smaak A en B), `pull` en echte MediaWiki-publicatie via pywikibot, bronbeheer, lint, `workspace-check` en `harness sync|check`.
- `llmwiki harness sync` genereert de Claude Code-brug, `.claude/settings.json`, `.vscode/settings.json`, `opencode.json` en (voor sync-wiki's) de MCP-configuratie voor Claude Code/VS Code/Cursor. `llmwiki harness check` staat in de pre-commit-hook en in `.github/workflows/check.yml`.
- Testsjablonen: `wikis/_template-md/` (curatie) en `wikis/_template/` (sync, wijst naar GEMMA staging als testomgeving).

**Nog niet zelf geverifieerd** (kon niet vanuit deze sessie: geen live MCP-registratie, geen netwerkcredentials):

- MCP-registratie en een live verbinding tegen GEMMA staging/productie.
- Codex- en Cursor-specifieke discovery (`llmwiki harness sync` genereert daar bewust niets voor — zie verificatiepunten V6t/m V10 in `docs/onderbouwing.md` sectie 8).
- Windows: de junction-fallback van de skill-brug (geschreven, niet op Windows getest).
- De volledige `wiki-edit`-workflow (pull → bewerken → plan → akkoord → publish) tegen een echte testpagina op staging.

Zie `docs/kluswijzer.md` Klus 4 voor het vervolg (de GEMMA-wiki zelf inrichten).

## Installatie voor redacteuren

Je hebt maar twee dingen nodig: deze map op je computer (gekregen via Git, of gewoon als map van een collega/IT), en een terminalvenster om één keer een setup-script te starten.

1. Open een terminal in deze map:
   - **Windows**: rechtsklik in de mapweergave op een lege plek → "Openen in Terminal" (of "PowerShell hier openen").
   - **macOS**: rechtsklik de map → Services → "Nieuwe Terminal in map" (of open Terminal en typ `cd ` gevolgd door de map hierheen slepen).
   - **Linux**: rechtsklik in je bestandsbeheerder → "Open in Terminal".
2. Typ en druk op Enter:
   - **Windows (PowerShell)**: `.\scripts\setup.ps1`
   - **macOS/Linux**: `./scripts/setup.sh`
3. Het script installeert zelf wat nodig is (de tool `uv`, de Python-omgeving) en sluit af met "Klaar." Lees onderweg gerust mee; er wordt niets onomkeerbaars gedaan.
4. Open deze map daarna in je AI-assistent (bijvoorbeeld Claude Code, zoals je organisatie die heeft ingericht) en stel een inhoudelijke vraag. Zie "Gebruik voor redacteuren" hieronder.

Loopt er iets vast? Het script stopt met een duidelijke melding in gewone taal over wat je zelf nog moet doen (bijvoorbeeld: terminal opnieuw openen). Vraag anders je AI-assistent om `uv run llmwiki workspace-check` te draaien en de uitkomst uit te leggen.

## Gebruik voor redacteuren

1. Open de map (of de map van de specifieke wiki, bijvoorbeeld `wikis/gemma`) in je AI-assistent.
2. Stel een gewone vraag in je eigen woorden, bijvoorbeeld: *"Verwerk dit document voor onderwerp zaakgericht werken"*. De assistent controleert eerst zelf de werkplek en legt uit als er iets ontbreekt.
3. De assistent werkt in stappen (lezen, beoordelen, schrijven, controleren) en stopt daarna altijd voor een menselijke beslissing: je krijgt een voorstel te lezen, óf je moet in de chat letterlijk het woord **AKKOORD** typen. Zonder die stap publiceert of wijzigt de assistent nooit iets definitiefs.
4. Na jouw akkoord vraagt je AI-omgeving (Claude Code, Cursor, …) nóg een keer om een klik ter bevestiging voordat het commando echt uitvoert. Dat is een ingebouwde veiligheidsklep; keur die alleen goed als je de wijziging al hebt gelezen.
5. Twijfel je? Vraag de assistent gewoon: "wat gebeurt hierna?" of "laat me eerst het voorstel zien". Er gaat niets verloren als je een taak halverwege afbreekt.

## Installatie: technische achtergrond

Het setup-script hierboven doet het volgende, en je kunt het ook los uitvoeren:

Nodig op elk besturingssysteem: [Git](https://git-scm.com/) en [uv](https://docs.astral.sh/uv/). Node.js is pas nodig zodra Klus 2 de MediaWiki-MCP-server aansluit.

```bash
git clone <url>
cd second-brain
uv sync
uv run llmwiki --version
```

### Windows

- Installeer Git en uv zoals hierboven (het setup-script doet dit voor je).
- Zet lange paden aan (eenmalig, geen beheerdersrechten nodig); het setup-script doet dit ook automatisch:
  ```powershell
  git config --global core.longpaths true
  ```

### Werkplekcontrole

Bij elke sessie draait de AI-assistent eerst `uv run llmwiki workspace-check` (zie de root-`AGENTS.md`). Die controleert de Python-omgeving, de harness-bindingen (`llmwiki harness check`), CLAUDE.md-uitschakeling, of `pywikibot`/`npx` aanwezig zijn waar nodig, of de in `wiki.yaml` genoemde pywikibot-family geregistreerd is, en onafgeronde runs. Voor een sync-wiki toont ze ook het eenmalige MCP-registratiecommando als dat nog niet is uitgevoerd.
