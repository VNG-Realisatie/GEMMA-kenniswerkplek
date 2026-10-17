---
id: data-object-modelleerafspraken
type: kennismodel
titel: Data-object — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Data-object — modelleerafspraken

*Data Object* in ArchiMate · laag Applicatiearchitectuur · paginatype `data-object`

| Afspraak | Inhoud |
|---|---|
| Definitie | Samenhangende set gegevens die geautomatiseerd kan worden verwerkt. (GEMMA) |
| In Over GEMMA | ja (Data-object) |
| Duiding | De schakel van een element naar het GGM. Geen beoordeling: het script leidt het af uit de GGM-match van het element, of sterkte geen met een terugmelding hiaat, en het volgt de status van het element. |
| Eigenschappen | `ggm` · `data_objecten` ([betekenis](../README.md#eigenschappen)) |
| Naamvorm | de naam van het element met -data (Graf-data) |
| Afstemming | GGM: de match van het element, of een extra in `data_objecten`; zwakker dan sterk voorleggen |
| Voorbeeld | wel: Graf-data (hiaat); Ingeschreven persoon-data · niet: Beleidsnota-data (geen match, geen hiaat) |

## Afspraken

- Registratie en haar wettelijke grondslag staan bij het element in de bedrijfslaag.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| realisatie | [Bedrijfsobject](../bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| realisatie | [Afspraak](../bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | vrij, uit de bron |  | nee |  |
| associatie | [Rol](../bedrijfsarchitectuur/rol-modelleerafspraken.md) | vrij, uit de bron |  | nee | ArchiMate: geen realisatie |
| associatie | [Actor](../bedrijfsarchitectuur/actor-modelleerafspraken.md) | vrij, uit de bron |  | nee | ArchiMate: geen realisatie |
| associatie | [Gebeurtenis](../bedrijfsarchitectuur/gebeurtenis-modelleerafspraken.md) | vrij, uit de bron |  | nee | ArchiMate: geen realisatie |
