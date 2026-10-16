---
id: stempas-ontvangen
type: dienst
archimate_type: business-service
status: review
naam: Stempas ontvangen
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het als kiezer ontvangen van een stempas voor een verkiezing, en bij verlies of niet-ontvangst een nieuwe aanvragen.
match:
  gemma: geen
afnemer: extern
domein: Publieksdiensten
synoniemen:
- Stempas (UPL)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-kieswet-bwbr0004627
---

# Stempas ontvangen

<!-- Gegenereerd door tools/render.py uit de beoordeling stempas-ontvangen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het als kiezer ontvangen van een stempas voor een verkiezing, en bij verlies of niet-ontvangst een nieuwe aanvragen.

### Beschrijving

Elke kiezer ontvangt ten minste veertien dagen voor de stemming een stempas van de burgemeester van de gemeente waar hij als kiezer is geregistreerd; wie haar kwijt is of niet heeft ontvangen, vraagt een nieuwe aan (Kieswet art. J 7, J 8). Grondslag art. J 7 Kieswet; doelgroep burger; niet digitaal (UPL nr. 397).

### Synoniemen

| Synoniem | Context |
|---|---|
| Stempas | UPL |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) (wiki, Kieswet art. J 7) | Het document zelf, waarmee de kiezer stemt | Deze pagina heet Stempas ontvangen, de dienst; de UPL-naam stempas is een synoniem, omdat het bedrijfsobject Stempas die naam draagt (precedent Briefadres aanvragen). Ontvangen volgt de wet: elke kiezer ontvangt een stempas (art. J 7 lid 2). |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md).
- **Afnemer**: extern.
- **Domein**: Publieksdiensten.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een stempas waarmee de kiezer kan stemmen (Kieswet art. J 7 lid 2). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke afnemer die erom vraagt. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, de kiezer, extern (UPL nr. 397: burger). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Verstrekken stempas](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-stempas.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Stempas ontvangen | bedient *bediening* | [Kiezer](../../../rollen/kiezer.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Kieswet](../../../../motivatie/beleidskaders/rijksregelgeving/kieswet.md) | is grondslag voor *associatie (gericht)* | Stempas ontvangen | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. J 7; UPL nr. 397) |
| [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md) | omvat *aggregatie* | Stempas ontvangen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 397 (GEMMA-domein Publieksdiensten)) |
| [Verstrekken stempas](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-stempas.md) | realiseert *realisatie* | Stempas ontvangen | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (UPL nr. 397) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 15](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (product, open): **UPL:** het product heet stempas ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 397). **Bevinding:** de stempas is ook het bedrijfsobject Stempas, kernobject van Beheren stempassen ([2026-rijk-kieswet-bwbr0004627](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), art. J 7 lid 2). Een dienst met dezelfde naam als het object maakt het model dubbelzinnig. GEMMA noemt de dienst daarom Stempas ontvangen, met de UPL-naam als synoniem, zoals Briefadres aanvragen bij briefadres. **Voorstel:** geef een product in de UPL de naam van wat de afnemer doet of krijgt (stempas ontvangen) wanneer de productnaam ook een object is; of leg vast dat GEMMA in dat geval de naam aanvult.
