class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1 = bin(num1)[2:]
        num2 = bin(num2)[2:]
        count = num2.count("1")
        
        if count >= len(num1):
            return int("1" * count, 2)
        else:
            n = len(num1)
            res = ["0"] * n
            for i in range(n):
                if num1[i] == "1":
                    res[i] = "1"
                    count -= 1
                    if count == 0:
                        break
            i = n - 1
            while i >= 0 and count > 0:
                if res[i] == "0":
                    res[i] = "1"
                    count -= 1
                i -= 1

            return int("".join(res), 2)