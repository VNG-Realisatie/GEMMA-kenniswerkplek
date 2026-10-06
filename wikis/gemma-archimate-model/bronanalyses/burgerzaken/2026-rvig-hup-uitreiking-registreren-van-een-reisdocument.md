---
id: 2026-rvig-hup-uitreiking-registreren-van-een-reisdocument
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-uitreiking-registreren-van-een-reisdocument
relevant: ja
korte_titel: HUP Uitreiking reisdocument
bijgewerkt: 2026-10-06
---

# Uitreiking of registreren van een reisdocument (HUP, RvIG)

Bron: [tekst](../../../../sources/raw/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md) · [origineel (html)](../../../../sources/raw/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.html) · [online](https://www.rvig.nl/hup/uitreiking-registreren-van-een-reisdocument)

## Samenvatting

Procedure waarin de bijhoudingsgemeente de uitreiking van een Nederlands reisdocument in de BRP registreert (categorie 12). De procedure geldt ook wanneer een reisdocument wordt getoond dat nog niet op de persoonslijst staat en bij verwerking van een kennisgeving. Alle reisdocumenten worden opgenomen als de verstrekking niet langer dan zestien jaar geleden is (elf jaar bij een geldigheidsduur van vijf jaar of korter). Een nooddocument, laissez-passer, diplomatiek paspoort, dienstpaspoort en buitenlands reisdocument worden niet opgenomen. De pagina onderscheidt vier uitgevers: een Nederlandse gemeente, de Minister van Buitenlandse Zaken buiten het Koninkrijk, de gezaghebber van Bonaire, Saba of Sint Eustatius en de Gouverneur van Aruba, Curaçao of Sint Maarten. Het is registratiedetail (documentnummer, autoriteit van afgifte, paspoortdossier) en valt grotendeels buiten de afbakening. Voor het model blijft over: het paspoortdossier als bewaarplaats van de aanvraagstukken bij de verstrekkende gemeente, en het reisdocumentnummer met de letter die het soort document aangeeft.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| uitreiking van een reisdocument | registratie in de BRP met een eigen stapel categorie 12 Reisdocument; categorie 12 kent geen historie | uitreiking, verstrekking (de pagina gebruikt verstrekt en uitgegeven voor hetzelfde) | sectie Uitreiking door een Nederlandse gemeente |
| paspoortdossier | dossier van de gemeente die het verstrekte reisdocument beheert, met de aanvullende reisdocumentgegevens, bijvoorbeeld het aanvraagformulier | gemeente waar het paspoortdossier zich bevindt | sectie Document |
| soort reisdocument | de eerste letter van het documentnummer: N nationaal paspoort, I Nederlandse identiteitskaart, B zakenpaspoort, A vreemdelingenpaspoort, R vluchtelingenpaspoort, D diplomatiek paspoort, S dienstpaspoort | zakenpaspoort, vreemdelingenpaspoort, vluchtelingenpaspoort (gemeentelijke namen) | sectie Nummer Nederlands reisdocument |
| Reisdocumentenmodule | module waarin de bijhoudingsgemeente de gegevens van een door een andere gemeente uitgegeven reisdocument raadpleegt | RDM | sectie Document |
| Basisregister Reisdocumenten | register waarin het documentnummer kan worden gecontroleerd | BR | sectie Nummer Nederlands reisdocument |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| bijhoudingsgemeente | neemt op | categorie 12 Reisdocument voor een reisdocument dat is uitgegeven door een Nederlandse gemeente | sectie Uitreiking door een Nederlandse gemeente |
| gemeente | beheert | het dossier van het verstrekte reisdocument (paspoortdossier) | sectie Document |
| Minister van Buitenlandse Zaken | verstrekt | reisdocumenten buiten het Koninkrijk (autoriteit van afgifte BU0518 vanaf 2014-03-09) | sectie Autoriteit van afgifte |
| gezaghebber van Bonaire, Saba of Sint Eustatius | verstrekt | reisdocumenten in het Caribisch deel van Nederland | sectie Uitreiking door de Gezaghebber |
| Gouverneur van Aruba, Curaçao of Sint Maarten | verstrekt | reisdocumenten | sectie Uitreiking door de Gouverneur |
| bijhoudingsgemeente | leest uit (bij aangifte van verblijf en adres) | de chip van een Nederlands reisdocument dat in het buitenland, in het Caribisch deel van Nederland of bij een grensgemeente is verstrekt | inleiding |

## Relevantie voor de architectuur

- **Gebeurtenis:** uitreiking van een reisdocument en de registratie ervan in de BRP; de registratiestappen zelf blijven buiten het model.
- **Bedrijfsobject:** paspoortdossier (bij de verstrekkende gemeente) en de soorten reisdocument volgens de letter van het documentnummer; de gemeentelijke namen zakenpaspoort, vreemdelingenpaspoort en vluchtelingenpaspoort komen hier terug.
- **Rollen:** uitgevende autoriteiten (gemeente, Buitenlandse Zaken, gezaghebber, Gouverneur).

## Citaten

> De gegevens over een nooddocument, een laissez-passer, een diplomatiek paspoort, een dienstpaspoort of een buitenlands reisdocument worden niet opgenomen op de persoonslijst. (vindplaats: inleiding)

> Het uitreiken van een reisdocument wordt met behulp van deze procedure uitgevoerd. (vindplaats: inleiding)
