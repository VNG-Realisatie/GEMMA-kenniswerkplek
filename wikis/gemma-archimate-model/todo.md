# Todo

Open punten voor deze wiki. Een punt verdwijnt als het is afgehandeld; de afhandeling staat in de commit.

## Herziening van de regels

De redacteur wil de regels van deze wiki herzien omdat ze te strak zijn (besloten 2026-09-30).

- **Statusregel [EL18].** `voorgestelde_status` in `tools/bepaal_type.py` zet een governance-object en een data-object zonder GGM-match altijd op `kandidaat`; een besluit van de redacteur kan dat niet opheffen, en `promote apply` weigert het goedkeuren van een kandidaat. Zulke elementen kunnen dus nooit worden goedgekeurd. Voorstel: een frontmatter-veld `besluit_redacteur` (datum, door, besluit) waarmee de status `review` wordt als dit het enige bezwaar is; een conflict of "voorleggen" uit de beslistabel blijft kandidaat. [EL18] krijgt daarvoor een UITZONDERING, en `tools/check_elementen.py` meldt een `besluit_redacteur` zonder datum of naam.
- **Daarna opnieuw voorleggen:** Regeling (governance-object), Graf en Grafrecht (data-object zonder GGM-entiteit, terugmeldingen 3 en 4). De redacteur heeft opname akkoord bevonden (run 2026-09-30T1144-3c57); ze staan nog op `kandidaat`.
