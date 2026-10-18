---
id: beleidsregel
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Beleidsregel
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Algemene regel die een bestuursorgaan bij besluit vaststelt over hoe het een bevoegdheid gebruikt, zonder algemeen verbindend voorschrift te zijn.
match:
  ggm: geen
  gemma: geen
objectniveau: generiek
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
---

# Beleidsregel

<!-- Gegenereerd door tools/render.py uit de beoordeling beleidsregel.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Algemene regel die een bestuursorgaan bij besluit vaststelt over hoe het een bevoegdheid gebruikt, zonder algemeen verbindend voorschrift te zijn.

### Beschrijving

Een beleidsregel is een bij besluit vastgestelde algemene regel, niet zijnde een algemeen verbindend voorschrift, over de afweging van belangen, de vaststelling van feiten of de uitleg van wettelijke voorschriften bij het gebruik van een bevoegdheid van een bestuursorgaan (Awb art. 1:3 lid 4). Een bestuursorgaan kan beleidsregels vaststellen voor een bevoegdheid die het heeft of heeft gedelegeerd (art. 4:81). Het bestuursorgaan handelt ernaar, tenzij dat voor een belanghebbende door bijzondere omstandigheden onevenredige gevolgen heeft, en kan ter motivering van een besluit naar de beleidsregel verwijzen (art. 4:82, 4:84). De beleidsregel wordt bekendgemaakt zoals een besluit dat niet tot belanghebbenden is gericht (art. 3:42).

Een beleidsregel bindt alleen het bestuursorgaan zelf, anders dan een Regeling, die iedereen bindt; en zij gaat over het gebruik van één bevoegdheid, anders dan een Beleidsnota, die het beleid voor een onderwerp vastlegt.

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: ding. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, per bevoegdheid een eigen beleidsregel, vastgesteld bij besluit (art. 1:3 lid 4, 4:81). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, wordt bij besluit vastgesteld en bekendgemaakt, en geldt tot zij wordt gewijzigd of ingetrokken (art. 1:3 lid 4, 3:42, 4:83). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Bekendmaken besluit](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/bekendmaken-besluit.md), Vaststellen beleidsregel (bedrijfsproces, nog geen element): Het bestuursorgaan stelt haar vast (art. 4:81), maakt haar bekend (art. 3:42, 4:83) en past haar toe bij het nemen van besluiten: het handelt ernaar en mag ernaar verwijzen ter motivering (art. 4:82, 4:84). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **generiek**: Komt het met dezelfde betekenis in veel onderwerpen voor? | Ja, komt met dezelfde betekenis voor in elk onderwerp waarin een bestuursorgaan een bevoegdheid heeft. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bekendmaken besluit](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/bekendmaken-besluit.md) | maakt bekend *toegang (verstrekken)* | Beleidsregel | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 3:42, 4:83) |
| [Beslisser](../../../rollen/beslisser.md) | houder *toegang (houder)* | Beleidsregel | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:81) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |

### Afstemming met GGM

Geen GGM-entiteit. Het GGM kent geen beleidsregel. Zij ontstaat in het besluit waarmee een bestuursorgaan haar vaststelt (art. 4:81), een proces dat de wiki nog niet heeft.

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen bedrijfsobject voor dit begrip (alleen technologie, zoals Policy editor); nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-12: Eigen generiek bedrijfsobject naast Regeling en Beleidsnota: een besluit van algemene strekking dat alleen het bestuursorgaan bindt (Awb art. 1:3 lid 4, 4:84), geen algemeen verbindend voorschrift en geen beleidsnota. *Zekerheid: kennis.*
