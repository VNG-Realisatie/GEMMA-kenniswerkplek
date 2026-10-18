---
id: ketenpartner
type: rol
archimate_type: business-role
status: review
naam: Ketenpartner
onderwerpen:
- kern
- lijkbezorging
- burgerzaken
definitie: Verantwoordelijkheid van een andere organisatie voor haar deel van een keten die zij met de gemeente uitvoert.
match:
  gemma: exact
doelgroep: ketenpartners
bronnen:
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605
- 2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie
- 2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194
- 2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog
gemma_id: id-e03a0402-1890-4a21-8143-c44a8ba53ea4
gemma_naam: Ketenpartner
gemma_type: business-role
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: e03a0402-1890-4a21-8143-c44a8ba53ea4
---

# Ketenpartner

<!-- Gegenereerd door tools/render.py uit de beoordeling ketenpartner.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Verantwoordelijkheid van een andere organisatie voor haar deel van een keten die zij met de gemeente uitvoert.

### Beschrijving

Een ketenpartner is een andere organisatie die een eigen deel van een keten uitvoert, vanuit een eigen wettelijke taak, en niet als klant of alleen als adviseur. GEMMA kent de rol Ketenpartner in de procesarchitectuur en de doelgroep Ketenpartners.

### Per onderwerp

#### [Lijkbezorging](../../../onderwerpen/lijkbezorging/begrippen.md)

De officier van justitie is ketenpartner in Bezorgen stoffelijk overschot: hij ontvangt bij een niet-natuurlijke dood het verslag van de lijkschouwer, geeft de verklaring van geen bezwaar af en stemt in met een vervroegde uitvaart (Wet op de lijkbezorging art. 10, 12, 17).

De arts is als behandelende arts ketenpartner in Bezorgen stoffelijk overschot: hij schouwt het stoffelijk overschot en geeft de verklaring van overlijden af, en meldt zich bij de gemeentelijke lijkschouwer als hij dat niet kan of als het om een minderjarige gaat (Wet op de lijkbezorging art. 3, 7, 10a, 12).

#### [Burgerzaken](../../../onderwerpen/burgerzaken/begrippen.md)

Het Rijk is ketenpartner in Beheren Nederlanderschap via de minister van Justitie en Veiligheid, in de praktijk de IND: hij ontvangt het naturalisatieverzoek met het advies van de burgemeester, beoordeelt het en beslist; de Koning verleent het Nederlanderschap op zijn voordracht, en hij adviseert bij sommige opties en kan het Nederlanderschap intrekken (Besluit verkrijging en verlies Nederlanderschap art. 37, 38; Rijkswet op het Nederlanderschap art. 6 lid 3, 7, 15; Utrecht). Het Rijk is ook ketenpartner in Afgeven verklaring omtrent het gedrag via de minister van Justitie en Veiligheid, in de praktijk Justis: de gemeente ontvangt, controleert en zendt door, de minister onderzoekt het gedrag en beslist (Wet justitiële en strafvorderlijke gegevens art. 30, 36, 37; Utrecht). Bijhouden persoonsgegevens, Beheren reisdocumenten en Beheren rijbewijzen zijn geen keten: de minister van BZK voert daar tegenover de burger geen eigen deel uit, en de RDW en het CBR leveren productie, register en verklaring van geschiktheid als invoer terwijl de burgemeester besluit (Wegenverkeerswet 1994 art. 116, 118a; Reglement rijbewijzen art. 97, 105, 119).

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (1 toetskenmerken ja).

### Plaats in de indelingen

- **Doelgroep**: ketenpartners.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md), [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Bezorgen stoffelijk overschot](../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md), [Stellen andere termijn](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md), [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md), [Beheren Nederlanderschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-nederlanderschap.md), [Afgeven verklaring omtrent het gedrag](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/afgeven-verklaring-omtrent-het-gedrag.md). [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md), [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) |

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Ketenpartner | voert zijn deel uit van *toewijzing* | [Bezorgen stoffelijk overschot](../bedrijfsinteracties/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/bezorgen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 10, 12, 17) |
| Ketenpartner | stemt in met vervroegen bij *toewijzing* | [Stellen andere termijn](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/stellen-andere-termijn.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 17 lid 1) |
| Ketenpartner | schouwt als behandelende arts *toewijzing* | [Schouwen stoffelijk overschot](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/schouwen-stoffelijk-overschot.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 7 lid 1) |
| Ketenpartner | beoordeelt en beslist over de naturalisatie *toewijzing* | [Beheren Nederlanderschap](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-nederlanderschap.md) | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) (Besluit art. 37, 38; Utrecht) |
| Ketenpartner | onderzoekt het gedrag en beslist over de afgifte *toewijzing* | [Afgeven verklaring omtrent het gedrag](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/afgeven-verklaring-omtrent-het-gedrag.md) | [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md), [Utrecht VOG aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) (art. 30, 36, 37; Utrecht regel 59) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Arts](../actoren/arts.md) | vervult als behandelende arts *toewijzing* | Ketenpartner | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 3, 7, 10a, 12) |
| [Officier van justitie](../actoren/officier-van-justitie.md) | vervult *toewijzing* | Ketenpartner | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) (art. 10, 12, 17) |
| [Rijk](../actoren/rijk.md) | vervult *toewijzing* | Ketenpartner | [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md), [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) (art. 37, 38; Wjsg art. 30, 37) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [Besluit verkrijging en verlies Nederlanderschap](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-besluit-verkrijging-verlies-nederlanderschap-bwbr0013605.md) | Besluit verkrijging en verlies Nederlanderschap |
| [Utrecht Nederlander worden](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-nederlander-worden-door-naturalisatie-of-optie.md) | Gemeente Utrecht: Nederlander worden door naturalisatie of optie |
| [Wet justitiële en strafvorderlijke gegevens](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-justitiele-en-strafvorderlijke-gegevens-bwbr0014194.md) | Wet justitiële en strafvorderlijke gegevens |
| [Utrecht VOG aanvragen](../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verklaring-omtrent-het-gedrag-aanvragen-vog.md) | Gemeente Utrecht: Verklaring omtrent het gedrag (VOG) aanvragen |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Ketenpartner* (business-role). GEMMA-rol Ketenpartner (procesarchitectuur, actoren en rollen); zelfde begrip, in GEMMA zonder definitie. Nieuw: een definitie.

GEMMA-terugmeldingen:

- [Nummer 4](../../../modellen/gemma/terugmeldingen/gemma-team.md) (definitie, open): **GEMMA:** de rollen Ketenpartner, Adviseur en Beslisser in de procesarchitectuur hebben geen definitie ([2026-vng-gemma-2026-10-02](../../../modellen/gemma/bronduidingen/model/2026-vng-gemma-2026-10-02.md)). **Bevinding:** de wiki heeft deze drie rollen aan GEMMA gekoppeld en gebruikt ze in lijkbezorging en burgerzaken. De import vult dus de definities in. Via Beslisser hangen burgemeester, college en raad aan de processen; welk orgaan beslist, staat in de beschrijving van het proces. De definitie van Ketenpartner spreekt van een andere organisatie, terwijl in de wiki ook personen de rol vervullen, zoals de behandelende arts en de officier van justitie; de wiki kan die definitie nog verbreden. **Voorstel:** controleer de definities bij de import: Ketenpartner: verantwoordelijkheid van een andere organisatie voor haar deel van een keten die zij met de gemeente uitvoert; Adviseur: verantwoordelijkheid voor het geven van advies aan wie een besluit neemt; Beslisser: verantwoordelijkheid voor het nemen van het besluit in een proces.
