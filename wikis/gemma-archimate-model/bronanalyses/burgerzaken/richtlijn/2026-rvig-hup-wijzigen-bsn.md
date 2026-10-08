---
id: 2026-rvig-hup-wijzigen-bsn
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-wijzigen-bsn
relevant: ja
bijgewerkt: 2026-10-06
---

# HUP BRP: Wijzigen BSN

Bron: [tekst](../../../../../sources/raw/2026-rvig-hup-wijzigen-bsn.md) · [origineel (html)](../../../../../sources/raw/2026-rvig-hup-wijzigen-bsn.html) · [online](https://www.rvig.nl/hup/wijzigen-bsn)

## Samenvatting

Procedure voor het wijzigen van het burgerservicenummer (BSN), bijvoorbeeld om bij een dubbelinschrijving één juiste persoonslijst over te houden. Het college van burgemeester en wethouders van de bijhoudingsgemeente besluit; dit gebeurt altijd als actualisering. De pagina noemt het Foutenmeldpunt BSN (FMP), de af te wegen belangen van de persoon (toeslagen, pensioenfonds), het van rechtswege vervallen van het reisdocument en de gevolgen voor gerelateerden. Voor het model: het BSN als bedrijfsobject en het besluit van het college.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| burgerservicenummer | identificatienummer dat het college bij de inschrijving als ingezetene toekent | BSN | regel 19 |
| wijzigen van het BSN | besluit van het college, bijvoorbeeld bij dubbelinschrijving; belang van de persoon wordt afgewogen en de persoon wordt geïnformeerd | besluit wijziging BSN | regel 19-25 |
| Foutenmeldpunt BSN (FMP) | voorziening waarmee gebruikers van de Beheervoorziening BSN foutvermoedens melden, zoals één persoon met twee BSN's | FMP | regel 23 |
| dubbelinschrijving | een persoon met twee persoonslijsten | — | regel 19, 23 |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| college van burgemeester en wethouders | kent toe | burgerservicenummer | regel 19 |
| college van burgemeester en wethouders | wijzigt | BSN bij een dubbelinschrijving | regel 19, 25 |
| college | meldt | foutvermoedens aan het FMP | regel 23 |
| FMP | zet door naar | bronhouder (gemeente of RNI) | regel 23 |
| college | betrekt | belang van de persoon bij het besluit over het BSN | regel 25 |

## Relevantie voor de architectuur

- Gebeurtenis BSN wijzigen met een eigen besluit van het college; bedrijfsobject BSN; partijen FMP en Beheervoorziening BSN. Raakvlak met Dubbelinschrijving (aparte bronanalyse).

## Citaten

> Het college van burgemeester en wethouders van de bijhoudingsgemeente kent een Burgerservicenummer (BSN) toe bij de inschrijving als ingezetene in de BRP van een persoon. (regel 19)
