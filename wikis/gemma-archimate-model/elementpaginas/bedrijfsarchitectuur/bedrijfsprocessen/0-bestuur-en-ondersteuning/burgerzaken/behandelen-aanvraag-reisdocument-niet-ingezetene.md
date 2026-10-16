---
id: behandelen-aanvraag-reisdocument-niet-ingezetene
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen aanvraag reisdocument niet-ingezetene
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het in ontvangst nemen en beoordelen van een aanvraag voor een reisdocument van iemand die niet als ingezetene in de BRP staat, tot de uitreiking of weigering.
match:
  gemma: geen
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Verstrekken reisdocument aan niet-ingezetene (wet)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-paspoortbesluit-bwbr0044308
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen
---

# Behandelen aanvraag reisdocument niet-ingezetene

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-aanvraag-reisdocument-niet-ingezetene.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het in ontvangst nemen en beoordelen van een aanvraag voor een reisdocument van iemand die niet als ingezetene in de BRP staat, tot de uitreiking of weigering.

### Beschrijving

Alleen de burgemeester van een bij ministeriële regeling aangewezen gemeente is bevoegd aanvragen in ontvangst te nemen en reisdocumenten te verstrekken voor personen die niet als ingezetene in de basisregistratie personen zijn ingeschreven: het nationaal paspoort, de reisdocumenten voor vluchtelingen en voor vreemdelingen en het nooddocument (Paspoortbesluit art. 3.2, 4.2; Paspoortwet art. 2 lid 1 onder a, d, e en g). Het document is hetzelfde Reisdocument als bij een ingezetene; bijzonder zijn de bevoegde gemeente en de aanvrager. Verder volgt de behandeling Behandelen aanvraag reisdocument.

### Deelprocessen

1. **Aanvraag innemen**: Een aangewezen gemeente neemt de aanvraag in ontvangst van wie niet als ingezetene in de basisregistratie personen staat. [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 3.2, 4.2)
2. **Verstrekken of weigeren**: Zoals bij Behandelen aanvraag reisdocument. [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 40, 41, 44)
3. **Uitreiken**: Binnen twee weken na de verstrekking krijgt de aanvrager het document in handen, na vaststelling van zijn identiteit, en levert hij zijn oude Nederlandse reisdocumenten in. Een document dat niet binnen drie maanden is opgehaald, wordt aan het verkeer onttrokken. [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (Paspoortwet art. 32, 42; Paspoortbesluit art. 4.6)

### Synoniemen

| Synoniem | Context |
|---|---|
| Verstrekken reisdocument aan niet-ingezetene | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren reisdocumenten](beheren-reisdocumenten.md).
- **Kernobject**: [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een aanvraag voor een product dat de gemeente na een toets op identiteit en aanspraak verstrekt; GEMMA noemt het paspoort als voorbeeld.
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Beslisser](../../../rollen/beslisser.md), [Houder van het reisdocument](../../../rollen/houder-van-het-reisdocument.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md), [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de aanvraag, op afspraak aan de balie (Paspoortwet art. 27; Utrecht). [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, het uitgereikte reisdocument, na de verstrekking, of de weigering (Paspoortwet art. 1 onder c, d en e, 42). [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke aanvraag. [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, een eigen bevoegdheid voor alleen de aangewezen gemeenten en alleen voor personen die niet als ingezetene in de BRP staan (Paspoortbesluit art. 3.2, 4.2); verder gelden de regels van de Paspoortwet voor de aanvraag (art. 26-41). [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Beheren reisdocumenten](beheren-reisdocumenten.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de aanvraag tot de uitreiking of de weigering. [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) |
| **eigen besluit**: Eindigt het in een besluit van een bevoegd orgaan of een mandataris? | Ja, de verstrekking of de weigering door de burgemeester van de aangewezen gemeente (Paspoortbesluit art. 4.2; Paspoortwet art. 40, 44). [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md), [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Reisdocument niet-ingezetene](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument-niet-ingezetene.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, specialisatie van Behandelen aanvraag reisdocument met een eigen bevoegdheid, een eigen doelgroep en een taak die alleen aangewezen gemeenten uitvoeren (Paspoortbesluit art. 3.2, 4.2). [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen aanvraag reisdocument niet-ingezetene | is een *specialisatie* | [Behandelen aanvraag reisdocument](behandelen-aanvraag-reisdocument.md) | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 3.2, 4.2) |
| Behandelen aanvraag reisdocument niet-ingezetene | verstrekt *toegang (registreren)* | [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md) | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 4.2) |
| Behandelen aanvraag reisdocument niet-ingezetene | stelt identiteit en nationaliteit vast *toegang (raadplegen)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 2.1, 3.2) |
| Behandelen aanvraag reisdocument niet-ingezetene | realiseert *realisatie* | [Reisdocument niet-ingezetene](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument-niet-ingezetene.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (UPL nr. 356, 357; Paspoortbesluit art. 3.2, 4.2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren reisdocumenten](beheren-reisdocumenten.md) | omvat *aggregatie* | Behandelen aanvraag reisdocument niet-ingezetene | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 3.2, 4.2) |
| [Beslisser](../../../rollen/beslisser.md) | verstrekt of weigert *toewijzing* | Behandelen aanvraag reisdocument niet-ingezetene | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 4.2) |
| [Houder van het reisdocument](../../../rollen/houder-van-het-reisdocument.md) | vraagt aan *toewijzing* | Behandelen aanvraag reisdocument niet-ingezetene | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 3.2) |
| [Paspoortbesluit](../../../../motivatie/beleidskaders/rijksregelgeving/paspoortbesluit.md) | is grondslag voor *associatie (gericht)* | Behandelen aanvraag reisdocument niet-ingezetene | [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 3.2, 4.2) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Paspoortbesluit](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) | Paspoortbesluit |
| [Paspoortwet](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [Utrecht Paspoort of identiteitskaart aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md) | Gemeente Utrecht: Paspoort of ID-kaart aanvragen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA. Het specialiseert het generieke proces Behandelen aanvraag product.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../../modellen/gemma/terugmeldingen/procesarchitectuur.md) (kennismodel, opgelost): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-over-gemma.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [2025-vng-upl-producten-en-diensten-intern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-intern.md)). **Opgelost (2026-10-08):** de procesniveaus van het model volgen nu de ladder van GEMMA Online, Proceshiërarchie ([2026-vng-gemma-proceshierarchie](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-proceshierarchie.md), regel 47, 81, 83): wat het model deelproces noemde, is een bedrijfsproces, en een bedrijfsproces realiseert de dienst, zoals het kennismodel zegt. De afwijking bestaat niet meer; de melding wordt niet verstuurd.

### Besluiten redacteur

- 2026-10-07: Eigen deelproces voor de aanvraag van een niet-ingezetene, specialisatie van Behandelen aanvraag reisdocument: bijzonder is niet het document maar de taak, die alleen aangewezen gemeenten uitvoeren (Paspoortbesluit art. 3.2, 4.2). Realiseert de dienst Reisdocument niet-ingezetene. *Zekerheid: logica.*
