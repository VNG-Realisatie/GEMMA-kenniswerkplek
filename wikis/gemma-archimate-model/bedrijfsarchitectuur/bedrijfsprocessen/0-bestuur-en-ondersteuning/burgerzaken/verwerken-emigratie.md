---
id: verwerken-emigratie
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Verwerken emigratie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verwerken van het vertrek van een ingezetene naar het buitenland, waarna hij als niet-ingezetene in de RNI staat.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: deelproces
afnemer: extern
synoniemen:
- Uitschrijving (dagelijks gebruik)
bronnen:
- 2026-utrecht-burgerzaken-emigratie-doorgeven
- 2026-rvig-hup-emigratie
- 2026-rijk-besluit-brp-bwbr0034306
- 2025-rvig-logisch-ontwerp-brp-2025q1
- 2025-vng-upl-producten-en-diensten-extern
---

# Verwerken emigratie

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verwerken-emigratie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het verwerken van het vertrek van een ingezetene naar het buitenland, waarna hij als niet-ingezetene in de RNI staat.

### Beschrijving

Wie ten minste twee derde van een jaar in het buitenland gaat wonen, doet aangifte van vertrek, vanaf vijf dagen voor het vertrek; ook een verhuizing naar het Caribisch deel van het Koninkrijk is een emigratie, waarbij de persoon kosteloos een verhuisbericht krijgt (HUP Emigratie; Regeling BRP bijlage 9). Na verwerking verhuist de persoonslijst naar de RNI en blijft de laatste bijhoudingsgemeente verantwoordelijk voor rechtsfeiten van voor de emigratie (HUP Emigratie). Is de persoon niet te bereiken, dan neemt de gemeente het vertrek ambtshalve op na een adresonderzoek (HUP Emigratie; Circulaire adresonderzoek 4.8).

### Synoniemen

| Synoniem | Context |
|---|---|
| Uitschrijving | dagelijks gebruik |

## Plaats in het model

### Typering

Bedrijfsproces, niveau deelproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: deelproces.
- **Procesindeling naar taak, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. De verwerking volgt op een aangifte van vertrek die de basisregistratie bijwerkt (HUP Emigratie).
- **Gestart door gebeurtenis**: [Emigratie](../../../gebeurtenissen/emigratie.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 45 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar als emigratie doorgeven (Utrecht) en emigratie (HUP). [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md), [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente verwerkt de emigratie binnen een week en geeft haar door aan andere instanties (Utrecht Emigratie doorgeven). [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, bijhoudingsgemeente; de Aangever doet aangifte van vertrek (HUP Emigratie). [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, werkt de ingeschreven persoon bij: de persoonslijst verhuist naar de RNI, de gemeente houdt verwijsgegevens (HUP Emigratie). [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, aangifte van vertrek, vanaf vijf dagen voor het vertrek (HUP Emigratie). [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de persoon is niet-ingezetene en staat in de RNI (Utrecht Emigratie doorgeven). [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, verplicht bij een verblijf van ten minste twee derde van een jaar buiten Nederland (art. 2.43 Wet BRP; HUP Emigratie); aangifte in persoon of schriftelijk (Besluit BRP art. 29). [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) |
| **bijdrage aan groter proces**: Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden persoonsgegevens: de opschorting van de bijhouding wegens emigratie (LO BRP 1.6). [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst Aangifte vertrek buitenland (UPL nr. 1). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder proces in deze wiki. [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken emigratie | schrijft uit naar de RNI *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) (inleiding) |
| Verwerken emigratie | realiseert *realisatie* | [Aangifte vertrek buitenland](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/aangifte-vertrek-buitenland.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) (UPL nr. 1) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Verwerken emigratie | [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Besluit basisregistratie personen](../../../../motivatie/beleidskaders/besluit-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Verwerken emigratie | [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) (art. 29) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verwerken emigratie | [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) (inleiding) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Verwerken emigratie | [HUP BRP Achtergronden en begrippen](../../../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |
| [Emigratie](../../../gebeurtenissen/emigratie.md) | leidt tot *triggering* | Verwerken emigratie | [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) (inleiding) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Emigratie doorgeven](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-emigratie-doorgeven.md) | Gemeente Utrecht: Emigratie doorgeven |
| [HUP Emigratie](../../../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |
| [Besluit BRP](../../../../bronanalyses/burgerzaken/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |
| [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) | Logisch Ontwerp BRP Versie 2025.Q1 |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, open): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern).
