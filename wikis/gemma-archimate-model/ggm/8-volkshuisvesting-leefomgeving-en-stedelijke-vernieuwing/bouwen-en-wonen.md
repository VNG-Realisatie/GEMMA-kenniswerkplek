<!-- gegenereerd door tools/ggm.py; hash: c62bcec3f62abc5a4ae94aee99a15f654364fcb2b5b31ef44c36cd45d194a946 -->
# Bouwen en Wonen

Taakveld: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing. Alleen objecttypen; letterlijke definities uit het GGM.

## Gebouw

Een complex van ruimten uitsluitend bedoeld voor de huisvesting van een afzonderlijk huishouden

Attributen: aantal, aantalAdressen, aantalKamers, energielabel, oppervlakte, duurzaam, natuurinclusief, regenwater, aardgasloos.

GUID: `EAID_681DB26F_D779_4796_B467_576E5A25F581`

## Huurwoningen

Wen woning die de bewoner huurt van de eigenaar, veelal een woningcorporatie of een particulier.

Attributen: huurprijs.

GUID: `EAID_E0F7D3A0_46C8_4e70_AA10_3888B60D14C0`

Relaties:

- → Gebouw (*Generalization*,  → , `EAID_1646F826_1B9C_483e_AF6D_592A6B4ECF39`)

## Koopwoningen

Een woning die eigendom is van een particulier (in het algemeen de bewoner van de woning).

Attributen: koopprijs.

GUID: `EAID_7FECB5B2_E6CB_4637_9FD4_6EBA2CA96BBA`

Relaties:

- → Gebouw (*Generalization*,  → , `EAID_F73997E8_7D9F_4abc_B8BA_EBB8657BF6DE`)

## Plan

Project waarin woningen worden gerealiseerd

Attributen: naam, nummer, aardgasloos, gebiedstransformatie, intentie, bestemmingGoedgekeurd, onherroepelijk, eigendomGemeente, 70ProcentVerkocht, startVerkoop, startbouw, eersteOplevering, laatsteOplevering, percelen.

GUID: `EAID_D857E285_1EA3_4ba3_9614_5FACAC8BA133`

Relaties:

- Bestaat uit → Gebouw (*Association*, 1 → 1..*, `EAID_E5612426_29C1_41dc_9289_1E7583EE153E`)

## Projectleider

De persoon die een project aanstuurt

Attributen: naam.

GUID: `EAID_888BBB4F_BEBA_4b9a_BB2E_0E1F2A3606DF`

Relaties:

- is projectleider van → Plan (*Association*, 0..1 → 0..*, `EAID_BCAFF0F6_3351_45ae_BD46_EA29D08AB8B5`)
- → NatuurlijkPersoon (*Generalization*,  → , `EAID_3CDFB4A1_F4F8_4bb3_9F9B_EE617BE46331`)

## Projectontwikkelaar

Een persoon of een firma die een project ontwikkelt voor financieel gewin.

Attributen: naam, adres.

GUID: `EAID_6BBB2AE0_6F42_4676_8C6C_E727032F5F47`

Relaties:

- heeft → Plan (*Association*, 1..* → 0..*, `EAID_0695940F_CBA6_466e_8F9C_6E37C74771AE`)
- → NietNatuurlijkPersoon (*Generalization*,  → , `EAID_7C9D2F13_7FA5_40bd_ABC4_6535F6692831`)

## Studentenwoningen

Een woning waar uitsluitend (meerdere) studenten (of soms ook werkende jongeren) een woongemeenschap vorme

Attributen: zelfstandig, huurprijs.

GUID: `EAID_98C74EAB_3411_4d1a_8321_FF30567B6877`

Relaties:

- → Gebouw (*Generalization*,  → , `EAID_5EBC4BCB_52AB_4330_AE72_FBD108CDB3BA`)
