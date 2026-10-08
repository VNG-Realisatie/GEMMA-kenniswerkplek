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

De uitwerking van de regel Wettelijke grondslag (`AGENTS.md`). Het waarom en de gevallen A tot en met D staan in `docs/wettelijke-grondslag.md`.

- Het model geldt voor alle gemeenten; daarom heeft elk element een landelijke wettelijke bron, dat is een bron van brontype `europese-regelgeving` of `rijksregelgeving` (regel Bronvoorrang), genoemd met het artikel.
- Een relatie heeft geen eigen landelijke grondslag nodig: de structuur wordt uit de wet afgeleid, maar per relatie volstaat een bron (regel Elke claim een bron).
- Bronnen van `richtlijn`, `beleid` en `overig` dienen voor taal, voorbeelden, werkwijze en het vinden van lacunes, niet als onderbouwing; een grondslag uit de UPL geldt pas na controle in de wettekst.
- Eén uitzondering: een product of dienst uit de UPL blijft altijd, ook zonder landelijke wettelijke grondslag.
- Heeft het dan een grondslag in een bron van brontype `gemeentelijke-regelgeving` (een VNG-model, niet de verordening van één gemeente), dan wordt die genoemd; heeft het geen grondslag, of noemt de UPL een grondslag die geen taak geeft, dan volgt een procesarchitectuur-terugmelding.
- Zo'n product wordt niet uitgewerkt in processen, objecten, gebeurtenissen of rollen.
- Een element zonder landelijke wettelijke bron, en een product of dienst buiten de UPL zonder die bron, blijft niet.
- Staat de landelijke grondslag eenduidig in de nagelezen wettekst, dan voegt de AI de bron en de relatie *is grondslag voor* toe zonder voorleggen en noemt het geval in de samenvatting ter bevestiging; alleen bij twijfel voorleggen.
- Een bedrijfsfunctie heeft geen eigen wettelijke bron nodig: zij volgt de grondslag van de diensten en processen die zij omvat, en vervalt alleen als zij niets meer omvat.
- Een bedrijfsfunctie die alleen UPL-producten of -diensten zonder landelijke grondslag zou omvatten, bedient geen proces en vervalt in de wiki; die producten hangen onder de functie van hun beleidsdomein, met een GEMMA-terugmelding (`beoordelingen/terugmeldingen/gemma.yaml`).
- De grondslag staat als relatie *is grondslag voor* van een beleidskader; een beleidskader in *Gemeentelijke regelgeving* is alleen grondslag voor een UPL-product of -dienst zonder landelijke grondslag, en werkt voor de rest de wet uit (relatie *werkt uit voor*).
- Een beleidskader staat in de Regelgevingindeling onder het brontype van zijn regeling: in de groep en de map *Europese regelgeving*, *Rijksregelgeving*, *Richtlijn* of *Gemeentelijke regelgeving*.
- Een beleidskader in *Richtlijn* (een landelijke richtlijn als geheel) is geen wettelijke grondslag; zijn relatie heet *geeft richtlijn voor* (besluiten redacteur 2026-10-08; onderbouwing in `docs/wettelijke-grondslag.md`).

Controles: fout bij een relatie is grondslag voor vanuit een richtlijn, of vanuit gemeentelijke regelgeving naar iets anders dan een UPL-product zonder landelijke grondslag, en een bedrijfsproces dat een UPL-product zonder landelijke grondslag realiseert; signaal bij een element zonder landelijke wettelijke bron.
