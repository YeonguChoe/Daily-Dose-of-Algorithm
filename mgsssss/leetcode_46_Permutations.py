'''
https://leetcode.com/problems/permutations/
2024-08-19

전형적인 backtracking 문제
코드를 암기하고 있다. 해당 코드는 암기가 필수
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtracking(curr)
                    curr.pop()
        backtracking([])
        return res