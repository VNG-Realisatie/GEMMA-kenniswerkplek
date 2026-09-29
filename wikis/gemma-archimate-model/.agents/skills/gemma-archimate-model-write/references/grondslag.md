# Grondslag

Waarop het element steunt. Bepaal in deze volgorde:

| Stap | Vraag | Grondslag |
|---|---|---|
| 1 | Is er een directe GGM-entiteit? | `ggm-entiteit` |
| 2 | Geen entiteit, wel af te leiden uit GGM-objecten (berekening, aggregatie)? | `ggm-afgeleid` |
| 3 | Geen GGM-basis; een artefact dat in een gemeentelijk proces ontstaat? | `procesobject` |
| 4 | Geen GGM-basis; een juridisch of beleidsmatig kader (wet, verordening, regeling)? | `governance-object` |
| 5 | Geen GGM-basis en geen van beide (actor, rol, proces, dienst, gebeurtenis uit bronnen)? | `bron` |

Het GGM modelleert vooral gegevens. Processen, functies, diensten, gebeurtenissen en regelingen zijn er doorgaans niet compleet in gedekt (uitzonderingen bestaan, bijv. GGM-beleidsdomein Normafwijking met Maatregel en Boete). Het ontbreken van een GGM-grondslag is daar normaal en geen hiaat.

Body-sectie per grondslag:
- `ggm-entiteit` → `## GGM-bron`
- `ggm-afgeleid` → `## Afleiding`: welke GGM-objecten, welke berekening of aggregatie
- `procesobject` → `## Procesbron`: uit welk proces, met link naar de bronanalyse
- `governance-object` → `## Juridische bron`: welke wet of verordening, met link naar de bronanalyse. Een `governance-object` wordt altijd voorgelegd (status `kandidaat`).
- `bron` → de bronnen in `## Bronnen` volstaan
