---
id: verwerken-vermissing-rijbewijs
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Verwerken vermissing rijbewijs
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ontvangen en vastleggen van de verklaring dat een rijbewijs kwijt of gestolen is, waardoor het rijbewijs ongeldig wordt.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: bedrijfsproces
afnemer: extern
synoniemen:
- Melding van vermissing van het rijbewijs (wet)
bronnen:
- 2026-rijk-wegenverkeerswet-1994-bwbr0006622
- 2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen
- 2026-rijk-reglement-rijbewijzen-bwbr0008074
---

# Verwerken vermissing rijbewijs

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verwerken-vermissing-rijbewijs.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het ontvangen en vastleggen van de verklaring dat een rijbewijs kwijt of gestolen is, waardoor het rijbewijs ongeldig wordt.

### Beschrijving

De houder geeft de vermissing online door aan de RDW met DigiD, waar ze direct wordt geregistreerd, of aan de balie van de gemeente, waar hij de vermissingsverklaring invult bij een nieuwe aanvraag of in een eigen afspraak (Utrecht). Een rijbewijs verliest zijn geldigheid door aangifte van vermissing; wie het terugvindt, levert het in bij degene die het nieuwe rijbewijs afgaf (Wegenverkeerswet 1994 art. 123 lid 1 onder h, 119 lid 4, 120 lid 3).

Bij een vermoeden van misbruik na identiteitsfraude houdt de gemeente het rijbewijs in en vraagt direct een nieuw rijbewijs aan (Utrecht; Wegenverkeerswet 1994 art. 115). Het Reglement rijbewijzen vraagt bij een aanvraag na vermissing een proces-verbaal van een opsporingsambtenaar (art. 39 lid 1), terwijl Utrecht spreekt van een vermissingsverklaring die aan de balie wordt ingevuld; wat formeel geldt, volgt de wet en de verhouding is uit de bronnen niet te halen (verificatie nodig).

### Synoniemen

| Synoniem | Context |
|---|---|
| Melding van vermissing van het rijbewijs | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau bedrijfsproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: bedrijfsproces.
- **Procesindeling naar kernobject, onderdeel van**: [Beheren rijbewijzen](beheren-rijbewijzen.md).
- **Kernobject**: [Rijbewijs](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een melding van een gebeurtenis waardoor het rijbewijs ongeldig wordt; de melder krijgt een afspraak voor een nieuw rijbewijs (Utrecht).
- **Gestart door gebeurtenis**: [Vermissing van het rijbewijs](../../../gebeurtenissen/vermissing-van-het-rijbewijs.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 44 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, vermissing Rijbewijs doorgeven aan de balie (Utrecht); het verlies van geldigheid door aangifte van vermissing staat in de wet (Wegenverkeerswet 1994 art. 123 lid 1 onder h). [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente neemt aan de balie de vermissingsverklaring op en houdt bij vermoeden van misbruik het rijbewijs in (Utrecht; Wegenverkeerswet 1994 art. 115). [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip: een eigen afspraak zonder nieuwe aanvraag (Utrecht). [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per gemelde vermissing doorlopen. [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, de Houder van het rijbewijs geeft de vermissing door, online bij de RDW of aan de balie (Utrecht). [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, werkt het rijbewijs bij: vermist en daarmee ongeldig (Wegenverkeerswet 1994 art. 123 lid 1 onder h; Utrecht). [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de vermissing van het rijbewijs en de melding daarvan (Wegenverkeerswet 1994 art. 123 lid 1 onder h; Utrecht). [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de geregistreerde vermissing: het rijbewijs is niet meer geldig (Utrecht; Wegenverkeerswet 1994 art. 123). [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke gemelde vermissing. [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, wegenverkeerswet 1994 art. 123 lid 1 onder h (verlies van geldigheid door aangifte van vermissing), art. 119 lid 4 en 120 lid 3 (inlevering van een teruggevonden rijbewijs); Reglement rijbewijzen art. 39. [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Reglement rijbewijzen](../../../../bronanalyses/burgerzaken/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) |
| **bijdrage aan groter proces**: Is het een deel van een groter proces: van het levensloopproces van een kernobject, of van een bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Beheren rijbewijzen: het einde van een vermist rijbewijs. [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) |
| **klant tot klant**: Begint het bij een aanleiding van buiten het proces (een verzoek of melding van een klant, een gebeurtenis of een termijn) en loopt het door tot het resultaat voor die klant, zonder dat het de voortzetting is van een ander proces voor hetzelfde geval? | Ja, ja, van de melding van de vermissing tot de registratie. [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst Vermissing of diefstal rijbewijs doorgeven (Utrecht). [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken vermissing rijbewijs | registreert vermissing van *toegang (bijwerken)* | [Rijbewijs](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/rijbewijs.md) | [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (WVW art. 123 lid 1 onder h; Utrecht regel 126-140) |
| Verwerken vermissing rijbewijs | realiseert *realisatie* | [Vermissing of diefstal rijbewijs doorgeven](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/vermissing-of-diefstal-rijbewijs-doorgeven.md) | [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (Utrecht regel 134-140) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren rijbewijzen](beheren-rijbewijzen.md) | omvat *aggregatie* | Verwerken vermissing rijbewijs | [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Reglement rijbewijzen](../../../../bronanalyses/burgerzaken/2026-rijk-reglement-rijbewijzen-bwbr0008074.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (WVW art. 123 lid 1 onder h; Reglement art. 39; Utrecht regel 126-140) |
| [Houder van het rijbewijs](../../../rollen/houder-van-het-rijbewijs.md) | geeft vermissing door *toewijzing* | Verwerken vermissing rijbewijs | [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (Utrecht regel 126-140) |
| [Reglement rijbewijzen](../../../../motivatie/beleidskaders/reglement-rijbewijzen.md) | is grondslag voor *associatie (gericht)* | Verwerken vermissing rijbewijs | [Reglement rijbewijzen](../../../../bronanalyses/burgerzaken/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) (art. 39) |
| [Vermissing van het rijbewijs](../../../gebeurtenissen/vermissing-van-het-rijbewijs.md) | leidt tot *triggering* | Verwerken vermissing rijbewijs | [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md), [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) (WVW art. 123 lid 1 onder h; Utrecht regel 126-140) |
| [Wegenverkeerswet 1994](../../../../motivatie/beleidskaders/wegenverkeerswet-1994.md) | is grondslag voor *associatie (gericht)* | Verwerken vermissing rijbewijs | [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) (art. 123 lid 1 onder h) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wegenverkeerswet 1994](../../../../bronanalyses/burgerzaken/2026-rijk-wegenverkeerswet-1994-bwbr0006622.md) | Wegenverkeerswet 1994 |
| [Utrecht Rijbewijs aanvragen of verlengen](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-rijbewijs-aanvragen-of-verlengen.md) | Gemeente Utrecht: Rijbewijs aanvragen of verlengen |
| [Reglement rijbewijzen](../../../../bronanalyses/burgerzaken/2026-rijk-reglement-rijbewijzen-bwbr0008074.md) | Reglement rijbewijzen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA. Het specialiseert het generieke proces Behandelen aangifte of melding.
