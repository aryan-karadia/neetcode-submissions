import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        max_speed = max(piles)
        mid = (max_speed + speed) // 2
        res = max_speed
        while speed <= max_speed:
            # check if mid works
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)

            if totalTime <= h:
                # works
                res = min(mid, res)
                # check lower
                max_speed = mid - 1
            else:
                # didnt work - look upwards
                speed = mid + 1
            
            # update mid
            mid = (max_speed + speed) // 2

        return res