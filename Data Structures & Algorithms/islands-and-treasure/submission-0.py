class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
                    visited.add((row, col))

        while q:
            row, col, curr_distance = q.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != -1:
                    grid[nr][nc] = curr_distance + 1

                    visited.add((nr, nc))
                    q.append((nr, nc, curr_distance + 1))

        # def bfs(row, col):
            
        #     visited.add((row, col))
        #     q.append((row,col,0))

        #     while q:
        #         curr = q.popleft()
        #         row = curr[0]
        #         col = curr[1]
        #         curr_distance = curr[2]

        #         if grid[row][col] == -1:
        #             continue
                
        #         if grid[row][col] == 0:
        #             return curr_distance

        #         for dr, dc in directions:
        #             nr = row + dr
        #             nc = col + dc 

        #             if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
        #                 visited.add((nr, nc))
        #                 q.append((nr, nc, curr_distance + 1))
                
        #     return 2147483647
                
        
