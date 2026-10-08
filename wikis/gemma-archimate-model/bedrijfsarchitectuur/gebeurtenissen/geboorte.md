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
grondslag: bron
match:
  gemma: geen
data_object: nee
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rvig-hup-geboorte
- 2026-utrecht-burgerzaken-geboorteaangifte-doen
---

# Geboorte

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/geboorte.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

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

Alleen de kenmerken met ja; de overige 50 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar; de aangifte van geboorte en de akte van geboorte (BW 1 art. 19, 19e; HUP Geboorte; Utrecht). [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, wordt aangegeven bij de gemeente waar het kind is geboren (BW 1 art. 19e). [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, het kind wordt geboren: één moment met rechtsgevolgen (afstamming, naam, inschrijving; HUP Geboorte). [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, gebeurt bij veel personen, elk jaar opnieuw. [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start de aangifte en het opmaken van de geboorteakte (BW 1 art. 19e) en de inschrijving van het kind in de BRP van de woongemeente van de moeder (HUP Geboorte). [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Geboorte | leidt tot *triggering* | [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md) | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (art. 19e) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden burgerlijke stand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Geboorte | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19e) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP BRP: Geboorte](../../bronanalyses/burgerzaken/2026-rvig-hup-geboorte.md) | HUP BRP: Geboorte |
| [Utrecht Geboorteaangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) | Gemeente Utrecht: Geboorteaangifte |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
