# https://leetcode.com/problems/course-schedule-ii/description/
def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    course_to_prerequisites_map: dict[int: list[int]] = {i: [] for i in range(num_courses)}
    for course, prerequisite in prerequisites:
        course_to_prerequisites_map[course].append(prerequisite)
    completed_courses, completed_courses_in_cycle = set(), set()
    course_complete_order = []

    def dfs(course_number: int) -> bool:
        if course_number in completed_courses_in_cycle:
            return False
        if course_number in completed_courses:
            return True
        completed_courses_in_cycle.add(course_number)
        for prerequisite_course_for_course_number in course_to_prerequisites_map[course_number]:
            if not dfs(prerequisite_course_for_course_number):
                return False
        completed_courses_in_cycle.remove(course_number)
        completed_courses.add(course_number)
        course_complete_order.append(course_number)
        return True

    return []
