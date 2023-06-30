import pytest
@pytest.mark.parametrize("s, expected", [
    ("Hello World", 5),
    ("   fly me   to   the moon  ",4),
    ("luffy is still joyboy", 6)
])
def test_length_of_last_word(s: str, expected: int):
    assert False
