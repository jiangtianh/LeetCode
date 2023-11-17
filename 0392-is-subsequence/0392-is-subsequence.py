class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        p1 = 0
        
        for i in range(len(t)):
            if t[i] == s[p1]:
                p1 += 1
            
            if p1 == len(s):
                return True 
        
        return False