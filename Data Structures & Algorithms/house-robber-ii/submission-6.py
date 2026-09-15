class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def rob1(numbers):
            if len(numbers) == 0:
                return 0
            if len(numbers) <= 2:
                return max(numbers)

            dp = [0] * len(numbers)
            dp[0] = numbers[0]
            dp[1] = max(numbers[0], numbers[1])

            for i in range(2, len(numbers)):
                dp[i] = max(dp[i - 1], dp[i - 2] + numbers[i])
            
            return dp[-1]
        
        return max(rob1(nums[:-1]), rob1(nums[1:]))

        