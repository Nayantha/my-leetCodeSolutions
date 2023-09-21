import pytest


@pytest.mark.parametrize("start_gene, end_gene, bank, min_mutations")
def test_min_mutation(start_gene: str, end_gene: str, bank: list[str], min_mutations: int):
    assert False
