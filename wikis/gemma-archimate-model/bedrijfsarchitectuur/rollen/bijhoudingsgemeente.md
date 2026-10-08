---
id: bijhoudingsgemeente
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Bijhoudingsgemeente
onderwerpen:
- burgerzaken
definitie: Verantwoordelijkheid van een gemeente voor de bijhouding van de gegevens van de ingezetenen die er hun adres hebben.
grondslag: bron
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2026-rvig-hup-intergemeentelijke-adreswijziging
- 2026-rvig-hup-emigratie
- 2026-rvig-hup-wijzigen-bsn
- 2026-rvig-hup-achtergronden-en-begrippen
---

# Bijhoudingsgemeente

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/bijhoudingsgemeente.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid van een gemeente voor de bijhouding van de gegevens van de ingezetenen die er hun adres hebben.

### Beschrijving

Het college van de gemeente waar een ingezetene zijn adres heeft, is verantwoordelijk voor de bijhouding van zijn gegevens (HUP Achtergronden). Bij een verhuizing naar een andere gemeente wordt die de nieuwe bijhoudingsgemeente; na emigratie blijft de laatste bijhoudingsgemeente verantwoordelijk voor rechtsfeiten van voor de emigratie (HUP Intergemeentelijke adreswijziging; HUP Emigratie).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: gemeente.

### Kenmerken

Alleen de kenmerken met ja; de overige 53 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbare term in de HUP (Intergemeentelijke adreswijziging, Emigratie, Wijzigen BSN). [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [HUP Emigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [HUP BRP: Wijzigen bsn](../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, een verantwoordelijkheid van de gemeente zelf (HUP Achtergronden). [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de verantwoordelijkheid voor de bijhouding van de persoonslijsten van de ingezetenen met een adres in de gemeente (HUP Achtergronden). [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, toegewezen aan Bijhouden persoonsgegevens en zijn bedrijfsprocessen (HUP Achtergronden; HUP Intergemeentelijke adreswijziging). [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere rol in deze wiki. [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md), [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Bijhoudingsgemeente | houdt bij *toewijzing* | [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verwerken emigratie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Inschrijven op briefadres](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Uitvoeren adresonderzoek](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitvoeren-adresonderzoek.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Behandelen verzoek om geheimhouding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-geheimhouding.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verstrekken persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verstrekken overzicht gegevensverstrekkingen](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-overzicht-gegevensverstrekkingen.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Behandelen verzoek om correctie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-correctie.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Behandelen verzoek om verwijdering van gegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-verwijdering-van-gegevens.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Wijzigen identificatienummers](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-identificatienummers.md) | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Gemeente](../actoren/gemeente.md) | vervult *toewijzing* | Bijhoudingsgemeente | [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Intergemeentelijke adreswijziging](../../bronanalyses/burgerzaken/2026-rvig-hup-intergemeentelijke-adreswijziging.md) | HUP BRP: Intergemeentelijke adreswijziging |
| [HUP Emigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |
| [HUP BRP: Wijzigen bsn](../../bronanalyses/burgerzaken/2026-rvig-hup-wijzigen-bsn.md) | HUP BRP: Wijzigen bsn |
| [HUP BRP Achtergronden en begrippen](../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) | HUP BRP: Achtergronden en begrippen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
