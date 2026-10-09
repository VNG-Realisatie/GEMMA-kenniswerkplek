---
id: data-object-modelleerafspraken
type: kennismodel
titel: Data-object — modelleerafspraken
---

# Data-object — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Data Object* in ArchiMate · laag Applicatiearchitectuur · geen pagina (annotatie)

| Afspraak | Inhoud |
|---|---|
| Definitie | Samenhangende set gegevens die geautomatiseerd kan worden verwerkt. (GEMMA) |
| In Over GEMMA | ja (Data-object) |
| Duiding | Nu een annotatie (`data_object: ja`) bij een begrip dat *geautomatiseerd verwerkt* wordt; voorbereiding op de applicatielaag. In GEMMA realiseert een data-object een bedrijfsobject. |
| Eigenschappen | `data_object`: annotatie: het begrip wordt als gegevensstructuur geautomatiseerd verwerkt · `ggm`: de match met het GGM: entiteit, sterkte en onderbouwing |
| Naamvorm | als het bedrijfsobject dat het realiseert |
| Afstemming | GGM: matchdoel: een gegevensobject zonder sterke GGM-match wordt voorgelegd |
| Voorbeeld | wel: zaak in het zaaksysteem · niet: keukentafelgesprek |

## Afspraken

- Gegevensvastlegging bepaalt nooit of iets een element is; *geautomatiseerd verwerkt* is alleen een annotatie.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| uit | realisatie | [Bedrijfsobject](../bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md) | vrij, uit de bron |  | ja | nu een annotatie |
