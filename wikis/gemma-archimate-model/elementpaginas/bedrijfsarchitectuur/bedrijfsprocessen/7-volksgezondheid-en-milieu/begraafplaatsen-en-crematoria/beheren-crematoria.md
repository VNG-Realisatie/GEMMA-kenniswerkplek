---
id: beheren-crematoria
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Beheren crematoria
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: 'Het beheer van een crematorium over de hele levensloop: vestigen, uitbreiden of wijzigen, en opheffen.'
match:
  gemma: geen
procesniveau: levensloopproces
afnemer: extern
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Beheren crematoria

<!-- Gegenereerd door tools/render.py uit de beoordeling beheren-crematoria.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het beheer van een crematorium over de hele levensloop: vestigen, uitbreiden of wijzigen, en opheffen.

### Beschrijving

Crematoria zijn gemeentelijk of bijzonder; een bijzonder crematorium wordt gevestigd en in werking gehouden door een kerkgenootschap, een privaatrechtelijke rechtspersoon of een natuurlijk persoon (Wet op de lijkbezorging art. 51, 52). Het college besluit tot vestiging van een gemeentelijk crematorium of verleent een vergunning voor een bijzonder crematorium, in beide gevallen na een openbare kennisgeving van ten minste dertig dagen (art. 53, 54). Bij opheffing van een bijzonder crematorium gaat het register naar het archief van de gemeente (art. 50 lid 3).

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Verlenen vergunning bijzonder crematorium](verlenen-vergunning-bijzonder-crematorium.md).
- **Beleidsdomeinindeling**: beleidsdomein Begraafplaatsen en crematoria, taakveld 7 Volksgezondheid en Milieu (van het kernobject).
- **Kernobject**: [Crematorium](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **procesniveau**: levensloopproces, kernobject [Crematorium](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md) | Omvat de levensloop van het crematorium: vestiging, uitbreiding of wijziging, en opheffing (art. 50 lid 3, 53, 54). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Houder van het crematorium](../../../rollen/houder-van-het-crematorium.md). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Voornemen tot vestiging crematorium gemeld (gebeurtenis, nog geen element), Aanvraag vergunning bijzonder crematorium ingediend (gebeurtenis, nog geen element): Het voornemen tot vestiging van een gemeentelijk crematorium, of een aanvraag om vergunning voor een bijzonder crematorium (art. 53, 54). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

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
