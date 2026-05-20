class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        rows = len(heights)
        cols = len(heights[0])

        def dfs(x, y, ocean, prev_height):
            if x < 0 or x == rows or y < 0 or y == cols or (x,y) in ocean or heights[x][y] < prev_height:
                return

            ocean.add((x,y))
            
            for dr, dc in directions:
                nr, nc = x + dr, y + dc

                dfs(nr, nc, ocean, heights[x][y])

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows-1, col, atlantic, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols-1, atlantic, heights[row][cols-1])
        
        ans = []
        for row in range(rows):
            for col in range(cols):
                if (row,col) in pacific and (row, col) in atlantic:
                    ans.append([row,col])
        
        return ans
        
