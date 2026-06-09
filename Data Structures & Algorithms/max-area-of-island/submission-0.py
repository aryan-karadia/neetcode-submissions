class Solution:
    tmp_area = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0:
                return
            
            # mark visited
            grid[r][c] = 0
            self.tmp_area += 1
            # go up down left right
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i, j)
                    area = max(area, self.tmp_area)
                    self.tmp_area = 0

        return area