class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        count = 0

        for c in s:
            if c == "(":
                count += 1
            else:
                count -= 1
            
            if count < 0:
                res += 1
                count = 0

        res += count 
        return res