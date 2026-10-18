---
id: behandelen-verzoek-om-geheimhouding
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Behandelen verzoek om geheimhouding
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het verwerken van een verzoek om persoonsgegevens niet aan bepaalde derden te verstrekken, of om die geheimhouding te beëindigen.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden
- 2026-rvig-hup-verstrekkingsbeperking
- 2026-rijk-wet-brp-bwbr0033715
- 2025-vng-upl-producten-en-diensten-extern
---

# Behandelen verzoek om geheimhouding

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-verzoek-om-geheimhouding.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het verwerken van een verzoek om persoonsgegevens niet aan bepaalde derden te verstrekken, of om die geheimhouding te beëindigen.

### Beschrijving

De burger kan verstrekking aan overheidsorganen op grond van een autorisatiebesluit niet tegenhouden, maar wel schriftelijk verzoeken geen gegevens te verstrekken aan bepaalde derden (HUP Verstrekkingsbeperking). Het verzoek is vormvrij en hoeft niet te worden gemotiveerd; de gemeente stelt de identiteit vast, verwerkt het binnen vier weken, bevestigt het schriftelijk en weigert het niet als de juiste persoon het doet (HUP Verstrekkingsbeperking). Online kan het met DigiD binnen vijf werkdagen; de geheimhouding verhuist mee naar een nieuwe gemeente (Utrecht Persoonsgegevens geheimhouden).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek om een product dat de gemeente toekent als de juiste persoon het doet (HUP Verstrekkingsbeperking).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md) |
| **procesniveau**: bedrijfsproces, kernobject [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | Ja, van het verzoek tot de aantekening en de bevestiging. [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, schriftelijk verzoek van de ingeschrevene van 16 jaar of ouder, of van ouder, voogd of curator (HUP Verstrekkingsbeperking). [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen verzoek om geheimhouding | tekent geheimhouding aan *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.59 lid 1) |
| Behandelen verzoek om geheimhouding | realiseert *realisatie* | [BRP-geheimhoudingsverzoek](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-geheimhoudingsverzoek.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 87; Wet BRP art. 2.59) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Behandelen verzoek om geheimhouding | [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) (art. 2.60 Wet BRP) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Behandelen verzoek om geheimhouding | [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) (inleiding) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Behandelen verzoek om geheimhouding | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 2.59) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Behandelen verzoek om geheimhouding | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.59) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Persoonsgegevens geheimhouden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-geheimhouden.md) | Gemeente Utrecht: Persoonsgegevens geheimhouden |
| [HUP Verstrekkingsbeperking](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verstrekkingsbeperking.md) | HUP BRP: Verstrekkingsbeperking |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
