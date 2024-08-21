class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        a = num
        num = str(num)
        l = 0
        res = 0
        for r in range(k, len(num)+1):
            n = int(num[l:r])
            
            if n != 0 and a % n == 0:
                res += 1
            l += 1
        return res