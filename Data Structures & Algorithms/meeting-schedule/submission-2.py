"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if len(intervals) == 0: return True
        last_end = intervals[0].end


        for inter in intervals[1:]:
            s, e = inter.start, inter.end
            if s < last_end:
                return False
            last_end = max(last_end, e)
        
        return True
