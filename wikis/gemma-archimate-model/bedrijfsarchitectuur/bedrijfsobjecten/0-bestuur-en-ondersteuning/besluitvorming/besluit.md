---
id: besluit
type: bedrijfsobject
status: goedgekeurd
naam: Besluit
archimate_type: business-object
onderwerp: lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
bronnen:
- 2026-vng-ggm-2-5-1
- 2026-rijk-algemene-wet-bestuursrecht-wettekst
definitie: Schriftelijke beslissing van een bestuursorgaan met rechtsgevolg, voor
  een concreet geval of van algemene strekking.
definitie_formeel: Een schriftelijke beslissing van een bestuursorgaan, inhoudende
  een publiekrechtelijke rechtshandeling.
definitie_formeel_bron:
  bron: 2026-rijk-algemene-wet-bestuursrecht-wettekst
  plaats: art. 1:3 lid 1
grondslag: ggm-entiteit
match:
  ggm: sterk
  gemma: sterk
data_object: nee
kenmerken:
  herkenbaar: ja
  gemeentelijk: ja
  buiten_kernlagen: nee
  betekenis_in_onderwerp: ja
  slechts_eigenschap: nee
  eigen_identiteit: ja
  relaties: ja
  zelfstandig_beleidsbegrip: ja
  gedrag: nee
  handelende_partij: nee
  hoedanigheid: nee
  samenwerkingsverband: nee
  toegangspunt: nee
  plaats: nee
  aanbod_als_geheel: nee
  per_keer_doorlopen: nee
  gegroepeerd_gedrag: nee
  toestandsverandering: nee
  aangeboden_gedrag: nee
  gezamenlijk_gedrag: nee
  los_van_verantwoordelijkheid: nee
  meerdere_vervullers: nee
  onderscheidbare_exemplaren: ja
  levenscyclus: ja
  wordt_bewerkt: ja
  afspraak: nee
  waarneembare_vorm: nee
  geautomatiseerd_verwerkt: nee
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
ggm_definitie: Een na overweging of beraadslaging vastgestelde beslissing voor een
  individueel of concreet geval.
ggm_duplicaat_entiteiten:
- entiteit: Besluit
  guid: EAID_0CA08ED2_6990_8292_BBC7_281C33037374
  beleidsdomein: Diensten
  taakveld: Inkomen
gemma_id: id-865c7c57c41b41b6847a258458c8421d
gemma_naam: Besluit
gemma_type: business-object
gemma_definitie: Een na overweging of beraadslaging vastgestelde beslissing voor een
  individueel of concreet geval.
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-10d36920-683f-4cb4-84bf-b00ac045674f
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{AFB100D2-8C68-4488-8949-13E945D15920}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: 10d36920-683f-4cb4-84bf-b00ac045674f
bijgewerkt: '2026-09-30'
---

# Besluit

## Definitie

Schriftelijke beslissing van een bestuursorgaan met rechtsgevolg, voor een concreet geval of van algemene strekking.

De herkenbare definitie volgt de Awb, in gewone taal: "publiekrechtelijke rechtshandeling" is weergegeven als "met rechtsgevolg", en de definitie noemt uitdrukkelijk dat een besluit ook van algemene strekking kan zijn. Daarin wijkt ze af van de GGM-definitie, die alleen het concrete geval noemt.

> Onder besluit wordt verstaan: een schriftelijke beslissing van een bestuursorgaan, inhoudende een publiekrechtelijke rechtshandeling. (Awb art. 1:3 lid 1)

## Beschrijving

Het besluit is het bredere begrip boven alle besluiten die raad, college en burgemeester in de lijkbezorging nemen. Een besluit voor een concreet geval is een [Beschikking](beschikking.md), zoals een vergunning of een verlof; een besluit van algemene strekking is bijvoorbeeld de vaststelling van een verordening (Awb art. 1:3). Het element is generiek en domeinoverstijgend (besluit redacteur 2026-09-30).

## Kenmerken

