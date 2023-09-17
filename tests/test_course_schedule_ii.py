import pytest


@pytest.mark.parametrize("num_courses, prerequisites, expected")
def test_find_order(num_courses: int, prerequisites: list[list[int]], expected: list[int]):
    assert False
