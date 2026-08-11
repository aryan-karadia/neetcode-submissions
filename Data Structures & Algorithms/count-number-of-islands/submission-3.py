class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(ROWS):
            for n in range(COLS):
                if grid[i][n] == "1":
                    dfs(i, n)
                    count += 1
        
        return count

