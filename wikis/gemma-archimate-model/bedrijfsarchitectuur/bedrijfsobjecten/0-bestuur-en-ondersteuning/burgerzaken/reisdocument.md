---
id: reisdocument
type: bedrijfsobject
archimate_type: business-object
status: kandidaat
naam: Reisdocument
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Document van het Koninkrijk op naam van een persoon waarmee hij kan reizen en zich kan identificeren, zoals een paspoort of identiteitskaart.
grondslag: ggm-entiteit
match:
  ggm: sterk
  gemma: sterk
data_object: ja
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2025-vng-upl-producten-en-diensten-extern
- 2025-rvig-logisch-ontwerp-brp-2025q1
- 2026-rvig-hup-reisdocument
ggm_entiteit: Reisdocument
ggm_guid: EAID_CA9BC1BB_D572_4e47_BECF_17CFD379BD6A
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: 99 Kern
ggm_diagram:
- Burgerzaken
- Detaillering subjecten op hoofdlijnen
- Detaillering subjecten met attributen
- Reidoscumentsoorten referenties
- mGBA
- INGESCHREVEN NATUURLIJK  PERSOON
- REISDOCUMENT
ggm_diagram_ids:
- EAID_D9511F60_3CA7_43bd_B6C8_F66447D66DBA
- EAID_BE50EA2F_917E_434f_91ED_0EB06CCBEFB6
- EAID_EB4053EE_18A5_4578_8973_7FD5967CDFC8
- EAID_8FDA2EB0_1359_493c_B72E_751468C6153C
- EAID_9A447DCF_183C_4efc_819F_1C5CD48D9F83
- EAID_D6979B1E_19B7_405d_A366_0F319815E0A0
- EAID_58363CF8_C242_4dca_8651_1DBB7B5D5BF7
ggm_definitie: Een document dat vereist is voor reizen naar het buitenland
gemma_id: id-07cb7da54dac4181839b23d677fefd4e
gemma_naam: Reisdocument
gemma_type: business-object
gemma_definitie: Een document dat vereist is voor reizen naar het buitenland
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  Bron: BRP
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-bd460a48-7720-465d-b12b-c15097ec620c
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{CA9BC1BB-D572-4e47-BECF-17CFD379BD6A}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: bd460a48-7720-465d-b12b-c15097ec620c
---

# Reisdocument

<!-- Gegenereerd door tools/render.py uit beoordelingen/begrippen/reisdocument.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: kandidaat.** Er staat een vraag open voor de redacteur (zie *Ter discussie*).

## Ter discussie

- geen proces bepaalt de levensloop van dit object (kernobject), en het is geen deel van een object of generiek

## Betekenis

### Definitie

Document van het Koninkrijk op naam van een persoon waarmee hij kan reizen en zich kan identificeren, zoals een paspoort of identiteitskaart.

### Beschrijving

De Paspoortwet kent onder meer het nationaal paspoort, het reisdocument voor vluchtelingen en voor vreemdelingen en het nooddocument; de Nederlandse identiteitskaart heeft een eigen wet maar valt voor vermissing, inhouding en signalering ook onder de Paspoortwet (Paspoortwet art. 1, 2). Het document blijft rijkseigendom (art. 2 lid 4). In de BRP staan de gegevens over Nederlandse reisdocumenten in categorie 12 van de persoonslijst (HUP Reisdocument; LO BRP 1.1: Nederlands paspoort of Nederlandse identiteitskaart). De processen rond reisdocumenten worden apart beoordeeld.

## Plaats in het model

### Typering

Bedrijfsobject. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, kernbegrip van de Paspoortwet en de UPL: paspoort, identiteitskaart en andere reisdocumenten (Paspoortwet art. 1, 2; UPL nr. 329, 186, 356). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de burgemeester neemt de aanvraag in ontvangst, verstrekt het reisdocument en reikt het uit (Paspoortwet art. 26, 40, 42). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken; geen ander onderwerp beoordeelt het. [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elk reisdocument heeft een documentnummer en een houder (Paspoortwet art. 1, 3). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, aanvraag, verstrekking, uitreiking, en verval of vervallenverklaring, inhouding of vermissing (Paspoortwet art. 1, 44, 47). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, de burgemeester verstrekt en reikt uit; de gemeente legt de gegevens over Nederlandse reisdocumenten vast in categorie 12 van de persoonslijst (Paspoortwet art. 40, 42; HUP Reisdocument). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Reisdocument](../../../../bronanalyses/burgerzaken/2026-rvig-hup-reisdocument.md) |
| **geautomatiseerd verwerkt**: Wordt het als gegevensstructuur geautomatiseerd verwerkt? | Ja, reisdocumentenadministratie, basisregister reisdocumenten en categorie 12 van de persoonslijst (Paspoortwet art. 3, 4c; LO BRP 4.4). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md), [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip in deze wiki; paspoort, identiteitskaart en de andere soorten zijn zijn specialisaties (Paspoortwet art. 2). [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) |

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Ingeschreven persoon](ingeschreven-persoon.md) | is houder van *associatie (gericht), 1 → 0..** | Reisdocument | [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md), [HUP Reisdocument](../../../../bronanalyses/burgerzaken/2026-rvig-hup-reisdocument.md) (LO 4.4, categorie 12; HUP Reisdocument); GGM (EAID_423300D3_B0CE_4c89_BA5F_84D7317DE876) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../../../bronanalyses/burgerzaken/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/2025-rvig-logisch-ontwerp-brp-2025q1.md) | Logisch Ontwerp BRP Versie 2025.Q1 |
| [HUP Reisdocument](../../../../bronanalyses/burgerzaken/2026-rvig-hup-reisdocument.md) | HUP BRP: Reisdocument |

### Afstemming met GGM

Match **sterk** met GGM-entiteit *Reisdocument* (beleidsdomein RSGBPlus, taakveld 99 Kern). GGM-entiteit Reisdocument (RSGBPlus): een document dat vereist is voor reizen naar het buitenland. Zelfde begrip; de attributen volgen categorie 12 van het LO BRP. De GGM-definitie noemt de identificatie en de houder niet; de wiki volgt de Paspoortwet (art. 1, 2).

> Een document dat vereist is voor reizen naar het buitenland

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Reisdocument* (business-object). GEMMA-bedrijfsobject Reisdocument, overgenomen uit het GGM (zelfde GGM-guid en definitie). Nieuw: een definitie volgens de Paspoortwet.

> Een document dat vereist is voor reizen naar het buitenland
