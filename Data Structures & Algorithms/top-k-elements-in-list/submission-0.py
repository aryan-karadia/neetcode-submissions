class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.defaultdict(int)
        for n in nums:
            freqs[n] += 1
        
        maxHeap = []
        for n in freqs:
            heapq.heappush_max(maxHeap, (freqs[n], n))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop_max(maxHeap)[1])
        
        return res
