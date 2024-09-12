class Solution:
    def knightDialer(self, n: int) -> int:
        self.path = {1: [6, 8], 2: [7, 9], 3:[4, 8],5:[], 4:[0, 3, 9], 6:[0, 1, 7], 7:[6, 2], 8:[1, 3], 9:[4, 2], 0:[4, 6]}
        MOD = 10 ** 9 + 7

        @cache
        def f(n, pos):
            if n == 1:
                return 1
            if pos == 5:
                return 0
            res = 0
            for nei in self.path[pos]:
                res += f(n-1, nei)
            return res
        res = 0
        for i in range(10):
            res += f(n, i)
        return res % MOD