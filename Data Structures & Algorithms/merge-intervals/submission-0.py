class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals
        minHeap = intervals
        heapq.heapify(minHeap)
        res = []
        prevStart, prevEnd = heapq.heappop(minHeap)
        while minHeap:
            currStart, currEnd = heapq.heappop(minHeap)
            if prevEnd >= currStart:
                prevEnd = max(currEnd, prevEnd)
            else:
                res.append([prevStart, prevEnd])
                prevStart, prevEnd = currStart, currEnd
            if not minHeap:
                res.append([prevStart, prevEnd])            
        
        return res