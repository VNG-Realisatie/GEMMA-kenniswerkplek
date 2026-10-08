---
id: registreren-kiesgerechtigdheid
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Registreren kiesgerechtigdheid
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het registreren van wie in de gemeente kiesgerechtigd is, met de uitsluiting van het kiesrecht en de deelname van EU-onderdanen aan de Europese verkiezingen.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Kiezersregistratie (dagelijks gebruik)
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvig-hup-kiesrecht
- 2026-rvig-hup-europees-kiesrecht
- 2026-rvig-hup-nederlands-kiesrecht
---

# Registreren kiesgerechtigdheid

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/registreren-kiesgerechtigdheid.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het registreren van wie in de gemeente kiesgerechtigd is, met de uitsluiting van het kiesrecht en de deelname van EU-onderdanen aan de Europese verkiezingen.

### Beschrijving

Burgemeester en wethouders registreren de kiesgerechtigdheid van de ingezetenen; wie als ingezetene met een adres in de basisregistratie personen staat, wordt geacht daar te wonen (Kieswet art. B 4, D 1). Kiesgerechtigd voor de gemeenteraad zijn ook niet-Nederlanders met verblijfsrecht na vijf jaar verblijf in Nederland (art. B 3). Op verzoek delen B&W onverwijld mee of iemand als kiezer is geregistreerd, en zo niet waarom; wie ten onrechte niet is geregistreerd, kan om wijziging vragen (art. D 5, D 6, D 7).

Een uitsluiting van het kiesrecht volgt uit een onherroepelijke rechterlijke uitspraak; de minister van Justitie en Veiligheid meldt haar aan de burgemeester, die de persoon in kennis stelt, en de gemeente legt haar vast in de persoonslijst (art. B 5; HUP Nederlands kiesrecht). Tegenspraak: de HUP spreekt van een mededeling aan de gemeente en noemt de kennisgeving aan de persoon niet; formeel geldt de Kieswet. Een EU-onderdaan die in Nederland wil stemmen voor het Europees Parlement, verzoekt met formulier Y32 om registratie; de gemeente informeert hem daarover bij de aangifte van verblijf en adres, en de registratie eindigt op verzoek, bij vertrek of bij verkrijging van het Nederlanderschap (HUP Europees kiesrecht).

De registratie van kiezers buiten Nederland is een taak van één gemeente, 's-Gravenhage (Kieswet art. D 2, D 3).

### Synoniemen

| Synoniem | Context |
|---|---|
| Kiezersregistratie | dagelijks gebruik |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Functie-indeling naar domein, bediend door**: [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md).
- **Gestart door gebeurtenis**: [Uitsluiting van het kiesrecht](../../../gebeurtenissen/uitsluiting-van-het-kiesrecht.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 43 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, burgemeester en wethouders registreren de kiesgerechtigdheid van de ingezetenen (Kieswet art. D 1); UPL-product stemrecht (nr. 398); de BRP kent de categorie kiesrecht (HUP Kiesrecht). [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [HUP Kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-kiesrecht.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, b&W registreren de kiesgerechtigdheid en delen op verzoek mee of iemand als kiezer is geregistreerd; de burgemeester stelt een uitgesloten persoon in kennis (Kieswet art. B 5, D 1, D 5). [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij burgerzaken: bedrijfsproces onder Bijhouden persoonsgegevens. [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-kiesrecht.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, per mededeling of verzoek doorlopen (Kieswet art. B 5, D 5; HUP Europees kiesrecht). [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, beslisser: burgemeester en wethouders, die op een aanvraag tot wijziging beslissen (Kieswet art. D 1, D 7); Kiezer: verzoekt om mededeling of, als EU-onderdaan, om registratie voor het Europees Parlement (art. D 5; HUP Europees kiesrecht). [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, werkt de ingeschreven persoon bij: de uitsluiting van het kiesrecht en de deelname aan het Europees kiesrecht in de persoonslijst (HUP Nederlands kiesrecht; HUP Europees kiesrecht); de kiesgerechtigdheid volgt uit de inschrijving als ingezetene (Kieswet art. B 4). [HUP Nederlands kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlands-kiesrecht.md), [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md), [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een mededeling van de minister over een uitsluiting, een verzoek van een EU-onderdaan (formulier Y32) of een verzoek om mededeling (Kieswet art. B 5, D 5; HUP Europees kiesrecht). [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de registratie als kiezer, de mededeling of iemand is geregistreerd, en de kennisgeving van een uitsluiting (Kieswet art. B 5, D 1, D 5). [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke mededeling en elk verzoek. [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, kieswet art. B 1-B 5 en D 1-D 8; HUP Nederlands en Europees kiesrecht. [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Nederlands kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlands-kiesrecht.md), [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Bijhouden persoonsgegevens: de kiesrechtgegevens van de ingeschreven persoon. [HUP Kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-kiesrecht.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de mededeling of het verzoek tot de registratie of de kennisgeving. [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, b&W beslissen op een aanvraag tot wijziging van de registratie (Kieswet art. D 6 lid 1 onder a, D 7 lid 1). [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst Stemrecht (UPL nr. 398). [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Registreren kiesgerechtigdheid | registreert de kiesgerechtigdheid *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Nederlands kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlands-kiesrecht.md), [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) (Kieswet art. D 1; HUP Nederlands en Europees kiesrecht) |
| Registreren kiesgerechtigdheid | realiseert *realisatie* | [Stemrecht](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/stemrecht.md) | [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) (UPL nr. 398) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist op een aanvraag tot wijziging *toewijzing* | Registreren kiesgerechtigdheid | [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) (art. D 7) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Registreren kiesgerechtigdheid | [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-kiesrecht.md) (Kieswet art. D 1; HUP Kiesrecht) |
| [Kieswet](../../../../motivatie/beleidskaders/kieswet.md) | is grondslag voor *associatie (gericht)* | Registreren kiesgerechtigdheid | [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) (art. B 5, D 1-D 7) |
| [Kiezer](../../../rollen/kiezer.md) | verzoekt om mededeling of registratie *toewijzing* | Registreren kiesgerechtigdheid | [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) (Kieswet art. D 5; HUP Europees kiesrecht) |
| [Uitsluiting van het kiesrecht](../../../gebeurtenissen/uitsluiting-van-het-kiesrecht.md) | leidt tot *triggering* | Registreren kiesgerechtigdheid | [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md), [HUP Nederlands kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlands-kiesrecht.md) (Kieswet art. B 5 lid 3; HUP Nederlands kiesrecht) |
| [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md) | bedient *bediening* | Registreren kiesgerechtigdheid | [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) (Kieswet art. D 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../../bronanalyses/burgerzaken/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP Kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-kiesrecht.md) | HUP BRP: Kiesrecht |
| [HUP Europees kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) | HUP BRP: Europees kiesrecht |
| [HUP Nederlands kiesrecht](../../../../bronanalyses/burgerzaken/2026-rvig-hup-nederlands-kiesrecht.md) | HUP BRP: Nederlands kiesrecht |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../analyses/proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
