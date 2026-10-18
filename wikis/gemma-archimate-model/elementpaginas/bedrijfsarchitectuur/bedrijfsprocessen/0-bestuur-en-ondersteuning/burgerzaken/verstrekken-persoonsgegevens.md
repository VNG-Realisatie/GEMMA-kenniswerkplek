---
id: verstrekken-persoonsgegevens
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Verstrekken persoonsgegevens
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beslissen op een verzoek om gegevens uit de basisregistratie personen en het verstrekken ervan aan de ingeschrevene of aan anderen.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Schriftelijke gegevensverstrekking (beleid)
bronnen:
- 2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp
- 2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen
- 2026-rijk-besluit-brp-bwbr0034306
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-bewijs-van-in-leven-zijn-of-attestatie-de-vita-aanvragen
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
---

# Verstrekken persoonsgegevens

<!-- Gegenereerd door tools/render.py uit de beoordeling verstrekken-persoonsgegevens.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het beslissen op een verzoek om gegevens uit de basisregistratie personen en het verstrekken ervan aan de ingeschrevene of aan anderen.

### Beschrijving

Het college ontvangt verzoeken om gegevens uit de BRP: van de ingeschrevene zelf (inzage, kopie, uittreksel; art. 2.55 Wet BRP) en van overheidsorganen, bij besluit aangewezen derden, bij gemeentelijke verordening aangewezen derden en overige verzoekers (NVVB Schema; UPL). De medewerker stelt vast wie verzoekt en waarvoor, deelt het verzoek in, verstrekt de gegevens die daarbij horen en protocolleert de verstrekking; bij een geregistreerde verstrekkingsbeperking volgt een belangenafweging (NVVB Schema). Gegevens in onderzoek worden met vermelding daarvan verstrekt; verzoeken over niet-ingezetenen gaan naar een RNI-loket (NVVB Schema).

De systematische verstrekking aan afnemers loopt via de BRP-verstrekkingsvoorziening van de minister, niet via dit proces (LO BRP 1.5.2; Besluit BRP art. 37).

### Synoniemen

| Synoniem | Context |
|---|---|
| Schriftelijke gegevensverstrekking | beleid |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek om een product (uittreksel, verstrekking) dat de gemeente levert (NVVB Schema).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md), [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |
| **procesniveau**: bedrijfsproces, kernobject [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | Ja, van het verzoek tot de verstrekking of de weigering. [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md), [RNI-loket](../../../rollen/rni-loket.md). [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md), [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een verzoek van de ingeschrevene, een overheidsorgaan of een derde (NVVB Schema, stap 1). [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md), [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verstrekken persoonsgegevens | verstrekt gegevens van *toegang (verstrekken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) (Schema 1 t/m 4) |
| Verstrekken persoonsgegevens | realiseert *realisatie* | [BRP-inzagerecht](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inzagerecht.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 91) |
| Verstrekken persoonsgegevens | realiseert *realisatie* | [BRP-uittreksel](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-uittreksel.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) (UPL nr. 93) |
| Verstrekken persoonsgegevens | realiseert *realisatie* | [BRP-uittreksel met gezag](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-uittreksel-met-gezag.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (UPL nr. 94) |
| Verstrekken persoonsgegevens | realiseert *realisatie* | [Bewijs van in leven zijn](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/bewijs-van-in-leven-zijn.md) | [Utrecht Bewijs van in leven zijn of attestatie de vita](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-bewijs-van-in-leven-zijn-of-attestatie-de-vita-aanvragen.md) (Bewijs van in leven zijn (uittreksel BRP)) |
| Verstrekken persoonsgegevens | realiseert *realisatie* | [Bewijs van nederlanderschap](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/bewijs-van-nederlanderschap.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (UPL nr. 62; Besluit art. 61) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Verstrekken persoonsgegevens | [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) (Belangenafweging) |
| [Besluit basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Verstrekken persoonsgegevens | [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) (art. 40) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Verstrekken persoonsgegevens | [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) (Waarom dit schema) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Verstrekken persoonsgegevens | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP hoofdstuk 3, paragraaf 3) |
| [RNI-loket](../../../rollen/rni-loket.md) | verstrekt gegevens over niet-ingezetenen *toewijzing* | Verstrekken persoonsgegevens | [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Niet-ingezetenen; Wet BRP art. 2.79, 3.19 lid 2) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [NVVB Schema schriftelijke gegevensverstrekking BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2024-nvvb-schema-schriftelijke-gegevensverstrekking-brp.md) | Schema verzoeken om schriftelijke gegevensverstrekking uit de BRP |
| [Utrecht BRP bekijken en overzicht aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-brp-bekijken-en-overzicht-aanvragen.md) | Gemeente Utrecht: Persoonsgegevens bekijken of aanvragen |
| [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Bewijs van in leven zijn of attestatie de vita](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-bewijs-van-in-leven-zijn-of-attestatie-de-vita-aanvragen.md) | Gemeente Utrecht: Verklaring van in leven zijn (attestatie de vita) |
| [Besluit verkrijging en verlies Nederlanderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
