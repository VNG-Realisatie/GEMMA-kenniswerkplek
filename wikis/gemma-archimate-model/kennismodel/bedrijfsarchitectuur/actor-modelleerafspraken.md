---
id: actor-modelleerafspraken
type: kennismodel
titel: Actor — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Actor — modelleerafspraken

*Business Actor* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/actief-intern` · paginatype `actor`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een organisatie, afdeling daarbinnen of persoon die activiteiten kan uitvoeren. (GEMMA) |
| In Over GEMMA | ja (Actor) |
| Duiding | Persoon, organisatie of eenheid, ook extern of generiek (inwoner), en een samenwerkingsverband met eigen rechtspersoon (GGD). Hangt alleen via een rol aan gedrag en objecten. |
| Herken je aan | *handelende partij* met *los van verantwoordelijkheid*; of *samenwerkingsverband* met *eigen rechtspersoon*. Toetskenmerken, alle ja: *vervult een rol* †. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Actor ─toewijzing→ Rol |
| Eigenschappen | `doelgroep` (verplicht) · `gemma` · `ggm` · `data_objecten` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Doelgroepindeling](../indelingen.md) |
| Naamvorm | de soort partij in de gangbare term (College van B&W; Kerkgenootschap) |
| Afstemming | GGM: matchdoel voor het data-object (`ggm`, niet verplicht) · GEMMA-model: match op betekenis; het GEMMA-id gaat mee in de export en overschrijft naam en definitie van het GEMMA-element; een zwakke of partiële match voorleggen |
| Voorbeeld | wel: College van B&W; Kerkgenootschap; GGD; Rijk · niet: gemeente Utrecht (één exemplaar); een afzonderlijk ministerie of rijksdienst (staat in de beschrijving van Rijk) |

## Afspraken

- Een actor is een soort partij: elke gemeente heeft ermee te maken in dezelfde rol. Dat sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat: Rijk, Provincie en Waterschap zijn een soort partij.
- Tussen actoren alleen structurele relaties (deel van, lid van, voorzitter van); een handeling loopt via rollen en processen of een gebeurtenis.
- Een externe partij wordt alleen een actor bij een structurele relatie met de gemeente (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht).

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| toewijzing | [Rol](rol-modelleerafspraken.md) | vervult | *vervult een rol* | ja |  |
| aggregatie | [Actor](actor-modelleerafspraken.md) | omvat |  | nee | structureel: deel van, lid van |
| associatie (gericht) | [Actor](actor-modelleerafspraken.md) | is voorzitter van |  | nee | alleen een structurele relatie |

Inkomend, bij het brontype: [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) (aggregatie); [Data-object](../applicatiearchitectuur/data-object-modelleerafspraken.md) (associatie); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
