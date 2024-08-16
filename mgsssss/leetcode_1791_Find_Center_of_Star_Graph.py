'''
https://leetcode.com/problems/find-center-of-star-graph/
2024-08-17
'''

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        g_list = [[] for _ in range(len(graph)+1)]
        g_list[0] = 0
        for key, d_list in graph.items():
            g_list[key] = len(d_list)
        return g_list.index(max(g_list))