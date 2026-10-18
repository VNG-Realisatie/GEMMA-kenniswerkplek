---
id: beleidskader-modelleerafspraken
type: kennismodel
titel: Beleidskader — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Beleidskader — modelleerafspraken

*Driver* in ArchiMate · laag Motivatie · vak `motivatie` · paginatype `beleidskader`

| Afspraak | Inhoud |
|---|---|
| Definitie | Beleidskader is gebaseerd op bestaand overheidsbeleid (Nationaal en Europees) en op de instrumenten die in het kader van dat beleid zijn ontwikkeld, zoals wetten, regelgeving, Kamerstukken en bestuursakkoorden. (NORA) |
| In Over GEMMA | ja (Beleidskader) |
| Duiding | Een concreet benoemde regeling als geheel die voor alle gemeenten geldt: Europese regelgeving, rijksregelgeving of een VNG-modelverordening van gemeentelijke regelgeving. |
| Herken je aan | *regeling als geheel* en *landelijk*. Toetskenmerken, alle ja: *is grondslag voor* †, *in werking*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Beleidskader ─associatie (gericht)→ Product; Beleidskader ─associatie (gericht)→ Dienst; Beleidskader ─associatie (gericht)→ Bedrijfsproces |
| Eigenschappen | `regelgever` (verplicht) · `taakveld` · `beleidsdomein` · `gemma` · `kwaliteitsdoelen` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md); [Grondslagindeling](../indelingen.md) |
| Naamvorm | de officiële citeertitel (Wet op de lijkbezorging); de afkorting wordt een synoniem |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; de motivatielaag van het GEMMA-model bevat nog vooral kernwaarden |
| Voorbeeld | wel: Wet op de lijkbezorging; Archiefwet; AVG; Model-beheersverordening begraafplaatsen · niet: beheersverordening van één gemeente (blijft bron); Circulaire adresonderzoek BRP (richtlijn, blijft bron); artikel 16 (losse norm, buiten het model); 'verordening' als soort (bedrijfsobject Regeling) |

## Afspraken

- Een regeling of beleid van één gemeente blijft bron en wordt geen element; de VNG-modelverordening staat in het model als gemeenschappelijke vorm.
- Een landelijke richtlijn (uitvoeringsvoorschrift, handleiding, circulaire of handreiking) wordt nooit een beleidskader, ook niet als geheel: zij blijft bron voor taal, werkwijze en het vinden van lacunes.
- Een VNG-modelverordening is nooit grondslag: zij werkt de wet uit (*werkt uit voor*), ook bij een UPL-dienst zonder landelijke grondslag.
- De relaties naar een ander beleidskader (*werkt uit*, *verwijst naar*) en naar een rol, gebeurtenis of bedrijfsobject zijn een uitbreiding op het GEMMA-kennismodel, dat een beleidskader alleen aan een product en een kwaliteitsdoel koppelt.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| associatie (gericht) | [Product](../bedrijfsarchitectuur/product-modelleerafspraken.md) | is grondslag voor, werkt uit voor | *is grondslag voor* | ja | de grondslag; bij voorkeur naar een product |
| associatie (gericht) | [Dienst](../bedrijfsarchitectuur/dienst-modelleerafspraken.md) | is grondslag voor, werkt uit voor | *is grondslag voor* | nee | de grondslag; bij voorkeur naar een product |
| associatie (gericht) | [Bedrijfsproces](../bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) | is grondslag voor, werkt uit voor | *is grondslag voor* | nee | de grondslag; bij voorkeur naar een product |
| associatie (gericht) | [Beleidskader](beleidskader-modelleerafspraken.md) | werkt uit, verwijst naar |  | nee | een AMvB of VNG-modelverordening werkt een wet uit |
| associatie (gericht) | [Rol](../bedrijfsarchitectuur/rol-modelleerafspraken.md) | is grondslag voor |  | nee | de regeling die de rol regelt |
| associatie (gericht) | [Gebeurtenis](../bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md) | is grondslag voor |  | nee | de regeling die de gebeurtenis regelt |
| associatie (gericht) | [Bedrijfsobject](../bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md) | is grondslag voor, is model voor |  | nee | de regeling die het object regelt; *is model voor*: een VNG-modelverordening voor de soort regeling (Regeling) |
| invloed | [Kwaliteitsdoel](kwaliteitsdoel-modelleerafspraken.md) | geeft grondslag aan |  | ja | met een sterkte; het kwaliteitsdoel is een element van GEMMA (veld `kwaliteitsdoelen`) |

Inkomend, bij het brontype: [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
