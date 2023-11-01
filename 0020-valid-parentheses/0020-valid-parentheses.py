class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            c = s[i]
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if stack and stack[-1] == d[c]:
                    stack.pop()
                    continue 
                else:
                    return False 

        return not stack
