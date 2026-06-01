class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # empty matrix check
        if len(matrix[0]) == 0:
            return False

        # check what row our target is in
        row_index = len(matrix) // 2
        while row_index >= 0 and row_index <= len(matrix) - 1:
            row = matrix[row_index]
            left, right = row[0], row[-1]
            # check if we are in the right row
            if left <= target and right >= target:
                if left == target or right == target:
                    return True
                return self.binarySearch(row, target)
        

            # else wrong row
            if target < left:
                # does it exist in row below us?
                if row_index > 0:
                    lower_row_limit = matrix[row_index - 1][-1]
                    if target > lower_row_limit:
                        return False 
                row_index -= 1
            else:
                if row_index < len(matrix) - 1:
                    upper_row_limit = matrix[row_index + 1][0]
                    if target < upper_row_limit:
                        return False
                row_index += 1
        
        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        left, right, pivot = 0, len(nums) - 1, len(nums) // 2

        # edge case of len(nums) == 1
        if len(nums) == 1:
            if nums[left] == target:
                return True
            else:
                return False

        # check the nums
        while left != right:
            # check if our values equal
            if nums[pivot] == target or nums[left] == target or nums[right] == target:
                return True
            
            # find where to go
            if nums[pivot] > target:
                # go left half
                right = pivot - 1
            else:
                # go right
                left = pivot + 1
            pivot = (left + right) // 2

        return False
