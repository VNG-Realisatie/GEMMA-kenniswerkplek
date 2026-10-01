# <wiki-naam>-wiki

Deze wiki valt onder de repository-Rules in `../../AGENTS.md`. Als die niet al in de Context staan: lees dat bestand voordat je iets wijzigt.

## Domein

<Beschrijf hier het domein, de taal, de doelgroep en naamgevingsconventies van deze
wiki. Dit sjabloon bevat opzettelijk geen domeinkennis.>

## Standaard Workflow

Gebruik skill `wiki-curatie-update`: de AI schrijft per begrip een beoordeling, scripts van de wiki leiden af en renderen de pagina's, de redacteur geeft akkoord met AKKOORD in de chat. Daarvoor heeft de wiki in `wiki.yaml` `curation.beoordelingen`, `curation.afleiden` en `curation.render` nodig, met eigen scripts (de wiki gemma-archimate-model is een uitgewerkt voorbeeld); zie `docs/onderbouwing.md` 5.13c. Een wiki-specifieke workflow die uitbreidingen toevoegt, verwijst naar `wiki-curatie-update`.
