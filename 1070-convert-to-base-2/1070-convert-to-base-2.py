class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        res = []
        while n != 0:
            res.append(str(n%2))
            n = - (n // 2)
        
        res.reverse()
        return ''.join(res)