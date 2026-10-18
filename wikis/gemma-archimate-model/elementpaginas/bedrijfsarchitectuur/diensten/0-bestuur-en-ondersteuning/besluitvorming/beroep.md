---
id: beroep
type: dienst
archimate_type: business-service
status: review
naam: Beroep
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Het instellen van beroep bij de bestuursrechter tegen een besluit van de gemeente.
match:
  gemma: geen
afnemer: extern
domein: Bestuur
synoniemen:
- Beroep instellen (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
---

# Beroep

<!-- Gegenereerd door tools/render.py uit de beoordeling beroep.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het instellen van beroep bij de bestuursrechter tegen een besluit van de gemeente.

### Beschrijving

Een belanghebbende kan tegen een besluit beroep instellen bij de bestuursrechter, door binnen zes weken een beroepschrift bij die rechter in te dienen (Awb art. 8:1, 6:4 lid 3, 6:7). Meestal gaat bezwaar vooraf; tegen de beslissing op bezwaar staat dan beroep open, en na de uniforme openbare voorbereidingsprocedure gaat de belanghebbende direct in beroep (art. 7:1). Bij de bekendmaking van een besluit vermeldt de gemeente of en waar beroep openstaat (art. 3:45). De bestuursrechter behandelt het beroep; de gemeente is partij: zij zendt binnen vier weken de stukken, kan een verweerschrift indienen, en neemt een nieuw besluit als de rechter het besluit vernietigt en dat opdraagt (art. 8:42, 8:72). De UPL noemt de dienst voor burgers en bedrijven (nr. 54).

### Synoniemen

| Synoniem | Context |
|---|---|
| Beroep instellen | wet |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Afnemer**: extern.
- **Domein**: Bestuur.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Voeren verweer in beroep](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/voeren-verweer-in-beroep.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Algemene wet bestuursrecht](../../../../motivatie/beleidskaders/rijksregelgeving/algemene-wet-bestuursrecht.md) | is grondslag voor *associatie (gericht)* | Beroep | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 8:1) |
| [Voeren verweer in beroep](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/voeren-verweer-in-beroep.md) | realiseert *realisatie* | Beroep | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 8:1, 8:42; UPL nr. 54) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst en geen proces voor beroep; alleen de functie Bezwaar- en beroepafhandeling. Nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 26](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (product, open): **UPL:** beroep is een gemeentelijk product met grondslag art. 8:1 Awb, domein Bestuur ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 54; Logius: ook voor gemeenten). De interne lijst noemt Beroep behandelen als ondersteunend proces ([2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md), nr. 33). **Bevinding:** het beroep wordt ingesteld bij en behandeld door de bestuursrechter, niet door de gemeente ([2026-rijk-algemene-wet-bestuursrecht-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), art. 6:4 lid 3, 8:1). De gemeente is partij: zij zendt binnen vier weken de stukken en kan een verweerschrift indienen, en neemt een nieuw besluit als de rechter dat opdraagt (art. 8:42, 8:72 lid 4). GEMMA houdt de dienst Beroep, omdat een UPL-product niet wegvalt, en laat haar realiseren door het proces Voeren verweer in beroep, het deel van de gemeente; de bestuursrechter is geen element. **Voorstel:** vermeld bij het UPL-product dat de bestuursrechter het beroep behandelt en dat de gemeente partij is (stukken, verweer, uitvoeren van de uitspraak), en noem art. 8:42 naast art. 8:1 als grondslag voor de taak van de gemeente. Noem het interne proces Voeren verweer in beroep in plaats van Beroep behandelen.
