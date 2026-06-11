class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # min heap size k
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) == 0 or val >= self.minHeap[0]:
            heapq.heappush(self.minHeap, val)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
            
        return self.minHeap[0]
