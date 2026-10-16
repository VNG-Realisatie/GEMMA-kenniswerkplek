---
id: opmaken-geboorteakte
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Opmaken geboorteakte
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ontvangen van de aangifte van een geboorte en het opmaken van de geboorteakte.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-utrecht-burgerzaken-geboorteaangifte-doen
- 2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rvig-hup-geboorte
---

# Opmaken geboorteakte

<!-- Gegenereerd door tools/render.py uit de beoordeling opmaken-geboorteakte.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het ontvangen van de aangifte van een geboorte en het opmaken van de geboorteakte.

### Beschrijving

De aangever doet binnen drie dagen aangifte in de gemeente van geboorte; verplicht is de vader of de moeder uit wie het kind niet is geboren, anders wie bij de bevalling aanwezig was of het hoofd van de instelling. Elektronisch kan alleen de moeder of de andere ouder; de ambtenaar stelt de identiteit vast en controleert de verklaring van arts of verloskundige (BW 1 art. 19e; Besluit burgerlijke stand art. 27; Utrecht). Een te late aangifte meldt hij aan het openbaar ministerie (art. 19e lid 7).

De ambtenaar weigert ongepaste voornamen (BW 1 art. 4). Bij de aangifte kan ook een erkenning of een naamskeuze worden opgenomen. De geboorteakte gaat naar de woongemeente van de moeder, die het kind in de BRP inschrijft (HUP Geboorte; Utrecht).

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md).
- **Kernobject**: [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een aangifte van een gebeurtenis van de burgerlijke stand die de gemeente verwerkt (BW 1 art. 19e).
- **Gestart door gebeurtenis**: [Geboorte](../../../gebeurtenissen/geboorte.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Aangever](../../../rollen/aangever.md), [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md), [Ouder](../../../rollen/ouder.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, met [Geboorte](../../../gebeurtenissen/geboorte.md). |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de geboorteakte; de aangever krijgt een uittreksel (Utrecht). [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elk geval dat zich voordoet. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, BW 1 art. 4, 5, 19-19e; Besluit burgerlijke stand art. 27, 43-47. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de aangifte van de geboorte tot de akte. [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Geboorteaangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/geboorteaangifte.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Opmaken geboorteakte | maakt geboorteakte op *toegang (registreren)* | [Akte van de burgerlijke stand](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/akte-van-de-burgerlijke-stand.md) | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19) |
| Opmaken geboorteakte | realiseert *realisatie* | [Geboorteaangifte](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/geboorteaangifte.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (UPL nr. 136) |
| Opmaken geboorteakte | zendt geboorteakte aan *stroom* | [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | [HUP BRP: Geboorte](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (HUP Geboorte inleiding; Utrecht Na de aangifte) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangever](../../../rollen/aangever.md) | doet aangifte *toewijzing* | Opmaken geboorteakte | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19e) |
| [Ambtenaar van de burgerlijke stand](../../../rollen/ambtenaar-van-de-burgerlijke-stand.md) | maakt akte op *toewijzing* | Opmaken geboorteakte | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19) |
| [Bijhouden burgerlijke stand](bijhouden-burgerlijke-stand.md) | omvat *aggregatie* | Opmaken geboorteakte | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19, 19e) |
| [Geboorte](../../../gebeurtenissen/geboorte.md) | leidt tot *triggering* | Opmaken geboorteakte | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (art. 19e) |
| [Ouder](../../../rollen/ouder.md) | doet aangifte *toewijzing* | Opmaken geboorteakte | [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) (art. 19e) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [BW boek 1](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [Utrecht Geboorteaangifte doen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-geboorteaangifte-doen.md) | Gemeente Utrecht: Geboorteaangifte |
| [Besluit burgerlijke stand 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-burgerlijke-stand-1994-bwbr0006493.md) | Besluit burgerlijke stand 1994 |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [HUP BRP: Geboorte](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-geboorte.md) | HUP BRP: Geboorte |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
