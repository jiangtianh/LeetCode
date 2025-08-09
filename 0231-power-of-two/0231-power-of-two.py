class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1:
            return True
        
        elif int(n) != n or n == 0:
            return False
        
        return self.isPowerOfTwo(n / 2)