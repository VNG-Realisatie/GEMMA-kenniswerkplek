---
id: behandelen-verzoek-om-verwijdering-van-gegevens
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Behandelen verzoek om verwijdering van gegevens
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beslissen op een verzoek om gegevens van vóór een adoptie of geslachtswijziging van de persoonslijst te verwijderen.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-wet-brp-bwbr0033715
---

# Behandelen verzoek om verwijdering van gegevens

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-verzoek-om-verwijdering-van-gegevens.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het beslissen op een verzoek om gegevens van vóór een adoptie of geslachtswijziging van de persoonslijst te verwijderen.

### Beschrijving

Na een adoptie of een wijziging van de vermelding van het geslacht kunnen de betrokkenen schriftelijk vragen de oude gegevens van de persoonslijst te verwijderen: voor een adoptiekind jonger dan 16 jaar de adoptieouders, daarna het kind zelf, en de biologische ouders voor de gegevens over het kind; bij een geslachtswijziging de ingeschrevene, of voor hem de ouder, voogd of curator (Utrecht Gegevens verwijderen). De gemeente neemt binnen vier weken een besluit waartegen bezwaar mogelijk is (Utrecht). Het afvoeren van een ten onrechte opgenomen persoonslijst is een registratiestap zonder eigen besluit (HUP Afvoeren persoonslijst).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek waarop de gemeente beslist (Utrecht).
- **Gestart door gebeurtenis**: [Adoptie](../../../gebeurtenissen/adoptie.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Adoptie](../../../gebeurtenissen/adoptie.md), [Wijzigen geslachtsvermelding](wijzigen-geslachtsvermelding.md). |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, verwijderde gegevens en een mededeling aan de verzoeker (Utrecht). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 2.57 (UPL nr. 86). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek tot de verwijderde gegevens en de mededeling; een eigen verzoek, ook na een geslachtswijziging. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, het college beslist binnen vier weken; bezwaar is mogelijk (Utrecht). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [BRP-adoptie-uitschrijving](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-adoptie-uitschrijving.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen verzoek om verwijdering van gegevens | verwijdert gegevens van *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Gegevens verwijderen; Wet BRP art. 2.57) |
| Behandelen verzoek om verwijdering van gegevens | realiseert *realisatie* | [BRP-adoptie-uitschrijving](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-adoptie-uitschrijving.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 86; Wet BRP art. 2.57) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Adoptie](../../../gebeurtenissen/adoptie.md) | kan leiden tot *triggering* | Behandelen verzoek om verwijdering van gegevens | [HUP BRP: Adoptie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-adoptie.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.57) |
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Behandelen verzoek om verwijdering van gegevens | [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) (Na uw aanvraag) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Behandelen verzoek om verwijdering van gegevens | [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (Utrecht Gegevens verwijderen; UPL nr. 86) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Behandelen verzoek om verwijdering van gegevens | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 2.57) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Behandelen verzoek om verwijdering van gegevens | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.57) |
| [Wijzigen geslachtsvermelding](wijzigen-geslachtsvermelding.md) | kan leiden tot *triggering* | Behandelen verzoek om verwijdering van gegevens | [HUP BRP: Geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geslachtswijziging.md), [HUP BRP: Overschrijven gegevens bij geslachtswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overschrijven-gegevens-bij-geslachtswijziging.md) (art. 2.57 Wet BRP) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) | Gemeente Utrecht: Persoonsgegevens opvragen of aanpassen |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
