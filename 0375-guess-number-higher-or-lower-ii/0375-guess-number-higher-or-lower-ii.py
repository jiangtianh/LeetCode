class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        self.d = {}
        def f(l, r):
            if (l,r) in self.d:
                return self.d[(l, r)]
            if l >= r:
                return 0
            elif l == r-1:
                return l
            res = math.inf
            for i in range(l+1, r):
                left = f(l, i-1)
                right = f(i+1, r)

                res = min(res, max(left, right)+i)
            self.d[(l, r)] = res
            return res

        return f(1, n)


