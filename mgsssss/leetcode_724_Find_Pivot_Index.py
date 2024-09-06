'''
https://leetcode.com/problems/find-pivot-index/
2024-08-29

easy 문제 인줄 알고 쉽게 생각했는데 쉬운 문제가 아니었다.
이것 저것 방법을 많이 고민한 문제 
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        total = 0
        for i in range(len(nums)):
            if nums_sum - total - nums[i] == total:
                return i
            total += nums[i]
        return -1