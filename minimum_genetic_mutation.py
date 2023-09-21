# https://leetcode.com/problems/minimum-genetic-mutation/
from collections import deque


def min_mutation(startGene: str, endGene: str, bank: list[str]) -> int:
    possible_bases = ['A', 'C', 'G', 'T']
    queue = deque([startGene])
    visited_genes = set()
    visited_genes.add(startGene)
    total_mutations = 0
    while queue:
        gene = queue.popleft()
        if gene == endGene:
            return total_mutations
        for i in range(len(startGene)):
            for base in possible_bases:
                mutated_gene = f"{gene[:i]}{base}{gene[i + 1:]}"
                if mutated_gene in bank and mutated_gene not in visited_genes:
                    visited_genes.add(mutated_gene)
                    queue.append(mutated_gene)
        total_mutations += 1
    return -1
