---
id: ontkenning-ouderschap
type: gebeurtenis
archimate_type: business-event
status: review
naam: Ontkenning ouderschap
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het vervallen van het juridisch ouderschap van een ouder die niet de biologische ouder is, door een uitspraak of verklaring.
match:
  gemma: geen
data_object: nee
synoniemen:
- Ontkenning van het vaderschap (wet)
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2026-rvig-hup-ontkenning-ouderschap
---

# Ontkenning ouderschap

<!-- Gegenereerd door tools/render.py uit de beoordeling ontkenning-ouderschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het vervallen van het juridisch ouderschap van een ouder die niet de biologische ouder is, door een uitspraak of verklaring.

### Beschrijving

De vader, de moeder of het kind kan het ouderschap ontkennen op de grond dat de ouder niet de biologische ouder is (BW 1 art. 200); de moeder uit wie het kind is geboren kan in bepaalde gevallen zelf een verklaring afleggen bij de ambtenaar (HUP Ontkenning ouderschap). Ook de geslachtsnaam van het kind kan daardoor veranderen.

### Synoniemen

| Synoniem | Context |
|---|---|
| Ontkenning van het vaderschap | wet |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, gebeurt bij veel personen, elk jaar opnieuw. [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Ontkenning ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-ontkenning-ouderschap.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Ontkenning ouderschap | leidt tot *triggering* | [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md) | [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md), [HUP BRP: Ontkenning ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-ontkenning-ouderschap.md) (art. 49-52) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Ontkenning ouderschap | [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (art. 49-52) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Besluit burgerlijke stand 1994](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [HUP BRP: Ontkenning ouderschap](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-ontkenning-ouderschap.md) | HUP BRP: Ontkenning ouderschap |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
