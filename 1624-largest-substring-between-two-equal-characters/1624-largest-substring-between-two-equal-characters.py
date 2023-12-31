class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        last = {}

        for i, c in enumerate(s):
            if c in first:
                last[c] = i
            else:
                first[c] = i
        
        res = -1
        for c in first:
            if c in last:
                res = max(res, last[c] - first[c] - 1)

        return res


