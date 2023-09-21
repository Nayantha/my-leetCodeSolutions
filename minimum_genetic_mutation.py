# https://leetcode.com/problems/minimum-genetic-mutation/
def min_mutation(startGene: str, endGene: str, bank: list[str]) -> int:
    total_mutations = 0
    if endGene not in bank:
        return -1
    bases_in_dna_count = {"A": 0, "C": 0, "G": 0, "T": 0}
    start_gene_base_count = bases_in_dna_count.copy()
    end_gene_base_count = bases_in_dna_count.copy()
    for i in range(len(startGene)):
        start_gene_base_count[startGene[i]] += 1
        end_gene_base_count[endGene[i]] += 1
        if startGene[i] != endGene[i]:
            total_mutations += 1
    return total_mutations if total_mutations and start_gene_base_count != end_gene_base_count else -1
