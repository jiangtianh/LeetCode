class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        pairCount = 0
        l = 0
        res = 0
        
        for r in range(1, len(s)):
            if s[r] == s[r-1]:
                pairCount += 1
            
            while pairCount > 1:
                if s[l] == s[l+1]:
                    pairCount -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
        