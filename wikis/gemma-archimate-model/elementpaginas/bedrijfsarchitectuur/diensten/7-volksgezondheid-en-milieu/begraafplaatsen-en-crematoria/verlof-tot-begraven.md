---
id: verlof-tot-begraven
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Verlof tot begraven
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Toestemming van de gemeente om een stoffelijk overschot te begraven of te cremeren.
match:
  gemma: geen
afnemer: extern
domein: Fysieke leefomgeving
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2010-vng-model-beheersverordening-begraafplaatsen
- 2026-rvo-aangifte-en-akte-van-overlijden
---

# Verlof tot begraven

<!-- Gegenereerd door tools/render.py uit de beoordeling verlof-tot-begraven.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Toestemming van de gemeente om een stoffelijk overschot te begraven of te cremeren.

### Beschrijving

Geen begraving of crematie zonder schriftelijk verlof van de ambtenaar van de burgerlijke stand, dat kosteloos wordt afgegeven (Wet op de lijkbezorging art. 11). De UPL-naam noemt alleen begraven; het verlof geldt ook voor crematie. Voor vervoer over land naar België of Luxemburg volstaat het verlof (Besluit op de lijkbezorging art. 11 lid 3).

De UPL rekent het product tot Iv3 0.2 (Burgerzaken) en het GEMMA-domein Fysieke leefomgeving (UPL). In dit model staat het bij de begraafplaatsen en crematoria, naast het bedrijfsproces dat het levert, en in de functie-indeling bij het domein van de UPL.

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Functie-indeling naar domein, onderdeel van**: GEMMA-functie *Producten- en dienstenrealisatie fysieke leefomgeving* (geen element van de wiki; Fysieke leefomgeving › Uitvoering fysieke leefomgeving › Producten- en dienstenrealisatie fysieke leefomgeving), bron: [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 438 (GEMMA-domein Fysieke leefomgeving)).
- **Afnemer**: extern.
- **Domein**: Fysieke leefomgeving.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, schriftelijk verlof tot begraving of crematie, kosteloos (Wlb art. 11). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger en bedrijf (UPL): wie in de lijkbezorging voorziet, meestal via de uitvaartondernemer (RVO). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, met [Verlenen verlof tot begraving of crematie](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-verlof-tot-begraving-of-crematie.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verlof tot begraven | bedient *bediening* | [Degene die in de lijkbezorging voorziet](../../../rollen/degene-die-in-de-lijkbezorging-voorziet.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (Wlb art. 11, 18 lid 1; UPL nr. 438; RVO inleiding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Verlenen verlof tot begraving of crematie](../../../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-verlof-tot-begraving-of-crematie.md) | realiseert *realisatie* | Verlof tot begraven | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (Wlb art. 11; UPL nr. 438) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Verlof tot begraven | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (UPL nr. 438, art. 11) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [VNG Model-beheersverordening begraafplaatsen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) | Model-beheersverordening begraafplaatsen 2010 (VNG), met toelichting |
| [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 2](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (indeling, open): **UPL:** verlof tot begraven valt onder Iv3 0.2 (Burgerzaken); de andere producten van de lijkbezorging vallen onder 7.5 ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md)). **Bevinding:** het verlof hoort bij de lijkbezorging, ook al geeft de ambtenaar van de burgerlijke stand het af ([2026-rijk-wet-op-de-lijkbezorging-wettekst](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), art. 11). GEMMA zet het onder 7.5, beleidsdomein Begraafplaatsen en crematoria, naast het bedrijfsproces Verlenen verlof tot begraving of crematie onder Toestaan lijkbezorging. **Voorstel:** verplaats verlof tot begraven in de UPL naar taakveld 7.5.
