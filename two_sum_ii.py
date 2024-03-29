# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
def two_sum(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        rest = target - numbers[i]
        if rest in numbers[i + 1:]:
            return [i + 1, numbers.index(rest, i + 1) + 1]


def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers) - 1
    while l < r:
        current_sum = numbers[l] + numbers[r] == target
        if current_sum:
            return [l + 1, r + 1]
        elif current_sum:
            r -= 1
        else:
            l += 1
