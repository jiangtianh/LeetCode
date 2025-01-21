class Solution:
    def maxProduct(self, s: str) -> int:
        res = set()
        s1 = []
        s2 = []
        def f(i):
            if i == len(s):
                res.add((''.join(s1), ''.join(s2)))
                return 
            
            s1.append(s[i])
            f(i+1)
            s1.pop()

            s2.append(s[i])
            f(i+1)
            s2.pop()

            f(i+1)
        
        f(0)

        result = 0 
        for l, r in res:
            if r == r[::-1] and l == l[::-1]:
                result = max(result, len(l) * len(r))
        return result