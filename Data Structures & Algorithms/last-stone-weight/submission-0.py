class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        while len(maxHeap) >= 2:
            stone1 = heapq.heappop_max(maxHeap)
            stone2 = heapq.heappop_max(maxHeap)
            remaining = abs(stone1 - stone2)
            print(stone1, stone2)
            if remaining != 0:
                # add remaining
                heapq.heappush_max(maxHeap, remaining)
        
        # have 1 stone or 0 stones
        if len(maxHeap) == 1:
            return maxHeap[0]
        else:
            return 0

        