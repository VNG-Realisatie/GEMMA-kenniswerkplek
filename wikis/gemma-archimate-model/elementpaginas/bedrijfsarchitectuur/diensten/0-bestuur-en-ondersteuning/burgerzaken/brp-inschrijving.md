---
id: brp-inschrijving
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: BRP-inschrijving
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Inschrijving in de basisregistratie personen van wie zich vanuit het buitenland in de gemeente vestigt.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Inschrijven vanuit het buitenland (beleid)
- Aangifte van verblijf en adres (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland
- 2026-rvig-hup-immigratie
- 2026-rvig-hup-verblijfplaats
---

# BRP-inschrijving

<!-- Gegenereerd door tools/render.py uit de beoordeling brp-inschrijving.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Inschrijving in de basisregistratie personen van wie zich vanuit het buitenland in de gemeente vestigt.

### Beschrijving

Wie vanuit het buitenland in de gemeente komt wonen, maakt binnen vijf dagen een afspraak om zich in te schrijven, met identiteitsbewijs, bewijs van verblijfsrecht en eventueel buitenlandse akten; de inschrijving kan vier weken duren en levert ook een burgerservicenummer op (Utrecht Inschrijven vanuit het buitenland). Grondslag is art. 2.38 Wet BRP (UPL nr. 88).

### Synoniemen

| Synoniem | Context |
|---|---|
| Inschrijven vanuit het buitenland | beleid |
| Aangifte van verblijf en adres | wet |

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
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Inschrijven ingezetene](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| BRP-inschrijving | bedient *bediening* | [Aangever](../../../rollen/aangever.md) | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | BRP-inschrijving | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 88 (GEMMA-domein Publieksdiensten)) |
| [Inschrijven ingezetene](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | realiseert *realisatie* | BRP-inschrijving | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) (UPL nr. 88) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | BRP-inschrijving | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 88, art. 2.38) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) | Gemeente Utrecht: Inschrijven vanuit het buitenland |
| [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) | HUP BRP: Immigratie |
| [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
