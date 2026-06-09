from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        minute = 0
        freshFruit = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    freshFruit += 1
        
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while q and freshFruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] != 1
                    ):
                        continue
                    
                    grid[nr][nc] = 2
                    freshFruit -= 1
                    q.append((nr, nc))
            minute += 1

        return minute if freshFruit == 0 else -1


