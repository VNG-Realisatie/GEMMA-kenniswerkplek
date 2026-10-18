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
match:
  ggm: exact
  gemma: exact
data_objecten:
- Briefadres-data
objectniveau: subobject
bronnen:
- 2026-rvig-hup-verblijfplaats
- 2026-nvvb-beleidsregel-briefadres
- 2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek
- 2023-rvig-circulaire-adresonderzoek-brp
- 2026-rvig-hup-binnengemeentelijke-adreswijziging
- 2026-rijk-wet-brp-bwbr0033715
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

<!-- Gegenereerd door tools/render.py uit de beoordeling briefadres.yaml. Wijzig de beoordeling, niet deze pagina. -->

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

Bedrijfsobject, niveau subobject. Uitkomst van de beslistabel: Passief, object (3 toetskenmerken ja).

### Plaats in de indelingen

- **Objectniveau**: subobject.
- **Mutaties door bedrijfsprocessen**: [Inschrijven op briefadres](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: object.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: onderdeel | Een vorm van de verblijfplaats van één ingeschreven persoon (HUP Verblijfplaats: functie adres B). [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Inschrijven op briefadres](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md). [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md), [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md), [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, standaard. [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md), [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md), [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, standaard. [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md), [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md), [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Briefadres | is een *specialisatie* | [Verblijfplaats](verblijfplaats.md) | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (HUP Verblijfplaats, functie adres B; Wet BRP art. 1.1 (adres)) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Briefadresgever](../../../rollen/briefadresgever.md) | geeft post door *toegang (beheerder)* | Briefadres | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Briefadres; Wet BRP art. 2.45 lid 3) |
| [Inschrijven op briefadres](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-op-briefadres.md) | legt vast *toegang (registreren)* | Briefadres | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (Briefadres; Wet BRP art. 2.23) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Briefadres | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 1.1, 2.23, 2.40) |

### Data-objecten

- [Briefadres-data](../../../../applicatiearchitectuur/data-objecten/briefadres-data.md) *realisatie*: GGM-entiteit *Briefadres*, match exact.

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |
| [NVVB Beleidsregel briefadres](../../../../../onderwerpen/burgerzaken/bronduidingen/gemeentelijke-regelgeving/2026-nvvb-beleidsregel-briefadres.md) | NVVB: Beleidsregel briefadres |
| [Utrecht Onjuiste inschrijving melden (adresonderzoek)](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-onjuiste-inschrijving-op-uw-adres-melding-doen-adresonderzoek.md) | Gemeente Utrecht: Adresonderzoek |
| [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) | Circulaire adresonderzoek BRP |
| [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) | HUP BRP: Binnengemeentelijke adreswijziging |
| [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) | Wet basisregistratie personen |

### Afstemming met GGM

Match **exact** met GGM-entiteit *Briefadres* (beleidsdomein RSGBPlus, taakveld 99 Kern). GGM-entiteit Briefadres (RSGBPlus): een adres waar door de overheid verzonden stukken voor een persoon in ontvangst worden genomen; zelfde begrip.

> Een briefadres is een adres waar door de overheid verzonden stukken voor een persoon in ontvangst wordt genomen.

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Briefadres* (business-object). GEMMA-bedrijfsobject Briefadres, overgenomen uit het GGM (zelfde GGM-guid en definitie).

> Een briefadres is een adres waar door de overheid verzonden stukken voor een persoon in ontvangst wordt genomen.
