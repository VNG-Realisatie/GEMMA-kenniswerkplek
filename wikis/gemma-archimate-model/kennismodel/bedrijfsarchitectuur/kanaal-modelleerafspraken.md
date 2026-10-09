---
id: kanaal-modelleerafspraken
type: kennismodel
titel: Kanaal — modelleerafspraken
---

# Kanaal — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Interface* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `kanaal`

| Afspraak | Inhoud |
|---|---|
| Definitie | Communicatiekanaal dat bij de dienstverlening wordt gebruikt. Elk kanaal kent verschillende vormen waarin informatie kan worden gedeeld. (NORA) |
| In Over GEMMA | ja (Kanaal) |
| Duiding | Loket, website, telefoon. |
| Herken je aan | *toegangspunt*. Moet ja: *ontsluit een dienst* (kernrelatie). Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Kanaal ─toewijzing→ Dienst |
| Eigenschappen | `doelgroep` (verplicht): gemeente, inwoners en ondernemers of ketenpartners: de plaats in de Doelgroepindeling (gemeente, inwoners en ondernemers, ketenpartners) · `gemma`: de match met het GEMMA-model: het id gaat mee in de export |
| Indelingen | [Doelgroepindeling](../indelingen.md) |
| Naamvorm | de gangbare naam van het kanaal |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: publieksbalie; gemeentelijke website · niet: klantcontact (gedrag) |

## Afspraken

- Kanalen vormen één centrale set: een onderwerp koppelt een dienst aan een bestaand kanaal; een nieuw kanaal alleen na besluit van de redacteur.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| uit | toewijzing | [Dienst](dienst-modelleerafspraken.md) | vrij, uit de bron | *ontsluit een dienst* | ja |  |
| uit | bediening | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron |  | ja |  |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing→ Kanaal | tussen partijen is alleen *actor vervult rol* een toewijzing |
| Rol, Bedrijfssamenwerking ─toewijzing→ Kanaal | tussen partijen is alleen *actor vervult rol* een toewijzing |
| Kanaal ─andere relatie→ elk type | een kanaal is toegewezen aan een dienst en bedient een rol |
