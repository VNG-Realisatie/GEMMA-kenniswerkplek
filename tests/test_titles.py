from llmwiki import titles


def test_main_namespace_page():
    assert titles.title_to_path("Contact", 0) == "main/Contact.wiki"


def test_colon_becomes_section_sign():
    assert titles.title_to_path("Sjabloon:Foo", 10) == "template/Foo.wiki"


def test_forbidden_character_percent_encoded():
    path = titles.title_to_path('Sjabloon:Foo*Bar', 10)
    assert "%2A" in path
    assert "*" not in path


def test_css_page_keeps_own_extension_no_double_extension():
    path = titles.title_to_path("MediaWiki:Common.css", 8, "sanitized-css")
    assert path == "mediawiki/Common.css"
    assert not path.endswith(".css.css")


def test_js_page_keeps_own_extension():
    path = titles.title_to_path("MediaWiki:Common.js", 8, "javascript")
    assert path == "mediawiki/Common.js"


def test_subpage_becomes_nested_path():
    path = titles.title_to_path("Sjabloon:Foo/Bar", 10)
    assert path == "template/Foo/Bar.wiki"


def test_reserved_name_gets_hash_suffix():
    path = titles.title_to_path("CON", 0)
    assert "~" in path
    assert path.startswith("main/CON~")


def test_apply_index_convention_moves_parent_into_subfolder():
    paths_by_title = {
        "Foo": titles.title_to_path("Foo", 0),
        "Foo/Bar": titles.title_to_path("Foo/Bar", 0),
    }
    result = titles.apply_index_convention(paths_by_title)
    assert result["Foo"] == "main/Foo/_index.wiki"
    assert result["Foo/Bar"] == "main/Foo/Bar.wiki"


def test_apply_index_convention_leaves_standalone_pages_alone():
    paths_by_title = {"Foo": titles.title_to_path("Foo", 0)}
    result = titles.apply_index_convention(paths_by_title)
    assert result["Foo"] == "main/Foo.wiki"
