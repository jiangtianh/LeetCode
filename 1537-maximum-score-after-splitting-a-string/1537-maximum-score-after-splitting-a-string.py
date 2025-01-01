class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0 if s[0] == "1" else 1
        one = s[1:].count("1")
        res = 0
        for i in range(1, len(s)):
            c = s[i]
            res = max(res, zero + one)
            if c == "0":
                zero += 1
            else:
                one -= 1
            
        return res