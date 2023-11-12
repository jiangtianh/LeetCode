class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def f(l, r, temp):
            if l < r or l > n or r > n:
                return 
            if l == r == n:
                self.res.append("".join(temp))
                return 
            
            temp.append("(")
            f(l + 1, r, temp)   
            temp.pop()

            temp.append(")")
            f(l, r + 1, temp)
            temp.pop()

        f(0, 0, [])
        return self.res