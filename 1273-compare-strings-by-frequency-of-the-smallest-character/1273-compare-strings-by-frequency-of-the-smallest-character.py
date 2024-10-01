class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            smallest = ord('z') + 1
            res = 0
            for c in word:
                n = ord(c)
                if n < smallest:
                    smallest = n
                    res = 1
                elif n == smallest:
                    res += 1
            return res

        w = [f(word) for word in words]
        res = []
        for s in queries: 
            n = f(s)
            c = 0
            for i in w:
                if n < i:
                    c += 1
            res.append(c)
        return res
