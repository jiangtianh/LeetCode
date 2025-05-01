class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        res = 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if matrix[i][j] == "1":
                    temp = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
                    res = max(res, temp)
                    dp[i][j] = temp

        return res * res