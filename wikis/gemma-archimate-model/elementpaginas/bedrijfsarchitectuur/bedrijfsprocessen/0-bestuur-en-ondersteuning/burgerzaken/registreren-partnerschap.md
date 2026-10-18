---
id: registreren-partnerschap
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Registreren partnerschap
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het behandelen van de melding van een voorgenomen partnerschap en het registreren ervan, of het omzetten van een partnerschap in een huwelijk, met de akte.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Registratie van partnerschap (wet)
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-utrecht-burgerzaken-geregistreerd-partnerschap-aanvragen
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-voorgenomen-huwelijk-of-geregistreerd-partnerschap-melden
---

# Registreren partnerschap

<!-- Gegenereerd door tools/render.py uit de beoordeling registreren-partnerschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het behandelen van de melding van een voorgenomen partnerschap en het registreren ervan, of het omzetten van een partnerschap in een huwelijk, met de akte.

### Beschrijving

Het partnerschap wordt geregistreerd bij akte, opgemaakt door de ambtenaar; een ja-woord is niet verplicht (BW 1 art. 80a; Utrecht). Een partnerschap kan worden omgezet in een huwelijk met een akte van omzetting, zonder melding vooraf en zonder getuigen (BW 1 art. 80g; Utrecht). Locaties, tarieven en trouwambtenaar volgen het huwelijk (Utrecht Trouwen in Utrecht).

### Deelprocessen

1. **Melding voorgenomen partnerschap**: Zoals bij het huwelijk; een omzetting van een partnerschap in een huwelijk begint met een eigen verzoek, zonder melding. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80a, 80g)
2. **Registreren**: De ambtenaar maakt de akte van registratie op, of de akte van omzetting in een huwelijk. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80a, 80g)

### Synoniemen

| Synoniem | Context |
|---|---|
| Registratie van partnerschap | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md).
- **Kernobject**: [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geregistreerd partnerschap aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geregistreerd-partnerschap-aanvragen.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **procesniveau**: bedrijfsproces, kernobject [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | Ja, van de melding van het voorgenomen partnerschap, of het verzoek om omzetting, tot de akte. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geregistreerd partnerschap aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geregistreerd-partnerschap-aanvragen.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geregistreerd partnerschap aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geregistreerd-partnerschap-aanvragen.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met Melding van voorgenomen partnerschap gedaan (gebeurtenis, nog geen element), Verzoek om omzetting in huwelijk ingediend (gebeurtenis, nog geen element): De melding van het voorgenomen partnerschap, of het verzoek om omzetting in een huwelijk (BW 1 art. 80a, 80g; Utrecht). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geregistreerd partnerschap aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geregistreerd-partnerschap-aanvragen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geregistreerd partnerschap aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geregistreerd-partnerschap-aanvragen.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Registreren partnerschap | maakt partnerschapsakte of akte van omzetting op *toegang (registreren)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (art. 80a, 80g) |
| Registreren partnerschap | realiseert *realisatie* | [Geregistreerd partnerschap omzetting in huwelijk](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/geregistreerd-partnerschap-omzetting-in-huwelijk.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geregistreerd partnerschap aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geregistreerd-partnerschap-aanvragen.md) (UPL nr. 156) |
| Registreren partnerschap | verifieert gegevens van *toegang (raadplegen)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 18 lid 2) |
| Registreren partnerschap | realiseert *realisatie* | [Geregistreerd partnerschapaangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/geregistreerd-partnerschapaangifte.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Voorgenomen huwelijk melden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voorgenomen-huwelijk-of-geregistreerd-partnerschap-melden.md) (UPL nr. 158) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | maakt akte op, ontvangt kennisgeving *toewijzing* | Registreren partnerschap | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80a lid 3, 80g; art. 44) |
| [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Registreren partnerschap | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80a, 80g) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Utrecht Geregistreerd partnerschap aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geregistreerd-partnerschap-aanvragen.md) | Gemeente Utrecht: Geregistreerd partnerschap |
| [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Voorgenomen huwelijk melden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voorgenomen-huwelijk-of-geregistreerd-partnerschap-melden.md) | Gemeente Utrecht: Melden voorgenomen huwelijk |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
