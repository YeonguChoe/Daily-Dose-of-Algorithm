'''
https://leetcode.com/problems/maximum-total-importance-of-roads/
2024-08-01

문제를 이해하는데 힘들었던 문제,

중요도를 계산해서 heap을 사용함
'''

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        res = 0
        count_dict = defaultdict(int)
        point_dict = defaultdict(int)
        for i, j in roads:
            count_dict[i] += 1
            count_dict[j] += 1
        hq = []
        for key, val in count_dict.items():
            heapq.heappush(hq, (-val, key))
        while hq:
            _, key = heapq.heappop(hq)
            point_dict[key] = n
            n -= 1
        for i, j in roads:
            res += point_dict[i] + point_dict[j]
        return res