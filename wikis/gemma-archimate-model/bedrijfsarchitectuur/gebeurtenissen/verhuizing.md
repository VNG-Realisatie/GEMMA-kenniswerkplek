---
id: verhuizing
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Verhuizing
onderwerpen:
- burgerzaken
definitie: Het gaan wonen van een persoon op een ander adres in Nederland.
grondslag: bron
match:
  gemma: geen
data_object: nee
synoniemen:
- Adreswijziging (wet)
bronnen:
- 2026-utrecht-burgerzaken-verhuizing-doorgeven
- 2026-rvig-hup-binnengemeentelijke-adreswijziging
- 2026-rvig-hup-intergemeentelijke-adreswijziging
- 2026-rijk-wet-brp-bwbr0033715
---

# Verhuizing

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verhuizing.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het gaan wonen van een persoon op een ander adres in Nederland.

### Beschrijving

Bij een verhuizing binnen of naar een gemeente doet de persoon aangifte van adreswijziging in de nieuwe gemeente (Utrecht Verhuizing doorgeven; HUP Intergemeentelijke adreswijziging).

### Synoniemen

| Synoniem | Context |
|---|---|
| Adreswijziging | wet |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md).

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar (Utrecht Verhuizing doorgeven; HUP Binnengemeentelijke adreswijziging). [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, wordt aangegeven bij de gemeente en start gemeentelijk gedrag (HUP Binnengemeentelijke adreswijziging). [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, gebeurt op één moment en heeft gevolgen voor de inschrijving. [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke persoon die het overkomt. [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start Verwerken adreswijziging (HUP Binnengemeentelijke en Intergemeentelijke adreswijziging). [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere gebeurtenis in deze wiki. [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verhuizing | leidt tot *triggering* | [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md) | [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (HUP inleiding; Utrecht inleiding; Wet BRP art. 2.39 lid 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verhuizing | [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) (Wet BRP art. 2.20, 2.39) |
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Verhuizing | [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.39) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Verhuizing doorgeven](../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) | Gemeente Utrecht: Verhuizing doorgeven |
| [HUP Binnengemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) | HUP BRP: Binnengemeentelijke adreswijziging |
| [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) | HUP BRP: Intergemeentelijke adreswijziging |
| [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
