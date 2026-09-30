---
id: beschikking
type: bedrijfsobject
status: kandidaat
naam: Beschikking
archimate_type: business-object
onderwerp: lijkbezorging
taakveld: 0 Bestuur en Ondersteuning
beleidsdomein: Besluitvorming
bronnen:
- 2026-vng-ggm-2-5-1
- 2026-rijk-wet-op-de-lijkbezorging-wettekst
- 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen
definitie: Besluit van een bestuursorgaan in een concreet geval, zoals het verlenen
  van een vergunning.
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
  los_van_verantwoordelijkheid: nee
  meerdere_vervullers: nee
  per_keer_doorlopen: nee
  gegroepeerd_gedrag: nee
  toestandsverandering: nee
  aangeboden_gedrag: nee
  gezamenlijk_gedrag: nee
  onderscheidbare_exemplaren: ja
  levenscyclus: ja
  wordt_bewerkt: ja
  afspraak: nee
  waarneembare_vorm: nee
  geautomatiseerd_verwerkt: nee
ggm_entiteit: Beschikking
ggm_guid: EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836
ggm_uml_type: Class
ggm_beleidsdomein: Generiek Jeugd en Wmo
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- 'Sociaal Domein Beschikking en Voorziening: Domain Objects'
- Beperkingen
- AanvraagOfMelding
ggm_diagram_ids:
- EAID_5AE29494_3572_4924_B2B8_3206E55D71BB
- EAID_9B278A50_862A_4085_B362_C41392101916
- EAID_5F3782EB_C416_461c_A9FA_40991A7F0165
ggm_definitie: 'In het bestuursrecht: Een beslissing van een overheidsorgaan in een
  concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele
  recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.'
ggm_duplicaat_entiteiten:
- entiteit: Beschikking
  guid: EAID_16ABCFF8_4817_6A73_59BA_281C3303F8D2
  beleidsdomein: Diensten
  taakveld: Inkomen
gemma_id: id-3d9b45d27b6840b39b99e8ede85db6f4
gemma_naam: Beschikking
gemma_type: business-object
gemma_definitie: 'In het bestuursrecht: Een beslissing van een overheidsorgaan in
  een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele
  recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.'
gemma_map: Business / _Sync GEMMA en project / GGM / Bedrijfsobjecten
gemma_eigenschappen:
  GEMMA URL: https://gemmaonline.nl/index.php/GEMMA/id-c481e8b8-f7d7-4979-b767-ebf2a9b04712
  GGM-datum-tijd-export: 10122024-112046
  GGM-guid: '{71D7E96D-641A-4b6a-A325-DED07C3B5836}'
  GGM-uml-type: Class
  Let op: '"ggm-" properties worden beheerd in het GGM informatiemodel'
  Object ID: c481e8b8-f7d7-4979-b767-ebf2a9b04712
bijgewerkt: '2026-09-30'
---

# Beschikking

## Beschrijving

In de lijkbezorging nemen burgemeester, college en gemeenteraad een reeks beschikkingen die elk een eigen wetsartikel hebben, maar geen eigen gegevens of levenscyclus. Ze zijn specialisaties zonder eigen pagina; de toestemmingen voor een handeling vallen onder [Vergunning](vergunning.md).

## Kenmerken

| Kenmerk | Waarde | Onderbouwing | Bron |
|---|---|---|---|
| herkenbaar | ja | GEMMA-bedrijfsobject Beschikking; GGM Beschikking (Diensten, Generiek Jeugd en Wmo). | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| gemeentelijk | ja | Besluit van een gemeentelijk bestuursorgaan. | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| buiten kernlagen | nee | Geen doel, norm, waarde, thema of vermogen. |  |
| betekenis in onderwerp | ja | Het hoogste herkenbare niveau voor de vergunningen, verloven, toestemmingen en verklaringen in de lijkbezorging (assess §3). | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| slechts eigenschap | nee | Geen eigenschap, status of indeling van één ander begrip. |  |
| eigen identiteit | ja | Bestaat zelfstandig, niet als onderdeel of deelstap van één ander begrip. | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| relaties | ja | Burgemeester verleent vergunning tot opgraving en verlof tot ontleding (art. 29, 68); B&W verlenen vergunningen en toestemmingen (art. 41, 53, 64, 66b); het college verleent vergunning grafbedekking (Groningen art. 22): opgetild van de specialisaties. | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| zelfstandig beleidsbegrip | ja | GEMMA-niveau (Beschikking naast Besluit). | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| gedrag | nee | Beschikking is een passief ding. |  |
| handelende partij | nee | Beschikking is een passief ding. |  |
| hoedanigheid | nee | Beschikking is een passief ding. |  |
| samenwerkingsverband | nee | Beschikking is een passief ding. |  |
| toegangspunt | nee | Beschikking is een passief ding. |  |
| plaats | nee | Beschikking is een passief ding. |  |
| aanbod als geheel | nee | Beschikking is een passief ding. |  |
| los van verantwoordelijkheid | nee | Geen partij. |  |
| meerdere vervullers | nee | Geen verantwoordelijkheid. |  |
| per keer doorlopen | nee | Geen gedrag of niet deze soort gedrag. |  |
| gegroepeerd gedrag | nee | Geen gedrag of niet deze soort gedrag. |  |
| toestandsverandering | nee | Geen gedrag of niet deze soort gedrag. |  |
| aangeboden gedrag | nee | Geen gedrag of niet deze soort gedrag. |  |
| gezamenlijk gedrag | nee | Geen gedrag of niet deze soort gedrag. |  |
| onderscheidbare exemplaren | ja | Per besluit een exemplaar. | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| levenscyclus | ja | Aangevraagd, verleend of geweigerd, eventueel ingetrokken. | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| wordt bewerkt | ja | De gemeente neemt het besluit. | 2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen, 2026-rijk-wet-op-de-lijkbezorging-wettekst |
| afspraak | nee | Eenzijdig besluit. |  |
| waarneembare vorm | nee | Geen document of formulier. |  |
| geautomatiseerd verwerkt | nee | De bronnen noemen geen geautomatiseerde verwerking. |  |

