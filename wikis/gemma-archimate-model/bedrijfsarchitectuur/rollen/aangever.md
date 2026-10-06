---
id: aangever
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Aangever
onderwerpen:
- burgerzaken
definitie: Hoedanigheid van wie bij de gemeente aangifte doet van een feit dat in de basisregistratie personen moet worden verwerkt, voor zichzelf of een ander.
grondslag: bron
match:
  gemma: geen
data_object: nee
doelgroep: inwoners en ondernemers
synoniemen:
- Doorgever (beleid)
bronnen:
- 2026-rvig-hup-verblijfplaats
- 2026-rvig-hup-emigratie
---

# Aangever

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/aangever.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Hoedanigheid van wie bij de gemeente aangifte doet van een feit dat in de basisregistratie personen moet worden verwerkt, voor zichzelf of een ander.

### Beschrijving

Een meerderjarige doet zelf aangifte van verblijf en adres, adreswijziging en vertrek; ouders, voogden en verzorgers zijn verplicht aangifte te doen voor minderjarigen; echtgenoten, partners en ouders met een meerderjarig kind zijn bevoegd voor elkaar; het hoofd van een instelling kan aangifte doen voor wie er verblijft (HUP Verblijfplaats). Het college kan verplichten in persoon te verschijnen (HUP Verblijfplaats; Besluit BRP art. 30).

### Synoniemen

| Synoniem | Context |
|---|---|
| Doorgever | beleid |

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.

### Kenmerken

Alleen de kenmerken met ja; de overige 53 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbare term (HUP Verblijfplaats: verplichte of bevoegde aangever). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, doet aangifte bij de gemeente (HUP Verblijfplaats). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de hoedanigheid waarin iemand aangifte doet voor zichzelf of een ander, verplicht of bevoegd (HUP Verblijfplaats). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, toegewezen aan Inschrijven ingezetene, Verwerken adreswijziging, Verwerken emigratie en Inschrijven op briefadres (HUP Verblijfplaats; HUP Emigratie). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [HUP Emigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere rol in deze wiki. [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Aangever | doet aangifte *toewijzing* | [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| Aangever | doet aangifte *toewijzing* | [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| Aangever | doet aangifte *toewijzing* | [Verwerken emigratie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| Aangever | doet aangifte *toewijzing* | [Inschrijven op briefadres](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangifte vertrek buitenland](../diensten/0-bestuur-en-ondersteuning/burgerzaken/aangifte-vertrek-buitenland.md) | bedient *bediening* | Aangever | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Briefadres aanvragen](../diensten/0-bestuur-en-ondersteuning/burgerzaken/briefadres-aanvragen.md) | bedient *bediening* | Aangever | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [BRP-inschrijving](../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving.md) | bedient *bediening* | Aangever | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Verhuismelding](../diensten/0-bestuur-en-ondersteuning/burgerzaken/verhuismelding.md) | bedient *bediening* | Aangever | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |
| [HUP Emigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
