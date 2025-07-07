class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        num = list([int(c) for c in str(n)])
        
        @cache
        def f(i, strict, good):
            if i == len(num):
                if good:
                    return 1
                else:
                    return 0
            
            res = 0
            bound = num[i] if strict else 10
            for d in [0, 1, 8]:
                if d < bound:
                    res += f(i+1, False, good)
                elif d == bound:
                    res += f(i+1, True, good)
            
            for d in [2, 5, 6, 9]:
                if d < bound:
                    res += f(i+1, False, True)
                elif d == bound:
                    res += f(i+1, True, True)
            
            return res
        return f(0, True, False)
