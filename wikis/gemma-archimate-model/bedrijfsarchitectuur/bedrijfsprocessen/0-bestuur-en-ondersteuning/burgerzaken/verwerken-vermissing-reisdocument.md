---
id: verwerken-vermissing-reisdocument
type: bedrijfsproces
archimate_type: business-process
status: goedgekeurd
naam: Verwerken vermissing reisdocument
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het ontvangen en registreren van de melding dat een reisdocument kwijt of gestolen is, waardoor het document ongeldig wordt.
grondslag: bron
match:
  gemma: geen
data_object: nee
procesniveau: deelproces
afnemer: extern
synoniemen:
- Melding van vermissing (wet)
bronnen:
- 2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven
- 2026-rvig-hup-inhouding-inlevering-vermissing
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-reisdocument
---

# Verwerken vermissing reisdocument

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verwerken-vermissing-reisdocument.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het ontvangen en registreren van de melding dat een reisdocument kwijt of gestolen is, waardoor het document ongeldig wordt.

### Beschrijving

De houder meldt de vermissing per document, online en gratis; de gemeente registreert de schriftelijke verklaring van vermissing direct (Utrecht; HUP Inhouding). Met de registratie wordt het document in het basisregister reisdocumenten automatisch ongeldig en vervalt het van rechtswege (HUP Inhouding; Paspoortwet art. 47 lid 1 onder j). De minister vermeldt vermiste reisdocumenten in het register vermiste of vervallen reisdocumenten, ter voorkoming van fraude (art. 4a).

Een vermissing is onomkeerbaar: een teruggevonden document wordt nooit meer teruggegeven, maar ingeleverd bij de gemeente (HUP Inhouding; Utrecht). Wie na een vermissing een nieuw document aanvraagt zonder ander reisdocument, laat eerst de identiteit vaststellen (Utrecht).

### Synoniemen

| Synoniem | Context |
|---|---|
| Melding van vermissing | wet |

## Plaats in het model

### Typering

Bedrijfsproces, niveau deelproces. Uitkomst van de beslistabel: Gedrag, *per keer doorlopen* (kern ja).

### Plaats in de indelingen

