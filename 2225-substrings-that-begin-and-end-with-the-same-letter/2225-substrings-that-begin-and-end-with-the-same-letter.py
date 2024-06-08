class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = collections.defaultdict(int)
        res = 0
        for c in s:
            res += d[c] 
            d[c] += 1

        return res + len(s)