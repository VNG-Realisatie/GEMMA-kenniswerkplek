---
id: optant
type: rol
archimate_type: business-role
status: review
naam: Optant
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Hoedanigheid van degene die een optieverklaring aflegt om Nederlander te worden.
match:
  gemma: geen
doelgroep: inwoners en ondernemers
bronnen:
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
---

# Optant

<!-- Gegenereerd door tools/render.py uit de beoordeling optant.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Hoedanigheid van degene die een optieverklaring aflegt om Nederlander te worden.

### Beschrijving

De optant legt de verklaring schriftelijk en in persoon af, verstrekt gegevens over zichzelf en de personen die hij in zijn optie betrekt, en verklaart dat die naar waarheid zijn (Besluit verkrijging en verlies Nederlanderschap art. 3, 6). Voor een minderjarige treedt de wettelijke vertegenwoordiger op (Rijkswet op het Nederlanderschap art. 2 lid 3; Besluit art. 60a lid 2). Na de bevestiging verschijnt de optant op oproeping bij de uitreiking en legt hij de verklaring van verbondenheid af (Besluit art. 60a). Utrecht spreekt van aanvrager.

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Behandelen optieverklaring](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Optant | legt de optieverklaring af, legt de verklaring van verbondenheid af *toewijzing* | [Behandelen optieverklaring](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md) | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 3, 6, 7; art. 60a lid 2 en 4) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Naturalisatieceremonie](../diensten/0-bestuur-en-ondersteuning/burgerzaken/naturalisatieceremonie.md) | bedient *bediening* | Optant | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 60a; Utrecht) |
| [Naturalisatieoptie](../diensten/0-bestuur-en-ondersteuning/burgerzaken/naturalisatieoptie.md) | bedient *bediening* | Optant | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 3; Utrecht) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
