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
grondslag: bron
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

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/naamswijziging.yaml. Wijzig de beoordeling, niet deze pagina. -->

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

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar: het wijzigen van voornaam of achternaam (HUP Naamswijziging en naamgebruik; Utrecht Voornaam of achternaam veranderen). [HUP BRP: Naamswijziging en naamgebruik](../../bronanalyses/burgerzaken/2026-rvig-hup-naamswijziging-en-naamgebruik.md), [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, na goedkeuring neemt de gemeente de nieuwe naam op, eerst op de geboorteakte, daarna in de BRP (Utrecht). [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP BRP: Naamswijziging en naamgebruik](../../bronanalyses/burgerzaken/2026-rvig-hup-naamswijziging-en-naamgebruik.md), [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP BRP: Naamswijziging en naamgebruik](../../bronanalyses/burgerzaken/2026-rvig-hup-naamswijziging-en-naamgebruik.md), [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [HUP BRP: Naamswijziging en naamgebruik](../../bronanalyses/burgerzaken/2026-rvig-hup-naamswijziging-en-naamgebruik.md), [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, het besluit van de Koning of de beschikking van de rechtbank verandert de naam op één moment (BW 1 art. 4, 7; HUP Vaststelling geslachtsnaam). [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Vaststelling geslachtsnaam](../../bronanalyses/burgerzaken/2026-rvig-hup-vaststelling-geslachtsnaam.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, gebeurt bij veel personen, elk jaar opnieuw. [HUP BRP: Naamswijziging en naamgebruik](../../bronanalyses/burgerzaken/2026-rvig-hup-naamswijziging-en-naamgebruik.md), [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start het toevoegen van de latere vermelding aan de geboorteakte en de verwerking in de BRP (Utrecht; HUP Wijziging geslachtsnaam). [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md), [HUP BRP: Wijziging geslachtsnaam](../../bronanalyses/burgerzaken/2026-rvig-hup-wijziging-geslachtsnaam.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [HUP BRP: Naamswijziging en naamgebruik](../../bronanalyses/burgerzaken/2026-rvig-hup-naamswijziging-en-naamgebruik.md), [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Naamswijziging | leidt tot *triggering* | [Toevoegen latere vermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/toevoegen-latere-vermelding.md) | [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md), [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (Utrecht inleiding; art. 20) |
| Naamswijziging | doet het reisdocument vervallen *triggering* | [Verval van het reisdocument](verval-van-het-reisdocument.md) | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) (Paspoortwet art. 47 lid 1 onder e; HUP Van rechtswege vervallen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Naamswijziging | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) (art. 4, 7) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Wijziging voornaam](../../bronanalyses/burgerzaken/2026-rvig-hup-wijziging-voornaam.md) | HUP BRP: Wijziging voornaam |
| [HUP BRP: Naamswijziging en naamgebruik](../../bronanalyses/burgerzaken/2026-rvig-hup-naamswijziging-en-naamgebruik.md) | HUP BRP: Naamswijziging en naamgebruik |
| [Utrecht Voornaam of achternaam veranderen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) | Gemeente Utrecht: Voornaam of achternaam veranderen |
| [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP BRP: Vaststelling geslachtsnaam](../../bronanalyses/burgerzaken/2026-rvig-hup-vaststelling-geslachtsnaam.md) | HUP BRP: Vaststelling geslachtsnaam |
| [HUP BRP: Wijziging geslachtsnaam](../../bronanalyses/burgerzaken/2026-rvig-hup-wijziging-geslachtsnaam.md) | HUP BRP: Wijziging geslachtsnaam |
| [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Van rechtswege vervallen reisdocument](../../bronanalyses/burgerzaken/2026-rvig-hup-van-rechtswege-vervallen-reisdocument.md) | HUP BRP: Van rechtswege vervallen reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
