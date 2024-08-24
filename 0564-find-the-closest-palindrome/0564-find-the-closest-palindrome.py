class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n)-1)

        def f(n):
            l = len(n) // 2
            r = len(n) // 2 
            if len(n) % 2 == 0:
                l -= 1
            res = collections.deque()
            while l >= 0:
                num = n[l]
                if l == r:
                    res.append(num)
                else:
                    res.append(num)
                    res.appendleft(num)
                l -= 1
                r += 1
            return int("".join(res))
        

        res = []
        res.append(f(n))
        if len(n) % 2 == 1:
            firstHalf = n[:len(n) // 2 + 1]
            secondHalf = n[len(n) // 2 + 1:]
        else:
            firstHalf = n[:len(n) // 2]
            secondHalf = n[len(n) // 2:]
        
        res.append(f(str(int(firstHalf) - 1) + secondHalf))
        res.append(f(str(int(firstHalf) + 1) + secondHalf))
        
        res.append(int("9" * (len(n)-1)))
        res.append(int("1" + "0" * (len(n) - 1) + "1"))
        
        print(res)

        diff = math.inf
        result = None

        for num in res:
            if int(n) == num:
                continue 
            d = abs(int(n) - num)
            if d < diff:
                result = num
                diff = d
            elif d == diff:
                result = min(result, num)

        return str(result)