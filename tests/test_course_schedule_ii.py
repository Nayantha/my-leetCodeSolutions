import pytest

from course_schedule_ii import find_order


@pytest.mark.parametrize("num_courses, prerequisites, expected", [
    (2, [[1, 0]], [0, 1]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
    (1, [], 0)
])
def test_find_order(num_courses: int, prerequisites: list[list[int]], expected: list[int]):
    assert find_order(num_courses, prerequisites) == expected
