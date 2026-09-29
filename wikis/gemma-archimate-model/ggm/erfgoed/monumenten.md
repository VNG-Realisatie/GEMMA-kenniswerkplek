<!-- gegenereerd door tools/ggm.py; hash: f00ff74b3791984a4434fe69deacb21a06e53ec20206d42914fb092b020c54b6 -->
# Monumenten

Taakveld: Erfgoed. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Ambacht | `EAID_54944273_F312_44b2_A78D_43488F915429` | Beroep waarbij een handwerker met gereedschap eindproducten maakt. | jaarAmbachtVanaf, jaarAmbachtTot, ambachtsoort |
| Beschermde Status | `EAID_32C02923_EE3A_4553_B94B_31E0C273A829` | Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks- provinciaal- of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente, | rijksmonumentcode, gemeentelijkMonumentCode, datumInschrijvingRegister, naam, type, gezichtscode, complex, opmerkingen, bronnen, omschrijving |
| Bouwactiviteit | `EAID_4AD539EC_A308_43da_B025_17A1647303F3` | Het bouwen van een bouwwerk. | bouwjaarVan, bouwjaarTot, indicatie, bouwjaarklasse, omschrijving |
| Bouwstijl | `EAID_8C0888C9_7B2E_4fcb_AEFF_E1733875CDCA` | Trant van bouwen met bepaalde kenmerken in een bepaalde periode. In de betrokken tijdperken waren het geen levende voorstellingen; het zijn later geformuleerde (generaliserende) geschiedkundige constructies. Doelbewust komt deze tendens op sedert c. 1830. (Haslinghuis) | hoofdstijl, substijl, zuiverheid, toelichting |
| Bouwtype | `EAID_5E9DAFBB_C9B5_4706_A43D_07AD4979DED4` | Typering van een bouwstijl | hoofdcategorie, subcategorie, toelichting |
| OorspronkelijkeFunctie | `EAID_49993EF9_ED8B_49e0_B8F7_FC7C8C28669D` | De functie van een object na bouw of oplevering | hoofdfunctie, functiesoort, hoofdcategorie, subcategorie, functie, verbijzondering, toelichting |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Beschermde Status | Association | monument bouwstijl | Bouwstijl | 0..* → 0..* | `EAID_144ADF26_C2E9_4080_8F4F_32F9B255E4AE` |  |
| Beschermde Status | Association | monument fotos | Foto | 1 → 0..* | `EAID_1F08C810_A491_4e07_B859_C3D4EDEBA557` |  |
| Beschermde Status | Association | betreft | OpenbareRuimte | 0..1 → 0..* | `EAID_24E90A75_8207_4975_8184_438890708976` |  |
| Beschermde Status | Association | betreft | OpenbareRuimte | 0..1 → 0..* | `EAID_44E4F035_7E96_48df_B6CF_93C945FF97C3` |  |
| Beschermde Status | Association | monument bouwactiviteit | Bouwactiviteit | 0..* → 0..* | `EAID_55585CB9_E569_47ca_9EFE_B9D5CF46BCBD` |  |
| Beschermde Status | Association | betreft | KadastraleOnroerendeZaak | 1 → 0..* | `EAID_59A9090E_CF7A_4e6f_91E1_592085B0DA94` |  |
| Beschermde Status | Association | monument ambacht | Ambacht | 0..* → 0..* | `EAID_8E18F665_2A86_44fd_AD55_3E435A282BDF` |  |
| Beschermde Status | Association | monument bouwtype | Bouwtype | 0..* → 0..* | `EAID_D9634EAD_2869_40a1_B243_805897E4B1B3` |  |
| Beschermde Status | Association | betreft | Pand | 0..1 → 0..* | `EAID_F7893BFE_1A66_4760_9124_B62A81F45997` |  |
| Beschermde Status | Association | monument functie | OorspronkelijkeFunctie | 0..* → 0..* | `EAID_FD27EB67_1CFA_4f40_AE79_329DE9DE6754` |  |
| Beschermde Status | Usage | documentatie | Document | 0..1 → 0..* | `EAID_1ED1613A_DE5F_4ee2_8356_4BB729911C69` |  |
