class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = collections.Counter(s)
        oddCount = 0
        oddC = None
        for c in counter:
            if counter[c] % 2 == 1:
                oddCount += 1
                oddC = c
                if oddCount == 2:
                    return []
            counter[c] //= 2

        res = []
        def f(n, temp):
            if n == 0:
                s = "".join(temp)
                if oddC:
                    s = s + oddC + s[::-1]
                else:
                    s = s + s[::-1]
                res.append(s)
                return 
            for c in counter:
                if counter[c] > 0:
                    counter[c] -= 1
                    f(n-1, temp + [c])
                    counter[c] += 1
        f(len(s) // 2, [])
        return res    
        