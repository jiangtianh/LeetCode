class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/")
        print(path)
        li = path.split("/")
        print(li)
        res = []
        
        for s in li:
            if s == "..":
                if res:
                    res.pop() 
            elif s == "." or s == "":
                continue 
            else:
                res.append(s)
        
        return "/" + "/".join(res)
        
        
        