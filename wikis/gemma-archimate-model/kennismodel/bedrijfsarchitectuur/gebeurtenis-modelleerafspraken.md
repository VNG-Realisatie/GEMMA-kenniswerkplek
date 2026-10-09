---
id: gebeurtenis-modelleerafspraken
type: kennismodel
titel: Gebeurtenis — modelleerafspraken
---

# Gebeurtenis — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Event* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `gebeurtenis`

| Afspraak | Inhoud |
|---|---|
| Definitie | Iets dat binnen of buiten een organisatie is gebeurd en binnen die organisatie of daarbuiten gevolgen heeft. (GEMMA) |
| In Over GEMMA | ja (Gebeurtenis) |
| Duiding | Ogenblikkelijk voorval dat gedrag start of afsluit (verhuizing, aanvraag ontvangen). |
| Herken je aan | *gedrag* en *toestandsverandering*. Moet ja: *leidt tot gedrag* (kernrelatie); hoogstens 1 nee: *komt herhaald voor*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Gebeurtenis ─triggering→ Bedrijfsproces; Gebeurtenis ─triggering→ Bedrijfsinteractie |
| Eigenschappen | `gemma`: de match met het GEMMA-model: het id gaat mee in de export · `gemma_generiek`: het generieke GEMMA-element waarvan dit een specialisatie is (exacte match) |
| Indelingen | [Procesindeling naar kernobject](../indelingen.md); [Procesindeling naar soort werk](../indelingen.md) (bij *generiek*) |
| Naamvorm | een voltooide toestandsverandering (Overlijden; Verval van het grafrecht) |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen · generiek GEMMA-element: bij *generiek*: specialisatie van een generieke GEMMA-gebeurtenis (`gemma_generiek`, exacte match) |
| Voorbeeld | wel: Overlijden; Verval van het grafrecht; Aanvraag ontvangen · niet: verhuizing doorgeven (proces) |

## Afspraken

- Een gebeurtenis van buiten (de klant, een derde, het recht of een termijn) start een bedrijfsproces, nooit een deelproces.
- Een gebeurtenis die het resultaat is van een bedrijfsproces (een rechtsgevolg) kan elders een bedrijfsproces starten; een tussentoestand binnen één bedrijfsproces is geen element.
- Een gebeurtenis hangt onder het levensloopproces van het object waarvan de toestand verandert.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | aggregatie | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | omvat |  | nee: uitbreiding op het GEMMA-kennismodel | levensloopproces → gebeurtenis van zijn kernobject |
| in | triggering | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | leidt tot |  | ja |  |
| uit | triggering | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | leidt tot | *leidt tot gedrag* | ja |  |
| uit | triggering | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | start | *leidt tot gedrag* | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | triggering | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel | een rechtsgevolg dat een ander teweegbrengt |
| uit | specialisatie | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | is een |  | nee: uitbreiding op het GEMMA-kennismodel | naar een generieke gebeurtenis |
| in | associatie (gericht) | [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) | is grondslag voor |  | nee: uitbreiding op het GEMMA-kennismodel | de regeling die de gebeurtenis regelt |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing of toegang of associatie→ Gebeurtenis | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
| Gebeurtenis ─associatie→ Bedrijfsobject, Afspraak | het object volgt uit het levensloopproces waaronder de gebeurtenis hangt |
