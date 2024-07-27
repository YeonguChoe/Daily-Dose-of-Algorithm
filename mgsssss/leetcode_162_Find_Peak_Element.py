'''
https://leetcode.com/problems/find-peak-element/description/
2024-07-27

이렇게 풀면 안되는데, 풀렸다 ...;;;

문제는 binary search 를 사용하라는거 같은데 Topics에 나와있었는데,
이렇게 해보면 어떨까 싶어서 해봤는데 되었다.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums) - 1
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i