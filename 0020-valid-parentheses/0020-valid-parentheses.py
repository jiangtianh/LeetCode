class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenMap = {"}": "{", ")":"(", "]": "["}
        
        for c in s:
            if c not in parenMap:
                stack.append(c)
            else:
                if not stack or parenMap[c] != stack[-1]:
                    return False 
                stack.pop() 
        return len(stack) == 0
        
        
        