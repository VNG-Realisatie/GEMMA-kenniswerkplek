---
id: 2026-rvig-hup-geboorte
type: bronanalyse
onderwerp: burgerzaken
bronnen:
- 2026-rvig-hup-geboorte
relevant: ja
bijgewerkt: 2026-10-06
---

# HUP BRP: Geboorte

Bron: [tekst](../../../../../sources/raw/2026-rvig-hup-geboorte.md) · [origineel (html)](../../../../../sources/raw/2026-rvig-hup-geboorte.html) · [online](https://www.rvig.nl/hup/geboorte)

## Samenvatting

Deze HUP-pagina beschrijft hoe de bijhoudingsgemeente een pasgeboren kind inschrijft in de BRP op basis van een geboorteakte of een kennisgeving (Tb01) van de ambtenaar van de burgerlijke stand. Voor het model is het een bron voor de gebeurtenis geboorte, het bedrijfsobject geboorteakte en de rollen van moeder (uit wie het kind is geboren) en andere ouder; de categorieën, akteaanduidingen en voorbeelden zijn gegevensbeschrijving en blijven buiten het model.

Het uitgangspunt is dat een kind juridisch altijd een moeder heeft en hoogstens één andere ouder. Het kind wordt als ingezetene ingeschreven als de moeder op de geboortedatum als ingezetene staat ingeschreven; anders volgt inschrijving op aangifte van verblijf en adres (buitenland, vondeling). Bijzondere situaties met een eigen besluit of rechtsgevolg: een kind erkend voor of bij de aangifte, een kind levend geboren maar overleden voor de aangifte, ontkenning van het ouderschap voor de aangifte en het levenloos geboren kind, dat alleen op verzoek van de ouder wordt opgenomen (art. 2.56a Wet BRP; weigeren is een besluit in de zin van de Awb, art. 2.60). Binnen vier weken na inschrijving krijgen de ouders een overzicht van de persoonslijst. Buiten scope: persoonslijstopbouw, nationaliteitssituaties A tot en met F, hervestiging uit het Caribisch deel van het Koninkrijk.

## Kernbegrippen

| Begrip | Omschrijving in de bron | Andere termen in deze bron | Vindplaats |
|---|---|---|---|
| geboorteaangifte | aangifte van de geboorte, waarop een geboorteakte wordt opgemaakt; bij aangifte kan het kind tegelijk worden erkend of het ouderschap zijn ontkend | aangifte van geboorte | regel 2404-2640 |
| geboorteakte | akte van de burgerlijke stand waaruit de BRP het kind inschrijft; een geboorteakte kan latere vermeldingen krijgen (erkenning, ontkenning) | akte van geboorte; kennisgeving Tb01 | regel 50, 58 |
| ingezetene | persoon die in de BRP als ingezetene staat ingeschreven; bepaalt of het kind via de geboorteakte of via aangifte van verblijf en adres wordt ingeschreven | niet-ingezetene (RNI) | regel 50, 553 |
| moeder (uit wie het kind is geboren) | juridisch altijd aanwezig; Ouder1 | ouder 1 | regel 66-68 |
| andere ouder | de vader of moeder uit wie het kind niet is geboren; Ouder2; er kan juridisch ook geen andere ouder zijn | ouder 2 | regel 70-84 |
| familierechtelijke betrekking | betrekking tussen kind en ouder, ingaande op de geboortedatum van het kind | — | regel 86-88 |
| vondeling | kind van onbekende moeder; wordt ingeschreven op aangifte of ambtshalve door het college | — | regel 922 |
| kind geboren in het buitenland | 'toevallig' in het buitenland geboren kind dat in Nederland woont; inschrijving op aangifte van verblijf en adres | — | regel 1294 |
| erkenning als ongeboren vrucht | erkenning voor de geboorte; verwerkt op de geboorteakte bij de aangifte | erkenning bij de aangifte | regel 2404, 2626 |
| kind levend geboren, overleden voor de geboorteaangifte | krijgt een geboorte- en een overlijdensakte; eerst inschrijving, dan overlijden | levenloos aangegeven kind (oude akte) | regel 3237-3247 |
| levenloos geboren kind | kind waarvan de gegevens alleen op verzoek van de ouder in de BRP komen (art. 2.56a Wet BRP) | akte van geboorte (levenloos) | regel 4195-4205 |
| verzoek om registratie van een levenloos geboren kind | persoonlijk, schriftelijk verzoek van de ouder, binnen vier weken af te handelen; weigering is gelijkgesteld aan een besluit op grond van de Awb (art. 2.60 Wet BRP) | — | regel 4199-4211 |
| verzoek om verwijdering gegevens levenloos geboren kind | persoonlijk verzoek van de ouder; binnen vier weken af te handelen | — | regel 4430-4436 |
| overzicht persoonslijst | binnen vier weken na inschrijving naar de ouders, voogden of verzorgers, met mededeling over de AVG | — | regel 34-36 |

## Relaties

| Van | Werkwoord | Naar | Vindplaats |
|---|---|---|---|
| bijhoudingsgemeente | ontvangt | geboorteakte van de ambtenaar van de burgerlijke stand | regel 50 |
| bijhoudingsgemeente | schrijft in | kind als ingezetene | regel 50 |
| bijhoudingsgemeente | zendt toe | overzicht persoonslijst aan ouders, voogden of verzorgers | regel 36 |
| college van burgemeester en wethouders | schrijft in ambtshalve | vondeling | regel 924 |
| bijhoudingsgemeente | geeft binnen vier weken gevolg aan | verzoek om registratie van een levenloos geboren kind | regel 4199 |
| ouder | verzoekt om | gegevens over levenloos geboren kind | regel 4197 |
| ouder | verzoekt om verwijdering van | gegevens levenloos geboren kind | regel 4432 |
| RNI-loket | verwijdert (op verzoek van een niet-ingezetene) | gegevens levenloos geboren kind | regel 4436 |
| bijhoudingsgemeente | licht telefonisch in | RIVM (bij overlijden voor de aangifte) | regel 3249 |
| gemeente | neemt | beslissing om geen gevolg te geven aan het verzoek (gelijkgesteld aan een Awb-besluit) | regel 4201 |

## Relevantie voor de architectuur

- Gebeurtenis geboorte met de varianten in Nederland, in het buitenland, vondeling, levend geboren maar overleden voor de aangifte en levenloos geboren; bedrijfsobject geboorteakte (met latere vermeldingen) en geboorteaangifte.
- Besluit: weigeren om een levenloos geboren kind op te nemen is een Awb-besluit (art. 2.60 Wet BRP). Overige deelprocessen (inschrijving, nationaliteit, verblijfplaats) zijn registratiestappen en blijven buiten het model.
- Rollen: moeder (uit wie het kind is geboren), andere ouder, ouder; juridisch kent het kind geen vader- of moederrol, maar Ouder1 en Ouder2.
- Raakvlak met het product Geboorteaangifte doen van Utrecht (aparte bronanalyse) en met Lijkbezorging (kind overleden voor de aangifte: overlijden).
- Termverschil: de HUP zegt erkend 'als ongeboren vrucht'; de gemeentelijke praktijk zegt erkenning voor de geboorte.

## Citaten

> Op grond van artikel 2.56a, eerste lid, van de Wet BRP mag de ouder van een kind dat levenloos is geboren verzoeken om de gegevens over dat kind in de BRP te vermelden. (regel 4197)

> Er wordt in het Nederlands recht vanuit gegaan dat er juridisch gezien altijd een moeder (uit wie het kind is geboren) is. (regel 68)
