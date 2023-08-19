import pytest

from simplify_path import simplify_path


@pytest.mark.parametrize("path, expected")
def test_simplify_path(path: str, expected: str):
    assert simplify_path(path) == expected
