class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            # go all directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count