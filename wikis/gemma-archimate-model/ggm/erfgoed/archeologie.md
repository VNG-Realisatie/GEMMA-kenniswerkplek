<!-- gegenereerd door tools/ggm.py; hash: 4e54ec67c2cae383e5eef7cf76dc47ca794ba6dab4c6d57789af6b04bbf4aa85 -->
# Archeologie

Taakveld: Erfgoed. Alleen objecttypen; letterlijke definities uit het GGM.

## Archeologiebesluit

Een professioneel oordeel dat gebaseerd is op algemeen aanvaarde wetenschap ten aanzien van de archeologie

GUID: `EAID_836E51BF_65E9_4482_B555_C9AB737D264D`

## Artefact

De benaming voor ieder verplaatsbaar object dat door de mens is vervaardigd, bewerkt en/of gebruikt.

Attributen: projectCD, putnummer, vondstnummer, artefectnummer, datering, maten, type, beschrijving, determinatieniveau, naam, doosnummer, tekeningnummer, dianummer, fotonummer, restauratieWenselijk, exposabel, conserveren, key, keyPut, keyMagazijnplaatsing, keyDoos, dateringComplex, opmerkingen, functie, origine, literatuur, herkomst, keyVondst.

GUID: `EAID_2C230EE7_036D_48be_B82A_FF45598170F7`

Relaties:

- is van soort → Artefactsoort (*Association*, 0..* → 1..1, `EAID_C4C65D59_136E_4a4c_8E5B_96A6396D3CE6`)
- zit in → Doos (*Association*, 0..* → 0..1, `EAID_919B5B41_AEC2_4f84_B1E9_65741BF8C493`)
- vindbaar op → Magazijnplaatsing (*Association*, 0..* → 0..1, `EAID_44E14266_7033_40f1_AC08_6F9BF5ED5C00`)

## Artefactsoort

Typering van artefacten

Attributen: code, naam, omschrijving.

GUID: `EAID_67CF25EB_EBB0_4185_8171_1F9DD3B5D212`

## boring

Een verticale grondmonstername binnen een project De gegevens over het geheel van activiteiten, voor zover relevant voor het onderzoek, dat tot doel heeft door boren een gat in de ondergrond te maken om monsters uit de ondergrond te nemen en/of metingen aan de ondergrond te doen. Een middel om door boren of steken toegang te krijgen tot de ondergrond om bijvoorbeeld geroerde en/of ongeroerde monsters aan de ondergrond te ontlenen voor nader onderzoek.

GUID: `EAID_E11FDCA7_7538_4353_83FF_72164D928452`

## Doos

Een afsluitbaar object waar iets in wordt opgeborgen of verpakt.

Attributen: projectCD, doosnummer, inhoud, herkomst, key, keyMagazijnlocatie.

GUID: `EAID_703CAFCF_FDC0_4861_AA76_1692303DE7BE`

Relaties:

- staat op → Magazijnlocatie (*Association*, 0..* → 1..1, `EAID_EFA6E5A8_4A4A_4fc8_89C5_6DFDB6186DB4`)

## Kaart

De geografische weergave van een gedeelte van het aardoppervlak

Attributen: naam, omschrijving, content.

GUID: `EAID_F28DDE36_7BE4_45f7_A820_FFF0261CAA4E`

## locatie

Een specifieke plaats

Attributen: locatiePunt.

GUID: `EAID_F25EE5A8_2CF4_498b_8DAD_8EEE48FAF3A5`

## Magazijnlocatie

Locatie van een magazijn

Attributen: vaknummer, volgletter, key, stelling.

GUID: `EAID_4C1543FD_250B_4291_9B23_BC9D3D9C0C4A`

## Magazijnplaatsing

Het ergens neerzetten van een object in een magazijn.

Attributen: uitgeleend, beschrijving, datumGeplaatst, key, keyDoos, keyMagazijnlocatie, projectCD, herkomst.

GUID: `EAID_F954FB72_AE88_4a0e_A3D8_555FCF8D9C9F`

Relaties:

- zit in → Doos (*Association*, 0..1 → 0..*, `EAID_09CA27B3_BF50_45a5_8708_65E789BB518C`)
- staat op → Magazijnlocatie (*Association*, 0..* → 0..1, `EAID_8C0C6E8C_2CFD_4f2b_95DB_6417D1A1398D`)
- hoort bij → Project (*Association*, 0..* → 0..1, `EAID_CAEF36F1_E915_4dc3_BFA4_53FD9C8F5E33`)

## Project

Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat.

Attributen: projectCD, naam, datumStart, datumEinde, naamcode, toponiem, locatie, coordinaten, jaarVan, jaarTot, trefwoorden.

