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
data_object: nee
afnemer: extern
domein: Bestuur
bronnen:
- 2026-logius-upl-actueel
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
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

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Afnemer**: extern.
- **Domein**: Bestuur.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

Alleen de kenmerken met ja; de overige 48 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, product in de UPL van Logius (rij 330, dwangsom bij niet tijdig beslissen); gangbaar als de dwangsom bij niet tijdig beslissen (Awb § 4.1.3.2). [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md), [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, het gemeentelijke bestuursorgaan dat een beschikking op aanvraag te laat geeft, verbeurt de dwangsom aan de aanvrager en stelt haar bij beschikking vast (art. 4:17, 4:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, een eigen product in de UPL, niet een onderdeel van één ander begrip (rij 330). [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij besluitvorming: de dwangsom geldt voor elke beschikking op aanvraag die niet tijdig wordt gegeven (Awb art. 4:17). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat de gemeente aanbiedt: een vergoeding als zij te laat beslist. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) |
| **aangeboden gedrag**: Is het een afgebakende prestatie die de gemeente aan haar omgeving aanbiedt, beschreven vanuit de behoefte van de afnemer en los van hoe zij wordt uitgevoerd? | Ja, een prestatie voor de aanvrager: na een ingebrekestelling krijgt hij een dwangsom per dag dat de beschikking uitblijft, ten hoogste 42 dagen (art. 4:17; UPL rij 330). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een beschikking die verschuldigdheid en hoogte van de dwangsom vaststelt, en de betaling ervan (art. 4:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke beschikking op aanvraag die na een ingebrekestelling niet tijdig wordt gegeven. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, paragraaf 4.1.3.2 Awb: ingebrekestelling, bedragen per dag, ten hoogste 42 dagen, vaststelling binnen twee weken, uitzonderingen (art. 4:17–4:20). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger en bedrijf (UPL rij 330): de aanvrager van de beschikking (art. 4:17 lid 1). [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md), [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert? | Ja, het bedrijfsproces Vaststellen dwangsom bij niet tijdig beslissen (art. 4:17, 4:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (rij 330); geen bredere dienst in deze wiki. [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) |

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
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen dienst of proces voor de dwangsom bij niet tijdig beslissen. Nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 28](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (product, open): **UPL:** de UPL van Logius noemt dwangsom bij niet tijdig beslissen als product van onder meer gemeenten, met grondslag art. 4:17 Awb ([2026-logius-upl-actueel](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md), rij 330). De UPL-lijst extern van GEMMA noemt het niet ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md)). **Bevinding:** elk gemeentelijk bestuursorgaan dat een beschikking op aanvraag na een ingebrekestelling niet tijdig geeft, verbeurt een dwangsom aan de aanvrager en stelt die bij beschikking vast ([2026-rijk-algemene-wet-bestuursrecht-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), art. 4:17, 4:18). Het is daarmee een wettelijke taak van elke gemeente. GEMMA modelleert het als de dienst Dwangsom bij niet tijdig beslissen, gerealiseerd door het generieke proces Vaststellen dwangsom bij niet tijdig beslissen. **Voorstel:** neem dwangsom bij niet tijdig beslissen op in de UPL-lijst extern, met grondslag art. 4:17 Awb, domein Bestuur.

### Besluiten redacteur

- 2026-10-12: Dienst Dwangsom bij niet tijdig beslissen, gerealiseerd door het generieke bedrijfsproces Vaststellen dwangsom bij niet tijdig beslissen; procesarchitectuur-terugmelding: de dienst ontbreekt in de UPL-lijst extern van GEMMA. Geen plek in de Functie-indeling naar domein: GEMMA heeft geen functie voor de dwangsom bij niet tijdig beslissen, en welke elementtypen op welk niveau worden ingedeeld, moet eerst worden bepaald (todo, Indelingen). *Stand: open: Functie-indeling naar domein (todo)*
