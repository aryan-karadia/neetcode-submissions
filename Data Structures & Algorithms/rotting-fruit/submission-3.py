class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        freshFruit = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    freshFruit += 1
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        minute = 0
        while q and freshFruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    freshFruit -= 1
                    q.append((nr, nc))
            minute += 1
        
        return minute if freshFruit == 0 else -1


