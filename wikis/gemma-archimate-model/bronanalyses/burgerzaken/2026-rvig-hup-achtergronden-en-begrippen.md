---
id: 2026-rvig-hup-achtergronden-en-begrippen
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-achtergronden-en-begrippen
relevant: ja
korte_titel: HUP BRP Achtergronden en begrippen
bijgewerkt: 2026-10-06
---

# HUP BRP: Achtergronden en Begrippen

Bron: [tekst](../../../../sources/raw/2026-rvig-hup-achtergronden-en-begrippen.md) · [origineel (html)](../../../../sources/raw/2026-rvig-hup-achtergronden-en-begrippen.html) · [online](https://www.rvig.nl/hup/achtergronden-en-begrippen)

## Samenvatting

Achtergrondpagina van de HUP die de begrippen van de BRP in gewone taal uitlegt. Ze beschrijft de overgang van het GBA-stelsel naar het BRP-stelsel en wie waarvoor verantwoordelijk is: het college van burgemeester en wethouders van de gemeente waar een ingezetene zijn adres heeft is verantwoordelijk voor de bijhouding van de gegevens over die ingezetene; de minister van BZK voor die van niet-ingezetenen (met een uitzondering voor feiten uit de tijd dat de persoon nog ingezetene was, dan de laatste bijhoudingsgemeente); RvIG beheert namens de minister de BRP-V en de RNI. Bijhouden omvat het inschrijven van personen en het actualiseren, corrigeren en verwijderen van gegevens; verstrekken (aan overheidsorganen, derden of de ingeschrevene) staat buiten de handleiding. De pagina onderscheidt eerste inschrijving en vervolginschrijving (oude termen die niet meer in de Wet BRP staan), de persoonslijst als administratieve levensloop met historie, en de opbouw in categorieën, groepen, elementen en stapels. Rubrieken, soorten gegevens en toelichting op afzonderlijke gegevens (adellijke titel, voorvoegsel, land en plaats) zijn gegevensbeschrijving op rubriekniveau en vallen buiten de afbakening. De gemeentelijke term voor de gegevensverstrekking is afnemer.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| persoonslijst | verzameling van persoonsgegevens over een bepaald persoon; moet de administratieve levensloop van een persoon weergeven; van elke persoon mag maar één persoonslijst aanwezig zijn | PL, persoonskaart (voorganger) | regel 77, 87 |
| ingezetene | persoon van wie het college van de gemeente waar hij zijn adres heeft verantwoordelijk is voor de bijhouding | — | regel 38 |
| niet-ingezetene | persoon die eerder als ingezetene was ingeschreven en van wie het vertrek uit Nederland is geregistreerd, of die als zodanig is ingeschreven door de minister van BZK | — | regel 38 |
| registratie niet-ingezetenen (RNI) | het systeem waarmee de registratie van niet-ingezetenen wordt gevoerd; inschrijving kan op verzoek van de persoon bij een RNI-loket of op voordracht van een aangewezen bestuursorgaan | RNI-loket, inschrijfvoorziening | regel 38 |
| eerste inschrijving | het voor het eerst aanleggen van een persoonslijst van een persoon die nog niet was ingeschreven in de BRP | inschrijving | regel 77 |
| vervolginschrijving | inschrijving bij intergemeentelijke adreswijziging of (her)vestiging: de PL wordt opgehaald bij de vorige gemeente of de RNI | verhuizing naar andere gemeente, (her)vestiging | regel 77 |
| verwijsgegevens | gegevens in de voorziening van de vorige gemeente of de RNI die verwijzen naar de bijhoudingsgemeente; niet genoemd in de Wet BRP | verwijzing | regel 171 |
| brondocument | document waaraan de gegevens van de persoonslijst worden ontleend, zoals een geboorteakte of een rechterlijke uitspraak | akte, document | regel 87 |
| afnemer | overheidsorgaan, en soms een derde, aan wie systematisch gegevens worden verstrekt uit de BRP-V | overheidsorgaan, derde | regel 54 |
| BRP-Verstrekkingsvoorziening (BRP-V) | centrale voorziening waaruit de minister van BZK gegevens verstrekt | BRP-V | regel 54 |
| administratieve levensloop | de persoonslijst geeft aan wanneer gegevens zijn opgenomen, vanaf wanneer ze geldig zijn en laat geen gaten zien | historie | regel 87 |
| categorie 14 afnemersindicatie | in het LO nog onderdeel van de persoonslijst, in de praktijk bij de PL in BRP-V gevoegd | afnemersindicatie | regel 114 |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| college van burgemeester en wethouders | is verantwoordelijk voor de bijhouding van | gegevens over een ingezetene in de gemeentelijke voorziening | regel 38 |
| minister van BZK | is verantwoordelijk voor de bijhouding van | gegevens over alle niet-ingezetenen | regel 38 |
| laatste bijhoudingsgemeente | is verantwoordelijk voor het verwerken van | rechtsfeiten die plaatsvonden vóór de emigratie | regel 38 |
| RvIG | beheert namens de minister van BZK | BRP-V en RNI | regel 50 |
| RvIG | ondersteunt gemeenten bij | uitvoering van de Wet BRP (met de HUP en een Frontoffice) | regel 50 |
| minister van BZK | verstrekt | gegevens uit de BRP-V aan afnemers | regel 54 |
| gemeenten | leveren aan | gegevens in de BRP-V (synchronisatieberichten) | regel 54 |
| aangewezen bestuursorgaan | draagt voor | persoon voor inschrijving als niet-ingezetene | regel 38 |
| persoon | verzoekt om | inschrijving als niet-ingezetene bij een RNI-loket | regel 32 |
| vorige gemeente of RNI | neemt op | verwijsgegevens | regel 77 |
| vorige gemeente of RNI | verwijdert | persoonslijst | regel 77 |
| nieuwe bijhoudingsgemeente | neemt op | persoonslijst in de gemeentelijke voorziening | regel 77 |

## Relevantie voor de architectuur

- **Bedrijfsobjecten (kandidaten):** persoonslijst, verwijzing (verwijsgegevens), brondocument; de opbouw in categorieën, groepen en elementen is gegevensbeschrijving en geen element.
- **Rollen/partijen:** college van burgemeester en wethouders als bijhouder van ingezetenen, minister van BZK als bijhouder van niet-ingezetenen, RvIG als beheerder van BRP-V en RNI, afnemer.
- **Gebeurtenissen (kandidaten):** eerste inschrijving, vervolginschrijving (intergemeentelijke adreswijziging, (her)vestiging).
- **Buiten de afbakening:** rubrieken, stapels, soorten gegevens, toelichting op adellijke titel, voorvoegsel, land en plaats.

## Citaten

> Een inschrijving is het voor het eerst aanleggen van een persoonslijst van een persoon die nog niet was ingeschreven in de BRP. (De inschrijving in de gemeentelijke voorziening)

> Het college van burgemeester en wethouders van de gemeente waar een ingezetene zijn adres heeft, is verantwoordelijk voor de bijhouding van de gegevens over die ingezetene in de gemeentelijke voorziening. (BRP stelsel)

> Een persoonslijst is een verzameling van persoonsgegevens over een bepaald persoon. (Administratieve levensloop)

> RvIG beheert namens de minister van BZK de BRP-V en de RNI. (Rijksdienst voor Identiteitsgegevens)

> Verwijsgegevens zijn niet genoemd in de Wet BRP, maar komen wel voor in de gemeentelijke voorzieningen en in de RNI. (Verwijsgegevens)
