---
id: trouwlocatie
type: dienst
archimate_type: business-service
status: review
naam: Trouwlocatie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het kiezen of laten goedkeuren van de locatie waar een huwelijk of partnerschap wordt voltrokken.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-trouwlocaties-in-utrecht
- 2026-rijk-burgerlijk-wetboek-boek-1
---

# Trouwlocatie

<!-- Gegenereerd door tools/render.py uit de beoordeling trouwlocatie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het kiezen of laten goedkeuren van de locatie waar een huwelijk of partnerschap wordt voltrokken.

### Beschrijving

Drie soorten: eigen locaties van de gemeente, vaste door de gemeente goedgekeurde trouwlocaties en een locatie naar keuze binnen de gemeente, aan te vragen uiterlijk zes weken voor de datum (Utrecht). De individuele locaties zijn lokaal. Grondslag art. 63 BW 1; digitaal kanaal (UPL nr. 414).

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een goedgekeurde locatie voor de voltrekking (Utrecht). [Utrecht Trouwlocaties](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwlocaties-in-utrecht.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Trouwlocaties](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwlocaties-in-utrecht.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger en bedrijf (UPL nr. 414): het paar en de eigenaar van een locatie. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Trouwlocaties](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwlocaties-in-utrecht.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Voltrekken huwelijk](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (nr. 414); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Burgerlijk Wetboek Boek 1](../../../../motivatie/beleidskaders/rijksregelgeving/burgerlijk-wetboek-boek-1.md) | is grondslag voor *associatie (gericht)* | Trouwlocatie | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 414, art. 63) |
| [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md) | omvat *aggregatie* | Trouwlocatie | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 414 (GEMMA-domein Publieksdiensten)) |
| [Voltrekken huwelijk](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/voltrekken-huwelijk.md) | realiseert *realisatie* | Trouwlocatie | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Trouwlocaties](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwlocaties-in-utrecht.md) (UPL nr. 414) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Trouwlocaties](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwlocaties-in-utrecht.md) | Gemeente Utrecht: Trouwlocaties |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
