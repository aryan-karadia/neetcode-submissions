class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        stack.append((0, heights[0]))
        for i, h in enumerate(heights):
            startingIndex = i
            while stack and stack[-1][1] > h:
                oldI, oldH = stack.pop()
                startingIndex = oldI
                maxArea = max(maxArea, (i - oldI) * oldH)
            
            stack.append((startingIndex, h))
        
        n = len(heights)
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (n - i) * h)

        return maxArea
