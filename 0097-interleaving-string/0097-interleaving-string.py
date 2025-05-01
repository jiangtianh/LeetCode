class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def f(i, x, y):
            if i == len(s3):
                return True
            elif x > len(s1) or y > len(s2):
                return False
            res = False
            if x < len(s1) and s3[i] == s1[x]:
                res = res or f(i+1, x+1, y)
            if y < len(s2) and s3[i] == s2[y]:
                res = res or f(i+1, x, y+1)
            
            return res

        return f(0, 0, 0)
            