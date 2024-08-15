'''
https://leetcode.com/problems/non-overlapping-intervals/
2024-08-15
두가지 방법중 위에 방법이 효율이 더 좋다.
이런 문제는 많이 풀어봐야한다.
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = []
        for i in range(len(intervals)):
            if len(res) == 0 or res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
        return len(intervals) - len(res)

        # intervals.sort(key=lambda x:x[1])
        # prev = intervals[0]
        # res = 0
        # for i in range(1, len(intervals)):
        #     if prev[1] <= intervals[i][0]:
        #         prev = intervals[i]
        #     else:
        #         res += 1
        # return res