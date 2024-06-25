# https://leetcode.com/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def generate_parentheses(n: int) -> List[str]:
    stack: list[str] = []
    result: list[str] = []

    def backtrack(open_parenthesis_count, closed_parenthesis_count):
        if open_parenthesis_count == closed_parenthesis_count == n:
            result.append("".join(stack))
            return

        if open_parenthesis_count < n:
            stack.append("(")
            backtrack(open_parenthesis_count + 1, closed_parenthesis_count)
            stack.pop()

        if closed_parenthesis_count < open_parenthesis_count:
            stack.append(")")
            backtrack(open_parenthesis_count, closed_parenthesis_count + 1)
            stack.pop()

    backtrack(0, 0)

    return result
