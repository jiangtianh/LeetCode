class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        stack = []
        while i < len(path):
            l = i + 1
            r = l
            while r < len(path) and path[r] != "/":
                r += 1
            if r == l or r > len(path):
                i = l
                continue 

            else:
                if path[l:r] == "..":
                    if stack:
                        stack.pop() 
                elif path[l:r] == ".":
                    pass
                else:
                    stack.append(path[l:r])
                i = r

        
        res = "/".join(stack)
        return "/" + res