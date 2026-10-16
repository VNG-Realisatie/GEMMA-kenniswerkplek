---
id: brp-geheimhoudingsverzoek
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: BRP-geheimhoudingsverzoek
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verzoek om persoonsgegevens uit de basisregistratie personen niet aan bepaalde derden te verstrekken, of om dat stop te zetten.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Persoonsgegevens geheimhouden (beleid)
- Verzoek om verstrekkingsbeperking (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden
- 2026-rvig-hup-verstrekkingsbeperking
---

# BRP-geheimhoudingsverzoek

<!-- Gegenereerd door tools/render.py uit de beoordeling brp-geheimhoudingsverzoek.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het verzoek om persoonsgegevens uit de basisregistratie personen niet aan bepaalde derden te verstrekken, of om dat stop te zetten.

### Beschrijving

Met geheimhouding krijgen onder meer advocaten, niet-commerciële instellingen en de Stichting Interkerkelijke Ledenadministratie geen gegevens zonder toestemming; instellingen met een wettelijke taak krijgen ze wel. De aanvraag kan online met DigiD of schriftelijk, en de geheimhouding gaat mee bij een verhuizing (Utrecht Persoonsgegevens geheimhouden). Grondslag is art. 2.59 Wet BRP (UPL nr. 87).

### Synoniemen

| Synoniem | Context |
|---|---|
| Persoonsgegevens geheimhouden | beleid |
| Verzoek om verstrekkingsbeperking | wet |

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
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, geen verstrekking van gegevens aan bepaalde derden zonder toestemming (Utrecht). [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md), [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger (UPL nr. 87): de ingeschrevene van 16 jaar of ouder (HUP Verstrekkingsbeperking). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Behandelen verzoek om geheimhouding](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-geheimhouding.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (UPL nr. 87); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen verzoek om geheimhouding](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-geheimhouding.md) | realiseert *realisatie* | BRP-geheimhoudingsverzoek | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 87; Wet BRP art. 2.59) |
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | BRP-geheimhoudingsverzoek | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 87 (GEMMA-domein Publieksdiensten)) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | BRP-geheimhoudingsverzoek | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 87, art. 2.59) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md) | Gemeente Utrecht: Persoonsgegevens geheimhouden |
| [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) | HUP BRP: Verstrekkingsbeperking |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
