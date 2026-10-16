---
id: stellen-andere-termijn
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Stellen andere termijn
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het toestaan dat een overledene eerder dan 36 uur of later dan de zesde werkdag na het overlijden wordt begraven of gecremeerd.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Andere termijn stellen (wet)
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rvo-aangifte-en-akte-van-overlijden
---

# Stellen andere termijn

<!-- Gegenereerd door tools/render.py uit de beoordeling stellen-andere-termijn.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het toestaan dat een overledene eerder dan 36 uur of later dan de zesde werkdag na het overlijden wordt begraven of gecremeerd.

### Beschrijving

Begraving of crematie geschiedt niet eerder dan 36 uur en uiterlijk op de zesde werkdag na het overlijden (Wet op de lijkbezorging art. 16). Na een arts te hebben gehoord kan de burgemeester van de gemeente waar het stoffelijk overschot zich bevindt een andere termijn stellen; binnen 36 uur alleen in overeenstemming met de officier van justitie (art. 17 lid 1). Tegen het besluit staat binnen 24 uur beroep open bij de commissaris van de Koning (art. 17 lid 2). De nabestaanden vragen de vergunning aan bij de gemeente waar de persoon is overleden, meestal via de uitvaartondernemer (RVO).

### Synoniemen

| Synoniem | Context |
|---|---|
| Andere termijn stellen | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Behandelen vergunningaanvragen lijkbezorging](behandelen-vergunningaanvragen-lijkbezorging.md), [Toestaan lijkbezorging](toestaan-lijkbezorging.md).
- **Kernobject**: [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md).
- **Functie-indeling naar domein, bediend door**: [Vergunningenbeheer Publieksdiensten](../../../bedrijfsfuncties/publieksdiensten/vergunningenbeheer-publieksdiensten.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Ketenpartner](../../../rollen/ketenpartner.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md), [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, een aanvraag van de nabestaanden, via de uitvaartondernemer, bij de gemeente waar de persoon is overleden (RVO). [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een vergunning voor begraving of crematie eerder dan 36 uur of later dan de zesde werkdag na het overlijden (art. 16, 17; RVO). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, regelmatig, bijvoorbeeld om religieuze redenen of omdat familie uit het buitenland moet komen (RVO). [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, art. 17: na het horen van een arts; binnen 36 uur alleen in overeenstemming met de officier van justitie; beroep binnen 24 uur bij de commissaris van de Koning. [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Toestaan lijkbezorging](toestaan-lijkbezorging.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de aanvraag tot de vergunning voor een andere termijn. [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, de burgemeester stelt de andere termijn, na een arts te hebben gehoord (art. 17 lid 1). [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Uitvaart vervroegen of uitstellen](../../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvaart-vervroegen-of-uitstellen.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Stellen andere termijn | stelt *toegang (registreren)* | [Beschikking](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/beschikking.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17 lid 1) |
| Stellen andere termijn | betreft *toegang (bijwerken)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17 lid 1) |
| Stellen andere termijn | realiseert *realisatie* | [Uitvaart vervroegen of uitstellen](../../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/uitvaart-vervroegen-of-uitstellen.md) | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) (art. 17; § Uitvaart vervroegen, § Uitvaart uitstellen) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen vergunningaanvragen lijkbezorging](behandelen-vergunningaanvragen-lijkbezorging.md) | omvat *aggregatie* | Stellen andere termijn | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |
| [Beslisser](../../../rollen/beslisser.md) | stelt *toewijzing* | Stellen andere termijn | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17 lid 1) |
| [Ketenpartner](../../../rollen/ketenpartner.md) | stemt in met vervroegen bij *toewijzing* | Stellen andere termijn | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17 lid 1) |
| [Toestaan lijkbezorging](toestaan-lijkbezorging.md) | omvat *aggregatie* | Stellen andere termijn | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |
| [Vergunningenbeheer Publieksdiensten](../../../bedrijfsfuncties/publieksdiensten/vergunningenbeheer-publieksdiensten.md) | bedient *bediening* | Stellen andere termijn | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |
| [Wet op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/wet-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Stellen andere termijn | [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Ondernemersplein Aangifte overlijden](../../../../../onderwerpen/lijkbezorging/bronduidingen/overig/2026-rvo-aangifte-en-akte-van-overlijden.md) | Aangifte en akte van overlijden (Ondernemersplein) |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.

### Besluiten redacteur

- 2026-10-04: Eigen deelproces dat de dienst Uitvaart vervroegen of uitstellen realiseert, niet de functie Lijkbezorging. Herziet het besluit van 2026-10-01. *Zekerheid: logica.*
