class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [None for _ in range(len(cost))]
        def climb(curr):
            if curr >= len(cost):
                return 0
            if memo[curr]:
                return memo[curr]
            
            step1 = climb(curr + 1)
            # memo[curr + 1] = step1

            step2 = climb(curr + 2)
            # if curr + 2 < len(cost): memo[curr + 2] = step2
            currCost = min(cost[curr] + step1, cost[curr] + step2)
            memo[curr] = currCost
            return currCost
        
        return min(climb(0), climb(1))