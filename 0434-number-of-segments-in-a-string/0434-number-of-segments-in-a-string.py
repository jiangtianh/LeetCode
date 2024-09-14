class Solution:
    def countSegments(self, s: str) -> int:
        cCount = 0
        res = 0

        for c in s:
            if c != " ":
                cCount += 1
            else:
                if cCount:
                    res += 1
                cCount = 0
        if cCount:
            res += 1
        return res