class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        d = {}
        l = 0
        res = 1
        
        for r, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            
            
            most = max(d.values())
            
            while (r - l + 1) - most > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
                
            
            res = max(res, r - l + 1)
            
            
            
            
            
        return res