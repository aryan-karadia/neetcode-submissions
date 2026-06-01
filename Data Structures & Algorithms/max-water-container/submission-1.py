class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = (r - l) * (min(heights[l], heights[r]))
        while (l < r):
            tempArea = (r - l) * (min(heights[l], heights[r]))
            if (tempArea > area):
                area = tempArea
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        
        return area