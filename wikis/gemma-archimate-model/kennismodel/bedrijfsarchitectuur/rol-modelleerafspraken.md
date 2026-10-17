---
id: rol-modelleerafspraken
type: kennismodel
titel: Rol — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Rol — modelleerafspraken

*Business Role* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/actief-intern` · paginatype `rol`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. (ArchiMate) |
| In Over GEMMA | ja (Rol) |
| Duiding | Verantwoordelijkheid of hoedanigheid (aanvrager, belastingplichtige, heffingsambtenaar). |
| Herken je aan | *hoedanigheid*, niet *los van verantwoordelijkheid*. Moet ja: *voert gedrag uit* (kernrelatie). Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Rol ─toewijzing→ Bedrijfsproces; Rol ─toewijzing→ Bedrijfsfunctie; Rol ─toewijzing→ Bedrijfsinteractie |
| Eigenschappen | `doelgroep` (verplicht) · `gemma` · `gemma_generiek` · `ggm` · `data_objecten` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Procesindeling naar soort werk](../indelingen.md) (bij *generiek*); [Doelgroepindeling](../indelingen.md) |
| Naamvorm | de hoedanigheid in de gangbare term (Houder van de begraafplaats; Rechthebbende op het graf) |
| Afstemming | GGM: matchdoel voor het data-object (`ggm`, niet verplicht) · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen · generiek GEMMA-element: bij *generiek*: specialisatie van een generieke GEMMA-rol (`gemma_generiek`, exacte match), zoals Klant |
| Voorbeeld | wel: Houder van de begraafplaats; Rechthebbende op het graf; Aanvrager · niet: gemeenteraad (actor) |

## Afspraken

- Wat een rol met een object is, is toegang met een vaste verantwoordelijkheid; een handeling (aanvragen, afgeven) is een toewijzing van de rol aan het proces dat het object gebruikt of maakt.
- Een doelgroep (minima, jongeren) is geen rol maar een indeling van een actor.
- Een bestuursorgaan (gemeenteraad, college, burgemeester) hangt via de rol Beslisser aan gedrag; welk orgaan bij welk proces bevoegd is, staat met het wetsartikel in de beschrijving van het proces.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| toewijzing | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit*, *toegewezen partij* | ja |  |
| toewijzing | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | ja |  |
| toewijzing | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit*, *toegewezen partij* | nee |  |
| toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een [verantwoordelijkheid](../README.md#relatietypen) |  | ja | een verantwoordelijkheid; *partij* alleen naar een afspraak |
| toegang | [Afspraak](afspraak-modelleerafspraken.md) | een [verantwoordelijkheid](../README.md#relatietypen) |  | nee |  |
| aggregatie | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| specialisatie | [Rol](rol-modelleerafspraken.md) | is een |  | ja |  |

Inkomend, bij het brontype: [Actor](actor-modelleerafspraken.md) (toewijzing); [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) (aggregatie); [Kanaal](kanaal-modelleerafspraken.md) (bediening); [Dienst](dienst-modelleerafspraken.md) (bediening); [Product](product-modelleerafspraken.md) (bediening); [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) (associatie); [Data-object](../applicatiearchitectuur/data-object-modelleerafspraken.md) (associatie); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
