---
id: beleidskader-modelleerafspraken
type: kennismodel
titel: Beleidskader — modelleerafspraken
---

# Beleidskader — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Driver* in ArchiMate · laag Motivatie · paginatype `beleidskader`

| Afspraak | Inhoud |
|---|---|
| Definitie | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden. (NORA) |
| In Over GEMMA | ja (Beleidskader) |
| Duiding | Een concreet benoemde regeling of richtlijn als geheel die voor alle gemeenten geldt: Europese regelgeving, rijksregelgeving, een landelijke richtlijn of een VNG-model van gemeentelijke regelgeving. |
| Herken je aan | *regeling als geheel* en *landelijk*. Moet ja: *is grondslag voor* (kernrelatie); hoogstens 1 nee: *in werking*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Beleidskader ─associatie (gericht)→ Product; Beleidskader ─associatie (gericht)→ Dienst; Beleidskader ─associatie (gericht)→ Bedrijfsproces |
| Eigenschappen | `regelgever` (verplicht): EU, rijk, landelijke organisatie of VNG-model: bepaalt de groep in de Grondslagindeling (EU, rijk, landelijke organisatie, VNG-model) · `taakveld`: het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling · `beleidsdomein`: het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling · `gemma`: de match met het GEMMA-model: het id gaat mee in de export |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md); [Grondslagindeling](../indelingen.md) |
| Naamvorm | de officiële citeertitel (Wet op de lijkbezorging); de afkorting wordt een synoniem |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; de motivatielaag van het GEMMA-model bevat nog vooral kernwaarden |
| Voorbeeld | wel: Wet op de lijkbezorging; Archiefwet; AVG; Circulaire adresonderzoek BRP; Model-beheersverordening begraafplaatsen · niet: beheersverordening van één gemeente (blijft bron); artikel 16 (losse norm, buiten het model); 'verordening' als soort (bedrijfsobject Regeling) |

## Afspraken

- Een regeling of beleid van één gemeente blijft bron en wordt geen element; het VNG-model staat in het model als gemeenschappelijke vorm.
- Een beleidskader in de groep Richtlijn is geen wettelijke grondslag: zijn relatie heet *geeft richtlijn voor*. Een beleidskader in Gemeentelijke regelgeving is alleen grondslag voor een UPL-product of -dienst zonder landelijke grondslag, en werkt voor de rest de wet uit (*werkt uit voor*).
- De relaties naar een ander beleidskader (*werkt uit*, *verwijst naar*) en naar een rol, gebeurtenis of bedrijfsobject zijn een uitbreiding op het GEMMA-kennismodel, dat een beleidskader alleen aan een product en een kwaliteitsdoel koppelt.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| uit | associatie (gericht) | [Product](../bedrijfsarchitectuur/product-modelleerafspraken.md) | is grondslag voor, werkt uit voor, geeft richtlijn voor | *is grondslag voor* | ja | de grondslag; bij voorkeur naar een product |
| uit | associatie (gericht) | [Dienst](../bedrijfsarchitectuur/dienst-modelleerafspraken.md) | is grondslag voor, werkt uit voor, geeft richtlijn voor | *is grondslag voor* | nee: uitbreiding op het GEMMA-kennismodel | de grondslag; bij voorkeur naar een product |
| uit | associatie (gericht) | [Bedrijfsproces](../bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) | is grondslag voor, werkt uit voor, geeft richtlijn voor | *is grondslag voor* | nee: uitbreiding op het GEMMA-kennismodel | de grondslag; bij voorkeur naar een product |
| uit | associatie (gericht) | [Beleidskader](beleidskader-modelleerafspraken.md) | werkt uit, verwijst naar |  | nee: uitbreiding op het GEMMA-kennismodel | een AMvB of VNG-model werkt een wet uit |
| uit | associatie (gericht) | [Rol](../bedrijfsarchitectuur/rol-modelleerafspraken.md) | is grondslag voor |  | nee: uitbreiding op het GEMMA-kennismodel | de regeling die de rol regelt |
| uit | associatie (gericht) | [Gebeurtenis](../bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md) | is grondslag voor |  | nee: uitbreiding op het GEMMA-kennismodel | de regeling die de gebeurtenis regelt |
| uit | associatie (gericht) | [Bedrijfsobject](../bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md) | is grondslag voor, is model voor |  | nee: uitbreiding op het GEMMA-kennismodel | de regeling die het object regelt; *is model voor*: een VNG-model voor de soort regeling (Regeling) |
