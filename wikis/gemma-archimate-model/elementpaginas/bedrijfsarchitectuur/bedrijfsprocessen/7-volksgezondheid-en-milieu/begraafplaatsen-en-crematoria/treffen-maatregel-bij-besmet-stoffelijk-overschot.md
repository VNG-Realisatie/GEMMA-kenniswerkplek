---
id: treffen-maatregel-bij-besmet-stoffelijk-overschot
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Treffen maatregel bij besmet stoffelijk overschot
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het nemen van maatregelen om gevaar voor de volksgezondheid door een besmet stoffelijk overschot af te wenden.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Treffen maatregel bij besmet lijk (wet)
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rijk-wet-publieke-gezondheid-wettekst
---

# Treffen maatregel bij besmet stoffelijk overschot

<!-- Gegenereerd door tools/render.py uit de beoordeling treffen-maatregel-bij-besmet-stoffelijk-overschot.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het nemen van maatregelen om gevaar voor de volksgezondheid door een besmet stoffelijk overschot af te wenden.

### Beschrijving

Is een stoffelijk overschot besmet met een infectieus of giftig agens of stof, of bestaat daarvan een gegrond vermoeden, waardoor een ernstig gevaar voor de volksgezondheid kan ontstaan, dan kan de burgemeester maatregelen treffen om dit gevaar af te wenden, na advies van de GGD (Wet op de lijkbezorging art. 22a). Beslisser is de burgemeester. De melding komt van een arts via de GGD (Wet publieke gezondheid art. 21 lid 2, 27 lid 3). De maatregel zelf is een beschikking.

### Synoniemen

| Synoniem | Context |
|---|---|
| Treffen maatregel bij besmet lijk | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Toestaan lijkbezorging](toestaan-lijkbezorging.md).
- **Kernobject**: [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen melding*. De GGD meldt een besmet lijk aan de burgemeester, die een maatregel treft (Wpg art. 27 lid 3; Wlb art. 22a): een melding waarop de gemeente actie onderneemt.
- **Gestart door gebeurtenis**: [Besmet stoffelijk overschot gemeld](../../../gebeurtenissen/besmet-stoffelijk-overschot-gemeld.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **procesniveau**: bedrijfsproces, kernobject [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | Ja, van de melding van de GGD tot de maatregel. [Wet publieke gezondheid](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Adviseur](../../../rollen/adviseur.md), [Beslisser](../../../rollen/beslisser.md). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Besmet stoffelijk overschot gemeld](../../../gebeurtenissen/besmet-stoffelijk-overschot-gemeld.md). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Treffen maatregel bij besmet stoffelijk overschot | treft *toegang (registreren)* | [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |
| Treffen maatregel bij besmet stoffelijk overschot | betreft *toegang (raadplegen)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Adviseur](../../../rollen/adviseur.md) | adviseert over *toewijzing* | Treffen maatregel bij besmet stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |
| [Beslisser](../../../rollen/beslisser.md) | treft *toewijzing* | Treffen maatregel bij besmet stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |
| [Besmet stoffelijk overschot gemeld](../../../gebeurtenissen/besmet-stoffelijk-overschot-gemeld.md) | leidt tot *triggering* | Treffen maatregel bij besmet stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) (Wlb art. 22a; Wpg art. 27 lid 3) |
| [Toestaan lijkbezorging](toestaan-lijkbezorging.md) | omvat *aggregatie* | Treffen maatregel bij besmet stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Treffen maatregel bij besmet stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Wet publieke gezondheid](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) | Wet publieke gezondheid (BWBR0024705) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
