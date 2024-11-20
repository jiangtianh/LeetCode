class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeroCount = 0
        oneCount = 0
        for c in s:
            if c == "1":
                oneCount += 1
            else:
                zeroCount += 1
        
        res = zeroCount
        leftZero = leftOne = 0

        for i, c in enumerate(s):
            if c == "1":
                res = min(res, leftOne + zeroCount)
                leftOne += 1
                oneCount -= 1
            else:
                res = min(res, leftOne + oneCount)
                leftZero -= 1
                zeroCount -= 1

        return res            
            
            
        return res