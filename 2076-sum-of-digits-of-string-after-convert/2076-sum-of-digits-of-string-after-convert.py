class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        a = []

        for c in s:
            a.append(str(ord(c) - ord('a') + 1))
        
        num = int(''.join(a))

        for _ in range(k):
            temp = 0
            while num > 0:
                temp += num % 10
                num //= 10
            num = temp
        
        return num