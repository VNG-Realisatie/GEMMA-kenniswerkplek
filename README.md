| Eigenaar                    | Ingevuld door |
| --------------------------- | ------------- |
| Kennis Centrum Architectuur | Mark Backer   |

# GEMMA kenniswerkplek: monorepo voor LLM-wiki's

Zie [ARCHITECTURE.md](ARCHITECTURE.md) voor het architectuur-kompas en [docs/onderbouwing.md](docs/onderbouwing.md) voor de volledige onderbouwing.

## Wat er werkt

- Drie wiki-soorten (`sync`, `curation`, `knowledge-base`; zie `ARCHITECTURE.md` §1 en `docs/onderbouwing.md` 5.18) met de bijbehorende `llmwiki`-CLI: run-State, de publicatiegate (`promote plan|apply` voor curatie, `publish plan|apply` voor sync), `pull` en publicatie naar MediaWiki via pywikibot, bronbeheer, lint, `workspace-check` en `harness sync|check`.
- `llmwiki harness sync` genereert de Claude Code-brug naar de skills, `.claude/settings.json`, `.vscode/settings.json`, `opencode.json` en (voor sync-wiki's) de MCP-configuratie voor Claude Code/VS Code/Cursor. `llmwiki harness check` staat in de pre-commit-hook en in `.github/workflows/check.yml`.
- Wiki's: `wikis/gemma-online` (sync met GEMMA Online), `wikis/gemma-archimate-model` (curatie van het GEMMA-architectuurmodel), en de sjablonen `wikis/_template` (sync) en `wikis/_template-md` (curatie).

**Nog niet live getest:**

- Publiceren naar GEMMA Online (redactie en staging). Inloggen en ophalen met de inloggegevens uit omgevingsvariabelen is getest en werkt (zie *Inloggen op GEMMA Online*).
- De MCP-verbinding met GEMMA Online.
- Codex- en Cursor-specifieke discovery (zie verificatiepunten V6 t/m V11 in `docs/onderbouwing.md` sectie 8).
- De volledige `wiki-edit`-workflow (pull → bewerken → plan → akkoord → publish) tegen een echte testpagina op staging.

## Installatie voor redacteuren

Je hebt maar twee dingen nodig: deze map op je computer (gekregen via Git, of gewoon als map van een collega/IT), en een terminalvenster om één keer een setup-script te starten.

1. Open een terminal in deze map:
   - **Windows**: rechtsklik in de mapweergave op een lege plek → "Openen in Terminal" (of "PowerShell hier openen").
   - **macOS**: rechtsklik de map → Services → "Nieuwe Terminal in map" (of open Terminal en typ `cd ` gevolgd door de map hierheen slepen).
   - **Linux**: rechtsklik in je bestandsbeheerder → "Open in Terminal".
2. Typ en druk op Enter:
   - **Windows (PowerShell)**: `.\scripts\setup.ps1`
   - **macOS/Linux**: `./scripts/setup.sh`
3. Het script installeert zelf wat nodig is (de tool `uv`, de Python-omgeving), controleert de werkplek en sluit af met "Klaar." Er wordt niets onomkeerbaars gedaan.
4. Het script vraagt of je met de wiki GEMMA Online (`wikis/gemma-online`) gaat werken. Alleen dan heb je inloggegevens nodig; het script laat zien welke nog ontbreken en biedt op Windows aan ze meteen in te stellen (zie *Inloggen op GEMMA Online*). Werk je alleen met `gemma-archimate-model` of een andere wiki, antwoord dan *nee*: je kunt zonder. Later alsnog instellen kan met `.\scripts\setup.ps1 -GemmaOnline` of `./scripts/setup.sh --gemma-online`.
5. Open deze map daarna in je AI-assistent (bijvoorbeeld Claude Code) en stel een inhoudelijke vraag. Zie "Gebruik voor redacteuren" hieronder.

Loopt er iets vast? Het script stopt met een duidelijke melding in gewone taal over wat je zelf nog moet doen (bijvoorbeeld: terminal opnieuw openen). Vraag anders je AI-assistent om `uv run python -m llmwiki workspace-check` te draaien en de uitkomst uit te leggen.

## Gebruik voor redacteuren

1. Open de map (of de map van de specifieke wiki, bijvoorbeeld `wikis/gemma-online`) in je AI-assistent.
2. Stel een gewone vraag in je eigen woorden, bijvoorbeeld: *"Verwerk dit document voor onderwerp zaakgericht werken"*. De assistent controleert eerst zelf de werkplek en legt uit als er iets ontbreekt.
3. De assistent werkt in stappen (lezen, beoordelen, schrijven, controleren) en stopt daarna altijd voor een menselijke beslissing: je krijgt een voorstel te lezen, óf je moet in de chat letterlijk het woord **AKKOORD** typen. Zonder die stap publiceert of wijzigt de assistent nooit iets definitiefs.
4. Na jouw akkoord vraagt je AI-omgeving (Claude Code, Cursor, …) nóg een keer om een klik ter bevestiging voordat het commando echt uitvoert. Dat is een ingebouwde veiligheidsklep; keur die alleen goed als je de wijziging al hebt gelezen.
5. Twijfel je? Vraag de assistent gewoon: "wat gebeurt hierna?" of "laat me eerst het voorstel zien". Er gaat niets verloren als je een taak halverwege afbreekt.

## Inloggen op GEMMA Online

Alleen nodig voor de sync-wiki `wikis/gemma-online`, om pagina's op te halen van en te publiceren naar GEMMA Online. Voor `gemma-archimate-model` en de andere wiki's kun je zonder; dan heb je ook Node.js (`npx`, voor de MCP-server van GEMMA Online) niet nodig. Je inloggegevens staan **nooit** in een bestand in deze map: je zet ze als omgevingsvariabelen van je eigen gebruikersaccount. `wikis/gemma-online/wiki.yaml` noemt alleen de namen.

### 1. Maak botwachtwoorden aan

Gebruik niet je gewone wachtwoord, maar per omgeving een **botwachtwoord**. Dat heeft alleen de rechten die publiceren nodig heeft en kun je los intrekken.

1. Log in op de wiki en ga naar *Speciaal:BotWachtwoorden* (redactie: `https://redactie.gemmaonline.nl/wiki/Speciaal:BotWachtwoorden`; staging: dezelfde pagina op `gemma2-redactie.staging.wikixl.nl`).
2. Kies een botnaam, bijvoorbeeld `llmwiki`, en vink alleen *Basisrechten* en *Pagina's bewerken* aan (en *Grote bewerkingen* als je veel pagina's tegelijk publiceert).
3. Je krijgt een gebruikersnaam in de vorm `Jouwnaam@llmwiki` en een wachtwoord. Die twee heb je hieronder nodig.

