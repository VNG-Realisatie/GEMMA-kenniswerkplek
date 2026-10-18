---
id: besluit
type: bedrijfsobject
archimate_type: business-object
status: review
naam: Besluit
onderwerpen:
- besluitvorming
- lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
definitie: Schriftelijke beslissing van een bestuursorgaan met rechtsgevolg, voor een concreet geval of van algemene strekking.
match:
  ggm: sterk
  gemma: sterk
data_objecten:
- Besluit-data
objectniveau: generiek
bronnen:
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
ggm_entiteit: Besluit
ggm_guid: EAID_AFB100D2_8C68_4488_8949_13E945D15920
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: 99 Kern
ggm_diagram:
- Diagram Vergunningen en Meldingen
- Diagram Aanvragen, Zaken en Besluiten
- Verkamering en Woonoverlast
- Referentiemodel Gemeentelijke Basisgegevens Zaken in schema
ggm_diagram_ids:
- EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267
- EAID_A2BA1F0D_8428_42fc_80D6_7184F243D268
- EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF
- EAID_8AC9A512_0538_48f7_B25E_5BC65B17A147
ggm_definitie: Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.
gemma_id: id-865c7c57c41b41b6847a258458c8421d
gemma_naam: Besluit
gemma_type: business-object
gemma_definitie: Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-10d36920-683f-4cb4-84bf-b00ac045674f
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{AFB100D2-8C68-4488-8949-13E945D15920}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: 10d36920-683f-4cb4-84bf-b00ac045674f
---

# Besluit

<!-- Gegenereerd door tools/render.py uit de beoordeling besluit.yaml. Wijzig de beoordeling, niet deze pagina. -->

**Status: review.** Wacht op het akkoord van de redacteur.

## Betekenis

### Definitie

Schriftelijke beslissing van een bestuursorgaan met rechtsgevolg, voor een concreet geval of van algemene strekking.

### Beschrijving

Een besluit is een schriftelijke beslissing van een bestuursorgaan, inhoudende een publiekrechtelijke rechtshandeling (Awb art. 1:3 lid 1). Een besluit voor een concreet geval is een beschikking, zoals een vergunning of een verlof; een besluit van algemene strekking is bijvoorbeeld de vaststelling van een verordening. Het element is generiek en domeinoverstijgend.

### Per onderwerp

#### [Lijkbezorging](../../../../../onderwerpen/lijkbezorging/begrippen.md)

Raad, college en burgemeester nemen op grond van de Wet op de lijkbezorging een reeks besluiten; vrijwel allemaal zijn het beschikkingen, zoals vergunningen, verloven en de sluiting van een begraafplaats.

## Plaats in het model

### Typering

Bedrijfsobject, niveau generiek. Uitkomst van de beslistabel: Passief, object (3 toetskenmerken ja).

### Plaats in de indelingen

- **Objectniveau**: generiek.
- **Mutaties door bedrijfsprocessen**: [Bekendmaken besluit](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/bekendmaken-besluit.md), [Uitvoeren uniforme openbare voorbereidingsprocedure](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md), [Voeren verweer in beroep](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/voeren-verweer-in-beroep.md).
- **Beleidsdomeinindeling**: 0 Bestuur en Ondersteuning, Besluitvorming.

### Kenmerken

**Vak**: bedrijfslaag, passief (Bedrijfsobject, Afspraak, Representatie (geen pagina)). **Hoofdkenmerk**: object.

De scope is doorlopen (herkenbaar, gemeentelijk, binnen dit model, betekenis in dit onderwerp) en alle toetskenmerken van het type zijn ja; een antwoord zonder eigen onderbouwing steunt op de bronnen van de beoordeling.

