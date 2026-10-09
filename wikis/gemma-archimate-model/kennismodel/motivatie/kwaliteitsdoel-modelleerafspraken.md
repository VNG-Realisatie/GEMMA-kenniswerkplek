---
id: kwaliteitsdoel-modelleerafspraken
type: kennismodel
titel: Kwaliteitsdoel — modelleerafspraken
---

# Kwaliteitsdoel — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Goal* in ArchiMate · laag Motivatie · geen pagina (matchdoel (GEMMA))

| Afspraak | Inhoud |
|---|---|
| Definitie | Gewenste kenmerken van overheidsdienstverlening vanuit het perspectief van de wensen van de samenleving, de burgers en bedrijven. (NORA) |
| In Over GEMMA | ja (Kwaliteitsdoel) |
| Duiding | Geen begrip uit een bron: de kwaliteitsdoelen staan vast in GEMMA (uit NORA en GEMMA). De wiki legt alleen vast welke beleidskaders er grondslag aan geven, en hoe sterk. Een doel van één beleidsveld (armoedebestrijding) is geen kwaliteitsdoel en geen element. |
| Naamvorm | de naam uit GEMMA, letterlijk (Privacy, Rechtmatig) |
| Afstemming | GEMMA-model: een kwaliteitsdoel van GEMMA (GEMMA type Kwaliteitsdoel), op id; de wiki maakt er geen nieuw |
| Voorbeeld | wel: Privacy (de AVG geeft er grondslag aan) · niet: armoedebestrijding (een beleidsdoel) |

## Afspraken

- Een kwaliteitsdoel krijgt geen pagina en geen beoordeling; het beleidskader noemt het in `kwaliteitsdoelen`, met het GEMMA-id, de sterkte, een onderbouwing en de bronnen.
- Sterkte: `++` bindend: de regeling stelt eisen of normen voor het doel; `+` draagt bij: de regeling bevordert het doel; `-` beperkt: de regeling staat het doel deels in de weg; `--` staat haaks: de regeling gaat tegen het doel in.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | invloed | [Beleidskader](beleidskader-modelleerafspraken.md) | geeft grondslag aan |  | ja | met een sterkte; het kwaliteitsdoel is een element van GEMMA (veld `kwaliteitsdoelen`) |
