class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.d = {}
        def f(i, M, alice):
            if i == len(piles):
                return 0
            if (i, M, alice) in self.d:
                return self.d[(i, M, alice)]
            total = 0
            res = 0
            if not alice:
                res = math.inf
            for X in range(2*M):
                if i + X >= len(piles):
                    break 
                total += piles[i+X]
                if alice:
                    res = max(res, f(i+X+1, max(M, X+1), False) + total)
                else:
                    res = min(res, f(i+X+1, max(M, X+1), True))
            self.d[(i, M, alice)] = res
            return res

        return f(0, 1, True)