Voor staging heb je daarnaast de gebruikersnaam en het wachtwoord van de extra toegangslaag (de inlogvraag van je browser vóór de wiki); die krijg je van de beheerder van staging.

### 2. Zet de omgevingsvariabelen

| Variabele | Inhoud |
|---|---|
| `GEMMA_REDACTIE_USER` | Botgebruikersnaam op redactie, bijv. `Jouwnaam@llmwiki` |
| `GEMMA_REDACTIE_BOTPASSWORD` | Botwachtwoord op redactie |
| `GEMMA_STAGING_USER` | Botgebruikersnaam op staging |
| `GEMMA_STAGING_BOTPASSWORD` | Botwachtwoord op staging |
| `GEMMA_STAGING_HTTP_USER` | Gebruikersnaam van de extra toegangslaag van staging |
| `GEMMA_STAGING_HTTP_PASSWORD` | Wachtwoord van de extra toegangslaag van staging |

**Windows, met het script (aanbevolen, geen beheerdersrechten nodig):** open PowerShell in deze map en typ

```powershell
.\scripts\inlog-instellen.ps1
```

Het script vraagt per variabele de waarde en slaat die blijvend op voor je eigen account. Wachtwoorden typ je onzichtbaar in en ze komen niet in de PowerShell-geschiedenis. Laat een vraag leeg om een variabele ongewijzigd te laten, bijvoorbeeld als je alleen staging wilt instellen. Sluit daarna VS Code en elke terminal volledig af en open ze opnieuw: alleen nieuwe vensters zien de variabelen.

**Windows, via het menu** (hetzelfde resultaat):

1. Open *Start*, typ `omgevingsvariabelen` en kies **Omgevingsvariabelen voor uw account bewerken** (niet "Systeemomgevingsvariabelen bewerken"; daarvoor zijn beheerdersrechten nodig).
2. Klik in het bovenste blok, *Gebruikersvariabelen voor \<jouw naam\>*, op **Nieuw...**.
3. Vul bij *Naam van variabele* bijvoorbeeld `GEMMA_REDACTIE_USER` in en bij *Waarde van variabele* je botgebruikersnaam. Klik **OK**.
4. Herhaal dit voor elke variabele uit de tabel en sluit af met **OK**.
5. Sluit VS Code en elke terminal volledig af en open ze opnieuw.

