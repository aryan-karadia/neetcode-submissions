class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}

        for i, n in enumerate(nums):
            rem = target - n
            if rem in remainders:
                return sorted([i, remainders[rem]])
            remainders[n] = i
        
        
            
