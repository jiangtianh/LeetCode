class Solution:
    def reverseBits(self, n: int) -> int:
        res = bin(n)[2:][::-1]
        while len(res) < 32:
            res += "0"
        return int(res, 2)