class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        prev = nums[0]
        for i in range(1, len(nums)):
            res.append(prev)
            prev *= nums[i]
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prev
            prev *= nums[i]
        
        return res

