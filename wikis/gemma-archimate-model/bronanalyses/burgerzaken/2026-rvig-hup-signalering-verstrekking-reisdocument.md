---
id: 2026-rvig-hup-signalering-verstrekking-reisdocument
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-signalering-verstrekking-reisdocument
relevant: ja
korte_titel: HUP Signalering verstrekking reisdocument
bijgewerkt: 2026-10-06
---

# Signalering verstrekking reisdocument (HUP, RvIG)

Bron: [tekst](../../../../sources/raw/2026-rvig-hup-signalering-verstrekking-reisdocument.md) · [origineel (html)](../../../../sources/raw/2026-rvig-hup-signalering-verstrekking-reisdocument.html) · [online](https://www.rvig.nl/hup/signalering-verstrekking-reisdocument)

## Samenvatting

Procedure voor het opnemen en beëindigen van een signalering in categorie 12 bij een ingezetene van wie de gegevens in het Register paspoortsignaleringen (RPS) staan. Een mutatie in het RPS gaat via een Vb01-bericht naar de bijhoudingsgemeente, die de signalering verwerkt; maandelijks (of bij een nieuwe signalering op grond van artikel 23 of 23b van de Paspoortwet) komt de totaallijst in de Kwaliteitsmonitor, die bij elke aangifte van verblijf en adres moet worden gecontroleerd. Bij beëindiging verwijdert de gemeente de categorie. Voor het model is dit alleen de aanduiding dat het RPS bestaat en dat de gemeente de signalering vastlegt; de berichtenstappen en rubrieken zijn registratiedetail.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| signalering | aanduiding in categorie 12 bij een ingezetene van wie de gegevens in het Register paspoortsignaleringen staan | signalering Nederlands reisdocument | inleiding |
| Register paspoortsignaleringen | register met personen ten aanzien van wie gronden tot weigering of vervallenverklaring bestaan | RPS | inleiding |
| signaleringslijst | totaallijst van signaleringen, maandelijks in de Kwaliteitsmonitor opgenomen | totaallijst | sectie Melding van een signalering |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| bijhoudingsgemeente | verwerkt | de signalering aan de hand van een Vb01-bericht | sectie Melding van een signalering |
| RvIG | verstrekt | de ingangsdatum van de signalering in het Vb01-bericht en in de totaallijst | sectie Melding van een signalering |
| gemeente | controleert | de signaleringslijst bij elke aangifte van verblijf en adres | sectie Melding van een signalering |
| gemeente | verwijdert | de categorie met de signalering als die niet langer van toepassing is | sectie Beëindiging van de signalering |

## Relevantie voor de architectuur

- **Bedrijfsobject:** Register paspoortsignaleringen (zelfde object als in de Paspoortwet art. 25 en het Paspoortbesluit art. 1.1).
- **Verband:** de gemeente controleert de signalering bij de aangifte van verblijf en adres, een verband tussen reisdocumenten en de verblijfplaats.

## Citaten

> Bij elke ingezetene van wie de gegevens zijn opgenomen in het Register paspoortsignaleringen (RPS), moet in categorie 12 van de persoonslijst een signalering worden opgenomen. (vindplaats: inleiding)
