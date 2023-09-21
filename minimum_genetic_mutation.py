# https://leetcode.com/problems/minimum-genetic-mutation/
def min_mutation(startGene: str, endGene: str, bank: list[str]) -> int:
    total_mutations = 0
    if endGene not in bank:
        return -1
    for i in range(len(startGene)):
        if startGene[i] != endGene[i]:
            total_mutations += 1
    return total_mutations if total_mutations else -1
