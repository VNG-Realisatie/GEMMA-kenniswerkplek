---
id: bezwaar
type: dienst
archimate_type: business-service
status: review
naam: Bezwaar
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Het maken van bezwaar tegen een besluit bij het bestuursorgaan dat het nam, zodat het het besluit heroverweegt.
match:
  gemma: geen
afnemer: extern
domein: Bestuur
synoniemen:
- Bezwaar maken (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
---

# Bezwaar

<!-- Gegenereerd door tools/render.py uit de beoordeling bezwaar.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het maken van bezwaar tegen een besluit bij het bestuursorgaan dat het nam, zodat het het besluit heroverweegt.

### Beschrijving

Een belanghebbende die het niet eens is met een besluit, maakt bezwaar door binnen zes weken na de bekendmaking een bezwaarschrift in te dienen bij het bestuursorgaan dat het besluit nam (Awb art. 6:4 lid 1, 6:7, 6:8). Bezwaar gaat in de regel vooraf aan beroep bij de bestuursrechter; dat geldt niet voor een besluit dat met de uniforme openbare voorbereidingsprocedure is voorbereid (art. 7:1). Het bestuursorgaan hoort de belanghebbenden, heroverweegt het besluit en beslist binnen zes weken, of binnen twaalf weken als een adviescommissie adviseert (art. 7:2, 7:10, 7:11). De UPL noemt de dienst voor burgers en bedrijven (nr. 64).

### Synoniemen

| Synoniem | Context |
|---|---|
| Bezwaar maken | wet |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Afnemer**: extern.
- **Domein**: Bestuur.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Behandelen bezwaar](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-bezwaar.md). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Algemene wet bestuursrecht](../../../../motivatie/beleidskaders/rijksregelgeving/algemene-wet-bestuursrecht.md) | is grondslag voor *associatie (gericht)* | Bezwaar | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 6:4, 7:1) |
| [Behandelen bezwaar](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-bezwaar.md) | realiseert *realisatie* | Bezwaar | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 7:1; UPL nr. 64) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst bezwaar; wel het bedrijfsproces Behandelen bezwaar, dat de wiki koppelt aan het realiserende proces. Nieuw voor GEMMA.
