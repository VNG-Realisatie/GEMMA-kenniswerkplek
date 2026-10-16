---
id: kiezer
type: rol
archimate_type: business-role
status: goedgekeurd
naam: Kiezer
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Hoedanigheid van wie kiesgerechtigd en als kiezer geregistreerd is en bij een verkiezing mag stemmen.
match:
  gemma: exact
data_object: nee
doelgroep: inwoners en ondernemers
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2026-rvig-hup-europees-kiesrecht
gemma_id: id-d649e10e-d9a6-4ac7-b436-2d659cb4fdbf
gemma_naam: Kiezer
gemma_type: business-role
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: d649e10e-d9a6-4ac7-b436-2d659cb4fdbf
---

# Kiezer

<!-- Gegenereerd door tools/render.py uit de beoordeling kiezer.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Hoedanigheid van wie kiesgerechtigd en als kiezer geregistreerd is en bij een verkiezing mag stemmen.

### Beschrijving

De kiezer ontvangt een stempas, kan een nieuwe stempas of een kiezerspas aanvragen en kan een andere kiezer machtigen om voor hem te stemmen; als volmachtgever wijst hij zelf een gemachtigde aan, die zelf als kiezer moet zijn geregistreerd (Kieswet art. J 7, J 8, K 3, L 2, L 8). GEMMA kent de rol Kiezer onder de rol Klant.

## Plaats in het model

### Typering

Rol. Uitkomst van de beslistabel: Hoedanigheid (kern ja).

### Plaats in de indelingen

- **Doelgroep**: inwoners en ondernemers.
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, actief, intern (Actor, Rol, Bedrijfssamenwerking). **Hoofdkenmerk**: hoedanigheid. De poort is doorlopen (herkenbaar, gemeentelijk, eigen identiteit, betekenis in dit onderwerp); dat steunt op de bronnen onder Herkomst.

De kenmerken met ja; de andere zijn nee, behalve *zelfstandige specialisatie* (standaard ja).

| Kenmerk | Onderbouwing |
|---|---|
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, met [Verstrekken stempas](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-stempas.md), [Behandelen verzoek om kiezerspas](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-kiezerspas.md), [Behandelen verzoek om volmacht](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-volmacht.md), [Registreren kiesgerechtigdheid](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md). |

### Specialisaties

- **Volmachtgever**: De kiezer die een andere kiezer machtigt om voor hem te stemmen (Kieswet art. L 2). Geen eigen pagina.
- **Gemachtigde**: De kiezer die namens een volmachtgever stemt, met hoogstens twee volmachten per verkiezing (Kieswet art. L 2, L 4, L 8). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Kiezer | ontvangt de stempas en vraagt een nieuwe aan *toewijzing* | [Verstrekken stempas](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-stempas.md) | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2, J 8) |
| Kiezer | vraagt de kiezerspas aan *toewijzing* | [Behandelen verzoek om kiezerspas](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-kiezerspas.md) | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 3) |
| Kiezer | dient het verzoekschrift in *toewijzing* | [Behandelen verzoek om volmacht](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-volmacht.md) | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 8) |
| Kiezer | verzoekt om mededeling of registratie *toewijzing* | [Registreren kiesgerechtigdheid](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md) | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) (Kieswet art. D 5; HUP Europees kiesrecht) |
| Kiezer | ontvangt *toegang (houder)* | [Stempas](../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Kiezerspas](../diensten/0-bestuur-en-ondersteuning/burgerzaken/kiezerspas.md) | bedient *bediening* | Kiezer | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 3) |
| [Stempas ontvangen](../diensten/0-bestuur-en-ondersteuning/burgerzaken/stempas-ontvangen.md) | bedient *bediening* | Kiezer | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2) |
| [Stemrecht](../diensten/0-bestuur-en-ondersteuning/burgerzaken/stemrecht.md) | bedient *bediening* | Kiezer | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. D 5) |
| [Volmachtbewijs verkiezingen](../diensten/0-bestuur-en-ondersteuning/burgerzaken/volmachtbewijs-verkiezingen.md) | bedient *bediening* | Kiezer | [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 8) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [HUP Europees kiesrecht](../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-europees-kiesrecht.md) | HUP BRP: Europees kiesrecht |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Kiezer* (business-role). GEMMA-rol Kiezer (procesarchitectuur, actoren en rollen), geaggregeerd door Klant; zelfde begrip, in GEMMA zonder definitie. Nieuw: een definitie.

GEMMA-terugmeldingen:

- [Nummer 2](../../../modellen/gemma/terugmeldingen/gemma-team.md) (definitie, open): **GEMMA:** de rol Kiezer en de actoren Gemeenteraad, College en Rijk hebben geen definitie ([2026-vng-gemma-2026-10-02](../../../modellen/gemma/bronduidingen/model/2026-vng-gemma-2026-10-02.md)). Rijk heeft ook geen relaties. **Bevinding:** de wiki heeft deze vier elementen aan GEMMA gekoppeld. De import vult dus de definities in en hernoemt College naar College van B&W, want "College" kan meerdere organen bedoelen. **Voorstel:** controleer de definities en de nieuwe naam bij de import: Kiezer: wie kiesgerechtigd en als kiezer geregistreerd is en bij een verkiezing mag stemmen; Gemeenteraad: het bestuursorgaan dat de bevolking vertegenwoordigt en de gemeentelijke verordeningen vaststelt; College van B&W: het dagelijks bestuur, de burgemeester en de wethouders; Rijk: de Staat der Nederlanden als bestuurslaag, met zijn ministers en rijksdiensten, en de relaties daarvan.
