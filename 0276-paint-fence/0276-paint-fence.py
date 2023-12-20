class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache 
        def f(i):
            if i == 1:
                return k 
            elif i == 2:
                return k * k
            
            return f(i-1) * (k-1) + f(i-2) * (k-1)
        
        return f(n)