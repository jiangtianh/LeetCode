class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        def find():
            for x in range(8):
                for y in range(8):
                    if board[x][y] == 'R':
                        return x, y
        def valid(x, y):
            return 0 <= x < 8 and 0 <= y < 8

        x, y = find()
        res = 0
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        for i, j in directions:
            newX, newY = x, y
            while valid(newX, newY) and (board[newX][newY] != 'p' and board[newX][newY] != 'B'):
                newX += i
                newY += j
            
            if valid(newX, newY) and board[newX][newY] == 'p':
                res += 1

        return res