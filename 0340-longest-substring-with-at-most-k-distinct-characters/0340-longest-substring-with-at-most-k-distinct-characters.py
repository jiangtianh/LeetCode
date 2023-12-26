class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0 
        l = 0
        d = {}
        
        for r, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            
            while len(d) > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
            res = max(r - l + 1, res)
            
        
        
        return res
            
            
            