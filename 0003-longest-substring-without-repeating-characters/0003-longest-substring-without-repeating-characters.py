class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = collections.defaultdict(int)
        res = 0
        for i in range(len(s)):
            c = s[i]
            
            d[c] += 1
            
            while d[c] > 1:
                lc = s[l]
                d[lc] -= 1
                l += 1
            
            res = max(res, i - l + 1)
        
        return res
        
            
            
            
            
            
        
        