# GEMMA-match

Het GEMMA-model (AMEFF-export of Archi-bronbestand) is een matchdoel: hoe staat dit element nu in GEMMA? Het is geen bron voor begrippen (het bestaande GEMMA-bedrijfsobjectenmodel is grotendeels een kopie van het GGM).

1. `uv run python tools/gemma.py kandidaten <naam> [--ggm-guid <guid>]` geeft de elementen die de GGM-guid als eigenschap dragen, de elementen met dezelfde naam en de treffers, elk met type, definitie en groepering (beleidsdomein).
2. Kies op betekenis en leg vast in `gemma`: `id` (bij een match), `sterkte` (zelfde schaal als bij het GGM) en `onderbouwing`: wat dit element verandert ten opzichte van GEMMA (nieuwe definitie, ander type, splitsing of samenvoeging). Geen GEMMA-element: `sterkte: geen` en in de onderbouwing waarom het nieuw is.
3. De letterlijke `gemma_*`-velden haalt `tools/afleiden.py` op. Wijkt de GEMMA-naam af van de naam: neem haar op in `synoniemen` met context "GEMMA".

De groepering op beleidsdomein is in GEMMA een aggregatie vanuit een Grouping; die leg je niet vast als relatie.
