# https://leetcode.com/problems/course-schedule/description/
def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    prerequisites_course_map: dict[int: list[int]] = {i: [] for i in range(numCourses)}
    for course, prerequisite in prerequisites:
        prerequisites_course_map[course].append(prerequisite)
    completed_courses = set()

    def dfs(current_course: int):
        if current_course in completed_courses:
            return False
        if not prerequisites_course_map[current_course]:
            return True
        completed_courses.add(current_course)
        for prerequisite_course in prerequisites_course_map[current_course]:
            if not dfs(prerequisite_course):
                return False
        completed_courses.remove(current_course)
        prerequisites_course_map[current_course] = []
        return True
    return all(dfs(course) for course in range(numCourses))
