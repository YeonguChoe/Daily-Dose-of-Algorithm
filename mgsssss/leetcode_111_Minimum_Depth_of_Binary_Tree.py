'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/
2024-07-15
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        if node is None:
            return 0
        self.min_depth = sys.maxsize # 최소값을 구해줄때는 이렇게 시스템에서 사용할 수 있는 제일 큰값을 넣어준다.
        def dfs(node, val):
            if not node.left and not node.right:
                self.min_depth = min(self.min_depth, val)
                return 1 # [0] 이렇게 하나만 있는 경우 여기서 바로 1을 return 해줘야함
            
            if node.left:
                dfs(node.left, val+1)
            if node.right:
                dfs(node.right, val+1)

            return self.min_depth

        res = dfs(node, 1)
        return res
