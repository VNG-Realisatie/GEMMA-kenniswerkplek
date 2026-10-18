---
id: vervoersdocumenten-stoffelijk-overschot
type: dienst
archimate_type: business-service
status: review
naam: Vervoersdocumenten stoffelijk overschot
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het document van de gemeente waarmee een stoffelijk overschot ongehinderd naar het buitenland wordt vervoerd.
match:
  gemma: geen
afnemer: extern
domein: Fysieke leefomgeving
synoniemen:
- Laissez-passer voor lijken (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvo-aangifte-en-akte-van-overlijden
---

# Vervoersdocumenten stoffelijk overschot

<!-- Gegenereerd door tools/render.py uit de beoordeling vervoersdocumenten-stoffelijk-overschot.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het document van de gemeente waarmee een stoffelijk overschot ongehinderd naar het buitenland wordt vervoerd.

### Beschrijving

Vervoer naar een staat die partij is bij de Overeenkomst van Straatsburg gaat ongehinderd met een laissez-passer voor lijken van de burgemeester van de gemeente waar de akte van overlijden is ingeschreven (Besluit op de lijkbezorging art. 11 lid 1). Voor vervoer over land naar België of Luxemburg volstaat het verlof tot begraving of crematie (art. 11 lid 3). Bij binnenkomst wordt het document aan de douane overgelegd (art. 11 lid 5).

### Synoniemen

| Synoniem | Context |
|---|---|
| Laissez-passer voor lijken | wet |

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| Laissez-passer voor lijken (Specialisatie van Vergunning zonder eigen pagina in deze wiki) | Het document van de burgemeester waarmee een stoffelijk overschot ongehinderd naar een verdragsstaat van de Overeenkomst van Straatsburg wordt vervoerd (Besluit op de lijkbezorging art. 11 lid 1) | Deze pagina heet Vervoersdocumenten stoffelijk overschot: de dienst, met de UPL-naam, en Laissez-passer voor lijken als synoniem (wet). Het document zelf is de specialisatie Laissez-passer voor lijken van Vergunning en krijgt geen pagina; het afgeven is het bedrijfsproces Afgeven laissez-passer. |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: GEMMA-functie *Producten- en dienstenrealisatie fysieke leefomgeving* (geen element van de wiki; Fysieke leefomgeving › Uitvoering fysieke leefomgeving › Producten- en dienstenrealisatie fysieke leefomgeving), bron: [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 445 (GEMMA-domein Fysieke leefomgeving)).
- **Afnemer**: extern.
- **Domein**: Fysieke leefomgeving.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Afgeven laissez-passer](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/afgeven-laissez-passer.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vervoersdocumenten stoffelijk overschot | bedient *bediening* | [Degene die in de lijkbezorging voorziet](../../../rollen/degene-die-in-de-lijkbezorging-voorziet.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (UPL nr. 445; RVO, Zie ook) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Afgeven laissez-passer](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/afgeven-laissez-passer.md) | realiseert *realisatie* | Vervoersdocumenten stoffelijk overschot | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (Besluit op de lijkbezorging art. 11; UPL nr. 445) |
| [Besluit op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Vervoersdocumenten stoffelijk overschot | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) (UPL nr. 445, art. 11) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
