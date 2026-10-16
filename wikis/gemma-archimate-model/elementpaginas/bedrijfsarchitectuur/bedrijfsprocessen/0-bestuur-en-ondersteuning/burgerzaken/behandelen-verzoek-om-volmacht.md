---
id: behandelen-verzoek-om-volmacht
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Behandelen verzoek om volmacht
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het behandelen van het schriftelijke verzoek van een kiezer om bij volmacht te stemmen, tot inwilliging met een volmachtbewijs of afwijzing.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2025-vng-upl-producten-en-diensten-extern
---

# Behandelen verzoek om volmacht

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-verzoek-om-volmacht.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het behandelen van het schriftelijke verzoek van een kiezer om bij volmacht te stemmen, tot inwilliging met een volmachtbewijs of afwijzing.

### Beschrijving

Een kiezer die verwacht niet in persoon te kunnen stemmen, kan bij volmacht stemmen: op een schriftelijke aanvraag bij de burgemeester, of door zijn stempas of kiezerspas met de gemachtigde te ondertekenen en over te dragen, zonder tussenkomst van de gemeente (Kieswet art. L 1, L 2, L 14). Bij het verzoekschrift op een formulier wijst de kiezer een gemachtigde aan die zelf als kiezer is geregistreerd en zich bereid verklaart (art. L 8). De burgemeester beslist zo spoedig mogelijk, niet eerder dan op de dag van de kandidaatstelling; bij inwilliging maakt hij een volmachtbewijs op voor de gemachtigde en wordt de stempas van de volmachtgever ongeldig; een afwijzing deelt hij met redenen mee (art. L 6, L 11, J 7a).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren stempassen](beheren-stempassen.md).
- **Kernobject**: [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Kiezer](../../../rollen/kiezer.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, het verzoekschrift van de kiezer op een formulier, met de verklaring van de gemachtigde (Kieswet art. L 8). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de inwilliging met een volmachtbewijs voor de gemachtigde, of de afwijzing met redenen (Kieswet art. L 6, L 11). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk verzoek. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, kieswet art. L 1-L 15: wie gemachtigde kan zijn, termijnen, beslissing niet eerder dan op de dag van de kandidaatstelling. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Beheren stempassen](beheren-stempassen.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoekschrift tot het volmachtbewijs of de afwijzing. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, een beschikking van de burgemeester op het verzoek (Kieswet art. L 11 lid 1 en 4). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Volmachtbewijs verkiezingen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/volmachtbewijs-verkiezingen.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen verzoek om volmacht | maakt de stempas van de volmachtgever ongeldig *toegang (beëindigen)* | [Stempas](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7a lid 2 onder a, L 11) |
| Behandelen verzoek om volmacht | realiseert *realisatie* | [Volmachtbewijs verkiezingen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/volmachtbewijs-verkiezingen.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (UPL nr. 453) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren stempassen](beheren-stempassen.md) | omvat *aggregatie* | Behandelen verzoek om volmacht | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 1-L 15) |
| [Beslisser](../../../rollen/beslisser.md) | beslist op het verzoek *toewijzing* | Behandelen verzoek om volmacht | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 11) |
| [Kiezer](../../../rollen/kiezer.md) | dient het verzoekschrift in *toewijzing* | Behandelen verzoek om volmacht | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 8) |

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
