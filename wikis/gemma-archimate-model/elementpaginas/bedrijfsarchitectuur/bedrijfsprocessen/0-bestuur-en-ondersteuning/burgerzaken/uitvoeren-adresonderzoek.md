---
id: uitvoeren-adresonderzoek
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Uitvoeren adresonderzoek
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het onderzoeken of een persoon woont op het adres waarop hij is ingeschreven, en het besluiten over een juiste inschrijving.
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Adresonderzoek (beleid)
bronnen:
- 2023-rvig-circulaire-adresonderzoek-brp
- 2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek
- 2026-nvvb-handreiking-adresonderzoek
- 2026-rijk-besluit-brp-bwbr0034306
- 2026-rijk-wet-brp-bwbr0033715
---

# Uitvoeren adresonderzoek

<!-- Gegenereerd door tools/render.py uit de beoordeling uitvoeren-adresonderzoek.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het onderzoeken of een persoon woont op het adres waarop hij is ingeschreven, en het besluiten over een juiste inschrijving.

### Beschrijving

Het adresonderzoek is het instrument waarmee de gemeente een verkeerde adresinschrijving verbetert; zij start het bij twijfel over de juistheid van adresgegevens (Circulaire adresonderzoek par. 2). Aanleidingen zijn een melding van een bewoner of organisatie, een terugmelding van een bestuursorgaan, een signaal uit de Landelijke Aanpak Adreskwaliteit (LAA), een eigen constatering of een aangifte van verhuizing (Circulaire adresonderzoek; NVVB Handreiking adresonderzoek). De gemeente legt een onderzoeksdossier aan, plaatst een aantekening in onderzoek, schrijft de persoon aan, kan een huisbezoek laten afleggen door een toezichthouder BRP en neemt na een voornemen een besluit; de melder wordt over het resultaat geïnformeerd (Circulaire adresonderzoek 3.2–4.7). Een richtlijn voor de doorlooptijd is tien weken.

De uitkomst is: woont nog op het adres, inschrijving op een briefadres, vestiging vanuit het buitenland, ambtshalve verhuizing binnen of naar een andere gemeente, of ambtshalve vertrek naar het buitenland of naar een onbekend land (Circulaire adresonderzoek 4.8).

### Synoniemen

| Synoniem | Context |
|---|---|
| Adresonderzoek | beleid |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md), [Toezichthouder BRP](../../../rollen/toezichthouder-brp.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een melding van een persoon of organisatie, een terugmelding, een LAA-signaal of een eigen constatering (Circulaire adresonderzoek par. 2; NVVB Handreiking adresonderzoek). [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [NVVB Handreiking adresonderzoek](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-nvvb-handreiking-adresonderzoek.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een besluit: woont nog op het adres, briefadres, ambtshalve verhuizing, ambtshalve vertrek of vestiging vanuit het buitenland (Circulaire adresonderzoek 4.8). [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [NVVB Handreiking adresonderzoek](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-nvvb-handreiking-adresonderzoek.md), [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, circulaire adresonderzoek BRP: voornemen en besluit, terugkoppeling binnen vijf werkdagen of vier weken, richtlijn tien weken; Besluit BRP art. 28a tot en met 28g (LAA). [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de melding, het signaal of de eigen constatering tot het besluit. [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [NVVB Handreiking adresonderzoek](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-nvvb-handreiking-adresonderzoek.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, het college neemt na een voornemen een besluit en maakt het bekend (Circulaire adresonderzoek 4.6). [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Onjuiste inschrijving op adres melden](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/onjuiste-inschrijving-op-adres-melden.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Uitvoeren adresonderzoek | verbetert *toegang (bijwerken)* | [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md) | [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) (4.8) |
| Uitvoeren adresonderzoek | realiseert *realisatie* | [Onjuiste inschrijving op adres melden](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/onjuiste-inschrijving-op-adres-melden.md) | [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md), [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) (Na uw melding; Wet BRP art. 2.20 lid 2; Circulaire adresonderzoek 4.7 (melder)) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | besluit na *toewijzing* | Uitvoeren adresonderzoek | [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) (4.6) |
| [Besluit basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Uitvoeren adresonderzoek | [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) (art. 28a–28g) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Uitvoeren adresonderzoek | [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) (par. 2, 4) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Uitvoeren adresonderzoek | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.20 lid 2) |
| [Toezichthouder BRP](../../../rollen/toezichthouder-brp.md) | legt huisbezoek af *toewijzing* | Uitvoeren adresonderzoek | [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (4.5; Wet BRP art. 4.2) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) | Circulaire adresonderzoek BRP |
| [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md) | Gemeente Utrecht: Adresonderzoek |
| [NVVB Handreiking adresonderzoek](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-nvvb-handreiking-adresonderzoek.md) | NVVB: Adresonderzoek |
| [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
