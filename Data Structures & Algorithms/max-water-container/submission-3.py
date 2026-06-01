class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_fill = 0
        left, right = 0, len(heights) - 1
        while left != right:
            length = right - left
            height = min(heights[left], heights[right])
            current_area = length * height
            max_fill = max(max_fill, current_area)
             
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_fill