# https://leetcode.com/problems/minimum-genetic-mutation/
def min_mutation(startGene: str, endGene: str, bank: list[str]) -> int:
    changed_indexes = []
    possible_bases = ['A', 'C', 'G', 'T']
    for i in range(len(startGene)):
        if startGene[i] != endGene[i]:
            changed_indexes.append(i)
