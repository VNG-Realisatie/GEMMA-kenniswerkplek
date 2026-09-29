<!-- gegenereerd door tools/ggm.py; hash: 2b1c7045f37270e815bd62b117b0c268d48cf69824768f2c9f9fcf4c08eaa13f -->
# Generieke Entiteiten Erfgoed

Taakveld: Erfgoed. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Erfgoed Object | `EAID_71A5C565_C2CC_495f_910A_76C199C6AF0E` | Uit het verleden geërfde materiële en immateriële objecten | titel, omschrijving, dateringVanaf, dateringTot |
| Historisch Persoon | `EAID_3BBB3264_592A_4d8c_A741_C2A3C38E3932` | Natuurlijk persoon waarvan informatie beschikbaar is uit het verleden. | naam, datumGeboorte, datumOverlijden, omschrijving, woondeOp, beroep, publiekToegankelijk |
| Objectclassificatie | `EAID_65792171_62FA_4c35_930A_8B9C999ADC14` | Systematische identificatie en ordening van objecten in categorieën overeenkomstig logisch gestructureerde conventies, methoden en procedureregels weergegeven in een classificatiesysteem. | naam, omschrijving |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Erfgoed Object | Association | valt binnen | Objectclassificatie | 0..* → 0..* | `EAID_C3745FB4_D387_4ccc_8B35_F89C76EBC4F1` |  |
| Historisch Persoon | Association | speelt rol in | Erfgoed Object | 0..* → 0..* | `EAID_6D8C062B_73D8_40c4_8C1B_497F39295AF0` |  |
| Historisch Persoon | Generalization |  | NatuurlijkPersoon |  →  | `EAID_DF9C3B5F_5A7B_43e8_A620_3E8B9CB3CE1E` |  |
