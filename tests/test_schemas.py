import pytest

from llmwiki import validate


def test_valid_source_instance_passes():
    validate.validate_instance(
        {"run": "2026-01-01T0000-abcd", "bronnen": [{"id": "2026-test-bron"}]},
        "source",
    )


def test_invalid_source_instance_fails():
    with pytest.raises(validate.ValidationFailed):
        validate.validate_instance({"run": "x"}, "source")  # bronnen ontbreekt


def test_run_state_requires_fields():
    with pytest.raises(validate.ValidationFailed):
        validate.validate_instance({"run_id": "x"}, "run-state")


def test_unknown_schema_name_raises_keyerror():
    with pytest.raises(KeyError):
        validate.schema_path("does-not-exist")
