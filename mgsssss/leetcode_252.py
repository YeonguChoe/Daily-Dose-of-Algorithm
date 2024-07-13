"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        now = 0
        i = []
        for interval in intervals:
            i.append((interval.start, interval.end))
        i.sort()
        for interval in i:
            
            if interval[0] < now:
                return False
            now = interval[1]
        return True