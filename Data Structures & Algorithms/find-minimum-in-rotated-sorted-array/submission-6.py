class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        res = min(nums[l], nums[r])
        while l <= r:
            p = (l + r) // 2
            pivot = nums[p]
            left = nums[l]
            right = nums[r]
            res = min(res, pivot, left, right)
            if pivot > left and pivot > right:
                if left < right:
                    r = p - 1
                else:
                    l = p + 1
            else:
                if left > right:
                    r = p - 1
                else:
                    l = p + 1
        
        return res