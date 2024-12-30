class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        def check(x, y):
            return 0 <= x < m and 0 <= y < n
            
        def crush(board):
            toBeCrushed = set()
            for x in range(m):
                for y in range(n):
                    if board[x][y] == 0:
                        continue     
                    if check(x+1, y) and check(x-1, y) and board[x+1][y] == board[x-1][y] == board[x][y]:
                        toBeCrushed.add((x, y))
                        toBeCrushed.add((x-1, y))
                        toBeCrushed.add((x+1, y))
                    if check(x, y-1) and check(x, y+1) and board[x][y+1] == board[x][y-1] == board[x][y]:
                        toBeCrushed.add((x, y))
                        toBeCrushed.add((x, y+1))
                        toBeCrushed.add((x, y-1))
            for x, y in toBeCrushed:
                board[x][y] = 0
            return len(toBeCrushed) > 0



        def gravity(board):
            for y in range(n):
                col = []
                for x in range(m-1, -1, -1):
                    if board[x][y] != 0:
                        col.append(board[x][y])    
                i = 0
                for x in range(m-1, -1, -1):
                    if i < len(col):
                        board[x][y] = col[i]
                        i += 1
                    else:
                        board[x][y] = 0
        while crush(board):
            gravity(board)
        
        return board
        
