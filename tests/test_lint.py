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
