---
id: vestiging-vanuit-het-buitenland
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Vestiging vanuit het buitenland
onderwerpen:
- burgerzaken
definitie: Het gaan wonen in een Nederlandse gemeente van een persoon die in het buitenland woonde.
match:
  gemma: geen
data_object: nee
bronnen:
- 2023-rvig-circulaire-adresonderzoek-brp
- 2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland
- 2026-rvig-hup-immigratie
- 2026-rvig-hup-hervestiging
- 2026-rijk-wet-brp-bwbr0033715
---

# Vestiging vanuit het buitenland

<!-- Gegenereerd door tools/render.py uit de beoordeling vestiging-vanuit-het-buitenland.yaml. Wijzig de beoordeling, niet deze pagina. -->

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

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elke persoon die het overkomt. [HUP Immigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md), [Utrecht Inschrijven vanuit het buitenland](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md). |

### Specialisaties

- **Immigratie**: Vestiging van iemand die nooit in de BRP of RNI stond: eerste inschrijving (HUP Immigratie). Geen eigen pagina.
- **Hervestiging**: Vestiging van iemand die in de RNI staat (HUP Hervestiging). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vestiging vanuit het buitenland | leidt tot *triggering* | [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | [HUP Immigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.2, 2.38 lid 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Vestiging vanuit het buitenland | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [HUP Immigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) (Wet BRP art. 2.4, 2.38) |
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Vestiging vanuit het buitenland | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.38) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [RvIG Circulaire adresonderzoek BRP](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) | Circulaire adresonderzoek BRP |
| [Utrecht Inschrijven vanuit het buitenland](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) | Gemeente Utrecht: Inschrijven vanuit het buitenland |
| [HUP Immigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) | HUP BRP: Immigratie |
| [HUP Hervestiging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md) | HUP BRP: Hervestiging |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
