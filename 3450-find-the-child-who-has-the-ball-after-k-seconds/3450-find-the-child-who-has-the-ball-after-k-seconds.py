class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        d = 1
        i = 0
        while k > 0:
            i += d
            if i == 0 or i == n-1:
                d *= -1
            k -= 1
        return i