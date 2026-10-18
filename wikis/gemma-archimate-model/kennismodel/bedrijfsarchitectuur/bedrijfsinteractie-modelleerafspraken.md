---
id: bedrijfsinteractie-modelleerafspraken
type: kennismodel
titel: Bedrijfsinteractie — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Bedrijfsinteractie — modelleerafspraken

*Business Interaction* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/gedrag-intern` · paginatype `bedrijfsinteractie`

| Afspraak | Inhoud |
|---|---|
| Definitie | A unit of collective business behavior performed by two or more business actors, roles or collaborations. (ArchiMate) |
| In Over GEMMA | nee: uitbreiding op het GEMMA-kennismodel |
| Duiding | Gezamenlijk gedrag, zoals een ketensamenwerking waarin de bedrijfsprocessen van de partijen samenkomen (in het GEMMA-model het element Ketensamenwerking), of een keukentafelgesprek. |
| Herken je aan | *gedrag* en *gezamenlijk gedrag*. Toetskenmerken, alle ja: *toegewezen partij* †, *aanleiding* †, *benoembaar resultaat*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Rol ─toewijzing→ Bedrijfsinteractie |
| Eigenschappen | `kernobject` · `taakveld` · `beleidsdomein` · `gemma` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Beleidsdomeinindeling](../indelingen.md) (onder het beleidsdomein van haar kernobject); [Procesindeling naar kernobject](../indelingen.md) |
| Naamvorm | als bij een bedrijfsproces: infinitief met het object (Bezorgen stoffelijk overschot) |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: Bezorgen stoffelijk overschot (ketensamenwerking van gemeente, arts en uitvaartondernemer) · niet: Treffen maatregel bij besmet lijk (de GGD adviseert alleen) |

## Afspraken

- Een ketensamenwerking is een bedrijfsinteractie met een kernobject: het object dat door de keten gaat. De bedrijfsprocessen van de partijen bedienen haar; een bedrijfssamenwerking of de rollen van de partijen voeren haar uit. Het ketenproces erboven is impliciet en staat alleen in de beschrijving.
- Elke nieuwe bedrijfsinteractie wordt voorgelegd: estafette (elke partij verantwoordelijk voor haar deel: een bedrijfsinteractie) of orkestratie (één partij verantwoordelijk: geen interactie; voert de gemeente het deel uit, dan specialiseert dat bedrijfsproces het GEMMA-proces *Leveren dienst aan derden*).

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een [handeling](../README.md#relatietypen) | *wordt bewerkt* | nee |  |

Inkomend, bij het brontype: [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) (toewijzing); [Rol](rol-modelleerafspraken.md) (toewijzing); [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) (bediening); [Gebeurtenis](gebeurtenis-modelleerafspraken.md) (triggering); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
