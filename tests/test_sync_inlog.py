"""Inloggen op een sync-doel met omgevingsvariabelen (docs/onderbouwing.md 5.10a), met een nep-pywikibot."""
import sys
import types

import pytest

from llmwiki import sync

WIKI_YAML = {
    "site": {"family": "gemmaonline", "code": "en",
             "inlog": {"gebruiker": "T_REDACTIE_USER", "wachtwoord": "T_REDACTIE_PW"}},
    "test_targets": {"staging": {
        "family": "gemmaonline", "code": "staging", "server": "staging.example.org",
        "inlog": {"gebruiker": "T_STAGING_USER", "wachtwoord": "T_STAGING_PW"},
        "http_toegang": {"gebruiker": "T_HTTP_USER", "wachtwoord": "T_HTTP_PW"},
    }},
}


@pytest.fixture
def nep(monkeypatch):
    logins = []
    sessies = set()  # (code, gebruiker) met een geldige sessiecookie

    class Site:
        def __init__(self, code, family, user=None):
            self.code, self.family, self.user = code, family, user
            self.ingelogd = False

        def login(self, cookie_only=False):
            if not cookie_only or (self.code, self.user) in sessies:
                self.ingelogd = True

        def logged_in(self):
            return self.ingelogd

    class ClientLoginManager:
        def __init__(self, site, user, password):
            self.site, self.username, self.password = site, user, password
            self.login_name = user

        def login(self):
            if (self.site.code, self.username) in sessies:
                raise AssertionError("Cannot log in when using BotPasswordSessionProvider sessions")
            logins.append((self.site.code, self.login_name, self.password))
            sessies.add((self.site.code, self.username))
            return True

    config = types.SimpleNamespace(authenticate={}, register_families_folder=lambda pad: None)
    module = types.SimpleNamespace(Site=Site, config=config, login=types.SimpleNamespace(ClientLoginManager=ClientLoginManager))
    monkeypatch.setitem(sys.modules, "pywikibot", module)
    return types.SimpleNamespace(logins=logins, config=config)


def test_ontbrekende_variabelen_geven_duidelijke_fout(nep, monkeypatch):
    monkeypatch.delenv("T_REDACTIE_USER", raising=False)
    monkeypatch.setenv("T_REDACTIE_PW", "geheim")
    with pytest.raises(sync.SyncError, match="T_REDACTIE_USER"):
        sync.get_site(WIKI_YAML, "site")
    assert nep.logins == []


def test_botwachtwoord_uit_omgeving(nep, monkeypatch):
    monkeypatch.setenv("T_REDACTIE_USER", "Mark@llmwiki")
    monkeypatch.setenv("T_REDACTIE_PW", "geheim")
    site = sync.get_site(WIKI_YAML, "site")
    assert site.user == "Mark" and site.ingelogd
    assert nep.logins == [("en", "Mark@llmwiki", "geheim")]


def test_staging_zet_http_toegang(nep, monkeypatch):
    for naam, waarde in (("T_STAGING_USER", "Mark@llmwiki"), ("T_STAGING_PW", "geheim"),
                         ("T_HTTP_USER", "vng"), ("T_HTTP_PW", "http-geheim")):
        monkeypatch.setenv(naam, waarde)
    sync.get_site(WIKI_YAML, "staging")
    assert nep.config.authenticate == {"staging.example.org": ("vng", "http-geheim")}


def test_zonder_inlogblok_eigen_configuratie(nep):
    site = sync.get_site({"site": {"family": "gemmaonline", "code": "en"}}, "site")
    assert site.user is None and site.ingelogd and nep.logins == []


def test_tweede_keer_hergebruikt_de_sessie(nep, monkeypatch):
    monkeypatch.setenv("T_REDACTIE_USER", "Mark@llmwiki")
    monkeypatch.setenv("T_REDACTIE_PW", "geheim")
    sync.get_site(WIKI_YAML, "site")
    site = sync.get_site(WIKI_YAML, "site")  # zou falen als opnieuw werd ingelogd
    assert site.ingelogd and len(nep.logins) == 1
