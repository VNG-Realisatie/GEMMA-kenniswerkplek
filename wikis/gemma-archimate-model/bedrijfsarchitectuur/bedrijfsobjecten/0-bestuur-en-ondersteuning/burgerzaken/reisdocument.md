---
id: reisdocument
type: bedrijfsobject
archimate_type: business-object
status: goedgekeurd
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
objectniveau: kernobject
bronnen:
- 2026-rijk-paspoortwet-bwbr0005212
- 2025-vng-upl-producten-en-diensten-extern
- 2025-rvig-logisch-ontwerp-brp-2025q1
- 2026-rvig-hup-reisdocument
- 2026-rvig-hup-uitreiking-registreren-van-een-reisdocument
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

**Status: goedgekeurd** door de redacteur.

## Betekenis

### Definitie

Document van het Koninkrijk op naam van een persoon waarmee hij kan reizen en zich kan identificeren, zoals een paspoort of identiteitskaart.

> Reisdocumenten van het Koninkrijk der Nederlanden zijn: nationaal paspoort; diplomatiek paspoort; dienstpaspoort; reisdocument voor vluchtelingen; reisdocument voor vreemdelingen; nooddocument: laissez-passer of noodpaspoort; andere reisdocumenten, bij of krachtens algemene maatregel van rijksbestuur vast te stellen.
>
> — [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), art. 1 onder p, art. 2 lid 1

### Beschrijving

De Paspoortwet kent het nationaal paspoort, het diplomatiek paspoort en het dienstpaspoort, het reisdocument voor vluchtelingen en voor vreemdelingen, het nooddocument en andere reisdocumenten (Paspoortwet art. 2). De Nederlandse identiteitskaart heeft een eigen wet en valt formeel niet onder het reisdocument van de Paspoortwet, maar de wet noemt haar bij vermissing, signalering en inhouding (art. 1 onder u, 4a, 25, 50b); in de BRP en in de praktijk is het reisdocument een Nederlands paspoort of een Nederlandse identiteitskaart (LO BRP 1.1; Utrecht). Dat is het verschil met de formele definitie.

Het document staat op naam van de houder, vermeldt zijn persoonsgegevens, gezichtsopname, vingerafdrukken en handtekening en blijft rijkseigendom (Paspoortwet art. 1 onder f, 2 lid 4, 3). Het is het kernobject van Beheren reisdocumenten: het ontstaat bij de verstrekking en eindigt door verval van rechtswege, vervallenverklaring of inhouding, waarna het definitief aan het verkeer wordt onttrokken (art. 1, 44, 47, 54). De uitreikende autoriteiten houden een reisdocumentenadministratie bij; de minister het basisregister reisdocumenten en het register vermiste of vervallen reisdocumenten (art. 3 lid 8, 4a, 4c).

In de BRP staan de gegevens over uitgereikte Nederlandse reisdocumenten en een signalering in categorie 12 van de persoonslijst; een nooddocument, diplomatiek paspoort, dienstpaspoort of buitenlands reisdocument wordt niet opgenomen (HUP Reisdocument; HUP Uitreiking; LO BRP 4.4).

## Plaats in het model

### Typering

Bedrijfsobject, niveau kernobject. Uitkomst van de beslistabel: Passief (kern ja, 2/2).

### Plaats in de indelingen

