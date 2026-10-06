---
id: burgemeester
type: actor
archimate_type: business-actor
status: goedgekeurd
naam: Burgemeester
onderwerpen:
- algemeen
- lijkbezorging
definitie: Bestuursorgaan van de gemeente, voorzitter van gemeenteraad en college, benoemd bij koninklijk besluit.
grondslag: bron
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2024-rijk-gemeentewet-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Burgemeester

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/burgemeester.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Bestuursorgaan van de gemeente, voorzitter van gemeenteraad en college, benoemd bij koninklijk besluit.

### Beschrijving

De burgemeester wordt bij koninklijk besluit benoemd voor zes jaar (Gemeentewet art. 61) en is voorzitter van de raad en van het college (art. 9, 34). De burgemeester vertegenwoordigt de gemeente in en buiten rechte (art. 171).

### Per onderwerp

#### [Lijkbezorging](../../begrippen/lijkbezorging.md)

De burgemeester draagt zorg voor de lijkbezorging als niemand daarin voorziet, verleent vergunning tot opgraving en verlof tot ontleding, stelt een andere termijn en treft maatregelen bij een besmet stoffelijk overschot (Wet op de lijkbezorging art. 17, 21, 22a, 29, 68).

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Handelende partij (kern ja).

### Plaats in de indelingen

- **Doelgroep**: gemeente.

### Kenmerken

Alleen de kenmerken met ja; de overige 50 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, bestuursorgaan van elke gemeente (Gemeentewet art. 6). [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, orgaan van de gemeente zelf; neemt besluiten in de lijkbezorging (Wlb art. 17, 21, 29, 68). [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **handelende partij**: Is het een organisatie, afdeling of persoon die activiteiten kan uitvoeren? | Ja, persoon en bestuursorgaan dat activiteiten uitvoert. [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) |
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja, bestaat los van elke afzonderlijke bevoegdheid; vervult ook andere rollen (voorzitter van raad en college, art. 9, 34). [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, vervult de rol Beslisser: verleent vergunning tot opgraving en verlof tot ontleding, draagt zorg voor de lijkbezorging als niemand dat doet, treft maatregelen bij een besmet lijk (Wlb art. 21, 22a, 29, 68). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **soort partij**: Komt deze partij met dezelfde rol bij elke gemeente voor, en is het geen individuele organisatie? | Ja, elke gemeente heeft een raad, een college van burgemeester en wethouders en een burgemeester (Gemeentewet art. 6). [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder element in deze wiki. [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt in elk onderwerp voor als bestuursorgaan (Gemeentewet art. 6). [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Burgemeester | vervult *toewijzing* | [Beslisser](../rollen/beslisser.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17, 21, 22a, 29, 68) |
| Burgemeester | is voorzitter van *associatie (gericht)* | [Gemeenteraad](gemeenteraad.md) | [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) (art. 9) |
| Burgemeester | is voorzitter van *associatie (gericht)* | [College van B&W](college-van-b-w.md) | [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) (art. 34 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Gemeente](gemeente.md) | omvat *aggregatie* | Burgemeester | [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) (art. 6) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen actor Burgemeester (tools/gemma.py kandidaten: geen naamgenoot); nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 6](../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, open): **Kennismodel:** het kennismodel procesarchitectuur kent geen relaties tussen actoren; een actor wordt alleen aan een rol toegewezen ([2026-vng-over-gemma](../../analyses/gemma-kennismodel.md), regel 602). **GEMMA:** tussen actoren alleen structurele relaties: deel van, lid van, voorzitter van. De Gemeente omvat de Gemeenteraad, het College van B&W en de Burgemeester, en de Burgemeester is voorzitter van de gemeenteraad en van het college ([2024-rijk-gemeentewet-wettekst](../../bronanalyses/lijkbezorging/2024-rijk-gemeentewet-wettekst.md), art. 6, 9, 34). Een handeling tussen partijen loopt via rollen en processen of een gebeurtenis.

### Besluiten redacteur

- 2026-10-05: Stoffelijk overschot in lopende tekst: per onderwerp lijkbezorging.
