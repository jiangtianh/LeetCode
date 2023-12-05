class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        si = 0
        
        for c in t:
            if c == s[si]:
                si += 1
            if si == len(s):
                return True
        
        return False