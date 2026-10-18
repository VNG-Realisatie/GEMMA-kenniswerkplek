---
id: verhuizing
type: gebeurtenis
archimate_type: business-event
status: review
naam: Verhuizing
onderwerpen:
- burgerzaken
definitie: Het gaan wonen van een persoon op een ander adres in Nederland.
match:
  gemma: geen
synoniemen:
- Adreswijziging (wet)
bronnen:
- 2026-utrecht-burgerzaken-verhuizing-doorgeven
- 2026-rvig-hup-binnengemeentelijke-adreswijziging
- 2026-rvig-hup-intergemeentelijke-adreswijziging
- 2026-rijk-wet-brp-bwbr0033715
---

# Verhuizing

<!-- Gegenereerd door tools/render.py uit de beoordeling verhuizing.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

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

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md).

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Utrecht Verhuizing doorgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md). [Utrecht Verhuizing doorgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [Utrecht Verhuizing doorgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verhuizing | leidt tot *triggering* | [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md) | [HUP Binnengemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (HUP inleiding; Utrecht inleiding; Wet BRP art. 2.39 lid 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verhuizing | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) (Wet BRP art. 2.20, 2.39) |
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Verhuizing | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.39) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Verhuizing doorgeven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) | Gemeente Utrecht: Verhuizing doorgeven |
| [HUP Binnengemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) | HUP BRP: Binnengemeentelijke adreswijziging |
| [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) | HUP BRP: Intergemeentelijke adreswijziging |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
