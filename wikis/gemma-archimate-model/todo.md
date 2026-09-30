# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Migratierun lijkbezorging (gedragskenmerken, [EL19] en [EL20])

Eén run over de goedgekeurde pagina's van lijkbezorging, zodat alles in één keer door de gate gaat.

- **Beschrijving los van het onderwerp [EL19].** Algemene beschrijving uit een algemene bron, onderwerptekst naar `## Per onderwerp`: Burgemeester, Kerkgenootschap, GGD, Gemeente, Ambtenaar van de burgerlijke stand (ook de definitie), Besluit, Beschikking, Vergunning, Regeling, Heffing, Heffingsverordening, Overlijden. `check_elementen.py` vindt de meeste (`beschrijving-onderwerp`); GGD, Heffingsverordening en Overlijden niet, die zijn anders geformuleerd. Gemeenteraad, College van B&W en Inwoner zijn al herschreven in run 2026-09-30T1915-69e2.

- **Naamvorm van processen [EL20].** Per geval voorleggen ([EL9]); voorstel: Lijkschouwing → Schouwen lijk, Opgraving → Opgraven lijk, Ruiming → Ruimen graf, Uitgifte van een graf → Uitgeven graf, Lijkbezorging door de burgemeester → Verzorgen gemeentebegrafenis, Lijkbezorging → Bezorgen lijk. De oude naam wordt synoniem (context "beleid"); links bijwerken. Overweeg een functie Lijkbezorging als overkoepeling, zoals Participatie. `check_elementen.py` meldt ze als `naam-vorm`.

- **Gedragskenmerken.** Sinds 2026-09-30 kent de beslistabel zeven gedragskenmerken (toegewezen partij, gebruikt objecten, aanleiding, benoembaar resultaat, herhaald uitgevoerd, eigen normering, stabiel over tijd); de drempel voor proces en functie rust erop. De 42 elementpagina's van lijkbezorging missen ze nog (`check_elementen.py`: `kenmerken-onvolledig`). Voeg ze toe via een run: bij passieve begrippen en partijen nee, bij de zes processen, de dienst en de twee gebeurtenissen een beoordeling met onderbouwing. Opgraving en Uitgifte van een graf hebben geen toegewezen partij in de wiki (6/7); leg dat voor.

## Herziening van de regels

De redacteur wil de regels van deze wiki herzien omdat ze te strak zijn (besloten 2026-09-30).

- **Statusregel [EL18].** `voorgestelde_status` in `tools/bepaal_type.py` zet een governance-object en een data-object zonder GGM-match altijd op `kandidaat`; een besluit van de redacteur kan dat niet opheffen, en `promote apply` weigert het goedkeuren van een kandidaat. Zulke elementen kunnen dus nooit worden goedgekeurd. Voorstel: een frontmatter-veld `besluit_redacteur` (datum, door, besluit) waarmee de status `review` wordt als dit het enige bezwaar is; een conflict of "voorleggen" uit de beslistabel blijft kandidaat. [EL18] krijgt daarvoor een UITZONDERING, en `tools/check_elementen.py` meldt een `besluit_redacteur` zonder datum of naam.
- **Daarna opnieuw voorleggen:** Regeling (governance-object), Graf en Grafrecht (data-object zonder GGM-entiteit, terugmeldingen 3 en 4). De redacteur heeft opname akkoord bevonden (run 2026-09-30T1144-3c57); ze staan nog op `kandidaat`.
