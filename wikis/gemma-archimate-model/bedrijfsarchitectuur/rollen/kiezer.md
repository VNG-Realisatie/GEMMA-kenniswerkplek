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
grondslag: bron
match:
  gemma: exact
data_object: nee
doelgroep: inwoners en ondernemers
bronnen:
- 2026-rijk-kieswet-bwbr0004627
- 2026-vng-gemma-2026-10-02
- 2026-rvig-hup-europees-kiesrecht
gemma_id: id-d649e10e-d9a6-4ac7-b436-2d659cb4fdbf
gemma_naam: Kiezer
gemma_type: business-role
gemma_map: Business / Procesarchitectuur / Actoren en rollen
gemma_eigenschappen:
  Object ID: d649e10e-d9a6-4ac7-b436-2d659cb4fdbf
---

# Kiezer

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/kiezer.yaml. Wijzig de beoordeling, niet deze pagina. -->

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

Alleen de kenmerken met ja; de overige 53 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, wetsbegrip (Kieswet art. J 7, K 1, L 1) en GEMMA-rol Kiezer. [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, ontvangt de stempas van de burgemeester en richt verzoeken aan hem (Kieswet art. J 7, J 8, K 3, L 8). [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, een eigen hoedanigheid. [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort bij burgerzaken: de rol voert gedrag uit in Beheren stempassen en Registreren kiesgerechtigdheid. [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **hoedanigheid**: Is het een verantwoordelijkheid voor specifiek gedrag waaraan een partij kan worden toegewezen, of de hoedanigheid waarin een partij optreedt? | Ja, de hoedanigheid van wie kiesgerechtigd is en als kiezer is geregistreerd (Kieswet art. D 1, J 7). [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **voert gedrag uit**: Is de rol of het verband aanwijsbaar toegewezen aan een gemeentelijk proces of een functie? | Ja, toegewezen aan Verstrekken stempas, Behandelen verzoek om kiezerspas, Behandelen verzoek om volmacht en Registreren kiesgerechtigdheid (Kieswet art. J 8, K 3, L 8, D 5). [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip in deze wiki; in GEMMA een specialisatie van Klant. [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md) |

### Specialisaties

- **Volmachtgever**: De kiezer die een andere kiezer machtigt om voor hem te stemmen (Kieswet art. L 2). Geen eigen pagina.
- **Gemachtigde**: De kiezer die namens een volmachtgever stemt, met hoogstens twee volmachten per verkiezing (Kieswet art. L 2, L 4, L 8). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Kiezer | ontvangt de stempas en vraagt een nieuwe aan *toewijzing* | [Verstrekken stempas](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verstrekken-stempas.md) | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2, J 8) |
| Kiezer | vraagt de kiezerspas aan *toewijzing* | [Behandelen verzoek om kiezerspas](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-kiezerspas.md) | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 3) |
| Kiezer | dient het verzoekschrift in *toewijzing* | [Behandelen verzoek om volmacht](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-verzoek-om-volmacht.md) | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 8) |
| Kiezer | verzoekt om mededeling of registratie *toewijzing* | [Registreren kiesgerechtigdheid](../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/registreren-kiesgerechtigdheid.md) | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md), [HUP Europees kiesrecht](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-europees-kiesrecht.md) (Kieswet art. D 5; HUP Europees kiesrecht) |
| Kiezer | ontvangt *toegang (houder)* | [Stempas](../bedrijfsobjecten/0-bestuur-en-ondersteuning/burgerzaken/stempas.md) | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Kiezerspas](../diensten/0-bestuur-en-ondersteuning/burgerzaken/kiezerspas.md) | bedient *bediening* | Kiezer | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. K 3) |
| [Stempas ontvangen](../diensten/0-bestuur-en-ondersteuning/burgerzaken/stempas-ontvangen.md) | bedient *bediening* | Kiezer | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. J 7 lid 2) |
| [Stemrecht](../diensten/0-bestuur-en-ondersteuning/burgerzaken/stemrecht.md) | bedient *bediening* | Kiezer | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. D 5) |
| [Volmachtbewijs verkiezingen](../diensten/0-bestuur-en-ondersteuning/burgerzaken/volmachtbewijs-verkiezingen.md) | bedient *bediening* | Kiezer | [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) (art. L 8) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Kieswet](../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-kieswet-bwbr0004627.md) | Kieswet |
| [GEMMA](../../../../sources/raw/2026-vng-gemma-2026-10-02.md) | GEMMA-architectuurmodel |
| [HUP Europees kiesrecht](../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-europees-kiesrecht.md) | HUP BRP: Europees kiesrecht |

### Afstemming met GEMMA

Match **exact** met GEMMA-element *Kiezer* (business-role). GEMMA-rol Kiezer (procesarchitectuur, actoren en rollen), geaggregeerd door Klant; zelfde begrip, in GEMMA zonder definitie. Nieuw: een definitie.

GEMMA-terugmeldingen:

- [Nummer 2](../../analyses/gemma-terugmeldingen.md) (definitie, open): **GEMMA:** de rol Kiezer en de actoren Gemeenteraad, College en Rijk (Procesarchitectuur, Actoren en rollen) hebben geen definitie ([2026-vng-gemma-2026-10-02](../../../../sources/raw/2026-vng-gemma-2026-10-02.md)). Rijk heeft ook geen relaties. **Bevinding:** zonder definitie is niet te zien wat de elementen omvatten. Kiezer is een hoedanigheid (Kieswet art. D 1), de Gemeenteraad vertegenwoordigt de gehele bevolking (Gemeentewet art. 7), het College bestaat uit de burgemeester en de wethouders (Gemeentewet art. 34) en het Rijk is de Staat der Nederlanden als bestuurslaag. De naam College is bovendien niet eenduidig: de wiki noemt het element College van B&W. De wiki-elementen zijn gekoppeld aan deze GEMMA-elementen (exacte match), dus de import van het wiki-model werkt ze bij: de definities komen uit de wiki, en de naam College wordt College van B&W. **Voorstel:** controleer bij de import de definities die de wiki aan GEMMA toevoegt: Kiezer, "hoedanigheid van wie kiesgerechtigd en als kiezer geregistreerd is en bij een verkiezing mag stemmen"; Gemeenteraad, "bestuursorgaan van de gemeente dat de gehele bevolking vertegenwoordigt en de gemeentelijke verordeningen vaststelt"; College (nieuwe naam College van B&W), "dagelijks bestuur van de gemeente, bestaande uit de burgemeester en de wethouders"; Rijk, "de Staat der Nederlanden als bestuurslaag, die met zijn ministers en rijksdiensten wettelijke taken uitvoert waarmee elke gemeente te maken heeft". Laat het GEMMA-team beslissen of de naam College van B&W en de relaties van het Rijk zo in GEMMA komen.
