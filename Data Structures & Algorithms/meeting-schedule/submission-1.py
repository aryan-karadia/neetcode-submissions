"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        heap = []
        for i in intervals:
            heapq.heappush(heap, [i.start, i.end])
        
        _, lastEnd = heapq.heappop(heap)
        while heap:
            curStart, curEnd = heapq.heappop(heap)
            if curStart < lastEnd:
                return False
            lastEnd = curEnd
        
        return True

