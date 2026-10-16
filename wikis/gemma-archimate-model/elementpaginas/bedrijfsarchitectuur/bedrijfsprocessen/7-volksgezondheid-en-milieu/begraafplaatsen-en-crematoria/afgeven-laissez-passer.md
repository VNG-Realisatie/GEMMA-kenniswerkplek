---
id: afgeven-laissez-passer
type: bedrijfsproces
archimate_type: business-process
status: review
naam: Afgeven laissez-passer
onderwerpen:
- lijkbezorging
taakveld: 7 Volksgezondheid en Milieu
beleidsdomein: Begraafplaatsen en crematoria
definitie: Het afgeven van het laissez-passer voor lijken voor vervoer van een stoffelijk overschot naar een verdragsstaat.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
bronnen:
- 2026-rijk-besluit-op-de-lijkbezorging-wettekst
- 2025-vng-upl-producten-en-diensten-extern
---

# Afgeven laissez-passer

<!-- Gegenereerd door tools/render.py uit de beoordeling afgeven-laissez-passer.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het afgeven van het laissez-passer voor lijken voor vervoer van een stoffelijk overschot naar een verdragsstaat.

### Beschrijving

De burgemeester van de gemeente waar de akte van overlijden is ingeschreven, geeft het laissez-passer af voor vervoer naar een staat die partij is bij de Overeenkomst van Straatsburg; voor vervoer over land naar België of Luxemburg volstaat het verlof tot begraving of crematie (Besluit op de lijkbezorging art. 11 lid 1, 3). Beslisser is de burgemeester.

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Behandelen vergunningaanvragen lijkbezorging](behandelen-vergunningaanvragen-lijkbezorging.md), [Toestaan lijkbezorging](toestaan-lijkbezorging.md).
- **Kernobject**: [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 7 Volksgezondheid en Milieu, Begraafplaatsen en crematoria.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Vergunning](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/vergunning.md), [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, vervoer van een stoffelijk overschot naar een staat die partij is bij de Overeenkomst van Straatsburg (Besluit op de lijkbezorging art. 11 lid 1). [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, een laissez-passer voor lijken (Besluit op de lijkbezorging art. 11 lid 1). [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, bij elk vervoer naar een verdragsstaat buiten België en Luxemburg (Besluit op de lijkbezorging art. 11 lid 1, 3). [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, besluit op de lijkbezorging art. 11: bevoegde burgemeester, verdragsstaten, uitzondering België en Luxemburg, overleggen aan de douane. [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Toestaan lijkbezorging](toestaan-lijkbezorging.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van het verzoek voor vervoer naar een verdragsstaat tot het afgegeven laissez-passer. [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, de burgemeester geeft het laissez-passer af (Besluit op de lijkbezorging art. 11 lid 1). [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Vervoersdocumenten stoffelijk overschot](../../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vervoersdocumenten-stoffelijk-overschot.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Afgeven laissez-passer | geeft af *toegang (registreren)* | [Vergunning](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/besluitvorming/vergunning.md) | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) (art. 11 lid 1) |
| Afgeven laissez-passer | betreft *toegang (bijwerken)* | [Stoffelijk overschot](../../../bedrijfsobjecten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stoffelijk-overschot.md) | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) (art. 11 lid 1) |
| Afgeven laissez-passer | realiseert *realisatie* | [Vervoersdocumenten stoffelijk overschot](../../../diensten/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/vervoersdocumenten-stoffelijk-overschot.md) | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) (Besluit op de lijkbezorging art. 11; UPL nr. 445) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen vergunningaanvragen lijkbezorging](behandelen-vergunningaanvragen-lijkbezorging.md) | omvat *aggregatie* | Afgeven laissez-passer | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) (Besluit op de lijkbezorging art. 11) |
| [Beslisser](../../../rollen/beslisser.md) | geeft af *toewijzing* | Afgeven laissez-passer | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) (art. 11 lid 1) |
| [Besluit op de lijkbezorging](../../../../motivatie/beleidskaders/rijksregelgeving/besluit-op-de-lijkbezorging.md) | is grondslag voor *associatie (gericht)* | Afgeven laissez-passer | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) (art. 11) |
| [Toestaan lijkbezorging](toestaan-lijkbezorging.md) | omvat *aggregatie* | Afgeven laissez-passer | [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) (Besluit op de lijkbezorging art. 11) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Besluit op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-besluit-op-de-lijkbezorging-wettekst.md) | Besluit op de lijkbezorging |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen element voor dit begrip; nieuw voor GEMMA.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.
