import pytest

from ransom_note import can_construct


@pytest.mark.parametrize("ransom_note, magazine, expected", [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True)
])
def test_can_construct(ransom_note: str, magazine: str, expected: bool):
    assert can_construct(ransom_note, magazine) == expected
