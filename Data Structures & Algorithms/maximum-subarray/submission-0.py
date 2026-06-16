class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for r in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum = curSum + nums[r]
            maxSum = max(curSum, maxSum)
        
        return maxSum