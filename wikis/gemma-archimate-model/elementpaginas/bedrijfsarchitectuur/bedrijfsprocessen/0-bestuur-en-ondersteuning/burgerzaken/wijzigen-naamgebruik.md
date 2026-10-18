---
id: wijzigen-naamgebruik
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Wijzigen naamgebruik
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het beslissen op een verzoek van een (voormalig) gehuwde of geregistreerde partner welke achternaam de overheid voor hem gebruikt.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rvig-hup-wijziging-naamgebruik
- 2026-utrecht-burgerzaken-achternaamgebruik-veranderen
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-wet-brp-bwbr0033715
---

# Wijzigen naamgebruik

<!-- Gegenereerd door tools/render.py uit de beoordeling wijzigen-naamgebruik.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het beslissen op een verzoek van een (voormalig) gehuwde of geregistreerde partner welke achternaam de overheid voor hem gebruikt.

### Beschrijving

Wie getrouwd of geregistreerd partner is of was, kiest de eigen naam, de naam van de partner of een combinatie in beide volgorden (BW 1 art. 9; Utrecht). Het college geeft binnen vier weken gevolg; weigeren is gelijkgesteld aan een Awb-besluit (Wet BRP art. 2.60; HUP Wijziging naamgebruik). De keuze gaat naar andere overheidsorganisaties; op een paspoort of rijbewijs staat altijd de eigen achternaam (Utrecht).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een verzoek waarop het college beslist (HUP Wijziging naamgebruik).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **procesniveau**: bedrijfsproces, kernobject [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | Ja, van het verzoek tot de gewijzigde aanduiding of de weigering. [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Verzoek om wijziging naamgebruik ingediend (gebeurtenis, nog geen element): Een schriftelijk verzoek van een (voormalig) gehuwde of geregistreerde partner, online, aan de balie of met een formulier (HUP Wijziging naamgebruik; Utrecht). [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Wijzigen naamgebruik | wijzigt naamgebruik van *toegang (bijwerken)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.25) |
| Wijzigen naamgebruik | realiseert *realisatie* | [Naamgebruik verzoek aanduiding](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/naamgebruik-verzoek-aanduiding.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (UPL nr. 257; Wet BRP art. 2.25) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Wijzigen naamgebruik | [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) (regel 34) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Wijzigen naamgebruik | [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) (inleiding) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Wijzigen naamgebruik | [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) (regel 34, 60) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Wijzigen naamgebruik | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 2.25) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Wijziging naamgebruik](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-wijziging-naamgebruik.md) | HUP BRP: Wijziging naamgebruik |
| [Utrecht Achternaamgebruik veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-achternaamgebruik-veranderen.md) | Gemeente Utrecht: Achternaamgebruik |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
