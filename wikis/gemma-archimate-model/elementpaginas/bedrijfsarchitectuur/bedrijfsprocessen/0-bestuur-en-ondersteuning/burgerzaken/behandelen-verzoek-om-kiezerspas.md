---
id: behandelen-verzoek-om-kiezerspas
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Behandelen verzoek om kiezerspas
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het behandelen van het verzoek van een kiezer om in een stembureau naar keuze te stemmen, tot uitreiking van een kiezerspas.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-kieswet-bwbr0004627
---

# Behandelen verzoek om kiezerspas

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-verzoek-om-kiezerspas.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het behandelen van het verzoek van een kiezer om in een stembureau naar keuze te stemmen, tot uitreiking van een kiezerspas.

### Beschrijving

De kiezer richt zijn verzoek schriftelijk, tot de vijfde dag voor de stemming, of mondeling in persoon, tot de dag voor de stemming om twaalf uur, aan de burgemeester van de gemeente waar hij op de dag van de kandidaatstelling als kiezer is geregistreerd, met een kopie van een identiteitsbewijs; de burgemeester maakt de termijnen bekend in het gemeenteblad (Kieswet art. K 3, K 6). Als bewijs krijgt de kiezer een kiezerspas, waarmee hij in het hele gebied van de verkiezing kan stemmen; een kwijtgeraakte kiezerspas wordt niet vervangen en de stempas wordt ongeldig (art. K 1, K 4, J 7a).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren stempassen](beheren-stempassen.md).
- **Kernobject**: [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een aanvraag voor een document dat na een directe toets wordt uitgereikt of verzonden.
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Kiezer](../../../rollen/kiezer.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, het schriftelijke of mondelinge verzoek van de kiezer (Kieswet art. K 3). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de kiezerspas, uitgereikt of verzonden als bewijs dat aan het verzoek is voldaan (Kieswet art. K 4 lid 1). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk verzoek. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, kieswet art. K 1-K 6: termijnen, kopie identiteitsbewijs, formulier, geen vervanging. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Beheren stempassen](beheren-stempassen.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek tot de uitgereikte of verzonden kiezerspas. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Kiezerspas](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/kiezerspas.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen verzoek om kiezerspas | reikt een kiezerspas uit in plaats van de stempas *toegang (registreren)* | [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 4, J 7a lid 2 onder a) |
| Behandelen verzoek om kiezerspas | realiseert *realisatie* | [Kiezerspas](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/kiezerspas.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (UPL nr. 208) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren stempassen](beheren-stempassen.md) | omvat *aggregatie* | Behandelen verzoek om kiezerspas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 1-K 6) |
| [Kiezer](../../../rollen/kiezer.md) | vraagt de kiezerspas aan *toewijzing* | Behandelen verzoek om kiezerspas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 3) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
