---
id: gemeentelijke-lijkschouwer
type: rol
archimate_type: business-role
status: review
naam: Gemeentelijke lijkschouwer
onderwerpen:
- lijkbezorging
definitie: Arts die door het college is benoemd om stoffelijke overschotten te schouwen.
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Gemeentelijke lijkschouwer

<!-- Gegenereerd door tools/render.py uit de beoordeling gemeentelijke-lijkschouwer.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Arts die door het college is benoemd om stoffelijke overschotten te schouwen.

### Beschrijving

Burgemeester en wethouders benoemen een of meer gemeentelijke lijkschouwers, uitsluitend forensisch artsen (art. 4, 5). Normaal schouwt de behandelend arts het stoffelijk overschot; de gemeentelijke lijkschouwer is de uitzondering en schouwt alleen als de behandelend arts dat niet doet, geeft een verklaring van overlijden af of waarschuwt bij een niet-natuurlijke dood de officier van justitie en de ambtenaar van de burgerlijke stand, en leidt het nader onderzoek bij een minderjarige (art. 3, 7, 10, 10a). Hij kan de elektronische weg openstellen voor mededelingen van de behandelend arts (art. 7 lid 3).

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
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Gemeentelijke lijkschouwer | verricht *toewijzing* | [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Arts](../actoren/arts.md) | vervult als forensisch arts *toewijzing* | Gemeentelijke lijkschouwer | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 4, 5) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
