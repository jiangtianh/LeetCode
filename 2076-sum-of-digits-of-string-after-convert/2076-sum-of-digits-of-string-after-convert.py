class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ''
        for c in s:
            temp += str(ord(c) - ord('a') + 1)
        
        res = int(temp)

        for _ in range(k):
            temp = 0

            while res > 0:
                temp += res % 10
                res //= 10
            res = temp

        return res