<!-- gegenereerd door tools/ggm.py; hash: e8a31b4c70a567431f5768106d15daa36393b7dffe54e832d78039514a243277 -->
# Bouwen en Wonen

Taakveld: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Gebouw | `EAID_681DB26F_D779_4796_B467_576E5A25F581` | Een complex van ruimten uitsluitend bedoeld voor de huisvesting van een afzonderlijk huishouden | aantal, aantalAdressen, aantalKamers, energielabel, oppervlakte, duurzaam, natuurinclusief, regenwater, aardgasloos |
| Huurwoningen | `EAID_E0F7D3A0_46C8_4e70_AA10_3888B60D14C0` | Wen woning die de bewoner huurt van de eigenaar, veelal een woningcorporatie of een particulier. | huurprijs |
| Koopwoningen | `EAID_7FECB5B2_E6CB_4637_9FD4_6EBA2CA96BBA` | Een woning die eigendom is van een particulier (in het algemeen de bewoner van de woning). | koopprijs |
| Plan | `EAID_D857E285_1EA3_4ba3_9614_5FACAC8BA133` | Project waarin woningen worden gerealiseerd | naam, nummer, aardgasloos, gebiedstransformatie, intentie, bestemmingGoedgekeurd, onherroepelijk, eigendomGemeente, 70ProcentVerkocht, startVerkoop, startbouw, eersteOplevering, laatsteOplevering, percelen |
| Projectleider | `EAID_888BBB4F_BEBA_4b9a_BB2E_0E1F2A3606DF` | De persoon die een project aanstuurt | naam |
| Projectontwikkelaar | `EAID_6BBB2AE0_6F42_4676_8C6C_E727032F5F47` | Een persoon of een firma die een project ontwikkelt voor financieel gewin. | naam, adres |
| Studentenwoningen | `EAID_98C74EAB_3411_4d1a_8321_FF30567B6877` | Een woning waar uitsluitend (meerdere) studenten (of soms ook werkende jongeren) een woongemeenschap vorme | zelfstandig, huurprijs |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Huurwoningen | Generalization |  | Gebouw |  →  | `EAID_1646F826_1B9C_483e_AF6D_592A6B4ECF39` |  |
| Koopwoningen | Generalization |  | Gebouw |  →  | `EAID_F73997E8_7D9F_4abc_B8BA_EBB8657BF6DE` |  |
| Plan | Association | Bestaat uit | Gebouw | 1 → 1..* | `EAID_E5612426_29C1_41dc_9289_1E7583EE153E` |  |
| Projectleider | Association | is projectleider van | Plan | 0..1 → 0..* | `EAID_BCAFF0F6_3351_45ae_BD46_EA29D08AB8B5` |  |
| Projectleider | Generalization |  | NatuurlijkPersoon |  →  | `EAID_3CDFB4A1_F4F8_4bb3_9F9B_EE617BE46331` |  |
| Projectontwikkelaar | Association | heeft | Plan | 1..* → 0..* | `EAID_0695940F_CBA6_466e_8F9C_6E37C74771AE` |  |
| Projectontwikkelaar | Generalization |  | NietNatuurlijkPersoon |  →  | `EAID_7C9D2F13_7FA5_40bd_ABC4_6535F6692831` |  |
| Studentenwoningen | Generalization |  | Gebouw |  →  | `EAID_5EBC4BCB_52AB_4330_AE72_FBD108CDB3BA` |  |
