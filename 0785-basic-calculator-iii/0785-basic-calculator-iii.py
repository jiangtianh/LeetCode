class Solution:
    def calculate(self, s: str) -> int:
        def parseNumber(s, i):
            n = []
            while i < len(s) and s[i].isnumeric():
                n.append(s[i])
                i += 1
            return int("".join(n)), i

        def f(s, i):
            stack = []
            prevSign = None

            while i < len(s):
                if s[i] == "(":
                    n, i = f(s, i+1)
                    if prevSign:
                        prevNum = stack.pop()
                        if prevSign == "*":
                            n = prevNum * n
                        else:
                            n = prevNum / n
                            if n < 0:
                                n = ceil(n)
                            else:
                                n = floor(n)
                        prevSign = None
                    stack.append(n)
                elif s[i] == ")":
                    res = stack[0]
                    j = 1
                    while j < len(stack):
                        if stack[j] == "+":
                            res += stack[j+1]
                        else:
                            res -= stack[j+1]
                        j += 2
                    return res, i+1
                elif s[i].isnumeric():
                    n, i = parseNumber(s, i)
                    if prevSign:
                        prevNum = stack.pop()
                        if prevSign == "*":
                            n = prevNum * n
                        else:
                            n = prevNum / n
                            if n < 0:
                                n = ceil(n)
                            else:
                                n = floor(n)
                        prevSign = None
                    stack.append(n)
                elif s[i] == "*" or s[i] == "/":
                    prevSign = s[i]
                    i += 1
                else:
                    stack.append(s[i])
                    i += 1
            return stack[0], i
        res, i = f("(" + s + ")", 0)
        return res