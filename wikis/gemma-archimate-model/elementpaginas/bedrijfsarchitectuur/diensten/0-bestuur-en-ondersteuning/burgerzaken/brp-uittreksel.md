---
id: brp-uittreksel
type: dienst
archimate_type: business-service
status: review
naam: BRP-uittreksel
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Een gewaarmerkt uittreksel met de eigen gegevens uit de basisregistratie personen, als officieel bewijs van inschrijving.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Uittreksel BRP (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp
---

# BRP-uittreksel

<!-- Gegenereerd door tools/render.py uit de beoordeling brp-uittreksel.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Een gewaarmerkt uittreksel met de eigen gegevens uit de basisregistratie personen, als officieel bewijs van inschrijving.

### Beschrijving

Een uitdraai van de persoonslijst is alleen voor eigen gebruik en geen bewijs van inschrijving; een officieel bewijs is een gewaarmerkt uittreksel uit de BRP (Utrecht Persoonsgegevens bekijken). Grondslag is art. 2.55 Wet BRP (UPL nr. 93).

### Synoniemen

| Synoniem | Context |
|---|---|
| Uittreksel BRP | beleid |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Verstrekken persoonsgegevens](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) |

### Specialisaties

- **Uittreksel RNI**: Uittreksel uit de RNI voor wie erin staat, gestuurd naar het adres in de RNI (Utrecht RNI). Geen eigen pagina: de UPL noemt het niet apart.

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | BRP-uittreksel | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 93 (GEMMA-domein Publieksdiensten)) |
| [Verstrekken persoonsgegevens](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md) | realiseert *realisatie* | BRP-uittreksel | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) (UPL nr. 93) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | BRP-uittreksel | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 93, art. 2.55) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) | Schema verzoeken om schriftelijke gegevensverstrekking uit de BRP |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
