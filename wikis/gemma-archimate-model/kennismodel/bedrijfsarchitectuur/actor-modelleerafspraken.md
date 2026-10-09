---
id: actor-modelleerafspraken
type: kennismodel
titel: Actor — modelleerafspraken
---

# Actor — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Actor* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `actor`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. (GEMMA) |
| In Over GEMMA | ja (Actor) |
| Duiding | Persoon, organisatie of eenheid, ook extern of generiek (inwoner), en een samenwerkingsverband met eigen rechtspersoon (GGD). Hangt alleen via een rol aan gedrag en objecten. |
| Herken je aan | *handelende partij* met *los van verantwoordelijkheid*; of *samenwerkingsverband* met *eigen rechtspersoon*. Moet ja: *vervult een rol* (kernrelatie), *soort partij*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Actor ─toewijzing→ Rol |
| Eigenschappen | `doelgroep` (verplicht): gemeente, inwoners en ondernemers of ketenpartners: de plaats in de Doelgroepindeling (gemeente, inwoners en ondernemers, ketenpartners) · `gemma`: de match met het GEMMA-model: het id gaat mee in de export |
| Indelingen | [Doelgroepindeling](../indelingen.md) |
| Naamvorm | de soort partij in de gangbare term (College van B&W; Kerkgenootschap) |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: College van B&W; Kerkgenootschap; GGD; Rijk · niet: gemeente Utrecht (één exemplaar); een afzonderlijk ministerie of rijksdienst (staat in de beschrijving van Rijk) |

## Afspraken

- Een actor is een soort partij: elke gemeente heeft ermee te maken in dezelfde rol. Dat sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat: Rijk, Provincie en Waterschap zijn een soort partij.
- Tussen actoren alleen structurele relaties (deel van, lid van, voorzitter van); een handeling loopt via rollen en processen of een gebeurtenis.
- Een externe partij wordt alleen een actor bij een structurele relatie met de gemeente (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht).

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| uit | toewijzing | [Rol](rol-modelleerafspraken.md) | vervult | *vervult een rol* | ja |  |
| uit | aggregatie | [Actor](actor-modelleerafspraken.md) | omvat |  | nee: uitbreiding op het GEMMA-kennismodel | structureel: deel van, lid van |
| uit | associatie (gericht) | [Actor](actor-modelleerafspraken.md) | is voorzitter van |  | nee: uitbreiding op het GEMMA-kennismodel | alleen een structurele relatie |
| in | aggregatie | [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing of toegang of associatie→ Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Dienst, Bedrijfsinteractie, Bedrijfsobject, Afspraak | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
| Actor ─toewijzing→ Actor, Bedrijfssamenwerking, Kanaal | tussen partijen is alleen *actor vervult rol* een toewijzing |
| Rol, Bedrijfssamenwerking ─toewijzing→ Actor | tussen partijen is alleen *actor vervult rol* een toewijzing |
