class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        @cache
        def f(n):
            if n == 1:
                return 10

            res = 9
            j = 9
            for i in range(n-1):
                res *= j
                j -= 1
            return res + f(n-1)

        return f(n)