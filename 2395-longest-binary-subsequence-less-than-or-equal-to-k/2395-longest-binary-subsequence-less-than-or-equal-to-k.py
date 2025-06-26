class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        num = 0
        digit = 0

        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == "0":
                res += 1
                digit += 1
                
            else:
                if 2 ** digit + num <= k:
                    num += 2 ** digit
                    res += 1
                    digit += 1
        return res