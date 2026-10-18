---
id: dwangsom-bij-niet-tijdig-beslissen
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Dwangsom bij niet tijdig beslissen
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Een geldbedrag per dag dat de gemeente de aanvrager betaalt als zij na een ingebrekestelling niet tijdig op zijn aanvraag beslist.
match:
  gemma: geen
afnemer: extern
domein: Bestuur
bronnen:
- 2026-logius-upl-actueel
---

# Dwangsom bij niet tijdig beslissen

<!-- Gegenereerd door tools/render.py uit de beoordeling dwangsom-bij-niet-tijdig-beslissen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Een geldbedrag per dag dat de gemeente de aanvrager betaalt als zij na een ingebrekestelling niet tijdig op zijn aanvraag beslist.

### Beschrijving

Geeft een bestuursorgaan een beschikking op aanvraag niet binnen de beslistermijn, dan kan de aanvrager het schriftelijk in gebreke stellen. Twee weken daarna verbeurt het bestuursorgaan een dwangsom voor elke dag dat het in gebreke is, ten hoogste 42 dagen, oplopend van € 23 tot € 45 per dag (Awb art. 4:17). Geen dwangsom is verschuldigd als de aanvrager geen belanghebbende is, of de aanvraag kennelijk niet-ontvankelijk of ongegrond is (art. 4:17 lid 5). Het bestuursorgaan stelt de dwangsom bij beschikking vast binnen twee weken na de laatste dag (art. 4:18). De UPL van Logius noemt de dienst voor burgers en bedrijven (rij 330); de UPL-lijst van GEMMA noemt haar niet.

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
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Vaststellen dwangsom bij niet tijdig beslissen](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/vaststellen-dwangsom-bij-niet-tijdig-beslissen.md). [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, standaard. [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Algemene wet bestuursrecht](../../../../motivatie/beleidskaders/rijksregelgeving/algemene-wet-bestuursrecht.md) | is grondslag voor *associatie (gericht)* | Dwangsom bij niet tijdig beslissen | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:17, 4:18) |
| [Vaststellen dwangsom bij niet tijdig beslissen](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/vaststellen-dwangsom-bij-niet-tijdig-beslissen.md) | realiseert *realisatie* | Dwangsom bij niet tijdig beslissen | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) (art. 4:17; UPL rij 330) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) | Uniforme Productnamenlijst (UPL), actueel |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst of proces voor de dwangsom bij niet tijdig beslissen. Nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 28](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (product, open): **UPL:** de UPL van Logius noemt dwangsom bij niet tijdig beslissen als product van onder meer gemeenten, met grondslag art. 4:17 Awb ([2026-logius-upl-actueel](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md), rij 330). De UPL-lijst extern van GEMMA noemt het niet ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md)). **Bevinding:** elk gemeentelijk bestuursorgaan dat een beschikking op aanvraag na een ingebrekestelling niet tijdig geeft, verbeurt een dwangsom aan de aanvrager en stelt die bij beschikking vast ([2026-rijk-algemene-wet-bestuursrecht-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), art. 4:17, 4:18). Het is daarmee een wettelijke taak van elke gemeente. GEMMA modelleert het als de dienst Dwangsom bij niet tijdig beslissen, gerealiseerd door het generieke proces Vaststellen dwangsom bij niet tijdig beslissen. **Voorstel:** neem dwangsom bij niet tijdig beslissen op in de UPL-lijst extern, met grondslag art. 4:17 Awb, domein Bestuur.
