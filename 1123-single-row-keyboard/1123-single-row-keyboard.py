class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i, c in enumerate(keyboard):
            d[c] = i
        
        pos = 0
        res = 0
        for c in word:
            res += abs(pos - d[c])
            pos = d[c]

        return res