---
id: verkrijging-van-het-nederlanderschap
type: gebeurtenis
archimate_type: business-event
status: goedgekeurd
naam: Verkrijging van het Nederlanderschap
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het moment waarop een persoon Nederlander wordt, van rechtswege of door de uitreiking van de bevestiging van de optie of het naturalisatiebesluit.
grondslag: bron
match:
  gemma: geen
data_object: nee
synoniemen:
- Verkrijging Nederlanderschap (informatiemodel)
bronnen:
- 2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738
- 2026-rvig-hup-nederlandse-nationaliteit
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
- 2026-rvig-hup-vreemde-nationaliteit
- 2026-rijk-paspoortwet-bwbr0005212
- 2026-rvig-hup-verblijfstitel
- 2026-rvig-hup-europees-kiesrecht
---

# Verkrijging van het Nederlanderschap

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/verkrijging-van-het-nederlanderschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Het moment waarop een persoon Nederlander wordt, van rechtswege of door de uitreiking van de bevestiging van de optie of het naturalisatiebesluit.

### Beschrijving

Het Nederlanderschap wordt verkregen van rechtswege, bij geboorte, erkenning of adoptie, of door optie of verlening (Rijkswet op het Nederlanderschap art. 3-7). Bij optie en naturalisatie treedt de verkrijging in werking door de uitreiking van de bevestiging of van het uittreksel van het besluit, en werkt terug tot de dagtekening (Besluit verkrijging en verlies Nederlanderschap art. 60a, 60b).

In de basisregistratie personen wordt de Nederlandse nationaliteit opgenomen, met de datum van naturalisatie of optiebevestiging als ingangsdatum; de registratie van vreemde en onbekende nationaliteiten en van staatloosheid, de verblijfstitel en de aanduiding Europees kiesrecht worden beëindigd (HUP Nederlandse nationaliteit; HUP Vreemde nationaliteit; HUP Verblijfstitel; HUP Europees kiesrecht). Een reisdocument voor vluchtelingen of vreemdelingen vervalt van rechtswege (Paspoortwet art. 47 lid 1 onder b).

### Synoniemen

| Synoniem | Context |
|---|---|
| Verkrijging Nederlanderschap | informatiemodel |

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
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, wetsbegrip: verkrijging van rechtswege, door optie of door verlening (Rijkswet art. 3-7); de HUP behandelt de verkrijging als gebeurtenis in de BRP. [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente reikt de bevestiging of het uittreksel uit, waarmee de verkrijging in werking treedt, en verwerkt haar in de basisregistratie personen (Besluit art. 60a, 60b; HUP Nederlandse nationaliteit). [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, een zelfstandige gebeurtenis met eigen gevolgen voor BRP, reisdocument en kiesrecht (HUP Nederlandse nationaliteit). [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij burgerzaken: verandert de toestand van het Nederlanderschap, kernobject van dit onderwerp. [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **gedrag**: Beschrijft het iets wat gedaan wordt of gebeurt, en geen ding, partij, plaats of regeling? | Ja, iets wat gebeurt. [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |
| **toestandsverandering**: Is het iets dat binnen of buiten de gemeente gebeurt, op één moment en zonder eigen duur, en dat gevolgen heeft? | Ja, op één moment wordt de persoon Nederlander: van rechtswege, of bij de uitreiking van de bevestiging of het uittreksel, met terugwerkende kracht tot de dagtekening (Rijkswet art. 3; Besluit art. 60a lid 1, 60b lid 1). [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md), [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) |
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke persoon die Nederlander wordt. [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, start Bijhouden persoonsgegevens: opnemen van de Nederlandse nationaliteit en beëindigen van vreemde en onbekende nationaliteiten, de verblijfstitel en de aanduiding Europees kiesrecht (HUP Nederlandse nationaliteit; HUP Vreemde nationaliteit); en het verval van een reisdocument voor vluchtelingen of vreemdelingen (Paspoortwet art. 47 lid 1 onder b). [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md), [HUP Vreemde nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-vreemde-nationaliteit.md), [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip van hetzelfde type in deze wiki. [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verkrijging van het Nederlanderschap | leidt tot bijhouding van nationaliteit, verblijfstitel en Europees kiesrecht *triggering* | [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md), [HUP Verblijfstitel](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfstitel.md), [HUP Europees kiesrecht](../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) (HUP Nederlandse nationaliteit; HUP Verblijfstitel; HUP Europees kiesrecht) |
| Verkrijging van het Nederlanderschap | doet een reisdocument voor vluchtelingen of vreemdelingen vervallen *triggering* | [Verval van het reisdocument](verval-van-het-reisdocument.md) | [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) (Paspoortwet art. 47 lid 1 onder b) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Beheren Nederlanderschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-nederlanderschap.md) | omvat *aggregatie* | Verkrijging van het Nederlanderschap | [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 60a lid 1, 60b lid 1) |
| [Houden naturalisatieceremonie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/houden-naturalisatieceremonie.md) | leidt tot *triggering* | Verkrijging van het Nederlanderschap | [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 60a lid 1, 60b lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Rijkswet op het Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) | Rijkswet op het Nederlanderschap |
| [HUP Nederlandse nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-nederlandse-nationaliteit.md) | HUP BRP: Nederlandse nationaliteit |
| [Besluit verkrijging en verlies Nederlanderschap](../../bronanalyses/burgerzaken/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [HUP Vreemde nationaliteit](../../bronanalyses/burgerzaken/2026-rvig-hup-vreemde-nationaliteit.md) | HUP BRP: Vreemde nationaliteit |
| [Paspoortwet](../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Verblijfstitel](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfstitel.md) | HUP BRP: Verblijfstitel |
| [HUP Europees kiesrecht](../../bronanalyses/burgerzaken/2026-rvig-hup-europees-kiesrecht.md) | HUP BRP: Europees kiesrecht |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
