class Solution:
    def shortestPalindrome(self, s: str) -> str:
        res = 0
        
        for i in range(1, len(s) + 1):
            if s[:i][::-1] == s[:i]:
                res = i
            
        return s[res:][::-1] + s