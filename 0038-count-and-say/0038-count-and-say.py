class Solution:
    def countAndSay(self, n: int) -> str:
        
        def f(n):
            if n == 1:
                return "1"
            res = []
            prevRes = f(n-1)

            prevC = prevRes[0]
            count = 0

            for c in prevRes:
                if c == prevC:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(prevC)
                    prevC = c
                    count = 1
            res.append(str(count))
            res.append(prevC)
            return "".join(res)
        return f(n)