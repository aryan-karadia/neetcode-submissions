import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)
        
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush_max(self.maxHeap, heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))

        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (self.maxHeap[0] + self.minHeap[0]) / 2.0

        
        