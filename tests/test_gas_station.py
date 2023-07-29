import pytest


@pytest.mark.parametrize("gas, cost, expectation")
def test_can_complete_circuit(gas: list[int], cost: list[int], expectation: int):
    assert False
