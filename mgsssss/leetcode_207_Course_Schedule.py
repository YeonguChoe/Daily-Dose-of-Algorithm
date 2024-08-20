'''
https://leetcode.com/problems/course-schedule/
2024-08-20

생각보다 까다로운 문제, 재귀를 써야하는데 [0, 1] [1, 0] 서로가 서로를 호출해서, 이 부분 처리를 잘해줘야한다.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict: dict = defaultdict(list)
        course_list: list = [True] * numCourses
        for a, b in prerequisites:
            if a == b:
                return False
            pre_dict[a].append(b)
        def dfs(i, visited):
            if i in visited:
                return course_list[i]
            visited.add(i)
            if len(pre_dict[i]) == 0:
                course_list[i] = True
                return True
            course_list[i] = False
            for next_course in pre_dict[i]:
                if not dfs(next_course, visited):
                    return False
            pre_dict[i] = []
            course_list[i] = True
            return course_list[i]


        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True