<!-- gegenereerd door tools/ggm.py; hash: 58658e9c73285ec5643a29c342346eabc87e98f72ea8efa3b065a7d4fd1d6e00 -->
# Leerplicht en Leerlingenvervoer

Taakveld: 4 Onderwijs. Alleen objecttypen; letterlijke definities uit het GGM.

## Aanvraag Leerlingenvervoer

Een aanvraag voor een leerling die recht heeft op vervoer van en naar onderwijs.

GUID: `EAID_07F40D10_74AC_4f56_8B71_A236A63C2122`

## AanvraagOfMelding

Komt overeen met een VJV

Attributen: datum, opmerkingen, soortVerzuimOfAanvraag, reden.

GUID: `EAID_66E2B5BA_44A0_4fde_AE33_E211EE4832C2`

Relaties:

- leidt tot → Beslissing (*Association*, 0..1 → 0..1, `EAID_4D75AD5B_9FC4_4e2d_9C3B_A3ED4EDFB067`)
- betreft → Leerling (*Association*, 0..* → 1, `EAID_48E22FD5_48A0_4b73_8F26_F9BCC6219B30`)
- betreft → School (*Association*, 0..* → 0..1, `EAID_C9573A24_CBB6_4eef_80CA_B9BDB0AE36CE`)
- → AanvraagOfMelding (*Generalization*,  → , `EAID_F3716261_00DA_4215_8CE5_E87EC68DB622`)

## AanvraagVrijstelling

Vrijstelling van een aanvraag voor leerlingenvervoer

Attributen: datumAanvraag, buitenlandseSchoollocatie.

GUID: `EAID_450F47A7_758F_400c_82EB_05535EBDD426`

Relaties:

- → AanvraagOfMelding (*Generalization*,  → , `EAID_6610A986_57EF_4b25_BB8D_5BCD606A5E52`)

## Beschikking Leerlingenvervoer

Een formeel besluit dat genomen wordt door een bevoegde instantie over het al dan niet toekennen van leerlingenvervoer aan een bepaalde leerling.

GUID: `EAID_81870665_768C_4fb2_8A4F_A9CB7989C884`

Relaties:

- vervoerder → Vervoerder (*Association*, 0..* → 0..*, `EAID_EEB8F903_7B09_4df8_B1A2_7E28DD02269F`)
- → Beslissing (*Generalization*,  → , `EAID_F42E2F80_5BFB_4c4f_86CB_CF56FDC2DC02`)

## Beslissing

Selectie van een voorstelbare werkelijkheid (voorkeursvariant) uit een aantal mogelijke werkelijkheden (varianten) op basis van een verzameling van criteria.

Attributen: datum, reden, opmerkingen.

GUID: `EAID_B65280CD_3429_4966_AD2D_CB3EE76EE2E8`

Relaties:

- betreft → Leerling (*Association*, 0..* → 1, `EAID_5CD65CEA_FA82_48e6_AE24_33C9638A1BE3`)
- behandelaar → Leerplichtambtenaar (*Association*, 0..* → 1, `EAID_610BCAE9_CF8A_4f13_9BE5_8CA2F4E5A937`)
- betreft → School (*Association*, 0..* → 0..1, `EAID_EAE2E17D_3BF0_41ec_8ADC_0EED4B925F6D`)

## Doorgeleiding OM

De overdracht van een leerplichtzaak aan het Openbaar Ministerie voor juridische vervolging.

Attributen: afdoening.

GUID: `EAID_90E49701_2A06_4669_9199_6FCFDFCA707A`

Relaties:

- verantwoordelijk ouder → Ouder Of Verzorger (*Association*, 0..* → 0..*, `EAID_40A5CCFA_BC16_4bd5_BAE7_4DE44F139081`)
- → Beslissing (*Generalization*,  → , `EAID_97F65B17_8224_4d6a_BAD5_386318B4E64D`)

## HALT-verwijzing

Jongeren van 12 tot 18 jaar die strafbare feiten plegen, zoals bijvoorbeeld: winkeldiefstal, vernieling, openbaar dronkenschap of oplichting kunnen naar Halt worden verwezen. In sommige gevallen is daarvoor toestemming nodig van het Openbaar Ministerie.

Attributen: afdoening, datumRetour, datumMutatie, memo.

GUID: `EAID_70E3C6AF_1117_4cfc_B61F_0D168010FFB9`

Relaties:

