---
id: bedrijfsfunctie-modelleerafspraken
type: kennismodel
titel: Bedrijfsfunctie — modelleerafspraken
---

# Bedrijfsfunctie — modelleerafspraken

<!-- Gegenereerd door tools/kennismodel.py; wijzig de bron, niet deze pagina. -->

*Business Function* in ArchiMate · laag Bedrijfsarchitectuur · paginatype `bedrijfsfunctie`

| Afspraak | Inhoud |
|---|---|
| Definitie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. (GEMMA) |
| In Over GEMMA | ja (Bedrijfsfunctie) |
| Duiding | Doorlopende groepering van gedrag; bedient processen. Niet "wat de gemeente kan": dat is een vermogen. |
| Herken je aan | *gedrag* en *gegroepeerd gedrag*. Moet ja: *bedient gedrag* (kernrelatie); hoogstens 1 nee: *toegewezen partij*, *gebruikt objecten*, *stabiel over tijd*, *in functie-indeling*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsfunctie ─bediening→ Bedrijfsproces |
| Eigenschappen | `domein` (verplicht): het GEMMA-domein, de plaats in de Functie-indeling naar domein (Bestuur, Fysieke leefomgeving, Niet domeingebonden, Openbare orde en veiligheid, Ondersteuning, Publieksdiensten, Sociaal domein) · `gemma`: de match met het GEMMA-model: het id gaat mee in de export |
| Indelingen | [Functie-indeling naar domein](../indelingen.md) |
| Naamvorm | een zelfstandig naamwoord voor een doorlopend gebied van gedrag, vaak op -ing, -beheer of -verlening (Vergunningverlening); een functie en een proces hebben nooit dezelfde naam |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: bij voorkeur een exacte match met een GEMMA-functie; een functie zonder match breidt de GEMMA-functieketen uit |
| Voorbeeld | wel: Exploiteren van begraafplaatsen; Burgerlijke stand diensten · niet: Lijkbezorging als functie; aanslag opleggen |

## Afspraken

- Een bedrijfsfunctie heeft geen eigen wettelijke bron nodig: zij volgt de grondslag van de diensten en processen die zij omvat, en vervalt alleen als zij niets meer omvat.
- Bedienende GEMMA-functies worden een element met een exacte match; een proces mag door meer functies worden bediend.

## Relaties

In het kennismodel van de wiki; ze gaan mee in de export. *In Over GEMMA* nee betekent: een uitbreiding op het GEMMA-kennismodel, in de export gemarkeerd en een kandidaat voor een terugmelding over het kennismodel.

| Richting | Relatie | Ander type | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|---|
| in | toewijzing | [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | nee: uitbreiding op het GEMMA-kennismodel |  |
| in | toewijzing | [Rol](rol-modelleerafspraken.md) | vrij, uit de bron | *voert gedrag uit* | ja |  |
| uit | toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een handeling: registreren (schrijven), bijwerken (lezen-schrijven), beëindigen (schrijven), raadplegen (lezen), verstrekken (lezen), bewaren (lezen-schrijven), overbrengen (lezen), vernietigen (schrijven) | *wordt bewerkt* | ja |  |
| uit | realisatie | [Dienst](dienst-modelleerafspraken.md) | realiseert | *gerealiseerd door* | ja |  |
| uit | bediening | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | bedient | *bedient gedrag* | ja |  |
| in | bediening | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | bedient |  | ja |  |
| uit | aggregatie | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | omvat |  | ja | de GEMMA-functieketen |
| uit | aggregatie | [Dienst](dienst-modelleerafspraken.md) | omvat |  | nee: uitbreiding op het GEMMA-kennismodel | Functie-indeling naar domein |

## Weggefilterd

Niet in het kennismodel van de wiki, ook al is de relatie in ArchiMate geldig; de export laat haar weg. Een relatie die nergens in het kennismodel staat, is ook weggefilterd.

| Relatie | Reden |
|---|---|
| Actor ─toewijzing of toegang of associatie→ Bedrijfsfunctie | een actor hangt via een rol aan gedrag en objecten: actor → toewijzing → rol |
| Bedrijfsfunctie ─aggregatie of compositie→ Bedrijfsproces | een functie bedient een proces; processen groeperen in een cluster naar soort werk |
