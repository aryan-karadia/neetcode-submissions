class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while(1):
            attempt = numbers[left] + numbers[right]
            if(left == right):
                # should never get here
                return [-1, -1]
            if (attempt == target):
                return [left + 1, right + 1]
            if (attempt < target):
                left += 1
                continue
            elif (attempt > target):
                right -= 1
                continue
