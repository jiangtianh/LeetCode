class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            if matrix[i][-1] == "1":
                res = 1
            dp[i][-1] = int(matrix[i][-1])
        for i in range(n):
            if matrix[-1][i] == "1":
                res = 1
            dp[-1][i] = int(matrix[-1][i])
        
        for x in range(m-2, -1, -1):
            for y in range(n-2, -1, -1):
                if matrix[x][y] == '1':
                    dp[x][y] = min(dp[x+1][y+1], dp[x+1][y], dp[x][y+1]) + 1
                    res = max(res, dp[x][y], 1)
        return res ** 2