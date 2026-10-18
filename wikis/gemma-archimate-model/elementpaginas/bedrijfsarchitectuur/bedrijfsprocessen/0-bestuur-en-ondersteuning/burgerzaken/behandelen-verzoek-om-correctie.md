---
id: behandelen-verzoek-om-correctie
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Behandelen verzoek om correctie
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beslissen op een verzoek van een ingeschrevene om onjuiste gegevens in de basisregistratie personen te corrigeren.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Correctieverzoek (HUP)
bronnen:
- 2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp
- 2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens
- 2018-nvvb-stappenplan-identiteitswijziging-brp
- 2026-rijk-wet-brp-bwbr0033715
- 2025-vng-upl-producten-en-diensten-extern
---

# Behandelen verzoek om correctie

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-verzoek-om-correctie.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

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

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek waarop de gemeente na beoordeling van de bewijsstukken beslist (Utrecht).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **procesniveau**: bedrijfsproces, kernobject [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | Ja, van het verzoek tot de gecorrigeerde gegevens of de weigering. [HUP BRP Correcties](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [NVVB Stappenplan identiteitswijziging BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2018-nvvb-stappenplan-identiteitswijziging-brp.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, verzoek van de burger om correctie, met bewijsstukken (HUP Correcties; Utrecht). [HUP BRP Correcties](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) |

### Specialisaties

- **Identiteitswijziging**: Correctie waardoor in feite de identiteit in de BRP wijzigt, zoals de geboortedatum; met een eigen stappenplan van de NVVB (NVVB Identiteitswijziging). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen verzoek om correctie | corrigeert *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [HUP BRP Correcties](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Persoonsgegevens aanpassen; Wet BRP art. 2.58) |
| Behandelen verzoek om correctie | realiseert *realisatie* | [BRP-wijzigingsverzoek](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-wijzigingsverzoek.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 95; Wet BRP art. 2.58) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Behandelen verzoek om correctie | [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) (Na uw aanvraag) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Behandelen verzoek om correctie | [HUP BRP Correcties](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) (inleiding) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Behandelen verzoek om correctie | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 2.58) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Behandelen verzoek om correctie | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.58) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht BRP-gegevens opvragen of aanpassen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-persoonsgegevens-opvragen-of-aanpassen-brp.md) | Gemeente Utrecht: Persoonsgegevens opvragen of aanpassen |
| [HUP BRP Correcties](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-correcties-en-ten-onrechte-opgenomen-gegevens.md) | HUP BRP: Correcties en ten onrechte opgenomen gegevens |
| [NVVB Stappenplan identiteitswijziging BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2018-nvvb-stappenplan-identiteitswijziging-brp.md) | NVVB: Stappenplan identiteitswijziging in de BRP |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
