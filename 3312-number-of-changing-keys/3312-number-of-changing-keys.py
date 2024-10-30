class Solution:
    def countKeyChanges(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            c = s[i]
            if c.lower() == s[i-1] or c.upper() == s[i-1]:
                continue
            else:
                res += 1
        return res