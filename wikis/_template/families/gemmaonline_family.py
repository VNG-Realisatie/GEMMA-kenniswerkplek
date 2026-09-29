"""Pywikibot-family voor GEMMA Online: welke servers er zijn, onder welke code.

Naam en vorm (`<naam>_family.py`, klasse `Family`) schrijft pywikibot voor. Dit bestand bevat geen inloggegevens;
die komen uit omgevingsvariabelen (zie `wiki.yaml`, blokken `inlog` en `http_toegang`, en README). llmwiki meldt
dit bestand zelf aan bij pywikibot (tools/llmwiki/sync.py).
"""
from pywikibot import family


class Family(family.Family):
    name = "gemmaonline"
    langs = {
        "en": "redactie.gemmaonline.nl",  # hoofddoel, bron van waarheid
        "staging": "gemma2-redactie.staging.wikixl.nl",  # testkopie, achter een extra HTTP-toegangslaag
    }

    def scriptpath(self, code):
        return ""

    def protocol(self, code):
        return "https"
