import math
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        
        @cache
        def f(n):
            if n == 0:
                return 0
            
            if n < 0:
                return math.inf
            
            res = math.inf
            for num in nums:
                res = min(res, f(n - num) + 1)
            
            return res

        return f(n)


