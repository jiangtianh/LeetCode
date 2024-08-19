class Solution:
    def minSteps(self, n: int) -> int:



        @cache
        def f(n):
            if n == 1:
                return 0
            res = math.inf 
            
            for i in range(2, (n // 2) + 1):
                if n % i == 0:
                    res = min(res, f(n//i) + i)
            
            if res == math.inf:
                return n

            return res
            

        return f(n)