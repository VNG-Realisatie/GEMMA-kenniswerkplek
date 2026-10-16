---
id: inschrijven-levenloos-geboren-kind
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Inschrijven levenloos geboren kind
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beslissen op het verzoek van een ouder om de gegevens van een levenloos geboren kind in de basisregistratie personen op te nemen.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-wet-brp-bwbr0033715
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen
- 2026-rvig-hup-geboorte
---

# Inschrijven levenloos geboren kind

<!-- Gegenereerd door tools/render.py uit de beoordeling inschrijven-levenloos-geboren-kind.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het beslissen op het verzoek van een ouder om de gegevens van een levenloos geboren kind in de basisregistratie personen op te nemen.

### Beschrijving

Een levenloos geboren kind wordt alleen op verzoek van een ouder in de BRP opgenomen; een kind dat kort heeft geleefd wordt automatisch ingeschreven (HUP Geboorte; Utrecht). Het weigeren van de opname is een besluit in de zin van de Awb (Wet BRP art. 2.60; HUP Geboorte).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek waarop het college beslist (Wet BRP art. 2.56a, 2.60).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Ouder](../../../rollen/ouder.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een verzoek van een ouder, met formulier, online met DigiD of aan de balie (Utrecht). [Utrecht Levenloos geboren kind, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, opname van de gegevens van het kind op de persoonslijst van de ouder, of een besluit tot weigering (Wet BRP art. 2.56a, 2.60). [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Levenloos geboren kind, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 2.56a, 2.60. [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek tot de opname op de persoonslijst of de weigering. [Utrecht Levenloos geboren kind, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, het college beslist op het verzoek; weigeren is een Awb-besluit (Wet BRP art. 2.60; HUP Geboorte). [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [HUP BRP: Geboorte](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [BRP-inschrijving niet in leven zijnd kind](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving-niet-in-leven-zijnd-kind.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Inschrijven levenloos geboren kind | neemt gegevens kind op bij *toegang (registreren)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP BRP: Geboorte](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md) (levenloos geboren kind) |
| Inschrijven levenloos geboren kind | realiseert *realisatie* | [BRP-inschrijving niet in leven zijnd kind](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving-niet-in-leven-zijnd-kind.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 90) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Inschrijven levenloos geboren kind | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [HUP BRP: Geboorte](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md) (art. 2.56a) |
| [Ouder](../../../rollen/ouder.md) | verzoekt *toewijzing* | Inschrijven levenloos geboren kind | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [Utrecht Levenloos geboren kind, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md) (art. 2.56a) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Levenloos geboren kind, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md) | Gemeente Utrecht: Levenloos geboren kind |
| [HUP BRP: Geboorte](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md) | HUP BRP: Geboorte |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
