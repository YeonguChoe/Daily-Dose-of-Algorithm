class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hashmap to do a bucket sort: O(n)
        hashmap = {}
        bucket = [[] for i in range(len(nums)+1)] # frequency

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        for n, c in hashmap.items():
            bucket[c].append(n)
        
        res = []
        # sort by desc order to get the k most frequent elements
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
