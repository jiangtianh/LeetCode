class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        left = ["0", "1", "6", "8", "9"]
        right = ["0", "1", "9", "8", "6"]

        @cache
        def f(n, finalLength):
            if n == 0:
                return [""]
            if n == 1:
                return ["0","1","8"]
            
            else:
                prev = f(n-2, finalLength)
                
                res = []
                for s in prev:
                    for i in range(len(left)):
                        if left[i] != "0":
                            res.append(left[i] + s + right[i])
                        else:
                            if n != finalLength:
                                res.append(left[i] + s + right[i])
                return res

        return f(n, n)