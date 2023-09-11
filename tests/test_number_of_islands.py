import pytest

from number_of_islands import num_islands


@pytest.mark.parametrize("grid, expected_island_amount", [
    (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ], 1
    ),
    (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ], 3
    )
])
def test_num_islands(grid: list[list[str]], expected_island_amount: int):
    assert num_islands(grid) == expected_island_amount
