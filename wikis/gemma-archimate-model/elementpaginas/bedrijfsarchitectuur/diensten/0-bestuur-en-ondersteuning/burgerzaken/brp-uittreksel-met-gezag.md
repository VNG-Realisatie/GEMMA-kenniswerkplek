---
id: brp-uittreksel-met-gezag
type: dienst
archimate_type: business-service
status: review
naam: BRP-uittreksel met gezag
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Een uittreksel uit de basisregistratie personen met de gegevens over het gezag over een minderjarige.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-nvvb-handreiking-gezag
- 2026-utrecht-burgerzaken-ouderlijk-gezag-aanvragen
- 2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp
---

# BRP-uittreksel met gezag

<!-- Gegenereerd door tools/render.py uit de beoordeling brp-uittreksel-met-gezag.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Een uittreksel uit de basisregistratie personen met de gegevens over het gezag over een minderjarige.

### Beschrijving

Grondslag is art. 2.55 Wet BRP (UPL nr. 94). De UPL noemt het apart van het BRP-uittreksel; daarom is het een eigen dienst. Het gezag zelf komt uit het gezagsregister van de rechtbank en wordt in de BRP overgenomen; een uittreksel met gezag kan alleen als een gezaghouder uit de BRP-gegevens is af te leiden (NVVB Handreiking gezag). Utrecht geeft het op afspraak af, niet via DigiD (Utrecht Ouderlijk gezag aanvragen).

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een uittreksel uit de BRP met de gegevens over het gezag (UPL nr. 94). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger (UPL nr. 94). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Verstrekken persoonsgegevens](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (UPL nr. 94); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | BRP-uittreksel met gezag | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 94 (GEMMA-domein Publieksdiensten)) |
| [Verstrekken persoonsgegevens](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md) | realiseert *realisatie* | BRP-uittreksel met gezag | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 94) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | BRP-uittreksel met gezag | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 94, art. 2.55) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [NVVB Handreiking Gezag](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-nvvb-handreiking-gezag.md) | NVVB: Gezag |
| [Utrecht Ouderlijk gezag aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-ouderlijk-gezag-aanvragen.md) | Gemeente Utrecht: Ouderlijk gezag |
| [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) | Schema verzoeken om schriftelijke gegevensverstrekking uit de BRP |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
