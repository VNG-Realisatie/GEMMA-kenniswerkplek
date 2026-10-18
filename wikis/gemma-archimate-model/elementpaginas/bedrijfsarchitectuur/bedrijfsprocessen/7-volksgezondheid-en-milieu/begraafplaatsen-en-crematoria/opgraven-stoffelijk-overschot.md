---
id: opgraven-stoffelijk-overschot
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Opgraven stoffelijk overschot
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het opgraven van een stoffelijk overschot uit een graf, met vergunning van de burgemeester.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Opgraving (wet)
- Opgraven lijk (wet)
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
- 2025-vng-upl-producten-en-diensten-extern
---

# Opgraven stoffelijk overschot

<!-- Gegenereerd door tools/render.py uit de beoordeling opgraven-stoffelijk-overschot.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het opgraven van een stoffelijk overschot uit een graf, met vergunning van de burgemeester.

### Beschrijving

Een stoffelijk overschot wordt slechts opgegraven met vergunning van de burgemeester en, bij een particulier graf, met toestemming van de rechthebbende; de burgemeester verbindt voorschriften aan de vergunning over geneeskundig toezicht, vervoer en bestemming (art. 29). Beslisser is de burgemeester. De rechthebbende dient de aanvraag in en schakelt een erkend bedrijf in; opgraven gebeurt in de regel pas na tien jaar grafrust (Groningen art. 28).

### Synoniemen

| Synoniem | Context |
|---|---|
| Opgraving | wet |
| Opgraven lijk | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Behandelen vergunningaanvragen lijkbezorging](behandelen-vergunningaanvragen-lijkbezorging.md), [Toestaan lijkbezorging](toestaan-lijkbezorging.md).
- **Kernobject**: [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **procesniveau**: bedrijfsproces, kernobject [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | Ja, van de aanvraag tot het opgegraven lijk. [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Rechthebbende op het graf](../../../rollen/rechthebbende-op-het-graf.md). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Aanvraag opgraving ingediend (gebeurtenis, nog geen element): Aanvraag van de rechthebbende bij de burgemeester (Groningen art. 28 lid 1). [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Opgraven stoffelijk overschot | vereist *toegang (raadplegen)* | [Vergunning](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/vergunning.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 29 lid 1) |
| Opgraven stoffelijk overschot | graaft op *toegang (bijwerken)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 29) |
| Opgraven stoffelijk overschot | realiseert *realisatie* | [Herbegraven of alsnog cremeren](../../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/herbegraven-of-alsnog-cremeren.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (Wlb art. 29; UPL nr. 171) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen vergunningaanvragen lijkbezorging](behandelen-vergunningaanvragen-lijkbezorging.md) | omvat *aggregatie* | Opgraven stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 29) |
| [Beslisser](../../../rollen/beslisser.md) | verleent vergunning voor *toewijzing* | Opgraven stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 29 lid 1) |
| [Rechthebbende op het graf](../../../rollen/rechthebbende-op-het-graf.md) | vraagt aan *toewijzing* | Opgraven stoffelijk overschot | [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (art. 28 lid 1) |
| [Toestaan lijkbezorging](toestaan-lijkbezorging.md) | omvat *aggregatie* | Opgraven stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 29) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Opgraven stoffelijk overschot | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 29) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
