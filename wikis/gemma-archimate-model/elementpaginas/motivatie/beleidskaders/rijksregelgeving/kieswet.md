---
id: kieswet
type: beleidskader
archimate_type: driver
status: review
naam: Kieswet
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Wet over het kiesrecht en de verkiezing van de vertegenwoordigende organen, waaronder de gemeenteraad.
match:
  gemma: geen
data_object: nee
regelgever: rijk
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2025-vng-upl-producten-en-diensten-extern
---

# Kieswet

<!-- Gegenereerd door tools/render.py uit de beoordeling kieswet.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Wet over het kiesrecht en de verkiezing van de vertegenwoordigende organen, waaronder de gemeenteraad.

### Beschrijving

De Kieswet (BWBR0004627) regelt wie kiesgerechtigd is (hoofdstuk B), de registratie van de kiesgerechtigdheid door burgemeester en wethouders (D), de stempas (J), de kiezerspas (K) en het stemmen bij volmacht (L), en daarnaast de kandidaatstelling, de stembureaus, de stemming en de uitslag, die buiten dit onderwerp vallen (afbakening Burgerzaken).

### Per onderwerp

#### [Burgerzaken](../../../../onderwerpen/burgerzaken/begrippen.md)

In Burgerzaken is geen UPL-item een product: geen enkel item bundelt diensten met een afspraak voor de afnemer (kenmerk omvat diensten en afspraken). De wet is grondslag van de diensten Stempas ontvangen, Kiezerspas, Volmachtbewijs verkiezingen en Stemrecht (UPL nr. 397, 208, 453, 398) en van de processen Beheren stempassen en Registreren kiesgerechtigdheid. De UPL-items Kandidaatstelling verkiezingen, Stembiljet en Stemmen identificatieplicht (nr. 205, 395, 396) steunen ook op de Kieswet, maar vallen buiten de afbakening en zijn verwijzingen naar een later onderwerp verkiezingen.

## Plaats in het model

### Typering

Beleidskader. Uitkomst van de beslistabel: Regeling als geheel, landelijk (kern ja, 1/1).

### Plaats in de indelingen

- **Regelgever**: rijk.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: motivatie (Beleidskader). **Hoofdkenmerk**: regeling als geheel. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **landelijk**: Geldt het voor alle gemeenten: Europese regelgeving of rijksregelgeving (EU-verordening, wet, AMvB, ministeriële regeling) of een VNG-modelverordening van gemeentelijke regelgeving, en geen regeling of beleid van één gemeente? | Ja, wet. [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **in werking**: Is de regeling geldend recht, of als modelverordening actueel? | Ja, geldend recht (versie 2026-10-01). [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **is grondslag voor**: Geeft de regeling de gemeente een taak, bevoegdheid of plicht, of werkt de VNG-modelverordening die uit, in een aanwijsbaar proces, dienst of product? | Ja, met [Stempas ontvangen](../../../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/stempas-ontvangen.md), [Kiezerspas](../../../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/kiezerspas.md), [Volmachtbewijs verkiezingen](../../../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/volmachtbewijs-verkiezingen.md), [Stemrecht](../../../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/stemrecht.md), [Beheren stempassen](../../../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-stempassen.md), [Registreren kiesgerechtigdheid](../../../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Kieswet | is grondslag voor *associatie (gericht)* | [Stempas ontvangen](../../../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/stempas-ontvangen.md) | [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. J 7; UPL nr. 397) |
| Kieswet | is grondslag voor *associatie (gericht)* | [Kiezerspas](../../../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/kiezerspas.md) | [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. K 1; UPL nr. 208) |
| Kieswet | is grondslag voor *associatie (gericht)* | [Volmachtbewijs verkiezingen](../../../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/volmachtbewijs-verkiezingen.md) | [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. L 8, L 14; UPL nr. 453) |
| Kieswet | is grondslag voor *associatie (gericht)* | [Stemrecht](../../../bedrijfsarchitectuur/diensten/0-bestuur-en-ondersteuning/burgerzaken/stemrecht.md) | [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. B 1-B 3; UPL nr. 398) |
| Kieswet | is grondslag voor *associatie (gericht)* | [Beheren stempassen](../../../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-stempassen.md) | [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (hoofdstuk J, K, L) |
| Kieswet | is grondslag voor *associatie (gericht)* | [Registreren kiesgerechtigdheid](../../../bedrijfsarchitectuur/bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md) | [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. B 5, D 1-D 7) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [UPL-lijst extern](../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen beleidskader voor deze regeling; nieuw voor GEMMA.
