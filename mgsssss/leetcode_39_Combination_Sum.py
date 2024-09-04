'''
https://leetcode.com/problems/combination-sum/
2024-09-04

backtracking 으로 간단하게 풀었더니 풀렸다...
'''

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[int] = []
        def backtracking(curr, sum, index):
            if sum == target:
                res.append(curr[:])
                return
            if sum > target:
                return
            
            for i in range(index, len(candidates)):
                curr.append(candidates[i])
                backtracking(curr, sum+candidates[i], i)
                curr.pop()
        
        backtracking([], 0, 0)
        return res