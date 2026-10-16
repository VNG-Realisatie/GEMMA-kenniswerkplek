---
id: naamgebruik-verzoek-aanduiding
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Naamgebruik verzoek aanduiding
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: 'Het kiezen welke achternaam de overheid gebruikt na een huwelijk of geregistreerd partnerschap: de eigen, die van de partner of een combinatie.'
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Achternaamgebruik veranderen (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-achternaamgebruik-veranderen
- 2026-rvig-hup-wijziging-naamgebruik
---

# Naamgebruik verzoek aanduiding

<!-- Gegenereerd door tools/render.py uit de beoordeling naamgebruik-verzoek-aanduiding.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het kiezen welke achternaam de overheid gebruikt na een huwelijk of geregistreerd partnerschap: de eigen, die van de partner of een combinatie.

### Beschrijving

Online, aan de balie op afspraak of schriftelijk met het formulier Verzoek naamgebruik (Utrecht). Grondslag in de UPL: art. 2.25 Wet BRP (nr. 257); het naamgebruik zelf regelt BW 1 art. 9.

### Synoniemen

| Synoniem | Context |
|---|---|
| Achternaamgebruik veranderen | beleid |

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
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, het gekozen naamgebruik in de BRP, binnen vijf werkdagen verwerkt (Utrecht). [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger (UPL nr. 257): wie getrouwd of geregistreerd partner is of was. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Wijzigen naamgebruik](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-naamgebruik.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (nr. 257); geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bevolkingsadministratie bijhouding](../../../bedrijfsfuncties/publieksdiensten/bevolkingsadministratie-bijhouding.md) | omvat *aggregatie* | Naamgebruik verzoek aanduiding | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 257 (GEMMA-domein Publieksdiensten)) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Naamgebruik verzoek aanduiding | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 257, art. 2.25) |
| [Wijzigen naamgebruik](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-naamgebruik.md) | realiseert *realisatie* | Naamgebruik verzoek aanduiding | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 257; Wet BRP art. 2.25) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md) | Gemeente Utrecht: Achternaamgebruik |
| [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) | HUP BRP: Wijziging naamgebruik |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
