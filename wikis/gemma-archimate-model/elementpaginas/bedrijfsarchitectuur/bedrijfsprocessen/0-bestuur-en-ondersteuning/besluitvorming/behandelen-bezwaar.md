---
id: behandelen-bezwaar
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen bezwaar
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: 'Het behandelen van een bezwaarschrift tegen een besluit: belanghebbenden horen, het besluit heroverwegen en op het bezwaar beslissen.'
match:
  gemma: sterk
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

**Status: goedgekeurd** door de redacteur.

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

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Kernobject**: [Bezwaarschrift](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/bezwaarschrift.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **procesniveau**: bedrijfsproces, kernobject [Bezwaarschrift](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/bezwaarschrift.md) | Loopt van het bezwaarschrift van de belanghebbende tot de bekendmaking van de beslissing op bezwaar aan hem (art. 6:4, 7:12). Eén mutatie in de levensloop van een bezwaarschrift: van indiening tot de beslissing, met de heroverweging van het bestreden besluit (art. 6:4, 7:11, 7:12). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Belanghebbende](../../../rollen/belanghebbende.md), [Beslisser](../../../rollen/beslisser.md). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Bezwaarschrift ingediend (gebeurtenis, nog geen element): Een bezwaarschrift tegen een besluit, ingediend binnen zes weken na de bekendmaking (art. 6:4, 6:7, 6:8). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |

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
