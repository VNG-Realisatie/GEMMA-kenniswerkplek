---
id: verhuismelding
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Verhuismelding
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het doorgeven van een verhuizing binnen of naar de gemeente, zodat het nieuwe adres in de basisregistratie personen komt.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Verhuizing doorgeven (beleid)
- Aangifte van adreswijziging (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-verhuizing-doorgeven
- 2026-rvig-hup-binnengemeentelijke-adreswijziging
- 2026-rvig-hup-verblijfplaats
---

# Verhuismelding

<!-- Gegenereerd door tools/render.py uit de beoordeling verhuismelding.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het doorgeven van een verhuizing binnen of naar de gemeente, zodat het nieuwe adres in de basisregistratie personen komt.

### Beschrijving

De verhuizing wordt doorgegeven vanaf vier weken voor tot vijf dagen na de verhuisdatum, online met DigiD, per post of aan de balie; de gemeente past de gegevens binnen ongeveer een week aan en geeft de verhuizing door aan organisaties (Utrecht Verhuizing doorgeven). Grondslag is art. 2.39 Wet BRP (UPL nr. 424).

### Synoniemen

| Synoniem | Context |
|---|---|
| Verhuizing doorgeven | beleid |
| Aangifte van adreswijziging | wet |

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
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een aangepast adres in de BRP, doorgegeven aan organisaties (Utrecht Verhuizing doorgeven). [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger (UPL nr. 424): iedereen vanaf 16 jaar, en ouders voor hun kinderen (Utrecht). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Verwerken adreswijziging](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (UPL nr. 424); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verhuismelding | bedient *bediening* | [Aangever](../../../rollen/aangever.md) | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | Verhuismelding | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 424 (GEMMA-domein Publieksdiensten)) |
| [Verwerken adreswijziging](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md) | realiseert *realisatie* | Verhuismelding | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 424; Wet BRP art. 2.39) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Verhuismelding | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 424, art. 2.39) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) | Gemeente Utrecht: Verhuizing doorgeven |
| [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) | HUP BRP: Binnengemeentelijke adreswijziging |
| [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
