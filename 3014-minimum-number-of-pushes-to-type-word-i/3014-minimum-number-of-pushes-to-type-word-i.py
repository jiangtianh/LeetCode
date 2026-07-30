class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        res = 0
        c = 1
        while n > 0:
            
            if n > 8:
                res += c * 8
            else:
                res += c * n
            c += 1
            n -= 8

        return res
