'''
https://leetcode.com/problems/merge-intervals/
2024-07-25
정말 생각을 하면서 코딩을 해야된다고 느낀 문제
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x : x[0])
        res = []
        
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1] = [
                    min(res[-1][0], interval[0]),
                    max(res[-1][1], interval[1])
                ]
        return res