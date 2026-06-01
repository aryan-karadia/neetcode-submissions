class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, pivot = 0, len(nums) - 1, len(nums) // 2
        if left == right:
            # 1 integer array
            if nums[left] == target:
                return left
            else:
                return -1

                
        while left != right:
            if nums[pivot] == target:
                return pivot
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[pivot] > target:
                # move to left half
                right = pivot - 1
            else:
                # move to right half
                left = pivot + 1
            pivot = (left + right) // 2   

        return -1