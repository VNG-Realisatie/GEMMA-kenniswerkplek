---
id: officier-van-justitie
type: actor
archimate_type: business-actor
status: review
naam: Officier van justitie
onderwerpen:
- lijkbezorging
definitie: Lid van het openbaar ministerie dat beslist over strafrechtelijk onderzoek, ook naar een niet-natuurlijke dood.
match:
  gemma: geen
doelgroep: ketenpartners
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rvo-aangifte-en-akte-van-overlijden
---

# Officier van justitie

<!-- Gegenereerd door tools/render.py uit de beoordeling officier-van-justitie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Lid van het openbaar ministerie dat beslist over strafrechtelijk onderzoek, ook naar een niet-natuurlijke dood.

### Beschrijving

Bij een niet-natuurlijke dood brengt de gemeentelijke lijkschouwer verslag uit aan de officier van justitie, die een verklaring van geen bezwaar tegen begraving of crematie afgeeft als er geen strafrechtelijk onderzoek nodig is (Wet op de lijkbezorging art. 10, 12). Zonder die verklaring verleent de ambtenaar van de burgerlijke stand geen verlof. Een uitvaart binnen 36 uur vraagt ook zijn instemming (art. 17; RVO).

## Plaats in het model

### Typering

Actor. Uitkomst van de beslistabel: Handelende partij (kern ja).

### Plaats in de indelingen

- **Doelgroep**: ketenpartners.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: handelende partij. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **los van verantwoordelijkheid**: Blijft de partij bestaan als deze verantwoordelijkheid wegvalt, zodat zij ook andere rollen kan vervullen? | Ja, bestaat los van de lijkbezorging, met eigen taken in de strafrechtspleging (RVO: strafrechtelijk onderzoek). [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **vervult een rol**: Vervult de partij aanwijsbaar een rol in gemeentelijk gedrag? | Ja, met [Ketenpartner](../rollen/ketenpartner.md). |
| **soort partij**: Heeft elke gemeente met deze partij te maken in dezelfde rol, zodat het element voor alle gemeenten geldt? Het criterium sluit uit wat bij één of enkele gemeenten hoort, niet een partij die landelijk maar één keer bestaat. | Ja, bij elke gemeente betrokken bij een niet-natuurlijke dood (art. 10, 12); een soort partij, geen individuele officier. [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Officier van justitie | vervult *toewijzing* | [Ketenpartner](../rollen/ketenpartner.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 10, 12, 17) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Ondernemersplein Aangifte overlijden](../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen actor Officier van justitie; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-04: Actor als ketenpartner in Bezorgen stoffelijk overschot (Wlb art. 10, 12), zonder eigen deelproces. Herziet de uitkomst buiten scope. *Zekerheid: kennis.*
