---
id: verzoeker-om-naturalisatie
type: rol
archimate_type: business-role
status: review
naam: Verzoeker om naturalisatie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Hoedanigheid van degene die een verzoek om naturalisatie indient om Nederlander te worden.
match:
  gemma: geen
data_object: nee
doelgroep: inwoners en ondernemers
synoniemen:
- Verzoeker (wet)
bronnen:
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
- 2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie
- 2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738
---

# Verzoeker om naturalisatie

<!-- Gegenereerd door tools/render.py uit de beoordeling verzoeker-om-naturalisatie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Hoedanigheid van degene die een verzoek om naturalisatie indient om Nederlander te worden.

### Beschrijving

De verzoeker dient het verzoek schriftelijk, ondertekend en in persoon in, ook voor de minderjarige kinderen die in de naturalisatie delen; voor een minderjarige treedt de wettelijke vertegenwoordiger op (Rijkswet op het Nederlanderschap art. 2 lid 3, 7, 11; Besluit verkrijging en verlies Nederlanderschap art. 3, 31). Na het besluit verschijnt hij op oproeping bij de uitreiking en legt hij de verklaring van verbondenheid af (Besluit art. 60b).

### Synoniemen

| Synoniem | Context |
|---|---|
| Verzoeker | wet |

### Naamkeuze

De wet spreekt van verzoeker (Besluit art. 3, 31); dat is te algemeen voor het hele model. Verzoeker om naturalisatie volgt het precedent Rechthebbende op het graf en Houder van het reisdocument: de rol heet naar waar zij op betrekking heeft.

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
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Behandelen naturalisatieverzoek](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-naturalisatieverzoek.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verzoeker om naturalisatie | dient het verzoek in, legt de verklaring van verbondenheid af *toewijzing* | [Behandelen naturalisatieverzoek](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-naturalisatieverzoek.md) | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 3, 33; art. 60b lid 2 en 4) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Naturalisatieceremonie](../diensten/0-bestuur-en-ondersteuning/burgerzaken/naturalisatieceremonie.md) | bedient *bediening* | Verzoeker om naturalisatie | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 60b; Utrecht) |
| [Naturalisatieverzoek](../diensten/0-bestuur-en-ondersteuning/burgerzaken/naturalisatieverzoek.md) | bedient *bediening* | Verzoeker om naturalisatie | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 3; Utrecht) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) | Gemeente Utrecht: Nederlander worden door naturalisatie of optie |
| [Rijkswet op het Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) | Rijkswet op het Nederlanderschap |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
