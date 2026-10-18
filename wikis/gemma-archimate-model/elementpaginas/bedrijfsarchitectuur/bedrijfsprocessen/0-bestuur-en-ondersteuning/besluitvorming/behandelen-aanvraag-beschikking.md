---
id: behandelen-aanvraag-beschikking
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen aanvraag beschikking
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: 'Het beslissen op een aanvraag om een beschikking: de aanvraag ontvangen en zo nodig laten aanvullen, het besluit voorbereiden en binnen de termijn beslissen.'
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2025-vng-upl-producten-en-diensten-extern
---

# Behandelen aanvraag beschikking

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-aanvraag-beschikking.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beslissen op een aanvraag om een beschikking: de aanvraag ontvangen en zo nodig laten aanvullen, het besluit voorbereiden en binnen de termijn beslissen.

### Beschrijving

Een belanghebbende dient een aanvraag om een beschikking schriftelijk in bij het bevoegde bestuursorgaan (Awb art. 1:3 lid 3, 4:1, 4:2). Is de aanvraag onvolledig, dan krijgt de aanvrager gelegenheid haar aan te vullen; anders kan het bestuursorgaan besluiten haar niet te behandelen (art. 4:5). Steunt een voorgenomen afwijzing op gegevens die afwijken van wat de aanvrager zelf gaf, of heeft een andere belanghebbende naar verwachting bedenkingen, dan kan die vooraf zijn zienswijze geven (art. 4:7–4:9). Het bestuursorgaan geeft de beschikking binnen de wettelijke termijn, of anders binnen een redelijke termijn van ten hoogste acht weken; lukt dat niet, dan meldt het een nieuwe termijn, en de termijn wordt opgeschort tijdens het aanvullen (art. 4:13–4:15). Is een wettelijk voorschrift of het bestuursorgaan dat zo bepaalt, dan wordt het besluit voorbereid met de uniforme openbare voorbereidingsprocedure (art. 3:10). De beslisprocessen op aanvraag in de onderwerpen, zoals Behandelen aanvraag reisdocument, zijn gevallen van dit generieke proces.

### Deelprocessen

1. **Ontvangen aanvraag**: Het bestuursorgaan ontvangt de aanvraag, toetst de indieningseisen en laat haar zo nodig aanvullen, of besluit haar niet te behandelen (art. 4:1–4:5). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
2. **Voorbereiden beschikking**: Het bestuursorgaan verzamelt de kennis over feiten en belangen en stelt de aanvrager of een derde-belanghebbende zo nodig in de gelegenheid zijn zienswijze te geven (art. 3:2, 4:7–4:9). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
3. **Beslissen op aanvraag**: Het bestuursorgaan geeft de beschikking binnen de beslistermijn, of meldt een nieuwe termijn (art. 4:13–4:15). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)

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
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Aanvraag ingediend (gebeurtenis, nog geen element): Een aanvraag van een belanghebbende om een beschikking (art. 1:3 lid 3, 4:1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de beschikking op de aanvraag, toewijzend of afwijzend, of het besluit de aanvraag niet te behandelen (art. 1:3 lid 2, 4:5). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke aanvraag om een beschikking. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, afdeling 4.1 Awb: indieningseisen, aanvullen, zienswijze van aanvrager en derden, beslistermijn en opschorting (art. 4:1–4:15). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met Beheren beschikkingen (bedrijfsproces, nog geen element): Eén mutatie in de levensloop van een beschikking: van aanvraag tot gegeven beschikking (art. 4:1, 4:13). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, loopt van de aanvraag van de belanghebbende tot de beschikking aan hem (art. 4:1, 4:13). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, eindigt in de beschikking van het bevoegde bestuursorgaan (art. 1:3 lid 2, 4:1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Beschikking aanvragen](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/beschikking-aanvragen.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen aanvraag beschikking | realiseert *realisatie* | [Beschikking aanvragen](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/beschikking-aanvragen.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 1:3, 4:1; UPL nr. 55) |
| Behandelen aanvraag beschikking | geeft *toegang (registreren)* | [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 1:3 lid 2, 4:13) |
| Behandelen aanvraag beschikking | neemt in behandeling *toegang (raadplegen)* | [Aanvraag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/aanvraag.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:1, 4:5) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Belanghebbende](../../../rollen/belanghebbende.md) | vraagt de beschikking aan of geeft als derde zijn zienswijze *toewijzing* | Behandelen aanvraag beschikking | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 1:3 lid 3, 4:7, 4:8) |
| [Beslisser](../../../rollen/beslisser.md) | beslist op de aanvraag en geeft de beschikking *toewijzing* | Behandelen aanvraag beschikking | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:1, 4:13) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen generiek proces voor elke beschikking op aanvraag; Behandelen aanvraag product (producten die gereed liggen) en Behandelen aanvraag vergunning of ontheffing (toestemmingen) zijn smaller. Nieuw voor GEMMA.
