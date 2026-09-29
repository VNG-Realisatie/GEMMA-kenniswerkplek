<!-- gegenereerd door tools/ggm.py; hash: ff1a21a92e01016aa33f070db534031fd2ce101b0eac75bc038b7a0881b68200 -->
# Normafwijking

Taakveld: Inkomen. Alleen objecttypen; letterlijke definities uit het GGM.

| Objecttype | GUID | Definitie | Attributen |
|---|---|---|---|
| Afwijkende maatregel | `EAID_1BD0DD3A_888E_945B_4A20_276CADAE4D4C` | Een *afwijkende maatregel* is een maatregel die afwijkt van de standaardregel of wettelijke norm en die op basis van een wettelijke grondslag, beleidsregel of gemotiveerde beslissing in een concreet geval wordt toegepast. | Bedrag, Code reden afwijking maatregel, Motivatie afwijking maatregel, Percentage |
| Boete | `EAID_05E49616_803F_4C1B_9663_262C4A191DF9` | Een boete is de uitkomst van een onderzoek naar rechtmatigheid. Dit leidt in principe tot een terug te vorderen bedrag. Er is voor gekozen om dit als aparte klasse te modelleren en niet als typering van een vordering, omdat we dit gegeven ook willen gebruiken bij risicoprofilering. Als de vordering niet (meer) bestaat, zou dit gegeven daarmee niet beschikbaar zijn.Daarnaast kan dit ook helpen bij het vastleggen van een boete van een poging tot fraude (zonder financiele consequenties, waardoor geen vordering is ontstaan. (tijdig ondekte valsheid in geschifte e.d.).Bij bedragen hoger dan 50.000 euro, wordt aangifte van fraude gedaan en volgt strafrechtelijk onderzoek.Feitelijk is het uitgangspunt bij het opleggen van een boete dat er altijd sprake is van opzet. Daarom is een apart gegeven Fraude niet opgenomen. | Bedrag boete, Boetevorm, Reden boete, Voorwaarde boete |
| Maatregel | `EAID_0B63B508_9F69_A5D7_4387_2632D2C24782` | Een *maatregel* is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven. | Datum aanvang maatregel, Datum einde maatregel, Datum vaststelling maatregel, identificatie, Type maatregel |
| Maatregel op uitkering | `EAID_032C6459_3922_4AEF_0D73_262C4A138E25` | Een *maatregel op uitkering* is een sanctie van een uitvoerend orgaan (zoals een gemeente) waarbij de hoogte van een uitkering tijdelijk wordt verlaagd of aangepast omdat de uitkeringsgerechtigde niet heeft voldaan aan de aan de uitkering verbonden verplichtingen. | Code reden maatregel, Motivatie vermindering maatregel, Percentage maatregel |
| Normafwijking | `EAID_167FF4C9_6B66_EEDA_5189_262C4A139258` | Een *normafwijking* (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde **afwijkt van de normatieve verplichtingen** die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleiding kan geven tot toepassing van een maatregel op de uitkering. | Datum vaststelling normafwijking, Datum vaststelling verwijtbaarheid, identificatie, Motivatie verwijtbaarheid, Recidive, Type normafwijking, Verwijtbaarheid |

## Relaties

| Van | Type | Naam | Naar | Kardinaliteit | GUID | Definitie |
|---|---|---|---|---|---|---|
| Afwijkende maatregel | Aggregation (shared) | refereert | Maatregel op uitkering | 1..1 → 1..1 | `EAID_15977151_EC46_89CA_680B_276CADDFD8E5` |  |
| Afwijkende maatregel | Generalization | Maatregel generaliseert Afwijkende maatregel | Maatregel |  →  | `EAID_161E166F_377B_77CF_BF11_276CAE45C097` |  |
| Boete | Generalization | Maatregel generaliseert Boete | Maatregel |  →  | `EAID_02D32D3B_1AFE_54E9_20D4_2632D33E000F` |  |
| Maatregel op uitkering | Generalization | Maatregel generaliseert Maatregel op uitkering | Maatregel |  →  | `EAID_07EDB42A_2F9E_9557_14A9_2632D2E7753D` |  |
| Normafwijking | Aggregation (shared) | Normafwijking leidt tot Maatregel | Maatregel | 0..1 → 1..1 | `EAID_03151107_A266_68F8_F5DE_2632D35E1D57` |  |
