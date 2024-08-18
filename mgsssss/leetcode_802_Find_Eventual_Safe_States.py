'''
https://leetcode.com/problems/find-eventual-safe-states/
2024-08-18

dfs 로 풀어야 하는데 bfs 로 풀려다가 삽질을 해서 시간이 좀 걸림.
문제를 제대로 이해하지 못해서, 시간이 더 걸림.
문제를 제대로 이해해야겠다 ...
'''

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        safe_dict = {}
        def dfs(i):
            if i in safe_dict:
                return safe_dict[i]
            safe_dict[i] = False
            for next_node in graph[i]:
                if not dfs(next_node):
                    return safe_dict[i]
            safe_bool = True
            safe_dict[i] = safe_bool
            return safe_bool

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res