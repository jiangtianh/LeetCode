class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}   
        deleteDict = {"IX": 2, "IV": 2, "XL": 20, "XC": 20, "CD": 200, "CM": 200}
        res = 0
        for c in s:
            res += d[c]
        
        for c in deleteDict:
            res -= s.count(c) * deleteDict[c]
        return res