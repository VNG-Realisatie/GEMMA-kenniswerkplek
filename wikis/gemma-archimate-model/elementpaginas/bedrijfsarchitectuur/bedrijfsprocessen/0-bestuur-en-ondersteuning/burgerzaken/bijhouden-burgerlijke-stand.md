---
id: bijhouden-burgerlijke-stand
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Bijhouden burgerlijke stand
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het opmaken en bijhouden van de akten van de burgerlijke stand in de registers van de gemeente, van opmaken tot latere vermelding en afgifte.
match:
  gemma: geen
procesniveau: levensloopproces
afnemer: extern
synoniemen:
- Houden van de registers van de burgerlijke stand (wet)
bronnen:
- 2026-rvig-hup-algemeen
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2026-rvig-hup-vaststelling-ouderschap
- 2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen
---

# Bijhouden burgerlijke stand

<!-- Gegenereerd door tools/render.py uit de beoordeling bijhouden-burgerlijke-stand.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het opmaken en bijhouden van de akten van de burgerlijke stand in de registers van de gemeente, van opmaken tot latere vermelding en afgifte.

### Beschrijving

De ambtenaar van de burgerlijke stand maakt de akten op van geboorte, erkenning, naamskeuze, huwelijk, geregistreerd partnerschap, omzetting en overlijden, schrijft rechterlijke uitspraken en buitenlandse akten in en voegt latere vermeldingen toe, zoals een naamswijziging, adoptie, geslachtswijziging of echtscheiding (BW 1 art. 16a, 18, 20). Hij weigert een akte bij ongenoegzame bescheiden of strijd met de openbare orde; de belanghebbende kan dan de rechtbank verzoeken (art. 18c, 27).

De registers worden aan het eind van het jaar afgesloten; dubbelen en latere vermeldingen gaan naar de centrale bewaarplaats van de minister (Besluit burgerlijke stand art. 6, 7, 31). Een akte is een brondocument voor de BRP: de gemeente verwerkt haar in Bijhouden persoonsgegevens (HUP Algemeen).

De bedrijfsprocessen leveren elk een akte, latere vermelding of afschrift, en daarmee de diensten van de burgerlijke stand uit de UPL. Burgemeester en wethouders wijzen de ambtenaren aan en zorgen voor de voorzieningen (BW 1 art. 16, 16d; Besluit burgerlijke stand art. 2-4).

### Synoniemen

| Synoniem | Context |
|---|---|
| Houden van de registers van de burgerlijke stand | wet |

### Naamkeuze

