---
id: dienst-modelleerafspraken
type: kennismodel
titel: Dienst — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Dienst — modelleerafspraken

*Business Service* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/gedrag-extern` · paginatype `dienst`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). (NORA) |
| In Over GEMMA | ja (Dienst) |
| Duiding | Wat een afnemer van de gemeente kan krijgen, los van hoe het wordt uitgevoerd; gerealiseerd door een proces of functie. |
| Herken je aan | *gedrag* en *aangeboden gedrag*. Toetskenmerken, alle ja: *gerealiseerd door* †, *afnemer*, *benoembaar resultaat*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsproces ─realisatie→ Dienst; Bedrijfsfunctie ─realisatie→ Dienst |
| Eigenschappen | `afnemer` (verplicht) · `domein` (verplicht) · `gemma_functie` · `taakveld` · `beleidsdomein` · `gemma` · `gemma_generiek` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md); [Functie-indeling naar domein](../indelingen.md); [Procesindeling naar soort werk](../indelingen.md) (bij *generiek*) |
| Naamvorm | vanuit de afnemer, wat die kan doen of krijgen (Melding openbare ruimte doen); staat het in de UPL, dan de UPL-naam letterlijk (Verlof tot begraven) |
| Afstemming | UPL: bron én matchdoel: elk UPL-item wordt een dienst, valt nooit weg en houdt zijn naam; zonder match een procesarchitectuur-terugmelding · GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen · generiek GEMMA-element: bij *generiek*: specialisatie van een generieke GEMMA-dienst (`gemma_generiek`, exacte match); ontbreekt die, dan een voorstel aan GEMMA |
| Voorbeeld | wel: Onderhoud van graven; Melding openbare ruimte doen · niet: melding afhandelen (proces) |

## Afspraken

- Een dienst wordt gerealiseerd door een bedrijfsproces of bedrijfsfunctie; de verantwoordelijke rol hangt aan dat proces of die functie, niet aan de dienst.
- Een product of dienst valt nooit weg: wie het levert, is een bedrijfsproces.
- Een dienst uit de UPL blijft ook zonder landelijke wettelijke grondslag (de hoek zonder grondslag): zij is dan geen wettelijke taak, wordt niet uitgewerkt in processen, objecten, gebeurtenissen of rollen, wordt teruggemeld aan de procesarchitectuur en niet geëxporteerd; haar kenmerk *gerealiseerd door* steunt op de bron. Een VNG-modelverordening is nooit haar grondslag (*werkt uit voor*).
- Hangt de dienst onder een GEMMA-functie zonder beoordeling, dan noemt `gemma_functie` die functie, met de UPL als bron en het UPL-nummer als vindplaats.
- Een beleidskader hangt bij voorkeur aan een dienst of product; aan een proces alleen zolang er geen dienst of product is.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| bediening | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | bedient |  | ja |  |
| bediening | [Rol](rol-modelleerafspraken.md) | bedient |  | ja | de rol van de afnemer |
| aggregatie | [Dienst](dienst-modelleerafspraken.md) | omvat |  | ja |  |
| specialisatie | [Dienst](dienst-modelleerafspraken.md) | is een |  | nee | naar een generieke dienst |

Inkomend, bij het brontype: [Kanaal](kanaal-modelleerafspraken.md) (toewijzing); [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) (realisatie); [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) (realisatie, aggregatie); [Product](product-modelleerafspraken.md) (aggregatie); [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) (associatie); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
