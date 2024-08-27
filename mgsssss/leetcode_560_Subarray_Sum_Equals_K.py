'''
https://leetcode.com/problems/subarray-sum-equals-k/
2024-08-27

난이도 극상, 푸는 방법을 모르면 못 푼다 ...
예전에 풀어봤는데, 그때 정말 어렵게 푼 문제,
다시 풀어봐도 풀이 방법 생각해내는게 힘들었다.
좋은 문제 !
'''

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = res = 0
        nums_dict = defaultdict(int)
        nums_dict[0] = 1

        for num in nums:
            total += num
            res += nums_dict[total - k]
            nums_dict[total] += 1
        return res