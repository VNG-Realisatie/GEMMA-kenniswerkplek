---
id: afgeven-verklaring-omtrent-het-gedrag
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Afgeven verklaring omtrent het gedrag
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ontvangen en onderzoeken van een aanvraag voor een verklaring omtrent het gedrag en het afgeven of weigeren ervan, door gemeente en minister.
match:
  gemma: geen
procesniveau: levensloopproces
afnemer: extern
bronnen:
- 2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-besluit-justitiele-en-strafvorderlijke-gegevens-bwbr0016544
- 2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog
---

# Afgeven verklaring omtrent het gedrag

<!-- Gegenereerd door tools/render.py uit de beoordeling afgeven-verklaring-omtrent-het-gedrag.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het ontvangen en onderzoeken van een aanvraag voor een verklaring omtrent het gedrag en het afgeven of weigeren ervan, door gemeente en minister.

### Beschrijving

In het Europese deel van Nederland ontvangt de burgemeester de aanvraag van een natuurlijk persoon die als ingezetene in zijn gemeente staat, onderzoekt hij de volledigheid van de gegevens, verschaft hij zich zekerheid over de identiteit en zendt hij de aanvraag terstond door aan de minister; de gemeente kan een vergoeding verlangen en is de minister een vergoeding verschuldigd (Wet justitiële en strafvorderlijke gegevens art. 30, 39).

Het is een keten in het orkestratiemodel: de minister van Justitie en Veiligheid, in de praktijk Justis, onderzoekt de justitiële gegevens en politiegegevens, neemt de aanvraag zo nodig niet in behandeling, weigert of geeft af, en beslist binnen vier weken (art. 34 tot en met 37; Utrecht). Een aanvraag van een rechtspersoon, van wie niet als inwoner in de BRP staat ingeschreven of die een werkgever rechtstreeks bij Justis doet, loopt buiten de gemeente om (art. 30 lid 1, 31; Utrecht).

Het deel van de gemeente is het bedrijfsproces Behandelen aanvraag verklaring omtrent het gedrag; het deel van de minister staat alleen in deze beschrijving.

### Naamkeuze

Infinitief met object in GEMMA-volgorde, naar de afgifte in de wet (art. 28, 37): het proces omvat de levensloop van de verklaring waarbij gemeente en minister handelen, van aanvraag tot afgifte of weigering. Beheren is niet gekozen: de verklaring wordt niet bijgehouden en heeft geen latere gebeurtenissen.

## Plaats in het model

### Typering

Bedrijfsproces, niveau levensloopproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (3 toetskenmerken ja).

### Plaats in de indelingen

- **Procesniveau**: levensloopproces.
- **Procesindeling naar kernobject, omvat**: [Behandelen aanvraag verklaring omtrent het gedrag](behandelen-aanvraag-verklaring-omtrent-het-gedrag.md).
- **Beleidsdomeinindeling**: beleidsdomein Burgerzaken, taakveld 0 Bestuur en Ondersteuning (van het kernobject).
- **Kernobject**: [Verklaring omtrent het gedrag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-omtrent-het-gedrag.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Besluit justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-justitiele-en-strafvorderlijke-gegevens-bwbr0016544.md) |
| **procesniveau**: levensloopproces, kernobject [Verklaring omtrent het gedrag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-omtrent-het-gedrag.md) | Omvat de levensloop van de verklaring: aanvraag, ontvangst, onderzoek, afgifte of weigering (Wet justitiële en strafvorderlijke gegevens art. 30 tot en met 37). [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Ketenpartner](../../../rollen/ketenpartner.md). [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Besluit justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-justitiele-en-strafvorderlijke-gegevens-bwbr0016544.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de aanvraag om afgifte van de verklaring, aan de balie of online (Wet justitiële en strafvorderlijke gegevens art. 30; Utrecht). [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, standaard. [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Besluit justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-justitiele-en-strafvorderlijke-gegevens-bwbr0016544.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Afgeven verklaring omtrent het gedrag | ontvangt de aanvraag voor, onderzoekt en geeft af *toegang (registreren)* | [Verklaring omtrent het gedrag](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/verklaring-omtrent-het-gedrag.md) | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 30, 35, 37) |
| Afgeven verklaring omtrent het gedrag | toetst de inschrijving in de basisregistratie personen *toegang (raadplegen)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 30 lid 1) |
| Afgeven verklaring omtrent het gedrag | omvat *aggregatie* | [Behandelen aanvraag verklaring omtrent het gedrag](behandelen-aanvraag-verklaring-omtrent-het-gedrag.md) | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 30, 39) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Ketenpartner](../../../rollen/ketenpartner.md) | onderzoekt het gedrag en beslist over de afgifte *toewijzing* | Afgeven verklaring omtrent het gedrag | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) (art. 30, 36, 37; Utrecht regel 59) |
| [Wet justitiële en strafvorderlijke gegevens](../../../../motivatie/beleidskaders/rijksregelgeving/wet-justitiele-en-strafvorderlijke-gegevens.md) | is grondslag voor *associatie (gericht)* | Afgeven verklaring omtrent het gedrag | [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 28-39) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) | Wet justitiële en strafvorderlijke gegevens |
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Besluit justitiële en strafvorderlijke gegevens](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-justitiele-en-strafvorderlijke-gegevens-bwbr0016544.md) | Besluit justitiële en strafvorderlijke gegevens |
| [Utrecht VOG aanvragen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) | Gemeente Utrecht: Verklaring omtrent het gedrag (VOG) aanvragen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor de verklaring omtrent het gedrag. Nieuw voor GEMMA.

### Besluiten redacteur

- 2026-10-08: Orkestratie (IK 27): de minister is verantwoordelijk voor de verklaring, de gemeente voert de ontvangst en het onderzoek van de aanvraag voor hem uit (Wet justitiële en strafvorderlijke gegevens art. 30, 35-37). Geen bedrijfsinteractie; blijft het levensloopproces van Verklaring omtrent het gedrag, met het deel van de minister in de beschrijving, en aggregeert het bedrijfsproces Behandelen aanvraag verklaring omtrent het gedrag. *Zekerheid: kennis.*
