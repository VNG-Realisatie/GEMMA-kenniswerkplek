---
id: bedrijfssamenwerking-modelleerafspraken
type: kennismodel
titel: Bedrijfssamenwerking — modelleerafspraken
---

# Bedrijfssamenwerking — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Collaboration* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `bedrijfssamenwerking`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een bedrijfssamenwerking is een (tijdelijke) samenstelling van twee of meer bedrijfsrollen resulterend in een specifiek collectief gedrag in een bepaalde context. (ArchiMate) |
| In Over GEMMA | ja (Bedrijfssamenwerking) |
| Duiding | Samenwerkingsverband zonder eigen rechtspersoon (Zorg- en Veiligheidshuis); met eigen rechtspersoon is het een actor. |
| Herken je aan | *samenwerkingsverband* zonder *eigen rechtspersoon*. Moet ja: *voert gedrag uit* (kernrelatie), *soort partij*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfssamenwerking ─toewijzing→ Bedrijfsproces; Bedrijfssamenwerking ─toewijzing→ Bedrijfsfunctie; Bedrijfssamenwerking ─toewijzing→ Bedrijfsinteractie |
| Eigenschappen | `doelgroep` (verplicht): gemeente, inwoners en ondernemers of ketenpartners: de plaats in de Doelgroepindeling (gemeente, inwoners en ondernemers, ketenpartners) · `gemma`: de match met het GEMMA-model: het id gaat mee in de export |
| Indelingen | [Doelgroepindeling](../indelingen.md) |
| Naamvorm | de gangbare naam van het verband |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: Zorg- en Veiligheidshuis · niet: GGD (eigen rechtspersoon: actor) |

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| uit | aggregatie | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| uit | aggregatie | [Actor](actor-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |
| uit | toewijzing | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | ja |  |
| uit | toewijzing | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | toewijzing | [Bedrijfsinteractie](bedrijfsinteractie-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een verantwoordelijkheid: houder (lezen-schrijven), bronhouder (schrijven), beheerder (lezen-schrijven), verstrekker (lezen), afnemer (lezen), toezichthouder (lezen), betrokkene (lezen), partij (lezen-schrijven) |  | nee: uitbreiding op het GEMMA-kennismodel | een verantwoordelijkheid, als bij een rol |
| in | aggregatie | [Groepering](../overig/groepering-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Doelgroepindeling |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing→ Bedrijfssamenwerking | tussen partijen is alleen *actor vervult rol* een toewijzing |
| Bedrijfssamenwerking ─toewijzing→ Actor, Rol, Bedrijfssamenwerking, Kanaal | tussen partijen is alleen *actor vervult rol* een toewijzing |
| Bedrijfssamenwerking ─toewijzing→ Dienst | een dienst krijgt geen rol toegewezen: de rol hangt aan het proces of de functie die de dienst realiseert |
