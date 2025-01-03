class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l = 0
        res = 0
        d = {}

        for r, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            if r - l + 1 == k:
                if len(d) == k:
                    res += 1
                lc = s[l]
                d[lc] -= 1
                if d[lc] == 0:
                    d.pop(lc)
                l += 1
        return res