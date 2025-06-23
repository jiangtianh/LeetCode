class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def toBaseK(n):
            res = []
            while n > 0:
                res.append(str(n % k))
                n //= k
            return ''.join(reversed(res))

        def checkBaseKPalindrom(n):
            n = toBaseK(n)
            return n == n[::-1]
        
        def generate(length):
            res = []
            halfLength = length // 2
            temp = []
            def f(i):
                if i == halfLength:
                    n = "".join(temp)
                    if length % 2 == 0:
                        res.append(int(n + n[::-1]))
                        return 
                    else:
                        for j in range(0 if i != 0 else 1, 10):
                            res.append(int(n + str(j) + n[::-1]))
                        return
                for j in range(0 if i != 0 else 1, 10):
                    temp.append(str(j))
                    f(i+1)
                    temp.pop()
            f(0)
            return res
        
        
        res = 0
        currentLength = 1
        
        while n > 0:
            currentLengthNum = generate(currentLength)
            currentLength += 1
            for num in currentLengthNum:
                if checkBaseKPalindrom(num):
                    res += num
                    n -= 1
                    if n == 0:
                        break
        return res
    

