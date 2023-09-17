# https://leetcode.com/problems/course-schedule-ii/description/
def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    course_to_prerequisites_map: dict[int: list[int]] = {i: [] for i in range(num_courses)}
    for course, prerequisite in prerequisites:
        course_to_prerequisites_map[course].append(prerequisite)
    completed_courses, completed_courses_in_cycle = set(), set()
    course_complete_order = []

    def dfs(course_number: int):
        ...

    return []
