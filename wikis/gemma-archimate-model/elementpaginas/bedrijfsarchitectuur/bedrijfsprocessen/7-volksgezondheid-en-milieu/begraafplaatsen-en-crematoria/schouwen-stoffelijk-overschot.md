---
id: schouwen-stoffelijk-overschot
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Schouwen stoffelijk overschot
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Onderzoek van een stoffelijk overschot door een arts na het overlijden, om vast te stellen of de dood een natuurlijke oorzaak heeft.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Lijkschouwing (wet)
- Schouwen lijk (wet)
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Schouwen stoffelijk overschot

<!-- Gegenereerd door tools/render.py uit de beoordeling schouwen-stoffelijk-overschot.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Onderzoek van een stoffelijk overschot door een arts na het overlijden, om vast te stellen of de dood een natuurlijke oorzaak heeft.

### Beschrijving

Elk stoffelijk overschot wordt zo spoedig mogelijk geschouwd, door de behandelend arts of door een gemeentelijke lijkschouwer (art. 3). Is de dood natuurlijk, dan volgt een verklaring van overlijden (art. 7); anders waarschuwt de lijkschouwer de officier van justitie en de ambtenaar van de burgerlijke stand (art. 10). Bij een minderjarige kan een nader onderzoek naar de doodsoorzaak volgen (art. 10a). De schouwing door de behandelend arts valt buiten het gemeentelijk perspectief.

### Synoniemen

| Synoniem | Context |
|---|---|
| Lijkschouwing | wet |
| Schouwen lijk | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Toestaan lijkbezorging](toestaan-lijkbezorging.md).
- **Kernobject**: [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md).
- **Gestart door gebeurtenis**: [Overlijden](../../../gebeurtenissen/overlijden.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **procesniveau**: bedrijfsproces, kernobject [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | Ja, van het overlijden tot de verklaring van overlijden of het verslag aan de officier van justitie; het volgt niet op een ander gemeentelijk proces. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Gemeentelijke lijkschouwer](../../../rollen/gemeentelijke-lijkschouwer.md), [Ketenpartner](../../../rollen/ketenpartner.md). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Overlijden](../../../gebeurtenissen/overlijden.md). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Specialisaties

- **Nader onderzoek**: Onderzoek naar de doodsoorzaak van een minderjarige, geleid door de gemeentelijke lijkschouwer (art. 10a). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Schouwen stoffelijk overschot | schouwt *toegang (raadplegen)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |
| Schouwen stoffelijk overschot | geeft de verklaring van overlijden door aan, of waarschuwt bij een niet-natuurlijke dood *stroom* | [Verlenen verlof tot begraving of crematie](verlenen-verlof-tot-begraving-of-crematie.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 7, 10 lid 1, 12) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Gemeentelijke lijkschouwer](../../../rollen/gemeentelijke-lijkschouwer.md) | verricht *toewijzing* | Schouwen stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |
| [Ketenpartner](../../../rollen/ketenpartner.md) | schouwt als behandelende arts *toewijzing* | Schouwen stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 7 lid 1) |
| [Overlijden](../../../gebeurtenissen/overlijden.md) | leidt tot *triggering* | Schouwen stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |
| [Toestaan lijkbezorging](toestaan-lijkbezorging.md) | omvat *aggregatie* | Schouwen stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Schouwen stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 4, 7) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
