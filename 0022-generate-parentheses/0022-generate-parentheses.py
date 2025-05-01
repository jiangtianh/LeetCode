class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.temp = []

        def f(l, r):
            if l > r or l < 0 or r < 0:
                return 
            elif l == 0 and r == 0:
                self.res.append("".join(self.temp))
                return 

            self.temp.append("(")
            f(l-1, r)
            self.temp.pop()

            self.temp.append(")")
            f(l, r-1)
            self.temp.pop()

        f(n, n)
        return self.res