- **Procesniveau**: deelproces.
- **Procesindeling naar taak, onderdeel van**: [Beheren reisdocumenten](beheren-reisdocumenten.md).
- **Kernobject**: [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md).
- **Procesindeling naar soort werk, specialisatie van**: GEMMA-element *Behandelen aangifte of melding*. Een melding van een gebeurtenis waardoor de gemeente haar registratie bijwerkt; de melder krijgt bericht dat ze is verwerkt (HUP Inhouding).
- **Gestart door gebeurtenis**: [Vermissing van het reisdocument](../../../gebeurtenissen/vermissing-van-het-reisdocument.md).
- **Eindigt in gebeurtenis**: [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md).
- **Afnemer**: extern.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 44 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, vermissing of diefstal doorgeven (Utrecht); de HUP beschrijft de registratie van de vermissing (HUP Inhouding). [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md), [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente neemt de verklaring van vermissing in ontvangst en registreert haar (HUP Inhouding; Utrecht). [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md), [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md), [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gedaan wordt. [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md), [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **per keer doorlopen**: Is het een reeks opeenvolgende activiteiten die per geval van begin tot eind wordt doorlopen? | Ja, wordt per gemelde vermissing doorlopen. [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md), [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **toegewezen partij**: Is een rol aanwijsbaar die het gedrag uitvoert of ervoor verantwoordelijk is? | Ja, de Houder van het reisdocument meldt de vermissing, vanaf achttien jaar zelf; voor een kind tot en met elf jaar een Ouder, van twaalf tot en met zeventien jaar het kind of een ouder (Paspoortwet art. 5a; Utrecht). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **gebruikt objecten**: Registreert, bijwerkt, beëindigt, raadpleegt, verstrekt, bewaart, brengt over of vernietigt het gedrag aanwijsbare bedrijfsobjecten? | Ja, werkt het reisdocument bij: vermist en daarmee ongeldig (HUP Inhouding; Paspoortwet art. 47 lid 1 onder j). [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md), [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **aanleiding**: Start het door een aanwijsbare gebeurtenis, verzoek of termijn? | Ja, de vermissing van het reisdocument en de melding daarvan (Paspoortwet art. 5a, 31 lid 1). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **benoembaar resultaat**: Levert het een concreet resultaat op (besluit, product, verslag, afspraak); bij een dienst of product: wat krijgt de afnemer? | Ja, de geregistreerde vermissing: het document is niet meer geldig, ook niet als het terugkomt (Utrecht; HUP Inhouding). [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md), [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke gemelde vermissing. [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **eigen normering**: Gelden er eigen regels, termijnen of bevoegdheden voor uit een wet, verordening of beleidsregel? | Ja, paspoortwet art. 4a (register vermiste of vervallen reisdocumenten), 5a (melding), 31 lid 1 (melding bij een nieuwe aanvraag) en 47 lid 1 onder j (verval door de verklaring). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **bijdrage aan groter proces**: Wordt het binnen één organisatorische eenheid uitgevoerd als bijdrage aan een groter bedrijfsproces dat het eindresultaat levert? | Ja, draagt bij aan Beheren reisdocumenten: het einde van een vermist reisdocument. [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **levert aanbod**: Realiseert het een dienst of levert het een product aan een afnemer? | Ja, realiseert de dienst Vermissing of diefstal reisdocument doorgeven (Utrecht). [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |
| **leidt tot gebeurtenis**: Eindigt het in een toestandsverandering die domeinexperts benoemen, of die een ander proces start? | Ja, verval van het reisdocument: door de verklaring van vermissing vervalt het van rechtswege (Paspoortwet art. 47 lid 1 onder j). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md), [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verwerken vermissing reisdocument | registreert vermissing van *toegang (bijwerken)* | [Reisdocument](../../../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/reisdocument.md) | [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md), [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) (HUP Inhouding, inleiding; Paspoortwet art. 47 lid 1 onder j) |
| Verwerken vermissing reisdocument | realiseert *realisatie* | [Vermissing of diefstal reisdocument doorgeven](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/vermissing-of-diefstal-reisdocument-doorgeven.md) | [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) (regel 17-23) |
| Verwerken vermissing reisdocument | geeft vermissing door aan *stroom* | [Bijhouden persoonsgegevens](bijhouden-persoonsgegevens.md) | [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md), [HUP Reisdocument](../../../../bronanalyses/burgerzaken/2026-rvig-hup-reisdocument.md) (HUP Inhouding, inleiding; HUP Reisdocument) |
| Verwerken vermissing reisdocument | leidt tot *triggering* | [Verval van het reisdocument](../../../gebeurtenissen/verval-van-het-reisdocument.md) | [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) (Paspoortwet art. 47 lid 1 onder j; HUP Inhouding) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren reisdocumenten](beheren-reisdocumenten.md) | omvat *aggregatie* | Verwerken vermissing reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) (Paspoortwet art. 5a; HUP Inhouding) |
| [Houder van het reisdocument](../../../rollen/houder-van-het-reisdocument.md) | meldt vermissing *toewijzing* | Verwerken vermissing reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) (art. 5a; Utrecht regel 33-37) |
| [Ouder](../../../rollen/ouder.md) | meldt vermissing voor een kind *toewijzing* | Verwerken vermissing reisdocument | [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) (regel 35-37) |
| [Paspoortwet](../../../../motivatie/beleidskaders/paspoortwet.md) | is grondslag voor *associatie (gericht)* | Verwerken vermissing reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) (art. 4a, 5a, 31, 47 lid 1 onder j) |
| [Vermissing van het reisdocument](../../../gebeurtenissen/vermissing-van-het-reisdocument.md) | leidt tot *triggering* | Verwerken vermissing reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) (Paspoortwet art. 5a; Utrecht regel 17-23) |
| [Wet op de Nederlandse identiteitskaart](../../../../motivatie/beleidskaders/wet-op-de-nederlandse-identiteitskaart.md) | is grondslag voor *associatie (gericht)* | Verwerken vermissing reisdocument | [Wet op de Nederlandse identiteitskaart](../../../../bronanalyses/burgerzaken/2026-rijk-wet-op-de-nederlandse-identiteitskaart-bwbr0052951.md) (art. 5a, 7, 19, 30 lid 1 onder h) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Utrecht Vermissing paspoort of ID-kaart](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-vermissing-of-diefstal-doorgeven.md) | Gemeente Utrecht: Paspoort of ID-kaart kwijt |
| [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/2026-rvig-hup-inhouding-inlevering-vermissing.md) | HUP BRP: Inhouding inlevering vermissing |
| [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Reisdocument](../../../../bronanalyses/burgerzaken/2026-rvig-hup-reisdocument.md) | HUP BRP: Reisdocument |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen proces voor dit begrip; nieuw voor GEMMA. Het specialiseert het generieke proces Behandelen aangifte of melding.

Procesarchitectuur-terugmeldingen:

- [Nummer 4](../../../../analyses/procesarchitectuur-terugmeldingen.md) (kennismodel, open): **Kennismodel:** een deelproces realiseert een deelservice: een onderdeel van een dienst, dat in verschillende bedrijfsprocessen wordt gebruikt maar geen dienst is die de organisatie aan de buitenwereld levert. De dienst zelf wordt gerealiseerd door een bedrijfsproces of ketenproces ([2026-vng-over-gemma](../../../../analyses/gemma-kennismodel.md), regel 385, 398, 591, 603). **GEMMA:** een deelproces realiseert de dienst van een UPL-product, bijvoorbeeld Verlenen verlof tot begraving of crematie de dienst Verlof tot begraven en Verlenen grafrecht de dienst Graf aanvragen. Het model heeft één bedrijfs- of ketenproces per kernobject (Beheren grafrechten, Beheren graven, Bezorgen stoffelijk overschot); daaronder levert elk deelproces één product of dienst. Eén bedrijfsproces per product maakt het model plat: een gemeente levert zo'n 500 externe en 215 interne producten en diensten ([2025-vng-upl-producten-en-diensten-extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md), 2025-vng-upl-producten-en-diensten-intern).
