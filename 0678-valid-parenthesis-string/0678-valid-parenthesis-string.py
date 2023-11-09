class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @cache
        def f(i, left):
            if i == len(s):
                if left == 0:
                    return True
                else:
                    return False
            if left < 0:
                return False 

            if s[i] == "(":
                return f(i + 1, left + 1)
            elif s[i] == ")":
                return f(i + 1, left - 1)

            else:
                return f(i + 1, left + 1) or f(i + 1, left - 1) or f(i + 1, left)

        return f(0, 0)

