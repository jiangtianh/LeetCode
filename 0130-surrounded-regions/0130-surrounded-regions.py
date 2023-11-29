class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = collections.deque() 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(board)
        m = len(board[0])
        visited = set()
        
        for i in range(n):
            if board[i][0] == "O":
                visited.add((i, 0))
                q.append((i, 0))
            if board[i][m - 1] == "O" and (i, m-1) not in visited:
                visited.add((i, m-1))
                q.append((i, m-1))
        for i in range(m):
            if board[0][i] == "O" and (0, i) not in visited:
                visited.add((0, i))
                q.append((0, i))
            if board[n-1][i] == "O" and ((n-1, i)) not in visited:
                visited.add((n-1, i))
                q.append((n-1, i))

        print(visited)
        while q:
            x, y = q.popleft() 
            for i, j in directions:
                newX, newY = x + i, y + j
                if newX in range(n) and newY in range(m) and board[newX][newY] == "O" and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    q.append((newX, newY))

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"




