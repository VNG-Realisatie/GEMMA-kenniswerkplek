# Definities: herkenbaar en formeel

## Bronvoorrang

Voor welke begrippen er zijn en wat ze formeel betekenen (`definitie_formeel`): de regel Bronvoorrang, `europese-regelgeving` → `rijksregelgeving` → `informatiemodel` → `richtlijn` → `gemeentelijke-regelgeving` → `beleid` → `overig`.

UITZONDERING: de **naam** en de herkenbare **`definitie`** komen uit de gangbare taal: beleids- en praktijkbronnen, en wat domeinexperts zeggen. De wetsterm gaat naar `synoniemen` (context "wet"); zie `naamgeving.md`. Voorbeeld: het element heet *Urn* (VNG, praktijk), met *asbus* als synoniem (Wet op de lijkbezorging).

Gebruik alleen informatie uit de bronnen; verzin geen uitleg. Voor een actor of rol mag dat ook een bron buiten het onderwerp zijn (zie hieronder).

## `definitie` (herkenbaar, altijd)

- Eén zin, hoogstens 160 tekens, begrijpelijk voor domeinexperts (regel Begrijpelijk).
- Beschrijft wat het ding *is*, niet waar het wordt vastgelegd (geen registr*-taal).
- Zelfstandige tekst: nooit "gelijk aan GGM" of een verwijzing.
- Deze definitie gaat naar GEMMA.
- De render zet haar bovenaan de pagina, onder *Definitie*.

Werkwijze:
1. Is de GGM- of wetsdefinitie al herkenbaar en klopt ze met de bronnen? Neem haar over als herkenbare definitie; alleen opschonen (tikfouten, opmaak). Opsommingen, voorbeelden en uitweidingen gaan naar `toelichting`.
2. Anders: formuleer de herkenbare definitie uit het gangbare gebruik in de bronnen. Staat er in een bron een bruikbare definitie, neem die letterlijk over. Toon de brontekst en je voorstel aan de redacteur.
3. Aanvulling, uitleg of voorbeelden horen in `beschrijving`.

## `definitie_formeel` (alleen bij een wezenlijk verschil)

Toets: *vallen onder de herkenbare en de formele definitie precies dezelfde exemplaren?*
- Ja → geen formele definitie (het verschil zit alleen in de formulering).
- Nee, of de formele definitie bevat voorwaarden die voor de behandeling ertoe doen (termijn, uitzondering, afbakening) → wel: `definitie_formeel` letterlijk uit de hoogst gerangschikte bron, met `definitie_formeel_bron: {bron: <bron-id>, plaats: "art. …"}`. De render zet haar als citaat onder de herkenbare definitie; noem het verschil in één of twee zinnen in `beschrijving`.
- Twijfel → wel.
- Komt de formele definitie uit het GGM, dan staat ze al op de pagina (letterlijke GGM-velden): niet kopiëren.
- Spreekt de herkenbare definitie de formele tegen: tegenspraak markeren en voorleggen (regel Tegenspraak).

## Afwijking van het GGM

Wijkt de GGM-definitie inhoudelijk af van de wet of de bronnen: leg uit waarom in `ggm.onderbouwing` en meld terug als `definitie`.

## Actor en rol

- De definitie van een **actor** beschrijft wat de partij *is* (rechtsvorm, soort organisatie, plaats in het bestuur), los van het onderwerp waarin ze is gevonden. Niet: wat ze in dit onderwerp mag of doet.
- De definitie van een **rol** beschrijft de verantwoordelijkheid, niet wie haar vervult.
- Wat een partij binnen het onderwerp doet, staat in `relaties`: de rol die ze vervult (toewijzing); gedrag en objecten via die rol.
- Geeft de bron van het onderwerp alleen onderwerpgebonden taal, gebruik dan een algemene bron (bijv. het Burgerlijk Wetboek voor een kerkgenootschap, de Gemeentewet voor burgemeester en college) en voeg die bron toe aan `bronnen:`.
- Toets: past de definitie ongewijzigd in elk ander onderwerp waarin deze partij voorkomt? Nee → herschrijven.
- Hetzelfde geldt voor `beschrijving`, bij elk element dat in meer onderwerpen kan voorkomen (partijen, besluiten, regelingen, heffingen, gebeurtenissen als overlijden): wat het in één onderwerp doet, staat onder `per_onderwerp` (regel Los van het onderwerp).

Voorbeeld: niet "Kerkelijke organisatie die een bijzondere begraafplaats of crematorium mag houden", maar een definitie van het kerkgenootschap zelf; "houdt een bijzondere begraafplaats" wordt een relatie met Begraafplaats, via de rol Houder van de begraafplaats.

## Naam

De naam is de gangbare, herkenbare naam uit de beleids- en praktijkbronnen (zie `naamgeving.md`). Een afwijkende wetsterm komt in `synoniemen` met context "wet".
