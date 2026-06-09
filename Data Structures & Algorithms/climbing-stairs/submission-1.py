class Solution:
    count = 0
    def climbStairs(self, n: int) -> int:
        memo = [None for i in range(n + 1)] 
        def climb(curr):
            if memo[curr]:
                return memo[curr]

            if curr > n:
                return 0
            
            if curr == n:
                return 1
            
            if curr <= n - 2:
                # go 1
                c1 = climb(curr + 1)
                memo[curr + 1] = c1
                # orgo 2
                c2 = climb(curr + 2)
                memo[curr + 2] = c2
                return c1 + c2
            else:
                # go 1
                return climb(curr + 1)


        return climb(0)