---
id: beheren-crematoria
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Beheren crematoria
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: 'Het beheer van een crematorium over de hele levensloop: vestigen, uitbreiden of wijzigen, en opheffen.'
match:
  gemma: geen
data_object: nee
procesniveau: levensloopproces
afnemer: extern
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Beheren crematoria

<!-- Gegenereerd door tools/render.py uit de beoordeling beheren-crematoria.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beheer van een crematorium over de hele levensloop: vestigen, uitbreiden of wijzigen, en opheffen.

### Beschrijving

Crematoria zijn gemeentelijk of bijzonder; een bijzonder crematorium wordt gevestigd en in werking gehouden door een kerkgenootschap, een privaatrechtelijke rechtspersoon of een natuurlijk persoon (Wet op de lijkbezorging art. 51, 52). Het college besluit tot vestiging van een gemeentelijk crematorium of verleent een vergunning voor een bijzonder crematorium, in beide gevallen na een openbare kennisgeving van ten minste dertig dagen (art. 53, 54). Bij opheffing van een bijzonder crematorium gaat het register naar het archief van de gemeente (art. 50 lid 3).

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Verlenen vergunning bijzonder crematorium](verlenen-vergunning-bijzonder-crematorium.md).
- **Beleidsdomeinindeling**: beleidsdomein Begraafplaatsen en crematoria, taakveld 7 Volksgezondheid en Milieu (van het kernobject).
- **Kernobject**: [Crematorium](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Houder van het crematorium](../../../rollen/houder-van-het-crematorium.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Crematorium](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, het voornemen tot vestiging van een gemeentelijk crematorium, of een aanvraag om vergunning voor een bijzonder crematorium (art. 53, 54). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een crematorium dat gevestigd en in werking is, en na opheffing niet meer bestaat (art. 50 lid 3, 51, 54). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk crematorium, gemeentelijk of bijzonder. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet op de lijkbezorging art. 50–56. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, houders van bijzondere crematoria en nabestaanden (art. 52, 58). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **omvat processen**: Omvat het minstens twee bedrijfsprocessen van dezelfde soort werk? | Ja, met [Verlenen vergunning bijzonder crematorium](verlenen-vergunning-bijzonder-crematorium.md). |
| **omvat levensloop**: Omvat het het gedrag over de hele levensloop van één exemplaar van een bedrijfsobject, van ontstaan tot einde, of, binnen een ketensamenwerking, het deel van die levensloop dat één partij uitvoert? | Ja, omvat de levensloop van het crematorium: vestiging, uitbreiding of wijziging, en opheffing (art. 50 lid 3, 53, 54). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Beheren crematoria | omvat *aggregatie* | [Verlenen vergunning bijzonder crematorium](verlenen-vergunning-bijzonder-crematorium.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 53–55) |
| Beheren crematoria | beheert *toegang (bijwerken)* | [Crematorium](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 50, 51, 54) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Houder van het crematorium](../../../rollen/houder-van-het-crematorium.md) | houdt in werking *toewijzing* | Beheren crematoria | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 50, 52) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor het beheer van crematoria; nieuw voor GEMMA.
