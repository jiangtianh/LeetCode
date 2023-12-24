class Solution:
    def minOperations(self, s: str) -> int:
        final1 = ""
        final2 = ""
        for i in range(len(s)):
            if i % 2 == 0:
                final1 += "1"
                final2 += "0"
            else:
                final1 += "0"
                final2 += "1"
        
        res1 = res2 = 0
        
        for i in range(len(s)):
            if s[i] != final1[i]:
                res1 += 1
            else:
                res2 += 1
        
        return min(res1, res2)