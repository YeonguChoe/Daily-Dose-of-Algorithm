class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # remove negative prefix, kinda like using a sliding window
        max_sum = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:
                # remove that portion from the current sum
                current_sum = 0
            current_sum += n
            max_sum = max(max_sum, current_sum)
        return max_sum
