---
id: aangifte-vertrek-buitenland
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Aangifte vertrek buitenland
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het doorgeven aan de gemeente van een vertrek naar het buitenland voor acht maanden of langer per jaar.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Emigratie doorgeven (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-emigratie-doorgeven
- 2026-rvig-hup-emigratie
- 2026-rvig-hup-verblijfplaats
---

# Aangifte vertrek buitenland

<!-- Gegenereerd door tools/render.py uit de beoordeling aangifte-vertrek-buitenland.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het doorgeven aan de gemeente van een vertrek naar het buitenland voor acht maanden of langer per jaar.

### Beschrijving

Emigratie wordt doorgegeven online, aan de balie op afspraak of schriftelijk; de gemeente verwerkt haar binnen een week en geeft haar door aan andere instanties (Utrecht Emigratie doorgeven). Grondslag is art. 2.43 Wet BRP (UPL nr. 1).

### Synoniemen

| Synoniem | Context |
|---|---|
| Emigratie doorgeven | beleid |

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
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Verwerken emigratie](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Aangifte vertrek buitenland | bedient *bediening* | [Aangever](../../../rollen/aangever.md) | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | Aangifte vertrek buitenland | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 1 (GEMMA-domein Publieksdiensten)) |
| [Verwerken emigratie](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md) | realiseert *realisatie* | Aangifte vertrek buitenland | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) (UPL nr. 1) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Aangifte vertrek buitenland | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 1, art. 2.43) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Emigratie doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) | Gemeente Utrecht: Emigratie doorgeven |
| [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |
| [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
