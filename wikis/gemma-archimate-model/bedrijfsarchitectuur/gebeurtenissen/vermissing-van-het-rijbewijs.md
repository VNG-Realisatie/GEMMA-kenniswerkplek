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
grondslag: bron
match:
  gemma: geen
data_object: nee
synoniemen:
- Aangifte van vermissing van het rijbewijs (wet)
bronnen:
- 2026-rijk-wegenverkeerswet-1994-bwbr0006622
- 2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen
---

# Vermissing van het rijbewijs

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/vermissing-van-het-rijbewijs.yaml. Wijzig de beoordeling, niet deze pagina. -->

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

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Verwerken vermissing rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-rijbewijs.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 50 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, wetsbegrip aangifte van vermissing van het rijbewijs (Wegenverkeerswet 1994 art. 123 lid 1 onder h); gangbaar: rijbewijs kwijt of gestolen (Utrecht). [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de houder geeft de vermissing door aan de RDW of aan de balie van de gemeente, die haar opneemt (Utrecht). [Utrecht Rijbewijs aanvragen of verlengen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij burgerzaken: de toestand van het rijbewijs verandert (regel Thuishoren). [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, het moment waarop de houder niet meer over zijn rijbewijs beschikt, doordat het kwijt of gestolen is; door de aangifte vervalt de geldigheid (Wegenverkeerswet 1994 art. 123 lid 1 onder h). [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk rijbewijs dat kwijtraakt of wordt gestolen. [Utrecht Rijbewijs aanvragen of verlengen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start Verwerken vermissing rijbewijs: de houder geeft de vermissing zo snel mogelijk door, om misbruik te voorkomen (Utrecht). [Utrecht Rijbewijs aanvragen of verlengen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vermissing van het rijbewijs | leidt tot *triggering* | [Verwerken vermissing rijbewijs](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-rijbewijs.md) | [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (WVW art. 123 lid 1 onder h; Utrecht regel 126-140) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren rijbewijzen](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-rijbewijzen.md) | omvat *aggregatie* | Vermissing van het rijbewijs | [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (art. 123 lid 1 onder h) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wegenverkeerswet 1994](../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) | Wegenverkeerswet 1994 |
| [Utrecht Rijbewijs aanvragen of verlengen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) | Gemeente Utrecht: Rijbewijs aanvragen of verlengen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
