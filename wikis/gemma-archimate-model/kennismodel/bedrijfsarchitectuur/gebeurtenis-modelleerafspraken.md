---
id: gebeurtenis-modelleerafspraken
type: kennismodel
titel: Gebeurtenis — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Gebeurtenis — modelleerafspraken

*Business Event* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/gedrag-intern` · paginatype `gebeurtenis`

| Afspraak | Inhoud |
|---|---|
| Definitie | Iets dat binnen of buiten een organisatie is gebeurd en binnen die organisatie of daarbuiten gevolgen heeft. (GEMMA) |
| In Over GEMMA | ja (Gebeurtenis) |
| Duiding | Ogenblikkelijk voorval dat gedrag start of afsluit (verhuizing, aanvraag ontvangen). |
| Herken je aan | *gedrag* en *toestandsverandering*. Moet ja: *leidt tot gedrag* (kernrelatie); hoogstens 1 nee: *komt herhaald voor*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Gebeurtenis ─triggering→ Bedrijfsproces; Gebeurtenis ─triggering→ Bedrijfsinteractie |
| Eigenschappen | `gemma` · `gemma_generiek` · `ggm` · `data_objecten` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Procesindeling naar kernobject](../indelingen.md); [Procesindeling naar soort werk](../indelingen.md) (bij *generiek*) |
| Naamvorm | een voltooide toestandsverandering (Overlijden; Verval van het grafrecht) |
| Afstemming | GGM: matchdoel voor het data-object (`ggm`, niet verplicht) · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen · generiek GEMMA-element: bij *generiek*: specialisatie van een generieke GEMMA-gebeurtenis (`gemma_generiek`, exacte match) |
| Voorbeeld | wel: Overlijden; Verval van het grafrecht; Aanvraag ontvangen · niet: verhuizing doorgeven (proces) |

## Afspraken

- Een gebeurtenis van buiten (de klant, een derde, het recht of een termijn) start een bedrijfsproces, nooit een deelproces.
- Een gebeurtenis die het resultaat is van een bedrijfsproces (een rechtsgevolg) kan elders een bedrijfsproces starten; een tussentoestand binnen één bedrijfsproces is geen element.
- Een gebeurtenis hangt onder het levensloopproces van het object waarvan de toestand verandert.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| triggering | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | leidt tot | *leidt tot gedrag* | ja |  |
| triggering | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | start | *leidt tot gedrag* | nee |  |
| triggering | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | vrij, uit de bron |  | nee | een rechtsgevolg dat een ander teweegbrengt |
| specialisatie | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | is een |  | nee | naar een generieke gebeurtenis |

Inkomend, bij het brontype: [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) (aggregatie, triggering); [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) (associatie); [Data-object](../applicatiearchitectuur/data-object-modelleerafspraken.md) (associatie).
