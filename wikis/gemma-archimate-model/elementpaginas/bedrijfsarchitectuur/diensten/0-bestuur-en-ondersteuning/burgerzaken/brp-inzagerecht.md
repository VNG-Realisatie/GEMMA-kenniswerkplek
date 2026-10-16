---
id: brp-inzagerecht
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: BRP-inzagerecht
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Inzage voor de ingeschrevene in zijn eigen gegevens in de basisregistratie personen.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Persoonsgegevens BRP bekijken (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp
- 2026-rijk-besluit-brp-bwbr0034306
- 2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen
---

# BRP-inzagerecht

<!-- Gegenereerd door tools/render.py uit de beoordeling brp-inzagerecht.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Inzage voor de ingeschrevene in zijn eigen gegevens in de basisregistratie personen.

### Beschrijving

De ingeschrevene kan zijn gegevens ook zelf bekijken op MijnOverheid, een landelijke voorziening (Utrecht Persoonsgegevens bekijken). Grondslag is art. 2.55 Wet BRP; het college voldoet binnen vier weken aan het verzoek (UPL nr. 91).

### Synoniemen

| Synoniem | Context |
|---|---|
| Persoonsgegevens BRP bekijken | beleid |

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
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, inzage in of een kopie van de eigen persoonsgegevens (UPL nr. 91; Utrecht Persoonsgegevens bekijken). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger (UPL nr. 91): de ingeschrevene. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Verstrekken persoonsgegevens](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (UPL nr. 91); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | BRP-inzagerecht | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 91 (GEMMA-domein Publieksdiensten)) |
| [Verstrekken persoonsgegevens](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md) | realiseert *realisatie* | BRP-inzagerecht | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 91) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | BRP-inzagerecht | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 91, art. 2.55) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) | Schema verzoeken om schriftelijke gegevensverstrekking uit de BRP |
| [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |
| [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) | Gemeente Utrecht: Persoonsgegevens bekijken of aanvragen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
