class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) <= 1:
            return 0
        
        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1
        return res