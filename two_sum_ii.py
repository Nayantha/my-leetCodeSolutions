# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
def two_sum(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        rest = target - numbers[i]
        if rest in numbers[i:]:
            return [i + 1, numbers.index(rest, i + 1) + 1]


def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers) - 1
    for i in range(len(numbers)):
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l -= 1
