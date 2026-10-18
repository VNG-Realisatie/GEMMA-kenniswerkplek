---
id: brp-inschrijving-buitenlandse-akte
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: BRP-inschrijving buitenlandse akte
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het laten opnemen van een buitenlands document over een geboorte, huwelijk, overlijden, echtscheiding, erkenning of adoptie in de basisregistratie personen.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Buitenlandse documenten inschrijven (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
---

# BRP-inschrijving buitenlandse akte

<!-- Gegenereerd door tools/render.py uit de beoordeling brp-inschrijving-buitenlandse-akte.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het laten opnemen van een buitenlands document over een geboorte, huwelijk, overlijden, echtscheiding, erkenning of adoptie in de basisregistratie personen.

### Beschrijving

Op afspraak, met het gelegaliseerde en zo nodig vertaalde originele document (Utrecht). Wie Nederlander is, kan de buitenlandse akte daarna laten inschrijven in de registers van de gemeente Den Haag (BW 1 art. 25; Utrecht). Grondslag in de UPL: art. 2.38 Wet BRP (nr. 89).

### Synoniemen

| Synoniem | Context |
|---|---|
| Buitenlandse documenten inschrijven | beleid |

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
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Verwerken buitenlands document](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-buitenlands-document.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | BRP-inschrijving buitenlandse akte | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 89 (GEMMA-domein Publieksdiensten)) |
| [Verwerken buitenlands document](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-buitenlands-document.md) | realiseert *realisatie* | BRP-inschrijving buitenlandse akte | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Buitenlandse documenten inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) (UPL nr. 89) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | BRP-inschrijving buitenlandse akte | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 89, art. 2.38) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
