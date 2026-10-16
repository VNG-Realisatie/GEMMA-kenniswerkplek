---
id: behandelen-aanvraag-omwisseling-buitenlands-rijbewijs
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Behandelen aanvraag omwisseling buitenlands rijbewijs
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het in ontvangst nemen van een aanvraag om een buitenlands rijbewijs om te wisselen en het doorgeleiden ervan naar de RDW, die beslist.
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Omwisselen buitenlands rijbewijs (beleid)
bronnen:
- 2025-vng-upl-producten-en-diensten-extern
- 2026-rijk-reglement-rijbewijzen-bwbr0008074
- 2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen
- 2026-rijk-wegenverkeerswet-1994-bwbr0006622
---

# Behandelen aanvraag omwisseling buitenlands rijbewijs

<!-- Gegenereerd door tools/render.py uit de beoordeling behandelen-aanvraag-omwisseling-buitenlands-rijbewijs.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het in ontvangst nemen van een aanvraag om een buitenlands rijbewijs om te wisselen en het doorgeleiden ervan naar de RDW, die beslist.

### Beschrijving

Wie in Nederland woont, dient de aanvraag in bij de burgemeester van de gemeente van inschrijving en levert het buitenlandse rijbewijs in, met een paspoort, identiteitskaart of verblijfsvergunning, een pasfoto, bij een rijbewijs van buiten de EU en EER een gezondheidsverklaring van het CBR en bij de 30%-regeling de brief van de Belastingdienst (Reglement rijbewijzen art. 27, 33; Utrecht). De burgemeester geleidt de aanvraag terstond door naar de RDW, die het rijbewijs afgeeft; de gemeente stuurt het buitenlandse rijbewijs met de aanvraag naar de RDW, die het terugstuurt naar het land van afgifte (Reglement rijbewijzen art. 28, 105 lid 2, 109; Utrecht).

Of omwisselen kan en wat daarvoor nodig is, bepaalt de RDW; voor een rijbewijs uit een andere lidstaat van de EU of de EER gelden de vereisten van artikel 45, en kan niet worden omgewisseld, dan volgt rijexamen bij het CBR (Reglement rijbewijzen art. 45; Utrecht). De RDW laat binnen vier weken weten of ze akkoord is; de aanvrager maakt pas daarna de afspraak om het Nederlandse rijbewijs te laten uitreiken (Utrecht, zie Uitreiken rijbewijs). De omwisseling is een deel van de afgifte, niet iets wat de gemeente zelf beslist.

### Deelprocessen

1. **Aanvraag innemen**: De burgemeester neemt de aanvraag en het buitenlandse rijbewijs in ontvangst. [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) (art. 27, 28, 109)
2. **Doorgeleiden naar de RDW**: De burgemeester geleidt de aanvraag terstond door; de RDW beslist en geeft het rijbewijs af. [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) (Reglement rijbewijzen art. 105, 109; Utrecht)
3. **Uitreiken**: Na het akkoord van de RDW maakt de aanvrager een afspraak en haalt hij het Nederlandse rijbewijs op. [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md), [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (Utrecht; Wegenverkeerswet 1994 art. 119 lid 2)

### Synoniemen

| Synoniem | Context |
|---|---|
| Omwisselen buitenlands rijbewijs | beleid |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren rijbewijzen](beheren-rijbewijzen.md).
- **Kernobject**: [Rijbewijs](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aanvraag product*. Een aanvraag voor een product dat de gemeente na een toets op identiteit en voorwaarden ontvangt; hier beslist de RDW.
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: per keer doorlopen. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, met [Houder van het rijbewijs](../../../rollen/houder-van-het-rijbewijs.md). |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, met [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md). |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de aanvraag, op afspraak aan de balie (Reglement rijbewijzen art. 27; Utrecht). [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de ontvangen aanvraag met het ingeleverde buitenlandse rijbewijs, doorgeleid naar de RDW voor de beslissing (Reglement rijbewijzen art. 28, 109; Utrecht). [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke aanvraag. [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, reglement rijbewijzen art. 28, 45 en 105 tot en met 109: aanvraag via de burgemeester, afgifte door de RDW, vereisten voor een rijbewijs uit een andere lidstaat, inname van het buitenlandse rijbewijs. [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, met [Beheren rijbewijzen](beheren-rijbewijzen.md). |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de aanvraag aan de balie tot het afgegeven of geweigerde rijbewijs. [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, met [Rijbewijs buitenlands omwisseling](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs-buitenlands-omwisseling.md). |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, specialisatie van Behandelen aanvraag rijbewijs met een eigen afgever, de RDW, en een eigen eis, het inleveren van het buitenlandse rijbewijs (Reglement rijbewijzen art. 28, 105, 109). [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Behandelen aanvraag omwisseling buitenlands rijbewijs | is een *specialisatie* | [Behandelen aanvraag rijbewijs](behandelen-aanvraag-rijbewijs.md) | [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) (art. 28, 45, 105 lid 2) |
| Behandelen aanvraag omwisseling buitenlands rijbewijs | raadpleegt de basisregistratie personen *toegang (raadplegen)* | [Ingeschreven persoon](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/ingeschreven-persoon.md) | [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) (art. 33 lid 2) |
| Behandelen aanvraag omwisseling buitenlands rijbewijs | realiseert *realisatie* | [Rijbewijs buitenlands omwisseling](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs-buitenlands-omwisseling.md) | [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md), [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) (UPL nr. 361; Utrecht regel 17, 55) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren rijbewijzen](beheren-rijbewijzen.md) | omvat *aggregatie* | Behandelen aanvraag omwisseling buitenlands rijbewijs | [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) (art. 28, 45, 105 lid 2, 109) |
| [Houder van het rijbewijs](../../../rollen/houder-van-het-rijbewijs.md) | vraagt aan en levert het buitenlandse rijbewijs in *toewijzing* | Behandelen aanvraag omwisseling buitenlands rijbewijs | [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) (art. 27, 109; Utrecht regel 55) |
| [Reglement rijbewijzen](../../../../motivatie/beleidskaders/rijksregelgeving/reglement-rijbewijzen.md) | is grondslag voor *associatie (gericht)* | Behandelen aanvraag omwisseling buitenlands rijbewijs | [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) (art. 28, 45, 105, 109) |
| [Wegenverkeerswet 1994](../../../../motivatie/beleidskaders/rijksregelgeving/wegenverkeerswet-1994.md) | is grondslag voor *associatie (gericht)* | Behandelen aanvraag omwisseling buitenlands rijbewijs | [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (art. 116 lid 1, 123 lid 1 onder b) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [UPL-lijst extern](../../../../../modellen/upl/bronduidingen/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Reglement rijbewijzen](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) | Reglement rijbewijzen |
| [Utrecht Rijbewijs buitenland omwisselen](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-rijbewijs-buitenland-omwisselen.md) | Gemeente Utrecht: Rijbewijs buitenland omwisselen |
| [Wegenverkeerswet 1994](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) | Wegenverkeerswet 1994 |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA. Het specialiseert het generieke proces Behandelen aanvraag product.
