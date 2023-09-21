import pytest


@pytest.mark.parametrize("start_gene, end_gene, bank, min_mutations", [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2)
])
def test_min_mutation(start_gene: str, end_gene: str, bank: list[str], min_mutations: int):
    assert False
