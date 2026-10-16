---
id: naamswijziging
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Naamswijziging
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het wijzigen van de voornaam door de rechtbank of van de geslachtsnaam bij koninklijk besluit.
match:
  gemma: geen
data_object: nee
synoniemen:
- Wijziging van de geslachtsnaam (wet)
- Wijziging voornaam (HUP)
bronnen:
- 2026-rvig-hup-wijziging-voornaam
- 2026-rvig-hup-naamswijziging-en-naamgebruik
- 2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rvig-hup-vaststelling-geslachtsnaam
- 2026-rvig-hup-wijziging-geslachtsnaam
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-van-rechtswege-vervallen-reisdocument
---

# Naamswijziging

<!-- Gegenereerd door tools/render.py uit de beoordeling naamswijziging.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het wijzigen van de voornaam door de rechtbank of van de geslachtsnaam bij koninklijk besluit.

### Beschrijving

Een voornaam laat men wijzigen bij de rechtbank, een achternaam via Justis bij koninklijk besluit; de gemeente beslist er niet over maar neemt de nieuwe naam op (BW 1 art. 4 lid 4, 7; Utrecht). Een geldig Nederlands reisdocument vervalt bij een naamswijziging van rechtswege (HUP Erkenning). Het naamgebruik is iets anders: de keuze welke achternaam de overheid gebruikt (BW 1 art. 9).

### Synoniemen

| Synoniem | Context |
|---|---|
| Wijziging van de geslachtsnaam | wet |
| Wijziging voornaam | HUP |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md), [Verval van het reisdocument](verval-van-het-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, gebeurt bij veel personen, elk jaar opnieuw. [HUP BRP: Naamswijziging en naamgebruik](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-naamswijziging-en-naamgebruik.md), [Utrecht Voornaam of achternaam veranderen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Naamswijziging | leidt tot *triggering* | [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md) | [Utrecht Voornaam of achternaam veranderen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md), [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (Utrecht inleiding; art. 20) |
| Naamswijziging | doet het reisdocument vervallen *triggering* | [Verval van het reisdocument](verval-van-het-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder e; HUP Van rechtswege vervallen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Naamswijziging | [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Voornaam of achternaam veranderen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) (art. 4, 7) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Wijziging voornaam](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-voornaam.md) | HUP BRP: Wijziging voornaam |
| [HUP BRP: Naamswijziging en naamgebruik](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-naamswijziging-en-naamgebruik.md) | HUP BRP: Naamswijziging en naamgebruik |
| [Utrecht Voornaam of achternaam veranderen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) | Gemeente Utrecht: Voornaam of achternaam veranderen |
| [BW boek 1](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP BRP: Vaststelling geslachtsnaam](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-geslachtsnaam.md) | HUP BRP: Vaststelling geslachtsnaam |
| [HUP BRP: Wijziging geslachtsnaam](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-geslachtsnaam.md) | HUP BRP: Wijziging geslachtsnaam |
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Van rechtswege vervallen reisdocument](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) | HUP BRP: Van rechtswege vervallen reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
