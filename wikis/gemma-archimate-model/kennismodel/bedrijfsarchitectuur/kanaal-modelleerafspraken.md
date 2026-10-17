---
id: kanaal-modelleerafspraken
type: kennismodel
titel: Kanaal — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Kanaal — modelleerafspraken

*Business Interface* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/actief-extern` · paginatype `kanaal`

| Afspraak | Inhoud |
|---|---|
| Definitie | Communicatiekanaal dat bij de dienstverlening wordt gebruikt. Elk kanaal kent verschillende vormen waarin informatie kan worden gedeeld. (NORA) |
| In Over GEMMA | ja (Kanaal) |
| Duiding | Loket, website, telefoon. |
| Herken je aan | *toegangspunt*. Moet ja: *ontsluit een dienst* (kernrelatie). Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Kanaal ─toewijzing→ Dienst |
| Eigenschappen | `doelgroep` (verplicht) · `gemma` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Doelgroepindeling](../indelingen.md) |
| Naamvorm | de gangbare naam van het kanaal |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: publieksbalie; gemeentelijke website · niet: klantcontact (gedrag) |

## Afspraken

- Kanalen vormen één centrale set: een onderwerp koppelt een dienst aan een bestaand kanaal; een nieuw kanaal alleen na besluit van de redacteur.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| toewijzing | [Dienst](dienst-modelleerafspraken.md) | vrij, uit de bron | *ontsluit een dienst* | ja |  |
| bediening | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |

Inkomend, bij het brontype: [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