**macOS/Linux:** zet per variabele een regel `export GEMMA_REDACTIE_USER='Jouwnaam@llmwiki'` in je shellprofiel (`~/.zshrc` of `~/.bashrc`) en open een nieuwe terminal.

### 3. Controleer

Draai `uv run python -m llmwiki workspace-check` (of het setup-script opnieuw). Staan er geen opmerkingen meer over `GEMMA_…`-variabelen, dan zijn ze gezet. Of het inloggen zelf lukt, zie je bij de eerste `pull`, bijvoorbeeld `uv run python -m llmwiki pull --wiki wikis/gemma-online --titel "Wat is GEMMA" --doel staging`.

Omgevingsvariabelen zijn leesbaar voor elk programma dat onder je eigen account draait; daarom een botwachtwoord met beperkte rechten. Vermoed je dat het gelekt is: trek het in op *Speciaal:BotWachtwoorden* en maak een nieuw aan. De afweging staat in `docs/onderbouwing.md` 5.10a.

## Installatie: technische achtergrond

Het setup-script hierboven doet het volgende, en je kunt het ook los uitvoeren:

Nodig op elk besturingssysteem: [Git](https://git-scm.com/) en [uv](https://docs.astral.sh/uv/). Node.js is nodig voor de MediaWiki-MCP-server van sync-wiki's.

```bash
git clone <url>
cd GEMMA-kenniswerkplek
uv sync
uv run python -m llmwiki --version
```

### Python-omgeving

- **Altijd via `python -m`.** De CLI en de tests draaien als `uv run python -m llmwiki …` en `uv run python -m pytest`, niet als `uv run llmwiki`. De programma's die `uv` in `.venv\Scripts` aanmaakt (zoals `llmwiki.exe`) zijn lokaal gemaakt en niet ondertekend; op beheerde Windows-laptops kan beveiligingsbeleid ze blokkeren. `python.exe` is wel ondertekend. De permissies in `.claude/settings.json` en de pre-commit-hooks gaan van deze vorm uit.
- **Alles in één keer.** `uv sync` installeert alle onderdelen, ook de groepen `mediawiki` (pywikibot) en `pdf` (pdf-conversie); zie `[tool.uv] default-groups` in `pyproject.toml`. Een latere `uv sync` haalt er dus niets van weg.
- **Geen C-compiler nodig.** pywikibot gebruikt `mwparserfromhell`. Daarvan bestaat niet voor elke Python-versie een kant-en-klaar pakket (bijvoorbeeld nog niet voor Python 3.14 op Windows); zelf bouwen vraagt dan de Microsoft C++ Build Tools. `pyproject.toml` zet daarom `WITH_EXTENSION=0` voor dit pakket (`[tool.uv.extra-build-variables]`): uv bouwt dan de variant in puur Python. Komt er een kant-en-klaar pakket, dan gebruikt uv dat en doet de instelling niets. De Python-versie zelf zetten we bewust niet vast: een door uv gedownloade Python is niet ondertekend en loopt op beheerde laptops tegen hetzelfde beveiligingsbeleid aan.

### Windows

- Installeer Git en uv zoals hierboven (het setup-script doet dit voor je).
- Zet lange paden aan (eenmalig, geen beheerdersrechten nodig); het setup-script doet dit ook automatisch:
  ```powershell
  git config --global core.longpaths true
  ```

### Werkplekcontrole

Bij elke sessie draait de AI-assistent eerst `uv run python -m llmwiki workspace-check` (zie de root-`AGENTS.md`). Die controleert de Python-omgeving, de harness-bindingen (`llmwiki harness check`), CLAUDE.md-uitschakeling, of `pywikibot` aanwezig is waar nodig, of elk family-bestand uit `wiki.yaml` in de wiki-map staat (`wikis/<wiki>/families/<naam>_family.py`: de servers van een sync-wiki, zonder geheimen), en onafgeronde runs. Als opmerking (niet blokkerend, alleen van belang als je met `wikis/gemma-online` werkt) meldt ze welke inlogvariabelen voor GEMMA Online nog ontbreken, of `npx` ontbreekt, en het eenmalige MCP-registratiecommando.
