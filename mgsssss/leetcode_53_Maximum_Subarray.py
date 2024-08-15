'''
https://leetcode.com/problems/maximum-subarray/description/
2024-08-15

진짜 어렵다.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] + res[-1] > nums[i]:
                res.append(nums[i] + res[-1])
            else:
                res.append(nums[i])
        return max(res)
'''
[-2,1,-3,4,-1,2,1,-5,4]
[0] -2
[1] 1
[2] -2
[3] 4
[4] 3
[5] 5
[6] 6
[7] 1
[8] 5
'''



