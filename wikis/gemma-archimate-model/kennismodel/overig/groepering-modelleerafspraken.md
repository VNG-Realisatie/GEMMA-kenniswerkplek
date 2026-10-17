---
id: groepering-modelleerafspraken
type: kennismodel
titel: Groepering — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Groepering — modelleerafspraken

*Grouping* in ArchiMate · laag Overig · geen pagina (indeling)

| Afspraak | Inhoud |
|---|---|
| Definitie | Een groepering aggregeert of omvat concepten die bij elkaar horen op grond van een gemeenschappelijk kenmerk. (ArchiMate) |
| In Over GEMMA | ja (Groepering) |
| Duiding | Geen begrip uit een bron, maar een knoop van een indeling: taakveld, beleidsdomein, domein, groep van de Grondslagindeling. Zonder groepering heeft een indeling geen relaties in de export. Een groepering komt uit GEMMA, of de wiki maakt haar nieuw: een beleidsdomein dat GEMMA niet kent, een groep van de Grondslagindeling. |
| Naamvorm | de naam uit de indelingslijst (Iv3-taakveld, GGM-beleidsdomein, GEMMA-domein) of het brontype (Rijksregelgeving) |
| Afstemming | GEMMA-model: de groepering van GEMMA met dezelfde naam en hetzelfde GEMMA type; anders een nieuwe groepering in de map van de wiki, met een terugmelding · GGM: het beleidsdomein: per beleidsdomein de dekking |
| Voorbeeld | wel: Burgerzaken (beleidsdomein) · niet: lijkbezorging als thema (een onderwerp, geen groepering) |

## Afspraken

- Een groepering krijgt geen pagina en geen beoordeling; het script maakt haar bij de export uit de indelingsvelden van de elementen. De beschrijving van een beleidsdomein staat in het register van beleidsdomeinen.
- Een begrip dat alleen een thema is, wordt geen groepering en geen element.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| aggregatie | [Groepering](groepering-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | taakveld → beleidsdomein; domein → beleidsdomein |
| aggregatie | [Bedrijfsobject](../bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | Beleidsdomeinindeling |
| aggregatie | [Afspraak](../bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Beleidsdomeinindeling |
| aggregatie | [Product](../bedrijfsarchitectuur/product-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Beleidsdomeinindeling; Functie-indeling naar domein |
| aggregatie | [Dienst](../bedrijfsarchitectuur/dienst-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Beleidsdomeinindeling |
| aggregatie | [Bedrijfsproces](../bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Beleidsdomeinindeling: alleen een levensloopproces of een generiek bedrijfsproces |
| aggregatie | [Bedrijfsinteractie](../bedrijfsarchitectuur/bedrijfsinteractie-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Beleidsdomeinindeling |
| aggregatie | [Bedrijfsfunctie](../bedrijfsarchitectuur/bedrijfsfunctie-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | Functie-indeling naar domein: alleen een functie op domeinniveau |
| aggregatie | [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Beleidsdomeinindeling; Grondslagindeling |
| aggregatie | [Actor](../bedrijfsarchitectuur/actor-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Doelgroepindeling |
| aggregatie | [Rol](../bedrijfsarchitectuur/rol-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | Doelgroepindeling |
| aggregatie | [Bedrijfssamenwerking](../bedrijfsarchitectuur/bedrijfssamenwerking-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Doelgroepindeling |
| aggregatie | [Kanaal](../bedrijfsarchitectuur/kanaal-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee | Doelgroepindeling |
