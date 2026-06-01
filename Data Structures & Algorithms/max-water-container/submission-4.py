class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = -1
        l, r = 0, len(heights) - 1

        while l < r:
            # calc area
            length = r - l
            height = min(heights[l], heights[r])
            area = length * height
            maxWater = max(area, maxWater)
            # increment the smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxWater
        