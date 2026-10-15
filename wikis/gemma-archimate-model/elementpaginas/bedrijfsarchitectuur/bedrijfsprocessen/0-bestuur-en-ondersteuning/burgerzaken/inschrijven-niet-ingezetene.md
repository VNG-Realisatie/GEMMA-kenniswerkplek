---
id: inschrijven-niet-ingezetene
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Inschrijven niet-ingezetene
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het inschrijven van een persoon die niet in Nederland woont in de registratie niet-ingezetenen, door een gemeente die RNI-loket is.
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Inschrijving in de RNI (beleid)
bronnen:
- 2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvig-hup-achtergronden-en-begrippen
- 2026-rijk-wet-brp-bwbr0033715
---

# Inschrijven niet-ingezetene

<!-- Gegenereerd door tools/render.py uit de beoordeling inschrijven-niet-ingezetene.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het inschrijven van een persoon die niet in Nederland woont in de registratie niet-ingezetenen, door een gemeente die RNI-loket is.

### Beschrijving

Wie niet in Nederland woont maar een relatie heeft met de Nederlandse overheid, of hooguit vier maanden in Nederland blijft, laat zich inschrijven in de RNI en krijgt een BSN (Utrecht RNI). De inschrijving gebeurt op verzoek bij een RNI-loket of op voordracht van een aangewezen bestuursorgaan; de minister van BZK is verantwoordelijk voor de RNI (HUP Achtergronden; LO BRP 1.5.2). Utrecht schrijft sinds 2026 alleen personen met een Europees paspoort in; anderen gaan naar andere RNI-loketten (Utrecht RNI).

### Synoniemen

| Synoniem | Context |
|---|---|
| Inschrijving in de RNI | beleid |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een verzoek tot inschrijving dat de basisregistratie bijwerkt (Utrecht RNI).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [RNI-loket](../../../rollen/rni-loket.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, verzoek van de persoon die niet in Nederland woont maar een relatie heeft met de Nederlandse overheid (Utrecht RNI; HUP Achtergronden). [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md), [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een inschrijving in de RNI met BSN en een afschrift van de opgenomen gegevens (Utrecht RNI). [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md), [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet BRP art. 2.66 (grondslag UPL nr. 369); alleen bij aangewezen RNI-loketten (Utrecht RNI). [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek tot de inschrijving in de RNI. [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md), [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [RNI inschrijving](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/rni-inschrijving.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Inschrijven niet-ingezetene | schrijft in *toegang (registreren)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.66 lid 1) |
| Inschrijven niet-ingezetene | realiseert *realisatie* | [RNI inschrijving](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/rni-inschrijving.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 369; Wet BRP art. 2.66) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Inschrijven niet-ingezetene | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md) (HUP Achtergronden regel 38; Utrecht RNI) |
| [RNI-loket](../../../rollen/rni-loket.md) | schrijft in *toewijzing* | Inschrijven niet-ingezetene | [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Inschrijven RNI; Wet BRP art. 2.66, 2.67 lid 3) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Inschrijven niet-ingezetene | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.64, 2.66, 2.67) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht RNI inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-registratie-niet-ingezetenen-rni-inschrijven.md) | Gemeente Utrecht: Registratie niet-ingezetenen (RNI) |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md) | HUP BRP: Achtergronden en begrippen |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
- [Nummer 23](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (grondslag, open): **UPL:** de UPL noemt RNI-inschrijving als product van de gemeente, met grondslag art. 2.66 Wet BRP ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), nr. 369). **Bevinding:** de inschrijving in de RNI is een taak van de minister van BZK. De persoon verschijnt bij een inschrijfvoorziening van de minister ([2026-rijk-wet-brp-bwbr0033715](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), art. 2.64, 2.66, 2.67 lid 3); het Besluit BRP spreekt van de gemeente waar de inschrijfvoorziening is ondergebracht ([2026-rijk-besluit-brp-bwbr0034306](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md), art. 36). Welke gemeenten dat zijn, staat niet in de wet, het besluit of de regeling. Alleen een informatiepagina noemt de 19 gemeenten ([2026-nederlandwereldwijd-rni-hoe-kan-ik-mij-inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-nederlandwereldwijd-rni-hoe-kan-ik-mij-inschrijven.md)). Het product geldt dus niet voor alle gemeenten. GEMMA modelleert het als de rol RNI-loket met het proces Inschrijven niet-ingezetene, net als de reisdocumenten voor niet-ingezetenen bij aangewezen gemeenten. **Voorstel:** vermeld bij het UPL-product dat alleen gemeenten met een RNI-loket het leveren, en verwijs naar de grondslag van de loketten (de afspraak of aanwijzing door de minister), zodat gemeenten zonder loket het product niet hoeven aan te bieden.
