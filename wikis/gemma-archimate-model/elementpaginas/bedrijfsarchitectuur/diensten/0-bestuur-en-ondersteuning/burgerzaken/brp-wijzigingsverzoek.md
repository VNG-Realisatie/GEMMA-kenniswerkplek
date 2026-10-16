---
id: brp-wijzigingsverzoek
type: dienst
archimate_type: business-service
status: review
naam: BRP-wijzigingsverzoek
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verzoek om onjuiste eigen gegevens in de basisregistratie personen te laten corrigeren.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Persoonsgegevens aanpassen (beleid)
- Rectificatieverzoek (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp
- 2018-nvvb-stappenplan-identiteitswijziging-brp
---

# BRP-wijzigingsverzoek

<!-- Gegenereerd door tools/render.py uit de beoordeling brp-wijzigingsverzoek.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het verzoek om onjuiste eigen gegevens in de basisregistratie personen te laten corrigeren.

### Beschrijving

Adresgegevens aanpassen kan online of per post, persoonsgegevens zoals naam, geslacht en geboortedatum alleen persoonlijk of per post, met bewijsstukken (Utrecht Persoonsgegevens aanpassen). Grondslag is art. 2.58 Wet BRP; de aanvraag kan digitaal (UPL nr. 95).

### Synoniemen

| Synoniem | Context |
|---|---|
| Persoonsgegevens aanpassen | beleid |
| Rectificatieverzoek | beleid |

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
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, gecorrigeerde gegevens of een gemotiveerde weigering (Utrecht; NVVB Identiteitswijziging). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger (UPL nr. 95). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Behandelen verzoek om correctie](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-correctie.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (UPL nr. 95); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen verzoek om correctie](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-correctie.md) | realiseert *realisatie* | BRP-wijzigingsverzoek | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 95; Wet BRP art. 2.58) |
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | BRP-wijzigingsverzoek | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 95 (GEMMA-domein Publieksdiensten)) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | BRP-wijzigingsverzoek | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 95, art. 2.58) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) | Gemeente Utrecht: Persoonsgegevens opvragen of aanpassen |
| [NVVB Stappenplan identiteitswijziging BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2018-nvvb-stappenplan-identiteitswijziging-brp.md) | NVVB: Stappenplan identiteitswijziging in de BRP |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
