class Solution:
    def sumBase(self, n: int, k: int) -> int:
        num = 0

        while n > 0:
            remainder = n % k
            n //= k
            num = num * 10 + remainder
        res = 0
        while num > 0:
            res += num % 10
            num //= 10
        return res