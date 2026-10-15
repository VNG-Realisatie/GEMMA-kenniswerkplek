---
id: toezichthouder-brp
type: rol
archimate_type: business-role
status: review
naam: Toezichthouder BRP
onderwerpen:
- burgerzaken
definitie: Verantwoordelijkheid voor het toezicht op de juistheid van de inschrijving in de basisregistratie personen, onder meer met een huisbezoek.
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2023-rvig-circulaire-adresonderzoek-brp
- 2026-rijk-wet-brp-bwbr0033715
---

# Toezichthouder BRP

<!-- Gegenereerd door tools/render.py uit de beoordeling toezichthouder-brp.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid voor het toezicht op de juistheid van de inschrijving in de basisregistratie personen, onder meer met een huisbezoek.

### Beschrijving

De toezichthouder BRP heeft de bevoegdheid inlichtingen op te vragen en legt bij een adresonderzoek huisbezoeken af; het college kan ook externen tot onbezoldigd ambtenaar en toezichthouder benoemen (Circulaire adresonderzoek 4.4, 4.5).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Toezichthouder*. De toezichthouder BRP is een toezichthouder voor de basisregistratie personen (Circulaire adresonderzoek 4.4).
- **Doelgroep**: gemeente.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Uitvoeren adresonderzoek](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitvoeren-adresonderzoek.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Toezichthouder BRP | legt huisbezoek af *toewijzing* | [Uitvoeren adresonderzoek](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitvoeren-adresonderzoek.md) | [RvIG Circulaire adresonderzoek BRP](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (4.5; Wet BRP art. 4.2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Toezichthouder BRP | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 4.2) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [RvIG Circulaire adresonderzoek BRP](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) | Circulaire adresonderzoek BRP |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
