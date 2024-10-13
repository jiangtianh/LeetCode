class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a, b = pattern
       
        if a == b:
            c = text.count(a)
            return (c+1) * c // 2

        ac = 0
        bc = text.count(b)
        totalB = bc
        res = 0

        for c in text:
            if c == a:
                res += bc
                ac += 1
                
            if c == b:
                bc -= 1
           
        
        return res + max(ac, totalB)