# Repository-Rules

Deze regels gelden voor de hele repository. Wiki-specifieke regels staan in `wikis/<key>/AGENTS.md` en verwijzen hiernaar. Zie [ARCHITECTURE.md](ARCHITECTURE.md) voor de volledige uitleg, en `docs/onderbouwing.md` voor de redenen per keuze.

## Werkplek eerst

Bij de eerste Vraag in een Sessie, vóór inhoudelijk werk:

1. Draai `uv run python -m llmwiki workspace-check`. Werkt `uv` niet: leg in gewone taal uit dat de gebruiker eenmalig `scripts/setup.sh` (Linux/macOS) of `scripts/setup.ps1` (Windows) kan draaien (zie `README.md`, sectie Installatie), en stop.
2. Meldt workspace-check `herstelbaar`: vraag de gebruiker of je de werkplek mag inrichten, draai dan `uv run python -m llmwiki workspace-check --fix` en geef de meldingen in gewone taal door.
3. Meldt workspace-check `actie gebruiker`: leg per punt uit wat de gebruiker moet doen en begin niet aan inhoudelijk werk tot workspace-check `ok` meldt.
4. Opmerkingen van `workspace-check` (ontbrekende inloggegevens voor GEMMA Online, MCP-registratie) blokkeren geen inhoudelijk werk. Noem ze alleen als de Vraag pull of publish naar dat doel nodig heeft, en verwijs dan naar `README.md`, sectie *Inloggen op GEMMA Online*.

## Veiligheid

- Nooit publiceren of exporteren zonder akkoord van de redacteur. `llmwiki publish apply` en `llmwiki promote apply` controleren dit akkoord; omzeil ze niet.
- Vul akkoordvelden (`akkoord_voor_publicatie`, `beoordeeld_door`) nooit zelf in een publicatie- of promotievoorstel in, en wijzig daar nooit de kolommen Besluit en Opmerking: die zijn van de redacteur.
- Nooit credentials in bestanden. Alleen omgevingsvariabelen, genoemd bij naam in `wiki.yaml`.

## Herleidbaarheid

- Elke verwijzing naar een bron op een pagina is een relatieve link naar de domein-lens van die bron (laag 3), ook in tabellen; een bron-id als platte tekst is geen verwijzing. De domein-lens heeft onder de titel de links naar laag 1 (`llmwiki source bronregel --schrijf`). Keten: pagina → domein-lens → `sources/raw/`.
- `sources/index/` is een technische index om context te sparen (skill `wiki-intake`), geen schakel in die keten: pagina's linken er nooit naar.

## Rangorde

Bij tegenstrijdigheid: repository-veiligheidsregels > wiki-Rules > Skill-instructies
> Vraag van de gebruiker, voor zover die de publicatiegate raakt.

## Werkwijze

- Workflows zijn Skills (`.agents/skills/`), niet losse instructies in het gesprek.
- Tussenresultaten staan nooit alleen in het gesprek. Bij een curatie-wiki met beoordelingen (`curation.beoordelingen`) staan ze in de werkboom en zijn ze te zien in Git: het oordeel van de AI in de beoordelingen, de pagina's gegenereerd door de scripts van de wiki (skill `wiki-curatie-update`). Bij een sync-wiki gaan ze via `llmwiki run start|status|complete|resume|close|abandon`; een fase is pas afgerond na `llmwiki run complete <fase>`, dat het artefact tegen een schema valideert.
- Run-state staat in `.work/runs/<run-id>/` (gitignored). Dat is het kladblok; het wordt na afronding automatisch opgeruimd (`llmwiki workspace-check --fix`), nooit door het Model.
- Een gegenereerde pagina wordt nooit met de hand bewerkt; een status zet de AI nooit zelf, en het woord AKKOORD typt alleen de redacteur.
- Een Workflow noemt per stap een denkniveau: hoeveel redeneerinspanning het Model nodig heeft. **Laag**: een script draaien en de uitkomst doorgeven. **Middel**: nauwkeurig lezen en vastleggen, met weinig afweging. **Hoog**: oordelen en afwegen in samenhang, waar een fout doorwerkt in het resultaat. Een stap zonder niveau is middel. Elk harness vertaalt het niveau naar zijn eigen instelling (redeneerinspanning, of de keuze tussen een sneller en een sterker model); deze repository noemt geen model en geen harness-instelling. Bij de overgang naar een stap met een ander niveau: kan het Model het niveau zelf instellen, dan doet het dat; anders meldt het in één zin welk niveau de volgende stap vraagt en waarom, en wacht het tot de gebruiker het heeft ingesteld of zegt door te gaan. Een subagent krijgt het niveau van de stap die hij uitvoert. Wissel alleen tussen fasen, niet binnen een lus van stappen die elkaar herhalen.
- Todo's, afspraken en nieuwe regels komen in de repository, op de meest specifieke plek waar ze gelden: voor één wiki in `wikis/<key>/todo.md` of `wikis/<key>/AGENTS.md`, voor één Skill in die Skill, voor de hele repository in `todo.md` of deze `AGENTS.md`. Het persoonlijke geheugen van een harness (in de home-directory) alleen voor persoonlijke voorkeuren van de gebruiker: het is niet zichtbaar op andere werkplekken en niet voor andere gebruikers.

## Schrijfwijze

- Nooit een harde regelovergang binnen een zin of alinea in Markdown of wikitext: een alinea, een lijstitem of een tabelrij staat op één regel; de kolombreedte laat je over aan de viewer. Regelovergangen alleen waar ze betekenis hebben: tussen alinea's, lijstitems, tabelrijen, koppen, frontmatter-velden en in codeblokken. `llmwiki lint` controleert dit; `llmwiki ontvouw --schrijf` herstelt het. Uitgezonderd: `sources/raw/`, werkkopieën van externe sites (`wikis/*/content/`), logboeken en `Prompt en antwoorden/`.

## Grenzen

- Gedeelde Skills in `.agents/skills/` bevatten geen kennis van één specifieke wiki en verwijzen nooit naar een pad onder `wikis/`. Gecontroleerd door `llmwiki lint`.
- Wiki-Skills beginnen met de wiki-key (bijv. `gemma-`), gedeelde Skills met `wiki-`.
