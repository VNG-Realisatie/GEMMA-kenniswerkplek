---
id: verlies-van-het-nederlanderschap
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Verlies van het Nederlanderschap
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het moment waarop een persoon het Nederlanderschap verliest, door afstand, een andere nationaliteit, verblijf in het buitenland of intrekking.
grondslag: bron
match:
  gemma: geen
data_object: nee
synoniemen:
- Verlies Nederlanderschap (informatiemodel)
bronnen:
- 2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738
- 2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen
- 2026-rvig-hup-nederlandse-nationaliteit
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
- 2026-rvig-hup-nationaliteit
- 2026-rijk-paspoortwet-bwbr0005212
---

# Verlies van het Nederlanderschap

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verlies-van-het-nederlanderschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het moment waarop een persoon het Nederlanderschap verliest, door afstand, een andere nationaliteit, verblijf in het buitenland of intrekking.

### Beschrijving

Het Nederlanderschap gaat voor een meerderjarige verloren door het vrijwillig verkrijgen van een andere nationaliteit, door een verklaring van afstand, door dertien jaar hoofdverblijf buiten het Koninkrijk en de EU met ook een vreemde nationaliteit, of door intrekking door de minister; een minderjarige verliest het onder meer met zijn ouder (Rijkswet op het Nederlanderschap art. 14-16). Utrecht onderscheidt het opgeven, door een verklaring van afstand, van het verliezen zonder bewuste keuze.

In de basisregistratie personen wordt de Nederlandse nationaliteit beëindigd en worden vreemde of onbekende nationaliteiten weer opgenomen; een Nederlands reisdocument vervalt van rechtswege en de burgemeester bevordert dat het wordt ingenomen (HUP Nederlandse nationaliteit; Paspoortwet art. 47 lid 1 onder a; Besluit verkrijging en verlies Nederlanderschap art. 64 lid 3).

### Synoniemen

| Synoniem | Context |
|---|---|
| Verlies Nederlanderschap | informatiemodel |

## Plaats in het model

### Typering

Gebeurtenis. Uitkomst van de beslistabel: Gedrag, *toestandsverandering* (kern ja, 1/1).

### Plaats in de indelingen

- **Start**: [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md), [Verval van het reisdocument](verval-van-het-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 50 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, wetsbegrip (Rijkswet art. 15, 16); Utrecht: de Nederlandse nationaliteit verliezen; gebeurtenis in de BRP (HUP Nederlandse nationaliteit). [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Utrecht nationaliteit opgeven](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md), [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de burgemeester bevestigt de afstand en de gemeente verwerkt het verlies in de basisregistratie personen en laat reisdocumenten innemen (Besluit art. 63, 64; HUP Nederlandse nationaliteit). [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, een zelfstandige gebeurtenis met eigen gevolgen voor BRP en reisdocument (HUP Nationaliteit). [HUP Nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nationaliteit.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij burgerzaken: verandert de toestand van het Nederlanderschap, kernobject van dit onderwerp. [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, op één moment verliest de persoon het Nederlanderschap: door afstand, het vrijwillig verkrijgen van een andere nationaliteit, langdurig hoofdverblijf buiten het Koninkrijk en de EU, of intrekking (Rijkswet art. 15). [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke persoon die het Nederlanderschap verliest. [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start Bijhouden persoonsgegevens: beëindigen van de Nederlandse nationaliteit en opnieuw opnemen van vreemde of onbekende nationaliteiten (HUP Nederlandse nationaliteit); en het verval van een Nederlands reisdocument van rechtswege (Paspoortwet art. 47 lid 1 onder a; HUP Nationaliteit). [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md), [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nationaliteit.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verlies van het Nederlanderschap | leidt tot beëindiging van de Nederlandse nationaliteit *triggering* | [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) (HUP Nederlandse nationaliteit, kop Verlies) |
| Verlies van het Nederlanderschap | doet een Nederlands reisdocument vervallen *triggering* | [Verval van het reisdocument](verval-van-het-reisdocument.md) | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nationaliteit.md) (Paspoortwet art. 47 lid 1 onder a; HUP Nationaliteit) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen verklaring van afstand](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verklaring-van-afstand.md) | leidt tot *triggering* | Verlies van het Nederlanderschap | [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) (art. 15 lid 1 onder b) |
| [Beheren Nederlanderschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-nederlanderschap.md) | omvat *aggregatie* | Verlies van het Nederlanderschap | [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) (art. 15) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) | Rijkswet op het Nederlanderschap |
| [Utrecht nationaliteit opgeven](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-nederlandse-nationaliteit-opgeven-of-verliezen.md) | Gemeente Utrecht: Nederlandse nationaliteit opgeven of verliezen |
| [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) | HUP BRP: Nederlandse nationaliteit |
| [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [HUP Nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nationaliteit.md) | HUP BRP: Nationaliteit |
| [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
