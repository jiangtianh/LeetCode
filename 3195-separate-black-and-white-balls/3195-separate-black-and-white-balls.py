class Solution:
    def minimumSteps(self, s: str) -> int:
        
        res = 0

        l = 0 
        r = len(s) - 1

        while l < r:
            while l < r and s[l] == "0":
                l += 1
            while l < r and s[r] == "1":
                r -= 1
        
           
            res += r - l

            l += 1
            r -= 1
        return res