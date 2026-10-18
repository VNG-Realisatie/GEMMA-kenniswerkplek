---
id: behandelen-klacht
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Behandelen klacht
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: 'Het behandelen van een klacht over een gedraging van een bestuursorgaan: de klager horen, de klacht onderzoeken en een oordeel geven.'
match:
  gemma: sterk
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2025-vng-upl-producten-en-diensten-extern
gemma_id: id-904ab005-ae79-48be-8200-14ccb6676a53
gemma_naam: Behandelen klacht
gemma_type: business-process
gemma_definitie: Het afhandelen van klachten tegen het "gedrag of een houding" van een gemeentelijke ambtenaar. Elke blijk van onvrede over gedrag en/of houding met betrekking tot dienstverlening, tussen een klant en een of meer ambtenaren in functie.
gemma_map: Business / Procesarchitectuur / Processenlandschap
gemma_eigenschappen:
  GEMMA type: Bedrijfsproces
  Object ID: 904ab005-ae79-48be-8200-14ccb6676a53
---

# Behandelen klacht

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-klacht.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het behandelen van een klacht over een gedraging van een bestuursorgaan: de klager horen, de klacht onderzoeken en een oordeel geven.

### Beschrijving

Het bestuursorgaan draagt zorg voor een behoorlijke behandeling van mondelinge en schriftelijke klachten over zijn gedragingen en die van wie onder zijn verantwoordelijkheid werkt (Awb art. 9:1, 9:2). Voor een schriftelijke klacht bevestigt het de ontvangst, laat het de klacht behandelen door iemand die niet bij de gedraging betrokken was, hoort het de klager en degene over wie geklaagd wordt en maakt het een verslag (art. 9:4, 9:6, 9:7, 9:10). Het kan een klacht onder voorwaarden niet behandelen, bijvoorbeeld als bezwaar of beroep openstond (art. 9:8). Het handelt de klacht af binnen zes weken, of tien weken als een klachtadviescommissie adviseert, en meldt de klager schriftelijk en gemotiveerd zijn bevindingen en oordeel, met de ombudsman bij wie hij daarna terecht kan (art. 9:11, 9:12, afdeling 9.1.3). Het houdt de schriftelijke klachten bij en publiceert ze jaarlijks (art. 9:12a).

### Deelprocessen

1. **Ontvangen klacht**: Het bestuursorgaan bevestigt de ontvangst van de schriftelijke klacht en beoordeelt of het de klacht behandelt (art. 9:4, 9:6, 9:8). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
2. **Onderzoeken klacht**: Iemand die niet bij de gedraging betrokken was, onderzoekt de klacht en hoort de klager en degene over wie geklaagd wordt, met een verslag; eventueel adviseert een klachtadviescommissie (art. 9:7, 9:9, 9:10, afdeling 9.1.3). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
3. **Afhandelen klacht**: Het bestuursorgaan meldt de klager schriftelijk en gemotiveerd de bevindingen, het oordeel en de conclusies, met de ombudsman; de klacht komt in het jaarlijkse overzicht (art. 9:11, 9:12, 9:12a). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Kernobject**: [Schriftelijke klacht](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/schriftelijke-klacht.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **procesniveau**: bedrijfsproces, kernobject [Schriftelijke klacht](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/schriftelijke-klacht.md) | Loopt van de klacht van de klager tot de kennisgeving van het oordeel aan hem (art. 9:4, 9:12). Eén afhandeling binnen de klachtbehandeling van het bestuursorgaan, dat alle schriftelijke klachten bijhoudt en jaarlijks publiceert (art. 9:2, 9:12a). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Klager](../../../rollen/klager.md). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Schriftelijke klacht ingediend (gebeurtenis, nog geen element): Een klacht over een gedraging van het bestuursorgaan, voor de procedure van afdeling 9.1.2 een schriftelijke klacht (art. 9:1, 9:4). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen klacht | realiseert *realisatie* | [Klacht](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/klacht.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 9:1; UPL nr. 212) |
| Behandelen klacht | behandelt *toegang (registreren)* | [Schriftelijke klacht](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/schriftelijke-klacht.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 9:4, 9:6, 9:12a) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | behandelt de klacht en meldt zijn oordeel *toewijzing* | Behandelen klacht | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 9:2, 9:11, 9:12) |
| [Klager](../../../rollen/klager.md) | dient de klacht in en wordt gehoord *toewijzing* | Behandelen klacht | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 9:4, 9:10, 9:12) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Behandelen klacht* (business-process). Hetzelfde proces: het afhandelen van een klacht over een gedraging. GEMMA beperkt het tot gedrag of houding van een ambtenaar; de Awb omvat ook gedragingen van het bestuursorgaan zelf (art. 9:1). Nieuw: een definitie volgens de Awb, het kernobject Schriftelijke klacht en de relaties.

> Het afhandelen van klachten tegen het "gedrag of een houding" van een gemeentelijke ambtenaar. Elke blijk van onvrede over gedrag en/of houding met betrekking tot dienstverlening, tussen een klant en een of meer ambtenaren in functie.
