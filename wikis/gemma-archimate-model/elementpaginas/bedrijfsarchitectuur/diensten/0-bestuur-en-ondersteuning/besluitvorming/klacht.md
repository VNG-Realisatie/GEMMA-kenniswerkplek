---
id: klacht
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Klacht
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Het indienen van een klacht over de manier waarop een bestuursorgaan of een medewerker zich heeft gedragen.
match:
  gemma: geen
afnemer: extern
domein: Bestuur
synoniemen:
- Klacht indienen (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
---

# Klacht

<!-- Gegenereerd door tools/render.py uit de beoordeling klacht.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het indienen van een klacht over de manier waarop een bestuursorgaan of een medewerker zich heeft gedragen.

### Beschrijving

Ieder heeft het recht een klacht in te dienen bij een bestuursorgaan over de manier waarop het zich jegens hem of een ander heeft gedragen; de gedraging van een medewerker geldt als gedraging van het bestuursorgaan (Awb art. 9:1). Het bestuursorgaan behandelt mondelinge en schriftelijke klachten behoorlijk (art. 9:2); voor een schriftelijke klacht gelden vaste regels: ontvangstbevestiging, horen, afhandeling binnen zes weken en een gemotiveerd oordeel, waarna de klager zich tot de ombudsman kan wenden (art. 9:4–9:12). Tegen het oordeel staat geen beroep open (art. 9:3). De UPL noemt de dienst voor burgers en bedrijven (nr. 212).

### Synoniemen

| Synoniem | Context |
|---|---|
| Klacht indienen | wet |

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
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Behandelen klacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-klacht.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Algemene wet bestuursrecht](../../../../motivatie/beleidskaders/rijksregelgeving/algemene-wet-bestuursrecht.md) | is grondslag voor *associatie (gericht)* | Klacht | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 9:1, 9:2) |
| [Behandelen klacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-klacht.md) | realiseert *realisatie* | Klacht | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 9:1; UPL nr. 212) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst klacht; wel het bedrijfsproces Behandelen klacht, dat de wiki koppelt aan het realiserende proces. Nieuw voor GEMMA.
