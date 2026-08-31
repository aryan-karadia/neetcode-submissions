import heapq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        heap = intervals
        heapq.heapify(heap)
        res = 0
        _, lastEnd = heapq.heappop(heap)
        while heap:
            curStart, curEnd = heapq.heappop(heap)
            # if overlap, remove larger interval
            if curStart < lastEnd:
                lastEnd = min(lastEnd, curEnd)
                res += 1
            else:
                lastEnd = curEnd
        
        return res
