---
id: schriftelijke-klacht
type: bedrijfsobject
archimate_type: business-object
status: review
naam: Schriftelijke klacht
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Schriftelijke klacht over de manier waarop een bestuursorgaan of een medewerker zich heeft gedragen.
match:
  ggm: geen
  gemma: geen
data_object: nee
objectniveau: generiek
synoniemen:
- Klaagschrift (wet)
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
---

# Schriftelijke klacht

<!-- Gegenereerd door tools/render.py uit de beoordeling schriftelijke-klacht.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Schriftelijke klacht over de manier waarop een bestuursorgaan of een medewerker zich heeft gedragen.

### Beschrijving

Een schriftelijke klacht, in de wet ook klaagschrift, is een klacht over een gedraging van een bestuursorgaan jegens de klager die schriftelijk wordt ingediend. Zij is ondertekend en bevat ten minste naam en adres van de indiener, de dagtekening en een omschrijving van de gedraging (Awb art. 9:4). Het bestuursorgaan bevestigt de ontvangst schriftelijk, houdt de schriftelijke klachten bij en publiceert ze jaarlijks (art. 9:6, 9:12a). Een mondelinge klacht wordt ook behoorlijk behandeld, maar zonder deze vaste regels (art. 9:2).

### Synoniemen

| Synoniem | Context |
|---|---|
| Klaagschrift | wet |

### Naamkeuze

Schriftelijke klacht: de gangbare term, die ook in de wet staat (Awb art. 9:2, 9:4 lid 1); de wetsterm Klaagschrift is een synoniem (regel Bronvoorrang). De naam Klacht is van de UPL-dienst.

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Mutaties door bedrijfsprocessen**: [Behandelen klacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-klacht.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: ding. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elke schriftelijke klacht heeft een indiener, een dagtekening en een gedraging waarover geklaagd wordt (art. 9:4 lid 2). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, wordt ingediend, ontvangen en bevestigd, behandeld of niet in behandeling genomen, afgehandeld en jaarlijks gepubliceerd (art. 9:6, 9:8, 9:11, 9:12a). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Behandelen klacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-klacht.md). |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt met dezelfde betekenis voor in elk onderwerp, voor elk bestuursorgaan (art. 9:1, 9:4). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen klacht](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-klacht.md) | behandelt *toegang (registreren)* | Schriftelijke klacht | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 9:4, 9:6, 9:12a) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |

### Afstemming met GGM

Geen GGM-entiteit. Het GGM kent geen algemene klacht; alleen GEMMA heeft het bedrijfsobject Klacht Leerlingenvervoer, een specialisatie voor één domein. Zij ontstaat bij de klager en wordt behandeld in Behandelen klacht (Awb art. 9:4, 9:12a); hiaat, GGM-terugmelding.

GGM-terugmeldingen:

- [Nummer 21](../../../../../modellen/ggm/terugmeldingen.md) (hiaat, open): **GGM:** het GGM kent geen algemene klacht; alleen een klacht over leerlingenvervoer. **Bevinding:** ieder kan bij een bestuursorgaan een klacht indienen over de manier waarop het zich heeft gedragen. Het bestuursorgaan bevestigt de ontvangst, hoort de klager, handelt de klacht binnen zes weken af met een gemotiveerd oordeel, en registreert en publiceert de schriftelijke klachten ([2026-rijk-algemene-wet-bestuursrecht-wettekst](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), art. 9:1, 9:4, 9:6, 9:10–9:12a). Elke gemeente behandelt klachten, in elk domein. Relevante attributen: klager (naam en adres); dagtekening en datum van ontvangst, met ontvangstbevestiging; omschrijving van de gedraging, met datum en betrokken medewerker of orgaan; in behandeling genomen, of de reden om dat niet te doen; datum van horen, met verslag; advies van een klachtadviescommissie; afhandeltermijn en verdaging; oordeel (gegrond, ongegrond) en conclusies, met datum. **Voorstel:** opnemen als entiteit Klacht (of Schriftelijke klacht) in RGBZPlus, voor alle domeinen; Klacht Leerlingenvervoer wordt daar een specialisatie van.

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen algemeen bedrijfsobject klacht; Klacht Leerlingenvervoer (uit het GGM) is een specialisatie voor leerlingenvervoer. Nieuw voor GEMMA.
