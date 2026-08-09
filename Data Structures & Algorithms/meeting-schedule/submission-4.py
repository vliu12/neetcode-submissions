"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        length = len(intervals)
        for i in range(length-1):
            A = intervals[i]
            for j in range(i+1, length):
                B = intervals[j]
                if min(A.end, B.end) > max(A.start, B.start):
                    return False

        return True
        
                

