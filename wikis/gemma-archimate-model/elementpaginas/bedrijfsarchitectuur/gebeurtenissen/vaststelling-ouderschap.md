---
id: vaststelling-ouderschap
type: gebeurtenis
archimate_type: business-event
status: review
naam: Vaststelling ouderschap
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het door een uitspraak van de rechtbank ontstaan van het juridisch ouderschap van een man of vrouw over een kind.
match:
  gemma: geen
synoniemen:
- Gerechtelijke vaststelling van het ouderschap (wet)
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rvig-hup-vaststelling-ouderschap
---

# Vaststelling ouderschap

<!-- Gegenereerd door tools/render.py uit de beoordeling vaststelling-ouderschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het door een uitspraak van de rechtbank ontstaan van het juridisch ouderschap van een man of vrouw over een kind.

### Beschrijving

De rechtbank stelt het ouderschap vast op verzoek van de moeder of het kind (BW 1 art. 207); de gemeente verwerkt de uitspraak (HUP Vaststelling ouderschap). Naast geboorte, erkenning, adoptie en ontkenning is het een van de gronden van de afstamming (HUP Afstamming).

### Synoniemen

| Synoniem | Context |
|---|---|
| Gerechtelijke vaststelling van het ouderschap | wet |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Vaststelling ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md). [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Vaststelling ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Vaststelling ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Vaststelling ouderschap | leidt tot *triggering* | [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md) | [HUP BRP: Vaststelling ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) (inleiding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Vaststelling ouderschap | [HUP BRP: Vaststelling ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) (inleiding) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP BRP: Vaststelling ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) | HUP BRP: Vaststelling ouderschap |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
