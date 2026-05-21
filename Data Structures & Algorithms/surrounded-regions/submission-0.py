class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] == "X":
                return

            visited.add((r, c))
            board[r][c] = "I"
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                dfs(nr, nc)

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][cols-1] == "O":
                dfs(row, cols-1)
        
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "I":
                    board[row][col] = "O"
                