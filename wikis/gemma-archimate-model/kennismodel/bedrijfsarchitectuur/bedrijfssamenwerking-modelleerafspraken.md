---
id: bedrijfssamenwerking-modelleerafspraken
type: kennismodel
titel: Bedrijfssamenwerking — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Bedrijfssamenwerking — modelleerafspraken

*Business Collaboration* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/actief-intern` · paginatype `bedrijfssamenwerking`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. (ArchiMate) |
| In Over GEMMA | ja (Bedrijfssamenwerking) |
| Duiding | Samenwerkingsverband zonder eigen rechtspersoon (Zorg- en Veiligheidshuis); met eigen rechtspersoon is het een actor. |
| Herken je aan | *samenwerkingsverband* zonder *eigen rechtspersoon*. Toetskenmerken, alle ja: *voert gedrag uit* †. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfssamenwerking ─toewijzing→ Bedrijfsproces; Bedrijfssamenwerking ─toewijzing→ Bedrijfsfunctie; Bedrijfssamenwerking ─toewijzing→ Bedrijfsinteractie |
| Eigenschappen | `doelgroep` (verplicht) · `gemma` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Doelgroepindeling](../indelingen.md) |
| Naamvorm | de gangbare naam van het verband |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: Zorg- en Veiligheidshuis · niet: GGD (eigen rechtspersoon: actor) |

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| aggregatie | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| aggregatie | [Actor](actor-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| toewijzing | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | ja |  |
| toewijzing | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | nee |  |
| toewijzing | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | nee |  |
| toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een [verantwoordelijkheid](../README.md#relatietypen) |  | nee | een verantwoordelijkheid, als bij een rol |

Inkomend, bij het brontype: [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
