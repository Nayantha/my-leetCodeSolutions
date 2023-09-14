# https://leetcode.com/problems/evaluate-division
from collections import defaultdict


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    numerator_to_denominator_map = defaultdict(dict)
    for i, equation in enumerate(equations):
        a, b = equation
        numerator_to_denominator_map[a][b] = values[i]
        numerator_to_denominator_map[b][a] = 1 / values[i]

    def bfs(src, target) -> float:
        # given a / b, src = a, b = target. find a way from a to b
        if src not in numerator_to_denominator_map or target not in numerator_to_denominator_map:
            return -1

    return [bfs(query[0], query[1]) for query in queries]
