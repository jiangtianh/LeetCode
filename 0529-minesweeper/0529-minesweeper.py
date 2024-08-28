class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])

        allDirections = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        x, y = click
        
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        def hasAdjMine(x, y):
            res = 0
            for i, j in allDirections:
                newX, newY = x + i, y + j
                if check(newX, newY) and board[newX][newY] == "M":
                    res += 1
            return res
        def check(x, y):
            return 0 <= x < m and 0 <= y < n 

        q = collections.deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()
            count = hasAdjMine(x, y)
            if board[x][y] == "B" or board[x][y].isnumeric():
                continue
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for i, j in allDirections:
                    newX ,newY = x + i, y + j
                    if check(newX, newY) and (board[newX][newY] == "E"):
                        q.append((newX, newY))
                       
                    
        
        return board


[["B","B","B","B","B","B","1","E"],
 ["B","1","E","E","E","E","1","M"],
 ["E","E","M","E","E","E","1","1"],
 ["M","E","E","E","E","E","E","E"],
 ["E","E","E","E","E","E","E","E"],
 ["E","E","E","E","E","E","E","E"],
 ["E","E","E","E","E","E","E","E"],
 ["E","E","M","M","E","E","E","E"]]