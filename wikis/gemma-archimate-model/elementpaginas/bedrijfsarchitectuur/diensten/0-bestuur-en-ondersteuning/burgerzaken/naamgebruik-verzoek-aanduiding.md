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
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Wijzigen naamgebruik](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-naamgebruik.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) |

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
