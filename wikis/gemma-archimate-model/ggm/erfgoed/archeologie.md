<!-- gegenereerd door tools/ggm.py; hash: a1b27b48188a4a9736351ba0d3705a464c2ad4ac780fc5a53aae93b59ad7038f -->
# Archeologie

Taakveld: Erfgoed. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Archeologiebesluit | `EAID_836E51BF_65E9_4482_B555_C9AB737D264D` | Een professioneel oordeel dat gebaseerd is op algemeen aanvaarde wetenschap ten aanzien van de archeologie |  |
| Artefact | `EAID_2C230EE7_036D_48be_B82A_FF45598170F7` | De benaming voor ieder verplaatsbaar object dat door de mens is vervaardigd, bewerkt en/of gebruikt. | projectCD, putnummer, vondstnummer, artefectnummer, datering, maten, type, beschrijving, determinatieniveau, naam, doosnummer, tekeningnummer, dianummer, fotonummer, restauratieWenselijk, exposabel, conserveren, key, keyPut, keyMagazijnplaatsing, keyDoos, dateringComplex, opmerkingen, functie, origine, literatuur, herkomst, keyVondst |
| Artefactsoort | `EAID_67CF25EB_EBB0_4185_8171_1F9DD3B5D212` | Typering van artefacten | code, naam, omschrijving |
| boring | `EAID_E11FDCA7_7538_4353_83FF_72164D928452` | Een verticale grondmonstername binnen een project De gegevens over het geheel van activiteiten, voor zover relevant voor het onderzoek, dat tot doel heeft door boren een gat in de ondergrond te maken om monsters uit de ondergrond te nemen en/of metingen aan de ondergrond te doen. Een middel om door boren of steken toegang te krijgen tot de ondergrond om bijvoorbeeld geroerde en/of ongeroerde monsters aan de ondergrond te ontlenen voor nader onderzoek. |  |
| Doos | `EAID_703CAFCF_FDC0_4861_AA76_1692303DE7BE` | Een afsluitbaar object waar iets in wordt opgeborgen of verpakt. | projectCD, doosnummer, inhoud, herkomst, key, keyMagazijnlocatie |
| Kaart | `EAID_F28DDE36_7BE4_45f7_A820_FFF0261CAA4E` | De geografische weergave van een gedeelte van het aardoppervlak | naam, omschrijving, content |
| locatie | `EAID_F25EE5A8_2CF4_498b_8DAD_8EEE48FAF3A5` | Een specifieke plaats | locatiePunt |
| Magazijnlocatie | `EAID_4C1543FD_250B_4291_9B23_BC9D3D9C0C4A` | Locatie van een magazijn | vaknummer, volgletter, key, stelling |
| Magazijnplaatsing | `EAID_F954FB72_AE88_4a0e_A3D8_555FCF8D9C9F` | Het ergens neerzetten van een object in een magazijn. | uitgeleend, beschrijving, datumGeplaatst, key, keyDoos, keyMagazijnlocatie, projectCD, herkomst |
| Project | `EAID_E42A32F7_262F_4005_9EB9_4674B76E8825` | Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat. | projectCD, naam, datumStart, datumEinde, naamcode, toponiem, locatie, coordinaten, jaarVan, jaarTot, trefwoorden |
| Put | `EAID_17286CE1_21F2_454b_95A6_3E4C0C6E2453` | Grondspoor, veelal verstevigd en gefundeerd aangelegd, bedoeld voor de tijdelijke opslag van danwel water (waterput) danwel uitwerpselen en afval (beerput). | projectCD, putnummer, key |
| Spoor | `EAID_14939C33_2DCE_41bf_A2BE_FF1EDD292FE7` | Een blijk van eerdere aanwezigheid. | projectCD, putnummer, vlaknummer, spoornummer, hoogteBoven, hoogteOnder, aard, datering, datum, vorm, beschrijving, key, keyVlak |
| Stelling | `EAID_382D408F_41A3_49d2_9F66_DFFA6C75590D` | Een systeem om goederen op te slaan die worden vervoerd en opgeslagen op pallets, in bundels of per stuk.(Wikipedia) | stellingcode, inhoud |
| Vindplaats | `EAID_84DED9A9_2D33_4a77_94F2_29657024590F` | Een plek waar men iets gevonden heeft. | projectcode, locatie, vindplaatsOmschrijving, gemeente, datering, begindatering, einddatering, aard, onderzoek, mobilia, depot, documentatie, bibliografie, beschrijving |
| Vlak | `EAID_0644BD52_8C2B_462d_94B9_9C99908952F5` | Plat, oneindig oppervlak of variëteit zonder enige kromming. | projectCD, putnummer, vlaknummer, diepteVan, diepteTot, key, keyPut |
| Vondst | `EAID_F8283401_70F8_41b8_A97C_32A9074AD4B1` | Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument | projectCD, vondstnummer, putnummer, vlaknummer, spoornummer, vullingnummer, omstandigheden, omschrijving, key, keyVulling, datum, XCoordinaat, YCoordinaat |
| Vulling | `EAID_8417459E_2193_44a2_A1AC_38C39EA93CBF` | Dunne wegeringsplank gebruikt om de ruimte tussen de bovenste kimweger en de onderste balkweger op te vullen (Sopers, 1974). | projectCD, putnummer, vlaknummer, spoornummer, vullingnummer, grondsoort, kleur, structuur, key, keySpoor |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Artefact | Association | vindbaar op | Magazijnplaatsing | 0..* → 0..1 | `EAID_44E14266_7033_40f1_AC08_6F9BF5ED5C00` |  |
| Artefact | Association | zit in | Doos | 0..* → 0..1 | `EAID_919B5B41_AEC2_4f84_B1E9_65741BF8C493` |  |
| Artefact | Association | is van soort | Artefactsoort | 0..* → 1..1 | `EAID_C4C65D59_136E_4a4c_8E5B_96A6396D3CE6` |  |
| Doos | Association | staat op | Magazijnlocatie | 0..* → 1..1 | `EAID_EFA6E5A8_4A4A_4fc8_89C5_6DFDB6186DB4` |  |
| Magazijnplaatsing | Association | zit in | Doos | 0..1 → 0..* | `EAID_09CA27B3_BF50_45a5_8708_65E789BB518C` |  |
| Magazijnplaatsing | Association | staat op | Magazijnlocatie | 0..* → 0..1 | `EAID_8C0C6E8C_2CFD_4f2b_95DB_6417D1A1398D` |  |
| Magazijnplaatsing | Association | hoort bij | Project | 0..* → 0..1 | `EAID_CAEF36F1_E915_4dc3_BFA4_53FD9C8F5E33` |  |
| Project | Association | heeft | Archeologiebesluit | 1..1 → 0..* | `EAID_4610B0AB_0D86_42ab_9619_8B78B5EAB332` |  |
| Project | Association | heeft | Put | 1..1 → 0..* | `EAID_7356FAC0_F183_494b_948D_5DFC47CC5522` |  |
| Project | Association | heeft | boring | 1..1 → 0..* | `EAID_754FC6C1_D7B3_4b3d_9991_8DD4AA00CCC1` |  |
| Project | Association | wordt begrensd door | locatie | 0..* → 1..* | `EAID_7C1BBED5_4316_433a_A13D_CB353DB9B13C` |  |
| Project | Usage | vastlegging | Document |  →  | `EAID_4471950A_BB45_415e_8BD3_B6EAB33AA5CC` |  |
| Put | Association | heeft locatie | locatie | 0..* → 1..* | `EAID_0EB0ABE6_4A54_48ad_8B51_41EBF75F8EF1` |  |
| Put | Association | heeft | Vlak | 1..1 → 0..* | `EAID_E1790157_80B5_4537_BEDB_FB6A0AEB3A56` |  |
| Spoor | Association | heeft | Vulling | 1..1 → 0..* | `EAID_C1012227_462A_41ec_AF20_53B78105C045` |  |
| Stelling | Association | heeft | Magazijnlocatie | 1..1 → 0..* | `EAID_9DE067E7_2305_4f08_86EA_E5AF550E336F` |  |
| Vindplaats | Association | hoort bij | Project | 0..1 → 1 | `EAID_C0088790_7E28_4d9e_AEA3_ED3243330D49` |  |
| Vlak | Association | heeft | Spoor | 1..1 → 0..* | `EAID_65B9846F_78F1_46f7_B8BB_7A022AB7FEA2` |  |
| Vondst | Association | bevat | Artefact | 0..1 → 0..* | `EAID_F624D2ED_D364_4c68_A21F_606BF07EC1A3` |  |
| Vulling | Association | heeft | Vondst | 1..1 → 0..* | `EAID_9E33A846_9576_4387_8887_CF26687CAA07` |  |
