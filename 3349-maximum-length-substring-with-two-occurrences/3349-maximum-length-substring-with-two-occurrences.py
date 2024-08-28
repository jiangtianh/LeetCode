class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        res = 0
        d = collections.defaultdict(int)
        for r, c in enumerate(s):
            d[c] += 1

            while d[c] > 2:
                d[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res