<!-- gegenereerd door tools/ggm.py; hash: d4209b1a8619c3a4e1a0f0e71e16f3076535242029876076d3806679c91fb976 -->
# Sociale Teams

Taakveld: 6 Sociaal Domein. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Behandeling | `EAID_1B8CF61F_3039_4fc5_A57D_B758170FCA0E` | Een verzameling van interventies om bepaalde behandeldoelen te bewerkstelligen. | datumStart, datumEinde, toelichting |
| Behandelsoort | `EAID_4F518962_5EA3_4f56_8379_3A835FFE84CA` | Typering van een behandeling | naam, omschrijving |
| Bijzonderheid | `EAID_77A962E5_889A_4af6_ADFD_37C3EE8C48F0` | Kenmerkende eigenschap | omschrijving |
| Bijzonderheidsoort | `EAID_03BB6341_7C3E_4a4b_9207_6A2EB9D116FE` | Typering van een bijzonderheid | naam, omschrijving |
| Caseaanmelding | `EAID_294E3981_C1EF_451e_AE2B_758EC4E4B284` | Verzoek tot toelating | datum |
| Doelstelling | `EAID_28C572B5_C147_4b99_B920_00062C843FDE` | Een op korte of middellange termijn nagestreefde situatie | omschrijving |
| Doelstellingsoort | `EAID_79A14AF2_F1F9_43a3_914B_FD04CB609F44` | Typering van een doelstellig | naam, omschrijving |
| SociaalTeamDossier | `EAID_A22B8038_3C04_44a7_8E75_90A3A5E2615B` | SociaalTeamDossier* is een dossier-entiteit binnen het Model Sociale Teams dat de **geïntegreerde registratie van gegevens over ondersteuning, gesprekken, interventies en casusontwikkeling van een sociaal team** voor een inwoner of gezin omvat. | datumStart, omschrijving, datumEinde, status, datumVaststelling |
| SociaalteamDossiersoort | `EAID_E81990BA_1B6E_4e2a_9910_1E02CDDD53A6` | *SociaalteamDossiersoort* is de classificatie van een *SociaalTeamDossier* die aangeeft **het type of de categorie van het dossier** binnen de context van sociale ondersteuning en casemanagement in een sociaal team. | naam, omschrijving |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Behandeling | Association | is van soort | Behandelsoort | 0..* → 1..1 | `EAID_FDDAA5BD_12FD_4301_8601_F758417272CC` |  |
| Bijzonderheid | Association | is van soort | Bijzonderheidsoort | 0..* → 1..1 | `EAID_9EB392F7_17AF_488e_9A25_F6F50C22C142` |  |
| Doelstelling | Association | is van soort | Doelstellingsoort | 0..* → 1..1 | `EAID_F3D8FF7E_2CB8_46e1_9A48_452F97414C61` |  |
| SociaalTeamDossier | Association | heeft bijzonderheid | Bijzonderheid | 1..1 → 0..* | `EAID_507E6CB0_8844_4a39_AA86_7DE0A88CC0DB` |  |
| SociaalTeamDossier | Association | heeft doelstelling | Doelstelling | 1..1 → 0..* | `EAID_51748CAF_E7CE_4ce8_9897_DE5549EF0F09` |  |
| SociaalTeamDossier | Association | heeft behandeling | Behandeling | 1..1 → 0..* | `EAID_6D7DECEC_F17A_4ecb_B263_9AA07C56EF1E` |  |
| SociaalTeamDossier | Association | heeft betrokkenen | Relatie | 0..* → 0..* | `EAID_A72380B2_780A_4384_95FA_753AB757EF02` |  |
| SociaalTeamDossier | Association | heeft aanmelding | Caseaanmelding | 0..1 → 0..1 | `EAID_C49D501E_CC39_4b11_9579_7B0A180B98DD` |  |
| SociaalTeamDossier | Association | heeft soort | SociaalteamDossiersoort | 0..* → 1..1 | `EAID_E15D5C66_CF29_438f_8E91_3427CB747057` |  |
