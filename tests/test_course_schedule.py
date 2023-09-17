import pytest

from course_schedule import can_finish


@pytest.mark.parametrize("num_courses, prerequisites, expected", [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False)
])
def test_can_finish(num_courses: int, prerequisites: list[list[int]], expected: bool):
    assert can_finish(num_courses, prerequisites)
