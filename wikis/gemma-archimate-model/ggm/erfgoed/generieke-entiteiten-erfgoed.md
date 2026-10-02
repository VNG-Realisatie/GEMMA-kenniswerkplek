<!-- gegenereerd door tools/ggm.py; hash: 9ec8f72ba5e104e19e00d66a63be6149555fdff10770637ece35a93b8ac99d35 -->
# Generieke Entiteiten Erfgoed

Taakveld: Erfgoed. Alleen objecttypen; letterlijke definities uit het GGM.

## Erfgoed Object

Uit het verleden geërfde materiële en immateriële objecten

Attributen: titel, omschrijving, dateringVanaf, dateringTot.

GUID: `EAID_71A5C565_C2CC_495f_910A_76C199C6AF0E`

Relaties:

- valt binnen → Objectclassificatie (*Association*, 0..* → 0..*, `EAID_C3745FB4_D387_4ccc_8B35_F89C76EBC4F1`)

## Historisch Persoon

Natuurlijk persoon waarvan informatie beschikbaar is uit het verleden.

Attributen: naam, datumGeboorte, datumOverlijden, omschrijving, woondeOp, beroep, publiekToegankelijk.

GUID: `EAID_3BBB3264_592A_4d8c_A741_C2A3C38E3932`

Relaties:

- speelt rol in → Erfgoed Object (*Association*, 0..* → 0..*, `EAID_6D8C062B_73D8_40c4_8C1B_497F39295AF0`)
- → NatuurlijkPersoon (*Generalization*,  → , `EAID_DF9C3B5F_5A7B_43e8_A620_3E8B9CB3CE1E`)

## Objectclassificatie

Systematische identificatie en ordening van objecten in categorieën overeenkomstig logisch gestructureerde conventies, methoden en procedureregels weergegeven in een classificatiesysteem.

Attributen: naam, omschrijving.

GUID: `EAID_65792171_62FA_4c35_930A_8B9C999ADC14`
