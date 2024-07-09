import heapq 

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initializes the object with the integer k and the stream of integers nums
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap) # adding all elements to the min heap
        # only keeping k max elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Appends the integer val to the stream
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # returns the element representing the kth largest element in the stream
        return self.min_heap[0]
    
# TC: O(nlogn) - heap size n * heappush log(n)
# SC: O(n)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
