class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            p = (l + r) // 2
            if nums[p] == target:
                return p
            elif nums[p] > target:
                r = p - 1
            else:
                l = p + 1
        
        return -1
        