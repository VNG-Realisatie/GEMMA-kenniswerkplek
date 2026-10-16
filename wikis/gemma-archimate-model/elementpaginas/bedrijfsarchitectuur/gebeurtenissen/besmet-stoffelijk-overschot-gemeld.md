---
id: besmet-stoffelijk-overschot-gemeld
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Besmet stoffelijk overschot gemeld
onderwerpen:
- lijkbezorging
definitie: De burgemeester heeft van de GGD de melding ontvangen dat een stoffelijk overschot besmet is met gevaar voor de volksgezondheid.
match:
  gemma: geen
synoniemen:
- Melding besmet lijk (wet)
- Besmet lijk gemeld (wet)
bronnen:
- 2026-rijk-wet-publieke-gezondheid-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
---

# Besmet stoffelijk overschot gemeld

<!-- Gegenereerd door tools/render.py uit de beoordeling besmet-stoffelijk-overschot-gemeld.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

De burgemeester heeft van de GGD de melding ontvangen dat een stoffelijk overschot besmet is met gevaar voor de volksgezondheid.

### Beschrijving

De arts die vaststelt dat een stoffelijk overschot besmet is met een infectieus of giftig agens of stof met ernstig gevaar voor de volksgezondheid, meldt dat onverwijld aan de GGD (Wet publieke gezondheid art. 21 lid 2); de GGD geeft de ontvangst onverwijld door aan de burgemeester van de gemeente waarin het stoffelijk overschot zich bevindt (art. 27 lid 3).

### Synoniemen

| Synoniem | Context |
|---|---|
| Melding besmet lijk | wet |
| Besmet lijk gemeld | wet |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Treffen maatregel bij besmet stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/treffen-maatregel-bij-besmet-stoffelijk-overschot.md).

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elk besmet lijk. [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Treffen maatregel bij besmet stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/treffen-maatregel-bij-besmet-stoffelijk-overschot.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Besmet stoffelijk overschot gemeld | leidt tot *triggering* | [Treffen maatregel bij besmet stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/treffen-maatregel-bij-besmet-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) (Wlb art. 22a; Wpg art. 27 lid 3) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Toestaan lijkbezorging](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/toestaan-lijkbezorging.md) | omvat *aggregatie* | Besmet stoffelijk overschot gemeld | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a; Wpg art. 27 lid 3) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) | Wet publieke gezondheid (BWBR0024705) |
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.
