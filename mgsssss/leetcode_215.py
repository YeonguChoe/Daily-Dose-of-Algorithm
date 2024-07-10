class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        hq = []
        for i in nums:
            heapq.heappush(hq, (-i,i))
        res = 0
        for i in range(k):
            res = heapq.heappop(hq)
        return res[1]
