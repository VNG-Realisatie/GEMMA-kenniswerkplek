---
id: klager
type: rol
archimate_type: business-role
status: review
naam: Klager
onderwerpen:
- besluitvorming
definitie: Hoedanigheid van degene die een klacht indient over de manier waarop een bestuursorgaan zich heeft gedragen.
match:
  gemma: geen
data_object: nee
doelgroep: inwoners en ondernemers
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
---

# Klager

<!-- Gegenereerd door tools/render.py uit de beoordeling klager.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Hoedanigheid van degene die een klacht indient over de manier waarop een bestuursorgaan zich heeft gedragen.

### Beschrijving

Ieder heeft het recht een klacht in te dienen over de manier waarop een bestuursorgaan zich jegens hem of een ander heeft gedragen (Awb art. 9:1); wie dat doet, is klager. De klager krijgt een ontvangstbevestiging, wordt gehoord en krijgt een gemotiveerd oordeel, met de ombudsman bij wie hij daarna terecht kan (art. 9:6, 9:10, 9:12). Anders dan een belanghebbende hoeft de klager geen belang bij een besluit te hebben.

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Behandelen klacht](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-klacht.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Klager | dient de klacht in en wordt gehoord *toewijzing* | [Behandelen klacht](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-klacht.md) | [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 9:4, 9:10, 9:12) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol klager; de rol Klant heeft geen definitie en omvat elke afnemer. Nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-12: Nieuwe generieke rol in Besluitvorming: ieder kan klagen, ook over een gedraging jegens een ander, dus de rol Belanghebbende past niet (Awb art. 9:1). *Zekerheid: kennis.*
