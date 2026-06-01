class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = len(nums) - 1
        l = 0

        while True:
            if l >= r:
                l += 1
                r = len(nums) - 1
            
            current = nums[l] + nums[r]
            if target == current:
                return [l, r]
            
            r -= 1
            
            
