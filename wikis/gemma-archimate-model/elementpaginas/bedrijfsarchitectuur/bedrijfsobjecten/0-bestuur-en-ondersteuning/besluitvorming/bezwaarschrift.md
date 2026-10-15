---
id: bezwaarschrift
type: bedrijfsobject
archimate_type: business-object
status: review
naam: Bezwaarschrift
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Geschrift waarmee een belanghebbende bezwaar maakt tegen een besluit bij het bestuursorgaan dat het nam.
match:
  ggm: geen
  gemma: geen
data_object: nee
objectniveau: generiek
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
---

# Bezwaarschrift

<!-- Gegenereerd door tools/render.py uit de beoordeling bezwaarschrift.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Geschrift waarmee een belanghebbende bezwaar maakt tegen een besluit bij het bestuursorgaan dat het nam.

### Beschrijving

Bezwaar maken gaat door het indienen van een bezwaarschrift bij het bestuursorgaan dat het besluit nam (Awb art. 6:4 lid 1). Het bezwaarschrift is ondertekend en bevat ten minste naam en adres van de indiener, de dagtekening, een omschrijving van het besluit en de gronden van het bezwaar (art. 6:5). De termijn is zes weken na de bekendmaking van het besluit (art. 6:7, 6:8); voldoet het bezwaarschrift niet aan de eisen, dan kan het na een herstelmogelijkheid niet-ontvankelijk worden verklaard (art. 6:6). Voor het horen ligt het met de andere stukken ter inzage (art. 7:4).

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Mutaties door bedrijfsprocessen**: [Behandelen bezwaar](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-bezwaar.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, wetsterm en gangbaar: een bezwaarschrift indienen (Awb art. 6:4, 6:5). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, het gemeentelijke bestuursorgaan dat het besluit nam, ontvangt het bezwaarschrift en beslist erop (art. 6:4 lid 1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig als het geschrift waarmee bezwaar wordt gemaakt, met eigen eisen aan de inhoud; het is geen onderdeel van het bestreden besluit (art. 6:4, 6:5). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij besluitvorming: de Awb regelt het bezwaarschrift voor elk besluit (art. 6:4, 6:5). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elk bezwaarschrift heeft een indiener, een dagtekening, een bestreden besluit en gronden (art. 6:5 lid 1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, wordt ingediend, eventueel hersteld, ter inzage gelegd bij het horen, en eindigt in de beslissing op bezwaar of de niet-ontvankelijkverklaring (art. 6:6, 7:4, 7:11). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, behandelen bezwaar ontvangt en behandelt het bezwaarschrift (art. 6:4–6:6, 7:4). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder object in deze wiki. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt met dezelfde betekenis voor in elk onderwerp waarin de gemeente besluiten neemt (art. 6:4, 7:1). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Bezwaarschrift | is gericht tegen *associatie (gericht)* | [Besluit](besluit.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 6:5 lid 1 onder c, 7:11) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen bezwaar](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-bezwaar.md) | behandelt *toegang (registreren)* | Bezwaarschrift | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 6:4–6:6, 7:4) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |

### Afstemming met GGM

Geen GGM-entiteit. Het GGM kent geen bezwaar of bezwaarschrift. Het ontstaat bij de belanghebbende en wordt behandeld in Behandelen bezwaar (Awb art. 6:4, 7:11); hiaat, GGM-terugmelding.

GGM-terugmeldingen:

- [Nummer 20](../../../../../modellen/ggm/terugmeldingen.md) (hiaat, open): **GGM:** het GGM kent geen bezwaar of bezwaarschrift. **Bevinding:** een belanghebbende maakt bezwaar tegen een besluit door een bezwaarschrift in te dienen bij het bestuursorgaan dat het besluit nam; dat bestuursorgaan hoort de belanghebbenden, heroverweegt het besluit en beslist op het bezwaar ([2026-rijk-algemene-wet-bestuursrecht-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), art. 6:4, 6:5, 7:2, 7:10–7:12). Elke gemeente behandelt bezwaarschriften, in elk domein. Relevante attributen: indiener (naam en adres) en eventuele gemachtigde; dagtekening en datum van ontvangst; bestreden besluit (relatie naar Besluit); gronden van het bezwaar; ontvankelijk, met datum van herstel van een verzuim; datum van horen, met verslag; advies van een adviescommissie; beslistermijn en verdaging; beslissing op bezwaar (gegrond, ongegrond, niet-ontvankelijk) en datum. **Voorstel:** opnemen als entiteit Bezwaarschrift in RGBZPlus, naast Besluit, met een relatie naar het bestreden Besluit en naar het besluit dat de beslissing op bezwaar is.

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen bedrijfsobject bezwaarschrift; nieuw voor GEMMA.
