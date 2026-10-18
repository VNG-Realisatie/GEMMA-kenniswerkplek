---
id: regeling
type: bedrijfsobject
archimate_type: business-object
status: review
naam: Regeling
onderwerpen:
- besluitvorming
- lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Algemeen verbindend voorschrift van een overheid, zoals een wet, algemene maatregel van bestuur of gemeentelijke verordening.
match:
  ggm: geen
  gemma: sterk
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

<!-- Gegenereerd door tools/render.py uit de beoordeling regeling.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur. De beslistabel legt dit element voor (zie *Ter discussie*).

## Ter discussie

- homoniem van Regeling (GGM, Inkomen): naamkeuze voorleggen

## Betekenis

### Definitie

Algemeen verbindend voorschrift van een overheid, zoals een wet, algemene maatregel van bestuur of gemeentelijke verordening.

### Beschrijving

Een regeling bevat algemeen verbindende voorschriften van een overheid, zoals een wet, een algemene maatregel van bestuur of een gemeentelijke verordening. De gemeenteraad stelt de gemeentelijke verordeningen vast, voor zover die bevoegdheid niet bij het college of de burgemeester ligt (Gemeentewet art. 147, 149). Een concreet benoemde landelijke wet of VNG-modelverordening is daarnaast een beleidskader.

### Per onderwerp

#### [Lijkbezorging](../../../../../onderwerpen/lijkbezorging/begrippen.md)

De gemeenteraad stelt een beheersverordening begraafplaatsen vast, met de regels voor graven, grafrechten, grafbedekkingen en ruiming; de VNG biedt daarvoor een model (VNG Wet op de lijkbezorging; Groningen). De wet laat de raad verordenen over onder meer de tijden van begraven (art. 35, 90).

### Naamkeuze

Overwogen: Regeling (GEMMA, gangbaar), Regelgeving, Algemeen verbindend voorschrift (Awb). Gekozen is Regeling, in lijn met het GEMMA-element; het GGM-begrip Regeling (Inkomen) is een ander begrip en krijgt hier geen pagina.

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| Regeling (GGM-entiteiten Regeling in Terug- en invordering, Diensten en Model Inkomen) | Afspraak of regeling met een cliënt (terugbetaling, voorziening) | Deze pagina heet Regeling: de soort wet of verordening; het GGM-begrip krijgt hier geen pagina. |

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief, object (3 toetskenmerken ja).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Specialisaties per onderwerp

#### Lijkbezorging

- **Beheersverordening begraafplaatsen**: Specialisatie zonder pagina van Regeling: verordening van de gemeente over beheer en gebruik van haar begraafplaatsen (VNG; Groningen; VNG-modelverordening). Genoemd door [Gemeentewet](../../../../motivatie/beleidskaders/rijksregelgeving/gemeentewet.md).

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: object.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-wet-op-de-lijkbezorging.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Bekendmaken besluit](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/bekendmaken-besluit.md). [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-wet-op-de-lijkbezorging.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, standaard. [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-wet-op-de-lijkbezorging.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, standaard. [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md), [VNG Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-wet-op-de-lijkbezorging.md) |

### Specialisaties

- **Beheersverordening begraafplaatsen**: Verordening waarin de gemeente de regels voor de begraafplaats vastlegt; de VNG biedt een model (VNG; Groningen). Geen eigen pagina.
- **[Heffingsverordening](../belastingen/heffingsverordening.md)**: Verordening over de heffing van belastingen en rechten.
- **[Participatieverordening](../participatie/participatieverordening.md)**: Verordening van de raad over de manier waarop inwoners en maatschappelijke partijen bij het beleid worden betrokken, met het uitdaagrecht (Gemeentewet art. 150).

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Regeling | regelt (beheersverordening begraafplaatsen) *associatie (gericht)* | [Begraafplaats](../../7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/begraafplaats.md) | [VNG Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-wet-op-de-lijkbezorging.md), [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) (VNG inleiding; Groningen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bekendmaken besluit](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/bekendmaken-besluit.md) | plaatst in het gemeenteblad *toegang (verstrekken)* | Regeling | [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md) (art. 6, 8) |
| [Gemeentewet](../../../../motivatie/beleidskaders/rijksregelgeving/gemeentewet.md) | is grondslag voor *associatie (gericht)* | Regeling | [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 147 lid 1, 149) |
| [Heffingsverordening](../belastingen/heffingsverordening.md) | is een *specialisatie* | Regeling | [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) (art. 216) |
| [Model-APV](../../../../motivatie/beleidskaders/gemeentelijke-regelgeving/model-apv.md) | is model voor (algemene plaatselijke verordening) *associatie (gericht)* | Regeling | [Model-APV](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-vng-model-apv.md) (aanhef; leeswijzer) |
| [Participatieverordening](../participatie/participatieverordening.md) | is een *specialisatie* | Regeling | [Gemeentewet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-gemeentewet-wettekst.md), [VNG Model Participatieverordening](../../../../../onderwerpen/participatie/bronduidingen/gemeentelijke-regelgeving/2024-vng-model-participatieverordening.md) (Gemeentewet art. 150 lid 1; model aanhef) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Gemeentewet](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2024-rijk-gemeentewet-wettekst.md) | Gemeentewet (BWBR0005416) - geldend per 2024-01-31 |
| [VNG Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-vng-wet-op-de-lijkbezorging.md) | Wet op de lijkbezorging |
| [Beheersverordening begraafplaatsen Groningen](../../../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md) | Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023 |

### Afstemming met GGM

Geen GGM-entiteit. De drie GGM-entiteiten Regeling (Inkomen) zijn een ander begrip (homoniem); geen GGM-grondslag.

GGM-terugmeldingen:

- [Nummer 10](../../../../../modellen/ggm/terugmeldingen.md) (homoniem, open): **GGM:** Regeling is een afspraak of regeling met een cliënt (Terug- en invordering, Diensten, Model Inkomen). **Bevinding:** GEMMA en het spraakgebruik gebruiken Regeling voor de soort wet of verordening (algemeen verbindend voorschrift; Gemeentewet art. 147, 149). **Voorstel:** de GGM-entiteiten een specifiekere naam geven, bijvoorbeeld Cliëntregeling of Betalingsregeling, en in alle drie de domeinen dezelfde naam gebruiken.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Regeling* (business-object). Zelfde begrip (verzamelnaam voor AMvB's, ministeriële regelingen, lokale verordeningen); nieuw: een herkenbare definitie.

> Verzamelnaam voor AMvB’s, Ministeriële regelingen, lokale verordeningen, etc. De regeling is de meest concrete uitleg van de wet.

### Besluiten redacteur

- 2026-10-10: Wordt bewerkt zonder toegang: het proces dat een regeling vaststelt of raadpleegt, komt bij het onderwerp Heffingen en betalingen (via de specialisatie Heffingsverordening) of een later onderwerp; tot dan blijft het signaal staan. *Zekerheid: logica.*
