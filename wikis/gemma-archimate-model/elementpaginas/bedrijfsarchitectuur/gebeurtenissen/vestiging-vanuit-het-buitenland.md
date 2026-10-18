---
id: vestiging-vanuit-het-buitenland
type: gebeurtenis
archimate_type: business-event
status: review
naam: Vestiging vanuit het buitenland
onderwerpen:
- burgerzaken
definitie: Het gaan wonen in een Nederlandse gemeente van een persoon die in het buitenland woonde.
match:
  gemma: geen
bronnen:
- 2023-rvig-circulaire-adresonderzoek-brp
- 2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland
- 2026-rvig-hup-immigratie
- 2026-rvig-hup-hervestiging
- 2026-rijk-wet-brp-bwbr0033715
---

# Vestiging vanuit het buitenland

<!-- Gegenereerd door tools/render.py uit de beoordeling vestiging-vanuit-het-buitenland.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het gaan wonen in een Nederlandse gemeente van een persoon die in het buitenland woonde.

### Beschrijving

Wie vanuit het buitenland in een gemeente komt wonen, of het komende half jaar ten minste vier maanden, schrijft zich binnen vijf dagen in (Utrecht Inschrijven vanuit het buitenland). Stond de persoon nooit in de BRP of RNI, dan is het een immigratie (eerste inschrijving); stond hij in de RNI, dan een hervestiging (HUP Immigratie; HUP Hervestiging).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md).

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [RvIG Circulaire adresonderzoek BRP](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [Utrecht Inschrijven vanuit het buitenland](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md). [RvIG Circulaire adresonderzoek BRP](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [Utrecht Inschrijven vanuit het buitenland](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [RvIG Circulaire adresonderzoek BRP](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [Utrecht Inschrijven vanuit het buitenland](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) |

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
