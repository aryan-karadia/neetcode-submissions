class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1

        while l < r:
            minHeight = min(heights[l], heights[r])
            width = r - l
            tempArea = minHeight * width
            maxWater = max(maxWater, tempArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxWater