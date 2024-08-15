class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by the starting points: O(logn)
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1] # keep track of the first end value
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end # update the end value to check
            else:
                # overlapping -> remove one of the intervals
                res += 1
                prevEnd = min(end, prevEnd)
        return res
