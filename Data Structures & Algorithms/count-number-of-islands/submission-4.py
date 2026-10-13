class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == '0':
                return
            
            # mark as visited
            grid[i][j] = '0'
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for nr, nc in directions:
                dfs(i + nr, j + nc)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        
        return res