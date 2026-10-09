---
id: bedrijfsinteractie-modelleerafspraken
type: kennismodel
titel: Bedrijfsinteractie — modelleerafspraken
---

# Bedrijfsinteractie — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Interaction* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `bedrijfsinteractie`

| Afspraak | Inhoud |
|---|---|
| Definitie | A unit of collective business behavior performed by two or more business actors, roles or collaborations. (ArchiMate) |
| In Over GEMMA | nee: uitbreiding op het GEMMA-kennismodel |
| Duiding | Gezamenlijk gedrag, zoals een ketensamenwerking waarin de bedrijfsprocessen van de partijen samenkomen (in het GEMMA-model het element Ketensamenwerking), of een keukentafelgesprek. |
| Herken je aan | *gedrag* en *gezamenlijk gedrag*. Moet ja: *toegewezen partij* (kernrelatie); hoogstens 1 nee: *aanleiding*, *benoembaar resultaat*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Rol ─toewijzing→ Bedrijfsinteractie |
| Eigenschappen | `kernobject`: het bedrijfsobject waarvan het proces de levensloop omvat (levensloopproces), waarin het een mutatie doet (bedrijfsproces), of dat door de keten gaat (bedrijfsinteractie) · `taakveld`: het Iv3-taakveld: de bovenste laag van de Beleidsdomeinindeling · `beleidsdomein`: het beleidsdomein (GGM, of gemeentelijk met een terugmelding) in de Beleidsdomeinindeling · `gemma`: de match met het GEMMA-model: het id gaat mee in de export |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md) (onder het beleidsdomein van haar kernobject); [Procesindeling naar kernobject](../indelingen.md) |
| Naamvorm | als bij een bedrijfsproces: infinitief met het object (Bezorgen stoffelijk overschot) |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: Bezorgen stoffelijk overschot (ketensamenwerking van gemeente, arts en uitvaartondernemer) · niet: Treffen maatregel bij besmet lijk (de GGD adviseert alleen) |

## Afspraken

- Een ketensamenwerking is een bedrijfsinteractie met een kernobject: het object dat door de keten gaat. De bedrijfsprocessen van de partijen bedienen haar; een bedrijfssamenwerking of de rollen van de partijen voeren haar uit. Het ketenproces erboven is impliciet en staat alleen in de beschrijving.
- Elke nieuwe bedrijfsinteractie wordt voorgelegd: estafette (elke partij verantwoordelijk voor haar deel: een bedrijfsinteractie) of orkestratie (één partij verantwoordelijk: geen interactie; voert de gemeente het deel uit, dan specialiseert dat bedrijfsproces het GEMMA-proces *Leveren dienst aan derden*).

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | toewijzing | [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | nee: uitbreiding op het GEMMA-kennismodel |  |
| in | toewijzing | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit*, *toegewezen partij* | nee: uitbreiding op het GEMMA-kennismodel |  |
| uit | toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een handeling: registreren (schrijven), bijwerken (lezen-schrijven), beëindigen (schrijven), raadplegen (lezen), verstrekken (lezen), bewaren (lezen-schrijven), overbrengen (lezen), vernietigen (schrijven) | *wordt bewerkt* | nee: uitbreiding op het GEMMA-kennismodel |  |
| in | bediening | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | vrij, uit de bron |  | nee: uitbreiding op het GEMMA-kennismodel | de bedrijfsprocessen van de partijen bedienen de ketensamenwerking |
| in | triggering | [Gebeurtenis](gebeurtenis-modelleerafspraken.md) | start | *leidt tot gedrag* | nee: uitbreiding op het GEMMA-kennismodel |  |
| in | aggregatie | [Groepering](../overig/groepering-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing of toegang of associatie→ Bedrijfsinteractie | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
