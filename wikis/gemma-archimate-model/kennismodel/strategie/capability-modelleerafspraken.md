---
id: capability-modelleerafspraken
type: kennismodel
titel: Capability — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Capability — modelleerafspraken

*Capability* in ArchiMate · laag Strategie · vak `strategie/gedrag` · paginatype `capability`

| Afspraak | Inhoud |
|---|---|
| Definitie | Een vermogen waarover een organisatie, persoon of systeem beschikt. (GEMMA) |
| In Over GEMMA | ja (Capability) |
| Duiding | Strategisch: wat de gemeente moet kunnen om haar opgaven waar te maken, los van hoe, door wie, in welke volgorde en met welk kanaal of systeem. Het verandert met de strategische opgaven en stuurt waarin zij investeert en wat zij ontwikkelt. Heeft het een uitvoerder of gebruikt het objecten, dan is het uitvoerend: een functie of proces. |
| Herken je aan | *vermogen*. Toetskenmerken, alle ja: *gerealiseerd door* †, *beoordeelbaar*, *onderscheidend*, *stabiel over tijd*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsfunctie ─realisatie→ Capability |
| Niveaus | capability: het grofste niveau dat genoeg onderscheid geeft · deelcapability: een deel dat apart ontwikkeld, beoordeeld of bestuurd wordt |
| Eigenschappen | `domein` (verplicht) · `gemma` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Capabilitykaart](../indelingen.md) |
| Naamvorm | object en werkwoord in de onbepaalde wijs (Identiteit vaststellen); nooit dezelfde naam als een functie of proces |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: optioneel, op betekenis: de capabilities van GEMMA beschrijven de informatievoorziening; een zwakke match voorleggen |
| Voorbeeld | wel: Identiteit vaststellen; Personen registreren; Lijkbezorging waarborgen · niet: Verkiezingen organiseren (valt samen met één functie); Dienstverlening (te breed); Aanvraag controleren op volledigheid (te concreet) |

## Afspraken

- Een element alleen als ten minste twee bedrijfsfuncties haar realiseren; valt zij samen met één functie, dan volstaat de functie.
- Alleen een bedrijfsfunctie realiseert een capability. De houder is altijd de gemeente: geen relatie naar een actor, rol of resource.
- De realisatie steunt op de bronnen van de functies; *beoordeelbaar* en *onderscheidend* op een landelijke richtlijn, of op een oordeel met onderbouwing.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| aggregatie | [Capability](capability-modelleerafspraken.md) | omvat |  | nee | capability → deelcapability |

Inkomend, bij het brontype: [Bedrijfsfunctie](../bedrijfsarchitectuur/bedrijfsfunctie-modelleerafspraken.md) (realisatie); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
