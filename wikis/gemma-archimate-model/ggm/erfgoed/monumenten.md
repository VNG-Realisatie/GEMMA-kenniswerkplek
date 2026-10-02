<!-- gegenereerd door tools/ggm.py; hash: b6b95ff3c5c18071b3a5c1a1b19c912804811f1d93f934666d989e319f665f8d -->
# Monumenten

Taakveld: Erfgoed. Alleen objecttypen; letterlijke definities uit het GGM.

## Ambacht

Beroep waarbij een handwerker met gereedschap eindproducten maakt.

Attributen: jaarAmbachtVanaf, jaarAmbachtTot, ambachtsoort.

GUID: `EAID_54944273_F312_44b2_A78D_43488F915429`

## Beschermde Status

Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks- provinciaal- of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente,

Attributen: rijksmonumentcode, gemeentelijkMonumentCode, datumInschrijvingRegister, naam, type, gezichtscode, complex, opmerkingen, bronnen, omschrijving.

GUID: `EAID_32C02923_EE3A_4553_B94B_31E0C273A829`

Relaties:

- monument ambacht → Ambacht (*Association*, 0..* → 0..*, `EAID_8E18F665_2A86_44fd_AD55_3E435A282BDF`)
- monument bouwactiviteit → Bouwactiviteit (*Association*, 0..* → 0..*, `EAID_55585CB9_E569_47ca_9EFE_B9D5CF46BCBD`)
- monument bouwstijl → Bouwstijl (*Association*, 0..* → 0..*, `EAID_144ADF26_C2E9_4080_8F4F_32F9B255E4AE`)
- monument bouwtype → Bouwtype (*Association*, 0..* → 0..*, `EAID_D9634EAD_2869_40a1_B243_805897E4B1B3`)
- monument fotos → Foto (*Association*, 1 → 0..*, `EAID_1F08C810_A491_4e07_B859_C3D4EDEBA557`)
- betreft → KadastraleOnroerendeZaak (*Association*, 1 → 0..*, `EAID_59A9090E_CF7A_4e6f_91E1_592085B0DA94`)
- monument functie → OorspronkelijkeFunctie (*Association*, 0..* → 0..*, `EAID_FD27EB67_1CFA_4f40_AE79_329DE9DE6754`)
- betreft → OpenbareRuimte (*Association*, 0..1 → 0..*, `EAID_24E90A75_8207_4975_8184_438890708976`)
- betreft → OpenbareRuimte (*Association*, 0..1 → 0..*, `EAID_44E4F035_7E96_48df_B6CF_93C945FF97C3`)
- betreft → Pand (*Association*, 0..1 → 0..*, `EAID_F7893BFE_1A66_4760_9124_B62A81F45997`)
- documentatie → Document (*Usage*, 0..1 → 0..*, `EAID_1ED1613A_DE5F_4ee2_8356_4BB729911C69`)

## Bouwactiviteit

Het bouwen van een bouwwerk.

Attributen: bouwjaarVan, bouwjaarTot, indicatie, bouwjaarklasse, omschrijving.

GUID: `EAID_4AD539EC_A308_43da_B025_17A1647303F3`

## Bouwstijl

Trant van bouwen met bepaalde kenmerken in een bepaalde periode. In de betrokken tijdperken waren het geen levende voorstellingen; het zijn later geformuleerde (generaliserende) geschiedkundige constructies. Doelbewust komt deze tendens op sedert c. 1830. (Haslinghuis)

Attributen: hoofdstijl, substijl, zuiverheid, toelichting.

GUID: `EAID_8C0888C9_7B2E_4fcb_AEFF_E1733875CDCA`

## Bouwtype

Typering van een bouwstijl

Attributen: hoofdcategorie, subcategorie, toelichting.

GUID: `EAID_5E9DAFBB_C9B5_4706_A43D_07AD4979DED4`

## OorspronkelijkeFunctie

De functie van een object na bouw of oplevering

Attributen: hoofdfunctie, functiesoort, hoofdcategorie, subcategorie, functie, verbijzondering, toelichting.

GUID: `EAID_49993EF9_ED8B_49e0_B8F7_FC7C8C28669D`
