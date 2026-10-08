---
id: emigratie
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Emigratie
onderwerpen:
- burgerzaken
definitie: Het vertrek van een ingezetene om ten minste acht maanden van een jaar in het buitenland te wonen.
grondslag: bron
match:
  gemma: geen
data_object: nee
synoniemen:
- Vertrek naar het buitenland (wet)
bronnen:
- 2026-utrecht-burgerzaken-emigratie-doorgeven
- 2026-rvig-hup-emigratie
---

# Emigratie

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/emigratie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

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

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar (Utrecht Emigratie doorgeven; HUP Emigratie). [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, wordt aangegeven bij de gemeente en start gemeentelijk gedrag (HUP Emigratie). [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, gebeurt op één moment en heeft gevolgen voor de inschrijving. [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke persoon die het overkomt. [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start Verwerken emigratie (HUP Emigratie). [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere gebeurtenis in deze wiki. [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Emigratie | leidt tot *triggering* | [Verwerken emigratie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md) | [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) (inleiding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Emigratie | [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) (Wet BRP art. 2.21, 2.43) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Emigratie doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-emigratie-doorgeven.md) | Gemeente Utrecht: Emigratie doorgeven |
| [HUP Emigratie](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
