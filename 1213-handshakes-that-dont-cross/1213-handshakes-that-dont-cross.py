class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        @cache
        def f(n):
            if n == 2:
                return 1
            res = 2 * f(n-2)
            
            for i in range(3, n-2, 2):
                left = f(i-1)
                right = f(n - (i+1))
                res += left * right
            return res % (10 ** 9 + 7)
        return f(numPeople)