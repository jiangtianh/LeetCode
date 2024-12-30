class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = [0] * (high + 1)

        dp[zero] += 1
        dp[one] += 1

        for i in range(1, high+1):
            takeZero = dp[i-zero] if i-zero >= 0 else 0
            takeOne = dp[i-one] if i-one >= 0 else 0

            dp[i] = (takeZero + takeOne + dp[i]) % (10 ** 9 + 7)

        return sum(dp[low:high+1]) % (10 ** 9 + 7)

            