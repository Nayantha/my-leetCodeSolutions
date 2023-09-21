# https://leetcode.com/problems/minimum-genetic-mutation/
def min_mutation(startGene: str, endGene: str, bank: list[str]) -> int:
    if endGene not in bank:
        return -1
