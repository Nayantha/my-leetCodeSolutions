# https://leetcode.com/problems/evaluate-division
from collections import defaultdict


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    numerator_to_denominator_map = defaultdict(list)
    for i, equation in enumerate(equations):
        a, b = equation
        numerator_to_denominator_map[a].append(b, values[i])
        numerator_to_denominator_map[b].append(a, 1 / values[i])
