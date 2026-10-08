---
id: aangever
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Aangever
onderwerpen:
- burgerzaken
definitie: Hoedanigheid van wie bij de gemeente aangifte doet van een feit voor de basisregistratie personen of de burgerlijke stand, voor zichzelf of een ander.
grondslag: bron
match:
  gemma: geen
data_object: nee
doelgroep: inwoners en ondernemers
bronnen:
- 2026-rvig-hup-verblijfplaats
- 2026-rijk-burgerlijk-wetboek-boek-1
- 2026-rvig-hup-emigratie
- 2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen
---

# Aangever

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/aangever.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Hoedanigheid van wie bij de gemeente aangifte doet van een feit voor de basisregistratie personen of de burgerlijke stand, voor zichzelf of een ander.

### Beschrijving

Een meerderjarige doet zelf aangifte van verblijf en adres, adreswijziging en vertrek; ouders, voogden en verzorgers zijn verplicht aangifte te doen voor minderjarigen; echtgenoten, partners en ouders met een meerderjarig kind zijn bevoegd voor elkaar; het hoofd van een instelling kan aangifte doen voor wie er verblijft (HUP Verblijfplaats). Het college kan verplichten in persoon te verschijnen (HUP Verblijfplaats; Besluit BRP art. 30).

Bij de burgerlijke stand doet de aangever aangifte bij de ambtenaar van de burgerlijke stand: van een geboorte (de vader of moeder, of wie bij de bevalling aanwezig was; BW 1 art. 19e), van een overlijden (wie het uit eigen wetenschap weet, of een gemachtigde zoals de uitvaartondernemer; art. 19h), van een levenloos geboren kind (art. 19i) en van de wijziging van de vermelding van het geslacht (art. 28). De ambtenaar stelt de identiteit van de aangever vast (art. 19e lid 8).

### Naamkeuze

Aangever is de wetsterm (BW 1 art. 19e, 19h, 19i, 28) en ook de term van de HUP (Verplichte of bevoegde aangever) en van Utrecht (Geboorteaangifte doen); een afwijkende gangbare term staat in geen bron. Doorgever, dat een eerdere versie als synoniem met context beleid noemde, komt als zelfstandig naamwoord in geen enkele bron voor (Utrecht noemt alleen het werkwoord doorgeven bij Verhuizing doorgeven en Emigratie doorgeven) en is vervallen.

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
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de hoedanigheid waarin iemand aangifte doet voor zichzelf of een ander, verplicht of bevoegd (HUP Verblijfplaats). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, toegewezen aan Inschrijven ingezetene, Verwerken adreswijziging, Verwerken emigratie en Inschrijven op briefadres (HUP Verblijfplaats; HUP Emigratie). Bij de burgerlijke stand: de aangifte van geboorte, overlijden, levenloos geboren kind en geslachtswijziging (BW 1 art. 19e, 19h, 19i, 28). [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [HUP Emigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md), [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen bredere rol in deze wiki. [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Aangever | doet aangifte *toewijzing* | [Inschrijven ingezetene](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| Aangever | doet aangifte *toewijzing* | [Verwerken adreswijziging](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| Aangever | doet aangifte *toewijzing* | [Verwerken emigratie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-emigratie.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| Aangever | doet aangifte *toewijzing* | [Inschrijven op briefadres](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| Aangever | doet aangifte *toewijzing* | [Opmaken akte van overlijden](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-van-overlijden.md) | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19h) |
| Aangever | doet aangifte *toewijzing* | [Opmaken geboorteakte](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-geboorteakte.md) | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 19e) |
| Aangever | doet aangifte *toewijzing* | [Opmaken akte levenloos geboren kind](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/opmaken-akte-levenloos-geboren-kind.md) | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md), [Utrecht Levenloos geboren kind, aangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md) (art. 19i) |
| Aangever | doet aangifte *toewijzing* | [Wijzigen geslachtsvermelding](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/wijzigen-geslachtsvermelding.md) | [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (art. 28) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aangifte vertrek buitenland](../diensten/0-bestuur-en-ondersteuning/burgerzaken/aangifte-vertrek-buitenland.md) | bedient *bediening* | Aangever | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Briefadres aanvragen](../diensten/0-bestuur-en-ondersteuning/burgerzaken/briefadres-aanvragen.md) | bedient *bediening* | Aangever | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [BRP-inschrijving](../diensten/0-bestuur-en-ondersteuning/burgerzaken/brp-inschrijving.md) | bedient *bediening* | Aangever | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |
| [Uitvaartondernemer](../actoren/uitvaartondernemer.md) | doet aangifte van overlijden als *toewijzing* | Aangever | [Utrecht Overlijden, aangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-overlijden-aangifte-doen.md), [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) (Utrecht inleiding; BW 1 art. 19h lid 2) |
| [Verhuismelding](../diensten/0-bestuur-en-ondersteuning/burgerzaken/verhuismelding.md) | bedient *bediening* | Aangever | [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Verplichte of bevoegde aangever) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Verblijfplaats](../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |
| [BW boek 1](../../bronanalyses/burgerzaken/2026-rijk-burgerlijk-wetboek-boek-1.md) | Burgerlijk Wetboek Boek 1 (Personen- en familierecht) |
| [HUP Emigratie](../../bronanalyses/burgerzaken/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |
| [Utrecht Levenloos geboren kind, aangifte doen](../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-levenloos-geboren-kind-of-overleden-pasgeboren-kind-aangifte-doen.md) | Gemeente Utrecht: Levenloos geboren kind |

### Afstemming met GEMMA

Nieuw voor GEMMA: het GEMMA-model kent geen element voor dit begrip. Het GEMMA-model kent geen rol voor dit begrip; nieuw voor GEMMA.
