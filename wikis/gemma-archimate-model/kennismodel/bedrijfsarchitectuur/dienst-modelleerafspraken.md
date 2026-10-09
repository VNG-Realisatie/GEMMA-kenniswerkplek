---
id: dienst-modelleerafspraken
type: kennismodel
titel: Dienst — modelleerafspraken
---

# Dienst — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Service* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `dienst`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een afgebakende prestatie van een persoon of organisatie (de dienstverlener), die voorziet in een behoefte van haar omgeving (de dienstafnemer(s)). (NORA) |
| In Over GEMMA | ja (Dienst) |
| Duiding | Wat een afnemer van de gemeente kan krijgen, los van hoe het wordt uitgevoerd; gerealiseerd door een proces of functie. |
| Herken je aan | *gedrag* en *aangeboden gedrag*. Moet ja: *gerealiseerd door* (kernrelatie); hoogstens 1 nee: *afnemer*, *benoembaar resultaat*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsproces ─realisatie→ Dienst; Bedrijfsfunctie ─realisatie→ Dienst |
| Eigenschappen | `afnemer` (verplicht): voor wie het is: extern of intern (de bovenste laag van het processenlandschap, de rol Klant en de externe en interne UPL-lijst) (extern, intern) · `domein` (verplicht): het GEMMA-domein, de plaats in de Functie-indeling naar domein (Bestuur, Fysieke leefomgeving, Niet domeingebonden, Openbare orde en veiligheid, Ondersteuning, Publieksdiensten, Sociaal domein) · `taakveld`: het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling · `beleidsdomein`: het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling · `gemma`: de match met het GEMMA-model: het id gaat mee in de export · `gemma_generiek`: het generieke GEMMA-element waarvan dit een specialisatie is (exacte match) |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md); [Functie-indeling naar domein](../indelingen.md); [Procesindeling naar soort werk](../indelingen.md) (bij *generiek*) |
| Naamvorm | vanuit de afnemer, wat die kan doen of krijgen (Melding openbare ruimte doen); staat het in de UPL, dan de UPL-naam letterlijk (Verlof tot begraven) |
| Afstemming | UPL: bron én matchdoel, als bij een product · GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen · generiek GEMMA-element: bij *generiek*: specialisatie van een generieke GEMMA-dienst (`gemma_generiek`, exacte match); ontbreekt die, dan een voorstel aan GEMMA |
| Voorbeeld | wel: Onderhoud van graven; Melding openbare ruimte doen · niet: melding afhandelen (proces) |

## Afspraken

- Een dienst wordt gerealiseerd door een bedrijfsproces of bedrijfsfunctie; de verantwoordelijke rol hangt aan dat proces of die functie, niet aan de dienst.
- Een product of dienst valt nooit weg: wie het levert, is een bedrijfsproces.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | toewijzing | [Kanaal](kanaal-modelleerafspraken.md) | vrij, uit de bron | *ontsluit een dienst* | ja |  |
| in | realisatie | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | realiseert | *gerealiseerd door* | ja |  |
| in | realisatie | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | realiseert | *gerealiseerd door* | ja |  |
| in | aggregatie | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | omvat |  | nee: uitbreiding op het GEMMA-kennismodel | Functie-indeling naar domein |
| uit | bediening | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | bedient |  | ja |  |
| uit | bediening | [Rol](rol-modelleerafspraken.md) | bedient |  | ja | de rol van de afnemer |
| uit | aggregatie | [Dienst](dienst-modelleerafspraken.md) | omvat |  | ja |  |
| uit | specialisatie | [Dienst](dienst-modelleerafspraken.md) | is een |  | nee: uitbreiding op het GEMMA-kennismodel | naar een generieke dienst |
| in | aggregatie | [Product](product-modelleerafspraken.md) | omvat | *omvat diensten en afspraken* | ja |  |
| in | associatie (gericht) | [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) | is grondslag voor, werkt uit voor, geeft richtlijn voor | *is grondslag voor* | nee: uitbreiding op het GEMMA-kennismodel | de grondslag; bij voorkeur naar een product |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing of toegang of associatie→ Dienst | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
| Rol, Bedrijfssamenwerking ─toewijzing→ Dienst | een dienst krijgt geen rol toegewezen: de rol hangt aan het proces of de functie die de dienst realiseert |
| Dienst ─toegang→ Bedrijfsobject, Afspraak | een dienst heeft geen toegang tot een object; het proces dat haar realiseert wel |
| Bedrijfsobject, Afspraak ─associatie→ Dienst | een object hangt via het proces dat de dienst realiseert (toegang) aan een dienst |
