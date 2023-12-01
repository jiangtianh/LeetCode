class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        def check(x, y):
            return x in range(len(board)) and y in range(len(board[0]))
        def count(x, y):
            deadCount, aliveCount = 0, 0
            for i, j in directions:
                newX, newY = x + i, y + j
                if check(newX, newY):
                    if board[newX][newY] == 1:
                        aliveCount += 1
                    else:
                        deadCount += 1
            return aliveCount, deadCount

        turnAlive, turnDead = set(), set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                aliveNeighbor, deadNeighbor = count(i, j)
                if board[i][j] == 0:
                    if aliveNeighbor == 3:
                        turnAlive.add((i, j))
                else:
                    if aliveNeighbor < 2:
                        turnDead.add((i, j))
                    elif aliveNeighbor > 3:
                        turnDead.add((i, j))

        for x, y in turnAlive:
            board[x][y] = 1
        for x, y in turnDead:
            board[x][y] = 0