---
id: herbegraven-of-alsnog-cremeren
type: dienst
archimate_type: business-service
status: review
naam: Herbegraven of alsnog cremeren
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Toestemming van de gemeente om een begraven stoffelijk overschot op te graven en elders te begraven of te cremeren.
match:
  gemma: geen
afnemer: extern
domein: Fysieke leefomgeving
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Herbegraven of alsnog cremeren

<!-- Gegenereerd door tools/render.py uit de beoordeling herbegraven-of-alsnog-cremeren.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Toestemming van de gemeente om een begraven stoffelijk overschot op te graven en elders te begraven of te cremeren.

### Beschrijving

Een stoffelijk overschot wordt alleen opgegraven met vergunning van de burgemeester van de gemeente waar het is begraven en, bij een particulier graf, met toestemming van de rechthebbende (Wet op de lijkbezorging art. 29 lid 1). Een opgegraven stoffelijk overschot mag worden gecremeerd op verzoek van de persoon uit art. 18 (art. 29 lid 3). De rechthebbende dient de aanvraag in bij de burgemeester (Groningen art. 28 lid 1).

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md).
- **Afnemer**: extern.
- **Domein**: Fysieke leefomgeving.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Opgraven stoffelijk overschot](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/opgraven-stoffelijk-overschot.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Herbegraven of alsnog cremeren | bedient *bediening* | [Rechthebbende op het graf](../../../rollen/rechthebbende-op-het-graf.md) | [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 28 lid 1; Wlb art. 29 lid 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | omvat *aggregatie* | Herbegraven of alsnog cremeren | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 171 (GEMMA-domein Fysieke leefomgeving)) |
| [Opgraven stoffelijk overschot](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/opgraven-stoffelijk-overschot.md) | realiseert *realisatie* | Herbegraven of alsnog cremeren | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (Wlb art. 29; UPL nr. 171) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Herbegraven of alsnog cremeren | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (UPL nr. 171, art. 29) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
