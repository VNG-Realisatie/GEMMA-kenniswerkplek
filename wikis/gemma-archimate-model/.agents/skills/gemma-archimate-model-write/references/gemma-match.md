# GEMMA-match

Het GEMMA-model (AMEFF-export of Archi-bronbestand) is een matchdoel: hoe staat dit element nu in GEMMA? Het is geen bron voor begrippen (het bestaande GEMMA-bedrijfsobjectenmodel is grotendeels een kopie van het GGM).

1. Heeft het element een `ggm_guid`: `uv run python tools/gemma.py koppel <ggm_guid>` (zoekt de GGM-GUID in de eigenschappen van GEMMA-elementen, in elk formaat). Anders: `tools/gemma.py zoek <naam>`.
2. Kies het GEMMA-element en bepaal `match.gemma` met dezelfde schaal als bij het GGM.
3. Plak de uitvoer van `uv run python tools/gemma.py velden <id>` ongewijzigd in de frontmatter (`gemma_*`).
4. In `## GEMMA`: de matchsterkte, en wat dit element verandert ten opzichte van GEMMA (nieuwe definitie, ander type, splitsing of samenvoeging). Geen GEMMA-element: vermeld dat het element nieuw is voor GEMMA.

De groepering op beleidsdomein is in GEMMA een aggregatie vanuit een Grouping. Die leg je niet vast als relatie; `tools/check_elementen.py` vergelijkt `beleidsdomein` met die groepering en meldt afwijkingen.
