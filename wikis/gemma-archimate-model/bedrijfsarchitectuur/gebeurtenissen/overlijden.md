---
id: overlijden
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Overlijden
onderwerpen:
- lijkbezorging
definitie: Het sterven van een persoon.
grondslag: bron
match:
  gemma: geen
data_object: nee
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rvo-aangifte-en-akte-van-overlijden
---

# Overlijden

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/overlijden.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het sterven van een persoon.

### Beschrijving

Het overlijden van een persoon wordt aangegeven bij de gemeente waar de persoon is overleden; voor de aangifte is een verklaring van overlijden nodig (Ondernemersplein).

### Per onderwerp

#### [Lijkbezorging](../../begrippen/lijkbezorging.md)

Het overlijden start de schouwing van het lijk (Wet op de lijkbezorging art. 3) en de termijn waarbinnen de lijkbezorging moet plaatsvinden: niet eerder dan 36 uur en uiterlijk op de zesde werkdag (art. 16).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Bezorgen lijken](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-lijken.md), [Schouwen lijk](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-lijk.md), [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md).

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, wordt aangegeven bij de gemeente en start gemeentelijk gedrag (RVO; art. 3, 16). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? | Ja, wordt in geen ander onderwerp beoordeeld; wat het in de lijkbezorging start, staat onder per_onderwerp. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, gebeurt op één moment en heeft gevolgen. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke overledene. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start het ketenproces Bezorgen lijken, met Schouwen lijk (art. 3) en de termijn voor de lijkbezorging (art. 16). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere gebeurtenis in deze wiki. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Overlijden | leidt tot *triggering* | [Schouwen lijk](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-lijk.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |
| Overlijden | leidt tot *triggering* | [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 16) |
| Overlijden | start *triggering* | [Bezorgen lijken](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-lijken.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 16) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-04: Niet generiek: Overlijden is een specifieke gebeurtenis, geen specialisatie van een generieke GEMMA-gebeurtenis; geen voorstel aan GEMMA.