Infinitief met object in GEMMA-volgorde, naar het bedrijfsproces Bijhouden persoonsgegevens; de wet spreekt van het houden van de registers (Besluit burgerlijke stand art. 5), wat een synoniem is.

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Inschrijven ontbinding huwelijk of partnerschap](inschrijven-ontbinding-huwelijk-of-partnerschap.md), [Opmaken akte levenloos geboren kind](opmaken-akte-levenloos-geboren-kind.md), [Opmaken akte van erkenning](opmaken-akte-van-erkenning.md), [Opmaken akte van naamskeuze](opmaken-akte-van-naamskeuze.md), [Opmaken akte van overlijden](opmaken-akte-van-overlijden.md), [Opmaken geboorteakte](opmaken-geboorteakte.md), [Registreren partnerschap](registreren-partnerschap.md), [Toevoegen latere vermelding](toevoegen-latere-vermelding.md), [Verstrekken uittreksels en verklaringen burgerlijke stand](verstrekken-uittreksels-en-verklaringen-burgerlijke-stand.md), [Voltrekken huwelijk](voltrekken-huwelijk.md), [Wijzigen geslachtsvermelding](wijzigen-geslachtsvermelding.md).
- **Beleidsdomeinindeling**: beleidsdomein Burgerzaken, taakveld 0 Bestuur en Ondersteuning (van het kernobject).
- **Kernobject**: [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md).
- **Functie-indeling naar domein, bediend door**: [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [HUP BRP Algemeen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-algemeen.md) |
| **procesniveau**: levensloopproces, kernobject [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | Omvat de levensloop van de akte: opmaken, latere vermeldingen, aanvulling of verbetering, afsluiten en overbrengen van de registers (BW 1 art. 18, 20, 24; Besluit burgerlijke stand art. 6, 7, 31). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md). [HUP BRP Algemeen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-algemeen.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een aangifte (geboorte, overlijden), een verklaring of kennisgeving (erkenning, naamskeuze, voornemen te trouwen) of een rechterlijke uitspraak of besluit (BW 1 art. 19e, 19h, 44, 203, 20). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [HUP BRP Algemeen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-algemeen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Bijhouden burgerlijke stand | maakt op en houdt bij *toegang (registreren)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 16a, 18, 20) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Opmaken akte van overlijden](opmaken-akte-van-overlijden.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19f) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Verstrekken uittreksels en verklaringen burgerlijke stand](verstrekken-uittreksels-en-verklaringen-burgerlijke-stand.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (BW 1 art. 23; Besluit art. 26) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Overlijden](../../../gebeurtenissen/overlijden.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19f, 19h) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Opmaken geboorteakte](opmaken-geboorteakte.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19, 19e) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Opmaken akte levenloos geboren kind](opmaken-akte-levenloos-geboren-kind.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19i) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Opmaken akte van erkenning](opmaken-akte-van-erkenning.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 203) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Toevoegen latere vermelding](toevoegen-latere-vermelding.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 20) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Geboorte](../../../gebeurtenissen/geboorte.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19e) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Levenloze geboorte](../../../gebeurtenissen/levenloze-geboorte.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19i) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Adoptie](../../../gebeurtenissen/adoptie.md) | [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (art. 53) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Ontkenning ouderschap](../../../gebeurtenissen/ontkenning-ouderschap.md) | [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (art. 49-52) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Vaststelling ouderschap](../../../gebeurtenissen/vaststelling-ouderschap.md) | [HUP BRP: Vaststelling ouderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) (inleiding) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Opmaken akte van naamskeuze](opmaken-akte-van-naamskeuze.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 5) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Wijzigen geslachtsvermelding](wijzigen-geslachtsvermelding.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 28b) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Naamswijziging](../../../gebeurtenissen/naamswijziging.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Voornaam of achternaam veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) (art. 4, 7) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Voltrekken huwelijk](voltrekken-huwelijk.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 63) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Registreren partnerschap](registreren-partnerschap.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80a, 80g) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Inschrijven ontbinding huwelijk of partnerschap](inschrijven-ontbinding-huwelijk-of-partnerschap.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80c, 163) |
| Bijhouden burgerlijke stand | omvat *aggregatie* | [Ontbinding huwelijk of partnerschap](../../../gebeurtenissen/ontbinding-huwelijk-of-partnerschap.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 80c, 163) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | houdt de registers bij *toewijzing* | Bijhouden burgerlijke stand | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (BW 1 art. 16a; Besluit art. 5) |
| [Besluit burgerlijke stand 1994](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-burgerlijke-stand-1994.md) | is grondslag voor *associatie (gericht)* | Bijhouden burgerlijke stand | [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) (art. 5-7, 26) |
| [Burgerlijk Wetboek Boek 1](../../../../motivatie/beleidskaders/rijksregelgeving/burgerlijk-wetboek-boek-1.md) | is grondslag voor *associatie (gericht)* | Bijhouden burgerlijke stand | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 16a, 18) |
| [Burgerlijke stand diensten](../../../bedrijfsfuncties/publieksdiensten/burgerlijke-stand-diensten.md) | bedient *bediening* | Bijhouden burgerlijke stand | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (BW 1 art. 16a; UPL taakveld 0.2) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP BRP Algemeen](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-algemeen.md) | HUP BRP: Algemeen |
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [HUP BRP: Vaststelling ouderschap](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vaststelling-ouderschap.md) | HUP BRP: Vaststelling ouderschap |
| [Utrecht Voornaam of achternaam veranderen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-voornaam-of-achternaam-veranderen.md) | Gemeente Utrecht: Voornaam of achternaam veranderen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor de burgerlijke stand; de functie Burgerlijke stand diensten bedient het, en het generieke proces Behandelen aangifte of melding is het patroon voor de bedrijfsprocessen op aangifte.
