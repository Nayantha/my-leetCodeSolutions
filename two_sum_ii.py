# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
def two_sum(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        rest = target - numbers[i]
        if rest in numbers[i:]:
            return [i + 1, numbers.index(rest, i + 1) + 1]
