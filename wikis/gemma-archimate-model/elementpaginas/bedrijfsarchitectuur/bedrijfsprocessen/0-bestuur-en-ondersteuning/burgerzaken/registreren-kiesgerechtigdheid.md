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
match:
  gemma: geen
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

<!-- Gegenereerd door tools/render.py uit de beoordeling registreren-kiesgerechtigdheid.yaml. Wijzig de beoordeling, niet deze pagina. -->

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

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Functie-indeling naar domein, bediend door**: [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md).
- **Gestart door gebeurtenis**: [Uitsluiting van het kiesrecht](../../../gebeurtenissen/uitsluiting-van-het-kiesrecht.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [HUP Kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md), [HUP Europees kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) |
| **procesniveau**: bedrijfsproces, kernobject [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | Ja, van de mededeling of het verzoek tot de registratie of de kennisgeving. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Kiezer](../../../rollen/kiezer.md). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [HUP Kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md), [HUP Europees kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Uitsluiting van het kiesrecht](../../../gebeurtenissen/uitsluiting-van-het-kiesrecht.md). [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [HUP Kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md), [HUP Europees kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [HUP Kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md), [HUP Europees kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Registreren kiesgerechtigdheid | registreert de kiesgerechtigdheid *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Nederlands kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlands-kiesrecht.md), [HUP Europees kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) (Kieswet art. D 1; HUP Nederlands en Europees kiesrecht) |
| Registreren kiesgerechtigdheid | realiseert *realisatie* | [Stemrecht](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/stemrecht.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (UPL nr. 398) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist op een aanvraag tot wijziging *toewijzing* | Registreren kiesgerechtigdheid | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. D 7) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Registreren kiesgerechtigdheid | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md) (Kieswet art. D 1; HUP Kiesrecht) |
| [Kieswet](../../../../motivatie/beleidskaders/rijksregelgeving/kieswet.md) | is grondslag voor *associatie (gericht)* | Registreren kiesgerechtigdheid | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. B 5, D 1-D 7) |
| [Kiezer](../../../rollen/kiezer.md) | verzoekt om mededeling of registratie *toewijzing* | Registreren kiesgerechtigdheid | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) (Kieswet art. D 5; HUP Europees kiesrecht) |
| [Uitsluiting van het kiesrecht](../../../gebeurtenissen/uitsluiting-van-het-kiesrecht.md) | leidt tot *triggering* | Registreren kiesgerechtigdheid | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Nederlands kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlands-kiesrecht.md) (Kieswet art. B 5 lid 3; HUP Nederlands kiesrecht) |
| [Verkiezingen gerelateerde diensten](../../../bedrijfsfuncties/publieksdiensten/verkiezingen-gerelateerde-diensten.md) | bedient *bediening* | Registreren kiesgerechtigdheid | [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (Kieswet art. D 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP Kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-kiesrecht.md) | HUP BRP: Kiesrecht |
| [HUP Europees kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) | HUP BRP: Europees kiesrecht |
| [HUP Nederlands kiesrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlands-kiesrecht.md) | HUP BRP: Nederlands kiesrecht |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
