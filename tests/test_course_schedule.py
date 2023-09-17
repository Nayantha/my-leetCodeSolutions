import pytest


@pytest.mark.parametrize("num_courses, prerequisites, expected")
def test_can_finish(num_courses: int, prerequisites: list[list[int]], expected: bool):
    assert False
