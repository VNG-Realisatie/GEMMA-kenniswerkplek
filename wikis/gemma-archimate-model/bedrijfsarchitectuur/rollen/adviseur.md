---
id: adviseur
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Adviseur
onderwerpen:
- lijkbezorging
definitie: Verantwoordelijkheid voor het geven van advies aan wie een besluit neemt.
grondslag: bron
match:
  gemma: sterk
data_object: nee
doelgroep: ketenpartners
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rijk-wet-publieke-gezondheid-wettekst
gemma_id: id-f3219a6a-532f-482d-897c-dafe0dc70bb0
gemma_naam: Adviseur
gemma_type: business-role
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: f3219a6a-532f-482d-897c-dafe0dc70bb0
---

# Adviseur

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/adviseur.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid voor het geven van advies aan wie een besluit neemt.

### Beschrijving

Een adviseur geeft een bestuursorgaan vooraf advies over een besluit. De wet bepaalt wanneer advies nodig is, bijvoorbeeld het advies van de GGD aan de burgemeester bij een besmet lijk (Wet op de lijkbezorging art. 22a) of aan het college bij besluiten met belangrijke gevolgen voor de publieke gezondheid (Wet publieke gezondheid art. 16).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: ketenpartners.

### Kenmerken

Alleen de kenmerken met ja; de overige 53 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, rol uit GEMMA; de wet spreekt van advies van de GGD (Wlb art. 22a, Wpg art. 16). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, adviseert de gemeentelijke bestuursorganen. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, en niet bij een ander onderwerp waar het wordt beoordeeld? | Ja, hoort primair bij dit onderwerp; geen ander onderwerp beoordeelt het. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de verantwoordelijkheid om de beslisser vooraf advies te geven. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, toegewezen aan Treffen maatregel bij besmet stoffelijk overschot: de GGD adviseert de burgemeester (Wlb art. 22a). [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder element in deze wiki. [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Adviseur | adviseert over *toewijzing* | [Treffen maatregel bij besmet stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/treffen-maatregel-bij-besmet-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [GGD](../actoren/ggd.md) | vervult *toewijzing* | Adviseur | [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) (Wlb art. 22a; Wpg art. 16) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Wet publieke gezondheid](../../bronanalyses/lijkbezorging/2026-rijk-wet-publieke-gezondheid-wettekst.md) | Wet publieke gezondheid (BWBR0024705) |

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Adviseur* (business-role). GEMMA-rol Adviseur; zelfde begrip, in GEMMA zonder definitie. Nieuw: een definitie.
