---
id: behandelen-verzoek-om-correctie
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen verzoek om correctie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beslissen op een verzoek van een ingeschrevene om onjuiste gegevens in de basisregistratie personen te corrigeren.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: deelproces
afnemer: extern
synoniemen:
- Correctieverzoek (HUP)
bronnen:
- 2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp
- 2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens
- 2018-nvvb-stappenplan-identiteitswijziging-brp
- 2025-vng-upl-producten-en-diensten-extern
---

# Behandelen verzoek om correctie

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/behandelen-verzoek-om-correctie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beslissen op een verzoek van een ingeschrevene om onjuiste gegevens in de basisregistratie personen te corrigeren.

### Beschrijving

De burger kan vragen gegevens te laten aanpassen: adresgegevens, zoals een onjuiste inschrijfdatum, of persoonsgegevens zoals naam, geslacht en geboortedatum, met bewijsstukken; de gemeente beoordeelt de bewijsstukken en neemt binnen vier weken een besluit waartegen bezwaar mogelijk is (Utrecht Persoonsgegevens aanpassen). Wijzigt daardoor in feite de identiteit, zoals bij een andere geboortedatum, dan zijn gemeenten bijzonder terughoudend; de NVVB heeft een stappenplan, een model rectificatieverzoek en een model weigeringsbeschikking (NVVB Identiteitswijziging). Correcties na een eigen constatering of een onderzoek zijn registratiestappen zonder eigen besluit (HUP Correcties).

### Synoniemen

| Synoniem | Context |
|---|---|
| Correctieverzoek | HUP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau deelproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: deelproces.
- **Procesindeling naar taak, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek waarop de gemeente na beoordeling van de bewijsstukken beslist (Utrecht).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 44 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar als persoonsgegevens aanpassen (Utrecht) en correctieverzoek (HUP). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente beoordeelt de bewijsstukken en neemt binnen vier weken een besluit (Utrecht). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per geval van begin tot eind doorlopen. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, bijhoudingsgemeente en Beslisser (college) (Utrecht; NVVB Identiteitswijziging). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, corrigeert gegevens van de ingeschreven persoon en de verblijfplaats aan de hand van bewijsstukken (Utrecht; HUP Correcties). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, verzoek van de burger om correctie, met bewijsstukken (HUP Correcties; Utrecht). [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een besluit: gecorrigeerde gegevens of een weigeringsbeschikking (Utrecht; NVVB Identiteitswijziging). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 2.58 en verder en de Awb (HUP Correcties; UPL nr. 95). [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **bijdrage aan groter proces**: Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden persoonsgegevens: één correctie in de persoonslijst (HUP Correcties). [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, het college beslist binnen vier weken; bezwaar is mogelijk (Utrecht; NVVB Model weigeringsbeschikking). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst BRP-wijzigingsverzoek (UPL nr. 95). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder proces in deze wiki. [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) |

### Specialisaties

- **Identiteitswijziging**: Correctie waardoor in feite de identiteit in de BRP wijzigt, zoals de geboortedatum; met een eigen stappenplan van de NVVB (NVVB Identiteitswijziging). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen verzoek om correctie | corrigeert *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) (Persoonsgegevens aanpassen) |
| Behandelen verzoek om correctie | realiseert *realisatie* | [BRP-wijzigingsverzoek](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-wijzigingsverzoek.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) (UPL nr. 95) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Behandelen verzoek om correctie | [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) (Na uw aanvraag) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Behandelen verzoek om correctie | [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) (inleiding) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Behandelen verzoek om correctie | [HUP BRP Achtergronden en begrippen](../../../../bronanalyses/burgerzaken/2026-rvig-hup-achtergronden-en-begrippen.md) (BRP stelsel) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht BRP-gegevens opvragen of aanpassen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) | Gemeente Utrecht: Persoonsgegevens opvragen of aanpassen |
| [HUP BRP Correcties](../../../../bronanalyses/burgerzaken/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) | HUP BRP: Correcties en ten onrechte opgenomen gegevens |
| [NVVB Stappenplan identiteitswijziging BRP](../../../../bronanalyses/burgerzaken/2018-nvvb-stappenplan-identiteitswijziging-brp.md) | NVVB: Stappenplan identiteitswijziging in de BRP |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, open): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern).
