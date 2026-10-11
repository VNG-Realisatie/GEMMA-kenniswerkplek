---
id: bijhoudingsgemeente
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Bijhoudingsgemeente
onderwerpen:
- burgerzaken
definitie: Verantwoordelijkheid van een gemeente voor de bijhouding van de gegevens van de ingezetenen die er hun adres hebben.
match:
  gemma: geen
data_object: nee
doelgroep: gemeente
bronnen:
- 2026-rvig-hup-intergemeentelijke-adreswijziging
- 2026-rvig-hup-emigratie
- 2026-rvig-hup-wijzigen-bsn
- 2026-rvig-hup-achtergronden-en-begrippen
- 2026-rijk-wet-brp-bwbr0033715
- 2026-rvig-hup-wijziging-naamgebruik
- 2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven
- 2026-rvig-hup-overlijden-buitenland
---

# Bijhoudingsgemeente

<!-- Gegenereerd door tools/render.py uit de beoordeling bijhoudingsgemeente.yaml. Wijzig de beoordeling, niet deze pagina. -->

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
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbare term in de HUP (Intergemeentelijke adreswijziging, Emigratie, Wijzigen BSN). [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [HUP Emigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [HUP BRP: Wijzigen bsn](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, een verantwoordelijkheid van de gemeente zelf (HUP Achtergronden). [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de verantwoordelijkheid voor de bijhouding van de persoonslijsten van de ingezetenen met een adres in de gemeente (HUP Achtergronden). [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, toegewezen aan Bijhouden persoonsgegevens en zijn bedrijfsprocessen (HUP Achtergronden; HUP Intergemeentelijke adreswijziging). [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere rol in deze wiki. [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Bijhoudingsgemeente | houdt bij *toewijzing* | [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.38) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.39) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verwerken emigratie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.43) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Inschrijven op briefadres](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.23) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Uitvoeren adresonderzoek](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitvoeren-adresonderzoek.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.20 lid 2) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Behandelen verzoek om geheimhouding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-geheimhouding.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 2.59) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verstrekken persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-persoonsgegevens.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP hoofdstuk 3, paragraaf 3) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verstrekken overzicht gegevensverstrekkingen](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-overzicht-gegevensverstrekkingen.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 3.22) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Behandelen verzoek om correctie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-correctie.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 2.58) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Behandelen verzoek om verwijdering van gegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-verwijdering-van-gegevens.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 2.57) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Wijzigen identificatienummers](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-identificatienummers.md) | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Wijzigen naamgebruik](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-naamgebruik.md) | [HUP BRP: Wijziging naamgebruik](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) (regel 34, 60) |
| Bijhoudingsgemeente | voert uit *toewijzing* | [Verwerken buitenlands document](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-buitenlands-document.md) | [Utrecht Buitenlandse documenten inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md), [HUP BRP: Overlijden buitenland](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) (Utrecht: Voorwaarden, Na uw afspraak; HUP regel 33) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Gemeente](../actoren/gemeente.md) | vervult *toewijzing* | Bijhoudingsgemeente | [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Bijhoudingsgemeente | [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 1.1 onder h, 1.4 lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Intergemeentelijke adreswijziging](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) | HUP BRP: Intergemeentelijke adreswijziging |
| [HUP Emigratie](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |
| [HUP BRP: Wijzigen bsn](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijzigen-bsn.md) | HUP BRP: Wijzigen bsn |
| [HUP BRP Achtergronden en begrippen](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) | HUP BRP: Achtergronden en begrippen |
| [Wet BRP](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [HUP BRP: Wijziging naamgebruik](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) | HUP BRP: Wijziging naamgebruik |
| [Utrecht Buitenlandse documenten inschrijven](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-buitenlandse-documenten-inschrijven.md) | Gemeente Utrecht: Buitenlandse documenten inschrijven |
| [HUP BRP: Overlijden buitenland](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) | HUP BRP: Overlijden buitenland |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
