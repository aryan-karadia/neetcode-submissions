class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = []

        dp.append(nums[0])
        dp.append(max(dp[0], nums[1]))

        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        
        return dp[-1]