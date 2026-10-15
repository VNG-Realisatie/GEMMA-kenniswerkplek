"""tools/afronden.py: de volgorde van de stappen, de stop bij de eerste fout en het vereiste akkoord."""
import subprocess

import pytest

import afronden


class Nep:
    def __init__(self, log_gewijzigd=True, faal=None):
        self.aanroepen, self.log, self.faal = [], log_gewijzigd, faal

    def __call__(self, cmd, cwd):
        self.aanroepen.append(cmd)
        if cmd[:2] == ["git", "status"]:
            return subprocess.CompletedProcess(cmd, 0, " M wikis/x/log.md\n" if self.log else "", "")
        if self.faal and self.faal in " ".join(cmd):
            return subprocess.CompletedProcess(cmd, 1, "", "kapot")
        return subprocess.CompletedProcess(cmd, 0, "", "")


def test_standaard_geen_export_alleen_check(archimate_repo):
    _, wiki = archimate_repo
    nep = Nep()
    afronden.afronden(wiki, "update: x", run=nep)
    export = [c for c in nep.aanroepen if any("archimate_export.py" in a for a in c)]
    assert len(export) == 1 and export[0][-1] == "--check"


def test_alle_stappen_in_volgorde_en_dan_commit(archimate_repo):
    _, wiki = archimate_repo
    nep = Nep()
    uit = afronden.afronden(wiki, "update: iets bijgewerkt", exporteren=True, run=nep)
    soorten = [" ".join(c[1:] if c[0] != "git" else c) for c in nep.aanroepen]
    def plek(sleutel, zonder=None):
        return next(i for i, t in enumerate(soorten) if sleutel in t and not (zonder and zonder in t))

    volgorde = [plek("git status"), plek("commit-check"), plek("archimate_export.py --check"),
                plek("archimate_export.py", "--check"), plek("render.py --check"), plek("llmwiki lint"),
                plek("git add"), plek("git commit -m update: iets bijgewerkt")]
    assert volgorde == sorted(volgorde) and len(set(volgorde)) == 8
    assert uit[-1] == "commit: gedaan"


def test_zonder_akkoord_in_log_geen_stap(archimate_repo):
    _, wiki = archimate_repo
    nep = Nep(log_gewijzigd=False)
    with pytest.raises(afronden.Gestopt, match="geen vastgelegd akkoord"):
        afronden.afronden(wiki, "update: x", run=nep)
    assert len(nep.aanroepen) == 1


@pytest.mark.parametrize("faal", ["commit-check", "archimate_export.py --check", "render.py", "lint"])
def test_een_fout_stopt_zonder_commit(archimate_repo, faal):
    _, wiki = archimate_repo
    nep = Nep(faal=faal)
    with pytest.raises(afronden.Gestopt, match="mislukt, niet gecommit"):
        afronden.afronden(wiki, "update: x", run=nep)
    assert not any(c[:2] == ["git", "commit"] for c in nep.aanroepen)


def test_droog_voert_niets_uit_en_leeg_bericht_weigert(archimate_repo):
    _, wiki = archimate_repo
    nep = Nep()
    uit = afronden.afronden(wiki, "update: x", droog=True, run=nep)
    assert len(nep.aanroepen) == 1 and uit[-1].startswith("commit: git add")
    with pytest.raises(afronden.Gestopt, match="--bericht"):
        afronden.afronden(wiki, "  ", run=nep)