- → Beslissing (*Generalization*,  → , `EAID_140A039F_3BE5_4f0f_B506_40EEFEA11323`)

## Klacht Leerlingenvervoer

Een uiting van ontevredenheid over het vervoer van leerlingen.

GUID: `EAID_07FE66E8_8316_406b_A590_922C2E7B4305`

Relaties:

- betreft → Leerling (*Association*, 0..* → 1..1, `EAID_26655188_F699_4467_B728_12C6D42B61DF`)
- betreft → Vervoerder (*Association*, 0..* → 1, `EAID_D6AE47CD_3BE5_492a_A143_A29C3B3F38EA`)

## Leerplichtambtenaar

Ambtenaar die toezicht houdt op de uitvoering van de leerplichtwet.

GUID: `EAID_B369B374_F560_4ea6_9A8B_DBBCB4961EFF`

Relaties:

- opgelegd door → Procesverbaal Onderwijs (*Association*, 1..1 → 0..*, `EAID_394820AC_FA0B_45c2_8E87_64DADE538231`)
- → Medewerker (*Generalization*,  → , `EAID_D81DDF18_5F40_4f5d_9520_CEB15BF26394`)

## Procesverbaal Onderwijs

Een officieel document dat een overtreding van de leerplichtwet vastlegt.

Attributen: reden, opmerkingen, datumIngelicht, sanctiesoort, uitspraak, proeftijd, geldboete, verzuimsoort, datumZitting, datumAfgehandeld, datumUitspraak, datumEindeProeftijd, geldboeteVoorwaardelijk.

GUID: `EAID_697F1730_B439_4b35_8799_1B2E9AB04548`

Relaties:

- verantwoordelijke ouder → Ouder Of Verzorger (*Association*, 0..* → 1..*, `EAID_1B912C26_ACAD_49a8_B48D_1F1D8B8BFD26`)
- → Beslissing (*Generalization*,  → , `EAID_1B05EE50_C227_4105_A8EF_BAC608792E54`)

## Verlofaanvraag

Een verzoek om toestemming te krijgen iets te doen, bijvoorbeeld vakantie of studie

Attributen: datumStart, datumTot, soortVerlof.

GUID: `EAID_E9DECE41_F7F5_49f1_94B5_63DE941F6094`

Relaties:

- → AanvraagOfMelding (*Generalization*,  → , `EAID_654A0103_3CC2_4580_9F2C_EE4E8E2C0AF1`)

## Vervoerder

Degene die openbaar vervoer of besloten busvervoer verricht, niet in de hoedanigheid van bestuurder van een auto, bus, trein, metro, tram of een via een geleidesysteem voortbewogen voertuig.

GUID: `EAID_613E192A_D0F2_4e67_BE73_51C09197EE3D`

Relaties:

- → Leverancier (*Generalization*,  → , `EAID_EFC8F306_37BD_43d2_856F_28BF3A5B85A6`)

## Verzuimmelding

Een melding dat een leerling niet op school verschijnt. De school moet actie ondernemen naar de leerling (en zijn ouders). Een school moet het verzuim melden bij de gemeente.

Attributen: datumStart, datumEinde, voorstelSchool.

GUID: `EAID_252C70B1_4E02_4033_B2B5_86F65496D7AB`

Relaties:

- heeft → School (*Association*, 0..* → 1..1, `EAID_744F71E2_CC6B_48ae_9683_DCAC2E276019`)
- → AanvraagOfMelding (*Generalization*,  → , `EAID_A2FD81A4_C8A2_4f5f_8C26_CEB12E0C6D0D`)

## Vrijstelling

Een formeel besluit waarbij een leerling wordt ontheven van de leerplicht.

Attributen: datumStart, datumEinde, aanvraagToegekend, verzuimsoort, buitenlandseSchoollocatie.

GUID: `EAID_B8584CD2_A54A_4a59_82B6_A597A0864CFA`

Relaties:

- heeft → School (*Association*, 0..* → 1..1, `EAID_5DBF09CA_CB0A_42e4_A90A_3BAAD6B7E95E`)
- → Beslissing (*Generalization*,  → , `EAID_7B3B179E_1F43_4cd6_864A_08033CF2A7FD`)

## Ziekmelding Leerlingenvervoer

Een melding van een zieke leerling die recht heeft op vervoer van en naar onderwijs.

GUID: `EAID_7689A6B7_2A9E_42db_A028_E4601305DBFF`
