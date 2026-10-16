---
id: emigratie
type: gebeurtenis
archimate_type: business-event
status: review
naam: Emigratie
onderwerpen:
- burgerzaken
definitie: Het vertrek van een ingezetene om ten minste acht maanden van een jaar in het buitenland te wonen.
match:
  gemma: geen
synoniemen:
- Vertrek naar het buitenland (wet)
bronnen:
- 2026-utrecht-burgerzaken-emigratie-doorgeven
- 2026-rvig-hup-emigratie
- 2026-rijk-wet-brp-bwbr0033715
---

# Emigratie

<!-- Gegenereerd door tools/render.py uit de beoordeling emigratie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het vertrek van een ingezetene om ten minste acht maanden van een jaar in het buitenland te wonen.

### Beschrijving

Wie in een jaar acht maanden of langer in het buitenland gaat wonen, emigreert; ook een verhuizing naar het Caribisch deel van het Koninkrijk geldt als emigratie (Utrecht Emigratie doorgeven; HUP Emigratie).

### Synoniemen

| Synoniem | Context |
|---|---|
| Vertrek naar het buitenland | wet |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Verwerken emigratie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md).

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke persoon die het overkomt. [Utrecht Emigratie doorgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Verwerken emigratie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Emigratie | leidt tot *triggering* | [Verwerken emigratie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md) | [HUP Emigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.43 lid 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Emigratie | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [HUP Emigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) (Wet BRP art. 2.21, 2.43) |
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Emigratie | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.43) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Emigratie doorgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) | Gemeente Utrecht: Emigratie doorgeven |
| [HUP Emigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
