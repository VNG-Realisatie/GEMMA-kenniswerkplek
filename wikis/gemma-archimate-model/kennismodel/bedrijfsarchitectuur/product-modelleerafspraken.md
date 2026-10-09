---
id: product-modelleerafspraken
type: kennismodel
titel: Product — modelleerafspraken
---

# Product — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Product* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `product`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een Product is een gebundeld aanbod van diensten met bijbehorende afspraken, geleverd door een organisatie aan een afnemer en met waarde voor die afnemer. (GEMMA) |
| In Over GEMMA | ja (Product) |
| Duiding | Wat de gemeente als geheel aanbiedt, zoals in de productencatalogus: diensten met afspraken, geen losse objecten. Een verleend exemplaar is een bedrijfsobject, geen product. |
| Herken je aan | *aanbod als geheel*. Moet ja: *omvat diensten en afspraken* (kernrelatie), *zelfstandig aanbod*; hoogstens 1 nee: *afnemer*, *benoembaar resultaat*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Product ─aggregatie→ Dienst; Product ─aggregatie→ Afspraak |
| Eigenschappen | `afnemer` (verplicht): voor wie het is: extern of intern (de bovenste laag van het processenlandschap, de rol Klant en de externe en interne UPL-lijst) (extern, intern) · `domein` (verplicht): het GEMMA-domein, de plaats in de Functie-indeling naar domein (Bestuur, Fysieke leefomgeving, Niet domeingebonden, Openbare orde en veiligheid, Ondersteuning, Publieksdiensten, Sociaal domein) · `taakveld`: het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling · `beleidsdomein`: het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling · `gemma`: de match met het GEMMA-model: het id gaat mee in de export |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md); [Functie-indeling naar domein](../indelingen.md) |
| Naamvorm | de UPL-naam letterlijk (Grafuitgifte), met een synoniem waar dat betekenis toevoegt |
| Afstemming | UPL: bron én matchdoel: een UPL-item valt nooit weg en houdt zijn naam; zonder match een procesarchitectuur-terugmelding · GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: bewonersparkeervergunning zoals de productencatalogus haar aanbiedt · niet: bezoekersparkeervergunning als tarief van de parkeervergunning (geen zelfstandig aanbod) |

## Afspraken

- Een product of dienst uit de UPL blijft ook zonder landelijke wettelijke grondslag; dan wordt het niet uitgewerkt in processen, objecten, gebeurtenissen of rollen.
- Een beleidskader hangt bij voorkeur aan een product; aan een proces of dienst alleen zolang er geen product is.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| uit | aggregatie | [Dienst](dienst-modelleerafspraken.md) | omvat | *omvat diensten en afspraken* | ja |  |
| uit | aggregatie | [Afspraak](afspraak-modelleerafspraken.md) | omvat | *omvat diensten en afspraken* | ja |  |
| uit | bediening | [Rol](rol-modelleerafspraken.md) | bedient |  | ja | de rol van de afnemer, een specialisatie van Klant |
| in | associatie (gericht) | [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) | is grondslag voor, werkt uit voor, geeft richtlijn voor | *is grondslag voor* | ja | de grondslag; bij voorkeur naar een product |
| in | aggregatie | [Groepering](../overig/groepering-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling; Functie-indeling naar domein |
