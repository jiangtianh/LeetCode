class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def f(i, j):
            if i == len(s1) and j == len(s2):
                return 0
            elif i == len(s1):
                return sum([ord(c) for c in s2[j:]])
            elif j == len(s2):
                return sum([ord(c) for c in s1[i:]])
            res = math.inf
            if s1[i] == s2[j]:
                res = min(res, f(i+1, j+1))
            
            res = min(res, f(i+1, j) + ord(s1[i]), f(i, j+1) + ord(s2[j]))
            return res
        return f(0, 0)

        dp = [[math.inf] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(len(s1)):
            dp[i][-1] = 0
        for j in range(len(s2)):
            dp[-1][j] = 0
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                dp[i][j] = math.inf
                if s1[i] == s2[j]:
                    dp[i][j] = min(dp[i][j], dp[i+1][j+1])
                dp[i][j] = min(dp[i][j], dp[i][j+1] + ord(s2[j]), dp[i+1][j] + ord(s1[i]))
        return dp[0][0]