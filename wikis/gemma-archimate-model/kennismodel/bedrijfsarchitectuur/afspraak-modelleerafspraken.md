---
id: afspraak-modelleerafspraken
type: kennismodel
titel: Afspraak — modelleerafspraken
---

# Afspraak — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Contract* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `bedrijfsobject`

| Afspraak | Inhoud |
|---|---|
| Definitie | Overeenkomst tussen meerdere partijen betreffende een bepaald onderwerp. (GEMMA) |
| In Over GEMMA | ja (Afspraak) |
| Duiding | Een afspraak tussen partijen (overeenkomst, convenant). Een besluit of verordening is géén afspraak. Een afspraak is een bijzonder bedrijfsobject en heeft dezelfde pagina en indeling. |
| Herken je aan | *afspraak*. Moet ja: *wordt bewerkt* (kernrelatie); hoogstens 1 nee: *onderscheidbare exemplaren*, *levenscyclus*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsproces ─toegang→ Afspraak |
| Niveaus | als bij een bedrijfsobject: kernobject, subobject of generiek |
| Eigenschappen | `taakveld`: het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling · `beleidsdomein`: het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling · `ggm`: de match met het GGM: entiteit, sterkte en onderbouwing · `gemma`: de match met het GEMMA-model: het id gaat mee in de export · `data_object`: annotatie: het begrip wordt als gegevensstructuur geautomatiseerd verwerkt |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md) |
| Naamvorm | de gangbare term uit beleid en praktijk, zoals bij een bedrijfsobject |
| Afstemming | GGM: als bij een bedrijfsobject · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: Uitvoeringsovereenkomst; Grafrecht · niet: subsidiebeschikking (eenzijdig besluit); verordening |

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | toegang | [Rol](rol-modelleerafspraken.md) | een verantwoordelijkheid: houder (lezen-schrijven), bronhouder (schrijven), beheerder (lezen-schrijven), verstrekker (lezen), afnemer (lezen), toezichthouder (lezen), betrokkene (lezen), partij (lezen-schrijven) |  | nee: uitbreiding op het GEMMA-kennismodel |  |
| in | toegang | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | een handeling: registreren (schrijven), bijwerken (lezen-schrijven), beëindigen (schrijven), raadplegen (lezen), verstrekken (lezen), bewaren (lezen-schrijven), overbrengen (lezen), vernietigen (schrijven) | *wordt bewerkt* | nee: uitbreiding op het GEMMA-kennismodel |  |
| in | aggregatie | [Product](product-modelleerafspraken.md) | omvat | *omvat diensten en afspraken* | ja |  |
| uit | associatie (gericht) | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel |  |
| in | aggregatie | [Groepering](../overig/groepering-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing of toegang of associatie→ Afspraak | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
| Rol ─associatie→ Afspraak | wat een rol met een object is, is toegang met een verantwoordelijkheid; een handeling is een toewijzing van de rol aan het proces |
| Dienst ─toegang→ Afspraak | een dienst heeft geen toegang tot een object; het proces dat haar realiseert wel |
| Gebeurtenis ─associatie→ Afspraak | het object volgt uit het levensloopproces waaronder de gebeurtenis hangt |
| Afspraak ─associatie→ Dienst | een object hangt via het proces dat de dienst realiseert (toegang) aan een dienst |
