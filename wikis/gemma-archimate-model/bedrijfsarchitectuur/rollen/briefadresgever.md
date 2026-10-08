---
id: briefadresgever
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Briefadresgever
onderwerpen:
- burgerzaken
definitie: Verantwoordelijkheid van een persoon of aangewezen rechtspersoon om post voor de houder van een briefadres in ontvangst te nemen en door te geven.
grondslag: bron
match:
  gemma: geen
data_object: nee
doelgroep: inwoners en ondernemers
bronnen:
- 2026-rvig-hup-verblijfplaats
- 2026-rijk-wet-brp-bwbr0033715
---

# Briefadresgever

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/briefadresgever.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid van een persoon of aangewezen rechtspersoon om post voor de houder van een briefadres in ontvangst te nemen en door te geven.

### Beschrijving

De briefadresgever is een natuurlijk persoon of een door het college aangewezen rechtspersoon; hij stemt schriftelijk in, zorgt dat geschriften voor de houder worden doorgegeven en verstrekt het college inlichtingen (HUP Verblijfplaats). Zonder briefadresgever registreert de gemeente een adres van de gemeente zelf (HUP Verblijfplaats).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.

### Kenmerken

Alleen de kenmerken met ja; de overige 53 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbare term (HUP Verblijfplaats). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, stemt schriftelijk in en verstrekt inlichtingen aan het college (HUP Verblijfplaats). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de verantwoordelijkheid om post voor de houder van een briefadres in ontvangst te nemen en door te geven (HUP Verblijfplaats). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, toegewezen aan Inschrijven op briefadres: stemt schriftelijk in (HUP Verblijfplaats). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere rol in deze wiki. [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Briefadresgever | stemt in met *toewijzing* | [Inschrijven op briefadres](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Briefadres; Wet BRP art. 2.23 lid 3, 2.45 lid 2) |
| Briefadresgever | geeft post door *toegang (beheerder)* | [Briefadres](../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/briefadres.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Briefadres; Wet BRP art. 2.45 lid 3) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Wet basisregistratie personen](../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Briefadresgever | [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 1.1, 2.42, 2.45) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Verblijfplaats](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |
| [Wet BRP](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
