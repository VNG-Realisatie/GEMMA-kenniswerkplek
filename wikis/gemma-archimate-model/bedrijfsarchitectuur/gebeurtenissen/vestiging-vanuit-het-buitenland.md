---
id: vestiging-vanuit-het-buitenland
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Vestiging vanuit het buitenland
onderwerpen:
- burgerzaken
definitie: Het gaan wonen in een Nederlandse gemeente van een persoon die in het buitenland woonde.
grondslag: bron
match:
  gemma: geen
data_object: nee
bronnen:
- 2023-rvig-circulaire-adresonderzoek-brp
- 2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland
- 2026-rvig-hup-immigratie
- 2026-rvig-hup-hervestiging
---

# Vestiging vanuit het buitenland

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/vestiging-vanuit-het-buitenland.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het gaan wonen in een Nederlandse gemeente van een persoon die in het buitenland woonde.

### Beschrijving

Wie vanuit het buitenland in een gemeente komt wonen, of het komende half jaar ten minste vier maanden, schrijft zich binnen vijf dagen in (Utrecht Inschrijven vanuit het buitenland). Stond de persoon nooit in de BRP of RNI, dan is het een immigratie (eerste inschrijving); stond hij in de RNI, dan een hervestiging (HUP Immigratie; HUP Hervestiging).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md).

### Kenmerken

Alleen de kenmerken met ja; de overige 50 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar (Circulaire adresonderzoek 4.8; Utrecht Inschrijven vanuit het buitenland). [RvIG Circulaire adresonderzoek BRP](../../bronanalyses/burgerzaken/2023-rvig-circulaire-adresonderzoek-brp.md), [Utrecht Inschrijven vanuit het buitenland](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, leidt tot inschrijving door de gemeente (HUP Immigratie; HUP Hervestiging). [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, gebeurt op één moment en heeft gevolgen voor de inschrijving. [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke persoon die het overkomt. [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start Inschrijven ingezetene (HUP Immigratie; HUP Hervestiging). [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere gebeurtenis in deze wiki. [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |

### Specialisaties

- **Immigratie**: Vestiging van iemand die nooit in de BRP of RNI stond: eerste inschrijving (HUP Immigratie). Geen eigen pagina.
- **Hervestiging**: Vestiging van iemand die in de RNI staat (HUP Hervestiging). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vestiging vanuit het buitenland | leidt tot *triggering* | [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) (inleiding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Vestiging vanuit het buitenland | [Wet BRP](../../bronanalyses/burgerzaken/2026-rijk-wet-brp-bwbr0033715.md), [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) (Wet BRP art. 2.4, 2.38) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [RvIG Circulaire adresonderzoek BRP](../../bronanalyses/burgerzaken/2023-rvig-circulaire-adresonderzoek-brp.md) | Circulaire adresonderzoek BRP |
| [Utrecht Inschrijven vanuit het buitenland](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) | Gemeente Utrecht: Inschrijven vanuit het buitenland |
| [HUP Immigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-immigratie.md) | HUP BRP: Immigratie |
| [HUP Hervestiging](../../bronanalyses/burgerzaken/2026-rvig-hup-hervestiging.md) | HUP BRP: Hervestiging |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
