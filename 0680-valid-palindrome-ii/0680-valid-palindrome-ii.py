class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def f(l, r, n):
            if n == -1:
                return False 
            
            while l < r:
                if s[l] != s[r]:
                    return f(l+1, r, n-1) or f(l, r-1, n-1)
                l += 1
                r -= 1
            
            return True 
        
        return f(0, len(s) - 1, 1)