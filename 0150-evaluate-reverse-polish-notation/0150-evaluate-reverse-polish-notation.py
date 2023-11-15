class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for c in tokens:
            try:
                c = int(c)
                stack.append(c)
            except ValueError:
                a = stack.pop() 
                b = stack.pop() 
                if c == "+":
                    res = a + b
                elif c == "-":
                    res = b - a
                elif c == "*":
                    res = a * b
                elif c == "/":
                    res = b / a
                    if res < 0:
                        res = math.ceil(res)
                    else:
                        res = math.floor(res)
                stack.append(res)
        return stack.pop()
        
        
        