class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    

        # parent coordinates as parameter? check if visiting parent coordinates before making the backtrack

        # run backtrack recursively on each vertically/horizontally adjacent path as long as it does not exceed
        # the boundaries of the board

        wordlen = len(word)
        rows = len(board)
        cols = len(board[0])

        def backtrack(x, y, letterindex):

            if board[x][y] != word[letterindex]:
                return False

            if letterindex == wordlen - 1:
                return True

            letterindex += 1
            visited.add((x,y))

            if x + 1 < rows and (x+1, y) not in visited:
                if backtrack(x+1, y, letterindex):
                    return True
            if x - 1 >= 0 and (x-1, y) not in visited:
                if backtrack(x-1, y, letterindex):
                    return True
            if y + 1 < cols and (x, y+1) not in visited:
                if backtrack(x, y+1, letterindex):
                    return True
            if y - 1 >= 0 and (x, y-1) not in visited:
                if backtrack(x, y-1, letterindex):
                    return True
            visited.remove((x,y))
            return False
                    
    
        for row in range(rows):
            for col in range(cols):
                visited = set()
                if backtrack(row, col, 0):
                    return True
        return False
            