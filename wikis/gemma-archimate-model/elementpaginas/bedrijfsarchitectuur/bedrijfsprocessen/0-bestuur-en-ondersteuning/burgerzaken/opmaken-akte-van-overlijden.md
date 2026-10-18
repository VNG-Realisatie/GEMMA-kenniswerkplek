---
id: opmaken-akte-van-overlijden
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Opmaken akte van overlijden
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ontvangen van de aangifte van een overlijden of lijkvinding en het opmaken van de akte van overlijden.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rvig-hup-lijkvinding
- 2026-rvig-hup-overlijden-buitenland
- 2026-rvig-hup-rechtsvermoeden-van-overlijden
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvig-hup-overlijden-nederland
- 2026-utrecht-burgerzaken-overlijden-aangifte-doen
- 2026-rvo-aangifte-en-akte-van-overlijden
---

# Opmaken akte van overlijden

<!-- Gegenereerd door tools/render.py uit de beoordeling opmaken-akte-van-overlijden.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het ontvangen van de aangifte van een overlijden of lijkvinding en het opmaken van de akte van overlijden.

### Beschrijving

De ambtenaar van de burgerlijke stand van de gemeente van overlijden stelt de identiteit van de aangever vast en maakt de akte op, op grond van de verklaring van overlijden; de aangifte kan elektronisch, met het burgerservicenummer van de overledene en de verklaring van de arts (BW 1 art. 19f, 19h; Besluit burgerlijke stand art. 67a). Bij een lijkvinding maakt hij de akte op de schriftelijke aangifte van de hulpofficier van justitie; datum en plaats van de vinding gelden als datum en plaats van overlijden (Besluit burgerlijke stand art. 62; HUP Lijkvinding).

De akte gaat naar de woongemeente, die het overlijden in de BRP verwerkt en de bijhouding van de persoonslijst opschort; bij een echtgenoot of geregistreerd partner wordt de ontbinding door overlijden verwerkt (HUP Overlijden in Nederland; Utrecht). Een overlijden in het buitenland of een rechtsvermoeden van overlijden wordt via een akte van inschrijving opgenomen (HUP Overlijden buitenland; HUP Rechtsvermoeden van overlijden).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md).
- **Kernobject**: [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een aangifte van een gebeurtenis van de burgerlijke stand die de gemeente verwerkt (BW 1 art. 19h).
- **Gestart door gebeurtenis**: [Overlijden](../../../gebeurtenissen/overlijden.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [HUP BRP: Lijkvinding](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-lijkvinding.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md), [HUP BRP: Rechtsvermoeden van overlijden](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-rechtsvermoeden-van-overlijden.md) |
| **procesniveau**: bedrijfsproces, kernobject [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | Ja, van de aangifte van het overlijden tot de akte. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Aangever](../../../rollen/aangever.md), [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md). [HUP BRP: Lijkvinding](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-lijkvinding.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md), [HUP BRP: Rechtsvermoeden van overlijden](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-rechtsvermoeden-van-overlijden.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Overlijden](../../../gebeurtenissen/overlijden.md). [HUP BRP: Lijkvinding](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-lijkvinding.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md), [HUP BRP: Rechtsvermoeden van overlijden](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-rechtsvermoeden-van-overlijden.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [HUP BRP: Lijkvinding](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-lijkvinding.md), [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md), [HUP BRP: Rechtsvermoeden van overlijden](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-rechtsvermoeden-van-overlijden.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Opmaken akte van overlijden | maakt akte van overlijden op *toegang (registreren)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19f) |
| Opmaken akte van overlijden | realiseert *realisatie* | [Overlijdensaangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/overlijdensaangifte.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (UPL nr. 315; art. 19h) |
| Opmaken akte van overlijden | zendt akte aan *stroom* | [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | [HUP BRP: Overlijden nederland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-nederland.md), [Utrecht Overlijden, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) (HUP regel 19; Utrecht Op de hoogte brengen van organisaties) |
| Opmaken akte van overlijden | leidt tot *triggering* | [Verlenen verlof tot begraving of crematie](../../7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/verlenen-verlof-tot-begraving-of-crematie.md) | [Utrecht Overlijden, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md), [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (Utrecht inleiding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Opmaken akte van overlijden | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19h) |
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | maakt akte op *toewijzing* | Opmaken akte van overlijden | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19f) |
| [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Opmaken akte van overlijden | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19f) |
| [Overlijden](../../../gebeurtenissen/overlijden.md) | leidt tot *triggering* | Opmaken akte van overlijden | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Overlijden, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) (art. 19f, 19h; Utrecht inleiding) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP: Lijkvinding](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-lijkvinding.md) | HUP BRP: Lijkvinding |
| [HUP BRP: Overlijden buitenland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-buitenland.md) | HUP BRP: Overlijden buitenland |
| [HUP BRP: Rechtsvermoeden van overlijden](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-rechtsvermoeden-van-overlijden.md) | HUP BRP: Rechtsvermoeden van overlijden |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP BRP: Overlijden nederland](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-overlijden-nederland.md) | HUP BRP: Overlijden nederland |
| [Utrecht Overlijden, aangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md) | Gemeente Utrecht: Overlijden |
| [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
