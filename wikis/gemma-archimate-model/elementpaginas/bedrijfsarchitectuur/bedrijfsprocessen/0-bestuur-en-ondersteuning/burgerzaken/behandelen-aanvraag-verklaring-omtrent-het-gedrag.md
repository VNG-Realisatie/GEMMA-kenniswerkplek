---
id: behandelen-aanvraag-verklaring-omtrent-het-gedrag
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen aanvraag verklaring omtrent het gedrag
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het in ontvangst nemen van een VOG-aanvraag, het controleren van de volledigheid en de identiteit en het doorzenden ervan naar de minister.
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Doorzenden aanvraag verklaring omtrent het gedrag (wet)
bronnen:
- 2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194
- 2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog
- 2026-vng-gemma-impact-ketensamenwerking
- 2025-vng-upl-producten-en-diensten-extern
---

# Behandelen aanvraag verklaring omtrent het gedrag

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-aanvraag-verklaring-omtrent-het-gedrag.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het in ontvangst nemen van een VOG-aanvraag, het controleren van de volledigheid en de identiteit en het doorzenden ervan naar de minister.

### Beschrijving

De aanvrager die als ingezetene in de gemeente staat, dient de aanvraag van een natuurlijk persoon in bij de burgemeester, online met een scan van het formulier van de werkgever of aan de balie op afspraak met dat formulier en een identiteitsbewijs, en betaalt direct (Wet justitiële en strafvorderlijke gegevens art. 30, 32, 33; Utrecht). De burgemeester onderzoekt de volledigheid van de gegevens, verschaft zich zekerheid over de identiteit en zendt de aanvraag terstond door aan de minister; de gemeente is de minister een vergoeding verschuldigd voor aanvragen die bij haar zijn ingediend (art. 30 lid 2 en 4, 39).

De minister van Justitie en Veiligheid, in de praktijk Justis, onderzoekt het gedrag en beslist binnen vier weken en stuurt de aanvrager bericht (art. 35 tot en met 37; Utrecht); de gemeente reikt de verklaring niet uit. Een aanvraag van een rechtspersoon, van wie niet als inwoner in de BRP staat ingeschreven, of die de werkgever rechtstreeks bij Justis doet, loopt buiten de gemeente om (art. 30 lid 1, 31; Utrecht).

Het is het deel dat de gemeente voor de minister uitvoert, binnen het levensloopproces Afgeven verklaring omtrent het gedrag.

### Synoniemen

| Synoniem | Context |
|---|---|
| Doorzenden aanvraag verklaring omtrent het gedrag | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Afgeven verklaring omtrent het gedrag](afgeven-verklaring-omtrent-het-gedrag.md).
- **Kernobject**: [Verklaring omtrent het gedrag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-omtrent-het-gedrag.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Leveren dienst aan derden*. De gemeente voert de ontvangst en het onderzoek van de aanvraag uit voor de minister, die over de verklaring beslist (art. 30, 37): een dienst aan een ketenpartner, zoals GEMMA Leveren dienst aan derden beschrijft ('een (deel)proces dat aan de gemeente is uitbesteed').
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Aanvrager van de verklaring omtrent het gedrag](../../../rollen/aanvrager-van-de-verklaring-omtrent-het-gedrag.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Verklaring omtrent het gedrag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-omtrent-het-gedrag.md), [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de aanvraag, online of aan de balie op afspraak (Wet justitiële en strafvorderlijke gegevens art. 30; Utrecht). [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de ontvangen, gecontroleerde en doorgezonden aanvraag (Wet justitiële en strafvorderlijke gegevens art. 30 lid 2 en 4). [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke aanvraag. [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wet justitiële en strafvorderlijke gegevens art. 30 tot en met 33 en 39 (indiening bij de burgemeester, volledigheid en identiteit, doorzending, vergoeding). [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Afgeven verklaring omtrent het gedrag](afgeven-verklaring-omtrent-het-gedrag.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de aanvraag tot de doorgezonden aanvraag, het deel van de gemeente. [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Verklaring omtrent gedrag aanvragen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-omtrent-gedrag-aanvragen.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen aanvraag verklaring omtrent het gedrag | ontvangt de aanvraag voor *toegang (bijwerken)* | [Verklaring omtrent het gedrag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-omtrent-het-gedrag.md) | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 30, 32) |
| Behandelen aanvraag verklaring omtrent het gedrag | toetst de inschrijving in de basisregistratie personen *toegang (raadplegen)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 30 lid 1) |
| Behandelen aanvraag verklaring omtrent het gedrag | realiseert *realisatie* | [Verklaring omtrent gedrag aanvragen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-omtrent-gedrag-aanvragen.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) (UPL nr. 434; Utrecht regel 21-55) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aanvrager van de verklaring omtrent het gedrag](../../../rollen/aanvrager-van-de-verklaring-omtrent-het-gedrag.md) | dient de aanvraag in *toewijzing* | Behandelen aanvraag verklaring omtrent het gedrag | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) (art. 30, 33; Utrecht regel 37-53) |
| [Afgeven verklaring omtrent het gedrag](afgeven-verklaring-omtrent-het-gedrag.md) | omvat *aggregatie* | Behandelen aanvraag verklaring omtrent het gedrag | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 30, 39) |
| [Wet justitiële en strafvorderlijke gegevens](../../../../motivatie/beleidskaders/rijksregelgeving/wet-justitiele-en-strafvorderlijke-gegevens.md) | is grondslag voor *associatie (gericht)* | Behandelen aanvraag verklaring omtrent het gedrag | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 30, 39) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) | Wet justitiële en strafvorderlijke gegevens |
| [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) | Gemeente Utrecht: Verklaring omtrent het gedrag (VOG) aanvragen |
| [GEMMA Procesarchitectuur Impact van ketensamenwerking](../../../../../modellen/gemma/bronduidingen/overig/2026-vng-gemma-impact-ketensamenwerking.md) | GEMMA Procesarchitectuur Impact van ketensamenwerking |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA.
