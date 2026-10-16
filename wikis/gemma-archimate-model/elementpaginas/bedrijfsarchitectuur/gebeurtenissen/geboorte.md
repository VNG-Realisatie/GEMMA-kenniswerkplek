---
id: geboorte
type: gebeurtenis
archimate_type: business-event
status: review
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

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het levend ter wereld komen van een kind.

### Beschrijving

Binnen drie dagen na de geboorte wordt aangifte gedaan in de gemeente van geboorte (BW 1 art. 19e). Een kind heeft juridisch altijd een moeder en hoogstens één andere ouder; het wordt in de BRP ingeschreven als de moeder ingezetene is, anders op aangifte van verblijf en adres (HUP Geboorte). Een kind dat levend is geboren maar vóór de aangifte overleed, krijgt een geboorteakte en een akte van overlijden (HUP Overlijden; Utrecht Levenloos geboren kind).

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, gebeurt bij veel personen, elk jaar opnieuw. [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md). |

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
