---
id: rol-modelleerafspraken
type: kennismodel
titel: Rol — modelleerafspraken
---

# Rol — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Role* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `rol`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een rol is de verantwoordelijkheid voor specifiek gedrag waar een actor aan toegewezen kan worden. (ArchiMate) |
| In Over GEMMA | ja (Rol) |
| Duiding | Verantwoordelijkheid of hoedanigheid (aanvrager, belastingplichtige, heffingsambtenaar). |
| Herken je aan | *hoedanigheid*, niet *los van verantwoordelijkheid*. Moet ja: *voert gedrag uit* (kernrelatie). Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Rol ─toewijzing→ Bedrijfsproces; Rol ─toewijzing→ Bedrijfsfunctie; Rol ─toewijzing→ Bedrijfsinteractie |
| Eigenschappen | `doelgroep` (verplicht): gemeente, inwoners en ondernemers of ketenpartners: de plaats in de Doelgroepindeling (gemeente, inwoners en ondernemers, ketenpartners) · `gemma`: de match met het GEMMA-model: het id gaat mee in de export · `gemma_generiek`: het generieke GEMMA-element waarvan dit een specialisatie is (exacte match) |
| Indelingen | [Procesindeling naar soort werk](../indelingen.md) (bij *generiek*); [Doelgroepindeling](../indelingen.md) |
| Naamvorm | de hoedanigheid in de gangbare term (Houder van de begraafplaats; Rechthebbende op het graf) |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen · generiek GEMMA-element: bij *generiek*: specialisatie van een generieke GEMMA-rol (`gemma_generiek`, exacte match), zoals Klant |
| Voorbeeld | wel: Houder van de begraafplaats; Rechthebbende op het graf; Aanvrager · niet: gemeenteraad (actor) |

## Afspraken

- Wat een rol met een object is, is toegang met een vaste verantwoordelijkheid; een handeling (aanvragen, afgeven) is een toewijzing van de rol aan het proces dat het object gebruikt of maakt.
- Een doelgroep (minima, jongeren) is geen rol maar een indeling van een actor.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | toewijzing | [Actor](actor-modelleerafspraken.md) | vervult | *vervult een rol* | ja |  |
| in | aggregatie | [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| uit | toewijzing | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit*, *toegewezen partij* | ja |  |
| uit | toewijzing | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | ja |  |
| uit | toewijzing | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit*, *toegewezen partij* | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een verantwoordelijkheid: houder (lezen-schrijven), bronhouder (schrijven), beheerder (lezen-schrijven), verstrekker (lezen), afnemer (lezen), toezichthouder (lezen), betrokkene (lezen), partij (lezen-schrijven) |  | ja | een verantwoordelijkheid; *partij* alleen naar een afspraak |
| uit | toegang | [Afspraak](afspraak-modelleerafspraken.md) | een verantwoordelijkheid: houder (lezen-schrijven), bronhouder (schrijven), beheerder (lezen-schrijven), verstrekker (lezen), afnemer (lezen), toezichthouder (lezen), betrokkene (lezen), partij (lezen-schrijven) |  | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | aggregatie | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| uit | specialisatie | [Rol](rol-modelleerafspraken.md) | is een |  | ja |  |
| in | bediening | [Kanaal](kanaal-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| in | bediening | [Dienst](dienst-modelleerafspraken.md) | bedient |  | ja | de rol van de afnemer |
| in | bediening | [Product](product-modelleerafspraken.md) | bedient |  | ja | de rol van de afnemer, een specialisatie van Klant |
| in | associatie (gericht) | [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) | is grondslag voor |  | nee: uitbreiding op het GEMMA-kennismodel | de regeling die de rol regelt |
| in | aggregatie | [Groepering](../overig/groepering-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | Doelgroepindeling |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Rol ─toewijzing→ Actor, Rol, Bedrijfssamenwerking, Kanaal | tussen partijen is alleen *actor vervult rol* een toewijzing |
| Rol ─toewijzing→ Dienst | een dienst krijgt geen rol toegewezen: de rol hangt aan het proces of de functie die de dienst realiseert |
| Rol ─associatie→ Bedrijfsobject, Afspraak | wat een rol met een object is, is toegang met een verantwoordelijkheid; een handeling is een toewijzing van de rol aan het proces |
| Rol ─associatie→ Rol | een handeling tussen rollen loopt via een proces (toewijzing), een stroom of een gebeurtenis, zoals tussen actoren |
