---
id: beleidsregel
type: bedrijfsobject
archimate_type: business-object
status: review
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

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Algemene regel die een bestuursorgaan bij besluit vaststelt over hoe het een bevoegdheid gebruikt, zonder algemeen verbindend voorschrift te zijn.

### Beschrijving

Een beleidsregel is een bij besluit vastgestelde algemene regel, niet zijnde een algemeen verbindend voorschrift, over de afweging van belangen, de vaststelling van feiten of de uitleg van wettelijke voorschriften bij het gebruik van een bevoegdheid van een bestuursorgaan (Awb art. 1:3 lid 4). Een bestuursorgaan kan beleidsregels vaststellen voor een bevoegdheid die het heeft of heeft gedelegeerd (art. 4:81). Het bestuursorgaan handelt ernaar, tenzij dat voor een belanghebbende door bijzondere omstandigheden onevenredige gevolgen heeft, en kan ter motivering van een besluit naar de beleidsregel verwijzen (art. 4:82, 4:84). De beleidsregel wordt bekendgemaakt zoals een besluit dat niet tot belanghebbenden is gericht (art. 3:42).

Een beleidsregel bindt alleen het bestuursorgaan zelf, anders dan een Regeling, die iedereen bindt; en zij gaat over het gebruik van één bevoegdheid, anders dan een Beleidsnota, die het beleid voor een onderwerp vastlegt.

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief, object (3 toetskenmerken ja).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: object.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Bekendmaken besluit](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/bekendmaken-besluit.md), Vaststellen beleidsregel (bedrijfsproces, nog geen element): Het bestuursorgaan stelt haar vast (art. 4:81), maakt haar bekend (art. 3:42, 4:83) en past haar toe bij het nemen van besluiten: het handelt ernaar en mag ernaar verwijzen ter motivering (art. 4:82, 4:84). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |

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
