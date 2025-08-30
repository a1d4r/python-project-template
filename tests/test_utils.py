import pytest

from hooks.pre_gen_project import validate_line_length


def test_validate_line_length():
    validate_line_length(88)

    with pytest.raises(ValueError, match="ERROR: line_length must be between"):
        validate_line_length(1_000)

    with pytest.raises(ValueError, match="ERROR: line_length must be between"):
        validate_line_length(-10)
