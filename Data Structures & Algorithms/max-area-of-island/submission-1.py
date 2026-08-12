class Solution:
    currArea = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return
            
            self.currArea += 1
            grid[r][c] = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for nr, nc in directions:
                dfs(r + nr, c + nc)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    self.currArea = 0
                    dfs(i, j)
                    area = max(area, self.currArea)

        return area