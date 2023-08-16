# https://leetcode.com/problems/merge-intervals/
def merge(intervals: list[list[int]]) -> list[list[int]]:
    res = [intervals[0]]
    intervals.sort(key=lambda i: i[0])
    for start, end in intervals[1:]:
        last_end = res[-1][1]
        if start <= last_end:
            res[-1][1] = max(last_end, end)
        else:
            res.append([start, end])
    return res
