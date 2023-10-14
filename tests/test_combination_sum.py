import pytest

from combination_sum import combination_sum


@pytest.mark.parametrize("num_list, target, expected_combination", [
    ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
    ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
])
def test_combination_sum(num_list: list[int], target: int, expected_combination: list[list[int]]):
    assert combination_sum(num_list, target) == expected_combination
