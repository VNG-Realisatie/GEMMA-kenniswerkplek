---
id: behandelen-bezwaar
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Behandelen bezwaar
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: 'Het behandelen van een bezwaarschrift tegen een besluit: belanghebbenden horen, het besluit heroverwegen en op het bezwaar beslissen.'
match:
  gemma: sterk
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2025-vng-upl-producten-en-diensten-extern
gemma_id: id-1e66364c-80c6-4d9f-9737-bab779a23119
gemma_naam: Behandelen bezwaar
gemma_type: business-process
gemma_definitie: 'Het afhandelen van bezwaren: door een wettelijk voorschrift bestaande bevoegdheid een voorziening tegen een besluit te vragen bij de gemeente dat het besluit heeft genomen. Een voorbeeld is het bezwaar tegen de hoogte van de WOZ-waarde of het niet toekennen van een bepaalde gevraagde Wmo-voorziening.'
gemma_map: Business / Procesarchitectuur / Processenlandschap
gemma_eigenschappen:
  GEMMA type: Bedrijfsproces
  Object ID: 1e66364c-80c6-4d9f-9737-bab779a23119
---

# Behandelen bezwaar

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-bezwaar.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het behandelen van een bezwaarschrift tegen een besluit: belanghebbenden horen, het besluit heroverwegen en op het bezwaar beslissen.

### Beschrijving

Een belanghebbende maakt bezwaar door een bezwaarschrift in te dienen bij het bestuursorgaan dat het besluit nam, binnen zes weken na de bekendmaking; een bezwaarschrift dat niet aan de eisen voldoet, kan na een herstelmogelijkheid niet-ontvankelijk worden verklaard (Awb art. 6:4–6:8). Voordat het bestuursorgaan beslist, stelt het de belanghebbenden in de gelegenheid te worden gehoord, legt het de stukken ter inzage en maakt het een verslag (art. 7:2–7:7). Is het bezwaar ontvankelijk, dan heroverweegt het het bestreden besluit en herroept en vervangt het dat zo nodig (art. 7:11). Het beslist binnen zes weken, en binnen twaalf weken als een adviescommissie met een onafhankelijke voorzitter hoort en adviseert; de beslissing wordt gemotiveerd en bekendgemaakt (art. 7:10, 7:12, 7:13). Tegen de beslissing op bezwaar staat beroep open bij de bestuursrechter (art. 7:1 lid 2).

### Deelprocessen

1. **Ontvangen bezwaarschrift**: Het bestuursorgaan ontvangt het bezwaarschrift, toetst termijn en vereisten en laat een verzuim zo nodig herstellen (art. 6:4–6:8). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
2. **Horen belanghebbenden**: Het bestuursorgaan of een adviescommissie hoort de belanghebbenden, met de stukken vooraf ter inzage en een verslag (art. 7:2–7:9, 7:13). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
3. **Beslissen op bezwaar**: Het bestuursorgaan heroverweegt het besluit, herroept en vervangt het zo nodig, en maakt de gemotiveerde beslissing bekend (art. 7:10–7:12). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Kernobject**: [Bezwaarschrift](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/bezwaarschrift.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Belanghebbende](../../../rollen/belanghebbende.md), [Beslisser](../../../rollen/beslisser.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Bezwaarschrift](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/bezwaarschrift.md), [Besluit](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een bezwaarschrift tegen een besluit, ingediend binnen zes weken na de bekendmaking (art. 6:4, 6:7, 6:8). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de gemotiveerde beslissing op het bezwaar, bekendgemaakt aan wie bezwaar maakte (art. 7:11, 7:12). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elk bezwaarschrift tegen een besluit. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, afdeling 7.2 Awb: horen, stukken ter inzage, verslag, beslistermijn van zes of twaalf weken, heroverweging, motivering (art. 7:2–7:13). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, eén mutatie in de levensloop van een besluit: de heroverweging van het bestreden besluit (art. 7:11). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, loopt van het bezwaarschrift van de belanghebbende tot de bekendmaking van de beslissing op bezwaar aan hem (art. 6:4, 7:12). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, eindigt in de beslissing op het bezwaar van het bestuursorgaan dat het besluit nam (art. 7:11, 7:12). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Bezwaar](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/bezwaar.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen bezwaar | realiseert *realisatie* | [Bezwaar](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/bezwaar.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 7:1; UPL nr. 64) |
| Behandelen bezwaar | behandelt *toegang (registreren)* | [Bezwaarschrift](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/bezwaarschrift.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 6:4–6:6, 7:4) |
| Behandelen bezwaar | heroverweegt en herroept zo nodig *toegang (bijwerken)* | [Besluit](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 7:11) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Belanghebbende](../../../rollen/belanghebbende.md) | maakt bezwaar en wordt gehoord *toewijzing* | Behandelen bezwaar | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 6:4, 7:2) |
| [Beslisser](../../../rollen/beslisser.md) | heroverweegt het besluit en beslist op het bezwaar *toewijzing* | Behandelen bezwaar | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 7:11, 7:12) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Behandelen bezwaar* (business-process). Hetzelfde proces: het afhandelen van een bezwaar tegen een besluit bij het bestuursorgaan dat het nam. Nieuw: een definitie volgens de Awb, het kernobject Bezwaarschrift en de relaties.

> Het afhandelen van bezwaren: door een wettelijk voorschrift bestaande bevoegdheid een voorziening tegen een besluit te vragen bij de gemeente dat het besluit heeft genomen. Een voorbeeld is het bezwaar tegen de hoogte van de WOZ-waarde of het niet toekennen van een bepaalde gevraagde Wmo-voorziening.

### Besluiten redacteur

- 2026-10-12: De adviescommissie (Awb art. 7:13) is geen element: het bestuursorgaan kan haar instellen; zij staat in de beschrijving. *Zekerheid: logica.*
