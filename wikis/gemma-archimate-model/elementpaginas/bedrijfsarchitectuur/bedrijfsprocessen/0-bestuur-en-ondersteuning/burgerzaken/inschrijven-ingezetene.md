---
id: inschrijven-ingezetene
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Inschrijven ingezetene
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het inschrijven van een persoon die zich vanuit het buitenland in de gemeente vestigt als ingezetene in de basisregistratie personen.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Eerste inschrijving (LO BRP)
bronnen:
- 2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland
- 2026-rvig-hup-hervestiging
- 2026-rijk-besluit-brp-bwbr0034306
- 2026-rvig-hup-immigratie
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-adoptie-kind-inschrijven
---

# Inschrijven ingezetene

<!-- Gegenereerd door tools/render.py uit de beoordeling inschrijven-ingezetene.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het inschrijven van een persoon die zich vanuit het buitenland in de gemeente vestigt als ingezetene in de basisregistratie personen.

### Beschrijving

Wie zich vanuit het buitenland in de gemeente vestigt, doet uiterlijk de vijfde dag na aanvang van het verblijf in persoon aangifte van verblijf en adres (HUP Immigratie). De gemeente stelt de identiteit vast, toetst de criteria (waaronder rechtmatig verblijf), gaat na of de persoon al in de BRP of RNI voorkomt, verifieert het adres en schrijft de persoon in met een A-nummer en een BSN; binnen vier weken stuurt zij een volledig overzicht van de persoonslijst (HUP Immigratie; Utrecht Inschrijven vanuit het buitenland). Kan de geboortedatum of de vreemde nationaliteit niet uit de gewone bronnen worden ontleend, dan vraagt de gemeente een mededeling ex artikel 2.17 Wet BRP op bij de IND (NVVB mededeling art. 2.17). Ontbreekt een brondocument, dan neemt de gemeente een verklaring onder eed of belofte af (HUP Immigratie; UPL nr. 335).

Bij een hervestiging staat de persoon al in de RNI: de gemeente wordt bijhoudingsgemeente en stelt alle gegevens vast aan de hand van brondocumenten (HUP Hervestiging). Het college beslist over de inschrijving (Besluit BRP art. 24).

### Synoniemen

| Synoniem | Context |
|---|---|
| Eerste inschrijving | LO BRP |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md).
- **Kernobject**: [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. De inschrijving volgt op een aangifte van verblijf en adres die de basisregistratie bijwerkt (HUP Immigratie).
- **Gestart door gebeurtenis**: [Adoptie](../../../gebeurtenissen/adoptie.md), [Vestiging vanuit het buitenland](../../../gebeurtenissen/vestiging-vanuit-het-buitenland.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Hervestiging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |
| **procesniveau**: bedrijfsproces, kernobject [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | Ja, van de aangifte tot de persoonslijst en het overzicht. [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Aangever](../../../rollen/aangever.md), [Beslisser](../../../rollen/beslisser.md), [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md). [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Hervestiging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Adoptie](../../../gebeurtenissen/adoptie.md), [Vestiging vanuit het buitenland](../../../gebeurtenissen/vestiging-vanuit-het-buitenland.md). [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Hervestiging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md), [HUP Hervestiging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md), [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Inschrijven ingezetene | schrijft in *toegang (registreren)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) (inleiding) |
| Inschrijven ingezetene | legt vast *toegang (registreren)* | [Verblijfplaats](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verblijfplaats.md) | [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) (Stap 5) |
| Inschrijven ingezetene | ontleent gegevens aan *toegang (raadplegen)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md), [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) (Utrecht Wat neemt u mee) |
| Inschrijven ingezetene | realiseert *realisatie* | [BRP-inschrijving](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) (UPL nr. 88) |
| Inschrijven ingezetene | realiseert *realisatie* | [Persoonsgegevens verklaring onder eed of belofte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/persoonsgegevens-verklaring-onder-eed-of-belofte.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) (UPL nr. 335; HUP Immigratie categorie 04) |
| Inschrijven ingezetene | realiseert *realisatie* | [Adoptie aangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/adoptie-aangifte.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Adoptie, kind inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-adoptie-kind-inschrijven.md) (UPL nr. 6; Utrecht inleiding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Inschrijven ingezetene | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Adoptie](../../../gebeurtenissen/adoptie.md) | leidt tot (adoptiekind uit het buitenland) *triggering* | Inschrijven ingezetene | [Utrecht Adoptie, kind inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-adoptie-kind-inschrijven.md) (inleiding) |
| [Beslisser](../../../rollen/beslisser.md) | beslist over *toewijzing* | Inschrijven ingezetene | [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) (Besluit BRP art. 24) |
| [Besluit basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Inschrijven ingezetene | [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) (art. 24, 30) |
| [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | omvat *aggregatie* | Inschrijven ingezetene | [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md) (HUP Immigratie; HUP Hervestiging) |
| [Bijhoudingsgemeente](../../../rollen/bijhoudingsgemeente.md) | voert uit *toewijzing* | Inschrijven ingezetene | [HUP BRP Achtergronden en begrippen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-achtergronden-en-begrippen.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (BRP stelsel; Wet BRP art. 1.4 lid 1, 2.38) |
| [Vestiging vanuit het buitenland](../../../gebeurtenissen/vestiging-vanuit-het-buitenland.md) | leidt tot *triggering* | Inschrijven ingezetene | [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md), [HUP Hervestiging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.2, 2.38 lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Inschrijven vanuit het buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-inschrijven-vanuit-het-buitenland.md) | Gemeente Utrecht: Inschrijven vanuit het buitenland |
| [HUP Hervestiging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-hervestiging.md) | HUP BRP: Hervestiging |
| [Besluit BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md) | Besluit basisregistratie personen |
| [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) | HUP BRP: Immigratie |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Adoptie, kind inschrijven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-adoptie-kind-inschrijven.md) | Gemeente Utrecht: Adoptie |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