- **Objectniveau**: kernobject.
- **Levensloop bepaald door**: [Beheren reisdocumenten](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md).
- **Mutaties door bedrijfsprocessen**: [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md), [Behandelen aanvraag reisdocument niet-ingezetene](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument-niet-ingezetene.md), [Inhouden reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md), [Verwerken vermissing reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

Alleen de kenmerken met ja; de overige 51 zijn nee.

| Kenmerk | Onderbouwing |
|---|---|
| **herkenbaar**: Kennen domeinexperts dit als een eigen begrip, onder deze of een gangbare naam? | Ja, kernbegrip van de Paspoortwet en de UPL: paspoort, identiteitskaart en andere reisdocumenten (Paspoortwet art. 1, 2; UPL nr. 329, 186, 356). [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **gemeentelijk**: Ziet, doet of beslist de gemeente hierover; of werkt de gemeente structureel samen met deze partij (opdrachtgever, mede-eigenaar, prestatieafspraken, wettelijke overlegplicht)? | Ja, de burgemeester neemt de aanvraag in ontvangst, verstrekt het reisdocument en reikt het uit (Paspoortwet art. 26, 40, 42). [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **eigen identiteit**: Bestaat het los van één ander begrip, en is het meer dan een onderdeel, deelstap, processtap of handeling daarvan? | Ja, bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **betekenis in onderwerp**: Hoort het begrip primair bij dit onderwerp, het eerste in `onderwerpen` (het thuisonderwerp), en niet bij een ander onderwerp? | Ja, hoort primair bij burgerzaken: kernobject van Beheren reisdocumenten (UPL taakveld 0.2). [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, elk reisdocument heeft een documentnummer en een houder (Paspoortwet art. 1, 3). [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, aanvraag, verstrekking, uitreiking, wijziging, en verval van rechtswege, vervallenverklaring, inhouding of vermissing, tot definitieve onttrekking aan het verkeer (Paspoortwet art. 1, 44, 47, 54). [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, beheren reisdocumenten registreert, werkt bij en beëindigt het: de burgemeester verstrekt, reikt uit, houdt in en onttrekt aan het verkeer; de gemeente legt de gegevens over Nederlandse reisdocumenten vast in categorie 12 van de persoonslijst (Paspoortwet art. 40, 42, 54; HUP Reisdocument). [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Reisdocument](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-reisdocument.md) |
| **geautomatiseerd verwerkt**: Wordt het als gegevensstructuur geautomatiseerd verwerkt? | Ja, reisdocumentenadministratie, basisregister reisdocumenten en categorie 12 van de persoonslijst (Paspoortwet art. 3, 4c; LO BRP 4.4). [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **zelfstandige specialisatie**: Is dit een specialisatie van een breder begrip van hetzelfde type die de gemeente anders behandelt, met eigen gegevens, regels of werkwijze? | Ja, geen breder begrip in deze wiki; het nationaal paspoort, de Nederlandse identiteitskaart en de andere soorten zijn zijn specialisaties (Paspoortwet art. 1 onder u, 2; HUP Uitreiking). [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Uitreiking reisdocument](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md) |

### Specialisaties

- **Nationaal paspoort**: Voor iedere Nederlander, voor alle landen, tien jaar en tot achttien jaar vijf jaar geldig (Paspoortwet art. 9; Paspoortbesluit art. 2.2). Gangbaar: paspoort; ook als tweede paspoort (art. 30) en als zakenpaspoort met 66 bladzijden (Utrecht). Geen eigen pagina; de diensten Paspoort, Paspoort tweede en Zakenpaspoort leveren het. (ggm_attribuut soort)
- **Nederlandse identiteitskaart**: Identiteitsbewijs met een eigen wet, voor een deel van de landen als reisdocument te gebruiken (Paspoortwet art. 1 onder u; Utrecht). Geen eigen pagina; de dienst Identiteitskaart levert het. (ggm_attribuut soort)
- **Reisdocument voor vluchtelingen**: Voor een als vluchteling toegelaten vreemdeling, vijf jaar geldig (Paspoortwet art. 11). Gangbaar: vluchtelingenpaspoort. Geen eigen pagina. (ggm_attribuut soort)
- **Reisdocument voor vreemdelingen**: Voor een vreemdeling die geen eigen nationaal paspoort kan krijgen (Paspoortwet art. 12 tot en met 15). Gangbaar: vreemdelingenpaspoort. Geen eigen pagina. (ggm_attribuut soort)
- **Nooddocument**: Laissez-passer of noodpaspoort bij een reis die geen uitstel gedoogt (Paspoortwet art. 16; Paspoortbesluit art. 2.10). Geen gemeentelijk product: de Koninklijke Marechaussee neemt de aanvraag in ontvangst (Paspoortbesluit art. 3.5; Utrecht). Geen eigen pagina.
- **Faciliteitenpaspoort**: Voor een staatloze die op grond van de Wet betreffende de positie van Molukkers als Nederlander wordt behandeld; de burgemeester neemt de aanvraag in ontvangst (Paspoortbesluit art. 2.12, 3.1). Geen eigen pagina: de UPL noemt het niet apart.
- **Diplomatiek paspoort en dienstpaspoort**: Verstrekt door de minister van Buitenlandse Zaken, niet door de gemeente (Paspoortwet art. 10, 40 lid 2). Geen eigen pagina.

### Relaties

#### Uitgaand

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| Reisdocument | staat op naam van *associatie (gericht)* | [Ingeschreven persoon](ingeschreven-persoon.md) | [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [HUP Reisdocument](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-reisdocument.md) (Paspoortwet art. 1 onder f, 26; HUP Reisdocument) |

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md) | verstrekt *toegang (registreren)* | Reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1 onder d, 40) |
| [Behandelen aanvraag reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument.md) | reikt uit *toegang (bijwerken)* | Reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1 onder e, 42) |
| [Behandelen aanvraag reisdocument niet-ingezetene](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/behandelen-aanvraag-reisdocument-niet-ingezetene.md) | verstrekt *toegang (registreren)* | Reisdocument | [Paspoortbesluit](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (art. 4.2) |
| [Beheren reisdocumenten](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/beheren-reisdocumenten.md) | verstrekt, reikt uit en onttrekt aan het verkeer *toegang (registreren)* | Reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1, 40, 42, 54) |
| [Houder van het reisdocument](../../../rollen/houder-van-het-reisdocument.md) | is houder van *toegang (houder)* | Reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (art. 1 onder f) |
| [Ingeschreven persoon](ingeschreven-persoon.md) | is houder van *associatie (gericht), 1 → 0..** | Reisdocument | [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md), [HUP Reisdocument](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-reisdocument.md), [Besluit BRP](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-besluit-brp-bwbr0034306.md), [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (LO 4.4, categorie 12; HUP Reisdocument; Besluit BRP bijlage 1 (gegevens omtrent het reisdocument); Paspoortwet art. 1 onder f (houder)); GGM (EAID_423300D3_B0CE_4c89_BA5F_84D7317DE876) |
| [Inhouden reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inhouden-reisdocument.md) | houdt in en onttrekt aan het verkeer, verklaart vervallen *toegang (beëindigen)* | Reisdocument | [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), [Paspoortbesluit](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortbesluit-bwbr0044308.md) (Paspoortwet art. 1 onder h en j, 54; Paspoortbesluit art. 7.1; art. 1 onder i, 44) |
| [Verwerken vermissing reisdocument](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-vermissing-reisdocument.md) | registreert vermissing van *toegang (bijwerken)* | Reisdocument | [HUP Inhouding, inlevering of vermissing](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-inhouding-inlevering-vermissing.md), [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) (HUP Inhouding, inleiding; Paspoortwet art. 47 lid 1 onder j) |

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Paspoortwet](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md) | Paspoortwet |
| [UPL-lijst extern](../../../../bronanalyses/burgerzaken/informatiemodel/2025-vng-upl-producten-en-diensten-extern.md) | Standaard producten en dienstenlijst extern basis UPL |
| [Logisch Ontwerp BRP 2025.Q1](../../../../bronanalyses/burgerzaken/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md) | Logisch Ontwerp BRP Versie 2025.Q1 |
| [HUP Reisdocument](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-reisdocument.md) | HUP BRP: Reisdocument |
| [HUP Uitreiking reisdocument](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-uitreiking-registreren-van-een-reisdocument.md) | HUP BRP: Uitreiking registreren van een reisdocument |

### Afstemming met GGM

Match **sterk** met GGM-entiteit *Reisdocument* (beleidsdomein RSGBPlus, taakveld 99 Kern). GGM-entiteit Reisdocument (RSGBPlus): een document dat vereist is voor reizen naar het buitenland. Zelfde begrip; de attributen volgen categorie 12 van het LO BRP. De GGM-definitie noemt de identificatie en de houder niet en het GGM kent de signalering niet; de wiki volgt de Paspoortwet (art. 1, 2). GGM-terugmelding 14.

> Een document dat vereist is voor reizen naar het buitenland

GGM-terugmeldingen:

- [Nummer 14](../../../../analyses/ggm-terugmeldingen.md) (definitie, open): **GGM:** Reisdocument is een document dat vereist is voor reizen naar het buitenland; de attributen volgen categorie 12 van de BRP (soort, nummer, uitgifte, autoriteit, geldigheid, inhouding of vermissing). **Bevinding:** de definitie noemt de houder en de identificatie niet, en ook een Nederlandse identiteitskaart is een reisdocument in de BRP en de praktijk ([2025-rvig-logisch-ontwerp-brp-2025q1](../../../../bronanalyses/burgerzaken/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md), 1.1; [2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen](../../../../bronanalyses/burgerzaken/overig/2026-utrecht-burgerzaken-paspoort-of-identiteitskaart-aanvragen.md)). De Paspoortwet maakt het document op naam van de houder en rijkseigendom ([2026-rijk-paspoortwet-bwbr0005212](../../../../bronanalyses/burgerzaken/rijksregelgeving/2026-rijk-paspoortwet-bwbr0005212.md), art. 1 onder f, 2 lid 4). Categorie 12 bevat naast het Nederlands reisdocument ook de signalering (groep 36), die het GGM niet kent ([2025-rvig-logisch-ontwerp-brp-2025q1](../../../../bronanalyses/burgerzaken/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md), 4.4; [2026-rvig-hup-signalering-verstrekking-reisdocument](../../../../bronanalyses/burgerzaken/richtlijn/2026-rvig-hup-signalering-verstrekking-reisdocument.md)). **Voorstel:** de definitie aanpassen: een document van het Koninkrijk op naam van een persoon waarmee hij kan reizen en zich kan identificeren, zoals een paspoort of identiteitskaart. Daarnaast de signalering opnemen, als attribuut van de ingeschreven persoon (verstrekkingsbelemmering) of als eigen groep, met ingangsdatum en verwijdering.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Reisdocument* (business-object). GEMMA-bedrijfsobject Reisdocument, overgenomen uit het GGM (zelfde GGM-guid en definitie). Nieuw: een definitie volgens de Paspoortwet.

> Een document dat vereist is voor reizen naar het buitenland
