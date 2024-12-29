class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0:
            return False
        nn = n
        s = {0: "0", 1: "1", 6:"9", 8: "8", 9:"6"}
        res = []
        
        while n > 0:
            d = n % 10
            if d not in s:
                return False
            res.append(s[d])
            n //= 10
        print(res)
        return int(''.join(res)) != nn