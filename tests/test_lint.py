from llmwiki import lint, paths


def test_shared_skills_pass_lint():
    repo_root = paths.find_repo_root()
    errors = lint.run_lint(repo_root)
    assert errors == []


def test_generic_skill_referencing_wiki_path_is_rejected(tmp_path):
    repo_root = tmp_path / "repo"
    skill_dir = repo_root / ".agents" / "skills" / "wiki-bad"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\nname: wiki-bad\ndescription: test\n---\n\nZie wikis/gemma-online/content voor meer.\n",
        encoding="utf-8",
    )
    errors = lint.run_lint(repo_root)
    assert any("wikis/" in e for e in errors)


def test_wiki_skill_without_prefix_is_rejected(tmp_path):
    repo_root = tmp_path / "repo"
    skill_dir = repo_root / "wikis" / "demo" / ".agents" / "skills" / "verkeerd"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\nname: verkeerd\ndescription: test\n---\n\nInhoud.\n", encoding="utf-8"
    )
    errors = lint.run_lint(repo_root)
    assert any("moet beginnen met 'demo-'" in e for e in errors)


def _wiki_met_budget(tmp_path, maximum):
    wiki = tmp_path / "repo" / "wikis" / "demo"
    wiki.mkdir(parents=True)
    (wiki / "wiki.yaml").write_text(
        f"key: demo\ntype: curation\nlint:\n  woordbudget:\n    AGENTS.md: {maximum}\n", encoding="utf-8"
    )
    (wiki / "AGENTS.md").write_text("een twee drie vier vijf\n", encoding="utf-8")
    return tmp_path / "repo"


def test_woordbudget_ok_within_limit(tmp_path):
    assert lint.check_woordbudget(_wiki_met_budget(tmp_path, 5)) == []


def test_woordbudget_exceeded_is_error(tmp_path):
    errors = lint.check_woordbudget(_wiki_met_budget(tmp_path, 4))
    assert len(errors) == 1 and "5 woorden (budget 4)" in errors[0] and "redacteur" in errors[0]


def test_woordbudget_pattern_without_files_is_error(tmp_path):
    repo = _wiki_met_budget(tmp_path, 5)
    (repo / "wikis" / "demo" / "AGENTS.md").unlink()
    assert any("vindt geen bestanden" in e for e in lint.check_woordbudget(repo))
