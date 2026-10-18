---
id: vermissing-van-het-rijbewijs
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Vermissing van het rijbewijs
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het moment waarop de houder niet meer over zijn rijbewijs beschikt, doordat het kwijt of gestolen is.
match:
  gemma: geen
synoniemen:
- Aangifte van vermissing van het rijbewijs (wet)
bronnen:
- 2026-rijk-wegenverkeerswet-1994-bwbr0006622
- 2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen
---

# Vermissing van het rijbewijs

<!-- Gegenereerd door tools/render.py uit de beoordeling vermissing-van-het-rijbewijs.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het moment waarop de houder niet meer over zijn rijbewijs beschikt, doordat het kwijt of gestolen is.

### Beschrijving

Diefstal of beroving is een vorm van vermissing; bij diefstal of beroving adviseert Utrecht ook aangifte bij de politie te doen, wat niet verplicht is maar nodig kan zijn voor de verzekering (Utrecht). Een rijbewijs dat bij identiteitsfraude of een datalek is betrokken, laat men op dezelfde manier ongeldig maken, ook als het niet kwijt is (Utrecht).

### Synoniemen

| Synoniem | Context |
|---|---|
| Aangifte van vermissing van het rijbewijs | wet |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Verwerken vermissing rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-rijbewijs.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Verwerken vermissing rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-rijbewijs.md). [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vermissing van het rijbewijs | leidt tot *triggering* | [Verwerken vermissing rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-rijbewijs.md) | [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (WVW art. 123 lid 1 onder h; Utrecht regel 126-140) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren rijbewijzen](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-rijbewijzen.md) | omvat *aggregatie* | Vermissing van het rijbewijs | [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (art. 123 lid 1 onder h) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wegenverkeerswet 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) | Wegenverkeerswet 1994 |
| [Utrecht Rijbewijs aanvragen of verlengen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) | Gemeente Utrecht: Rijbewijs aanvragen of verlengen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
