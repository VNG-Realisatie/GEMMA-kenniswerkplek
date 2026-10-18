---
id: geboorte
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Geboorte
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het levend ter wereld komen van een kind.
match:
  gemma: geen
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rvig-hup-geboorte
- 2026-utrecht-burgerzaken-geboorteaangifte-doen
---

# Geboorte

<!-- Gegenereerd door tools/render.py uit de beoordeling geboorte.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het levend ter wereld komen van een kind.

### Beschrijving

Binnen drie dagen na de geboorte wordt aangifte gedaan in de gemeente van geboorte (BW 1 art. 19e). Een kind heeft juridisch altijd een moeder en hoogstens één andere ouder; het wordt in de BRP ingeschreven als de moeder ingezetene is, anders op aangifte van verblijf en adres (HUP Geboorte). Een kind dat levend is geboren maar vóór de aangifte overleed, krijgt een geboorteakte en een akte van overlijden (HUP Overlijden; Utrecht Levenloos geboren kind).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (2 toetskenmerken ja).

### Plaats in de indelingen

- **Start**: [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md). [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **komt herhaald voor**: Gebeurt het regelmatig en voor verschillende gevallen, en is het geen eenmalig voorval? | Ja, standaard. [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Geboorte | leidt tot *triggering* | [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md) | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (art. 19e) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Geboorte | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19e) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP BRP: Geboorte](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md) | HUP BRP: Geboorte |
| [Utrecht Geboorteaangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) | Gemeente Utrecht: Geboorteaangifte |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
