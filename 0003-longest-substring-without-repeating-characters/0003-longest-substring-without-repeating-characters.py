class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        l = r = 0

        res = 0
        while r < len(s):
            c = s[r] 
            window[c] = window.get(c, 0) + 1

            while window[c] > 1:
                window[s[l]] -= 1
                l += 1
            
            r += 1
            res = max(res, r - l)

        return res