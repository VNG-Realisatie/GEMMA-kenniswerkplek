---
id: data-object-modelleerafspraken
type: kennismodel
titel: Data-object — modelleerafspraken
---

# Data-object — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Data Object* in ArchiMate · laag Applicatiearchitectuur · paginatype `data-object`

| Afspraak | Inhoud |
|---|---|
| Definitie | Samenhangende set gegevens die geautomatiseerd kan worden verwerkt. (GEMMA) |
| In Over GEMMA | ja (Data-object) |
| Duiding | De schakel van een element naar het GGM. Geen beoordeling: het script leidt het af uit de GGM-match van het element, of sterkte geen met een terugmelding hiaat, en het volgt de status van het element. |
| Eigenschappen | `ggm`: de match met het GGM: entiteit, sterkte en onderbouwing · `data_objecten`: een extra data-object voor een andere GGM-entiteit: naam en GGM-match |
| Naamvorm | de naam van het element met -data (Graf-data) |
| Afstemming | GGM: de match van het element, of een extra in `data_objecten`; zwakker dan sterk voorleggen |
| Voorbeeld | wel: Graf-data (hiaat); Ingeschreven persoon-data · niet: Beleidsnota-data (geen match, geen hiaat) |

## Afspraken

- Registratie en haar wettelijke grondslag staan bij het element in de bedrijfslaag.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| uit | realisatie | [Bedrijfsobject](../bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| uit | realisatie | [Afspraak](../bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | associatie | [Rol](../bedrijfsarchitectuur/rol-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel | ArchiMate: geen realisatie |
| uit | associatie | [Actor](../bedrijfsarchitectuur/actor-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel | ArchiMate: geen realisatie |
| uit | associatie | [Gebeurtenis](../bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel | ArchiMate: geen realisatie |
