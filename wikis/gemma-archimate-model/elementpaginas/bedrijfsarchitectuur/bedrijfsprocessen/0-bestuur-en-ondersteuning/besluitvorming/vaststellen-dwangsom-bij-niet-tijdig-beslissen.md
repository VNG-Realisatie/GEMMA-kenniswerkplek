---
id: vaststellen-dwangsom-bij-niet-tijdig-beslissen
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Vaststellen dwangsom bij niet tijdig beslissen
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Het vaststellen en betalen van de dwangsom die de gemeente verschuldigd is als zij na een ingebrekestelling niet tijdig op een aanvraag beslist.
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2026-logius-upl-actueel
---

# Vaststellen dwangsom bij niet tijdig beslissen

<!-- Gegenereerd door tools/render.py uit de beoordeling vaststellen-dwangsom-bij-niet-tijdig-beslissen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het vaststellen en betalen van de dwangsom die de gemeente verschuldigd is als zij na een ingebrekestelling niet tijdig op een aanvraag beslist.

### Beschrijving

Is de beslistermijn voor een beschikking op aanvraag verstreken, dan kan de aanvrager het bestuursorgaan schriftelijk in gebreke stellen. Vanaf twee weken na ontvangst verbeurt het bestuursorgaan een dwangsom per dag, ten hoogste 42 dagen (Awb art. 4:17). Het stelt verschuldigdheid en hoogte bij beschikking vast binnen twee weken na de laatste dag waarover de dwangsom verschuldigd was (art. 4:18). Bezwaar tegen de beschikking op de aanvraag geldt ook voor deze beschikking, voor zover de belanghebbende haar betwist (art. 4:19); een onverschuldigd betaalde dwangsom kan binnen vijf jaar worden teruggevorderd (art. 4:20). De ingebrekestelling start het proces en is geen eigen element.

### Deelprocessen

1. **Ontvangen ingebrekestelling**: Het bestuursorgaan ontvangt de schriftelijke ingebrekestelling na het verstrijken van de beslistermijn; twee weken later begint de dwangsom te lopen (art. 4:17 lid 3). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
2. **Vaststellen dwangsom**: Het bestuursorgaan stelt verschuldigdheid en hoogte bij beschikking vast binnen twee weken na de laatste dag, rekening houdend met de uitzonderingen (art. 4:17 lid 5, 4:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Kernobject**: [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Belanghebbende](../../../rollen/belanghebbende.md), [Beslisser](../../../rollen/beslisser.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md), [Aanvraag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/aanvraag.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een schriftelijke ingebrekestelling door de aanvrager na het verstrijken van de beslistermijn (art. 4:17 lid 3). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de beschikking tot vaststelling van verschuldigdheid en hoogte van de dwangsom (art. 4:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke ingebrekestelling na een te late beschikking op aanvraag. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, paragraaf 4.1.3.2 Awb: aanvang twee weken na de ingebrekestelling, bedragen per dag, ten hoogste 42 dagen, vaststelling binnen twee weken, terugvordering (art. 4:17, 4:18, 4:20). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, eén mutatie in de levensloop van een beschikking: de vaststelling van de dwangsom bij een te late beschikking (art. 4:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, loopt van de ingebrekestelling door de aanvrager tot de beschikking tot vaststelling aan hem (art. 4:17 lid 3, 4:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, eindigt in de beschikking tot vaststelling van de dwangsom van het bestuursorgaan (art. 4:18). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Dwangsom bij niet tijdig beslissen](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/dwangsom-bij-niet-tijdig-beslissen.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vaststellen dwangsom bij niet tijdig beslissen | realiseert *realisatie* | [Dwangsom bij niet tijdig beslissen](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/dwangsom-bij-niet-tijdig-beslissen.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) (art. 4:17; UPL rij 330) |
| Vaststellen dwangsom bij niet tijdig beslissen | stelt de dwangsom vast bij *toegang (registreren)* | [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:18) |
| Vaststellen dwangsom bij niet tijdig beslissen | raadpleegt *toegang (raadplegen)* | [Aanvraag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/aanvraag.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:17 lid 1, 5) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Belanghebbende](../../../rollen/belanghebbende.md) | stelt als aanvrager in gebreke *toewijzing* | Vaststellen dwangsom bij niet tijdig beslissen | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:17 lid 3, 5) |
| [Beslisser](../../../rollen/beslisser.md) | stelt de dwangsom bij beschikking vast *toewijzing* | Vaststellen dwangsom bij niet tijdig beslissen | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:18) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) | Uniforme Productnamenlijst (UPL), actueel |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor de dwangsom bij niet tijdig beslissen. Nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-12: De ingebrekestelling start het proces en is geen eigen element. *Zekerheid: logica.*
