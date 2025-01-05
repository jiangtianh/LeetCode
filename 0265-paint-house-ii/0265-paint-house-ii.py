class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])

        @cache
        def f(i, prev):
            if i == n:
                return 0
            res = math.inf
            for j in range(k):
                if j == prev:
                    continue
                res = min(res, costs[i][j] + f(i+1, j))
            return res
        
        return f(0, -1)