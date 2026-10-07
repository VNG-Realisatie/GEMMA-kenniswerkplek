---
id: overlijden
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Overlijden
onderwerpen:
- burgerzaken
- lijkbezorging
definitie: Het sterven van een persoon.
grondslag: bron
match:
  gemma: geen
data_object: nee
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rvo-aangifte-en-akte-van-overlijden
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-utrecht-burgerzaken-overlijden-aangifte-doen
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-van-rechtswege-vervallen-reisdocument
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

Het overlijden start de schouwing van het stoffelijk overschot (Wet op de lijkbezorging art. 3) en de termijn waarbinnen de lijkbezorging moet plaatsvinden: niet eerder dan 36 uur en uiterlijk op de zesde werkdag (art. 16).

#### [Burgerzaken](../../begrippen/burgerzaken.md)

Het overlijden wordt aangegeven bij de ambtenaar van de burgerlijke stand van de gemeente van overlijden, die de akte van overlijden opmaakt (BW 1 art. 19f, 19h). De woongemeente verwerkt het in de BRP: de bijhouding van de persoonslijst wordt opgeschort, en bij een echtgenoot of geregistreerd partner wordt de ontbinding door overlijden verwerkt (HUP Overlijden in Nederland).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Bezorgen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md), [Opmaken akte van overlijden](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md), [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md), [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md), [Verval van het reisdocument](verval-van-het-reisdocument.md).

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, wordt aangegeven bij de gemeente en start gemeentelijk gedrag (RVO; art. 3, 16). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, wordt in geen ander onderwerp beoordeeld; wat het in de lijkbezorging start, staat onder per_onderwerp. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, gebeurt op één moment en heeft gevolgen. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke overledene. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start het ketenproces Bezorgen stoffelijk overschot, met Schouwen stoffelijk overschot (art. 3) en de termijn voor de lijkbezorging (art. 16). In de burgerlijke stand start het de aangifte en het opmaken van de akte van overlijden (BW 1 art. 19f, 19h). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere gebeurtenis in deze wiki. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Specialisaties

- **Lijkvinding**: Het vinden van een stoffelijk overschot van een onbekende of niet aangegeven overledene; de hulpofficier van justitie doet aangifte en datum en plaats van de vinding gelden als die van het overlijden (Besluit burgerlijke stand art. 62; HUP Lijkvinding). Geen eigen pagina.
- **Rechtsvermoeden van overlijden**: Een uitspraak van de rechtbank dat een vermiste wordt vermoed te zijn overleden, ingeschreven in de registers (HUP Rechtsvermoeden van overlijden). Geen eigen pagina.
- **Overlijden in het buitenland**: Verwerkt op een buitenlandse, consulaire of Haagse akte (HUP Overlijden buitenland). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Overlijden | leidt tot *triggering* | [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |
| Overlijden | leidt tot *triggering* | [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 16) |
| Overlijden | start *triggering* | [Bezorgen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 16) |
| Overlijden | leidt tot *triggering* | [Opmaken akte van overlijden](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md) | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Overlijden, aangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) (art. 19f, 19h; Utrecht inleiding) |
| Overlijden | doet het reisdocument vervallen *triggering* | [Verval van het reisdocument](verval-van-het-reisdocument.md) | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder f; HUP Van rechtswege vervallen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bezorgen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md) | omvat *aggregatie* | Overlijden | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 16) |
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Overlijden | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19f, 19h) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Ondernemersplein Aangifte overlijden](../../bronanalyses/lijkbezorging/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |
| [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Utrecht Overlijden, aangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) | Gemeente Utrecht: Overlijden |
| [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) | HUP BRP: Van rechtswege vervallen reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-04: Niet generiek: Overlijden is een specifieke gebeurtenis, geen specialisatie van een generieke GEMMA-gebeurtenis; geen voorstel aan GEMMA.
- 2026-10-05: Stoffelijk overschot in lopende tekst: per onderwerp lijkbezorging.
- 2026-10-07: Thuisonderwerp Burgerzaken (regel Thuishoren): het overlijden verandert de toestand van de Ingeschreven persoon en wordt vastgelegd in de akte van overlijden (BW 1 art. 19f, 19h); Lijkbezorging gebruikt de gebeurtenis met een relatie, de tekst voor lijkbezorging staat per onderwerp. Het object in Archi blijft.
