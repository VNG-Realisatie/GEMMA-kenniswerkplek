# Repository-Rules

Deze regels gelden voor de hele repository. Wiki-specifieke regels staan in
`wikis/<key>/AGENTS.md` en verwijzen hiernaar. Zie [ARCHITECTURE.md](ARCHITECTURE.md)
voor de volledige uitleg, en `docs/onderbouwing.md` voor de redenen per keuze.

## Werkplek eerst

Bij de eerste Vraag in een Sessie, vóór inhoudelijk werk:

1. Draai `uv run llmwiki workspace-check`.
   Werkt `uv` niet: leg in gewone taal uit dat de gebruiker eenmalig
   `scripts/setup.sh` (Linux/macOS) of `scripts/setup.ps1` (Windows) kan draaien
   (zie `README.md`, sectie Installatie), en stop.
2. Meldt workspace-check `herstelbaar`: vraag de gebruiker of je de werkplek mag inrichten,
   draai dan `uv run llmwiki workspace-check --fix` en geef de meldingen in gewone taal door.
3. Meldt workspace-check `actie gebruiker`: leg per punt uit wat de gebruiker moet doen en
   begin niet aan inhoudelijk werk tot workspace-check `ok` meldt.
4. De Claude Code-brug en MCP-configuratie (Klus 2) zijn in deze inrichting nog niet
   gebouwd; `workspace-check` meldt dat als opmerking, niet als fout.

## Veiligheid

- Nooit publiceren of exporteren zonder akkoord van de redacteur. `llmwiki publish
  apply` en `llmwiki promote apply` controleren dit akkoord; omzeil ze niet.
- Vul akkoordvelden (`akkoord_voor_publicatie`, `beoordeeld_door`) nooit zelf in een
  publicatie- of promotievoorstel in.
- Nooit credentials in bestanden. Alleen omgevingsvariabelen, genoemd bij naam in
  `wiki.yaml`.

## Rangorde

Bij tegenstrijdigheid: repository-veiligheidsregels > wiki-Rules > Skill-instructies
> Vraag van de gebruiker, voor zover die de publicatiegate raakt.

## Werkwijze

- Workflows zijn Skills (`.agents/skills/`), niet losse instructies in het gesprek.
- Tussenresultaten gaan via `llmwiki run start|status|complete|resume|close|abandon`,
  nooit alleen in het gesprek. Een fase is pas afgerond na `llmwiki run complete
  <fase>`, dat het artefact tegen een schema valideert.
- State staat in `.work/runs/<run-id>/` (gitignored). Dat is het kladblok; het wordt
  na afronding automatisch opgeruimd (`llmwiki workspace-check --fix`), nooit door het Model.

## Grenzen

- Gedeelde Skills in `.agents/skills/` bevatten geen kennis van één specifieke wiki en
  verwijzen nooit naar een pad onder `wikis/`. Gecontroleerd door `llmwiki lint`.
- Wiki-Skills beginnen met de wiki-key (bijv. `gemma-`), gedeelde Skills met `wiki-`.
