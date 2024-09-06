'''
https://leetcode.com/problems/top-k-frequent-elements/
2024-08-15

여러 방법으로 해결 가능한 문제
'''

from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        nums_dict = defaultdict(int)
        hq = []
        for num in nums:
            nums_dict[num]+= 1
        for key, val in nums_dict.items():
            heappush(hq, (-val, key))
        while k > 0:
            val, key = heappop(hq)
            res.append(key)
            k -= 1
        return res

        # return [ i for i, j in Counter(nums).most_common(2)] 이렇게 한줄로도 가능