class Solution:
    def minSwaps(self, s: str) -> int:
        s = [c for c in s]
        r = len(s) - 1
        while r >= 0 and s[r] != "[":
            r -= 1
        
        count = 0
        res = 0
        
        l = 0
        while l < r:
            c = s[l]

            if c == "[":
                count += 1
            else:
                count -= 1

            if count < 0:
                s[l], s[r] = s[r], s[l]
                r -= 1
                res += 1
                count = 1
                while r >= l and s[r] != "[":
                    r -= 1
            l += 1
        
        return res

