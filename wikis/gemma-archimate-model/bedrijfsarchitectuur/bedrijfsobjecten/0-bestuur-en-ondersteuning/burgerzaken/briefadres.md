---
id: briefadres
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
naam: Briefadres
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Adres waar post voor een ingeschreven persoon zonder woonadres in ontvangst wordt genomen door een briefadresgever.
grondslag: ggm-entiteit
match:
  ggm: exact
  gemma: exact
data_object: ja
objectniveau: subobject
bronnen:
- 2026-rvig-hup-verblijfplaats
- 2026-nvvb-beleidsregel-briefadres
- 2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek
- 2023-rvig-circulaire-adresonderzoek-brp
- 2026-rvig-hup-binnengemeentelijke-adreswijziging
ggm_entiteit: Briefadres
ggm_guid: EAID_3015DCE3_7C05_4160_A717_533553258C15
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: 99 Kern
ggm_diagram:
- Diagram Gebied Vestiging en Adres
ggm_diagram_ids:
- EAID_19D888BE_5EC7_4590_BE67_8F66D91245F1
ggm_definitie: Een briefadres is een adres waar door de overheid verzonden stukken voor een persoon in ontvangst wordt genomen.
gemma_id: id-69e3c6f1bdcc4824a0af6b45213b5c31
gemma_naam: Briefadres
gemma_type: business-object
gemma_definitie: Een briefadres is een adres waar door de overheid verzonden stukken voor een persoon in ontvangst wordt genomen.
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-af282ab4-d6c4-4a5f-8126-db9b70cff048
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{3015DCE3-7C05-4160-A717-533553258C15}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: af282ab4-d6c4-4a5f-8126-db9b70cff048
---

# Briefadres

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/briefadres.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Adres waar post voor een ingeschreven persoon zonder woonadres in ontvangst wordt genomen door een briefadresgever.

### Beschrijving

Een briefadres vereist een briefadresgever die schriftelijk instemt en de post doorgeeft; dat is een natuurlijk persoon of een door het college aangewezen rechtspersoon (HUP Verblijfplaats). Een briefadres wordt geregistreerd als iemand geen woonadres heeft, in een aangewezen instelling verblijft of als opneming van het woonadres om veiligheidsredenen niet wenselijk is (HUP Verblijfplaats). Sinds 1 januari 2022 registreert de gemeente iemand zonder woonadres die geen aangifte doet ambtshalve op een briefadres; zonder briefadresgever op een adres van de gemeente (NVVB Beleidsregel briefadres; HUP Verblijfplaats).

### Homoniemen

| Begrip | Betekenis | Naamkeuze |
|---|---|---|
| [Briefadres aanvragen](../../../diensten/0-bestuur-en-ondersteuning/burgerzaken/briefadres-aanvragen.md) (UPL-lijst extern) | De dienst waarmee iemand een briefadres aanvraagt; in de UPL het product briefadres (nr. 85) | Deze pagina heet Briefadres: het adres zelf. De dienst heet Briefadres aanvragen, met de UPL-naam als synoniem. |

## Plaats in het model

### Typering

Bedrijfsobject, niveau subobject. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: subobject.
- **Mutaties door bedrijfsprocessen**: [Inschrijven op briefadres](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 49 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, gangbaar in wet, HUP, NVVB en gemeentelijke praktijk (HUP Verblijfplaats; NVVB Beleidsregel briefadres). [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../bronanalyses/burgerzaken/2026-nvvb-beleidsregel-briefadres.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de gemeente registreert iemand zonder woonadres op een briefadres, sinds 2022 ook verplicht ambtshalve (NVVB Beleidsregel briefadres). [NVVB Beleidsregel briefadres](../../../../bronanalyses/burgerzaken/2026-nvvb-beleidsregel-briefadres.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../bronanalyses/burgerzaken/2026-nvvb-beleidsregel-briefadres.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../bronanalyses/burgerzaken/2026-nvvb-beleidsregel-briefadres.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elk briefadres hoort bij één persoon en heeft een briefadresgever (HUP Verblijfplaats). [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, begint met de aangifte of ambtshalve registratie en eindigt als de persoon weer een woonadres heeft of na adresonderzoek (HUP Verblijfplaats; Utrecht Onjuiste inschrijving). [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, inschrijven op briefadres legt het vast; Uitvoeren adresonderzoek kan het beëindigen (HUP Verblijfplaats; Circulaire adresonderzoek 4.8). [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [RvIG Circulaire adresonderzoek BRP](../../../../bronanalyses/burgerzaken/2023-rvig-circulaire-adresonderzoek-brp.md) |
| **deel van object**: Is het een onderdeel van één ander object, dat ermee ontstaat en eindigt? | Ja, een vorm van de verblijfplaats van één ingeschreven persoon (HUP Verblijfplaats: functie adres B). [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **geautomatiseerd verwerkt**: Wordt het als gegevensstructuur geautomatiseerd verwerkt? | Ja, functie adres B in categorie 08, met een koppeling naar een nevenadres in de BAG (HUP Verblijfplaats). [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, specialisatie van Verblijfplaats die de gemeente anders behandelt: eigen voorwaarden, een briefadresgever en een eigen besluit (HUP Verblijfplaats; NVVB Beleidsregel briefadres); GGM en GEMMA kennen het als eigen begrip. [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../bronanalyses/burgerzaken/2026-nvvb-beleidsregel-briefadres.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Briefadres | is een *specialisatie* | [Verblijfplaats](verblijfplaats.md) | [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md), [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) (HUP Verblijfplaats, functie adres B) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Briefadresgever](../../../rollen/briefadresgever.md) | geeft post door *toegang (beheerder)* | Briefadres | [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Briefadres (art. 2.45)) |
| [Inschrijven op briefadres](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | legt vast *toegang (registreren)* | Briefadres | [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) (Briefadres) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Verblijfplaats](../../../../bronanalyses/burgerzaken/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |
| [NVVB Beleidsregel briefadres](../../../../bronanalyses/burgerzaken/2026-nvvb-beleidsregel-briefadres.md) | NVVB: Beleidsregel briefadres |
| [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../bronanalyses/burgerzaken/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md) | Gemeente Utrecht: Adresonderzoek |
| [RvIG Circulaire adresonderzoek BRP](../../../../bronanalyses/burgerzaken/2023-rvig-circulaire-adresonderzoek-brp.md) | Circulaire adresonderzoek BRP |
| [HUP Binnengemeentelijke adreswijziging](../../../../bronanalyses/burgerzaken/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) | HUP BRP: Binnengemeentelijke adreswijziging |

### Afstemming met GGM

Match **exact** met GGM-entiteit *Briefadres* (beleidsdomein RSGBPlus, taakveld 99 Kern). GGM-entiteit Briefadres (RSGBPlus): een adres waar door de overheid verzonden stukken voor een persoon in ontvangst worden genomen; zelfde begrip.

> Een briefadres is een adres waar door de overheid verzonden stukken voor een persoon in ontvangst wordt genomen.

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Briefadres* (business-object). GEMMA-bedrijfsobject Briefadres, overgenomen uit het GGM (zelfde GGM-guid en definitie).

> Een briefadres is een adres waar door de overheid verzonden stukken voor een persoon in ontvangst wordt genomen.
