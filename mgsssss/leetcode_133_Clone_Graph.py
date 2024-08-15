'''
https://leetcode.com/problems/clone-graph/submissions/1346191403/
2024-08-06
graph 문제 bfs dfs 둘다 가능 
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# bfs
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        clone = Node(node.val)
        graph_dict = {}
        graph_dict[node] = clone
        q = deque()
        q.append(node)

        while q:
            cur_node = q.popleft()
            for neighbors in cur_node.neighbors:
                if neighbors not in graph_dict:
                    q.append(neighbors)
                    graph_dict[neighbors] = Node(neighbors.val)
                graph_dict[cur_node].neighbors.append(graph_dict[neighbors])
        return clone

# dfs
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]
            clone = Node(node.val)
            clones[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)