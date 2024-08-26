'''
https://leetcode.com/problems/time-needed-to-inform-all-employees/
2024-08-26

문제를 잘못 이해해서 삽질이란 삽질을 다했다.
'''

from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_dict = defaultdict(list)
        for i in range(n):
            manager_dict[manager[i]].append(i)
        def dfs(id):
            max_val = 0
            for em in manager_dict[id]:
                max_val = max(max_val, dfs(em) + informTime[id])
            return max_val

        return dfs(headID)