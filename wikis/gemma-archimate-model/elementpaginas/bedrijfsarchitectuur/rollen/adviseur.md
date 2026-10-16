---
id: adviseur
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Adviseur
onderwerpen:
- lijkbezorging
definitie: Verantwoordelijkheid voor het geven van advies aan wie een besluit neemt.
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

<!-- Gegenereerd door tools/render.py uit de beoordeling adviseur.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid voor het geven van advies aan wie een besluit neemt.

### Beschrijving

Een adviseur geeft een bestuursorgaan vooraf advies over een besluit. De wet bepaalt wanneer advies nodig is, bijvoorbeeld het advies van de GGD aan de burgemeester bij een besmet stoffelijk overschot (Wet op de lijkbezorging art. 22a) of aan het college bij besluiten met belangrijke gevolgen voor de publieke gezondheid (Wet publieke gezondheid art. 16).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: ketenpartners.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Treffen maatregel bij besmet stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/treffen-maatregel-bij-besmet-stoffelijk-overschot.md). |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Adviseur | adviseert over *toewijzing* | [Treffen maatregel bij besmet stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/treffen-maatregel-bij-besmet-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 22a) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [GGD](../actoren/ggd.md) | vervult *toewijzing* | Adviseur | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) (Wlb art. 22a; Wpg art. 16) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Wet publieke gezondheid](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-publieke-gezondheid-wettekst.md) | Wet publieke gezondheid (BWBR0024705) |

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Adviseur* (business-role). GEMMA-rol Adviseur; zelfde begrip, in GEMMA zonder definitie. Nieuw: een definitie.

GEMMA-terugmeldingen:

- [Nummer 4](../../../modellen/gemma/terugmeldingen/gemma-team.md) (definitie, open): **GEMMA:** de rollen Ketenpartner, Adviseur en Beslisser in de procesarchitectuur hebben geen definitie ([2026-vng-gemma-2026-10-02](../../../modellen/gemma/bronduidingen/model/2026-vng-gemma-2026-10-02.md)). **Bevinding:** de wiki heeft deze drie rollen aan GEMMA gekoppeld en gebruikt ze in lijkbezorging en burgerzaken. De import vult dus de definities in. Via Beslisser hangen burgemeester, college en raad aan de processen; welk orgaan beslist, staat in de beschrijving van het proces. De definitie van Ketenpartner spreekt van een andere organisatie, terwijl in de wiki ook personen de rol vervullen, zoals de behandelende arts en de officier van justitie; de wiki kan die definitie nog verbreden. **Voorstel:** controleer de definities bij de import: Ketenpartner: verantwoordelijkheid van een andere organisatie voor haar deel van een keten die zij met de gemeente uitvoert; Adviseur: verantwoordelijkheid voor het geven van advies aan wie een besluit neemt; Beslisser: verantwoordelijkheid voor het nemen van het besluit in een proces.
