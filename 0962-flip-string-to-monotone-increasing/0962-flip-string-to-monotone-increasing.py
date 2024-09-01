class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        ones = s.count('1')
        zeros = s.count('0')

        leftZeros = 0
        leftOnes = 0

        res = min(zeros, ones)
        
        for i, c in enumerate(s):
            if c == '1':
                leftOnes += 1
                ones -= 1
            else:
                leftZeros += 1
                zeros -= 1
            res = min(res, leftOnes + zeros)
        return res


