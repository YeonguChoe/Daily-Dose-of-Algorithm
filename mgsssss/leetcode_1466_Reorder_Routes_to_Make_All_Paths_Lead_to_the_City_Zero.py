'''
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
2024-08-09

쉽게 생각하면 쉬운데 방법을 떠올리는게 진짜 힘들다...
'''

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        original = { (a, b) for a, b in connections }
        n_dict = defaultdict(list)
        visited = set()
        change_load = [0]
        for a, b in connections:
            n_dict[a].append(b)
            n_dict[b].append(a)

        def dfs(n):
            visited.add(n)
            for d in n_dict[n]:
                if d not in visited:
                    if (n, d) in original:
                        change_load[0] += 1
                    dfs(d)
        dfs(0)
        return change_load[0]