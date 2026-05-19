class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()

        anstime = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    visited.add((row,col))
                    q.append((row,col,0))

        while q:
            row, col, time = q.popleft()
            anstime = time
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                    q.append((nr, nc, time + 1))
                    visited.add((nr, nc))

            if row + 1 < rows:
                grid[row + 1][col] = 2
            if row - 1 >= 0:
                grid[row - 1][col] = 2
            if col + 1 < cols:
                grid[row][col + 1] = 2
            if col - 1 >= 0:
                grid[row][col - 1] = 2

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        
        return anstime

            

            

        