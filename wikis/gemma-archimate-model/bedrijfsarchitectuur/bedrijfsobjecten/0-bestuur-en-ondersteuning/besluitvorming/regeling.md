---
id: regeling
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Regeling
onderwerpen:
- algemeen
- lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Algemeen verbindend voorschrift van een overheid, zoals een wet, algemene maatregel van bestuur of gemeentelijke verordening.
grondslag: regelgeving
match:
  ggm: geen
  gemma: sterk
data_object: nee
objectniveau: generiek
bronnen:
- 2024-rijk-gemeentewet-wettekst
- 2026-vng-wet-op-de-lijkbezorging
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
gemma_id: id-e5771904f7a442de8f07744a66d37ef0
gemma_naam: Regeling
gemma_type: business-object
gemma_definitie: Verzamelnaam voor AMvB’s, Ministeriële regelingen, lokale verordeningen, etc. De regeling is de meest concrete uitleg van de wet.
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-4613c364-53f2-445d-a392-3b6661533a71
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{C25455F3-FEB0-4c6d-9AA4-3B027718BEE3}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: 4613c364-53f2-445d-a392-3b6661533a71
---

# Regeling

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/regeling.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Algemeen verbindend voorschrift van een overheid, zoals een wet, algemene maatregel van bestuur of gemeentelijke verordening.

### Beschrijving

Een regeling bevat algemeen verbindende voorschriften van een overheid, zoals een wet, een algemene maatregel van bestuur of een gemeentelijke verordening. De gemeenteraad stelt de gemeentelijke verordeningen vast, voor zover die bevoegdheid niet bij het college of de burgemeester ligt (Gemeentewet art. 147, 149). Een concreet benoemde landelijke wet of VNG-modelverordening is daarnaast een beleidskader.

### Per onderwerp

#### [Lijkbezorging](../../../../begrippen/lijkbezorging.md)

De gemeenteraad stelt een beheersverordening begraafplaatsen vast, met de regels voor graven, grafrechten, grafbedekkingen en ruiming; de VNG biedt daarvoor een model (VNG Wet op de lijkbezorging; Groningen). De wet laat de raad verordenen over onder meer de tijden van begraven (art. 35, 90).

### Naamkeuze

Overwogen: Regeling (GEMMA, gangbaar), Regelgeving, Algemeen verbindend voorschrift (Awb). Gekozen is Regeling, in lijn met het GEMMA-element; het GGM-begrip Regeling (Inkomen) is een ander begrip en krijgt hier geen pagina (besluit redacteur 2026-10-01).

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| Regeling (GGM-entiteiten Regeling in Terug- en invordering, Diensten en Model Inkomen) | Afspraak of regeling met een cliënt (terugbetaling, voorziening) | Deze pagina heet Regeling: de soort wet of verordening; het GGM-begrip krijgt hier geen pagina. |

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Specialisaties per onderwerp

#### Lijkbezorging

- **Beheersverordening begraafplaatsen**: Specialisatie zonder pagina van Regeling: verordening van de gemeente over beheer en gebruik van haar begraafplaatsen (VNG; Groningen; VNG-model).

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar als verzamelnaam (GEMMA); de soort wet of verordening. [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/overig/2026-vng-wet-op-de-lijkbezorging.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de raad stelt verordeningen vast (Gemeentewet art. 147, 149). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/overig/2026-vng-wet-op-de-lijkbezorging.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/overig/2026-vng-wet-op-de-lijkbezorging.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/overig/2026-vng-wet-op-de-lijkbezorging.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elke regeling apart. [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, vastgesteld, gewijzigd, ingetrokken (Groningen art. 31). [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, de raad stelt de beheersverordening vast; beheerder en college passen haar toe en stellen nadere regels (Gemeentewet art. 149; Groningen intitulé, art. 2 lid 2). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, het hoogste herkenbare niveau voor de beheersverordening begraafplaatsen; de gemeentelijke verordening is een specialisatie (besluit redacteur 2026-09-30). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, regelingen komen in elk onderwerp voor; de gemeentelijke verordening op grond van de Gemeentewet (art. 147). [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) |

### Specialisaties

- **Beheersverordening begraafplaatsen**: Verordening waarin de gemeente de regels voor de begraafplaats vastlegt; de VNG biedt een model (VNG; Groningen). Geen eigen pagina.
- **[Heffingsverordening](../belastingen/heffingsverordening.md)**: Verordening over de heffing van belastingen en rechten.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Regeling | regelt (beheersverordening begraafplaatsen) *associatie (gericht)* | [Begraafplaats](../../7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | [VNG Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/overig/2026-vng-wet-op-de-lijkbezorging.md), [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (VNG inleiding; Groningen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Heffingsverordening](../belastingen/heffingsverordening.md) | is een *specialisatie* | Regeling | [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 216) |
| [Model-APV](../../../../motivatie/beleidskaders/gemeentelijke-regelgeving/model-apv.md) | is model voor (algemene plaatselijke verordening) *associatie (gericht)* | Regeling | [Model-APV](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-vng-model-apv.md) (aanhef; leeswijzer) |
| [Model-beheersverordening begraafplaatsen](../../../../motivatie/beleidskaders/gemeentelijke-regelgeving/model-beheersverordening-begraafplaatsen.md) | is model voor (beheersverordening begraafplaatsen) *associatie (gericht)* | Regeling | [VNG Model-beheersverordening begraafplaatsen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md), [VNG Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/overig/2026-vng-wet-op-de-lijkbezorging.md) (aanhef; VNG inleiding) |

## Herkomst

### Bronnen

De soort regeling: algemeen verbindende voorschriften (Gemeentewet art. 147, 149); voor dit onderwerp de beheersverordening begraafplaatsen (Groningen, VNG-model).

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../../../bronanalyses/lijkbezorging/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [VNG Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/overig/2026-vng-wet-op-de-lijkbezorging.md) | Wet op de lijkbezorging |
| [Beheersverordening begraafplaatsen Groningen](../../../../bronanalyses/lijkbezorging/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GGM

Geen GGM-entiteit. De drie GGM-entiteiten Regeling (Inkomen) zijn een ander begrip (homoniem); geen GGM-grondslag.

GGM-terugmeldingen:

- [Nummer 10](../../../../terugmeldingen/ggm-terugmeldingen.md) (homoniem, open): **GGM:** Regeling is een afspraak of regeling met een cliënt (Terug- en invordering, Diensten, Model Inkomen). **Bevinding:** GEMMA en het spraakgebruik gebruiken Regeling voor de soort wet of verordening (algemeen verbindend voorschrift; Gemeentewet art. 147, 149). **Voorstel:** de GGM-entiteiten een specifiekere naam geven, bijvoorbeeld Cliëntregeling of Betalingsregeling, en in alle drie de domeinen dezelfde naam gebruiken.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Regeling* (business-object). Zelfde begrip (verzamelnaam voor AMvB's, ministeriële regelingen, lokale verordeningen); nieuw: een herkenbare definitie.

> Verzamelnaam voor AMvB’s, Ministeriële regelingen, lokale verordeningen, etc. De regeling is de meest concrete uitleg van de wet.

### Besluiten redacteur

- 2026-09-30: Element op het hoogste herkenbare niveau voor de beheersverordening begraafplaatsen; opname akkoord.
- 2026-10-01: Naam Regeling houden, in lijn met GEMMA; het GGM-homoniem staat bij Homoniemen.
