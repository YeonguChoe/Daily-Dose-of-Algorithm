import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap to find the kth largest element
        # TC: O(n*log(k))
        min_heap = []
        for i in nums:
            heapq.heappush(min_heap, i)
            # remove smallest node from the root when the length exceeds k
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = heapq.heappop(min_heap)
        return res
