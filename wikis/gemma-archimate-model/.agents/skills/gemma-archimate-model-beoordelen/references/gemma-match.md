# GEMMA-match

Het GEMMA-model (AMEFF-export of Archi-bronbestand) is een matchdoel: hoe staat dit element nu in GEMMA? Het is geen bron voor begrippen (het bestaande GEMMA-bedrijfsobjectenmodel is grotendeels een kopie van het GGM).

1. `uv run python tools/gemma.py kandidaten <naam> [--ggm-guid <guid>]` geeft de elementen die de GGM-guid als eigenschap dragen, de elementen met dezelfde naam en de treffers, elk met type, definitie en groepering (beleidsdomein).
2. Kies op betekenis en leg vast in `gemma`: `id` (bij een match), `sterkte` (zelfde schaal als bij het GGM) en `onderbouwing`: wat dit element verandert ten opzichte van GEMMA (nieuwe definitie, ander type, splitsing of samenvoeging). Geen GEMMA-element: `sterkte: geen` en in de onderbouwing waarom het nieuw is.
3. Een match met `id` is een koppeling: de export naar Archi geeft het element dat GEMMA-id en overschrijft daarmee naam en definitie van het GEMMA-element. Een `zwak` of `partieel` match leg je daarom altijd voor (regel Zwakke match voorleggen); is het niet hetzelfde begrip, dan `sterkte: geen` en het GEMMA-element in de onderbouwing.
4. De letterlijke `gemma_*`-velden haalt `tools/beslissen.py` op. Wijkt de GEMMA-naam af van de naam: neem haar op in `synoniemen` met context "GEMMA".
5. Staat een begrip meer dan eens als GGM-bedrijfsobject in GEMMA, omdat GEMMA de duplicaten van het GGM als losse objecten overneemt, koppel dan het object van de primaire GGM-entiteit (`ggm-match.md`, Duplicaten en homoniemen); de andere blijven ongewijzigd in GEMMA. Dat staat in één GEMMA-terugmelding voor alle duplicaten; meld het niet per geval. Een naamgenoot die een ander begrip is (een homoniem, zoals de interne Aanvraag van ICT), blijft ongekoppeld.

De groepering op beleidsdomein is in GEMMA een aggregatie vanuit een Grouping; die leg je niet vast als relatie.

## De plek in een GEMMA-indeling (`gemma_relatie`)

De wiki neemt de GEMMA-indelingen letterlijk over; een bewering over de plek van een element daarin steunt op de GEMMA-relatie, niet op een bron (regel Elke claim een bron).

- Kenmerk *in functie-indeling* van een gematchte functie: geen `bronnen`, maar `gemma_relatie` met het id van de aggregatie of compositie naar de GEMMA-match, vanuit de bovenliggende functie of de domeingroepering (`uv run python tools/gemma.py relaties <id>`). Het script toetst dat de relatie bestaat.
- Een aggregatie in de functieketen tussen twee gematchte functies: geen `bronnen` en `vindplaats`, maar `gemma_relatie: <id>`; het script toetst type, bron en doel.
- Alleen de plek is uitgezonderd. Wat een functie is en doet (*gedrag*, *gegroepeerd gedrag*, *afhankelijkheid*, *stabiel over tijd*, *herkenbaar*, *generiek*) heeft een bron voor de inhoud: de wet die de taak geeft, of een praktijkbron. GEMMA Online is matchdoel en geen bron, ook niet haar redactionele tekst over de inhoud (ARCHITECTURE.md, sectie 2).
- Wat een functie is, en welke functie een element wordt: de regels Bronvoorrang en Wettelijke grondslag.

## De plek onder een knoop (`gemma_functie`)

Hangt een wiki-functie of -dienst onder een GEMMA-functie zonder beoordeling, dan noemt `gemma_functie` die functie: `id` (zoek met `uv run python tools/gemma.py functie <naam>`, de hele hiërarchie met `uv run python tools/gemma.py functies`) en

- bij een gematchte functie of dienst `gemma_relatie`: het id van de aggregatie van die GEMMA-functie naar de GEMMA-match van het element;
- anders `bronnen` en `vindplaats`, zoals de UPL met het UPL-nummer bij een dienst.

Het script toetst dat de functie bestaat, dat de relatie in het model staat tussen die functie en de match, en dat geen wiki-element met dezelfde GEMMA-match het element al aggregeert (één plek). Is de bovenliggende functie zelf een element van de wiki, dan is de plek een aggregatie in haar beoordeling en geen `gemma_functie`.
