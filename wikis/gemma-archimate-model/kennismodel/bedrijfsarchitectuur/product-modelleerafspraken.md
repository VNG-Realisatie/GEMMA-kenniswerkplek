---
id: product-modelleerafspraken
type: kennismodel
titel: Product — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Product — modelleerafspraken

*Product* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/samengesteld` · paginatype `product`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. (GEMMA) |
| In Over GEMMA | ja (Product) |
| Duiding | Wat de gemeente als geheel aanbiedt, zoals in de productencatalogus: diensten met afspraken, geen losse objecten. Een verleend exemplaar is een bedrijfsobject, geen product. |
| Herken je aan | *aanbod als geheel*. Moet ja: *omvat diensten en afspraken* (kernrelatie), *zelfstandig aanbod*; hoogstens 1 nee: *afnemer*, *benoembaar resultaat*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Product ─aggregatie→ Dienst; Product ─aggregatie→ Afspraak |
| Eigenschappen | `afnemer` (verplicht) · `domein` (verplicht) · `taakveld` · `beleidsdomein` · `gemma` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md); [Functie-indeling naar domein](../indelingen.md) |
| Naamvorm | de UPL-naam letterlijk (Grafuitgifte), met een synoniem waar dat betekenis toevoegt |
| Afstemming | UPL: bron én matchdoel: een UPL-item valt nooit weg en houdt zijn naam; zonder match een procesarchitectuur-terugmelding · GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: bewonersparkeervergunning zoals de productencatalogus haar aanbiedt · niet: bezoekersparkeervergunning als tarief van de parkeervergunning (geen zelfstandig aanbod) |

## Afspraken

- Een product komt nooit uit één UPL-item: een UPL-item is een dienst, en een product bundelt zulke diensten met afspraken.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| aggregatie | [Dienst](dienst-modelleerafspraken.md) | omvat | *omvat diensten en afspraken* | ja |  |
| aggregatie | [Afspraak](afspraak-modelleerafspraken.md) | omvat | *omvat diensten en afspraken* | ja |  |
| bediening | [Rol](rol-modelleerafspraken.md) | bedient |  | ja | de rol van de afnemer, een specialisatie van Klant |

Inkomend, bij het brontype: [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) (associatie); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
