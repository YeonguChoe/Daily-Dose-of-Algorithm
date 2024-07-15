'''
https://leetcode.com/problems/contains-duplicate/
2024-07-15

넘나 쉬운 문제 푸는데 1분 걸렸다.
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                return True
        return False