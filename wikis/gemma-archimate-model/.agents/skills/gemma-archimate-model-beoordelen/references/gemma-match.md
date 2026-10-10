# GEMMA-match

Het GEMMA-model (AMEFF-export of Archi-bronbestand) is een matchdoel: hoe staat dit element nu in GEMMA? Het is geen bron voor begrippen (het bestaande GEMMA-bedrijfsobjectenmodel is grotendeels een kopie van het GGM).

1. `uv run python tools/gemma.py kandidaten <naam> [--ggm-guid <guid>]` geeft de elementen die de GGM-guid als eigenschap dragen, de elementen met dezelfde naam en de treffers, elk met type, definitie en groepering (beleidsdomein).
2. Kies op betekenis en leg vast in `gemma`: `id` (bij een match), `sterkte` (zelfde schaal als bij het GGM) en `onderbouwing`: wat dit element verandert ten opzichte van GEMMA (nieuwe definitie, ander type, splitsing of samenvoeging). Geen GEMMA-element: `sterkte: geen` en in de onderbouwing waarom het nieuw is.
3. Een match met `id` is een koppeling: de export naar Archi geeft het element dat GEMMA-id en overschrijft daarmee naam en definitie van het GEMMA-element. Een `zwak` of `partieel` match leg je daarom altijd voor (regel Zwakke match voorleggen); is het niet hetzelfde begrip, dan `sterkte: geen` en het GEMMA-element in de onderbouwing.
4. De letterlijke `gemma_*`-velden haalt `tools/beslissen.py` op. Wijkt de GEMMA-naam af van de naam: neem haar op in `synoniemen` met context "GEMMA".

De groepering op beleidsdomein is in GEMMA een aggregatie vanuit een Grouping; die leg je niet vast als relatie.

## De plek in een GEMMA-indeling (`gemma_relatie`)

De wiki volgt de GEMMA-indelingen; een bewering over de plek van een element daarin steunt op de GEMMA-relatie, niet op een bron (regel Elke claim een bron).

- Kenmerk *in functie-indeling* of *zelfstandige specialisatie* van een gematchte functie: geen `bronnen`, maar `gemma_relatie` met het id van de aggregatie of compositie naar de GEMMA-match, vanuit de bovenliggende functie of de domeingroepering (`uv run python tools/gemma.py relaties <id>`). Het script toetst dat de relatie bestaat en, bij *zelfstandige specialisatie*, dat de GEMMA-match geen ander element specialiseert.
- Een aggregatie in de functieketen tussen twee gematchte functies: geen `bronnen` en `vindplaats`, maar `gemma_relatie: <id>`; het script toetst type, bron en doel.
- Alleen de plek is uitgezonderd. Wat een functie is en doet (*gedrag*, *gegroepeerd gedrag*, *eigen identiteit*, *stabiel over tijd*, *herkenbaar*, *generiek*) heeft een bron: de redactionele tekst van GEMMA Online (Bedrijfsfuncties, de bedrijfsarchitectuur per domein), de wet of een praktijkbron. Een view, tabel, boom of toelichting op GEMMA Online komt uit het model en is geen bron.
