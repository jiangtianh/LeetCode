class Solution:
    def nextGreaterElement(self, n: int) -> int:

        if n == 2 ** 31:
            return -1
        n = list(str(n))
        i = len(n) - 2
        while i >= 0 and int(n[i]) >= int(n[i+1]):
            i -= 1
        
        if i == -1:
            return -1

        num = int(n[i])
        
        j = i + 1
        while j < len(n) and int(n[j]) > num:
            j += 1
        j -= 1
        
        n[i], n[j] = n[j], n[i]

        l = i + 1
    
        r = len(n) - 1
        while l < r:
            n[l], n[r] = n[r], n[l]
            l += 1
            r -= 1
        

        res = int("".join(n))

        if res >= 2 ** 31:
            return -1
        return res