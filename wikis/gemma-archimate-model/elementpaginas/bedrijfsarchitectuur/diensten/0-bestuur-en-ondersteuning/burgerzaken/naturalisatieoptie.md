---
id: naturalisatieoptie
type: dienst
archimate_type: business-service
status: review
naam: Naturalisatieoptie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het afleggen van een optieverklaring om door bevestiging van de burgemeester Nederlander te worden.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Nederlander worden door optie (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
---

# Naturalisatieoptie

<!-- Gegenereerd door tools/render.py uit de beoordeling naturalisatieoptie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het afleggen van een optieverklaring om door bevestiging van de burgemeester Nederlander te worden.

### Beschrijving

Wie al langer in Nederland woont of een andere optiegrond heeft, kan door optie Nederlander worden: hij verklaart dat hij Nederlander wil worden en de burgemeester beslist (Utrecht; Rijkswet op het Nederlanderschap art. 6). Aanvragen kan op afspraak aan de balie, alleen voor wie in de gemeente in de BRP staat; de gemeente rekent leges, met een verlaagde prijs bij een asielvergunning voor onbepaalde tijd of als staatloze (Utrecht). Grondslag art. 6 Rijkswet; doelgroep burger; niet digitaal, bewijs in persoon (UPL nr. 262). De UPL-naam noemt de optie een vorm van naturalisatie; in de wet zijn optie en naturalisatie twee wegen tot verkrijging (Besluit verkrijging en verlies Nederlanderschap art. 1 onder c en d; procesarchitectuur-terugmelding).

### Synoniemen

| Synoniem | Context |
|---|---|
| Nederlander worden door optie | beleid |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Nederlanderschap diensten](../../../bedrijfsfuncties/publieksdiensten/nederlanderschap-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Behandelen optieverklaring](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Naturalisatieoptie | bedient *bediening* | [Optant](../../../rollen/optant.md) | [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 3; Utrecht) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen optieverklaring](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md) | realiseert *realisatie* | Naturalisatieoptie | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (UPL nr. 262) |
| [Nederlanderschap diensten](../../../bedrijfsfuncties/publieksdiensten/nederlanderschap-diensten.md) | omvat *aggregatie* | Naturalisatieoptie | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 262 (GEMMA-domein Publieksdiensten)) |
| [Rijkswet op het Nederlanderschap](../../../../motivatie/beleidskaders/rijksregelgeving/rijkswet-op-het-nederlanderschap.md) | is grondslag voor *associatie (gericht)* | Naturalisatieoptie | [Rijkswet op het Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 6; UPL nr. 262) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Nederlander worden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) | Gemeente Utrecht: Nederlander worden door naturalisatie of optie |
| [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 13](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (product, open): **UPL:** het product heet naturalisatieoptie, met grondslag art. 6 Rijkswet op het Nederlanderschap ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 262). **Bevinding:** optie en naturalisatie zijn twee wegen tot het Nederlanderschap, met een andere beslisser en procedure: bij optie beslist de burgemeester, bij naturalisatie de Koning op voordracht van de minister ([2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), art. 1 onder c en d; [2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md)). Het product gaat over de optie; de naam naturalisatieoptie verwart de twee. GEMMA houdt de UPL-naam, met het synoniem Nederlander worden door optie. **Voorstel:** noem het product in de UPL optie of optieverklaring.