| Kenmerk | Waarde | Onderbouwing | Bron |
|---|---|---|---|
| herkenbaar | ja | Awb-kernbegrip; GEMMA-bedrijfsobject Besluit; GGM Besluit (RGBZPlus, Diensten). | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| gemeentelijk | ja | Raad, college en burgemeester nemen als bestuursorgaan besluiten (Awb art. 1:1, 1:3). | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| buiten kernlagen | nee | Geen doel, norm, waarde, thema of vermogen. |  |
| betekenis in onderwerp | ja | Hoogste niveau van de keten Besluit → Beschikking → Vergunning voor de lijkbezorgingsbesluiten. | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| slechts eigenschap | nee | Geen eigenschap, status of indeling van één ander begrip. |  |
| eigen identiteit | ja | Bestaat zelfstandig. | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| relaties | ja | Bestuursorgaan neemt besluit; Beschikking is een Besluit (Awb art. 1:3). | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| zelfstandig beleidsbegrip | ja | Hoogste herkenbare niveau; GEMMA kent Besluit naast Beschikking. | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| gedrag | nee | Besluit is een passief ding. |  |
| handelende partij | nee | Besluit is een passief ding. |  |
| hoedanigheid | nee | Besluit is een passief ding. |  |
| samenwerkingsverband | nee | Besluit is een passief ding. |  |
| toegangspunt | nee | Besluit is een passief ding. |  |
| plaats | nee | Besluit is een passief ding. |  |
| aanbod als geheel | nee | Besluit is een passief ding. |  |
| per keer doorlopen | nee | Geen gedrag of niet deze soort gedrag. |  |
| gegroepeerd gedrag | nee | Geen gedrag of niet deze soort gedrag. |  |
| toestandsverandering | nee | Geen gedrag of niet deze soort gedrag. |  |
| aangeboden gedrag | nee | Geen gedrag of niet deze soort gedrag. |  |
| gezamenlijk gedrag | nee | Geen gedrag of niet deze soort gedrag. |  |
| los van verantwoordelijkheid | nee | Geen partij. |  |
| meerdere vervullers | nee | Geen verantwoordelijkheid. |  |
| onderscheidbare exemplaren | ja | Per besluit een exemplaar. | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| levenscyclus | ja | Genomen, bekendgemaakt, eventueel gewijzigd of ingetrokken. | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| wordt bewerkt | ja | Het bestuursorgaan neemt het besluit. | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| afspraak | nee | Eenzijdige publiekrechtelijke rechtshandeling (Awb art. 1:3 lid 1). | 2026-rijk-algemene-wet-bestuursrecht-wettekst |
| waarneembare vorm | nee | Geen document of formulier. |  |
| geautomatiseerd verwerkt | nee | De bronnen noemen geen geautomatiseerde verwerking. |  |

## GGM-bron

> Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.

Entiteit Besluit, beleidsdomein RGBZPlus (99 Kern). Match **sterk**: hetzelfde begrip, maar de GGM-definitie beperkt het besluit tot een individueel of concreet geval. Volgens de Awb is dat een beschikking; een besluit omvat ook besluiten van algemene strekking. Zie de terugmelding.

## GEMMA

Match **sterk** met GEMMA-element Besluit (business-object), gekoppeld aan dezelfde GGM-entiteit. Nieuw in dit model: een definitie die de Awb volgt, en Beschikking als specialisatie.

## Specialisaties

| Specialisatie | Omschrijving | GGM-entiteit | GGM-guid | GGM-attribuut |
|---|---|---|---|---|
| [Beschikking](beschikking.md) | Heeft een eigen pagina: besluit dat niet van algemene strekking is (Awb art. 1:3 lid 2) | Beschikking | EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836 | |

## GGM-duplicaten

| Beleidsdomein | GUID | Status |
|---|---|---|
| RGBZPlus | EAID_AFB100D2_8C68_4488_8949_13E945D15920 | primair: domeinoverstijgend (99 Kern) en gekoppeld aan GEMMA-bedrijfsobject Besluit |
| Diensten | EAID_0CA08ED2_6990_8292_BBC7_281C33037374 | duplicaat: zelfde naam en definitie, andere GUID |

## Bronnen

- Gemeentelijk Gegevensmodel 2.5.1 (2026-vng-ggm-2-5-1)
- [Algemene wet bestuursrecht](../../../../bronanalyses/lijkbezorging/2026-rijk-algemene-wet-bestuursrecht-wettekst.md)

## Terugmelding GGM

Zie [GGM-terugmeldingen](../../../../analyses/ggm-terugmeldingen.md), nummers 6 en 7.
