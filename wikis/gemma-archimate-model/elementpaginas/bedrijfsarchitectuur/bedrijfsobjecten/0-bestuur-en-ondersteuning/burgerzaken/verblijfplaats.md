---
id: verblijfplaats
type: bedrijfsobject
archimate_type: business-object
status: review
naam: Verblijfplaats
onderwerpen:
- burgerzaken
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Burgerzaken
definitie: Het adres waar een ingeschreven persoon woont of, zonder woonadres, zijn post ontvangt, met de periode waarin dat adres geldt.
match:
  ggm: exact
  gemma: partieel
data_objecten:
- Verblijfplaats-data
objectniveau: subobject
synoniemen:
- VerblijfadresIngeschrevenPersoon (GGM)
bronnen:
- 2026-rvig-hup-verblijfplaats
- 2025-rvig-logisch-ontwerp-brp-2025q1
- 2026-utrecht-burgerzaken-verhuizing-doorgeven
- 2026-rvig-hup-binnengemeentelijke-adreswijziging
- 2026-rvig-hup-intergemeentelijke-adreswijziging
- 2026-rvig-hup-emigratie
- 2023-rvig-circulaire-adresonderzoek-brp
ggm_entiteit: VerblijfadresIngeschrevenPersoon
ggm_guid: EAID_F6DAC299_3F19_45c6_BFFE_EB38C1C51459
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: 99 Kern
ggm_definitie: De gegevens over het verblijf en adres van de INGESCHREVEN PERSOON
gemma_id: id-9a240ef1e16e476887b3c67526facb98
gemma_naam: Verblijfplaats
gemma_type: business-object
gemma_definitie: Een verblijfplaats is de locatie waar een persoon feitelijk woont of verblijft, ongeacht of dit permanent of tijdelijk is. Het kan een huis, appartement, kamer, opvanglocatie of andere woonruimte zijn, en wordt vaak gebruikt om iemands woonadres aan te duiden voor juridische, administratieve of sociale doeleinden. De verblijfplaats is doorgaans bepalend voor het ontvangen van voorzieningen, het uitoefenen van rechten, en het voldoen aan verplichtingen binnen een specifieke jurisdictie of gemeenschap.
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-397f0d07-8500-40ea-9d3a-a142dc9a94f9
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{0028CB85-5EF0-45aa-A06F-4A8F14E71AB8}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: 397f0d07-8500-40ea-9d3a-a142dc9a94f9
---

# Verblijfplaats

<!-- Gegenereerd door tools/render.py uit de beoordeling verblijfplaats.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Het adres waar een ingeschreven persoon woont of, zonder woonadres, zijn post ontvangt, met de periode waarin dat adres geldt.

### Beschrijving

De verblijfplaats is een woonadres of een briefadres (HUP Verblijfplaats). Een woonadres is het adres waar iemand woont, in een woning of op een vaste stand- of ligplaats; bij wisselend verblijf het adres waar hij in een half jaar de meeste malen overnacht. Wie geen woonadres heeft, wordt ingeschreven op een briefadres. Het actuele adres in de BRP verwijst sinds 1 januari 2024 verplicht naar een adres in de BAG (HUP Verblijfplaats).

De verblijfplaats verandert bij een verhuizing binnen of naar de gemeente, bij emigratie en na een adresonderzoek (HUP Binnengemeentelijke en Intergemeentelijke adreswijziging; Circulaire adresonderzoek). Na emigratie heeft een niet-ingezetene een adres in het buitenland.

### Synoniemen

| Synoniem | Context |
|---|---|
| VerblijfadresIngeschrevenPersoon | GGM |

## Plaats in het model

### Typering

Bedrijfsobject, niveau subobject. Uitkomst van de beslistabel: Passief, object (3 toetskenmerken ja).

### Plaats in de indelingen

