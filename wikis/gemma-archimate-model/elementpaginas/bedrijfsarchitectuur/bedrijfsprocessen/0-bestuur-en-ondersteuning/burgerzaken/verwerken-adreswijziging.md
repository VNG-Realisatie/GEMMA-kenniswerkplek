---
id: verwerken-adreswijziging
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Verwerken adreswijziging
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verwerken van een verhuizing binnen of naar de gemeente in de verblijfplaats van de ingeschreven persoon.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Binnengemeentelijke adreswijziging (HUP)
- Intergemeentelijke adreswijziging (HUP)
bronnen:
- 2026-utrecht-burgerzaken-verhuizing-doorgeven
- 2026-rvig-hup-intergemeentelijke-adreswijziging
- 2026-rvig-hup-binnengemeentelijke-adreswijziging
- 2026-rijk-wet-brp-bwbr0033715
- 2025-vng-upl-producten-en-diensten-extern
---

# Verwerken adreswijziging

<!-- Gegenereerd door tools/render.py uit de beoordeling verwerken-adreswijziging.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het verwerken van een verhuizing binnen of naar de gemeente in de verblijfplaats van de ingeschreven persoon.

### Beschrijving

Wie binnen of naar de gemeente verhuist, doet aangifte van adreswijziging, vanaf vier weken voor tot de vijfde dag na de verhuizing; alle verhuizende personen ondertekenen, de aangifte kan schriftelijk of digitaal met DigiD en de gemeente kan de betrouwbaarheid controleren (HUP Binnengemeentelijke adreswijziging; Utrecht Verhuizing doorgeven). Bij een verhuizing vanuit een andere gemeente wordt de nieuwe gemeente bijhoudingsgemeente en neemt zij de persoonslijst over, met openstaande onderzoeken (HUP Intergemeentelijke adreswijziging). Wie bij iemand anders gaat wonen, levert een verklaring van inwoning van de hoofdbewoner (Utrecht).

Een infrastructurele wijziging zonder verhuizing (straatnaamwijziging, vernummering, gemeentelijke herindeling) wordt als adreswijziging verwerkt, zonder aangifte (HUP Binnengemeentelijke en Intergemeentelijke adreswijziging).

### Synoniemen

| Synoniem | Context |
|---|---|
| Binnengemeentelijke adreswijziging | HUP |
| Intergemeentelijke adreswijziging | HUP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. De verwerking volgt op een aangifte van adreswijziging die de basisregistratie bijwerkt (HUP Binnengemeentelijke adreswijziging).
- **Gestart door gebeurtenis**: [Verhuizing](../../../gebeurtenissen/verhuizing.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **procesniveau**: bedrijfsproces, kernobject [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md) | Ja, van de aangifte, of ambtshalve, tot de nieuwe verblijfplaats. [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Aangever](../../../rollen/aangever.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Verhuizing](../../../gebeurtenissen/verhuizing.md). [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken adreswijziging | legt vast *toegang (bijwerken)* | [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md) | [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.20 lid 1) |
| Verwerken adreswijziging | realiseert *realisatie* | [Verhuismelding](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/verhuismelding.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 424; Wet BRP art. 2.39) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Verwerken adreswijziging | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verwerken adreswijziging | [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) (HUP Binnengemeentelijke en Intergemeentelijke adreswijziging) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Verwerken adreswijziging | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.39) |
| [Verhuizing](../../../gebeurtenissen/verhuizing.md) | leidt tot *triggering* | Verwerken adreswijziging | [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (HUP inleiding; Utrecht inleiding; Wet BRP art. 2.39 lid 1) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Verwerken adreswijziging | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.20, 2.39) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) | Gemeente Utrecht: Verhuizing doorgeven |
| [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) | HUP BRP: Intergemeentelijke adreswijziging |
| [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) | HUP BRP: Binnengemeentelijke adreswijziging |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