| Kenmerk | Onderbouwing |
|---|---|
| **afhankelijkheid**: zelfstandig | Zelfstandig, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **wordt bewerkt**: Wordt het door aanwijsbaar gemeentelijk gedrag geregistreerd, bijgewerkt, beëindigd, geraadpleegd of verstrekt, operationeel en niet alleen beleidsmatig? | Ja, met [Behandelen bezwaar](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-bezwaar.md), [Bekendmaken besluit](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/bekendmaken-besluit.md), [Uitvoeren uniforme openbare voorbereidingsprocedure](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md), [Voeren verweer in beroep](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/voeren-verweer-in-beroep.md). [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **onderscheidbare exemplaren**: Zijn de afzonderlijke exemplaren van elkaar te onderscheiden? | Ja, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |
| **levenscyclus**: Ontstaan, veranderen en eindigen de exemplaren? | Ja, standaard. [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md), [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) |

### Specialisaties

- **[Beschikking](beschikking.md)**: Besluit dat niet van algemene strekking is (Awb art. 1:3 lid 2).

### Relaties

#### Inkomend

| Van | Relatie | Naar | Bron |
|---|---|---|---|
| [Aanvraag](aanvraag.md) | leidt tot *associatie (gericht)* | Besluit | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 1:3 lid 3, 4:1); GGM (EAID_1778947E_A0EE_C776_2C1C_281C33036576) |
| [Behandelen bezwaar](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/behandelen-bezwaar.md) | heroverweegt en herroept zo nodig *toegang (bijwerken)* | Besluit | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 7:11) |
| [Bekendmaken besluit](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/bekendmaken-besluit.md) | maakt bekend *toegang (verstrekken)* | Besluit | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 3:41, 3:42) |
| [Beschikking](beschikking.md) | is een *specialisatie* | Besluit | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 1:3 lid 2) |
| [Bezwaarschrift](bezwaarschrift.md) | is gericht tegen *associatie (gericht)* | Besluit | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 6:5 lid 1 onder c, 7:11) |
| [Uitvoeren uniforme openbare voorbereidingsprocedure](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/uitvoeren-uniforme-openbare-voorbereidingsprocedure.md) | legt ter inzage als ontwerp en neemt *toegang (registreren)* | Besluit | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 3:11, 3:18) |
| [Voeren verweer in beroep](../../../bedrijfsprocessen/0-bestuur-en-ondersteuning/besluitvorming/voeren-verweer-in-beroep.md) | zendt de stukken over het bestreden besluit; neemt na vernietiging zo nodig een nieuw *toegang (raadplegen, registreren: lezen-schrijven)* | Besluit | [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) (art. 8:42 lid 1; art. 8:72 lid 4) |

### Data-objecten

- [Besluit-data](../../../../applicatiearchitectuur/data-objecten/besluit-data.md) *realisatie*: GGM-entiteit *Besluit*, match sterk.

## Herkomst

### Bronnen

| Korte titel | Bron |
|---|---|
| [Awb](../../../../../onderwerpen/besluitvorming/bronduidingen/rijksregelgeving/2026-rijk-algemene-wet-bestuursrecht-wettekst.md) | Algemene wet bestuursrecht (BWBR0005537) |
| [Wet op de lijkbezorging](../../../../../onderwerpen/lijkbezorging/bronduidingen/rijksregelgeving/2026-rijk-wet-op-de-lijkbezorging-wettekst.md) | Wet op de lijkbezorging |

### Afstemming met GGM

Match **sterk** met GGM-entiteit *Besluit* (beleidsdomein RGBZPlus, taakveld 99 Kern). Zelfde begrip; de GGM-definitie beschrijft een beschikking, niet een besluit in de zin van de Awb (terugmelding 6). Duplicaat in Diensten (terugmelding 7).

> Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.

Duplicaten in het GGM:

| Entiteit | Toelichting |
|---|---|
| Besluit (Diensten) | Besluit in Diensten (Inkomen), zelfde definitie; terugmelding 7. |

GGM-terugmeldingen:

- [Nummer 6](../../../../../modellen/ggm/terugmeldingen.md) (definitie, open): **GGM:** Besluit is 'een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval'. **Bevinding:** die definitie beschrijft een beschikking. Volgens de Awb is een besluit een schriftelijke beslissing van een bestuursorgaan, inhoudende een publiekrechtelijke rechtshandeling (art. 1:3 lid 1), en omvat het ook besluiten van algemene strekking; een beschikking is een besluit dat niet van algemene strekking is (art. 1:3 lid 2). **Voorstel:** de Awb-definitie overnemen.
- [Nummer 7](../../../../../modellen/ggm/terugmeldingen.md) (duplicaat, open): **GGM:** Besluit komt twee keer voor met verschillende GUID's en dezelfde definitie: RGBZPlus (99 Kern, EAID_AFB100D2_8C68_4488_8949_13E945D15920, gekoppeld aan GEMMA-bedrijfsobject Besluit); Diensten (Inkomen, EAID_0CA08ED2_6990_8292_BBC7_281C33037374). **Bevinding:** één begrip staat zo twee keer in het GGM; gegevens en koppelingen raken verdeeld over twee entiteiten, terwijl het GEMMA-bedrijfsobject Besluit maar aan één ervan hangt. **Voorstel:** samenvoegen tot de domeinoverstijgende entiteit in RGBZPlus.

### Afstemming met GEMMA

Match **sterk** met GEMMA-element *Besluit* (business-object). Gekoppeld aan dezelfde GGM-entiteit. Nieuw: een definitie die de Awb volgt, en Beschikking als specialisatie.

> Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.
