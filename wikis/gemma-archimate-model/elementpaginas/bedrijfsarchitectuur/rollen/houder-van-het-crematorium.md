---
id: houder-van-het-crematorium
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Houder van het crematorium
onderwerpen:
- lijkbezorging
definitie: Verantwoordelijkheid voor een crematorium, het bergen van de as en de bestemming daarvan.
match:
  gemma: geen
doelgroep: gemeente
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Houder van het crematorium

<!-- Gegenereerd door tools/render.py uit de beoordeling houder-van-het-crematorium.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid voor een crematorium, het bergen van de as en de bestemming daarvan.

### Beschrijving

De houder van het crematorium bergt de as in asbussen, bewaart ze en zorgt voor de bestemming van de as, en houdt een openbaar register van gecremeerde stoffelijke overschotten (art. 50, 58, 59). Bij een gemeentelijk crematorium is de gemeente houder, bij een bijzonder crematorium een kerkgenootschap, rechtspersoon of natuurlijk persoon (art. 51, 52).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (1 toetskenmerken ja).

### Plaats in de indelingen

- **Doelgroep**: gemeente.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md), [Beheren crematoria](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/beheren-crematoria.md). [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Houder van het crematorium | bergt de as bij, zorgt voor de bewaring en de bestemming van de as bij *toewijzing* | [Uitvoeren lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvoeren-lijkbezorging.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 58; art. 59) |
| Houder van het crematorium | houdt *toegang (houder)* | [Crematorium](../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/crematorium.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 50) |
| Houder van het crematorium | bergt as in en bewaart *toegang (houder)* | [Urn](../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/urn.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 58, 59 lid 1) |
| Houder van het crematorium | houdt in werking *toewijzing* | [Beheren crematoria](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/beheren-crematoria.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 50, 52) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Gemeente](../actoren/gemeente.md) | vervult *toewijzing* | Houder van het crematorium | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 51) |
| [Kerkgenootschap](../actoren/kerkgenootschap.md) | vervult *toewijzing* | Houder van het crematorium | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 52) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
