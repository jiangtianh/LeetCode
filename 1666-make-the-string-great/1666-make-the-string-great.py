class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            
            if c.isupper():
                if stack and stack[-1] == c.lower():
                    stack.pop() 
                else:
                    stack.append(c)
            elif c.islower():
                if stack and stack[-1].isupper() and stack[-1].lower() == c:    
                    stack.pop() 
                else:
                    stack.append(c)

        return "".join(stack)