GUID: `EAID_E42A32F7_262F_4005_9EB9_4674B76E8825`

Relaties:

- heeft → Archeologiebesluit (*Association*, 1..1 → 0..*, `EAID_4610B0AB_0D86_42ab_9619_8B78B5EAB332`)
- heeft → boring (*Association*, 1..1 → 0..*, `EAID_754FC6C1_D7B3_4b3d_9991_8DD4AA00CCC1`)
- wordt begrensd door → locatie (*Association*, 0..* → 1..*, `EAID_7C1BBED5_4316_433a_A13D_CB353DB9B13C`)
- heeft → Put (*Association*, 1..1 → 0..*, `EAID_7356FAC0_F183_494b_948D_5DFC47CC5522`)
- vastlegging → Document (*Usage*,  → , `EAID_4471950A_BB45_415e_8BD3_B6EAB33AA5CC`)

## Put

Grondspoor, veelal verstevigd en gefundeerd aangelegd, bedoeld voor de tijdelijke opslag van danwel water (waterput) danwel uitwerpselen en afval (beerput).

Attributen: projectCD, putnummer, key.

GUID: `EAID_17286CE1_21F2_454b_95A6_3E4C0C6E2453`

Relaties:

- heeft locatie → locatie (*Association*, 0..* → 1..*, `EAID_0EB0ABE6_4A54_48ad_8B51_41EBF75F8EF1`)
- heeft → Vlak (*Association*, 1..1 → 0..*, `EAID_E1790157_80B5_4537_BEDB_FB6A0AEB3A56`)

## Spoor

Een blijk van eerdere aanwezigheid.

Attributen: projectCD, putnummer, vlaknummer, spoornummer, hoogteBoven, hoogteOnder, aard, datering, datum, vorm, beschrijving, key, keyVlak.

GUID: `EAID_14939C33_2DCE_41bf_A2BE_FF1EDD292FE7`

Relaties:

- heeft → Vulling (*Association*, 1..1 → 0..*, `EAID_C1012227_462A_41ec_AF20_53B78105C045`)

## Stelling

Een systeem om goederen op te slaan die worden vervoerd en opgeslagen op pallets, in bundels of per stuk.(Wikipedia)

Attributen: stellingcode, inhoud.

GUID: `EAID_382D408F_41A3_49d2_9F66_DFFA6C75590D`

Relaties:

- heeft → Magazijnlocatie (*Association*, 1..1 → 0..*, `EAID_9DE067E7_2305_4f08_86EA_E5AF550E336F`)

## Vindplaats

Een plek waar men iets gevonden heeft.

Attributen: projectcode, locatie, vindplaatsOmschrijving, gemeente, datering, begindatering, einddatering, aard, onderzoek, mobilia, depot, documentatie, bibliografie, beschrijving.

GUID: `EAID_84DED9A9_2D33_4a77_94F2_29657024590F`

Relaties:

- hoort bij → Project (*Association*, 0..1 → 1, `EAID_C0088790_7E28_4d9e_AEA3_ED3243330D49`)

## Vlak

Plat, oneindig oppervlak of variëteit zonder enige kromming.

Attributen: projectCD, putnummer, vlaknummer, diepteVan, diepteTot, key, keyPut.

GUID: `EAID_0644BD52_8C2B_462d_94B9_9C99908952F5`

Relaties:

- heeft → Spoor (*Association*, 1..1 → 0..*, `EAID_65B9846F_78F1_46f7_B8BB_7A022AB7FEA2`)

## Vondst

Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument

Attributen: projectCD, vondstnummer, putnummer, vlaknummer, spoornummer, vullingnummer, omstandigheden, omschrijving, key, keyVulling, datum, XCoordinaat, YCoordinaat.

GUID: `EAID_F8283401_70F8_41b8_A97C_32A9074AD4B1`

Relaties:

- bevat → Artefact (*Association*, 0..1 → 0..*, `EAID_F624D2ED_D364_4c68_A21F_606BF07EC1A3`)

## Vulling

Dunne wegeringsplank gebruikt om de ruimte tussen de bovenste kimweger en de onderste balkweger op te vullen (Sopers, 1974).

Attributen: projectCD, putnummer, vlaknummer, spoornummer, vullingnummer, grondsoort, kleur, structuur, key, keySpoor.

GUID: `EAID_8417459E_2193_44a2_A1AC_38C39EA93CBF`

Relaties:

- heeft → Vondst (*Association*, 1..1 → 0..*, `EAID_9E33A846_9576_4387_8887_CF26687CAA07`)
