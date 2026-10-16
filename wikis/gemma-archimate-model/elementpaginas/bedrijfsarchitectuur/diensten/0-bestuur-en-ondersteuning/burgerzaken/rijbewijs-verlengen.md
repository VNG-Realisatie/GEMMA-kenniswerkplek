---
id: rijbewijs-verlengen
type: dienst
archimate_type: business-service
status: review
naam: Rijbewijs verlengen
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het vernieuwen van een Nederlands rijbewijs bij de gemeente, aan de balie of online via de RDW, en het afhalen ervan.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Rijbewijs vernieuwen (wet)
- Rijbewijs online verlengen (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen
- 2026-rijk-reglement-rijbewijzen-bwbr0008074
---

# Rijbewijs verlengen

<!-- Gegenereerd door tools/render.py uit de beoordeling rijbewijs-verlengen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het vernieuwen van een Nederlands rijbewijs bij de gemeente, aan de balie of online via de RDW, en het afhalen ervan.

### Beschrijving

Wie in de gemeente staat ingeschreven en een Nederlands rijbewijs heeft, kan de verlenging of een categorie-uitbreiding onder bepaalde voorwaarden online aanvragen via de RDW, met een digitale pasfoto van een erkende fotograaf of fotocabine en de DigiD-app; hij haalt het rijbewijs twee werkdagen later op afspraak op (Utrecht). Bij vernieuwing wordt het eerdere rijbewijs overgelegd en, bij een groot rijbewijs, vanaf 75 jaar of na een aantekening van het CBR, moet een verklaring van geschiktheid zijn geregistreerd (Reglement rijbewijzen art. 35).

### Synoniemen

| Synoniem | Context |
|---|---|
| Rijbewijs vernieuwen | wet |
| Rijbewijs online verlengen | beleid |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de aanvrager krijgt het vernieuwde rijbewijs uitgereikt, twee werkdagen na een online aanvraag. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke aanvraag. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, de aanvrager, een inwoner (UPL: doelgroep burger). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Behandelen aanvraag rijbewijs](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-rijbewijs.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, de UPL noemt het als eigen product. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen aanvraag rijbewijs](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-rijbewijs.md) | realiseert *realisatie* | Rijbewijs verlengen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md), [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) (UPL nr. 363; Utrecht regel 21-23; Reglement art. 35) |
| [Officiële documenten verstrekking](../../../bedrijfsfuncties/publieksdiensten/officiele-documenten-verstrekking.md) | omvat *aggregatie* | Rijbewijs verlengen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 363 (GEMMA-domein Publieksdiensten)) |
| [Reglement rijbewijzen](../../../../motivatie/beleidskaders/rijksregelgeving/reglement-rijbewijzen.md) | is grondslag voor *associatie (gericht)* | Rijbewijs verlengen | [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 35) |
| [Wegenverkeerswet 1994](../../../../motivatie/beleidskaders/rijksregelgeving/wegenverkeerswet-1994.md) | is grondslag voor *associatie (gericht)* | Rijbewijs verlengen | [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (art. 119 lid 1 onder a) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Rijbewijs aanvragen of verlengen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) | Gemeente Utrecht: Rijbewijs aanvragen of verlengen |
| [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) | Reglement rijbewijzen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.
