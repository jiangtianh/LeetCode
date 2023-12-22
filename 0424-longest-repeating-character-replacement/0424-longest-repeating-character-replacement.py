class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = collections.defaultdict(int)
        
        l = r = 0
        res = 0
        currentMax = 1
        
        while r < len(s):
            c = s[r]
            d[c] += 1
            currentMax = max(currentMax, d[c])
            while (r - l + 1) - currentMax > k:
                d[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
            r += 1
            
        return res
        
        
        