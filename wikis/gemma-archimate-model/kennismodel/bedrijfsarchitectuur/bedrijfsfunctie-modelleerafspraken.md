---
id: bedrijfsfunctie-modelleerafspraken
type: kennismodel
titel: Bedrijfsfunctie — modelleerafspraken
gegenereerd: tools/kennismodel.py
---

# Bedrijfsfunctie — modelleerafspraken

*Business Function* in ArchiMate · laag Bedrijfsarchitectuur · vak `bedrijf/gedrag-intern` · paginatype `bedrijfsfunctie`

| Afspraak | Inhoud |
|---|---|
| Definitie | Activiteiten die zijn gegroepeerd omdat daarvoor vergelijkbare bedrijfsmiddelen, kennis of competenties nodig zijn. (GEMMA) |
| In Over GEMMA | ja (Bedrijfsfunctie) |
| Duiding | Doorlopende groepering van gedrag; bedient processen. Niet "wat de gemeente kan": dat is een vermogen. |
| Herken je aan | *gedrag* en *gegroepeerd gedrag*. Moet ja: *bedient gedrag* (kernrelatie); hoogstens 1 nee: *toegewezen partij*, *gebruikt objecten*, *stabiel over tijd*, *in functie-indeling*. Zie [kenmerken en beslistabel](../kenmerken-en-beslistabel.md). |
| Kernrelatie | Bedrijfsfunctie ─bediening→ Bedrijfsproces |
| Eigenschappen | `domein` (verplicht) · `gemma_functie` · `gemma` ([betekenis](../README.md#eigenschappen)) |
| Indelingen | [Functie-indeling naar domein](../indelingen.md) |
| Naamvorm | een zelfstandig naamwoord voor een doorlopend gebied van gedrag, vaak op -ing, -beheer of -verlening (Vergunningverlening); een functie en een proces hebben nooit dezelfde naam |
| Afstemming | GGM: geen match: het GGM modelleert gegevens · GEMMA-model: bij voorkeur een exacte match met een GEMMA-functie; een functie zonder match breidt de GEMMA-functieketen uit |
| Voorbeeld | wel: Exploiteren van begraafplaatsen; Burgerlijke stand diensten · niet: Lijkbezorging als functie; aanslag opleggen |

## Afspraken

- Een bedrijfsfunctie heeft geen eigen wettelijke bron nodig: zij volgt de grondslag van de diensten en processen die zij omvat of bedient. Wat zij is, steunt op de wet die de groep taken aan de gemeente toewijst, niet op GEMMA (regel Bronvoorrang).
- Een bladfunctie van GEMMA die een proces van een onderwerp bedient, met een bron, wordt een element met een exacte match; een functie erboven is een knoop van de functiehiërarchie zonder beoordeling, en het element hangt eronder met `gemma_functie` (met de GEMMA-relatie). Een proces mag door meer functies worden bediend.

## Relaties

| Relatie | Naar | Namen | Kern | In Over GEMMA | Toelichting |
|---|---|---|---|---|---|
| toegang | [Bedrijfsobject](bedrijfsobject-modelleerafspraken.md) | een [handeling](../README.md#relatietypen) | *wordt bewerkt* | ja |  |
| realisatie | [Dienst](dienst-modelleerafspraken.md) | realiseert | *gerealiseerd door* | ja |  |
| bediening | [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) | bedient | *bedient gedrag* | ja |  |
| aggregatie | [Bedrijfsfunctie](bedrijfsfunctie-modelleerafspraken.md) | omvat |  | ja | de GEMMA-functieketen |
| aggregatie | [Dienst](dienst-modelleerafspraken.md) | omvat |  | nee | Functie-indeling naar domein |

Inkomend, bij het brontype: [Bedrijfssamenwerking](bedrijfssamenwerking-modelleerafspraken.md) (toewijzing); [Rol](rol-modelleerafspraken.md) (toewijzing); [Bedrijfsproces](bedrijfsproces-modelleerafspraken.md) (bediening); [Groepering](../overig/groepering-modelleerafspraken.md) (aggregatie).
