class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = {"0": 0, "1": 0}
        for c in s:
            counter[c] += 1
        
        counter["1"] -= 1

        res = ""
        while counter["1"] > 0:
            res += "1"
            counter["1"] -= 1
        while counter["0"] > 0:
            res += "0"
            counter["0"] -= 1

        return res + "1"