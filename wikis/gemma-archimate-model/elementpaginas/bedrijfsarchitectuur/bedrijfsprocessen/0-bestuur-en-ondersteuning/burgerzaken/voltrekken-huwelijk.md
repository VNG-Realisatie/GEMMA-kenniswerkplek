---
id: voltrekken-huwelijk
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Voltrekken huwelijk
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het behandelen van de melding van een voorgenomen huwelijk, het in het openbaar voltrekken ervan en het opmaken van de huwelijksakte.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Huwelijksvoltrekking (wet)
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-utrecht-burgerzaken-trouwen-in-utrecht
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2025-vng-upl-producten-en-diensten-extern
- 2026-utrecht-burgerzaken-trouwlocaties-in-utrecht
- 2026-rvig-hup-huwelijkgeregistreerd-partnerschap
- 2026-utrecht-burgerzaken-voorgenomen-huwelijk-of-geregistreerd-partnerschap-melden
---

# Voltrekken huwelijk

<!-- Gegenereerd door tools/render.py uit de beoordeling voltrekken-huwelijk.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het behandelen van de melding van een voorgenomen huwelijk, het in het openbaar voltrekken ervan en het opmaken van de huwelijksakte.

### Beschrijving

Het huwelijk wordt in het openbaar voltrokken in het gemeentehuis, met twee tot vier meerderjarige getuigen; de partijen verschijnen in persoon (BW 1 art. 63, 65). Burgemeester en wethouders kunnen andere gebouwen als huis der gemeente aanwijzen: eigen locaties, vaste trouwlocaties en een locatie naar keuze die de gemeente goedkeurt (BW 1 art. 63, 64; Utrecht Trouwlocaties). De gemeente kiest de trouwambtenaar; een eigen trouwambtenaar voor één dag wordt als buitengewoon ambtenaar aangewezen (BW 1 art. 16; Utrecht).

Gemeenten bieden varianten met eigen tarieven, van gratis trouwen op vaste momenten tot een locatie naar keuze (Utrecht); tarieven en wachtlijsten zijn lokaal. Bij het trouwen kunnen de ouders eenmalig de achternaam van hun gezamenlijke kinderen veranderen (Utrecht). De huwelijksakte gaat naar de woongemeenten voor de BRP.

De aanstaande echtgenoten verstrekken hun gegevens, een verklaring over bloedverwantschap en eerdere huwelijken, de getuigen en zo nodig gegevens over het verblijfsrecht; de ambtenaar verifieert die in de BRP, bewaart de verklaring omtrent verblijfsrecht twaalf jaar voor de IND en meldt een vermoeden van een schijnhuwelijk (BW 1 art. 18, 44, 58; Besluit burgerlijke stand art. 28). Bij beletselen stuit het openbaar ministerie het huwelijk (BW 1 art. 80a lid 4). De melding vervalt na een jaar (art. 46).

Online met DigiD, door beide partners elk met een eigen formulier, of aan de balie; gratis (Utrecht). Wie in het buitenland woont, meldt bij de gemeente Den Haag (Utrecht).

### Deelprocessen

1. **Melding voorgenomen huwelijk**: De aanstaande echtgenoten melden het huwelijk minstens 14 dagen en hoogstens een jaar vooraf; de ambtenaar verifieert de gegevens en meldt een vermoeden van een schijnhuwelijk. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Voorgenomen huwelijk melden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voorgenomen-huwelijk-of-geregistreerd-partnerschap-melden.md) (BW 1 art. 44, 46, 58; Utrecht)
2. **Voltrekken**: Het huwelijk wordt in het openbaar voltrokken met twee tot vier getuigen, in het gemeentehuis of op een aangewezen locatie, en de ambtenaar maakt de huwelijksakte op. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 63-65)

### Synoniemen

| Synoniem | Context |
|---|---|
| Huwelijksvoltrekking | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md).
- **Kernobject**: [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een aanvraag van een product van de gemeente: het voltrekken van het huwelijk op een gekozen datum en locatie (Utrecht).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md), [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de melding van het voorgenomen huwelijk en de afgesproken datum en locatie (BW 1 art. 44, 62; Utrecht). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Trouwen in Utrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-utrecht.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, het voltrokken huwelijk en de huwelijksakte (BW 1 art. 63). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Trouwen in Utrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-utrecht.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, BW 1 art. 62-67; Besluit burgerlijke stand art. 1, 57. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de melding van het voorgenomen huwelijk tot de voltrekking en de huwelijksakte. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Trouwen in Utrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-utrecht.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Huwelijk](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/huwelijk.md), [Trouwlocatie](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/trouwlocatie.md), [Ambtenaar burgerlijke stand aanvragen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/ambtenaar-burgerlijke-stand-aanvragen.md), [Huwelijksaangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/huwelijksaangifte.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Voltrekken huwelijk | maakt huwelijksakte op *toegang (registreren)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (art. 63; Besluit art. 57) |
| Voltrekken huwelijk | realiseert *realisatie* | [Huwelijk](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/huwelijk.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Trouwen in Utrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-utrecht.md) (UPL nr. 184) |
| Voltrekken huwelijk | realiseert *realisatie* | [Trouwlocatie](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/trouwlocatie.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Trouwlocaties](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwlocaties-in-utrecht.md) (UPL nr. 414) |
| Voltrekken huwelijk | realiseert *realisatie* | [Ambtenaar burgerlijke stand aanvragen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/ambtenaar-burgerlijke-stand-aanvragen.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Trouwen in Utrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-utrecht.md) (UPL nr. 28; Utrecht trouwambtenaar voor één dag) |
| Voltrekken huwelijk | zendt huwelijksakte aan *stroom* | [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | [HUP BRP: Huwelijk en geregistreerd partnerschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-huwelijkgeregistreerd-partnerschap.md) (inleiding) |
| Voltrekken huwelijk | verifieert gegevens van *toegang (raadplegen)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 18 lid 2) |
| Voltrekken huwelijk | realiseert *realisatie* | [Huwelijksaangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/huwelijksaangifte.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Voorgenomen huwelijk melden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voorgenomen-huwelijk-of-geregistreerd-partnerschap-melden.md) (UPL nr. 185) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | voltrekt, ontvangt kennisgeving *toewijzing* | Voltrekken huwelijk | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 63; art. 44) |
| [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Voltrekken huwelijk | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 63) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Utrecht Trouwen in Utrecht](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwen-in-utrecht.md) | Gemeente Utrecht: Trouwen |
| [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Utrecht Trouwlocaties](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-trouwlocaties-in-utrecht.md) | Gemeente Utrecht: Trouwlocaties |
| [HUP BRP: Huwelijk en geregistreerd partnerschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-huwelijkgeregistreerd-partnerschap.md) | HUP BRP: Huwelijk en geregistreerd partnerschap |
| [Utrecht Voorgenomen huwelijk melden](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voorgenomen-huwelijk-of-geregistreerd-partnerschap-melden.md) | Gemeente Utrecht: Melden voorgenomen huwelijk |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
