class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        minHeap = intervals
        heapq.heapify(minHeap)

        res = []
        lastStart, lastEnd = heapq.heappop(minHeap)
        while minHeap:
            curStart, curEnd = heapq.heappop(minHeap)
            if curStart <= lastEnd:
                lastEnd = max(lastEnd, curEnd)
            else:
                res.append([lastStart, lastEnd])
                lastStart, lastEnd = curStart, curEnd
            if not minHeap:
                res.append([lastStart, lastEnd])
        
        return res