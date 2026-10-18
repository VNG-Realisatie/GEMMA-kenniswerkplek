---
id: volmachtbewijs-verkiezingen
type: dienst
archimate_type: business-service
status: review
naam: Volmachtbewijs verkiezingen
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het aanvragen van een volmacht, zodat een andere kiezer met een volmachtbewijs namens de aanvrager stemt.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Stemmen bij volmacht (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-kieswet-bwbr0004627
---

# Volmachtbewijs verkiezingen

<!-- Gegenereerd door tools/render.py uit de beoordeling volmachtbewijs-verkiezingen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het aanvragen van een volmacht, zodat een andere kiezer met een volmachtbewijs namens de aanvrager stemt.

### Beschrijving

Een kiezer die niet in persoon kan stemmen, vraagt met een formulier bij de burgemeester een volmacht aan en wijst een gemachtigde aan; bij inwilliging krijgt de gemachtigde een volmachtbewijs. De kiezer kan ook zijn stempas of kiezerspas omzetten in een volmachtbewijs en aan de gemachtigde overdragen (Kieswet art. L 1, L 2, L 6, L 8, L 11, L 14). Grondslag art. L 14 en L 8 Kieswet; doelgroep burger; niet digitaal (UPL nr. 453). De volmacht is de dienst, het volmachtbewijs een onderdeel.

### Synoniemen

| Synoniem | Context |
|---|---|
| Stemmen bij volmacht | wet |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Behandelen verzoek om volmacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-volmacht.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Volmachtbewijs verkiezingen | bedient *bediening* | [Kiezer](../../../rollen/kiezer.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 8) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen verzoek om volmacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-volmacht.md) | realiseert *realisatie* | Volmachtbewijs verkiezingen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (UPL nr. 453) |
| [Kieswet](../../../../motivatie/beleidskaders/rijksregelgeving/kieswet.md) | is grondslag voor *associatie (gericht)* | Volmachtbewijs verkiezingen | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. L 8, L 14; UPL nr. 453) |
| [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md) | omvat *aggregatie* | Volmachtbewijs verkiezingen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 453 (GEMMA-domein Publieksdiensten)) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