## GGM-bron

> In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.

Entiteit Beschikking, beleidsdomein Generiek Jeugd en Wmo (6 Sociaal Domein). Match **sterk**: hetzelfde begrip voor het bestuursrecht; de GGM-definitie omvat ook de civielrechtelijke beschikking, die buiten dit model valt.

## GGM-duplicaten

| Beleidsdomein | GUID | Status |
|---|---|---|
| Generiek Jeugd en Wmo | EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836 | primair: de GUID waaraan GEMMA-bedrijfsobject Beschikking is gekoppeld |
| Diensten | EAID_16ABCFF8_4817_6A73_59BA_281C3303F8D2 | duplicaat: zelfde begrip ('een voor beroep vatbaar overheidsbesluit'), andere GUID |

## GEMMA

Match **sterk** met GEMMA-element Beschikking (business-object). Nieuw in dit model: een herkenbare definitie.

## Specialisaties

Met eigen pagina: [Vergunning](vergunning.md). Zonder eigen pagina, uit de lijkbezorging:

| Specialisatie | Omschrijving | GGM-entiteit | GGM-guid | GGM-attribuut |
|---|---|---|---|---|
| Aanwijzing van grond voor bijzondere begraafplaats | Aanwijzing door de gemeenteraad van grond voor aanleg of uitbreiding (art. 40 lid 1). Geen eigen pagina: Variant van een breder begrip (5/5). | | | |
| Sluiting van een begraafplaats | Besluit van B&W tot sluiting van een gemeentelijke begraafplaats, of geslotenverklaring na tien jaar zonder begraving (art. 43, 44). Geen eigen pagina: Variant van een breder begrip (5/5). | | | |
| Andere termijn | Door de burgemeester gestelde afwijkende termijn voor begraving of crematie (art. 17). Geen eigen pagina: Variant van een breder begrip (5/5). | | | |
| Verklaring van verwaarlozing | Schriftelijke verklaring van de houder dat het onderhoud van een particulier graf kennelijk verwaarloosd is (art. 28 lid 4). Geen eigen pagina: Variant van een breder begrip (5/5). | | | |
| Maatregel bij besmet lijk | Maatregel van de burgemeester na advies van de GGD om gevaar voor de volksgezondheid af te wenden (art. 22a). Geen eigen pagina: Variant van een breder begrip (5/5). | | | |

## Relaties

| Relatie | Naar | Naam | Kardinaliteit | Grondslag | GGM-relatie | Bron |
|---|---|---|---|---|---|---|
| associatie (gericht) | [Grafrecht](../../7-volksgezondheid-en-milieu/begraafplaatsen-en-crematoria/grafrecht.md) | doet vervallen (verklaring van verwaarlozing) | | bron | | 2026-rijk-wet-op-de-lijkbezorging-wettekst (art. 28 lid 6) |

## Bronnen

- Gemeentelijk Gegevensmodel 2.5.1 (2026-vng-ggm-2-5-1)
- [Wet op de lijkbezorging](../../../../bronanalyses/lijkbezorging/2026-rijk-wet-op-de-lijkbezorging-wettekst.md)
- [Beheersverordening gemeentelijke begraafplaatsen gemeente Groningen 2023](../../../../bronanalyses/lijkbezorging/2023-groningen-beheersverordening-gemeentelijke-begraafplaatsen.md)

## Ter discussie

- Nieuw generiek element, voorgesteld als breder begrip voor de lijkbezorgingsbesluiten (besluit redacteur 2026-09-30: generieke map 0 Bestuur en Ondersteuning / Besluitvorming).
- Keuze van de primaire GGM-GUID bij het duplicaat (Generiek Jeugd en Wmo, zoals GEMMA; of Diensten).
- Het GGM kent ook Besluit (RGBZPlus, Diensten) als bredere generalisatie; die is in deze run niet voorgesteld.

## Terugmelding GGM

Zie [GGM-terugmeldingen](../../../../analyses/ggm-terugmeldingen.md), nummer 5.
