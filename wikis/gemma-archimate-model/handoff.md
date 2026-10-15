# Handoff

Overdracht naar de volgende Sessie (2026-10-15). Wordt bij elke overdracht overschreven.

## Stand van zaken

- Plan goedgekeurd: [plannen/2026-10-15-lichtere-werkwijze.md](plannen/2026-10-15-lichtere-werkwijze.md).
- Stap 1 tot en met 4 uitgevoerd (commits "rules: afspraken lichtere werkwijze", "tools: beoordeling.py", "fix: kandidaten geven weer treffers", "tools: werkpakket", "tools: twee fasen in de beslistabel", "chore: opschonen 453 beoordelingen").
- Stap 5 uitgevoerd (commit "rules: skills herschreven voor fase A en B"):
  - Skill `gemma-archimate-model-update`: drie fasen (Sessies), elk met wat je leest. Fase 1: bronnen, werkpakket, eerst de catalogus, fase A, één tabel. Fase 2: fase B per cluster in beoordelingsagenten, met het sjabloon van de opdracht. Fase 3: beslissen tot en met commit (stap 11 tot en met 17). Skill `wiki-curatie-update` hoeft niet apart gelezen te worden.
  - Skill `criteria` is fase A, skill `beoordelen` is fase B. De gegenereerde vragenlijst staat niet meer in de criteria-skill: `bepaal_type.py vragen` vervangt haar, en `bepaal_type.py markdown` is vervallen. `kenmerken-en-beslistabel.md` blijft de volledige lijst.
  - `beslissen.py --alleen <id> …`: beslist over alles, schrijft en rendert niets, en toont alleen de meldingen en uitkomsten van die id's (met test).
  - Dubbelingen uit de references gehaald: de naamvorm per type (staat in de regel Naamvorm en in de modelleerafspraken), de volgorde van relaties (modelleerregels) en de GGM-vertaling van relaties (nu in de docstring van `tools/relaties.py`). Een verouderd registerpad in `relaties.md` is hersteld.
  - ARCHITECTURE.md, sectie 4: van 2.187 naar 1.424 woorden. De koppen 4.1 tot en met 4.5 en het waarom zijn gebleven; wat het kennismodel al beschrijft, is een verwijzing.
  - Gelezen regels per fase (gemeten met `wc`, inclusief beide AGENTS.md): fase 1 hoofdsessie 10.615 (de bronduiding in een subagent: 4.775; doet de hoofdsessie de ingest zelf: 12.607); fase 2 hoofdsessie 4.391; beoordelingsagent voor een cluster met proces, object, gebeurtenis en dienst 11.966, met alle references 13.930; fase 3 7.169.
  - Controle: `beslissen.py` werkt 0 bestanden bij, `render.py --check` en `archimate_export.py --check` slagen, pytest en lint zonder fouten.
- Stap 6 uitgevoerd (commits "tools: sjablonen en afronden", "rules: sjabloon en afronden in de skills"):
  - `beoordeling.py sjabloon upl-dienst <id> --naam … --onderwerp … --kernobject … --bron … (--proces <id> | --proces-naam …)` (logica in `tools/sjablonen.py`): zet de dienst klaar (kenmerken van fase A en B, velden van de indeling) met een bestaand proces (alleen de relatie realisatie erbij) of een nieuw proces (eigen kenmerken, kernobject, optioneel toegang). Elke ja-onderbouwing, definitie, beschrijving en GEMMA-tekst is `TODO` met de opgegeven bronnen; `beslissen.py` meldt een fout zolang er een TODO staat. Een bestaande beoordeling wordt niet overschreven. Geen `status`, geen `beslist`.
  - `tools/afronden.py --bericht "<prefix>: …"` (na `promote apply`): weigert zonder gewijzigde `log.md`, draait commit-check op het bericht, export-check, export, render-check en lint, en commit pas als alles slaagt (`--droog` toont de stappen). Skill update, stap 16 en 17, verwijst ernaar.
  - Controle: pytest (246) en lint zonder fouten; `beslissen.py` werkt 0 bestanden bij, `render.py --check` en `archimate_export.py --check` slagen. Tests: een sjabloon komt na invullen van de TODO's door `beslissen.py` als dienst en als bedrijfsproces.
  - Niet gebouwd: andere patronen dan upl-dienst (komt erbij als een patroon zich herhaalt); afronden is niet in een echte `promote apply`-cyclus gedraaid (dat gebeurt in de proef, stap 9).
- Nog niet gedaan: compacte uitvoer van `llmwiki promote plan` (valt onder stap 8, of als eigen punt in de todo).

## Scope

Stap 7 van het plan: **bronduiding** (B4, C4, D2) in skill `gemma-archimate-model-ingest`. Klaar als een nieuwe bronduiding met citaten uit het script komt. Denkniveau middel. Lees uit het plan alleen de rijen B4, C4 en D2, de rij van stap 7 en de sectie Controle. Daarna stap 8 en verder, elk in een eigen commit na akkoord.

## Besluiten die gelden

- Geen inhoudelijke wijzigingen in deze klus: de beslistabel, de typen, de uitkomsten en de export blijven gelijk.
- Alleen de kenmerken met ja vastleggen is afgeraden; de nee die de uitkomst bepaalt, blijft als dubbelcheck (afgedwongen: elk kenmerk op het pad staat er expliciet in).
- 2026-10-15: na een opschoning die de inhoudshash raakt, gaat het akkoord opnieuw via de gewone poort (`promote plan`, AKKOORD, `promote apply`), met het bewijs dat `beslist`, de pagina's en de export gelijk blijven; commit pas na het akkoord.
- 2026-10-15: ARCHITECTURE.md sectie 4 houdt het waarom; het wat staat in het kennismodel.
- 2026-10-14: elk levensloopproces met afnemer extern realiseert minstens één UPL-dienst (voor de proef, stap 9).
- 2026-10-14: de plaats van Verzorgen gemeentebegrafenis is geparkeerd; het advies is optie 1 (voor de proef, stap 9).
- 2026-10-15: geen gereedschaps- of harnessspecifieke hooks; controles zijn gewone commando's.
- De wiki-skills staan in `.agents/skills/`; `.claude/skills/` is een gitignored kopie (bijwerken met `llmwiki workspace-check --fix`), wijzig alleen `.agents/skills/`.

## Werkwijze

- Per stap: kort voorleggen wat er verandert, dan uitvoeren, dan commit met een prefix en een bericht van één of twee zinnen; controleer met `uv run python -m llmwiki commit-check <bestand>`.
- Voorleggen voor een architect: in gewone taal en analytisch, met de gevolgen voor het model, de bron als link.
- Commit direct op main.

## Modeladvies

Stap 7 vraagt denkniveau middel: een skill en een script rond bronduidingen, met weinig afweging. Een sneller model of een gemiddelde redeneerinspanning volstaat. Begin een nieuwe Sessie.

## Startprompt

```text
Lees wikis/gemma-archimate-model/handoff.md en voer stap 7 uit van plannen/2026-10-15-lichtere-werkwijze.md (sectie Uitvoering): bronduiding (B4, C4, D2) in skill gemma-archimate-model-ingest. Lees uit het plan alleen de rijen B4, C4 en D2, de rij van stap 7 en de sectie Controle. Klaar als een nieuwe bronduiding met citaten uit het script komt, en pytest en lint zonder fouten zijn. Leg kort voor wat je bouwt, voer uit na mijn akkoord, en commit met een prefix.
```
