class Solution:
    def findMin(self, nums: List[int]) -> int:
        # check if half of array is sorted in order to find pivot
        # arr is guaranteed to be in at most two sorted subarrays
        res = nums[0] # pick a random num
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left+right)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid +1
            else:
                right = mid-1
        
        return res
