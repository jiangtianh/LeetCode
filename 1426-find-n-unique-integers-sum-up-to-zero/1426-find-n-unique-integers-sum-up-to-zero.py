class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        num = 1
        while n > 1:
            res.append(num)
            res.append(-num)
            num += 1
            n -= 2
        
        if n == 1:
            res.append(0)
        return res