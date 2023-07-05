import pytest


@pytest.mark.parametrize("n, expected", [
    (19, True),
    (2, False)
])
def test_is_happy(n: int, expected: bool):
    ...
