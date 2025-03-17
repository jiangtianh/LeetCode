class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        

        dp = [[math.inf] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = 0
        for i in range(len(s1) - 1, -1, -1):
            dp[i][-1] = dp[i+1][-1] + ord(s1[i])
        for j in range(len(s2) - 1, -1, -1):
            dp[-1][j] = dp[-1][j+1] + ord(s2[j])
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = min(dp[i][j], dp[i+1][j+1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + ord(s2[j]), dp[i+1][j] + ord(s1[i]))
        return dp[0][0]