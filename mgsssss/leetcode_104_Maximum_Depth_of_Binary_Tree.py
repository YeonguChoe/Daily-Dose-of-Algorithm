'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
2024-07-17

dfs or bfs 둘다로 풀리는 문제 난이도 하
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        q = deque()
        q.append((root, 1))
        max_depth = 0
        while q:
            cur_node, cur_depth = q.popleft()
            max_depth = max(max_depth, cur_depth)
            if cur_node.left:
                q.append((cur_node.left, cur_depth+1))

            if cur_node.right:
                q.append((cur_node.right, cur_depth+1))
        return max_depth
