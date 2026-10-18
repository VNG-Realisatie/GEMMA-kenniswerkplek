---
id: verstrekken-stempas
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Verstrekken stempas
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het vaststellen, personaliseren en toezenden van stempassen aan de kiezers, en het uitreiken van een nieuwe stempas op verzoek.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2025-vng-upl-producten-en-diensten-extern
---

# Verstrekken stempas

<!-- Gegenereerd door tools/render.py uit de beoordeling verstrekken-stempas.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het vaststellen, personaliseren en toezenden van stempassen aan de kiezers, en het uitreiken van een nieuwe stempas op verzoek.

### Beschrijving

Daags na de kandidaatstelling stelt de burgemeester de gegevens vast voor het personaliseren van de stempassen, met de informatie van de minister voor de productie (Kieswet art. J 7 lid 1 en 4). Ten minste veertien dagen voor de stemming ontvangt elke kiezer een stempas met volgnummer (art. J 7 lid 2). Wie zijn stempas kwijt is of niet heeft ontvangen, vraagt schriftelijk tot de vijfde dag voor de stemming of mondeling tot de dag voor de stemming om twaalf uur een nieuwe aan, met een kopie van een identiteitsbewijs; de oude wordt ongeldig. Een stempas die ongeldig is door een kiezerspas, volmacht, briefstembewijs, onterechte registratie of ontvreemding, wordt niet vervangen (art. J 7a, J 8).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren stempassen](beheren-stempassen.md).
- **Kernobject**: [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **procesniveau**: bedrijfsproces, kernobject [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) | Ja, van de termijn (de dag van de kandidaatstelling) of het verzoek tot de stempas. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Kiezer](../../../rollen/kiezer.md). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Kandidaatstelling voor verkiezing (gebeurtenis, nog geen element), Verzoek om nieuwe stempas ingediend (gebeurtenis, nog geen element): De dag van de kandidaatstelling, en voor een nieuwe stempas het verzoek van de kiezer (Kieswet art. J 7 lid 1, J 8 lid 2). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verstrekken stempas | verstrekt en vervangt *toegang (registreren)* | [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7, J 8) |
| Verstrekken stempas | stelt de gegevens van de geregistreerde kiezers vast *toegang (raadplegen)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 1) |
| Verstrekken stempas | realiseert *realisatie* | [Stempas ontvangen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/stempas-ontvangen.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (UPL nr. 397) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren stempassen](beheren-stempassen.md) | omvat *aggregatie* | Verstrekken stempas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7, J 8) |
| [Kiezer](../../../rollen/kiezer.md) | ontvangt de stempas en vraagt een nieuwe aan *toewijzing* | Verstrekken stempas | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2, J 8) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
