class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]] # initialize with the first interval from the sorted list

        for i in range(1, len(intervals)):
            curr = intervals[i]
            # checks if the end of the last interval in res is less than the start of the current interval
            if res[-1][1] < curr[0]:
                # no overlap
                res.append(curr)
            else:
                # merges the intervals by updating the end of the last interval in res
                res[-1][1] = max(res[-1][1], curr[1])

        return res
