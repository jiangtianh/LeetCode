class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = {}
        l = 0
        res = 0

        for r, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            while len(d) > k:
                lc = s[l]
                d[lc] -= 1
                if d[lc] == 0:
                    d.pop(lc)
                l += 1
            res = max(res, r - l + 1)
        return res