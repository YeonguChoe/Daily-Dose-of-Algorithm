'''
https://leetcode.com/problems/two-sum/
2024-07-15
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            numsDict[nums[i]] = i

        for i in range(len(nums)):
            val  = target - nums[i]
            if val in numsDict:
                if numsDict[val] != i:
                    return [numsDict[val], i]