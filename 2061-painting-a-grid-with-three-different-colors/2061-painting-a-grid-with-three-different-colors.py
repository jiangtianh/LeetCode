class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        possibilities = []
        temp = []
        MOD = 10 ** 9 + 7
        def f(i):
            if i == m:
                possibilities.append(''.join(temp))
                return
            for j in range(3):
                if temp and temp[-1] == str(j):
                    continue
                temp.append(str(j))
                f(i+1)
                temp.pop()
        f(0)

        print(possibilities)
        print(len(possibilities))

        dp = [[0] * len(possibilities) for _ in range(n)]
        for j in range(len(possibilities)):
            dp[0][j] = 1

        @cache
        def noDigitEqual(i, j):
            for idx in range(m):
                if possibilities[i][idx] == possibilities[j][idx]:
                    return False
            return True
        
        for i in range(1, n):
            for j in range(len(possibilities)):
                for z in range(len(possibilities)):
                    if noDigitEqual(j, z):
                        dp[i][j] = (dp[i][j] + dp[i-1][z]) % MOD
        return sum(dp[-1]) % MOD
