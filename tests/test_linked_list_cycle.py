
from typing import List

import pytest


@pytest.mark.parametrize("values, next_node_indexes, expected", [
    ([3, 2, 0, -4], [1, 2, 3, 1], True),
    ([1, 2], [1, 0], True),
    ([1], [None], False)
])
def test_has_cycle(values: List[int], next_node_indexes: List[int], expected: bool):
    ...
