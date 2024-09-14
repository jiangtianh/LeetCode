class DisjointSet:
    def __init__(self):
        self.li = [i for i in range(26)]
    
    def find(self, i):
        if self.li[i] == i:
            return i
        res = self.find(self.li[i])
        self.li[i] = res
        return res

    def join(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return 
        
        elif xRoot < yRoot:
            self.li[yRoot] = xRoot
        else:
            self.li[xRoot] = yRoot

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        ds = DisjointSet()
        for i in range(n):
            ds.join(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
        res = []
        for c in baseStr:
            idx = ds.find(ord(c) - ord('a'))
            res.append(chr(idx + ord('a')))
        
        return ''.join(res)
        

