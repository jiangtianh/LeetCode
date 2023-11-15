class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.temp = []
        
        def f(l, r):
            if r > l or l > n or r > n:
                return 
            if l == r == n:
                self.res.append("".join(self.temp))
                return 
            
            self.temp.append("(")
            f(l + 1, r)
            self.temp.pop()
            
            self.temp.append(")")
            f(l, r + 1)
            self.temp.pop()
            
        f(0, 0)
        return self.res