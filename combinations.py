# https://leetcode.com/problems/combinations/
def combine(n: int, k: int) -> list[list[int]]:
    total_combinations = []

    def backtrack(start: int, current_combination: list[int]):
        if len(current_combination) == k:
            total_combinations.append(current_combination.copy())
            return
        for i in range(start, n + 1):
            current_combination.append(i)
            backtrack(i + 1, current_combination)
            current_combination.pop()

    backtrack(1, [])
    return total_combinations
