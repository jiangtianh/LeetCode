class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        self.set = set()
        def f(i):
            if i == len(s):
                return 0
            res = 0
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub not in self.set:
                    self.set.add(sub)
                    res = max(res, 1+f(j+1))
                    self.set.remove(sub)
            
            return res
        
        return f(0)