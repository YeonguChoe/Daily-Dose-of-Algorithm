'''
https://leetcode.com/problems/find-if-path-exists-in-graph/
2024-08-16
비슷한 패턴의 문제가 많아서 쉽게 풀림
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        e_dict = defaultdict(list)
        q = deque([source])
        visited = set()
        for a, b in edges:
            e_dict[a].append(b)
            e_dict[b].append(a)
        if source == destination:
            return True
        if destination not in e_dict:
            return False
        while q:
            cur_node = q.popleft()
            if destination == cur_node:
                return True
            for next_node in e_dict[cur_node]:
                if (cur_node, next_node) not in visited:
                    visited.add((cur_node, next_node))
                    q.append(next_node)

        return False
