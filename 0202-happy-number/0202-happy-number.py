class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        
        
        def f(n):
            res = 0 
            while n > 0:
                i = n % 10 
                res += i ** 2
                n //= 10 
            return res
        
        while n not in seen:
            seen.add(n) 
            n = f(n)
        
            if n == 1:
                return True 
        return False
        
        
        