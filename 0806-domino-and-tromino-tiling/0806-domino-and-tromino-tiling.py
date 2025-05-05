class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [[0, 0, 0] for _ in range(n+1)]
        
        dp[1][0] = 1
        dp[2][0] = 2
        dp[2][1] = 1
        dp[2][2] = 1

        for i in range(3, n+1):
            count = 0 
            count += dp[i-1][0]
            count += dp[i-2][0]
            count += dp[i-1][1]
            count += dp[i-1][2]
            dp[i][0] = count

            topCount = 0
            topCount += dp[i-2][0]
            topCount += dp[i-1][2]
            dp[i][1] = topCount

            botCount = 0
            botCount += dp[i-2][0]
            botCount += dp[i-1][1]
            dp[i][2] = botCount


        return dp[n][0] % (10 ** 9 + 7)