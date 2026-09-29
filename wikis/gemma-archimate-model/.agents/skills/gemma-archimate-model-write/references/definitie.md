# Definities: herkenbaar en formeel

## Bronvoorrang

Voor de formele betekenis: wet > informatiemodel (GGM, RSGB, catalogi) > beleid > overig.
Voor de gangbare taal: beleidsdocumenten en andere documenten. Gebruik alleen informatie uit de bronnen
van het onderwerp; verzin geen uitleg.

## `definitie` (herkenbaar, altijd)

- Eén zin, hoogstens 160 tekens, begrijpelijk voor domeinexperts ([VR2]).
- Beschrijft wat het ding *is*, niet waar het wordt vastgelegd (geen registr*-taal).
- Zelfstandige tekst: nooit "gelijk aan GGM" of een verwijzing.
- Deze definitie gaat naar GEMMA.

Werkwijze:
1. Is de GGM- of wetsdefinitie al herkenbaar en klopt ze met de bronnen? Neem haar over als herkenbare
   definitie; alleen opschonen (tikfouten, opmaak). Opsommingen, voorbeelden en uitweidingen gaan naar `toelichting`.
2. Anders: formuleer de herkenbare definitie uit het gangbare gebruik in de bronnen. Staat er in een bron een
   bruikbare definitie, neem die letterlijk over. Toon de brontekst en je voorstel aan de redacteur.
3. `toelichting`: aanvulling, uitleg of voorbeelden, ook uit de bronnen. Leeg laten (weglaten) als de definitie volstaat.

## `definitie_formeel` (alleen bij een wezenlijk verschil)

Toets: *vallen onder de herkenbare en de formele definitie precies dezelfde exemplaren?*
- Ja → geen formele definitie (het verschil zit alleen in de formulering).
- Nee, of de formele definitie bevat voorwaarden die voor de behandeling ertoe doen (termijn, uitzondering,
  afbakening) → wel: `definitie_formeel` letterlijk uit de hoogst gerangschikte bron, met
  `definitie_formeel_bron: {bron: <bron-id>, plaats: "art. …"}`, en een sectie `## Definitie` die in één
  of twee zinnen het verschil uitlegt.
- Twijfel → wel.
- Komt de formele definitie uit het GGM, dan staat ze al in `ggm_definitie`: niet kopiëren.
- Spreekt de herkenbare definitie de formele tegen: `⚠️ Tegenspraak` en voorleggen.

## Afwijking van het GGM

Wijkt de GGM-definitie inhoudelijk af van de wet of de bronnen: leg dat vast in `## GGM-bron` (GGM-tekst als
blockquote, waarom je afwijkt) en meld terug als `definitie`.

## Naam

De naam is de herkenbare naam. Een afwijkende wetsterm komt in `synoniemen` met context "wet".
