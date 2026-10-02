<!-- gegenereerd door tools/ggm.py; hash: 8f8aa2e54e194115a530ebcc44649011538575cdeadcae59502d491595ab7031 -->
# Sociale Teams

Taakveld: 6 Sociaal Domein. Alleen objecttypen; letterlijke definities uit het GGM.

## Behandeling

Een verzameling van interventies om bepaalde behandeldoelen te bewerkstelligen.

Attributen: datumStart, datumEinde, toelichting.

GUID: `EAID_1B8CF61F_3039_4fc5_A57D_B758170FCA0E`

Relaties:

- is van soort → Behandelsoort (*Association*, 0..* → 1..1, `EAID_FDDAA5BD_12FD_4301_8601_F758417272CC`)

## Behandelsoort

Typering van een behandeling

Attributen: naam, omschrijving.

GUID: `EAID_4F518962_5EA3_4f56_8379_3A835FFE84CA`

## Bijzonderheid

Kenmerkende eigenschap

Attributen: omschrijving.

GUID: `EAID_77A962E5_889A_4af6_ADFD_37C3EE8C48F0`

Relaties:

- is van soort → Bijzonderheidsoort (*Association*, 0..* → 1..1, `EAID_9EB392F7_17AF_488e_9A25_F6F50C22C142`)

## Bijzonderheidsoort

Typering van een bijzonderheid

Attributen: naam, omschrijving.

GUID: `EAID_03BB6341_7C3E_4a4b_9207_6A2EB9D116FE`

## Caseaanmelding

Verzoek tot toelating

Attributen: datum.

GUID: `EAID_294E3981_C1EF_451e_AE2B_758EC4E4B284`

## Doelstelling

Een op korte of middellange termijn nagestreefde situatie

Attributen: omschrijving.

GUID: `EAID_28C572B5_C147_4b99_B920_00062C843FDE`

Relaties:

- is van soort → Doelstellingsoort (*Association*, 0..* → 1..1, `EAID_F3D8FF7E_2CB8_46e1_9A48_452F97414C61`)

## Doelstellingsoort

Typering van een doelstellig

Attributen: naam, omschrijving.

GUID: `EAID_79A14AF2_F1F9_43a3_914B_FD04CB609F44`

## SociaalTeamDossier

SociaalTeamDossier* is een dossier-entiteit binnen het Model Sociale Teams dat de **geïntegreerde registratie van gegevens over ondersteuning, gesprekken, interventies en casusontwikkeling van een sociaal team** voor een inwoner of gezin omvat.

Attributen: datumStart, omschrijving, datumEinde, status, datumVaststelling.

GUID: `EAID_A22B8038_3C04_44a7_8E75_90A3A5E2615B`

Relaties:

- heeft behandeling → Behandeling (*Association*, 1..1 → 0..*, `EAID_6D7DECEC_F17A_4ecb_B263_9AA07C56EF1E`)
- heeft bijzonderheid → Bijzonderheid (*Association*, 1..1 → 0..*, `EAID_507E6CB0_8844_4a39_AA86_7DE0A88CC0DB`)
- heeft aanmelding → Caseaanmelding (*Association*, 0..1 → 0..1, `EAID_C49D501E_CC39_4b11_9579_7B0A180B98DD`)
- heeft doelstelling → Doelstelling (*Association*, 1..1 → 0..*, `EAID_51748CAF_E7CE_4ce8_9897_DE5549EF0F09`)
- heeft betrokkenen → Relatie (*Association*, 0..* → 0..*, `EAID_A72380B2_780A_4384_95FA_753AB757EF02`)
- heeft soort → SociaalteamDossiersoort (*Association*, 0..* → 1..1, `EAID_E15D5C66_CF29_438f_8E91_3427CB747057`)

## SociaalteamDossiersoort

*SociaalteamDossiersoort* is de classificatie van een *SociaalTeamDossier* die aangeeft **het type of de categorie van het dossier** binnen de context van sociale ondersteuning en casemanagement in een sociaal team.

Attributen: naam, omschrijving.

GUID: `EAID_E81990BA_1B6E_4e2a_9910_1E02CDDD53A6`
