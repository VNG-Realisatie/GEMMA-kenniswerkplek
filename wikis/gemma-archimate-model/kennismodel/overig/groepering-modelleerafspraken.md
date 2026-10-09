---
id: groepering-modelleerafspraken
type: kennismodel
titel: Groepering — modelleerafspraken
---

# Groepering — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

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

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| uit | aggregatie | [Groepering](groepering-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | taakveld → beleidsdomein; domein → beleidsdomein |
| uit | aggregatie | [Bedrijfsobject](../bedrijfsarchitectuur/bedrijfsobject-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | Beleidsdomeinindeling |
| uit | aggregatie | [Afspraak](../bedrijfsarchitectuur/afspraak-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling |
| uit | aggregatie | [Product](../bedrijfsarchitectuur/product-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling; Functie-indeling naar domein |
| uit | aggregatie | [Dienst](../bedrijfsarchitectuur/dienst-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling |
| uit | aggregatie | [Bedrijfsproces](../bedrijfsarchitectuur/bedrijfsproces-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling: alleen een levensloopproces |
| uit | aggregatie | [Bedrijfsinteractie](../bedrijfsarchitectuur/bedrijfsinteractie-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling |
| uit | aggregatie | [Bedrijfsfunctie](../bedrijfsarchitectuur/bedrijfsfunctie-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | Functie-indeling naar domein: alleen een functie op domeinniveau |
| uit | aggregatie | [Beleidskader](../motivatie/beleidskader-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Beleidsdomeinindeling; Grondslagindeling |
| uit | aggregatie | [Actor](../bedrijfsarchitectuur/actor-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Doelgroepindeling |
| uit | aggregatie | [Rol](../bedrijfsarchitectuur/rol-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | ja | Doelgroepindeling |
| uit | aggregatie | [Bedrijfssamenwerking](../bedrijfsarchitectuur/bedrijfssamenwerking-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Doelgroepindeling |
| uit | aggregatie | [Kanaal](../bedrijfsarchitectuur/kanaal-modelleerafspraken.md) | geen: het script maakt de relatie uit de indelingsvelden |  | nee: uitbreiding op het GEMMA-kennismodel | Doelgroepindeling |
