# https://leetcode.com/problems/combination-sum/description/
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(i: int, cur: list[int], total: int):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or target < total:
            return
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res
