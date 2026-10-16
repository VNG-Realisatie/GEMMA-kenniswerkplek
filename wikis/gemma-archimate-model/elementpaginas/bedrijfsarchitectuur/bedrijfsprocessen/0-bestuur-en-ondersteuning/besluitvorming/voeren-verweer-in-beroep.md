---
id: voeren-verweer-in-beroep
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Voeren verweer in beroep
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: 'Het optreden van de gemeente als partij in een beroep bij de bestuursrechter: stukken en verweer leveren en de uitspraak uitvoeren.'
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Behandelen beroep (GEMMA)
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2025-vng-upl-producten-en-diensten-extern
---

# Voeren verweer in beroep

<!-- Gegenereerd door tools/render.py uit de beoordeling voeren-verweer-in-beroep.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het optreden van de gemeente als partij in een beroep bij de bestuursrechter: stukken en verweer leveren en de uitspraak uitvoeren.

### Beschrijving

Stelt een belanghebbende beroep in bij de bestuursrechter tegen een besluit van de gemeente, dan zendt de rechter de gronden van het beroepschrift aan het bestuursorgaan dat het besluit nam. Dat zendt binnen vier weken de stukken die op de zaak betrekking hebben aan de bestuursrechter en kan een verweerschrift indienen; heeft de rechter erom gevraagd, dan moet het (Awb art. 8:42). Verklaart de rechter het beroep gegrond, dan vernietigt hij het besluit; hij kan het bestuursorgaan opdragen binnen een termijn een nieuw besluit te nemen met inachtneming van zijn aanwijzingen (art. 8:72). Op het beroep beslist de bestuursrechter, niet de gemeente.

### Deelprocessen

1. **Indienen verweer**: Het bestuursorgaan zendt binnen vier weken de stukken aan de bestuursrechter en dient zo nodig een verweerschrift in (art. 8:42). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
2. **Uitvoeren uitspraak**: Na een gegrond beroep neemt het bestuursorgaan zo nodig binnen de gestelde termijn een nieuw besluit met inachtneming van de aanwijzingen van de rechter (art. 8:72 lid 4). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)

### Synoniemen

| Synoniem | Context |
|---|---|
| Behandelen beroep | GEMMA |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Kernobject**: [Besluit](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Belanghebbende](../../../rollen/belanghebbende.md), [Beslisser](../../../rollen/beslisser.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Besluit](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een beroep bij de bestuursrechter: de rechter zendt de gronden van het beroepschrift aan het bestuursorgaan (art. 8:42 lid 1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, het verweerschrift en de stukken voor de bestuursrechter, en na de uitspraak zo nodig een nieuw besluit (art. 8:42, 8:72 lid 4). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elk beroep tegen een besluit van de gemeente. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, hoofdstuk 8 Awb: stukken en verweerschrift binnen vier weken, uitspraak, opdracht tot een nieuw besluit binnen een termijn (art. 8:42, 8:72). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, eén mutatie in de levensloop van een besluit: de rechterlijke toetsing, met zo nodig een nieuw besluit (art. 8:72). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, loopt van het beroep van de belanghebbende tot de uitvoering van de uitspraak (art. 8:42, 8:72). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Beroep](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/beroep.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Voeren verweer in beroep | realiseert *realisatie* | [Beroep](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/beroep.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 8:1, 8:42; UPL nr. 54) |
| Voeren verweer in beroep | zendt de stukken over het bestreden besluit; neemt na vernietiging zo nodig een nieuw *toegang (raadplegen, registreren: lezen-schrijven)* | [Besluit](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 8:42 lid 1; art. 8:72 lid 4) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Belanghebbende](../../../rollen/belanghebbende.md) | stelt beroep in *toewijzing* | Voeren verweer in beroep | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 8:1) |
| [Beslisser](../../../rollen/beslisser.md) | zendt de stukken, voert verweer en neemt zo nodig een nieuw besluit *toewijzing* | Voeren verweer in beroep | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 8:42, 8:72 lid 4) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor beroep; de interne UPL-lijst van GEMMA noemt Beroep behandelen als ondersteunend proces ([2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md), nr. 33). Nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 26](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (product, open): **UPL:** beroep is een gemeentelijk product met grondslag art. 8:1 Awb, domein Bestuur ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 54; Logius: ook voor gemeenten). De interne lijst noemt Beroep behandelen als ondersteunend proces ([2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md), nr. 33). **Bevinding:** het beroep wordt ingesteld bij en behandeld door de bestuursrechter, niet door de gemeente ([2026-rijk-algemene-wet-bestuursrecht-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), art. 6:4 lid 3, 8:1). De gemeente is partij: zij zendt binnen vier weken de stukken en kan een verweerschrift indienen, en neemt een nieuw besluit als de rechter dat opdraagt (art. 8:42, 8:72 lid 4). GEMMA houdt de dienst Beroep, omdat een UPL-product niet wegvalt, en laat haar realiseren door het proces Voeren verweer in beroep, het deel van de gemeente; de bestuursrechter is geen element. **Voorstel:** vermeld bij het UPL-product dat de bestuursrechter het beroep behandelt en dat de gemeente partij is (stukken, verweer, uitvoeren van de uitspraak), en noem art. 8:42 naast art. 8:1 als grondslag voor de taak van de gemeente. Noem het interne proces Voeren verweer in beroep in plaats van Beroep behandelen.

### Besluiten redacteur

- 2026-10-12: De bestuursrechter is geen element: de gemeente is partij in het beroep, de rechter staat in de beschrijving. *Zekerheid: logica.*
