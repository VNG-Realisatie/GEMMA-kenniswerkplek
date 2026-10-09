# Grondslag

Waarop het element steunt (`grondslag`). Bepaal in deze volgorde:

| Stap | Vraag | Grondslag |
|---|---|---|
| 1 | Is er een directe GGM-entiteit? | `ggm-entiteit` |
| 2 | Geen entiteit, wel af te leiden uit GGM-objecten (berekening, aggregatie)? | `ggm-afgeleid` |
| 3 | Geen GGM-basis; een artefact dat in een gemeentelijk proces ontstaat? | `procesobject` |
| 4 | Geen GGM-basis; zelf een juridisch of beleidsmatig kader (wet, verordening, regeling)? | `regelgeving` |
| 5 | Geen GGM-basis en geen van beide (actor, rol, proces, dienst, gebeurtenis uit bronnen)? | `bron` |

Het GGM modelleert vooral gegevens. Processen, functies, diensten, gebeurtenissen en regelingen zijn er doorgaans niet compleet in gedekt (uitzonderingen bestaan, bijv. GGM-beleidsdomein Normafwijking met Maatregel en Boete). Het ontbreken van een GGM-grondslag is daar normaal en geen hiaat.

`grondslag_toelichting` (alinea's) is verplicht bij:
- `ggm-afgeleid`: welke GGM-objecten, welke berekening of aggregatie;
- `procesobject`: uit welk proces, met de bron;
- `regelgeving`: welke wet of verordening, met de bron.

Een element met grondslag `regelgeving` wordt altijd voorgelegd: de grens tussen een kader (beleidskader, motivatielaag) en een object waar de gemeente mee werkt, is niet hard te trekken. Een concreet benoemde landelijke wet of VNG-modelverordening als geheel is een beleidskader (eigen type); de soort regeling is het bedrijfsobject Regeling; een verordening van één gemeente blijft een bron.

## Wettelijke grondslag

De regel Wettelijke grondslag, met haar uitwerking, staat in `kennismodel/modelleerregels.md`.
