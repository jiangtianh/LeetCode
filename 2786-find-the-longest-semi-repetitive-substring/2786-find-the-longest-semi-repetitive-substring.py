class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l, r = 0, 0
        samePair = 0
        res = 0
        prevC = None
    

        while r < len(s):
            if s[r] == prevC:
                samePair += 1
            
            while samePair > 1 and l < r:
                if s[l] == s[l+1]:
                    samePair -= 1
                l += 1
            
            res = max(res, r - l + 1)
            prevC = s[r]
            r += 1

        
        return res
