---
id: geregistreerd-partnerschap-ontbinding
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Geregistreerd partnerschap ontbinding
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het laten inschrijven van de beëindiging van een geregistreerd partnerschap.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Geregistreerd partnerschap beëindigen (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen
- 2026-rijk-burgerlijk-wetboek-boek-1
---

# Geregistreerd partnerschap ontbinding

<!-- Gegenereerd door tools/render.py uit de beoordeling geregistreerd-partnerschap-ontbinding.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het laten inschrijven van de beëindiging van een geregistreerd partnerschap.

### Beschrijving

Met wederzijds goedvinden met een verklaring van advocaten of notarissen, anders via de rechtbank (BW 1 art. 80c; Utrecht). Grondslag art. 80c BW 1 (UPL nr. 157).

### Synoniemen

| Synoniem | Context |
|---|---|
| Geregistreerd partnerschap beëindigen | beleid |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Inschrijven ontbinding huwelijk of partnerschap](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ontbinding-huwelijk-of-partnerschap.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Burgerlijk Wetboek Boek 1](../../../../motivatie/beleidskaders/rijksregelgeving/burgerlijk-wetboek-boek-1.md) | is grondslag voor *associatie (gericht)* | Geregistreerd partnerschap ontbinding | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 157, art. 80c) |
| [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md) | omvat *aggregatie* | Geregistreerd partnerschap ontbinding | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 157 (GEMMA-domein Publieksdiensten)) |
| [Inschrijven ontbinding huwelijk of partnerschap](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ontbinding-huwelijk-of-partnerschap.md) | realiseert *realisatie* | Geregistreerd partnerschap ontbinding | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md) (UPL nr. 157) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md) | Gemeente Utrecht: Scheiden of geregistreerd partnerschap beëindigen |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
