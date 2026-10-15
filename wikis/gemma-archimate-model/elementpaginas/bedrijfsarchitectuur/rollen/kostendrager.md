---
id: kostendrager
type: rol
archimate_type: business-role
status: review
naam: Kostendrager
onderwerpen:
- lijkbezorging
definitie: Verantwoordelijkheid voor het dragen van de kosten van een voorziening of handeling.
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Kostendrager

<!-- Gegenereerd door tools/render.py uit de beoordeling kostendrager.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid voor het dragen van de kosten van een voorziening of handeling.

### Beschrijving

Een kostendrager betaalt voor een voorziening of handeling die een ander uitvoert of die hij zelf laat uitvoeren, en kan de kosten soms verhalen.

### Per onderwerp

#### [Lijkbezorging](../../../onderwerpen/lijkbezorging/begrippen.md)

De gemeente draagt de kosten van de lijkbezorging als de burgemeester ervoor zorgt omdat niemand anders erin voorziet, en kan ze verhalen op de nalatenschap, onderhoudsplichtige verwanten of de werkgever (Wet op de lijkbezorging art. 22).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: gemeente.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Verzorgen gemeentebegrafenis](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verzorgen-gemeentebegrafenis.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Kostendrager | draagt de kosten van *toewijzing* | [Verzorgen gemeentebegrafenis](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verzorgen-gemeentebegrafenis.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Gemeente](../actoren/gemeente.md) | vervult *toewijzing* | Kostendrager | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor wie de kosten draagt; nieuw voor GEMMA.
