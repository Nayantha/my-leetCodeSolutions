# https://leetcode.com/problems/course-schedule/description/
def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    prerequisites_course_map: dict[int: list[int]] = {i: [] for i in range(numCourses)}
    for course, prerequisite in prerequisites:
        prerequisites_course_map[course].append(prerequisite)
