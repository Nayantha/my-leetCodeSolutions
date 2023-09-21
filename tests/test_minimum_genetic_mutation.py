import pytest

from minimum_genetic_mutation import min_mutation


@pytest.mark.parametrize("start_gene, end_gene, bank, min_mutations", [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
    ("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"], 4)
])
def test_min_mutation(start_gene: str, end_gene: str, bank: list[str], min_mutations: int):
    assert min_mutation(start_gene, end_gene, bank) == min_mutations
