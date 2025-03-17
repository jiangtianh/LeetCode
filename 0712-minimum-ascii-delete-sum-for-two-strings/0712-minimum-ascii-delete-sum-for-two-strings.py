class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def f(i, j):
            if i == len(s1) and j == len(s2):
                return 0
            elif i == len(s1):
                return sum([ord(c) for c in s2[j:]])
            elif j == len(s2):
                return sum([ord(c) for c in s1[i:]])
            res = math.inf
            if s1[i] == s2[j]:
                res = min(res, f(i+1, j+1))
            
            res = min(res, f(i+1, j) + ord(s1[i]), f(i, j+1) + ord(s2[j]))
            return res
        return f(0, 0)