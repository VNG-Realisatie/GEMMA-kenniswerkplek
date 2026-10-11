---
id: 2026-vng-gemma-bedrijfsfuncties
type: bronanalyse
onderwerp: kern
bronnen:
- 2026-vng-gemma-bedrijfsfuncties
relevant: ja
bijgewerkt: '2026-10-10'
---

# GEMMA Bedrijfsfuncties

Bron: [tekst](../../../../../sources/raw/2026-vng-gemma-bedrijfsfuncties.md) · [origineel (html)](../../../../../sources/raw/2026-vng-gemma-bedrijfsfuncties.html) · [online](https://www.gemmaonline.nl/wiki/Bedrijfsfuncties)

## Samenvatting

Alleen de redactionele tekst van deze pagina is bron: regel 20-24 en 344-348. De view BA02 Bedrijfsfunctiemodel (regel 26-342) en de tabel met naam en beschrijving per bedrijfsfunctie (regel 351-565) worden uit het GEMMA-model gegenereerd; dat model is matchdoel en geen bron (regel Bronvoorrang). Wat de view en de tabel zeggen, staat al in de GEMMA-match van een element.

De redactionele tekst zegt wat een bedrijfsfunctie in GEMMA is: een logische eenheid van activiteiten die zijn gegroepeerd omdat ze vergelijkbare bedrijfsmiddelen, kennis of competenties vragen, met eigen taken en verantwoordelijkheden, los van de uitvoering in bedrijfsprocessen, en stabiel omdat gemeenten op hoofdlijnen dezelfde activiteiten blijven uitvoeren (regel 20). Het model is per domein uitgewerkt in domeinarchitecturen (regel 24). Op hoofdlijnen betreft de functie Uitvoering het daadwerkelijk leveren van producten en diensten aan klanten (regel 346).

Voor de bedrijfsfuncties in de wiki onderbouwt deze tekst de algemene kenmerken *gedrag*, *gegroepeerd gedrag*, *eigen identiteit* en *stabiel over tijd*. De plek van een functie in de functieketen noemt de tekst niet; die steunt op de GEMMA-match (regel Elke claim een bron, `gemma_relatie`).

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| Bedrijfsfunctie | logische eenheid waarin activiteiten zijn gegroepeerd waarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn | functie | regel 20 |
| GEMMA bedrijfsfunctiemodel | toont de bedrijfsfuncties van gemeenten; stabiel en voor langere tijd bruikbaar referentiekader | bedrijfsfunctiemodel | regel 20-22 |
| Domeinarchitectuur | gedetailleerde uitwerking van het bedrijfsfunctiemodel per domein | — | regel 24 |
| Uitvoering | het daadwerkelijk leveren van producten en diensten aan klanten | — | regel 346 |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| bedrijfsfunctie | groepeert | activiteiten | regel 20 |
| bedrijfsfunctiemodel | is uitgewerkt in | domeinarchitecturen | regel 24 |

## Relevantie voor de architectuur

Onderbouwt dat elke GEMMA-bedrijfsfunctie gegroepeerd gedrag is, met een eigen identiteit en stabiel over tijd, los van de organisatie en de processen. De functieketen zelf (welke functie welke andere omvat) staat alleen in het model.

## Citaten

> Een bedrijfsfunctie is een logische eenheid waarin activiteiten zijn gegroepeerd waarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. Iedere functie kent bepaalde taken en verantwoordelijkheden. De bedrijfsfuncties beschrijven wat een gemeente doet, onafhankelijk van hoe de uitvoering via bedrijfsprocessen plaatsvindt. Omdat gemeenten op hoofdlijnen dezelfde activiteiten blijven uitvoeren vormen bedrijfsfuncties een stabiel en voor langere tijd bruikbaar referentiekader dat helpt bij het begrijpen, organiseren en beheren van de gemeentelijke bedrijfsvoering en daarbij behorende informatievoorziening. (regel 20)

> Het model is meer in detail uitgewerkt in een zestal domeinarchitecturen. (regel 24)

> Uitvoering betreft het daadwerkelijk leveren van producten en diensten aan klanten. (regel 346)
