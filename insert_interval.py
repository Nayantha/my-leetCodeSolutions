# https://leetcode.com/problems/insert-interval/
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    for i in range(len(intervals)):  # type: list[int]
        if intervals[i][1] <= new_interval[0]:
            intervals[i][1] = new_interval
    return intervals
