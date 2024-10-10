class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)

        stack = []
        for c in path:
            if not c or c == ".":
                continue 
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return '/' + '/'.join(stack)