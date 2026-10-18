---
id: crematoriumregister
type: dienst
archimate_type: business-service
status: review
naam: Crematoriumregister
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Inzage in het openbare register van alle daar gecremeerde stoffelijke overschotten en de bestemming van de as dat de houder van een crematorium bijhoudt.
match:
  gemma: geen
afnemer: extern
domein: Fysieke leefomgeving
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
---

# Crematoriumregister

<!-- Gegenereerd door tools/render.py uit de beoordeling crematoriumregister.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Inzage in het openbare register van alle daar gecremeerde stoffelijke overschotten en de bestemming van de as dat de houder van een crematorium bijhoudt.

### Beschrijving

De houder van een crematorium houdt een register bij van alle daar gecremeerde stoffelijke overschotten en de bestemming van de as; het register is openbaar en gaat bij opheffing naar het archief van de gemeente waar de plaats lag (Wet op de lijkbezorging art. 50). Is de gemeente houder, dan biedt zij de inzage aan. Het register zelf is een representatie, zonder pagina; de inhoud staat in het Besluit op de lijkbezorging (art. 10).

De UPL noemt alleen bedrijven als afnemer en rekent het product tot de Dienstenwet (UPL).

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
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | realiseert *realisatie* | Crematoriumregister | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 50) |
| [Exploiteren van begraafplaatsen](../../../bedrijfsfuncties/fysieke-leefomgeving/exploiteren-van-begraafplaatsen.md) | omvat *aggregatie* | Crematoriumregister | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 106 (GEMMA-domein Fysieke leefomgeving)) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Crematoriumregister | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (UPL nr. 106, art. 50) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
