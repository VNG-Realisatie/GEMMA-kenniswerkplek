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
match:
  gemma: geen
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

<!-- Gegenereerd door tools/render.py uit de beoordeling verkrijging-van-het-nederlanderschap.yaml. Wijzig de beoordeling, niet deze pagina. -->

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

**Vak**: bedrijfslaag, gedrag, intern (Bedrijfsproces, Bedrijfsfunctie, Gebeurtenis, Bedrijfsinteractie). **Hoofdkenmerk**: gedrag. **Soort gedrag**: toestandsverandering. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **komt herhaald voor**: Wordt het regelmatig en voor verschillende gevallen uitgevoerd, of gebeurt het voor verschillende gevallen, en is het geen eenmalig project of voorval? | Ja, voor elke persoon die Nederlander wordt. [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md) |
| **leidt tot gedrag**: Start, onderbreekt of beëindigt de gebeurtenis aanwijsbaar gemeentelijk gedrag? | Ja, met [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Verkrijging van het Nederlanderschap | leidt tot bijhouding van nationaliteit, verblijfstitel en Europees kiesrecht *triggering* | [Bijhouden persoonsgegevens](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/bijhouden-persoonsgegevens.md) | [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md), [HUP Verblijfstitel](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfstitel.md), [HUP Europees kiesrecht](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) (HUP Nederlandse nationaliteit; HUP Verblijfstitel; HUP Europees kiesrecht) |
| Verkrijging van het Nederlanderschap | doet een reisdocument voor vluchtelingen of vreemdelingen vervallen *triggering* | [Verval van het reisdocument](verval-van-het-reisdocument.md) | [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md) (Paspoortwet art. 47 lid 1 onder b) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen naturalisatieverzoek](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-naturalisatieverzoek.md) | leidt tot *triggering* | Verkrijging van het Nederlanderschap | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 60a lid 1, 60b lid 1) |
| [Behandelen optieverklaring](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-optieverklaring.md) | leidt tot *triggering* | Verkrijging van het Nederlanderschap | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (art. 60a lid 1, 60b lid 1) |
| [Beheren Nederlanderschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-nederlanderschap.md) | omvat *aggregatie* | Verkrijging van het Nederlanderschap | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) (art. 60a lid 1, 60b lid 1) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Rijkswet op het Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-rijkswet-op-het-nederlanderschap-bwbr0003738.md) | Rijkswet op het Nederlanderschap |
| [HUP Nederlandse nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-nederlandse-nationaliteit.md) | HUP BRP: Nederlandse nationaliteit |
| [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [HUP Vreemde nationaliteit](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-vreemde-nationaliteit.md) | HUP BRP: Vreemde nationaliteit |
| [Paspoortwet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [HUP Verblijfstitel](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfstitel.md) | HUP BRP: Verblijfstitel |
| [HUP Europees kiesrecht](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) | HUP BRP: Europees kiesrecht |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen gebeurtenis voor dit begrip; nieuw voor GEMMA.
