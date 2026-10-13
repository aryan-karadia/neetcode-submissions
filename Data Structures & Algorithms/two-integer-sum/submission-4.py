class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numbers:
                return [numbers[complement], i]
            numbers[nums[i]] = i