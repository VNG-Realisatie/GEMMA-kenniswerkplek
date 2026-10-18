---
id: adoptie
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Adoptie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het door een uitspraak van de rechtbank ontstaan van de familierechtelijke betrekking tussen een kind en zijn adoptiefouders.
match:
  gemma: geen
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rvig-hup-adoptie
- 2026-utrecht-burgerzaken-adoptie-kind-inschrijven
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2026-rijk-wet-brp-bwbr0033715
---

# Adoptie

<!-- Gegenereerd door tools/render.py uit de beoordeling adoptie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het door een uitspraak van de rechtbank ontstaan van de familierechtelijke betrekking tussen een kind en zijn adoptiefouders.

### Beschrijving

Adoptie geschiedt door een uitspraak van de rechtbank op verzoek van twee personen samen of één persoon alleen (BW 1 art. 227); een buitenlandse adoptie wordt erkend op grond van het Haags adoptieverdrag of een verklaring voor recht (HUP Adoptie). De adoptie zelf is geen gemeentelijk product; de gemeente verwerkt de uitspraak (Utrecht). Adoptiefouders krijgen het gezag van rechtswege; een herroeping van de adoptie wordt ook als latere vermelding verwerkt (HUP Adoptie; Besluit burgerlijke stand art. 53, 54).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Behandelen verzoek om verwijdering van gegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-verwijdering-van-gegevens.md), [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md), [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Adoptie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md), [Utrecht Adoptie, kind inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-adoptie-kind-inschrijven.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md), [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md), [Behandelen verzoek om verwijdering van gegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-verwijdering-van-gegevens.md). [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Adoptie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md), [Utrecht Adoptie, kind inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-adoptie-kind-inschrijven.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Adoptie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md), [Utrecht Adoptie, kind inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-adoptie-kind-inschrijven.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Adoptie | leidt tot *triggering* | [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md) | [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Adoptie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md) (art. 53) |
| Adoptie | leidt tot (adoptiekind uit het buitenland) *triggering* | [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | [Utrecht Adoptie, kind inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-adoptie-kind-inschrijven.md) (inleiding) |
| Adoptie | kan leiden tot *triggering* | [Behandelen verzoek om verwijdering van gegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-verwijdering-van-gegevens.md) | [HUP BRP: Adoptie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.57) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Adoptie | [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (art. 53) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP BRP: Adoptie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md) | HUP BRP: Adoptie |
| [Utrecht Adoptie, kind inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-adoptie-kind-inschrijven.md) | Gemeente Utrecht: Adoptie |
| [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
