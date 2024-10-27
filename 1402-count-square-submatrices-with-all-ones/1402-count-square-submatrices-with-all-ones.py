class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * (n+1) for _ in range(m+1)]

        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                if matrix[x][y] == 1:
                    dp[x][y] = min(dp[x+1][y], dp[x][y+1], dp[x+1][y+1]) + 1
        res = 0
        for i in range(m):
            for j in range(n):  
                res += dp[i][j]

        return res