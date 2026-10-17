---
id: beschikking-aanvragen
type: dienst
archimate_type: business-service
status: goedgekeurd
naam: Beschikking aanvragen
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Het aanvragen van een besluit van de gemeente in een concreet geval, zoals een vergunning of ontheffing.
match:
  gemma: geen
afnemer: extern
domein: Bestuur
synoniemen:
- Beschikking (UPL)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-logius-upl-actueel
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
---

# Beschikking aanvragen

<!-- Gegenereerd door tools/render.py uit de beoordeling beschikking-aanvragen.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het aanvragen van een besluit van de gemeente in een concreet geval, zoals een vergunning of ontheffing.

### Beschrijving

Een belanghebbende kan het bestuursorgaan vragen een beschikking te geven: een besluit in een concreet geval, zoals een vergunning (Awb art. 1:3). De aanvraag is schriftelijk, ondertekend en bevat ten minste naam en adres, dagtekening en de gevraagde beschikking (art. 4:1, 4:2). Het bestuursorgaan laat een onvolledige aanvraag aanvullen, hoort de aanvrager bij een voorgenomen afwijzing op afwijkende gegevens en geeft de beschikking binnen de wettelijke termijn of anders binnen acht weken (art. 4:5, 4:7, 4:13, 4:14). Het is het algemene aanbod waarvan de diensten op aanvraag in de onderwerpen, zoals een verlof of een reisdocument, gevallen zijn. De UPL noemt de dienst voor burgers en bedrijven (nr. 55).

### Synoniemen

| Synoniem | Context |
|---|---|
| Beschikking | UPL |

### Naamkeuze

Beschikking aanvragen: de dienst geformuleerd vanuit de afnemer, met de UPL-naam Beschikking als synoniem (precedent Rijbewijs aanvragen), zodat zij niet dezelfde naam draagt als het bedrijfsobject Beschikking.

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) (bedrijfsobject Beschikking in deze wiki) | Het besluit zelf, niet van algemene strekking (Awb art. 1:3 lid 2): het bedrijfsobject dat deze dienst oplevert | De dienst heet Beschikking aanvragen; het bedrijfsobject houdt de naam Beschikking. |

## Plaats in het model

### Typering

Dienst. Uitkomst van de beslistabel: Gedrag, *aangeboden gedrag* (kern ja, 2/2).

### Plaats in de indelingen

- **Afnemer**: extern.
- **Domein**: Bestuur.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, extern (Dienst). **Hoofdkenmerk**: gedrag. **Soort gedrag**: aangeboden gedrag. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een beschikking, ook als die de aanvraag afwijst (art. 1:3 lid 2). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke aanvraag om een beschikking. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, afdeling 4.1 Awb: indieningseisen, aanvullen, zienswijze bij een voorgenomen afwijzing, beslistermijn van ten hoogste acht weken (art. 4:1–4:15). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **afnemer**: Is er een afnemer buiten de uitvoerder aanwijsbaar, een klant intern of extern? | Ja, burger en bedrijf (UPL nr. 55): de aanvrager, een belanghebbende (art. 1:3 lid 3). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **gerealiseerd door**: Is er een proces of functie aanwijsbaar dat de dienst uitvoert, of een bedrijfsfunctie die het vermogen realiseert? | Ja, met [Behandelen aanvraag beschikking](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-aanvraag-beschikking.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, een eigen product in de UPL (nr. 55); de generieke dienst waarvan de diensten op aanvraag in de onderwerpen gevallen zijn; geen bredere dienst in deze wiki. [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Algemene wet bestuursrecht](../../../../motivatie/beleidskaders/rijksregelgeving/algemene-wet-bestuursrecht.md) | is grondslag voor *associatie (gericht)* | Beschikking aanvragen | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 1:3, afdeling 4.1) |
| [Behandelen aanvraag beschikking](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-aanvraag-beschikking.md) | realiseert *realisatie* | Beschikking aanvragen | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 1:3, 4:1; UPL nr. 55) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [UPL](../../../../../modellen/upl/bronduidingen/informatiemodel/2026-logius-upl-actueel.md) | Uniforme Productnamenlijst (UPL), actueel |
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen generieke dienst voor een beschikking; het bedrijfsobject Beschikking is een ander elementtype. Nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-12: De UPL-naam Beschikking is een synoniem van de dienst Beschikking aanvragen: zo is de dienst geen homoniem van het bedrijfsobject Beschikking. *Zekerheid: logica.*
