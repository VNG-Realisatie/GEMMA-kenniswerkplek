---
id: bekendmaken-besluit
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Bekendmaken besluit
onderwerpen:
- besluitvorming
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Het kenbaar maken van een genomen besluit of vastgestelde regeling, door toezending aan belanghebbenden of plaatsing in het gemeenteblad.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Bekendmaken (GEMMA)
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2026-rijk-bekendmakingswet-wettekst
- 2025-vng-upl-producten-en-diensten-extern
---

# Bekendmaken besluit

<!-- Gegenereerd door tools/render.py uit de beoordeling bekendmaken-besluit.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het kenbaar maken van een genomen besluit of vastgestelde regeling, door toezending aan belanghebbenden of plaatsing in het gemeenteblad.

### Beschrijving

Een besluit treedt niet in werking voordat het is bekendgemaakt (Awb art. 3:40). Het bestuursorgaan zendt een besluit dat tot belanghebbenden is gericht aan hen toe of reikt het uit; een algemeen verbindend voorschrift, een beleidsregel of een ander besluit dat niet tot belanghebbenden is gericht, plaatst het in het gemeenteblad, dat het college uitgeeft (art. 3:41, 3:42; Bekendmakingswet art. 2 lid 2, 6). Tegelijk of kort daarna doet het mededeling aan wie een zienswijze gaf; na de uniforme openbare voorbereidingsprocedure legt het het besluit met de stukken ter inzage en geeft het daarvan kennis (Awb art. 3:43, 3:44; Bekendmakingswet art. 12, 13). Bekendmaking en mededeling vermelden of, binnen welke termijn en bij wie bezwaar of beroep openstaat (Awb art. 3:45). Een algemeen verbindend voorschrift treedt zonder andere aanduiding op de achtste dag na de bekendmaking in werking (Bekendmakingswet art. 8, 10 lid 2).

### Deelprocessen

1. **Bekendmaken aan belanghebbenden**: Het bestuursorgaan zendt het besluit toe of reikt het uit aan de belanghebbenden tot wie het is gericht, onder wie de aanvrager (Awb art. 3:41). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)
2. **Plaatsen in het gemeenteblad**: Een algemeen verbindend voorschrift, een beleidsregel of een besluit zonder geadresseerden wordt in het gemeenteblad geplaatst (Awb art. 3:42; Bekendmakingswet art. 6). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md)
3. **Doen van mededeling**: Mededeling aan wie een zienswijze gaf, en na afdeling 3.4 kennisgeving van de terinzagelegging; met de vermelding van bezwaar en beroep (Awb art. 3:43–3:45; Bekendmakingswet art. 12, 13). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md)

### Synoniemen

| Synoniem | Context |
|---|---|
| Bekendmaken | GEMMA |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Kernobject**: [Besluit](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Besluit](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md), [Regeling](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/regeling.md), [Beleidsregel](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beleidsregel.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Besluit genomen (gebeurtenis, nog geen element): Een genomen besluit of vastgestelde regeling, die pas na bekendmaking in werking treedt (Awb art. 3:40; Bekendmakingswet art. 8). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, het bekendgemaakte besluit, dat in werking treedt, met de vermelding van bezwaar en beroep; de mededelingen aan wie een zienswijze gaf (art. 3:40, 3:43, 3:45). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elk besluit en elke regeling. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, afdeling 3.6 Awb en de Bekendmakingswet: wijze van bekendmaken, mededeling, vermelding van bezwaar en beroep, inwerkingtreding, terinzagelegging (Awb art. 3:40–3:45; Bekendmakingswet art. 6, 8, 10, 12, 13). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met Beheren besluiten (bedrijfsproces, nog geen element): Eén mutatie in de levensloop van een besluit: van genomen tot in werking (Awb art. 3:40). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, loopt van het genomen besluit tot het moment dat de belanghebbenden en ieder het kennen en het in werking treedt (art. 3:40–3:45). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Bekendmaking](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/bekendmaking.md), [Bekendmaking algemeen verbindend voorschrift](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/bekendmaking-algemeen-verbindend-voorschrift.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Bekendmaken besluit | realiseert *realisatie* | [Bekendmaking](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/bekendmaking.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 3:40; UPL nr. 47) |
| Bekendmaken besluit | realiseert *realisatie* | [Bekendmaking algemeen verbindend voorschrift](../../../diensten/0-bestuur-en-ondersteuning/besluitvorming/bekendmaking-algemeen-verbindend-voorschrift.md) | [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (art. 6, 8; UPL nr. 48) |
| Bekendmaken besluit | maakt bekend *toegang (verstrekken)* | [Besluit](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/besluit.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 3:41, 3:42) |
| Bekendmaken besluit | plaatst in het gemeenteblad *toegang (verstrekken)* | [Regeling](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/regeling.md) | [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md) (art. 6, 8) |
| Bekendmaken besluit | maakt bekend *toegang (verstrekken)* | [Beleidsregel](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beleidsregel.md) | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 3:42, 4:83) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | maakt het besluit bekend en doet mededeling *toewijzing* | Bekendmaken besluit | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md) (Awb art. 3:41–3:43; Bekendmakingswet art. 6) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [Bekendmakingswet](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-bekendmakingswet-wettekst.md) | Bekendmakingswet (BWBR0004287) |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent alleen smallere toepassingen: de procesbouwsteen Bekendmaken besluit vergunningaanvraag (id-f2fcbce2-f5ae-4f84-8b52-7c07fe8f3062) en het Deelproces Bekendmaken bij het omgevingsplan (id-d77cf7f1-2756-4b4a-8d17-ade11dbc9d6c). Nieuw voor GEMMA als generiek proces.
