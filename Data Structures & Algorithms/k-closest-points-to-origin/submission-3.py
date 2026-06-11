class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        vals = []
        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            vals.append([dist, x, y])

        heapq.heapify(vals)

        res = []

        while len(res) != k:
            dist, x, y = heapq.heappop(vals)
            res.append([x, y])
        
        return res