- **Objectniveau**: subobject.
- **Subobject van**: [Ingeschreven persoon](ingeschreven-persoon.md).
- **Mutaties door bedrijfsprocessen**: [Uitvoeren adresonderzoek](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitvoeren-adresonderzoek.md), [Verwerken adreswijziging](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Burgerzaken.

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: object.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: onderdeel | Een groep gegevens van de ingeschreven persoon (categorie 08 op de persoonslijst); bestaat niet zonder die persoon (LO BRP 4.4). [Logisch Ontwerp BRP 2025.Q1](../../../../../onderwerpen/burgerzaken/bronduidingen/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Inschrijven ingezetene](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md), [Uitvoeren adresonderzoek](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitvoeren-adresonderzoek.md), [Verwerken adreswijziging](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md). [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Logisch Ontwerp BRP 2025.Q1](../../../../../onderwerpen/burgerzaken/bronduidingen/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md), [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, standaard. [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Logisch Ontwerp BRP 2025.Q1](../../../../../onderwerpen/burgerzaken/bronduidingen/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md), [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, standaard. [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [Logisch Ontwerp BRP 2025.Q1](../../../../../onderwerpen/burgerzaken/bronduidingen/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md), [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md), [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md), [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md), [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) |

### Specialisaties

- **Woonadres**: Adres waar de ingeschreven persoon woont (functie adres W; HUP Verblijfplaats). Geen eigen pagina: het gewone geval van de verblijfplaats.
- **[Briefadres](briefadres.md)**: Adres waar post voor iemand zonder woonadres in ontvangst wordt genomen (HUP Verblijfplaats).
- **Verblijf in het buitenland**: Adres in het buitenland van een niet-ingezetene, door te geven via MyRNI (Utrecht Emigratie doorgeven). Geen eigen pagina. (ggm_guid EAID_E3567219_5744_4b70_901D_BAEBD8FF4947)

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Briefadres](briefadres.md) | is een *specialisatie* | Verblijfplaats | [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md), [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (HUP Verblijfplaats, functie adres B; Wet BRP art. 1.1 (adres)) |
| [Ingeschreven persoon](ingeschreven-persoon.md) | heeft *compositie* | Verblijfplaats | [Logisch Ontwerp BRP 2025.Q1](../../../../../onderwerpen/burgerzaken/bronduidingen/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (4.4, categorie 08 Verblijfplaats; Wet BRP art. 2.7 lid 1 onder a 7°) |
| [Inschrijven ingezetene](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/inschrijven-ingezetene.md) | legt vast *toegang (registreren)* | Verblijfplaats | [HUP Immigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-immigratie.md) (Stap 5) |
| [Uitvoeren adresonderzoek](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/uitvoeren-adresonderzoek.md) | verbetert *toegang (bijwerken)* | Verblijfplaats | [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) (4.8) |
| [Verwerken adreswijziging](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/burgerzaken/verwerken-adreswijziging.md) | legt vast *toegang (bijwerken)* | Verblijfplaats | [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md), [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (inleiding; Wet BRP art. 2.20 lid 1) |
| [Wet basisregistratie personen](../../../../motivatie/beleidskaders/rijksregelgeving/wet-basisregistratie-personen.md) | is grondslag voor *associatie (gericht)* | Verblijfplaats | [Wet BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/rijksregelgeving/2026-rijk-wet-brp-bwbr0033715.md) (art. 1.1 onder o, p, q, 2.7 lid 1, 2.20, 2.39) |

### Data-objecten

- [Verblijfplaats-data](../../../../applicatiearchitectuur/data-objecten/verblijfplaats-data.md) *realisatie*: GGM-entiteit *VerblijfadresIngeschrevenPersoon*, match exact.

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [HUP Verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md) | HUP BRP: Verblijfplaats |
| [Logisch Ontwerp BRP 2025.Q1](../../../../../onderwerpen/burgerzaken/bronduidingen/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md) | Logisch Ontwerp BRP Versie 2025.Q1 |
| [Utrecht Verhuizing doorgeven](../../../../../onderwerpen/burgerzaken/bronduidingen/overig/2026-utrecht-burgerzaken-verhuizing-doorgeven.md) | Gemeente Utrecht: Verhuizing doorgeven |
| [HUP Binnengemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-binnengemeentelijke-adreswijziging.md) | HUP BRP: Binnengemeentelijke adreswijziging |
| [HUP Intergemeentelijke adreswijziging](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-intergemeentelijke-adreswijziging.md) | HUP BRP: Intergemeentelijke adreswijziging |
| [HUP Emigratie](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-emigratie.md) | HUP BRP: Emigratie |
| [RvIG Circulaire adresonderzoek BRP](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2023-rvig-circulaire-adresonderzoek-brp.md) | Circulaire adresonderzoek BRP |

### Afstemming met GGM

Match **exact** met GGM-entiteit *VerblijfadresIngeschrevenPersoon* (beleidsdomein RSGBPlus, taakveld 99 Kern). GGM-entiteit VerblijfadresIngeschrevenPersoon (RSGBPlus): de gegevens over het verblijf en adres van de ingeschreven persoon, gelijk aan categorie 08 van het LO BRP.

> De gegevens over het verblijf en adres van de INGESCHREVEN PERSOON

Duplicaten in het GGM:

| Entiteit | Toelichting |
|---|---|
| VerblijfadresIngeschrevenNatuurlijkPersoon (RSGBPlus) | VerblijfadresIngeschrevenNatuurlijkPersoon, zelfde definitie bij de ingeschreven natuurlijk persoon; de primaire GUID volgt de match van Ingeschreven persoon (IngeschrevenPersoon). |

GGM-terugmeldingen:

- [Nummer 13](../../../../../modellen/ggm/terugmeldingen.md) (duplicaat, open): **GGM:** de gegevens over het verblijf en adres staan twee keer in RSGBPlus, met dezelfde definitie: VerblijfadresIngeschrevenPersoon (EAID_F6DAC299_3F19_45c6_BFFE_EB38C1C51459); VerblijfadresIngeschrevenNatuurlijkPersoon (EAID_E5E010C2_C1F3_4986_AA9A_C71C19263606). **Bevinding:** de BRP kent één categorie Verblijfplaats van de ingeschreven persoon ([2025-rvig-logisch-ontwerp-brp-2025q1](../../../../../onderwerpen/burgerzaken/bronduidingen/informatiemodel/2025-rvig-logisch-ontwerp-brp-2025q1.md), 4.4); de entiteit IngeschrevenNatuurlijkPersoon bestaat niet meer in het GGM. **Voorstel:** samenvoegen tot VerblijfadresIngeschrevenPersoon.

### Afstemming met GEMMA

Match **partieel** met GEMMA-element *Verblijfplaats* (business-object). GEMMA-bedrijfsobject Verblijfplaats: de locatie waar een persoon feitelijk woont of verblijft. Dat dekt het woonadres, niet het briefadres en de periode van adreshouding uit de BRP. De GGM-guid van het GEMMA-element komt in het huidige GGM niet meer voor. Bij koppelen krijgt het GEMMA-element de definitie uit de wiki.

> Een verblijfplaats is de locatie waar een persoon feitelijk woont of verblijft, ongeacht of dit permanent of tijdelijk is. Het kan een huis, appartement, kamer, opvanglocatie of andere woonruimte zijn, en wordt vaak gebruikt om iemands woonadres aan te duiden voor juridische, administratieve of sociale doeleinden. De verblijfplaats is doorgaans bepalend voor het ontvangen van voorzieningen, het uitoefenen van rechten, en het voldoen aan verplichtingen binnen een specifieke jurisdictie of gemeenschap.

GEMMA-terugmeldingen:

- [Nummer 3](../../../../../modellen/gemma/terugmeldingen/gemma-team.md) (definitie, open): **GEMMA:** Verblijfplaats is "de locatie waar een persoon feitelijk woont of verblijft" ([2026-vng-gemma-2026-10-02](../../../../../modellen/gemma/bronduidingen/model/2026-vng-gemma-2026-10-02.md)). **Bevinding:** dat past niet bij de BRP, waar de verblijfplaats het woonadres of het briefadres is, met de periode dat het adres geldt ([2026-rvig-hup-verblijfplaats](../../../../../onderwerpen/burgerzaken/bronduidingen/richtlijn/2026-rvig-hup-verblijfplaats.md)). De import vervangt de definitie door die van de wiki. De GGM-guid in GEMMA verwijst bovendien naar een entiteit die niet meer bestaat; die heet nu VerblijfadresIngeschrevenPersoon (GGM-terugmelding 13). **Voorstel:** neem de definitie van de wiki over: het adres waar een ingeschreven persoon woont of, zonder woonadres, zijn post ontvangt, met de periode waarin dat adres geldt. Werk de GGM-guid bij.

### Besluiten redacteur

- 2026-10-07: Koppelen aan het GEMMA-bedrijfsobject Verblijfplaats (partiële match): dezelfde naam en kern, het GEMMA-element is verweesd; de export overschrijft de definitie met die uit de wiki. *Zekerheid: logica.*
