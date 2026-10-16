---
id: belanghebbende
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Belanghebbende
onderwerpen:
- besluitvorming
- lijkbezorging
- participatie
definitie: Hoedanigheid van degene wiens belang rechtstreeks bij een besluit van een bestuursorgaan is betrokken.
match:
  gemma: sterk
doelgroep: inwoners en ondernemers
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2010-vng-model-beheersverordening-begraafplaatsen
gemma_id: id-bd369f13-44a4-41f0-8b95-7925a0c0eaa9
gemma_naam: Belanghebbende
gemma_type: business-role
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: bd369f13-44a4-41f0-8b95-7925a0c0eaa9
---

# Belanghebbende

<!-- Gegenereerd door tools/render.py uit de beoordeling belanghebbende.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Hoedanigheid van degene wiens belang rechtstreeks bij een besluit van een bestuursorgaan is betrokken.

### Beschrijving

Belanghebbende is degene wiens belang rechtstreeks bij een besluit is betrokken (Awb art. 1:2 lid 1). Dat kan een inwoner of onderneming zijn, maar ook een bestuursorgaan voor de belangen die het zijn toevertrouwd en een rechtspersoon voor de algemene en collectieve belangen die het behartigt (art. 1:2 lid 2 en 3). Een belanghebbende kan een besluit aanvragen (art. 1:3 lid 3) en zijn zienswijze over een ontwerpbesluit naar voren brengen (art. 3:15).

### Per onderwerp

#### [Lijkbezorging](../../../onderwerpen/lijkbezorging/begrippen.md)

De belanghebbende bij een algemeen graf, meestal een nabestaande, krijgt van de houder van de begraafplaats bericht van het verstrijken van de termijn van uitgifte en van het voornemen tot ruiming (Wlb art. 27a; VNG-modelverordening art. 24 lid 1). Bij een particulier graf heeft de rechthebbende die positie.

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Uitvoeren uniforme openbare voorbereidingsprocedure](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md), [Ruimen graf](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/ruimen-graf.md), [Behandelen bezwaar](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-bezwaar.md), [Voeren verweer in beroep](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/voeren-verweer-in-beroep.md), [Vaststellen dwangsom bij niet tijdig beslissen](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/vaststellen-dwangsom-bij-niet-tijdig-beslissen.md), [Behandelen aanvraag nadeelcompensatie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-aanvraag-nadeelcompensatie.md), [Behandelen aanvraag beschikking](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-aanvraag-beschikking.md). |

### Specialisaties

- **Aanvrager**: Belanghebbende die een aanvraag indient en de gegevens en bescheiden verschaft (Awb art. 1:3 lid 3, 4:2). Geen eigen pagina; in een onderwerp heet de rol naar het object, zoals Houder van het reisdocument.
- **Belanghebbende bij een algemeen graf**: Nabestaande die bericht krijgt van het verstrijken van de termijn van uitgifte en van de ruiming (Wlb art. 27a; VNG-modelverordening art. 24). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Belanghebbende | brengt een zienswijze naar voren *toewijzing* | [Uitvoeren uniforme openbare voorbereidingsprocedure](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md) | [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 3:15) |
| Belanghebbende | ontvangt bericht van de ruiming (bij een algemeen graf) *toewijzing* | [Ruimen graf](../bedrijfsprocessen/7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/ruimen-graf.md) | [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md), [VNG Model-beheersverordening begraafplaatsen](../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) (Wlb art. 27a; VNG-modelverordening art. 24 lid 1) |
| Belanghebbende | maakt bezwaar en wordt gehoord *toewijzing* | [Behandelen bezwaar](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-bezwaar.md) | [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 6:4, 7:2) |
| Belanghebbende | stelt beroep in *toewijzing* | [Voeren verweer in beroep](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/voeren-verweer-in-beroep.md) | [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 8:1) |
| Belanghebbende | stelt als aanvrager in gebreke *toewijzing* | [Vaststellen dwangsom bij niet tijdig beslissen](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/vaststellen-dwangsom-bij-niet-tijdig-beslissen.md) | [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:17 lid 3, 5) |
| Belanghebbende | vraagt als benadeelde de vergoeding aan *toewijzing* | [Behandelen aanvraag nadeelcompensatie](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-aanvraag-nadeelcompensatie.md) | [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 4:126, 4:127) |
| Belanghebbende | vraagt de beschikking aan of geeft als derde zijn zienswijze *toewijzing* | [Behandelen aanvraag beschikking](../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-aanvraag-beschikking.md) | [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 1:3 lid 3, 4:7, 4:8) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [Wet op de lijkbezorging](../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |
| [VNG Model-beheersverordening begraafplaatsen](../../../onderwerpen/lijkbezorging/bronduidingen/gemeentelijke-regelgeving/2010-vng-model-beheersverordening-begraafplaatsen.md) | Model-beheersverordening begraafplaatsen 2010 (VNG), met toelichting |

### Afstemming met GGM

GGM-terugmeldingen:

- [Nummer 9](../../../modellen/ggm/terugmeldingen.md) (scope, open): **GGM:** Belanghebbende (definitie gelijk aan art. 1:2 Awb) staat alleen in het beleidsdomein Musea. **Bevinding:** het is een algemeen begrip uit het bestuursrecht. **Voorstel:** onderbrengen in een algemeen beleidsdomein (bijvoorbeeld Kern of Besluitvorming), zodat alle beleidsdomeinen ernaar kunnen verwijzen.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Belanghebbende* (business-role). GEMMA-rol Belanghebbende uit de procesbouwstenen; zelfde begrip, in GEMMA zonder definitie. Nieuw: een definitie volgens de Awb. Het GEMMA-bedrijfsobject Belanghebbende (groepering Museum, uit het GGM) is de gegevensentiteit, geen rol.

### Besluiten redacteur

- 2026-10-11: Aanvrager (Awb art. 1:3 lid 3, 4:2) is een specialisatie zonder pagina; in een onderwerp heet de rol naar het object, zoals Houder van het reisdocument. *Zekerheid: logica.*
