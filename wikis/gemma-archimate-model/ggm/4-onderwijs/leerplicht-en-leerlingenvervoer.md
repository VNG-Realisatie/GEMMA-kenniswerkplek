<!-- gegenereerd door tools/ggm.py; hash: 630b330240038427cc594bf2e683ee154a4ccc9dba58e03964be47558e55b7a4 -->
# Leerplicht en Leerlingenvervoer

Taakveld: 4 Onderwijs. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Aanvraag Leerlingenvervoer | `EAID_07F40D10_74AC_4f56_8B71_A236A63C2122` | Een aanvraag voor een leerling die recht heeft op vervoer van en naar onderwijs. |  |
| AanvraagOfMelding | `EAID_66E2B5BA_44A0_4fde_AE33_E211EE4832C2` | Komt overeen met een VJV | datum, opmerkingen, soortVerzuimOfAanvraag, reden |
| AanvraagVrijstelling | `EAID_450F47A7_758F_400c_82EB_05535EBDD426` | Vrijstelling van een aanvraag voor leerlingenvervoer | datumAanvraag, buitenlandseSchoollocatie |
| Beschikking Leerlingenvervoer | `EAID_81870665_768C_4fb2_8A4F_A9CB7989C884` | Een formeel besluit dat genomen wordt door een bevoegde instantie over het al dan niet toekennen van leerlingenvervoer aan een bepaalde leerling. |  |
| Beslissing | `EAID_B65280CD_3429_4966_AD2D_CB3EE76EE2E8` | Selectie van een voorstelbare werkelijkheid (voorkeursvariant) uit een aantal mogelijke werkelijkheden (varianten) op basis van een verzameling van criteria. | datum, reden, opmerkingen |
| Doorgeleiding OM | `EAID_90E49701_2A06_4669_9199_6FCFDFCA707A` | De overdracht van een leerplichtzaak aan het Openbaar Ministerie voor juridische vervolging. | afdoening |
| HALT-verwijzing | `EAID_70E3C6AF_1117_4cfc_B61F_0D168010FFB9` | Jongeren van 12 tot 18 jaar die strafbare feiten plegen, zoals bijvoorbeeld: winkeldiefstal, vernieling, openbaar dronkenschap of oplichting kunnen naar Halt worden verwezen. In sommige gevallen is daarvoor toestemming nodig van het Openbaar Ministerie. | afdoening, datumRetour, datumMutatie, memo |
| Klacht Leerlingenvervoer | `EAID_07FE66E8_8316_406b_A590_922C2E7B4305` | Een uiting van ontevredenheid over het vervoer van leerlingen. |  |
| Leerplichtambtenaar | `EAID_B369B374_F560_4ea6_9A8B_DBBCB4961EFF` | Ambtenaar die toezicht houdt op de uitvoering van de leerplichtwet. |  |
| Procesverbaal Onderwijs | `EAID_697F1730_B439_4b35_8799_1B2E9AB04548` | Een officieel document dat een overtreding van de leerplichtwet vastlegt. | reden, opmerkingen, datumIngelicht, sanctiesoort, uitspraak, proeftijd, geldboete, verzuimsoort, datumZitting, datumAfgehandeld, datumUitspraak, datumEindeProeftijd, geldboeteVoorwaardelijk |
| Verlofaanvraag | `EAID_E9DECE41_F7F5_49f1_94B5_63DE941F6094` | Een verzoek om toestemming te krijgen iets te doen, bijvoorbeeld vakantie of studie | datumStart, datumTot, soortVerlof |
| Vervoerder | `EAID_613E192A_D0F2_4e67_BE73_51C09197EE3D` | Degene die openbaar vervoer of besloten busvervoer verricht, niet in de hoedanigheid van bestuurder van een auto, bus, trein, metro, tram of een via een geleidesysteem voortbewogen voertuig. |  |
| Verzuimmelding | `EAID_252C70B1_4E02_4033_B2B5_86F65496D7AB` | Een melding dat een leerling niet op school verschijnt. De school moet actie ondernemen naar de leerling (en zijn ouders). Een school moet het verzuim melden bij de gemeente. | datumStart, datumEinde, voorstelSchool |
| Vrijstelling | `EAID_B8584CD2_A54A_4a59_82B6_A597A0864CFA` | Een formeel besluit waarbij een leerling wordt ontheven van de leerplicht. | datumStart, datumEinde, aanvraagToegekend, verzuimsoort, buitenlandseSchoollocatie |
| Ziekmelding Leerlingenvervoer | `EAID_7689A6B7_2A9E_42db_A028_E4601305DBFF` | Een melding van een zieke leerling die recht heeft op vervoer van en naar onderwijs. |  |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| AanvraagOfMelding | Association | betreft | Leerling | 0..* → 1 | `EAID_48E22FD5_48A0_4b73_8F26_F9BCC6219B30` |  |
| AanvraagOfMelding | Association | leidt tot | Beslissing | 0..1 → 0..1 | `EAID_4D75AD5B_9FC4_4e2d_9C3B_A3ED4EDFB067` |  |
| AanvraagOfMelding | Association | betreft | School | 0..* → 0..1 | `EAID_C9573A24_CBB6_4eef_80CA_B9BDB0AE36CE` |  |
| AanvraagOfMelding | Generalization |  | AanvraagOfMelding |  →  | `EAID_F3716261_00DA_4215_8CE5_E87EC68DB622` |  |
| AanvraagVrijstelling | Generalization |  | AanvraagOfMelding |  →  | `EAID_6610A986_57EF_4b25_BB8D_5BCD606A5E52` |  |
| Beschikking Leerlingenvervoer | Association | vervoerder | Vervoerder | 0..* → 0..* | `EAID_EEB8F903_7B09_4df8_B1A2_7E28DD02269F` |  |
| Beschikking Leerlingenvervoer | Generalization |  | Beslissing |  →  | `EAID_F42E2F80_5BFB_4c4f_86CB_CF56FDC2DC02` |  |
| Beslissing | Association | betreft | Leerling | 0..* → 1 | `EAID_5CD65CEA_FA82_48e6_AE24_33C9638A1BE3` |  |
| Beslissing | Association | behandelaar | Leerplichtambtenaar | 0..* → 1 | `EAID_610BCAE9_CF8A_4f13_9BE5_8CA2F4E5A937` |  |
| Beslissing | Association | betreft | School | 0..* → 0..1 | `EAID_EAE2E17D_3BF0_41ec_8ADC_0EED4B925F6D` |  |
| Doorgeleiding OM | Association | verantwoordelijk ouder | Ouder Of Verzorger | 0..* → 0..* | `EAID_40A5CCFA_BC16_4bd5_BAE7_4DE44F139081` |  |
| Doorgeleiding OM | Generalization |  | Beslissing |  →  | `EAID_97F65B17_8224_4d6a_BAD5_386318B4E64D` |  |
| HALT-verwijzing | Generalization |  | Beslissing |  →  | `EAID_140A039F_3BE5_4f0f_B506_40EEFEA11323` |  |
| Klacht Leerlingenvervoer | Association | betreft | Leerling | 0..* → 1..1 | `EAID_26655188_F699_4467_B728_12C6D42B61DF` |  |
| Klacht Leerlingenvervoer | Association | betreft | Vervoerder | 0..* → 1 | `EAID_D6AE47CD_3BE5_492a_A143_A29C3B3F38EA` |  |
| Leerplichtambtenaar | Association | opgelegd door | Procesverbaal Onderwijs | 1..1 → 0..* | `EAID_394820AC_FA0B_45c2_8E87_64DADE538231` |  |
| Leerplichtambtenaar | Generalization |  | Medewerker |  →  | `EAID_D81DDF18_5F40_4f5d_9520_CEB15BF26394` |  |
| Procesverbaal Onderwijs | Association | verantwoordelijke ouder | Ouder Of Verzorger | 0..* → 1..* | `EAID_1B912C26_ACAD_49a8_B48D_1F1D8B8BFD26` |  |
| Procesverbaal Onderwijs | Generalization |  | Beslissing |  →  | `EAID_1B05EE50_C227_4105_A8EF_BAC608792E54` |  |
| Verlofaanvraag | Generalization |  | AanvraagOfMelding |  →  | `EAID_654A0103_3CC2_4580_9F2C_EE4E8E2C0AF1` |  |
| Vervoerder | Generalization |  | Leverancier |  →  | `EAID_EFC8F306_37BD_43d2_856F_28BF3A5B85A6` |  |
| Verzuimmelding | Association | heeft | School | 0..* → 1..1 | `EAID_744F71E2_CC6B_48ae_9683_DCAC2E276019` |  |
| Verzuimmelding | Generalization |  | AanvraagOfMelding |  →  | `EAID_A2FD81A4_C8A2_4f5f_8C26_CEB12E0C6D0D` |  |
| Vrijstelling | Association | heeft | School | 0..* → 1..1 | `EAID_5DBF09CA_CB0A_42e4_A90A_3BAAD6B7E95E` |  |
| Vrijstelling | Generalization |  | Beslissing |  →  | `EAID_7B3B179E_1F43_4cd6_864A_08033CF2A7FD` |  |
