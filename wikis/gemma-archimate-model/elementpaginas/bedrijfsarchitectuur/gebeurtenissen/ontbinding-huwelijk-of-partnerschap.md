---
id: ontbinding-huwelijk-of-partnerschap
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Ontbinding huwelijk of partnerschap
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het eindigen van een huwelijk door echtscheiding of van een geregistreerd partnerschap door beëindiging, anders dan door overlijden.
match:
  gemma: geen
data_object: nee
synoniemen:
- Echtscheiding (wet)
bronnen:
- 2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen
- 2026-rijk-burgerlijk-wetboek-boek-1
---

# Ontbinding huwelijk of partnerschap

<!-- Gegenereerd door tools/render.py uit de beoordeling ontbinding-huwelijk-of-partnerschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het eindigen van een huwelijk door echtscheiding of van een geregistreerd partnerschap door beëindiging, anders dan door overlijden.

### Beschrijving

Scheiden gaat via de rechtbank met een advocaat; een geregistreerd partnerschap kan zonder rechter worden beëindigd met een verklaring van advocaten of notarissen, behalve bij minderjarige kinderen of onenigheid (BW 1 art. 80c; Utrecht). De advocaat of notaris stuurt de stukken naar de gemeente van de akte; de ontbinding geldt vanaf de inschrijving (Utrecht; BW 1 art. 163). Een huwelijk of partnerschap eindigt ook door overlijden; dat is de gebeurtenis Overlijden.

### Synoniemen

| Synoniem | Context |
|---|---|
| Echtscheiding | wet |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Inschrijven ontbinding huwelijk of partnerschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ontbinding-huwelijk-of-partnerschap.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, gebeurt bij veel personen, elk jaar opnieuw. [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md), [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Inschrijven ontbinding huwelijk of partnerschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ontbinding-huwelijk-of-partnerschap.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Ontbinding huwelijk of partnerschap | leidt tot *triggering* | [Inschrijven ontbinding huwelijk of partnerschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ontbinding-huwelijk-of-partnerschap.md) | [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md), [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (Utrecht inleiding; art. 163) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Ontbinding huwelijk of partnerschap | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80c, 163) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Scheiden of geregistreerd partnerschap beëindigen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-scheiden-of-geregistreerd-partnerschap-beeindigen.md) | Gemeente Utrecht: Scheiden of geregistreerd partnerschap beëindigen |
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
