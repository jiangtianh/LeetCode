class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def f(i):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return i
            return f(i-2) + f(i-1) + f(i-3)
        return f(n)
        
        