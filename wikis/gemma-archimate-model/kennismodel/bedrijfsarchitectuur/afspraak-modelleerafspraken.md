---
id: afspraak-modelleerafspraken
type: kennismodel
titel: Afspraak — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Afspraak — modelleerafspraken

*Contract* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/passief` · paginatype `bedrijfsobject`

| Afspraak | Inhoud |
|---|---|
| Definitie | Overeenkomst tussen meerdere partijen betreffende een bepaald onderwerp. (GEMMA) |
| In Over GEMMA | ja (Afspraak) |
| Duiding | Een afspraak tussen partijen (overeenkomst, convenant). Een besluit of verordening is géén afspraak. Een afspraak is een bijzonder bedrijfsobject en heeft dezelfde pagina en indeling. |
| Herken je aan | *afspraak*. Moet ja: *wordt bewerkt* (kernrelatie); hoogstens 1 nee: *onderscheidbare exemplaren*, *levenscyclus*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsproces ─toegang→ Afspraak |
| Niveaus | als bij een bedrijfsobject: kernobject, subobject of generiek |
| Eigenschappen | `taakveld` · `beleidsdomein` · `ggm` · `gemma` · `data_objecten` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md) |
| Naamvorm | de gangbare term uit beleid en praktijk, zoals bij een bedrijfsobject |
| Afstemming | GGM: als bij een bedrijfsobject · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: Uitvoeringsovereenkomst; Grafrecht · niet: subsidiebeschikking (eenzijdig besluit); verordening |

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| associatie (gericht) | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | vrij, uit de bron |  | nee |  |

Inkomend, bij het brontype: [Rol](rol-modelleerafspraken.md) (toegang); [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) (toegang); [Product](product-modelleerafspraken.md) (aggregatie); [Data-object](../applicatiearchitectuur/data-object-modelleerafspraken.md) (realisatie); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
