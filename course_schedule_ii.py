# https://leetcode.com/problems/course-schedule-ii/description/
from collections import deque


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    degrees = [0] * num_courses
    adj = [[] for _ in range(num_courses)]
    for course, prerequisite in prerequisites:
        adj[prerequisite].append(course)
        degrees[course] += 1
    q = deque()
    for i in range(num_courses):
        if degrees[i] == 0:
            q.append(i)
    res = []
    while q:
        course = q.popleft()
        res.append(course)
        for neighbour in adj[course]:  # type: int
            degrees[neighbour] -= 1
            if degrees[neighbour] == 0:
                q.append(neighbour)
    return res if len(res) == num_courses else []
