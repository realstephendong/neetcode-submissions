class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0

            grid[row][col] = 0 

            left = dfs(row + 1, col)
            right = dfs( row - 1, col)
            up = dfs(row, col + 1)
            down = dfs(row, col - 1)

            return 1 + left + right + up + down

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    islandSize = dfs(row, col)
                    maxArea = max(maxArea, islandSize)

        return maxArea