'''
https://leetcode.com/problems/same-tree/
2024-09-27
생각보다 어렵게 풀었다. base case 를 만드는데 생각보다 어려웠다.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        def dfs(p, q):
            if not p and not q:
                    return True            
            if (not p or not q) or p.val != q.val:
                    return False

            if p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)