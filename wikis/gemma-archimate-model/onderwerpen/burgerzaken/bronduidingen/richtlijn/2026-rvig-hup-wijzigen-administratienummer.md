---
id: 2026-rvig-hup-wijzigen-administratienummer
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-wijzigen-administratienummer
relevant: ja
bijgewerkt: 2026-10-06
---

# HUP BRP: Wijzigen administratienummer

Bron: [tekst](../../../../../sources/raw/2026-rvig-hup-wijzigen-administratienummer.md) · [origineel (html)](../../../../../sources/raw/2026-rvig-hup-wijzigen-administratienummer.html) · [online](https://www.rvig.nl/hup/wijzigen-administratienummer)

## Samenvatting

Procedure voor het wijzigen van het administratienummer (A-nummer), bijvoorbeeld als verschillende personen hetzelfde A-nummer hebben; bij dubbelinschrijving wordt het A-nummer niet gewijzigd. De gemeente onderzoekt de oorzaak, kent nieuwe A-nummers toe aan alle betrokken personen, actualiseert de persoonslijst (nooit een correctie) en stuurt Wa01-berichten naar vorige bijhoudingsgemeenten, de geboortegemeente en de RNI en een Lg01-bericht naar BRP-V. Gerelateerden worden ook geactualiseerd. Voor het model: het bedrijfsobject administratienummer en de rol van de gemeente, RNI en BRP-V; de berichtenstappen zijn registratie.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| administratienummer | identificatienummer van een persoon | A-nummer | regel 19 |
| wijzigen van het A-nummer | de gemeente kent nieuwe A-nummers toe aan alle personen met hetzelfde nummer | — | regel 19-21 |
| dubbelinschrijving | een persoon met meerdere persoonslijsten; geen aanleiding voor wijziging van het A-nummer | — | regel 19 |
| Wa01-bericht | melding aan vorige bijhoudingsgemeenten, geboortegemeente en RNI over de wijziging | — | regel 21, 45 |
| BRP-V | voorziening die de wijziging meldt aan afnemers (Wa11) | — | regel 21 |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| gemeente | onderzoekt | oorzaak (meerdere personen met hetzelfde A-nummer) | regel 19 |
| gemeente | kent toe | nieuwe A-nummers aan alle betrokken personen | regel 21 |
| gemeente | stuurt | Wa01-berichten naar vorige bijhoudingsgemeenten, geboortegemeente en RNI | regel 21 |
| gemeente | stuurt | Lg01-bericht naar de BRP-V | regel 21 |
| BRP-V | meldt de wijziging aan | afnemers (Wa11) | regel 21 |

## Relevantie voor de architectuur

- Gebeurtenis wijziging administratienummer met een eigen besluit van de gemeente; partijen RNI, BRP-V en afnemers.
- Alleen het bedrijfsobject administratienummer en de rol van de gemeente zijn voor het model relevant.

## Citaten

Geen.
